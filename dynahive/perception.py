from __future__ import annotations

import copy
import ipaddress
import json
from collections import Counter, defaultdict
from pathlib import Path

from .tapas_stage import (
    ACTION_TO_TACTIC,
    STAGE_LABELS,
    TACTIC_TO_STAGE,
    TapasStageClassifier,
    stage_for_event,
)

# Backward-compatible aliases. Prefer stage_for_event / TapasStageClassifier.
STAGES = {action: TACTIC_TO_STAGE[tactic] for action, tactic in ACTION_TO_TACTIC.items()}
TACTICS = dict(TACTIC_TO_STAGE)


def stage_for(event):
    """Resolve a stage via the disclosed TAPAS-compatible local mapping."""
    return stage_for_event(event)


def shadow_topology(topology, subnet="10.77.0.0/24"):
    result = copy.deepcopy(topology)
    names = [h["name"] for h in result["hosts"]]
    switches = [s["id"] for s in result["switches"]]
    if len(set(names + switches)) != len(names + switches): raise ValueError("Duplicate identifiers")
    network = ipaddress.ip_network(subnet)
    if len(names) + 10 >= network.num_addresses: raise ValueError("Subnet too small")
    assigned=set()
    requester=ipaddress.ip_address(result.get('network',{}).get('attacker_ip','10.77.0.250'))
    declared={ipaddress.ip_address(h['ip']) for h in result['hosts'] if h.get('ip')}
    if len(declared)!=sum(bool(h.get('ip')) for h in result['hosts']):
        raise ValueError('Duplicate declared host addresses')
    for index, host in enumerate(result["hosts"], 10):
        address=ipaddress.ip_address(host['ip']) if host.get('ip') else network.network_address+index
        if not host.get('ip'):
            while address in declared or address in assigned or address==requester:address+=1
        if address not in network or address in {network.network_address,network.broadcast_address,requester}:
            raise ValueError('Host address is outside usable experiment scope')
        assigned.add(address)
        host.update(ip=str(address), shadow_of=host["name"], mininet_name=f"h{index - 9}")
    for link in result["links"]:
        if len(link["endpoints"]) != 2 or not set(link["endpoints"]).issubset(set(names + switches)):
            raise ValueError(f"Invalid link: {link}")
    result.update(alignment={n: n for n in names}, subnet=subnet)
    return result


def stage_statistics(topology, events, classifier=None):
    """Only typed stage counts and trusted host identities leave perception."""
    classified = None
    if classifier is not None:
        classified = classifier.classify(events)
        events = classified['events']
    counts = defaultdict(Counter)
    for event in events:
        stage = stage_for(event)
        if stage: counts[event.get("host", "unknown")][f"stage{stage}"] += 1
    hosts = [{"host_id": h["name"], "role": h.get("role", "unknown"),
              "stage_counts": {f"stage{i}": counts[h["name"]][f"stage{i}"] for i in range(1, 6)},
              "stage_labels": {f"stage{i}": STAGE_LABELS[i] for i in range(1, 6)}} for h in topology["hosts"]]
    return hosts, classified


def perceive(client, topology, events, classifier=None):
    if classifier is None:
        try:
            classifier = TapasStageClassifier()
        except FileNotFoundError:
            classifier = None
    hosts, classified = stage_statistics(topology, events, classifier=classifier)
    fallback = {"attacker_profile": {"aggressiveness": "low", "exploration_depth": "shallow",
        "primary_protocols": [], "target_services": [], "privilege_seeking": "none", "lateral_movement": "none",
        "overall_assessment": "No prior telemetry."}, "per_host_summary": []}
    payload = {
        "session_id": "prior-telemetry",
        "hosts": hosts,
        "stage_source": {
            "mapper": "tapas_stage.disclosed_local_mapping",
            "model_backend": None if classified is None else classified['model_backend'],
            "disclosure": (
                "Downstream receives structured stage statistics only. "
                "ATT&CK/stage labels come from the disclosed local mapping over "
                "TAPAS-compatible typed events; TAPAS itself is a "
                "benign/malicious subgraph detector."
            ),
        },
    }
    from . import prompts as _prompts
    fallback = {
        "facts": [],
        "access": {"hosts": [], "capabilities": []},
        "environment_summary": {"hosts": hosts},
        "history_links": [],
        "inferences": [],
        "unresolved": [],
        "attacker_profile": fallback["attacker_profile"],
        "per_host_summary": fallback["per_host_summary"],
    }
    return client.complete(_prompts.perception_system(),
        json.dumps(payload), fallback, task="perception")


def load_events(path):
    p = Path(path)
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()] if p.exists() else []
