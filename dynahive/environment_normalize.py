"""Make a generated decoy surface internally consistent before Review."""
from __future__ import annotations

import copy

from .honeypot import ACCOUNTS, BANNERS

SAFE_MTIME = "2024-03-18T09:12:00Z"
OS_RELEASE = (
    "PRETTY_NAME=\"Ubuntu 22.04.4 LTS\"\n"
    "NAME=\"Ubuntu\"\n"
    "VERSION_ID=\"22.04\"\n"
    "VERSION=\"22.04.4 LTS (Jammy Jellyfish)\"\n"
)
ARCHIVE_README = (
    "# staging archive index\n"
    "owner=records-ops\n"
    "ticket=CHG2916\n"
    "path=/srv/archive/staging\n"
)


def _ensure_file(host: dict, path: str, content: str, owner: str, mode: str = "0644"):
    ports = host.setdefault("ports", [])
    if not ports:
        ports.append({"port": 22, "service": "ssh", "banner": BANNERS["ssh"], "files": []})
    for port in ports:
        for artifact in port.get("files") or []:
            if artifact.get("path") == path:
                artifact["content"] = content
                meta = artifact.setdefault("metadata", {})
                meta["owner"] = owner
                meta["mode"] = mode
                meta["mtime"] = SAFE_MTIME
                return
    ports[0].setdefault("files", []).append({
        "path": path,
        "content": content,
        "metadata": {"owner": owner, "mode": mode, "mtime": SAFE_MTIME},
    })


def normalize_environment(honey: dict, topology: dict | None = None) -> dict:
    honey = copy.deepcopy(honey or {"hosts": []})
    topo_hosts = (topology or {}).get("hosts") or honey.get("hosts") or []
    roles = {h.get("name"): h.get("role") for h in topo_hosts}
    last = topo_hosts[-1]["name"] if topo_hosts else None
    for host in honey.get("hosts") or []:
        name = host.get("name")
        role = roles.get(name) or host.get("role") or "bastion"
        host["role"] = role
        account = ACCOUNTS.get(role, "ops")
        cred = host.setdefault("credential", {})
        cred["username"] = cred.get("username") or account
        for port in host.get("ports") or []:
            svc = str(port.get("service") or "ssh").lower()
            if svc in BANNERS:
                port["banner"] = BANNERS[svc]
            for artifact in port.get("files") or []:
                path = artifact.get("path") or ""
                text = artifact.get("content") or ""
                if "honeypot" in text.lower() or "decoy" in text.lower():
                    text = "\n".join(
                        ln for ln in text.splitlines()
                        if "honeypot" not in ln.lower() and "decoy" not in ln.lower()
                    )
                    artifact["content"] = (text + "\n") if text else f"# {name} operations snapshot\n"
                if path.rstrip("/") == "/etc/hostname":
                    artifact["content"] = name + "\n"
                meta = artifact.setdefault("metadata", {})
                if path.startswith("/etc/") or path.startswith("/var/log/"):
                    meta["owner"] = meta.get("owner") if meta.get("owner") in {"root", account} else "root"
                elif path.startswith("/home/"):
                    home_user = path.split("/")[2] if path.count("/") >= 2 else account
                    meta["owner"] = home_user
                else:
                    meta.setdefault("owner", account)
                mode = str(meta.get("mode") or "0644")
                digits = "".join(ch for ch in mode if ch.isdigit()) or "0644"
                if len(digits) == 3:
                    digits = "0" + digits
                # world-readable unless it is a private key
                if "id_" in path or path.endswith(".pem"):
                    meta["mode"] = "0640"
                else:
                    other = int(digits[-1])
                    if other < 4:
                        digits = digits[:-1] + "4"
                    meta["mode"] = digits
                mtime = str(meta.get("mtime") or "")
                if (not mtime) or mtime.startswith("2024-1") or "bootstrap" in path:
                    meta["mtime"] = SAFE_MTIME
        _ensure_file(host, "/etc/hostname", name + "\n", "root")
        _ensure_file(host, "/etc/os-release", OS_RELEASE, "root")
        _ensure_file(host, f"/home/{account}/.profile", f"# ~/.profile for {account} on {name}\n", account)
        if name == last or role == "fileserver":
            _ensure_file(host, "/srv/archive/staging/README.txt", ARCHIVE_README, account)
    return honey
