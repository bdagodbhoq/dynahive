from __future__ import annotations

import json
import http.client
import os
import threading
import time
import urllib.error
import urllib.request
import re
import tempfile
import stat
from pathlib import Path


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode=stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    temporary=None
    try:
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=path.parent,
                                         prefix='.'+path.name+'.',suffix='.tmp',delete=False) as stream:
            temporary=Path(stream.name)
            stream.write(json.dumps(value,indent=2,ensure_ascii=True))
            stream.flush();os.fsync(stream.fileno())
        os.chmod(temporary,mode)
        os.replace(temporary,path)
        if os.name=='posix':
            fd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
            try:os.fsync(fd)
            finally:os.close(fd)
    finally:
        if temporary and temporary.exists():temporary.unlink()


class Journal:
    def __init__(self, path: Path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
        self.lock = threading.Lock()

    def append(self, record: dict) -> None:
        with self.lock, self.path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps({"timestamp": time.time(), **record}, ensure_ascii=True) + "\n")
            stream.flush();os.fsync(stream.fileno())


class APIBlockedError(RuntimeError):
    """Non-retryable provider rejection; callers must stop the batch."""


class APITransportError(RuntimeError):
    pass


def normalized_usage(raw, wire_api='responses'):
    """Keep absent provider usage absent; never invent zero token usage."""
    if not isinstance(raw,dict):return {}
    mapping = {'input_tokens':'prompt_tokens','output_tokens':'completion_tokens','total_tokens':'total_tokens'} if wire_api=='responses' else {
        'prompt_tokens':'prompt_tokens','completion_tokens':'completion_tokens','total_tokens':'total_tokens'}
    result = {dst:raw[src] for src,dst in mapping.items() if type(raw.get(src)) is int and raw[src]>=0}
    details=raw.get('output_tokens_details' if wire_api=='responses' else 'completion_tokens_details',{}) or {}
    if type(details.get('reasoning_tokens')) is int and details['reasoning_tokens']>=0:
        result['reasoning_tokens']=details['reasoning_tokens']
    return result


def parse_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        # Only the first object. Nested recovery turned truncated planner JSON
        # into {"tool","command"} and crashed HoneyGPT trials as Invalid planner.
        start = text.find("{")
        if start < 0:
            raise ValueError("Expected JSON object")
        try:
            value, _ = json.JSONDecoder().raw_decode(text[start:])
        except json.JSONDecodeError as exc:
            raise ValueError("Expected JSON object") from exc
    if not isinstance(value, dict):
        raise ValueError("Expected JSON object")
    return value


class LLMClient:
    """Audited API client; live failures never become offline results."""
    def __init__(self, base_url=None, api_key=None, model=None, timeout=180, offline=False,
                 journal: Path | None = None, max_tokens=8000, wire_api=None, reasoning_effort=None):
        self.base_url = (base_url or os.getenv("DYNHIVE_BASE_URL", "https://api.openai.com/v1")).rstrip("/")
        self.api_key = api_key or os.getenv("DYNHIVE_API_KEY", "")
        self.model = model or os.getenv("DYNHIVE_MODEL", "gpt-6-luna")
        self.timeout, self.offline, self.max_tokens = timeout, offline, max_tokens
        self.wire_api = (wire_api or os.getenv("DYNHIVE_WIRE_API", "responses")).lower()
        self.reasoning_effort = reasoning_effort or os.getenv("DYNHIVE_REASONING_EFFORT", "high")
        self.journal = Journal(journal) if journal else None
        self.calls = []
        self.blocked_reason = None
        self.request_lock = threading.Lock()
        if not offline and not self.api_key:
            raise ValueError("API key required; --offline is integration verification only")

    def request(self, endpoint: str, body=None) -> dict:
        req = urllib.request.Request(self.base_url + endpoint,
            data=json.dumps(body).encode() if body else None,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json",
                     "User-Agent": "DynaHive-reproduction/1.0"})
        timeout = float(self.timeout or 180)
        box = {}

        def _call():
            try:
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    box['raw'] = json.loads(response.read().decode("utf-8"))
            except Exception as exc:
                box['exc'] = exc

        worker = threading.Thread(target=_call, daemon=True)
        worker.start()
        worker.join(timeout + 2)
        if worker.is_alive():
            raise TimeoutError(f'HTTP wall-clock deadline {timeout:.0f}s exceeded for {endpoint}')
        if 'exc' in box:
            raise box['exc']
        if 'raw' not in box:
            raise TimeoutError(f'HTTP produced no body for {endpoint}')
        return box['raw']

    def list_models(self):
        return sorted(item["id"] for item in self.request("/models").get("data", []))

    def complete(self, system, user, fallback=None, task="unspecified", json_output=True):
        # One client owns all agents in a batch: keep provider requests serial.
        with self.request_lock:
            if self.blocked_reason:
                raise APIBlockedError(self.blocked_reason)
            return self._complete(system, user, fallback, task, json_output)

    def complete_messages(self, messages, task='native-engine'):
        """Translate native Chat Completions messages without changing prompts."""
        if self.wire_api != 'responses':
            with self.request_lock:
                if self.blocked_reason:
                    raise APIBlockedError(self.blocked_reason)
                return self._complete('', '', task=task, json_output=False, native_messages=messages)
        instructions, history = [], []
        for message in messages:
            content = message.get('content', '')
            if not isinstance(content, str): content = json.dumps(content)
            if message['role'] == 'system': instructions.append(content)
            else: history.append({'role': message['role'], 'content': content})
        return self.complete('\n'.join(instructions), history, task=task, json_output=False)

    def _record(self, record):
        record = self._redact_secret(record)
        self.calls.append(record)
        if self.journal:
            self.journal.append(record)

    def _redact_secret(self, value):
        """Remove the configured transport credential from persisted diagnostics."""
        if isinstance(value, str):
            return value.replace(self.api_key, '[REDACTED_API_KEY]') if len(self.api_key) >= 8 else value
        if isinstance(value, dict):
            return {key:self._redact_secret(item) for key,item in value.items()}
        if isinstance(value, list):
            return [self._redact_secret(item) for item in value]
        return value

    def _complete(self, system, user, fallback=None, task="unspecified", json_output=True, native_messages=None):
        if self.offline:
            if fallback is None: raise ValueError(f"No offline fixture for {task}")
            value = fallback() if callable(fallback) else fallback
            record = {"task": task, "model": "offline-fixture", "latency_s": 0,
                      "usage": {}, "status": "offline", "output": value}
        else:
            if self.wire_api == "responses":
                body = {"model": self.model, "instructions": system + ('\nReturn a valid JSON object only, without markdown or surrounding prose.' if json_output else ''), "input": user,
                        "max_output_tokens": self.max_tokens, "reasoning": {"effort": self.reasoning_effort},
                        "store": False}
                endpoint = "/responses"
            else:
                messages = native_messages if native_messages is not None else [
                    {'role':'system', 'content':system + ('\nReturn a valid JSON object only.' if json_output else '')},
                    {'role':'user', 'content':user if isinstance(user,str) else json.dumps(user,ensure_ascii=False)}]
                token_field = 'max_tokens' if self.model.startswith('deepseek-') else 'max_completion_tokens'
                body = {"model": self.model, "messages": messages, "temperature": 1,
                        token_field: self.max_tokens}
                if json_output: body['response_format'] = {"type": "json_object"}
                endpoint = "/chat/completions"
            if len(self.api_key) >= 8 and self.api_key in json.dumps(body):
                self._record({'task':task, 'model':self.model, 'status':'input_secret_blocked',
                              'usage':{}, 'error':'Configured API credential found in model input'})
                raise ValueError('Transport credentials must not be included in model input')
            started = time.perf_counter()
            raw = None
            # World-first Honey/Trap calls already pass a JSON fallback. Do not
            # spend ~5 minutes retrying 502s before the SSH loop can start.
            http_retries = 1 if fallback is not None else 7
            for attempt in range(8):
                try:
                    raw = self.request(endpoint, body)
                    if self.wire_api == "responses":
                        refusals = [part.get('refusal') for item in raw.get('output', [])
                                    for part in item.get('content', []) if part.get('type') == 'refusal']
                        if refusals or (raw.get('incomplete_details') or {}).get('reason') == 'content_filter':
                            self.blocked_reason = self._redact_secret(f'{task}: provider refusal: {refusals[0] if refusals else "content_filter"}')
                            self._record({'task': task, 'model': self.model, 'status': 'policy_refusal',
                                          'usage': normalized_usage(raw.get('usage'),self.wire_api),
                                          'provider_usage_raw':raw.get('usage'), 'error': self.blocked_reason})
                            raise APIBlockedError(self.blocked_reason)
                        if raw.get("status") not in {None, "completed"}:
                            raise ValueError(f"Incomplete response: {raw.get('status')}; {raw.get('incomplete_details')}")
                        texts = [part.get("text", "") for item in raw.get("output", [])
                                 if item.get("type") == "message" for part in item.get("content", [])
                                 if part.get("type") == "output_text"]
                        content = "".join(texts)
                        value = parse_json(content) if json_output else content
                        usage = normalized_usage(raw.get('usage'),self.wire_api)
                    else:
                        if not isinstance(raw, dict) or not raw.get('choices'):
                            raise KeyError('choices')
                        choice = raw['choices'][0]
                        refusal = choice['message'].get('refusal')
                        if refusal or choice.get('finish_reason') == 'content_filter':
                            self.blocked_reason = self._redact_secret(f'{task}: provider refusal: {refusal or "content_filter"}')
                            self._record({'task': task, 'model': self.model, 'status': 'policy_refusal',
                                          'usage': normalized_usage(raw.get('usage'),self.wire_api),
                                          'provider_usage_raw':raw.get('usage'), 'error': self.blocked_reason})
                            raise APIBlockedError(self.blocked_reason)
                        content = choice['message'].get("content") or ""
                        if choice.get('finish_reason') not in {None, 'stop'}:
                            raise ValueError(f"Incomplete text response: {choice.get('finish_reason')}")
                        if not content.strip():
                            raise ValueError('Empty model response')
                        value = parse_json(content) if json_output else content
                        usage = normalized_usage(raw.get('usage'),self.wire_api)
                    record = {"task": task, "model": self.model, "response_model": raw.get("model"),
                              "request_id": raw.get("id"), "latency_s": time.perf_counter() - started,
                              "usage": usage, "provider_usage_raw":raw.get('usage'),
                              "usage_complete":all(k in usage for k in ['prompt_tokens','completion_tokens','total_tokens']),
                              "status": "ok", "input": body,
                              "provider_response": raw,
                              "output": value}
                    break
                except urllib.error.HTTPError as exc:
                    detail = self._redact_secret(exc.read().decode("utf-8", errors="replace"))[:1000]
                    if exc.code in {429, 500, 502, 503, 504} and attempt < http_retries:
                        self._record({'task': task, 'model': self.model, 'status': 'retryable_http_error',
                            'attempt': attempt+1, 'http_status': exc.code, 'error': detail, 'usage': {},
                            'latency_s': time.perf_counter()-started})
                        if fallback is not None:
                            delay = min(8, 2 ** (attempt + 1))
                        else:
                            try:
                                delay = min(60, float(exc.headers.get("Retry-After", 3 ** (attempt + 1))))
                            except ValueError:
                                delay = min(60, 3 ** (attempt + 1))
                        time.sleep(delay)
                        continue
                    if fallback is not None:
                        value = fallback() if callable(fallback) else fallback
                        record = {"task": task, "model": self.model, "status": "fallback_after_http",
                                  "http_status": exc.code, "latency_s": time.perf_counter() - started,
                                  "usage": {}, "error": detail, "output": value}
                        break
                    record = {"task": task, "model": self.model, "status": "error", "http_status": exc.code,
                              "latency_s": time.perf_counter() - started, "usage": {}, "error": detail}
                    self._record(record)
                    if (exc.code in {401, 402, 403, 429, 500, 502, 503, 504}
                            or "cyber_policy" in detail or "content policy" in detail.lower()
                            or "service_unavailable" in detail):
                        self.blocked_reason = f"{task}: HTTP {exc.code}: {detail}"
                        raise APIBlockedError(self.blocked_reason) from None
                    raise RuntimeError(f"{task}: HTTP {exc.code}: {detail}") from None
                except (urllib.error.URLError, http.client.RemoteDisconnected, ConnectionResetError,
                        TimeoutError, OSError) as exc:
                    if fallback is not None and attempt < 1:
                        self._record({'task': task, 'model': self.model, 'status': 'transport_retry',
                            'attempt': attempt+1, 'error': str(exc), 'usage': {},
                            'latency_s': time.perf_counter()-started})
                        time.sleep(2)
                        continue
                    if fallback is not None:
                        value = fallback() if callable(fallback) else fallback
                        record = {"task": task, "model": self.model, "status": "fallback_after_transport",
                                  "error": str(exc), "latency_s": time.perf_counter() - started,
                                  "usage": {}, "output": value}
                        break
                    if attempt < 7:
                        self._record({'task': task, 'model': self.model, 'status': 'transport_retry',
                            'attempt': attempt+1, 'error': str(exc), 'usage': {},
                            'latency_s': time.perf_counter()-started})
                        time.sleep(min(60, 3 ** (attempt + 1)))
                        continue
                    self._record({"task": task, "model": self.model, "status": "transport_error", "error": str(exc),
                                  "latency_s": time.perf_counter() - started, "usage": {}, 'input': body})
                    raise APITransportError(f"{task}: {exc}") from None
                except (ValueError, KeyError, IndexError) as exc:
                    retryable = (
                        isinstance(exc, (KeyError, IndexError))
                        or 'choices' in str(exc)
                        or 'Empty model' in str(exc)
                        or '900-second timeout' in str(exc)
                        or 'Incomplete text response' in str(exc)
                        or 'Expected JSON object' in str(exc)
                    )
                    empty = 'Empty model' in str(exc)
                    if retryable and attempt < (1 if empty else 7):
                        self._record({'task': task, 'model': self.model, 'status': 'invalid_output_retry',
                            'attempt': attempt+1, 'error': str(exc), 'usage': {},
                            'latency_s': time.perf_counter()-started, 'provider_response': raw})
                        time.sleep(min(60, 3 ** (attempt + 1)))
                        continue
                    self._record({"task": task, "model": self.model, "status": "invalid_output", "error": str(exc),
                                  "latency_s": time.perf_counter() - started,
                                  "usage":normalized_usage((raw or {}).get('usage'),self.wire_api),
                                  "provider_response": raw})
                    # Empty/truncated completions are per-command failures. Do not
                    # circuit-break the shared worker (one refused cat id_rsa used
                    # to freeze every other honeypot session).
                    if retryable and 'Empty model' not in str(exc):
                        self.blocked_reason = f"{task}: {exc}"
                        raise APIBlockedError(self.blocked_reason) from None
                    raise RuntimeError(f"{task}: {exc}") from None
        self._record(record)
        return value


def load_key(path=None):
    if not path: return os.getenv("DYNHIVE_API_KEY", "")
    raw = Path(path).read_text(encoding="utf-8-sig").strip()
    first = raw.splitlines()[0] if raw else ""
    return first.split("=", 1)[1].strip().strip("\"'") if first.startswith(("OPENAI_API_KEY=", "DYNHIVE_API_KEY=")) else first
