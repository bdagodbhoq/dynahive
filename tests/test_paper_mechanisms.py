from dynahive.agents import fixture_honey
from dynahive.controller import bootstrap, login
from dynahive.guidance_search import search, feasible_whole_chain, prepare_context
from dynahive.prompts import (
    environment_system, guidance_assess, guidance_expand, planner_system, review_system,
)
from dynahive.review_loop import review_until_pass, classify_llm_issue
from dynahive.environment_normalize import normalize_environment


def test_runtime_prompts_are_paper_length():
    for text in (environment_system(), guidance_expand(), guidance_assess(),
                 review_system(), planner_system()):
        assert len(text) > 400
        assert "JSON" in text


def test_algorithm1_returns_feasible_chain():
    topology = {
        "hosts": [
            {"name": "bastion-01", "role": "bastion", "ip": "10.77.0.10"},
            {"name": "app-01", "role": "application", "ip": "10.77.0.20"},
            {"name": "fileserver-01", "role": "fileserver", "ip": "10.77.0.30"},
        ]
    }
    honey = fixture_honey(topology)
    result = search(honey, [], "Obtain operational archive", "bastion-01", client=None, k=6, b=3)
    assert result["source"] == "algorithm1"
    assert result["traps"]["hosts"]
    if result["chain"]:
        facts, _, _ = prepare_context(honey, [], "Obtain operational archive", "bastion-01")
        ok, errors = feasible_whole_chain(result["chain"], facts)
        assert ok, errors


def test_review_blocks_missing_clue():
    topology = {"hosts": [{"name": "bastion-01", "role": "bastion"}]}
    honey = fixture_honey({"hosts": [{"name": "bastion-01", "role": "bastion", "ip": "10.77.0.10"}]})
    traps = {"hosts": [{"name": "bastion-01", "host_loops": [
        ["/no/such/file", "/also/missing", "/no/such/file"]
    ]}], "chains": []}
    report = review_until_pass(honey, traps, topology, client=None, repair_budget=0)
    assert report["deployable"] is False
    kinds = {item.get("kind") for item in report["blocking"]}
    assert "missing_clue" in kinds


def test_planner_retains_when_loops_exist(tmp_path):
    ctx = bootstrap(tmp_path / "retain", offline=True)
    login(ctx)
    coord = ctx["coordinator"]
    plan = coord.planner.make_task_plan(
        coord.environment.honey, coord.guidance.traps, ctx["topology"],
        observations=[{"host": "bastion-01", "command": "whoami", "action": "probe"}],
    )
    has_loops = any((h.get("host_loops") or []) for h in coord.guidance.traps.get("hosts") or [])
    has_chain = bool(coord.guidance.traps.get("chains"))
    if has_loops or has_chain:
        assert plan["invoke_guidance"] is False


def test_llm_style_nits_are_uncertain_not_blocking():
    assert classify_llm_issue({"kind": "generation_artifacts", "evidence": "bootstrap.log"}) == "uncertain"
    assert classify_llm_issue({"kind": "missing_clue", "path": "/x"}) == "blocking"


class _NitClient:
    def complete(self, system, user, fallback=None, task="unspecified", json_output=True):
        if task == "review.inspect":
            return {
                "risk_score": 0.98,
                "blocking": [{"kind": "generation_artifacts", "evidence": "bootstrap.log"}],
                "uncertain": [],
                "feedback": [],
            }
        return fallback


def test_review_deploys_after_normalizing_llm_nits():
    topology = {"hosts": [
        {"name": "bastion-01", "role": "bastion", "ip": "10.77.0.10"},
        {"name": "app-01", "role": "application", "ip": "10.77.0.20"},
        {"name": "fileserver-01", "role": "fileserver", "ip": "10.77.0.30"},
    ]}
    honey = fixture_honey(topology)
    traps = {"hosts": [], "chains": []}
    report = review_until_pass(honey, traps, topology, client=_NitClient(), repair_budget=2)
    assert report["deployable"] is True
    assert any(i.get("kind") == "generation_artifacts" for i in report.get("uncertain") or [])


class _RejectAssess:
    def complete(self, system, user, fallback=None, task="unspecified", json_output=True):
        if task == "guidance.assess":
            return {"progress": False, "reason": "strict"}
        if task == "guidance.expand":
            return fallback
        if task == "guidance.select":
            return {"selected": 0}
        return fallback


def test_search_recovers_archive_chain_when_assessor_rejects():
    topology = {
        "hosts": [
            {"name": "bastion-01", "role": "bastion", "ip": "10.77.0.10"},
            {"name": "app-01", "role": "application", "ip": "10.77.0.20"},
            {"name": "fileserver-01", "role": "fileserver", "ip": "10.77.0.30"},
        ]
    }
    honey = normalize_environment(fixture_honey(topology), topology)
    result = search(honey, [], "Obtain operational archive", "bastion-01",
                    client=_RejectAssess(), k=6, b=3, budget=4)
    assert result["chain"]
    hosts = {s.get("host") for s in result["chain"]}
    assert "fileserver-01" in hosts


def test_planner_task_plan_fields(tmp_path):
    ctx = bootstrap(tmp_path / "plan", offline=True)
    login(ctx)
    plan = ctx["coordinator"].planner.make_task_plan(
        ctx["coordinator"].environment.honey,
        ctx["coordinator"].guidance.traps,
        ctx["topology"],
        observations=[{"host": "bastion-01", "command": "whoami", "action": "probe"}],
    )
    for key in ("reconstruction", "G", "invoke_environment", "invoke_guidance",
                "invoke_review", "retain"):
        assert key in plan
