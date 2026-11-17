"""Online DynaHive session: artifact shell + constrained LLM + live adaptation.

Phase B wires TAPAS telemetry and EventDrivenAdapter.live_cycle so Anti-Recon
micro-adjustments can hot-reload the visible surface during an engagement.
"""
from __future__ import annotations

import re
import threading
import time
import uuid

from .anti_fingerprint import default_ar_constraints
from .frame_agents import Coordinator
from .honeypot import World, materialize
from .llm_shell import LLMPrimaryShell
from .runtime import Journal

LEAK_PATTERNS = re.compile(
    r'(honeypot|honey[\s-]?pot|decoy environment|this is a trap|simulated lab|'
    r'reconstructed runtime|PRODUCTION_ARCHIVE_SECRET_MARKER)',
    re.I)

COMMAND_TO_ACTION = {
    'ls': 'list', 'find': 'list',
    'cat': 'read', 'head': 'read', 'tail': 'read', 'less': 'read', 'more': 'read',
    'id': 'probe', 'whoami': 'probe', 'uname': 'probe', 'hostname': 'probe', 'pwd': 'probe',
    'ps': 'probe', 'ss': 'probe', 'netstat': 'probe', 'ip': 'probe', 'env': 'probe',
    'echo': 'probe', 'printf': 'probe', 'cd': 'probe',
    'sudo': 'privilege',
}

# Local World handlers that are complete enough for fingerprinting. Everything
# else, plus shell control / compounds, prefers the defender LLM.
ARTIFACT_SAFE_COMMANDS = {
    'ls', 'cat', 'head', 'tail', 'cd', 'pwd', 'id', 'whoami', 'uname', 'hostname',
    'echo', 'printf', 'env', 'true', 'false', 'clear',
    'ps', 'date', 'uptime', 'who', 'w', 'last', 'sudo', 'stat', 'ss', 'ip',
    'ifconfig', 'netstat', 'grep', 'find', 'which', 'type', 'mount', 'df',
    'free', 'crontab', 'getent', 'basename', 'dirname', 'realpath', 'readlink',
    'test', '[', 'wc', 'sort', 'uniq', 'cut', 'tr', 'awk', 'sed', 'file',
    'md5sum', 'sha256sum', 'sha1sum', 'od', 'history', 'export', 'set', 'unset',
    'chmod', 'chown', 'touch', 'mkdir', 'rm', 'cp', 'mv', 'ln', 'sleep', 'time',
    'groups', 'history', 'which', 'command', 'getent', 'systemctl',
    'journalctl', 'free', 'last', 'dash', 'bash', 'sh', 'monit',
    'ssh', 'scp', 'sftp', 'nc', 'netcat', 'ncat',
}

_SHELL_CONTROL_RE = re.compile(
    r'(^|[\s;|&])(for|while|until|if|case|function|do|done|then|else|elif|fi|esac)([\s;|&]|$)'
)


class LLMResponsePolicy:
    """Generate believable shell output without self-disclosure."""

    def __init__(self, client, journal=None):
        self.client = client
        self.journal = journal
        self.ar_constraints = []

    def set_constraints(self, constraints):
        self.ar_constraints = [str(item) for item in (constraints or []) if str(item).strip()][:12]

    def complete(self, command, context):
        # Response Generation (frame): persona-consistent shell conditioned on
        # Intent Perception / Anti-Recon constraints when available.
        system = (
            'You are GNU bash 5.1 on a real Ubuntu 22.04.4 LTS enterprise host '
            '(edge firewall / ops persona). '
            'Return ONLY raw terminal stdout/stderr text for ONE command line. No markdown. '
            'Never say honeypot, decoy, trap, simulated, reconstructed, lab, or fake. '
            'Never invent production archive secret markers. '
            'You understand bash keywords (for/do/done/if/fi), pipelines, redirections, '
            'and $()/$? expansion. Missing external tools print '
            '"bash: TOOL: command not found". '
            'Keep /etc/passwd, /etc/shadow, /proc/*, /bin/bash sizes, clocks, env, '
            'and uid/gid identity internally consistent with the supplied persona. '
            'The interactive login user is always uid/gid 1000 matching /etc/passwd. '
            'If intent_hint suggests privilege or lateral probing, stay boring and '
            'consistent; do not over-reveal. '
            'Obey Anti-Recon constraints when present. '
            'Do not wrap filesystem listings as JSON.'
        )
        user = {
            'command': command,
            'host': context.get('host'),
            'username': context.get('username'),
            'uid': context.get('uid', 1000),
            'gid': context.get('gid', 1000),
            'cwd': context.get('cwd'),
            'prompt': context.get('prompt'),
            'visible_files': context.get('visible_files', [])[:40],
            'os': context.get('os', 'Ubuntu 22.04.4 LTS'),
            'kernel': context.get('kernel', 'Linux 5.15.0-97-generic'),
            'lab_clock_utc': context.get('lab_clock_utc', 'Sun Oct 13 09:15:01 UTC 2024'),
            'env': context.get('env') or {},
            'recent': context.get('recent', [])[-4:],
            'ar_constraints': context.get('ar_constraints') or self.ar_constraints,
            'intent_hint': context.get('intent_hint'),
            'decision_hint': context.get('decision_hint'),
        }
        try:
            text = self.client.complete(system, user, task='dynahive.live.shell', json_output=False)
        except Exception as exc:
            if self.journal:
                self.journal.append({'event': 'dynahive_llm_fallback_error',
                                     'command': command, 'error': type(exc).__name__})
            token = command.split()[0] if command.split() else 'command'
            if '/' in token:
                token = token.rsplit('/', 1)[-1]
            return f'bash: {token}: command not found\n'
        if not isinstance(text, str):
            text = str(text)
        text = text.strip('\r\n') + '\n'
        return self.sanitize(text)

    def sanitize(self, text):
        if LEAK_PATTERNS.search(text):
            return 'bash: permission denied\n'
        # Drop accidental JSON wrappers that fingerprint reconstructed services.
        stripped = text.strip()
        if stripped.startswith('{') and '"ok"' in stripped:
            return 'bash: permission denied\n'
        if len(text) > 16000:
            return text[:16000] + '\n'
        return text


class DynaHiveLiveSession:
    """Native-frontend compatible session with artifact-first command handling."""

    def __init__(self, spec, host, client=None, adapter=None, journal=None, *,
                 prompt=None, adapt_every=3, ar_threshold=0.5, seed=0,
                 topology=None, honey=None, traps=None, llm_when_preferred=False):
        self.journal = journal
        self.host = host
        self.adapt_every = max(1, int(adapt_every))
        self.ar_threshold = ar_threshold
        self.adapter = adapter
        self.topology = topology
        self.honey = honey
        self.traps = traps
        self.session_id = uuid.uuid4().hex
        self.terminated = False
        self.command_count = 0
        self.trap_triggers = 0
        self.llm_fallbacks = 0
        self.artifact_hits = 0
        self.adapt_cycles = 0
        self.adapt_errors = 0
        self.recent = []
        self.telemetry_events = []
        self.ar_constraints = []
        self.lock = threading.RLock()

        class _NullJournal:
            def append(self, record):
                return None

        self.world = World(spec, journal if journal is not None else _NullJournal())
        credential = self.world.hosts[host]['credential']
        self.username = credential['username']
        # Default prompt tracks the live persona; callers may override with a matching string.
        self.prompt = prompt if prompt is not None else f'{self.username}@{host}:~$ '
        self.world.interact(self.session_id, {'op': 'login', 'host': host, **credential},
                            'virtual-control-login')
        self.policy = LLMResponsePolicy(client, journal) if client is not None else None
        # Route C: LLM-primary shell with world-state + consistency gate.
        self.llm_shell = LLMPrimaryShell(client, self.world, journal) if client is not None else None
        # When True, prefer_llm (sensitive / long-context) uses the defender LLM
        # even if World already returned a stub. Default False keeps RQ1/RQ2 Route B.
        self.llm_when_preferred = bool(llm_when_preferred)
        self.seed = seed
        self.ar_constraints = list(default_ar_constraints())
        if self.policy is not None:
            self.policy.set_constraints(self.ar_constraints)
        if self.llm_shell is not None:
            self.llm_shell.set_constraints(self.ar_constraints)
        if self.adapter is not None and honey is not None and traps is not None:
            if hasattr(self.adapter, 'seed_configuration'):
                hardened = self.adapter.seed_configuration(honey, traps)
                if hardened is not None and topology is not None:
                    # Reload the hardened surface immediately so first commands
                    # already see unique, persona-aligned artifacts.
                    self.reload_spec(hardened, traps, topology)
                    self.honey = hardened
        # Frame PDF agents: Planner(TAPAS) + Environment + Guidance(traps) + Review.
        self.frame = None
        self._last_frame = None
        self._last_output = ''
        self._last_handled = True
        if topology is not None and honey is not None:
            try:
                self.frame = Coordinator(
                    topology=topology,
                    honey=self.honey if self.honey is not None else honey,
                    traps=self.traps if self.traps is not None else (traps or {'hosts': [], 'chains': []}),
                    entry_host=host,
                    client=client,
                    journal=journal,
                    review_every=max(2, self.adapt_every),
                )
                # Sync Guidance traps into session state for adapter/reload.
                self.traps = self.frame.guidance.traps
            except Exception as exc:
                self.frame = None
                if self.journal:
                    self.journal.append({
                        'event': 'frame_controller_init_error',
                        'error': type(exc).__name__ + ': ' + str(exc)[:300],
                    })
        if self.journal:
            self.journal.append({
                'event': 'dynahive_live_session_start',
                'session_id': self.session_id,
                'host': host,
                'username': self.username,
                'adapt_every': self.adapt_every,
                'adapter': bool(adapter),
                'frame_controller': bool(self.frame),
                'phase': 'frame-env-guidance-review',
            })

    def reload_spec(self, honey, traps, topology=None):
        """Hot-reload materialized artifacts while keeping session identity."""
        with self.lock:
            topo = topology or self.topology
            if topo is None:
                raise ValueError('topology required for reload_spec')
            cwd = self.world._session_state(self.session_id, self.host).get('cwd')
            access = set(self.world._state(self.session_id).get('access', set()))
            spec = materialize(honey, traps, topo, seed=self.seed)
            self.world.spec = spec
            self.world.hosts = {h['name']: h for h in spec['hosts']}
            self.honey = honey
            self.traps = traps
            self.topology = topo
            state = self.world._session_state(self.session_id, self.host)
            if cwd:
                state['cwd'] = cwd
            state['access'] |= access
            if self.journal:
                self.journal.append({'event': 'dynahive_spec_reloaded',
                                     'hosts': sorted(self.world.hosts),
                                     'trap_hosts': len(traps.get('hosts') or []),
                                     'trap_chains': len(traps.get('chains') or [])})

    def _command_action(self, command):
        token = command.strip().split(maxsplit=1)[0] if command.strip() else ''
        return COMMAND_TO_ACTION.get(token, 'probe')

    def _record_telemetry(self, command, result, source):
        action = self._command_action(command)
        event = {
            'host': self.host,
            'action': action,
            'command': command,
            'source': source,
            'trap_trigger': bool(result.get('trap_trigger')),
            'session_id': self.session_id,
            'timestamp': time.time(),
        }
        if action == 'read':
            parts = command.strip().split(maxsplit=1)
            if len(parts) > 1:
                event['path'] = parts[1].split()[0].strip('"\'')
        self.telemetry_events.append(event)
        return event

    def telemetry_snapshot(self):
        """TAPAS-compatible typed event list for adaptation."""
        return list(self.telemetry_events)

    def _context(self):
        files = sorted(self.world._host_files(self.host))
        state = self.world._session_state(self.session_id, self.host)
        env = dict(state.get('env') or {})
        return {
            'host': self.host,
            'username': self.username,
            'uid': 1000,
            'gid': 1000,
            'cwd': state.get('cwd'),
            'prompt': self.prompt,
            'visible_files': files,
            'os': self.world.hosts[self.host].get('os', 'Ubuntu 22.04.4 LTS'),
            'kernel': f"Linux {self.host} 5.15.0-97-generic #107-Ubuntu SMP x86_64 GNU/Linux",
            'lab_clock_utc': 'Sun Oct 13 09:15:01 UTC 2024',
            'env': {
                'USER': env.get('USER', self.username),
                'HOME': env.get('HOME', f'/home/{self.username}'),
                'SHELL': env.get('SHELL', '/bin/bash'),
                'PATH': env.get('PATH'),
                'SSH_CONNECTION': env.get('SSH_CONNECTION'),
                'SSH_CLIENT': env.get('SSH_CLIENT'),
                'SSH_TTY': env.get('SSH_TTY'),
                'BASH_VERSION': env.get('BASH_VERSION', '5.1.16(1)-release'),
            },
            'recent': list(self.recent),
            'ar_constraints': list(self.ar_constraints),
            # Lightweight Intent Perception hint for Response Generation.
            'intent_hint': self._intent_hint(),
            'decision_hint': self._decision_hint(),
        }

    def _perceive_intent(self, command):
        """Intent Perception (frame): map one command to TAPAS-compatible stage."""
        action = self._command_action(command)
        text = (command or '').lower()
        # Stage labels aligned with perception.py / TAPAS mapping comments.
        if action == 'privilege' or 'sudo' in text or 'chmod 4755' in text:
            stage, label = 3, 'privilege_escalation'
        elif action == 'lateral' or 'ssh ' in text or 'scp ' in text:
            stage, label = 4, 'lateral_movement'
        elif action == 'objective' or 'archive' in text or 'secret' in text:
            stage, label = 5, 'objective_access'
        elif action in {'list', 'read', 'probe'} and any(
                tok in text for tok in ('nmap', 'masscan', 'ping ', 'ip a', 'ss ', 'netstat')):
            stage, label = 1, 'scanning'
        elif action in {'list', 'read'} and any(
                tok in text for tok in ('passwd', 'shadow', 'id_rsa', 'credential', 'config')):
            stage, label = 2, 'exploitation'
        else:
            stage, label = 2, 'recon'
        return {
            'action': action,
            'stage': stage,
            'label': label,
            'command_preview': (command or '')[:160],
        }

    def _decide_strategy(self, intent):
        """Decision Engine (frame): choose a response strategy from intent + AR state."""
        label = (intent or {}).get('label') or 'recon'
        if label in {'privilege_escalation', 'lateral_movement'}:
            strategy = 'tighten_anti_recon'
            prefer_llm = True
        elif label == 'objective_access':
            strategy = 'serve_lure_consistently'
            prefer_llm = False
        elif label == 'scanning':
            strategy = 'hold_boring_surface'
            prefer_llm = False
        else:
            strategy = 'persona_consistent_shell'
            prefer_llm = False
        if self.ar_constraints and any('risk' in c.lower() or 'inconsist' in c.lower()
                                       for c in self.ar_constraints):
            strategy = 'tighten_anti_recon'
            prefer_llm = True
        return {
            'strategy': strategy,
            'prefer_llm': prefer_llm,
            'force_adapt': label in {'privilege_escalation', 'lateral_movement', 'objective_access'},
        }

    def _intent_hint(self):
        if not self.telemetry_events:
            return 'recon'
        last = self.telemetry_events[-1]
        return last.get('intent_label') or last.get('action') or 'recon'

    def _decision_hint(self):
        if getattr(self, '_last_decision', None):
            return self._last_decision.get('strategy') or 'hold_persona'
        if self.adapt_cycles <= 0:
            return 'hold_persona'
        return 'anti_recon_adjusted' if self.ar_constraints else 'hold_persona'

    @staticmethod
    def _mask_quoted(text):
        """Replace quoted spans with spaces so | inside format strings is ignored."""
        out, quote = [], None
        for ch in text or '':
            if quote:
                out.append(' ')
                if ch == quote:
                    quote = None
                continue
            if ch in {'"', "'"}:
                quote = ch
                out.append(' ')
                continue
            out.append(ch)
        return ''.join(out)

    def _has_shell_control(self, command):
        """True for bash keywords / substitutions that must not be semicolon-split."""
        text = (command or '').strip()
        if not text:
            return False
        scan = self._mask_quoted(text)
        if '$( ' in scan or '$(' in scan or '`' in scan:
            return True
        return bool(_SHELL_CONTROL_RE.search(scan))

    def _split_shell_chain(self, command):
        """Split on ';', '&&', '||' outside quotes. Keep single '|' inside a chunk."""
        ops_chunks = []
        quote = None
        buf = []
        pending_op = ';'
        i = 0
        text = command or ''
        while i < len(text):
            ch = text[i]
            if quote:
                buf.append(ch)
                if ch == quote:
                    quote = None
                i += 1
                continue
            if ch in {'"', "'"}:
                quote = ch
                buf.append(ch)
                i += 1
                continue
            if ch == '&' and i + 1 < len(text) and text[i + 1] == '&':
                ops_chunks.append((pending_op, ''.join(buf).strip()))
                buf = []
                pending_op = '&&'
                i += 2
                continue
            if ch == '|' and i + 1 < len(text) and text[i + 1] == '|':
                ops_chunks.append((pending_op, ''.join(buf).strip()))
                buf = []
                pending_op = '||'
                i += 2
                continue
            if ch == ';':
                ops_chunks.append((pending_op, ''.join(buf).strip()))
                buf = []
                pending_op = ';'
                i += 1
                continue
            buf.append(ch)
            i += 1
        ops_chunks.append((pending_op, ''.join(buf).strip()))
        return [(op, chunk) for op, chunk in ops_chunks if chunk]

    @staticmethod
    def _looks_failed(output, result=None):
        text = (output or '').lower()
        if result and result.get('handled') is False and not (output or '').strip():
            return True
        markers = (
            'command not found', 'no such file', 'permission denied', 'cannot access',
            'not allowed', 'syntax error', 'invalid time',
        )
        return any(m in text for m in markers)

    def _should_prefer_llm(self, command):
        """Prefer defender LLM only for keywords/substitutions or uncovered tools.

        Simple ';' / '|' / '&&' / '||' chains of artifact-safe commands stay on
        World cache — sending them wholesale to the LLM caused false
        'command not found' tells in RQ1 smokes. Simple for-loops are expanded
        by World and must also stay on cache.
        """
        if self.policy is None:
            return False
        text = (command or '').strip()
        if not text:
            return False
        # World expands simple for-loops; keep them off the LLM path.
        if re.match(r'^\s*for\s+\w+\s+in\s+.+\s*;\s*do\s+.+\s*;\s*done\s*$', text, re.S):
            return False
        if self._has_shell_control(text):
            # while/if/case still need LLM; for already handled above.
            return True
        # If every atom is artifact-safe, keep cache even with pipes/chains.
        if self.frame is not None:
            route = self.frame.router.route(text)
            return bool(route.get('prefer_llm'))
        token = text.split(maxsplit=1)[0]
        if '/' in token:
            token = token.rsplit('/', 1)[-1]
        return token not in ARTIFACT_SAFE_COMMANDS

    def _maybe_adapt(self, force=False):
        if self.adapter is None:
            return
        risk_force = False
        # Force early when recent commands look like privilege/lateral probing.
        if self.telemetry_events:
            last = self.telemetry_events[-1]
            if last.get('action') in {'privilege', 'lateral', 'objective'}:
                risk_force = True
        if not force and not risk_force and self.command_count % self.adapt_every != 0:
            return
        event_id = f'live-{self.session_id}-{self.command_count}'
        events = self.telemetry_snapshot()
        try:
            if hasattr(self.adapter, 'live_cycle'):
                result = self.adapter.live_cycle(event_id, events)
            else:
                result = self.adapter.ingest(event_id, events)
            self.adapt_cycles += 1
            constraints = result.get('constraints') or result.get('audit', {}).get('feedback') or []
            if constraints:
                self.ar_constraints = [str(item) for item in constraints if str(item).strip()][:12]
                if self.policy is not None:
                    self.policy.set_constraints(self.ar_constraints)
            honey = result.get('honey')
            traps = result.get('traps')
            if honey is None and self.adapter.state.get('current_configuration'):
                honey = self.adapter.state['current_configuration'].get('honey')
                traps = self.adapter.state['current_configuration'].get('traps')
            if result.get('changed') and honey is not None and traps is not None and self.topology is not None:
                self.reload_spec(honey, traps, self.topology)
            if self.journal:
                self.journal.append({
                    'event': 'dynahive_adapt_ingest',
                    'event_id': event_id,
                    'cycles': self.adapter.state.get('cycles'),
                    'adapt_cycles': self.adapt_cycles,
                    'risk_score': result.get('risk_score'),
                    'changed': bool(result.get('changed')),
                    'memory_mode': result.get('memory_mode'),
                    'adaptation_kind': result.get('adaptation_kind'),
                    'constraints': self.ar_constraints[:6],
                })
        except Exception as exc:
            self.adapt_errors += 1
            if self.journal:
                self.journal.append({'event': 'dynahive_adapt_error',
                                     'error': type(exc).__name__ + ': ' + str(exc)[:300],
                                     'adapt_errors': self.adapt_errors})

    def _respond_one(self, command):
        active = command
        # Frame agents: Planner(TAPAS) → Environment / Guidance(traps) / Review.
        # ResponseRouter (cache vs LLM) is separate from Guidance.
        frame_step = None
        if self.frame is not None:
            frame_step = self.frame.step(
                command, self.telemetry_events,
                last_output=self._last_output, last_handled=self._last_handled)
            self._last_frame = frame_step
            review = frame_step.get('review') or {}
            if review.get('stealth_constraints'):
                self.ar_constraints = list(review.get('stealth_constraints'))[:12]
                if self.policy is not None:
                    self.policy.set_constraints(self.ar_constraints)
                if self.llm_shell is not None:
                    self.llm_shell.set_constraints(self.ar_constraints)
            prefer_llm = bool(frame_step.get('prefer_llm'))
            guidance = frame_step.get('guidance') or {}
            style_hints = list(frame_step.get('style_hints') or [])
        else:
            intent = self._perceive_intent(command)
            decision = self._decide_strategy(intent)
            self._last_decision = decision
            prefer_llm = bool(decision.get('prefer_llm')) or self._should_prefer_llm(command)
            guidance = {}
            style_hints = []
            intent_label = intent.get('label')
            intent_stage = intent.get('stage')
            decision_strategy = decision.get('strategy')

        if frame_step is not None:
            prefer_llm = prefer_llm or self._should_prefer_llm(command)
            planner = frame_step.get('planner')
            intent_label = getattr(planner, 'last_stage', None)
            intent_stage = getattr(planner, 'last_stage', None)
            decision_strategy = (guidance.get('reason') if isinstance(guidance, dict) else None)

        context = self._context()
        context['intent_hint'] = intent_label
        context['decision_hint'] = decision_strategy
        if style_hints:
            context['ar_constraints'] = list(dict.fromkeys(
                list(context.get('ar_constraints') or []) + style_hints))[:12]
        # Route B: VFS/World always first. LLM only when World cannot handle the atom.
        # Never skip World just because the line contains `for`/`echo` — that
        # produced a canned `bash: command not found` tell used as HRR evidence.
        result = self.world.execute_command(self.session_id, self.host, command)
        world_ok = bool(result.get('handled'))
        prefer_overrides = bool(
            getattr(self, 'llm_when_preferred', False) and prefer_llm and self.llm_shell is not None)
        if world_ok and not prefer_overrides:
            output = result['output']
            source = 'vfs' if getattr(self.world, 'vfs', None) else 'artifact'
            self.artifact_hits += 1
            if result.get('trap_trigger'):
                self.trap_triggers += 1
        elif self.llm_shell is not None and (prefer_llm or not world_ok):
            shell = self.llm_shell.complete(
                self.session_id, self.host, command,
                recent=self.recent,
                style_hints=style_hints,
            )
            output = shell.get('output') or ''
            source = shell.get('source') or 'llm_fallback'
            result = {
                'handled': True,
                'output': output,
                'trap_trigger': bool(shell.get('trap_trigger')),
            }
            self.llm_fallbacks += 1
            if source.startswith('world') or source == 'vfs':
                self.artifact_hits += 1
        elif prefer_llm and self.policy is not None:
            source = 'llm_preferred'
            result = {'handled': False, 'output': '', 'trap_trigger': False,
                      'unhandled_command': command}
            output = self.policy.complete(command, context)
            self.llm_fallbacks += 1
        else:
            source = 'cache' if frame_step is not None else 'artifact'
            if result['handled']:
                output = result['output']
                self.artifact_hits += 1
                if result.get('trap_trigger'):
                    self.trap_triggers += 1
            else:
                source = 'llm_fallback'
                active = result.get('unhandled_command') or command
                if self.policy is None:
                    token = active.split()[0] if active.split() else 'command'
                    if '/' in token:
                        token = token.rsplit('/', 1)[-1]
                    output = f"bash: {token}: command not found\n"
                else:
                    output = self.policy.complete(active, context)
                    self.llm_fallbacks += 1
        if LEAK_PATTERNS.search(output):
            output = 'bash: permission denied\n'
        self._record_telemetry(active, result, source)
        self._last_output = output
        self._last_handled = bool(result.get('handled', True))
        if self.telemetry_events:
            self.telemetry_events[-1]['intent_label'] = intent_label
            self.telemetry_events[-1]['intent_stage'] = intent_stage
            self.telemetry_events[-1]['decision_strategy'] = decision_strategy
            if isinstance(guidance, dict):
                self.telemetry_events[-1]['trap_next_path'] = guidance.get('next_path')
                self.telemetry_events[-1]['trap_action'] = guidance.get('action')
        if frame_step is None:
            if self._last_decision and self._last_decision.get('force_adapt'):
                self._maybe_adapt(force=True)
        elif intent_stage in {3, 4, 5}:
            self._maybe_adapt(force=True)
        return output, source, result

    def respond(self, command):
        with self.lock:
            if self.terminated:
                raise RuntimeError('DynaHive live session closed')
            if not isinstance(command, str) or not command.strip() or '\n' in command or '\r' in command:
                raise ValueError('Expected one bounded terminal input line')
            started = time.time()
            # Never semicolon-split shell keywords / substitutions.
            # Honour && / || short-circuit (do NOT rewrite both to ';' — that
            # made `ss || netstat` emit both branches and fingerprint the shell).
            if self._has_shell_control(command):
                chain = [(';', command.strip())]
            else:
                chain = self._split_shell_chain(command)
            pieces = []
            source = 'artifact'
            trap = False
            last_failed = False
            for idx, (op, chunk) in enumerate(chain):
                if idx > 0:
                    if op == '&&' and last_failed:
                        continue
                    if op == '||' and not last_failed:
                        continue
                piece, src, result = self._respond_one(chunk)
                pieces.append(piece)
                failed = self._looks_failed(piece, result)
                last_failed = failed
                if src in {'llm_fallback', 'llm_preferred', 'cache'}:
                    if source in {'artifact', 'cache'} and src.startswith('llm'):
                        source = src
                    elif source != src and src.startswith('llm'):
                        source = 'mixed'
                trap = trap or bool(result.get('trap_trigger'))
            output = ''.join(pieces)
            result = {'trap_trigger': trap}
            self.command_count += 1
            self.recent.append({'command': command, 'source': source,
                                'output_preview': output[:240]})
            if self.journal:
                self.journal.append({
                    'event': 'dynahive_live_command',
                    'session_id': self.session_id,
                    'command': command,
                    'source': source,
                    'trap_trigger': trap if len(chain) > 1 else bool(result.get('trap_trigger')),
                    'latency_ms': (time.time() - started) * 1000,
                    'command_count': self.command_count,
                    'action': self._command_action(command),
                    'intent_label': (self.telemetry_events[-1].get('intent_label')
                                     if self.telemetry_events else None),
                    'decision_strategy': (
                        ((self._last_frame or {}).get('guidance') or {}).get('reason')
                        if self._last_frame else
                        (getattr(self, '_last_decision', {}) or {}).get('strategy')
                    ),
                })
                # Adaptive Control Loop audit trail: one defense round per attacker command.
                self.journal.append({
                    'event': 'defense_round',
                    'session_id': self.session_id,
                    'round': self.command_count,
                    'attack_command': command,
                    'defense_source': source,
                    'defense_output_preview': output[:500],
                    'intent': (self.telemetry_events[-1].get('intent_label')
                               if self.telemetry_events else None),
                    'decision': (getattr(self, '_last_decision', {}) or {}).get('strategy'),
                    'ar_constraints': self.ar_constraints[:6],
                    'adapt_cycles': self.adapt_cycles,
                })
            self._maybe_adapt()
            return output

    def close(self):
        with self.lock:
            if self.terminated:
                return
            self.terminated = True
            self.world.sessions.pop(self.session_id, None)
            if self.journal:
                self.journal.append({
                    'event': 'dynahive_live_session_close',
                    'session_id': self.session_id,
                    'command_count': self.command_count,
                    'artifact_hits': self.artifact_hits,
                    'llm_fallbacks': self.llm_fallbacks,
                    'trap_triggers': self.trap_triggers,
                    'adapt_cycles': self.adapt_cycles,
                    'adapt_errors': self.adapt_errors,
                    'telemetry_events': len(self.telemetry_events),
                })
