"""Review Agent required checks, localized repair, budget R (paper §Review)."""
from __future__ import annotations

import json

from . import prompts
from .anti_fingerprint import default_ar_constraints, harden_honey_surface, resolve_directory_file_conflicts
from .environment_normalize import SAFE_MTIME, normalize_environment
from .guidance_search import host_files

REQUIRED_KINDS = {
    "unknown_host", "duplicate_host", "role_mismatch", "port_count", "duplicate_port",
    "fingerprint_label", "lab_clock_mtime", "missing_clue", "open_loop", "short_chain",
    "chain_host_missing", "exposed_rewrite",
}


R_DEFAULT = 2


def check_consistency(honey, topology):
    blocking = []
    names = {h["name"] for h in topology.get("hosts") or []}
    roles = {h["name"]: h.get("role") for h in topology.get("hosts") or []}
    seen = set()
    for host in honey.get("hosts") or []:
        n = host.get("name")
        if n not in names:
            blocking.append({"kind": "unknown_host", "evidence": n, "repair": "drop or rename host", "host": n, "blocking": True})
        if n in seen:
            blocking.append({"kind": "duplicate_host", "evidence": n, "repair": "keep one copy", "host": n, "blocking": True})
        seen.add(n)
        if host.get("role") and roles.get(n) and host.get("role") != roles.get(n):
            blocking.append({"kind": "role_mismatch", "evidence": f"{n}:{host.get('role')}", "repair": f"set role to {roles.get(n)}", "host": n, "blocking": True})
        ports = host.get("ports") or []
        if not (1 <= len(ports) <= 3):
            blocking.append({"kind": "port_count", "evidence": str(len(ports)), "repair": "keep 1-3 ports", "host": n, "blocking": True})
        numbers = [p.get("port") for p in ports]
        if len(set(numbers)) != len(numbers):
            blocking.append({"kind": "duplicate_port", "evidence": str(numbers), "repair": "unique ports", "host": n, "blocking": True})
        for port in ports:
            for artifact in port.get("files") or []:
                path = artifact.get("path") or ""
                meta = artifact.get("metadata") or {}
                mtime = str(meta.get("mtime") or "")
                if "honeypot" in (artifact.get("content") or "").lower():
                    blocking.append({"kind": "fingerprint_label", "evidence": path, "repair": "remove honeypot wording", "host": n, "path": path, "blocking": True})
                if len(mtime) >= 7 and mtime.startswith("2024-") and mtime[5:7] in {"10", "11", "12"}:
                    blocking.append({"kind": "lab_clock_mtime", "evidence": f"{path}:{mtime}", "repair": "mtime before lab clock", "host": n, "path": path, "blocking": True})
    return blocking


def check_path_refs(honey, traps):
    blocking = []
    files = host_files(honey)
    for host in traps.get("hosts") or []:
        name = host.get("name")
        available = set(files.get(name) or [])
        for i, loop in enumerate(host.get("host_loops") or []):
            if loop and loop[0] != loop[-1]:
                blocking.append({"kind": "open_loop", "evidence": str(loop), "repair": "close loop to first path", "host": name, "blocking": True})
            missing = [p for p in loop if p not in available]
            if missing:
                blocking.append({"kind": "missing_clue", "evidence": str(missing), "repair": "create files or drop loop steps", "host": name, "path": missing[0], "blocking": True})
    names = set(files)
    for chain in traps.get("chains") or []:
        steps = chain.get("steps") or []
        if len(steps) < 2:
            blocking.append({"kind": "short_chain", "evidence": chain.get("name"), "repair": "need >=2 steps", "blocking": True})
            continue
        if any(s.get("host") not in names for s in steps):
            blocking.append({"kind": "chain_host_missing", "evidence": str(steps), "repair": "use existing hosts", "blocking": True})
    return blocking


def check_exposed(honey, freeze):
    blocking = []
    if freeze is None:
        return blocking
    snapshot = getattr(freeze, "_last_honey", None)
    if not snapshot:
        return blocking
    index = {}
    for host in snapshot.get("hosts") or []:
        for port in host.get("ports") or []:
            for artifact in port.get("files") or []:
                index[(host["name"], artifact.get("path"))] = artifact.get("content")
    for host in honey.get("hosts") or []:
        for port in host.get("ports") or []:
            for artifact in port.get("files") or []:
                key = (host["name"], artifact.get("path"))
                if freeze.is_exposed(*key) and key in index:
                    if artifact.get("content") != index[key]:
                        blocking.append({
                            "kind": "exposed_rewrite",
                            "evidence": f"{key[0]}:{key[1]}",
                            "repair": "restore previously observed content",
                            "host": key[0],
                            "path": key[1],
                            "blocking": True,
                        })
    return blocking


def deterministic_review(honey, traps, topology, freeze=None):
    blocking = check_consistency(honey, topology) + check_path_refs(honey, traps) + check_exposed(honey, freeze)
    uncertain = []
    return blocking, uncertain


def classify_llm_issue(item: dict) -> str:
    """Paper: unsupported suspicions stay uncertain and do not block deploy."""
    kind = str(item.get("kind") or "")
    if kind in REQUIRED_KINDS:
        return "blocking"
    blob = " ".join(str(item.get(k) or "") for k in ("kind", "evidence", "repair")).lower()
    if "honeypot" in blob or "this is a trap" in blob:
        return "blocking"
    return "uncertain"


def llm_review(client, honey, traps, protocol_measurements=None):
    if client is None:
        return {"risk_score": 0.2, "blocking": [], "uncertain": [], "feedback": list(default_ar_constraints())}
    payload = {
        "candidate_environment": honey,
        "candidate_guidance": traps,
        "protocol_measurements": protocol_measurements,
    }
    fallback = {"risk_score": 0.2, "blocking": [], "uncertain": [], "feedback": []}
    result = client.complete(prompts.review_system(), json.dumps(payload), fallback, task="review.inspect")
    if not isinstance(result, dict):
        return fallback
    result.setdefault("blocking", [])
    result.setdefault("uncertain", [])
    result.setdefault("feedback", [])
    try:
        result["risk_score"] = float(result.get("risk_score") or 0.2)
    except Exception:
        result["risk_score"] = 0.2
    return result


def _apply_repairs(honey, traps, blocking, topology=None):
    honey = normalize_environment(honey, topology)
    honey = harden_honey_surface(honey, topology or {"hosts": honey.get("hosts") or []})
    honey = resolve_directory_file_conflicts(honey)
    files = host_files(honey)
    for issue in blocking:
        kind = issue.get("kind")
        host_name = issue.get("host")
        if kind == "missing_clue" and host_name:
            path = issue.get("path")
            for host in honey.get("hosts") or []:
                if host.get("name") != host_name:
                    continue
                if path and path not in files.get(host_name, []):
                    if host.get("ports"):
                        host["ports"][0].setdefault("files", []).append({
                            "path": path,
                            "content": f"# operational record for {path}\n",
                            "metadata": {"owner": "ops", "mode": "0644", "mtime": "2024-03-18T09:00:00Z"},
                        })
        if kind == "open_loop":
            for host in traps.get("hosts") or []:
                loops = []
                for loop in host.get("host_loops") or []:
                    if loop and loop[0] != loop[-1]:
                        loop = list(loop) + [loop[0]]
                    loops.append(loop)
                host["host_loops"] = loops
        if kind == "lab_clock_mtime":
            for host in honey.get("hosts") or []:
                for port in host.get("ports") or []:
                    for artifact in port.get("files") or []:
                        meta = artifact.setdefault("metadata", {})
                        mtime = str(meta.get("mtime") or "")
                        if mtime.startswith("2024-1"):
                            meta["mtime"] = SAFE_MTIME
    return honey, traps


def review_until_pass(honey, traps, topology, client=None, freeze=None,
                      protocol_measurements=None, repair_budget=R_DEFAULT):
    """Return deployable candidate or a blocking report for the Planner."""
    repairs = 0
    last_blocking = []
    last_llm = {}
    honey = normalize_environment(honey, topology)
    while True:
        blocking, uncertain = deterministic_review(honey, traps, topology, freeze=freeze)
        last_llm = llm_review(client, honey, traps, protocol_measurements)
        for item in last_llm.get("blocking") or []:
            if not isinstance(item, dict):
                continue
            if classify_llm_issue(item) == "blocking":
                blocking.append(item)
            else:
                uncertain.append(item)
        last_blocking = blocking
        if not blocking:
            return {
                "deployable": True,
                "honey": honey,
                "traps": traps,
                "blocking": [],
                "uncertain": uncertain + list(last_llm.get("uncertain") or []),
                "risk_score": last_llm.get("risk_score", 0.2),
                "feedback": last_llm.get("feedback") or list(default_ar_constraints()),
                "repairs": repairs,
                "issues": [],
                "stealth_constraints": last_llm.get("feedback") or list(default_ar_constraints()),
                "source": "review_loop",
            }
        if repairs >= repair_budget:
            return {
                "deployable": False,
                "honey": honey,
                "traps": traps,
                "blocking": blocking,
                "uncertain": uncertain,
                "risk_score": max(0.55, float(last_llm.get("risk_score") or 0.55)),
                "feedback": last_llm.get("feedback") or [],
                "repairs": repairs,
                "issues": [i.get("kind") for i in blocking],
                "stealth_constraints": last_llm.get("feedback") or list(default_ar_constraints()),
                "source": "review_loop_blocked",
            }
        honey, traps = _apply_repairs(honey, traps, blocking, topology=topology)
        repairs += 1
