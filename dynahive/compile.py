from __future__ import annotations

import json
import shutil
import hashlib
from pathlib import Path

from .runtime import write_json


def compile_deployment(root: Path, topology: dict, honey: dict, traps: dict, audit: dict) -> Path:
    root = Path(root)
    (root / "deployments").mkdir(parents=True, exist_ok=True)
    shadow = root / "shadow"
    shadow.mkdir(parents=True, exist_ok=True)
    for host in honey["hosts"]:
        bundle = root / "deployments" / host["name"]
        (bundle / "config").mkdir(parents=True, exist_ok=True)
        (bundle / "logs").mkdir(parents=True, exist_ok=True)
        write_json(bundle / "config" / "host.json", host)
        write_json(bundle / "config" / "traps.json", next((x for x in traps.get("hosts", []) if x["name"] == host["name"]), {}))
    write_json(shadow / "shadow_topology.json", topology)
    write_json(shadow / "environment.json", honey)
    write_json(shadow / "guidance.json", traps)
    write_json(shadow / "deception_consistency_report.json", audit)
    write_json(shadow / "runtime_spec.json", {"hosts": honey["hosts"], "topology": topology})
    # Build the actual reconstructed service implementation, not http.server.
    snapshot = root.parent/'code_snapshot'
    source = snapshot if snapshot.exists() else Path(__file__).resolve().parent
    code = shadow / 'code' / 'dynahive'
    code.mkdir(parents=True, exist_ok=True)
    for name in ['runtime.py', 'honeypot.py', 'run_honeypot.py', 'namespace_tool.py']:
        shutil.copyfile(source / name, code / name)
    (code/'__init__.py').write_text('"""Standalone reconstructed service runtime."""\n',encoding='utf-8')
    write_json(shadow/'service_source_manifest.json', {'sha256':{
        path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in code.glob('*.py')}})
    (shadow / 'Dockerfile').write_text(
        'FROM python:3.10-slim\nRUN pip install --no-cache-dir asyncssh==2.14.2\n'
        'COPY code /app\nWORKDIR /app\nENV PYTHONPATH=/app\n'
        'ENTRYPOINT ["python", "-m", "dynahive.run_honeypot"]\n', encoding='utf-8')
    services = {}
    for index, host in enumerate(honey["hosts"], 1):
        services[host["name"]] = {
            "build": {"context": ".", "dockerfile": "Dockerfile"},
            "image": "dynahive-reconstructed-service:local",
            "command": ["--project-root", "/lab", "--deployment", host['name']],
            "volumes": [f"{str(root.resolve()).replace(chr(92), '/')}:/lab"],
            "networks": ["shadow"], "mem_limit": "256m", "cpus": "0.50",
        }
    (shadow / "docker-compose.yml").write_text(json.dumps({"services": services,
        "networks": {"shadow": {"driver": "bridge", "internal": True}}}, indent=2), encoding="utf-8")
    return root / "deployments"
