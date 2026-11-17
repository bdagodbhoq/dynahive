"""Deterministic path verifier (checklist §8). LLM is not used here."""
from __future__ import annotations

from pathlib import PurePosixPath


def verify_step(world, host: str, session: str, clue_path: str, action: str) -> dict:
    """Check that a guidance step is actually executable in World."""
    errors = []
    vfs = (world.vfs or {}).get(host)
    if vfs is None:
        errors.append({"constraint": "host_vfs", "host": host, "evidence": "no vfs"})
        return {"ok": False, "errors": errors}

    path = str(PurePosixPath(clue_path or "/"))
    node = None
    try:
        node = vfs.get(path) if hasattr(vfs, "get") else None
    except Exception as exc:
        errors.append({"constraint": "path_lookup", "path": path, "evidence": str(exc)})

    if node is None and hasattr(vfs, "stat"):
        try:
            node = vfs.stat(path)
        except Exception:
            node = None
    if node is None:
        # Fall back to listing files known to World host spec.
        files = []
        spec = world.hosts.get(host) or {}
        for port in spec.get("ports") or []:
            files.extend(f.get("path") for f in port.get("files") or [] if f.get("path"))
        if path not in files:
            errors.append({"constraint": "clue_exists", "path": path, "host": host})

    if action.startswith("cat") or action.startswith("read"):
        result = world.execute_command(session, host, f"cat {path}")
        out = (result or {}).get("output") or ""
        if "No such file" in out or "Permission denied" in out:
            errors.append({
                "constraint": "readable",
                "path": path,
                "evidence": out[:200],
            })

    return {"ok": not errors, "errors": errors, "host": host, "path": path}


def verify_path(world, session: str, steps: list) -> dict:
    reports = [verify_step(world, s["host"], session, s["path"], s.get("action") or "cat") for s in steps]
    return {"ok": all(r["ok"] for r in reports), "steps": reports}
