"""Paper Algorithm 1: bounded goal-directed search for a feasible trap chain."""
from __future__ import annotations

import json
from pathlib import PurePosixPath

from . import prompts

K_DEFAULT = 6
B_DEFAULT = 3


def host_files(honey: dict) -> dict:
    out = {}
    for host in honey.get("hosts") or []:
        files = []
        for port in host.get("ports") or []:
            for artifact in port.get("files") or []:
                if artifact.get("path"):
                    files.append(artifact["path"])
        out[host["name"]] = list(dict.fromkeys(files))
    return out


def _other_readable(artifact: dict, identity: str) -> bool:
    meta = artifact.get("metadata") or {}
    owner = str(meta.get("owner") or artifact.get("owner") or "")
    mode = str(meta.get("mode") or artifact.get("mode") or "0644").replace("o", "")
    digits = "".join(ch for ch in mode if ch.isdigit())
    other = int(digits[-1]) if digits else 4
    return owner == identity or other >= 4


def readable_files(honey: dict, identities: dict | None = None) -> dict:
    out = {}
    for host in honey.get("hosts") or []:
        ident = (identities or {}).get(host["name"], "ops")
        files = []
        for port in host.get("ports") or []:
            for artifact in port.get("files") or []:
                path = artifact.get("path")
                if path and _other_readable(artifact, ident):
                    files.append(path)
        out[host["name"]] = list(dict.fromkeys(files))
    return out


def prepare_context(honey, observations, objective, entry_host):
    files = host_files(honey)
    identities = {}
    for host in honey.get("hosts") or []:
        identities[host["name"]] = (
            (host.get("credential") or {}).get("username")
            or {"bastion": "ops", "application": "deploy", "fileserver": "backup"}.get(host.get("role"), "ops")
        )
    readable = readable_files(honey, identities)
    facts = {
        "hosts": list(files),
        "files": files,
        "readable": readable,
        "identities": identities,
        "entry": entry_host,
        "exposed": [o.get("path") for o in (observations or []) if o.get("path")],
    }
    constraints = [
        "Do not invent hosts or paths absent from facts.files.",
        "Do not contradict exposed history.",
    ]
    goal = objective or "Obtain operational archive material reachable from the entry host."
    return facts, constraints, goal


def _file_rank(path: str, host: str, archive: str) -> int:
    text = (path or "").lower()
    score = 10
    if host == archive:
        score -= 5
    if any(token in text for token in ("archive", "backup", "credential", "ticket", "maintenance", "staging")):
        score -= 4
    if text.endswith("hostname") or text.endswith("os-release") or text.endswith("passwd"):
        score += 6
    return score


def _ranked_files(facts, host):
    archive = facts["hosts"][-1] if facts.get("hosts") else host
    files = list(facts.get("readable", {}).get(host) or facts["files"].get(host) or [])
    files.sort(key=lambda path: _file_rank(path, host, archive))
    return files


def greedy_archive_chain(facts):
    chain = []
    hosts = facts.get("hosts") or []
    for host in hosts:
        files = _ranked_files(facts, host)
        if not files:
            return []
        path_name = files[0]
        chain.append({
            "clue": path_name,
            "action": f"cat {path_name}",
            "result": "operational record or archive pointer",
            "host": host,
            "path": path_name,
            "preconditions": [f"{host}:{path_name} exists"],
        })
    return chain


def entry_paths(facts):
    entry = facts["entry"]
    files = _ranked_files(facts, entry)
    if not files:
        return [[]]
    first = files[0]
    return [[{
        "clue": first,
        "action": f"cat {first}",
        "result": "file content readable",
        "host": entry,
        "path": first,
        "preconditions": [f"identity can read {first}"],
    }]]


def _step_key(step):
    return (step.get("host"), step.get("path"), step.get("action"))


def expand_with_rewards(client, path, objective, facts, constraints, b=B_DEFAULT):
    used = {_step_key(s) for s in path}
    fallback = []
    visited = [s.get("host") for s in path]
    hosts = [h for h in facts["hosts"] if h not in visited] + [h for h in facts["hosts"] if h in visited]
    for host in hosts:
        for path_name in _ranked_files(facts, host):
            step = {
                "clue": path_name,
                "action": f"cat {path_name}",
                "result": "operational note or credential pointer",
                "host": host,
                "path": path_name,
                "preconditions": [f"{host}:{path_name} exists"],
            }
            if _step_key(step) in used:
                continue
            fallback.append(step)
            if len(fallback) >= b:
                break
        if len(fallback) >= b:
            break
    payload = {
        "G": objective,
        "F": facts,
        "Q": constraints,
        "current_path": path,
        "b": b,
    }
    if client is None:
        return fallback
    result = client.complete(
        prompts.guidance_expand(),
        json.dumps(payload),
        {"candidates": fallback},
        task="guidance.expand",
    )
    candidates = result.get("candidates") if isinstance(result, dict) else None
    if not isinstance(candidates, list):
        return fallback
    cleaned = []
    known = {h: set(facts["files"].get(h) or []) for h in facts["hosts"]}
    for item in candidates[:b]:
        if not isinstance(item, dict):
            continue
        host = item.get("host") or facts["entry"]
        path_name = item.get("path") or item.get("clue")
        if host not in known:
            continue
        if path_name and path_name not in known[host]:
            continue
        item.setdefault("action", f"cat {path_name}")
        item.setdefault("result", "readable")
        item["host"] = host
        item["path"] = path_name
        if _step_key(item) in used:
            continue
        cleaned.append(item)
    return cleaned or fallback


def assess_progress(client, goal, visible_prefix):
    payload = {"g": goal, "W": visible_prefix}
    fallback = {"progress": bool(visible_prefix), "reason": "prefix-nonempty"}
    if client is None:
        return True, fallback["reason"]
    result = client.complete(
        prompts.guidance_assess(),
        json.dumps(payload),
        fallback,
        task="guidance.assess",
    )
    if not isinstance(result, dict):
        return True, "assessor-fallback"
    return bool(result.get("progress")), str(result.get("reason") or "")


def feasible_whole_chain(path, facts, observations=None):
    """Deterministic FeasibleWholeChain. No LLM."""
    errors = []
    if not path:
        return False, [{"constraint": "empty_path"}]
    files = facts["files"]
    exposed = set(facts.get("exposed") or [])
    for i, step in enumerate(path):
        host = step.get("host")
        path_name = step.get("path")
        if host not in files:
            errors.append({"step": i, "constraint": "host_exists", "host": host})
            continue
        if path_name and path_name not in files[host]:
            errors.append({"step": i, "constraint": "clue_exists", "host": host, "path": path_name})
        readable = (facts.get("readable") or {}).get(host) or files.get(host) or []
        if path_name and path_name not in readable:
            errors.append({"step": i, "constraint": "readable_by_identity", "host": host, "path": path_name,
                           "identity": (facts.get("identities") or {}).get(host)})
        if path_name and ".." in PurePosixPath(str(path_name)).parts:
            errors.append({"step": i, "constraint": "unsafe_path", "path": path_name})
        if i > 0 and path[i - 1].get("host") != host:
            # Cross-host hop is allowed only if both hosts exist in facts.
            if path[i - 1].get("host") not in files:
                errors.append({"step": i, "constraint": "reachability", "from": path[i - 1].get("host"), "to": host})
        if observations and path_name in exposed:
            # Exposed facts may be reused; they must not be contradicted.
            pass
    return (not errors), errors


def select_chain(client, candidates, objective, facts):
    if not candidates:
        return None
    fallback = {"selected": 0, "reason": "first-feasible"}
    if client is None or len(candidates) == 1:
        return candidates[0]
    result = client.complete(
        prompts.guidance_select(),
        json.dumps({"G": objective, "F": facts, "chains": candidates}),
        fallback,
        task="guidance.select",
    )
    try:
        idx = int(result.get("selected", 0))
    except Exception:
        idx = 0
    if idx < 0 or idx >= len(candidates):
        idx = 0
    return candidates[idx]


def search(honey, observations, objective, entry_host, client=None, k=K_DEFAULT, b=B_DEFAULT, budget=None):
    """Algorithm 1. Returns {chain, traps, diagnostics, source}."""
    import os
    facts, constraints, goal = prepare_context(honey, observations, objective, entry_host)
    queue = list(entry_paths(facts))
    accepted = []
    diagnostics = []
    seen = set()
    if budget is None:
        budget = int(os.environ.get("DYNHIVE_GUIDANCE_BUDGET") or 24)
    while queue and budget > 0:
        budget -= 1
        path = queue.pop(0)
        sig = tuple(_step_key(s) for s in path)
        if sig in seen:
            continue
        seen.add(sig)
        archive = facts["hosts"][-1] if facts["hosts"] else entry_host
        reaches = bool(path) and path[-1].get("host") == archive
        if reaches:
            ok, errors = feasible_whole_chain(path, facts, observations)
            if ok:
                accepted.append(path)
            else:
                diagnostics.append({"kind": "chain_failure", "errors": errors})
            continue
        if len(path) >= k:
            diagnostics.append({"kind": "depth_limit", "depth": len(path)})
            continue
        for nxt in expand_with_rewards(client, path, goal, facts, constraints, b=b):
            extended = path + [nxt]
            visible = [{"clue": s.get("clue"), "result": s.get("result"), "host": s.get("host")} for s in extended]
            progress, reason = assess_progress(client, goal, visible)
            archive = facts["hosts"][-1] if facts["hosts"] else entry_host
            closer = (facts["hosts"].index(nxt.get("host")) if nxt.get("host") in facts["hosts"] else -1) > (
                facts["hosts"].index(path[-1].get("host")) if path and path[-1].get("host") in facts["hosts"] else -1
            )
            if progress or (closer and nxt.get("host") == archive):
                if not progress:
                    diagnostics.append({"kind": "assess_overruled_goal_gradient", "reason": reason})
                queue.append(extended)
            else:
                diagnostics.append({"kind": "rejected_prefix", "reason": reason, "path": extended})
    if not accepted:
        greedy = greedy_archive_chain(facts)
        ok, errors = feasible_whole_chain(greedy, facts, observations) if greedy else (False, [])
        if ok:
            diagnostics.append({"kind": "search_recovery_greedy", "note": "bounded search missed a feasible archive path"})
            accepted.append(greedy)
        else:
            return {
                "chain": None,
                "traps": {"hosts": [], "chains": []},
                "diagnostics": diagnostics or [{"kind": "no_feasible_path", "K": k, "b": b, "greedy_errors": errors}],
                "source": "algorithm1",
            }
    chosen = select_chain(client, accepted, goal, facts)
    traps = _as_traps(chosen, facts, entry_host)
    return {"chain": chosen, "traps": traps, "diagnostics": diagnostics, "source": "algorithm1"}


def _as_traps(chain, facts, entry_host):
    hosts_out = []
    for host, files in facts["files"].items():
        loop = [s["path"] for s in chain if s.get("host") == host and s.get("path")]
        if len(set(loop)) >= 2:
            if loop[0] != loop[-1]:
                loop = loop + [loop[0]]
            hosts_out.append({"name": host, "host_loops": [loop]})
        elif files:
            loop = files[:3]
            if len(set(loop)) >= 2:
                if loop[0] != loop[-1]:
                    loop = loop + [loop[0]]
                hosts_out.append({"name": host, "host_loops": [loop]})
            else:
                hosts_out.append({"name": host, "host_loops": []})
        else:
            hosts_out.append({"name": host, "host_loops": []})
    steps = [{"host": s.get("host"), "tier": "low" if i == 0 else "mid"} for i, s in enumerate(chain)]
    hosts_in_chain = [s.get("host") for s in chain]
    if len(set(hosts_in_chain)) >= 2 and steps[0]["host"] != steps[-1]["host"]:
        steps = steps + [dict(steps[0])]
    chains = []
    if len({s["host"] for s in steps}) >= 2:
        chains.append({"name": "ops-credential-loop", "steps": steps})
    return {"hosts": hosts_out, "chains": chains}
