"""Closed loop: observe → plan → environment → guidance → review → deploy."""
from __future__ import annotations

import json
from pathlib import Path

from .agents import fixture_honey
from .deception import deploy
from .frame_agents import Coordinator
from .freeze import FreezeLedger
from .honeypot import World, materialize
from .mock import MockClient
from .path_verifier import verify_path
from .perception import perceive
from .runtime import Journal, LLMClient


def load_topology(path: Path | None = None) -> dict:
    default = Path(__file__).resolve().parents[1] / "examples" / "topology.json"
    return json.loads((path or default).read_text(encoding="utf-8"))


def build_client(offline: bool = True, settings: Path | None = None, journal: Path | None = None):
    if offline:
        return MockClient(journal=journal)
    import os
    cfg = {}
    if settings and settings.is_file():
        cfg = json.loads(settings.read_text(encoding="utf-8"))
    return LLMClient(
        base_url=os.environ.get("DYNHIVE_BASE_URL") or cfg.get("DYNHIVE_BASE_URL"),
        api_key=os.environ.get("DYNHIVE_API_KEY") or cfg.get("DYNHIVE_API_KEY"),
        model=os.environ.get("DYNHIVE_MODEL") or cfg.get("DYNHIVE_MODEL") or "gpt-6.1-sol",
        wire_api=os.environ.get("DYNHIVE_WIRE_API") or cfg.get("DYNHIVE_WIRE_API") or "responses",
        reasoning_effort=os.environ.get("DYNHIVE_REASONING_EFFORT") or cfg.get("DYNHIVE_REASONING_EFFORT") or "high",
        journal=journal,
        timeout=int(os.environ.get("DYNHIVE_TIMEOUT") or cfg.get("DYNHIVE_TIMEOUT") or 180),
    )


def bootstrap(work: Path, topology: dict | None = None, offline: bool = True):
    work.mkdir(parents=True, exist_ok=True)
    topology = topology or load_topology()
    journal = Journal(work / "events.jsonl")
    client = build_client(offline=offline, journal=work / "api_calls.jsonl")
    honey = fixture_honey(topology)
    if not offline:
        from . import prompts as _prompts
        generated = client.complete(
            _prompts.environment_system(),
            json.dumps({"topology": topology, "task": "bootstrap three-host decoy"}),
            fallback=honey,
            task="environment.bootstrap",
        )
        if isinstance(generated, dict) and generated.get("hosts"):
            from .environment_normalize import normalize_environment
            honey = normalize_environment(generated, topology)
    traps = {"hosts": [], "chains": []}
    entry = topology["hosts"][0]["name"]
    freeze = FreezeLedger()
    coord = Coordinator(topology, honey, traps, entry, client=client, journal=journal, freeze=freeze)
    spec = materialize(coord.environment.honey, coord.guidance.traps, topology, seed=1)
    world = World(spec, journal, seed=1)
    freeze.protect(coord.environment.honey)
    return {
        "topology": topology,
        "honey": honey,
        "world": world,
        "coordinator": coord,
        "client": client,
        "journal": journal,
        "freeze": freeze,
        "entry": entry,
        "work": work,
    }


def login(ctx) -> str:
    host = ctx["entry"]
    cred = ctx["world"].hosts[host]["credential"]
    sid = "s1"
    ctx["world"].interact(sid, {"op": "login", "host": host, **cred}, "controller")
    return sid


def step(ctx, session: str, command: str):
    host = ctx["entry"]
    frame = ctx["coordinator"].step(command, telemetry_events=[{
        "action": command.split()[0] if command.strip() else "probe",
        "host": host,
        "command": command,
    }])
    result = ctx["world"].execute_command(session, host, command)
    output = (result or {}).get("output") or ""
    if command.strip().startswith(("cat ", "head ", "tail ")):
        parts = command.split()
        if len(parts) >= 2:
            ctx["freeze"].mark_read(host, parts[-1])
    return {"frame": frame, "result": result, "output": output}


def close_loop_demo(work: Path, offline: bool = True) -> dict:
    ctx = bootstrap(work, offline=offline)
    sid = login(ctx)
    traces = []
    for command in ("whoami", "ls", "cat /etc/hostname"):
        traces.append({"command": command, **{k: v for k, v in step(ctx, sid, command).items() if k != "frame"}})
    audit = {"ok": True, "issues": ctx["coordinator"].review_agent.last_review.get("issues") or []}
    deployed = deploy(
        work / "deploy",
        ctx["topology"],
        ctx["coordinator"].environment.honey,
        ctx["coordinator"].guidance.traps,
        audit,
        freeze=ctx["freeze"],
    )
    host = ctx["entry"]
    files = ctx["coordinator"].environment.host_files(host)
    path_report = {"ok": True, "steps": []}
    if files:
        path_report = verify_path(ctx["world"], sid, [{
            "host": host, "path": files[0], "action": "cat",
        }])
    perceive(ctx["client"], ctx["topology"], [
        {"action": "probe", "host": host, "command": "whoami"},
    ])
    return {
        "entry": host,
        "traces": traces,
        "deployed": str(deployed),
        "path_ok": path_report.get("ok"),
        "review": ctx["coordinator"].review_agent.last_review,
    }
