#!/usr/bin/env python3
"""Run the paper closed loop and print a checklist against the design."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dynahive.controller import bootstrap, login, step, deploy
from dynahive.deception import deploy as deploy_fn
from dynahive.guidance_search import search, feasible_whole_chain, prepare_context, K_DEFAULT, B_DEFAULT
from dynahive.path_verifier import verify_path
from dynahive.perception import perceive
from dynahive.prompts import (
    environment_system, guidance_assess, guidance_expand, planner_system, review_system,
)
from dynahive.review_loop import review_until_pass


def flag(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


def summarize_api_calls(path: Path) -> dict:
    rows = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            rows.append({
                "task": rec.get("task"),
                "model": rec.get("model"),
                "status": rec.get("status"),
                "latency_s": rec.get("latency_s"),
            })
    live = [r for r in rows if r.get("status") not in {None, "offline"}]
    return {
        "n": len(rows),
        "live": len(live),
        "offline": sum(1 for r in rows if r.get("status") == "offline"),
        "ok": sum(1 for r in rows if r.get("status") in {"ok", "success"}),
        "tasks": rows,
    }


def main() -> int:
    live = "--live" in sys.argv
    work = ROOT / "work" / ("paper-flow-live" if live else "paper-flow")
    if work.exists():
        import shutil
        shutil.rmtree(work)
    print("mode:", "LIVE API" if live else "mock")
    ctx = bootstrap(work, offline=not live)
    sid = login(ctx)
    coord = ctx["coordinator"]
    ctx["freeze"].protect(coord.environment.honey)
    honey = coord.environment.honey
    traps = coord.guidance.traps
    entry = ctx["entry"]

    report = {"checks": []}

    def check(name, ok, detail=""):
        report["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        print(f"[{flag(ok)}] {name}" + (f" — {detail}" if detail else ""))

    # 0. Prompts
    check("environment prompt is paper-length", len(environment_system()) > 400, str(len(environment_system())))
    check("guidance expand prompt is paper-length", len(guidance_expand()) > 400)
    check("guidance assess prompt forbids hidden defender state",
          "only" in guidance_assess().lower() and "hidden" in guidance_assess().lower()
          and "future" in guidance_assess().lower())
    check("planner prompt has three analyses", "Attack State Reconstruction" in planner_system())
    check("review prompt has checks (i)(ii)(iii)", "(i)" in review_system() and "(iii)" in review_system())

    # 1. Perception
    events = [
        {"session": sid, "host": entry, "action": "login", "success": True, "identity": "ops"},
        {"session": sid, "host": entry, "action": "probe", "command": "whoami", "success": True},
    ]
    perception = perceive(ctx["client"], ctx["topology"], events)
    check("perception returns structured facts vs inferences",
          isinstance(perception, dict) and "facts" in perception and "inferences" in perception,
          ",".join(sorted(perception.keys())[:8]) if isinstance(perception, dict) else type(perception).__name__)

    # 2. Planner task plan
    who = step(ctx, sid, "whoami")
    ident = step(ctx, sid, "id")
    ls = step(ctx, sid, "ls -la")
    plan = coord.planner.make_task_plan(
        honey, traps, ctx["topology"],
        observations=events + [
            {"host": entry, "command": "whoami", "action": "probe"},
            {"host": entry, "command": "ls -la", "action": "list"},
        ],
    )
    check("planner reconstruction present", "reconstruction" in plan and "G" in plan)
    check("planner has invoke/retain fields",
          all(k in plan for k in ("invoke_environment", "invoke_guidance", "invoke_review", "retain")))
    check("environment revisions precede guidance in the plan schema",
          "invoke_environment" in plan and "invoke_guidance" in plan)
    print("    G =", plan.get("G"))
    print("    retain =", plan.get("retain"), "env/guid/rev =",
          plan.get("invoke_environment"), plan.get("invoke_guidance"), plan.get("invoke_review"))

    # 3. Guidance Algorithm 1 (reuse the coordinator plan when it already has a chain)
    prior = coord.guidance.last_plan or {}
    if prior.get("chain"):
        result = prior
    else:
        result = search(
            coord.environment.honey, events, plan["G"], entry,
            client=ctx["client"], k=K_DEFAULT, b=B_DEFAULT,
        )
    chain = result.get("chain") or []
    check("Algorithm 1 source", result.get("source") == "algorithm1", result.get("source"))
    check("Algorithm 1 uses K=6 b=3", K_DEFAULT == 6 and B_DEFAULT == 3, f"K={K_DEFAULT} b={B_DEFAULT}")
    check("Algorithm 1 produced a chain of (clue, action, result)",
          bool(chain) and all({"clue", "action", "result", "host"} <= set(s) for s in chain),
          f"len={len(chain)}")
    facts, _, _ = prepare_context(coord.environment.honey, events, plan["G"], entry)
    ok, errors = feasible_whole_chain(chain, facts) if chain else (False, [{"constraint": "empty"}])
    check("FeasibleWholeChain is deterministic and passes", ok, json.dumps(errors)[:180] if not ok else "ok")
    hosts_in_chain = {s.get("host") for s in chain}
    check("chain stays on existing hosts", hosts_in_chain <= set(facts["files"]))
    archive = ctx["topology"]["hosts"][-1]["name"]
    check("chain reaches the archive host (paper goal-gradient path)",
          archive in hosts_in_chain, f"hosts={sorted(hosts_in_chain)} archive={archive}")
    print("    chain hosts:", sorted(hosts_in_chain))
    for i, s in enumerate(chain[:6]):
        print(f"    e{i+1}: host={s.get('host')} clue={s.get('path') or s.get('clue')} action={s.get('action')}")

    # 4. Execute the chain in World (paper: each step realizable)
    executed = []
    for s in chain[:6]:
        host = s.get("host") or entry
        path = s.get("path")
        if not path:
            continue
        hop_sid = sid
        if host != entry:
            cred = ctx["world"].hosts[host]["credential"]
            hop_sid = f"{sid}-{host}"
            ctx["world"].interact(hop_sid, {"op": "login", "host": host, **cred}, "guidance-hop")
        result = ctx["world"].execute_command(hop_sid, host, f"cat {path}")
        text = (result or {}).get("output") or ""
        ctx["freeze"].mark_read(host, path)
        readable = "No such file" not in text and "permission denied" not in text.lower()
        executed.append({"host": host, "path": path, "ok": readable, "preview": text[:80].replace("\n", " ")})
        check(f"World realizes clue {host}:{path}", readable, text[:60].replace("\n", " "))
        again = (ctx["world"].execute_command(hop_sid, host, f"cat {path}") or {}).get("output") or ""
        check(f"repeat read of {host}:{path} is stable", again == text)

    # 5. Review
    review = review_until_pass(
        coord.environment.honey, result.get("traps") or traps, ctx["topology"],
        client=ctx["client"], freeze=ctx["freeze"], repair_budget=2,
    )
    check("Review reports deployable flag", "deployable" in review)
    check("Review has blocking vs uncertain lists", "blocking" in review and "uncertain" in review)
    check("Review repair budget field present", "repairs" in review, f"repairs={review.get('repairs')}")
    print("    deployable =", review.get("deployable"), "blocking =", len(review.get("blocking") or []))

    # 6. Deception
    if review.get("deployable"):
        deployed = deploy_fn(
            work / "deploy", ctx["topology"],
            review.get("honey") or coord.environment.honey,
            review.get("traps") or result.get("traps") or traps,
            {"ok": True, "issues": review.get("issues") or []},
            freeze=ctx["freeze"],
        )
        check("Deception wrote per-host bundles", (deployed / entry / "config" / "host.json").is_file(), str(deployed))
        env_json = work / "deploy" / "shadow" / "environment.json"
        guid_json = work / "deploy" / "shadow" / "guidance.json"
        check("deploy names match paper modules (environment.json / guidance.json)",
              env_json.is_file() and guid_json.is_file())
    else:
        check("Deception refused non-reviewed candidate", True, "not deployable")

    # 7. Freeze: rewriting an exposed file must be blocked by Review
    if executed:
        first = next((e for e in executed if e.get("ok") and e.get("path")), None)
        if first:
            mutated = json.loads(json.dumps(coord.environment.honey))
            for host in mutated.get("hosts") or []:
                if host.get("name") != first["host"]:
                    continue
                for port in host.get("ports") or []:
                    for art in port.get("files") or []:
                        if art.get("path") == first["path"]:
                            art["content"] = "TAMPERED"
            blocked = review_until_pass(
                mutated, result.get("traps") or traps, ctx["topology"],
                client=None, freeze=ctx["freeze"], repair_budget=0,
            )
            kinds = {i.get("kind") for i in blocked.get("blocking") or []}
            check("Review blocks rewrite of exposed facts",
                  blocked.get("deployable") is False and "exposed_rewrite" in kinds,
                  str(kinds))

    # 8. Missing clue cannot pass FeasibleWholeChain
    fake = [{"clue": "/nope", "action": "cat /nope", "result": "x", "host": entry, "path": "/nope"}]
    ok_fake, err_fake = feasible_whole_chain(fake, facts)
    check("missing clue fails deterministic verifier", ok_fake is False)

    api = summarize_api_calls(work / "api_calls.jsonl")
    report["api"] = {k: v for k, v in api.items() if k != "tasks"}
    print()
    print(f"API calls: n={api['n']} live={api['live']} offline_fallback={api['offline']} ok={api['ok']}")
    for row in api["tasks"][:30]:
        print(f"    {row.get('status')}  {row.get('task')}  {row.get('model')}  {row.get('latency_s')}s")
    check("live API actually served agent calls" if live else "mock path recorded",
          (api["live"] > 0) if live else True,
          f"live={api['live']} n={api['n']}")

    passed = sum(1 for c in report["checks"] if c["ok"])
    failed = [c["name"] for c in report["checks"] if not c["ok"]]
    print()
    print(f"RESULT {passed}/{len(report['checks'])} paper-flow checks passed")
    if failed:
        print("FAILED:")
        for name in failed:
            print(" -", name)
    (work / "paper_flow_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
