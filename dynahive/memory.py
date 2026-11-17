from __future__ import annotations

import hashlib
import json
import math
import time

from .runtime import write_json
from .tapas_stage import stage_for_event


class BiLevelMemory:
    def __init__(self, root, enabled=True, capacity=64, eviction='FIFO', promotion_every=1):
        if type(capacity) is not int or capacity < 1 or type(promotion_every) is not int or promotion_every < 1:
            raise ValueError('Memory capacity and promotion interval must be positive integers')
        if eviction not in {'FIFO', 'LRU', 'relevance-scored'}:
            raise ValueError('Unknown memory eviction policy')
        self.enabled, self.capacity = enabled, capacity
        self.eviction, self.promotion_every = eviction, promotion_every
        self.path = root / "ltm.json"
        self.entries = json.loads(self.path.read_text(encoding="utf-8")) if enabled and self.path.exists() else []
        self.pending_path = root / 'stm_pending.json'
        self.pending = json.loads(self.pending_path.read_text(encoding='utf-8')) if enabled and self.pending_path.exists() else []
        self.stm = {}

    def retrieve(self, roles, limit=3):
        ranked = sorted(self.entries, key=lambda e: e["utility"] * e["anti_recon_pass_rate"] *
            math.exp(-(time.time() - e["timestamp"]) / (30 * 86400)) * (1 + len(set(e["roles"]) & roles)), reverse=True)
        selected = ranked[:limit] if self.enabled else []
        for entry in selected:
            entry['last_access'] = time.time()
            entry['retrieval_count'] = entry.get('retrieval_count', 0)+1
        if selected:
            write_json(self.path, self.entries)
        return selected

    def mode(self, distribution, topology_hash, theta=0.15):
        prev = self.entries[-1] if self.entries else None
        if not self.enabled or not prev or prev["topology_hash"] != topology_hash: return "initialization"
        kl = sum(p * math.log(p / q) for p, q in zip(distribution, prev["stage_distribution"]))
        return "finetune" if kl <= theta else "initialization"

    def distill(self, strategy, roles, topology_hash, distribution, utility, passed,
                utility_source='observed_dsr'):
        if not self.enabled: return
        # Paper LTM utility is historical defensive utility. Diagnostic retention
        # proxies are rejected so memory ranking cannot be gamed by unfinished
        # development runs.
        if utility_source != 'observed_dsr':
            raise ValueError('LTM utility must use observed_dsr; diagnostic proxies are rejected')
        if utility is None or type(utility) not in (int, float) or not 0 <= float(utility) <= 1:
            raise ValueError('Observed DSR utility must be a finite rate in [0,1]')
        digest = hashlib.sha256(json.dumps(strategy, sort_keys=True).encode()).hexdigest()
        entry = {"hash": digest, "timestamp": time.time(), "roles": sorted(roles), "topology_hash": topology_hash,
            "stage_distribution": distribution, "utility": float(utility),
            "anti_recon_pass_rate": float(passed), "strategy": strategy,
            "utility_source": utility_source}
        self.pending.append(entry)
        if len(self.pending) < self.promotion_every:
            write_json(self.pending_path, self.pending)
            return
        for promoted in self.pending:
            self.entries = [e for e in self.entries if e['hash'] != promoted['hash']]+[promoted]
        self.pending = []
        write_json(self.pending_path, self.pending)
        while len(self.entries) > self.capacity:
            if self.eviction == 'FIFO':
                index = 0
            elif self.eviction == 'LRU':
                index = min(range(len(self.entries)),key=lambda i:self.entries[i].get('last_access',self.entries[i]['timestamp']))
            else:
                # The paper specifies relevance-scored eviction but no formula.
                # Disclosed engineering choice: utility, review pass rate, reuse
                # count and recency; this internal score is not a paper metric.
                def score(e):
                    return e['utility']*e['anti_recon_pass_rate']*(1+e.get('retrieval_count',0))*math.exp(
                        -(time.time()-e['timestamp'])/(30*86400))
                index = min(range(len(self.entries)),key=lambda i:score(self.entries[i]))
            self.entries.pop(index)
        write_json(self.path, self.entries)


def stage_distribution(events):
    counts = [1.0] * 5
    for event in events:
        stage = stage_for_event(event)
        if stage: counts[stage - 1] += 1
    return [c / sum(counts) for c in counts]
