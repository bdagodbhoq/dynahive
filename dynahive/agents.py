from __future__ import annotations

import copy
import json
from .honeypot import filesystem_metadata
from pathlib import PurePosixPath

PORTS = {"firewall": [(22, "ssh"), (443, "https")], "bastion": [(22, "ssh")],
    "operations": [(22, "ssh"), (21, "ftp")], "public-web": [(80, "http"), (443, "https")],
    "public-api": [(80, "http")], "application": [(8080, "http"), (22, "ssh")],
    "database": [(3306, "mysql"), (5432, "postgresql"), (22, "ssh")], "fileserver": [(21, "ftp"), (22, "ssh")]}
FILES = {"ssh": ["/home/admin/.ssh/id_rsa.bak", "/etc/ops/maintenance.conf"],
    "http": ["/var/www/html/config.php.bak", "/var/www/html/backup-site.zip"],
    "https": ["/var/www/html/config.php.bak", "/etc/ssl/private/wildcard-prod.key"],
    "mysql": ["/etc/mysql/debian.cnf", "/var/lib/mysql/backup.sql"],
    "postgresql": ["/var/lib/postgresql/.pgpass", "/var/lib/postgresql/backup.sql"],
    "ftp": ["/srv/ftp/credentials.txt", "/srv/ftp/finance-export.csv"]}


def fixture_honey(topology):
    return {"hosts": [{"name": h["name"], "ports": [{"port": p, "service": s,
        "files": [{"path": f} for f in FILES[s]]} for p, s in PORTS.get(h["role"], [(22, "ssh")])],
        "vulnerabilities": [{"type": "weak creds", "target_port": PORTS.get(h["role"], [(22, "ssh")])[0][0]}]}
        for h in topology["hosts"]]}


def layer_context(context, layer):
    """Retrieve only the fields used by this hierarchical generation layer."""
    result = {k:context[k] for k in ('memory_mode','runtime_constraints','anti_recon_feedback',
              'consistency_feedback','short_term_telemetry') if k in context}
    def project(honey):
        hosts=[]
        for host in honey.get('hosts', []):
            if context.get('target_hosts') and host['name'] not in context['target_hosts']: continue
            item={'name':host['name']}
            if layer=='vulnerabilities': item['vulnerabilities']=host.get('vulnerabilities', [])
            else:
                item['ports']=[{k:v for k,v in p.items() if layer!='ports' or k!='files'} for p in host['ports']]
            hosts.append(item)
        return {'hosts':hosts}
    if context.get('baseline_honey'):
        result['baseline_'+layer]=project(context['baseline_honey'])
    result['retrieved_'+layer]=[project(s['honey']) for s in context.get('retrieved_strategies', [])]
    return result


def honey_agent(client, topology, preferences, context, flat=False):
    fixture = fixture_honey(topology)
    topology_hint = {"hosts": [{"name": h["name"], "role": h.get("role", "unknown")} for h in topology["hosts"]]}
    base = {"topology": topology_hint, "attacker_preferences": preferences, **context}
    if flat:
        return client.complete("Generate a complete honeynet tree in one pass. Return JSON hosts, each "
            "with name, ports [{port,service,files:[{path}]}], vulnerabilities [{type,target_port,target_file}]. "
            "Use all topology hosts, 1-3 ports per host, 1-2 files per port, 0-2 vulnerabilities per host. "
            "Include banners, short synthetic content and metadata (owner,mode,mtime). Apply runtime constraints.",
            json.dumps(base), fixture, task="honey.flat")
    ports_fixture = {"hosts": [{"name": h["name"], "ports": [{"port": p["port"], "service": p["service"]}
                     for p in h["ports"]]} for h in fixture["hosts"]]}
    ports = client.complete("You are Environment Agent Ports Layer (Appendix A). Use every topology host. "
        "Choose 1-3 plausible exposed ports consistent with role and attacker cues. Include a plausible banner per port. "
        "For finetune prefer small edits to baseline_ports. Return only JSON "
        '{"hosts":[{"name":"...","ports":[{"port":22,"service":"ssh"}]}]}.',
        json.dumps({'topology':topology_hint,'attacker_preferences':preferences,**layer_context(context,'ports')}), ports_fixture, task="honey.ports")
    from . import prompts as _prompts
    files_prompt = (
        _prompts.environment_system()
        + "\nLayer constraint: files only. Use provided ports exactly; "
        "invent no hosts or ports. For each port create 1-2 enticing role-appropriate file paths, "
        "such as operationally valuable configurations, credentials, keys, records or backups. "
        "Preserve the port banner and prefer minimal edits when baseline files exist. "
        "Include short synthetic file content and metadata (owner,mode,mtime); invent no real secrets. "
        "Keep synthetic provenance in controller metadata, not as artificial labels in emulated content. "
        "Use text-based artifacts supported by the runtime; do not claim ZIP/XLSX/PDF or native key support. "
        "Apply supplied feedback constraints and prefer minimal baseline edits. "
        "Use at most four text lines per artifact; put owner, mode and mtime only in metadata. "
        "Use the supplied login_accounts for local login identities; do not invent additional working "
        "login passwords. Accepted synthetic account references are appended during compilation. "
        'Return compact JSON {"hosts":[{"name":"...","ports":[{"port":22,"service":"ssh","files":[{"path":"..."}]}]}]}.'
    )
    constraints = layer_context(context,'files')
    # Repairs are targeted host queries, as in paper Section 4.5. Avoid sending
    # every host's prior configuration through every generation layer.
    selections = [[h] for h in ports['hosts']] if context.get('baseline_honey') else [ports['hosts']]
    collected = []
    for selection in selections:
        selected_names = {h['name'] for h in selection}
        scoped = copy.deepcopy(constraints)
        if 'baseline_files' in scoped:
            scoped['baseline_files']['hosts'] = [h for h in scoped['baseline_files']['hosts'] if h['name'] in selected_names]
        scoped['retrieved_files'] = [{'hosts':[h for h in entry['hosts'] if h['name'] in selected_names]}
                                     for entry in scoped['retrieved_files']]
        fixture_files = {'hosts': [{'name': h['name'], 'ports': [
            {**p,'files':[{'path':f} for f in FILES.get(p['service'], ['/etc/service/config.bak'])]}
            for p in h['ports']]} for h in selection]}
        generated = client.complete(files_prompt,json.dumps({'ports':{'hosts':selection},
            'roles':{h['name']:h['role'] for h in topology['hosts'] if h['name'] in selected_names},
            'attacker_preferences':preferences,'constraints':scoped}),fixture_files,
            task='honey.files' if len(selections)==1 else 'honey.files.'+selection[0]['name'])
        collected.extend(generated['hosts'])
    files = {'hosts':collected}
    expected_ports = {h["name"]: {(p["port"], p["service"]) for p in h["ports"]} for h in ports["hosts"]}
    actual_ports = {h["name"]: {(p["port"], p["service"]) for p in h["ports"]} for h in files["hosts"]}
    if expected_ports != actual_ports: raise ValueError("Files layer changed host/port allocation")
    # Keep the model's valid files and deterministically repair omitted file
    # arrays so the deployment tree remains executable and auditable.
    for host in files["hosts"]:
        for port in host["ports"]:
            if not port.get("files"):
                port["files"] = [{"path": f"/var/lib/{port['service']}/backup.conf"}]
    vulns = client.complete("You are the Environment Agent Vulnerabilities Layer (Appendix A). Use existing hosts, "
        "ports and files only. For each host output 0-2 short vulnerability entries, each referencing "
        "an existing target_port or target_file. Categories: weak creds, outdated ssh, config leak, "
        "path traversal, RCE, file upload. Avoid repeated type on same host. "
        'Return JSON {"hosts":[{"name":"...","vulnerabilities":[{"type":"...","target_port":22}]}]}.',
        json.dumps({"files": files, "constraints": layer_context(context,'vulnerabilities')}),
        {"hosts": [{"name": h["name"], "vulnerabilities": [{"type": "config leak",
                    "target_port": h["ports"][0]["port"], "target_file": h["ports"][0]["files"][0]["path"]}]}
                    for h in files["hosts"]]}, task="honey.vulnerabilities")
    mapping = {h["name"]: h.get("vulnerabilities", []) for h in vulns["hosts"]}
    repaired = []
    for host in files["hosts"]:
        valid_ports = {p["port"] for p in host["ports"]}
        valid_files = {f["path"] for p in host["ports"] for f in p.get("files", [])}
        values = [v for v in mapping.get(host["name"], []) if
                  v.get("target_port") in valid_ports or v.get("target_file") in valid_files]
        repaired.append({**host, "vulnerabilities": values[:2]})
    return {"hosts": repaired}


def trap_agent(client, honey, preferences, context):
    hosts = [{"name": h["name"], "role": h.get("role"), "files": [f for p in h["ports"] for f in p.get("files", [])]}
             for h in honey["hosts"]]
    loops = client.complete("You are the Guidance Agent Intra-host (Appendix A). Use only existing file paths "
        "for each host. Output 0-3 compact ordered loops per host, each closed back to its first path. "
        'Return JSON {"hosts":[{"name":"...","loops":[["path1","path2","path1"]]}]}.',
        json.dumps({"hosts": hosts, "preferences": preferences, **context}),
        {"hosts": [{"name": h["name"], "loops": [[f["path"] for f in h["files"][:3]] +
            [h["files"][0]["path"]]] if h["files"] else []} for h in hosts]}, task="trap.intra")
    names = [h["name"] for h in hosts][:4]
    steps = [{"host": n, "tier": "low" if i == 0 else "mid" if i < 2 else "high"} for i, n in enumerate(names)]
    chains = client.complete("You are the Guidance Agent Inter-host (Appendix A). For two or more provided hosts, generate 1-3 believable "
        "closed credential chains using provided hosts, low/mid/high tiers, maximum five steps "
        'including return to start. Return a JSON object with this exact root schema: '
        '{"chains":[{"name":"chain-name","steps":[{"host":"provided-host","tier":"low"}]}]}. '
        'For fewer than two provided hosts return {"chains":[]}, because an inter-host chain is impossible. '
        f'Current host count is {len(hosts)}; the only allowed host names are {json.dumps([h["name"] for h in hosts])}. '
        'Hosts appearing in preferences or historical reference_context are not current hosts. '
        'For current host count 1, the chains array MUST be empty even if reference_context contains other hosts. '
        'Never return a top-level array.',
        json.dumps({"hosts": honey["hosts"], "current_host_names":[h['name'] for h in hosts],
                    "preferences": preferences, "traps": loops, "reference_context":context}),
        {"chains": [{"name": "chain-1", "steps": steps + steps[:1]}] if len(names)>=2 else []}, task="trap.inter")
    count = len(chains['chains']) if isinstance(chains.get('chains'),list) else None
    if count is None or not (1 <= count <= 3 if len(names)>=2 else count==0):
        raise ValueError('Inter-host trap response requires a chains array: 1-3 for multiple hosts, 0 for one host')
    normalized_chains = [c for c in chains.get("chains", []) if len(c.get("steps", [])) >= 2]
    normalized_hosts = []
    for host in loops.get("hosts", []):
        host_loops = []
        for loop in host.get("loops", host.get("host_loops", [])):
            # A host with only one artifact cannot form a multi-artifact loop.
            if len(set(loop)) < 2: continue
            if len(loop) >= 2 and loop[0] != loop[-1]: loop = loop + [loop[0]]
            if loop: host_loops.append(loop)
        normalized_hosts.append({"name": host["name"], "host_loops": host_loops})
    return {"hosts": normalized_hosts, "chains": normalized_chains}


def anti_recon(client, honey, traps, protocol_measurements=None):
    surface = copy.deepcopy(honey)
    for host in surface['hosts']:
        host.pop('credential', None)
        host.pop('vulnerabilities', None)
        for port in host['ports']:
            for artifact in port.get('files', []):
                artifact.pop('runtime_links', None)
                artifact['metadata'] = filesystem_metadata(artifact)
                for key in ('provenance','controller_provenance','controller_metadata'):
                    artifact.pop(key, None)
    scope = ('deployed-protocol-measurements'
             if protocol_measurements and protocol_measurements.get('successful_probes', 0) > 0
             else 'materialized-configuration')
    prompt = ("You are DynaHive Anti-Recon reviewer. Audit persona, service banners, "
        "protocol behavior, timing, file metadata, lure density, credential plausibility and cross-host traps. "
        "Do not deploy or modify artifacts. Return JSON risk_score in [0,1], issues as strings, "
        "feedback as concrete constraints for Honey and Trap regeneration. "
        "Trap specifications are controller context; assess fingerprintability only from the observable surface. ")
    if scope == 'deployed-protocol-measurements':
        prompt += ("Deployed protocol measurements are authoritative for banners and response timing. "
                   "Treat banner mismatches, missing listeners, and implausible latency as fingerprint risks.")
    else:
        prompt += ("No live protocol probe is attached; this review covers the materialized configuration only.")
    result = client.complete(prompt,
        json.dumps({"observable_surface": surface, "controller_trap_context": traps,
                    "protocol_measurements": protocol_measurements, "review_scope": scope}),
        {"risk_score": 0.2, "issues": [], "feedback": []}, task="anti_recon")
    result["risk_score"] = float(result["risk_score"])
    if not 0 <= result["risk_score"] <= 1: raise ValueError("Invalid Anti-Recon risk score")
    result['review_scope'] = scope
    return result


def validate_schema(topology, honey):
    expected = {h["name"] for h in topology["hosts"]}
    if {h["name"] for h in honey["hosts"]} != expected or len(honey["hosts"]) != len(expected):
        raise ValueError("Honey tree must cover every topology host exactly once")
    for host in honey["hosts"]:
        if not 1 <= len(host["ports"]) <= 3: raise ValueError("Expected 1-3 ports")
        if len({p["port"] for p in host["ports"]}) != len(host["ports"]): raise ValueError("Duplicate ports")
        for p in host["ports"]:
            if type(p["port"]) is not int or not 1 <= p["port"] <= 65535: raise ValueError("Invalid port")
            if not isinstance(p["service"], str): raise ValueError("Invalid service")
            if not 1 <= len(p.get('files', [])) <= 2: raise ValueError('Expected 1-2 files per port (Appendix A)')
            for f in p.get("files", []):
                path = f["path"]
                if not isinstance(path, str) or ".." in PurePosixPath(path.replace("\\", "/")).parts:
                    raise ValueError("Unsafe artifact path")


def artifacts(honey, traps, topology):
    """Independent deterministic structural CVR inventory, evaluated also for -CC."""
    names = {h["name"] for h in honey["hosts"]}
    topo_names = {h["name"] for h in topology["hosts"]}
    inventory = []
    paths = {h["name"]: {f["path"] for p in h["ports"] for f in p.get("files", [])} for h in honey["hosts"]}
    ports = {h["name"]: {p["port"] for p in h["ports"]} for h in honey["hosts"]}
    for h in honey["hosts"]:
        n = h["name"]
        for p in h["ports"]:
            inventory.append({"id": f"{n}:port:{p['port']}", "violated": n not in topo_names})
            for f in p.get("files", []):
                inventory.append({"id": f"{n}:file:{p['port']}:{f['path']}", "violated": False})
        for i, v in enumerate(h.get("vulnerabilities", [])):
            invalid = (not v.get("target_port") and not v.get("target_file")) or (v.get("target_port") is not None and v["target_port"] not in ports[n]) or (v.get("target_file") is not None and v["target_file"] not in paths[n])
            inventory.append({"id": f"{n}:vulnerability:{i}", "violated": bool(invalid)})
    for h in traps.get("hosts", []):
        for i, loop in enumerate(h.get("host_loops", [])):
            invalid = len(set(loop)) < 2 or loop[0] != loop[-1] or not set(loop).issubset(paths.get(h["name"], set()))
            inventory.append({"id": f"{h['name']}:loop:{i}", "violated": invalid})
    for chain in traps.get("chains", []):
        steps = chain.get("steps", [])
        invalid = len(steps) < 2 or steps[0]["host"] != steps[-1]["host"] or any(s["host"] not in names for s in steps)
        inventory.append({"id": f"chain:{chain['name']}", "violated": invalid})
    return inventory


def consistency_audit(client, topology, honey, traps):
    inventory = artifacts(honey, traps, topology)
    result = client.complete("You are Deception Consistency Checking (Appendix A). Audit service/role "
        "identity, file plausibility, missing vulnerability targets, invalid trap loops, non-closed "
        "credential chains, mixed OS artifacts, lure density. Return JSON summary, issues [strings], "
        "confidence in [0,1], observations [strings]. Issues must identify actual contradictions or "
        "invalid references; report stylistic preferences and lure attractiveness as observations. "
        "Do not invent artifacts. Return artifact_decisions with exactly one {id,violated:boolean,reason} "
        "for EVERY provided inventory item, preserving IDs. A contradictory artifact counts once. "
        "These judgments control generation; they are not the independent final deployment CVR audit.",
        json.dumps({"short_memory": honey, "traps": traps, "topology": topology,
                    "artifact_inventory": inventory,
                    "deterministic_issues": [a["id"] for a in inventory if a["violated"]]}),
        {"summary": "Structural audit", "issues": [a["id"] for a in inventory if a["violated"]],
         "confidence": 1.0, "artifact_decisions": [dict(a,reason='structural fixture') for a in inventory]}, task="consistency.audit")
    result['issues'] = [d['id']+': '+str(d.get('reason','contradiction'))
                        for d in result['artifact_decisions'] if d['violated']]
    return result


# Paper/checklist names. honey_agent / trap_agent / anti_recon remain as aliases.
generate_environment = honey_agent
generate_guidance = trap_agent
review_surface = anti_recon
