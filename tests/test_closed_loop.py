from pathlib import Path

from dynahive.controller import close_loop_demo, bootstrap, login, step
from dynahive.freeze import FreezeLedger
from dynahive.path_verifier import verify_path


def test_mock_closed_loop(tmp_path):
    report = close_loop_demo(tmp_path / "work", offline=True)
    assert report["entry"] == "bastion-01"
    assert report["traces"]
    assert report["traces"][0]["output"]
    assert "honeypot" not in (report["traces"][0]["output"] or "").lower()
    assert Path(report["deployed"]).exists()


def test_world_identity_stable(tmp_path):
    ctx = bootstrap(tmp_path / "s", offline=True)
    sid = login(ctx)
    first = step(ctx, sid, "whoami")["output"]
    second = step(ctx, sid, "whoami")["output"]
    assert first.strip() == second.strip()
    assert first.strip()


def test_freeze_keeps_exposed_content():
    ledger = FreezeLedger()
    honey = {"hosts": [{"name": "h1", "ports": [{"files": [
        {"path": "/tmp/a.txt", "content": "one", "metadata": {}},
    ]}]}]}
    ledger.protect(honey)
    ledger.mark_read("h1", "/tmp/a.txt")
    honey2 = {"hosts": [{"name": "h1", "ports": [{"files": [
        {"path": "/tmp/a.txt", "content": "CHANGED", "metadata": {}},
    ]}]}]}
    out = ledger.protect(honey2)
    assert out["hosts"][0]["ports"][0]["files"][0]["content"] == "one"


def test_path_verifier_on_missing_file(tmp_path):
    ctx = bootstrap(tmp_path / "p", offline=True)
    sid = login(ctx)
    report = verify_path(ctx["world"], sid, [{
        "host": ctx["entry"],
        "path": "/this/does/not/exist",
        "action": "cat",
    }])
    assert report["ok"] is False
