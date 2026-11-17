"""DynaHive_frame agents aligned with the PDF + user clarifications.

(a) Planner — TAPAS stage statistics/sequence, progress & uncertainty,
    actions & outcomes (Success/Failure/Unknown)

(b) Agent Coordination
    * Environment Agent — honeynet state/goals, host configs, lure surface,
      credential links (AgentLure-style surface as internal capability)
    * Guidance Agent — trap planning: Select next / Fallback / Path needed;
      Probe→Login→Read objective; intra-host traps & inter-host paths
    * Review Agent — concealment, fingerprint audit → risk d_u + stealth Δ_u

Response-layer cache vs LLM routing is NOT Guidance; see ResponseRouter.
"""
from __future__ import annotations

import copy
import math
import re
from pathlib import PurePosixPath

from .anti_fingerprint import (
    default_ar_constraints,
    harden_honey_surface,
    resolve_directory_file_conflicts,
)
from .environment_normalize import normalize_environment
from .tapas_stage import STAGE_LABELS, TapasStageClassifier, map_distribution

# Response-layer only: high-volume / low-aggression → cache; complex → LLM.
CACHE_SAFE_COMMANDS = {
    'ls', 'cat', 'head', 'tail', 'cd', 'pwd', 'id', 'whoami', 'uname', 'hostname',
    'echo', 'printf', 'env', 'true', 'false', 'clear',
    'ps', 'date', 'uptime', 'who', 'w', 'last', 'stat', 'ss', 'ip',
    'ifconfig', 'netstat', 'which', 'type', 'mount', 'df', 'free', 'getent',
    'basename', 'dirname', 'groups', 'history', 'command', 'sleep',
    'grep', 'find', 'sudo', 'crontab', 'systemctl', 'ssh', 'scp', 'nc', 'wc', 'sort', 'uniq',
    'cut', 'tr', 'awk', 'sed', 'file', 'md5sum', 'sha256sum', 'chmod', 'chown',
    'touch', 'mkdir', 'rm', 'cp', 'mv', 'ln', 'export', 'set', 'unset', 'test', '[',
}

_SHELL_CONTROL_RE = re.compile(
    r'(^|[\s;|&])(for|while|until|if|case|function|do|done|then|else|elif|fi|esac)([\s;|&]|$)'
)
# Only force LLM for substitutions / heavy tools — NOT for simple '|' pipelines
# of cache-safe commands (World already executes those).
_COMPLEX_MARKERS = (
    '$(', '`', '>>', '<<',
    'python', 'perl', 'curl', 'wget', 'nmap', 'ssh ',
)


def _mask_quoted(text):
    out, quote = [], None
    for ch in text or '':
        if quote:
            out.append(' ')
            if ch == quote:
                quote = None
            continue
        if ch in {'"', "'"}:
            quote = ch
            out.append(' ')
            continue
        out.append(ch)
    return ''.join(out)


def _first_token(command):
    text = (command or '').strip()
    if not text:
        return ''
    token = text.split(maxsplit=1)[0]
    if '/' in token:
        token = token.rsplit('/', 1)[-1]
    return token


def classify_outcome(output, handled=True):
    text = (output or '').lower()
    if not text.strip():
        return 'unknown'
    fail_markers = (
        'command not found', 'no such file', 'permission denied', 'cannot access',
        'not allowed', 'invalid', 'syntax error', 'failed', 'error:',
    )
    if any(m in text for m in fail_markers):
        return 'failure'
    if handled is False and not text.strip():
        return 'unknown'
    return 'success'


class PlannerState:
    def __init__(self):
        self.stage_counts = {i: 0 for i in range(1, 6)}
        self.stage_sequence = []
        self.outcomes_hist = []
        self.progress = 0.0
        self.uncertainty = 1.0
        self.last_outcome = 'unknown'
        self.last_stage = None
        self.tapas_backend = None

    def to_dict(self):
        return {
            'stage_counts': dict(self.stage_counts),
            'stage_sequence': list(self.stage_sequence[-20:]),
            'stage_labels': {str(i): STAGE_LABELS[i] for i in range(1, 6)},
            'progress': self.progress,
            'uncertainty': self.uncertainty,
            'last_outcome': self.last_outcome,
            'last_stage': self.last_stage,
            'outcomes_hist': list(self.outcomes_hist[-20:]),
            'tapas_backend': self.tapas_backend,
        }


class Planner:
    """(a) Planner: TAPAS stage stats/sequence + progress/uncertainty + outcomes."""

    def __init__(self, tapas_classifier=None):
        self.tapas = tapas_classifier or TapasStageClassifier()
        self.state = PlannerState()

    def update(self, telemetry_events, last_output=None, last_handled=True):
        events = list(telemetry_events or [])
        classified = self.tapas.classify(events) if events else {
            'events': [], 'stage_counts': {i: 0 for i in range(1, 6)},
            'model_backend': getattr(self.tapas, 'model_backend', None),
        }
        counts = classified.get('stage_counts') or {}
        normalized = {i: 0 for i in range(1, 6)}
        for key, value in counts.items():
            try:
                idx = int(key)
            except Exception:
                continue
            if 1 <= idx <= 5:
                normalized[idx] = int(value)
        if not any(normalized.values()) and events:
            for ev in classified.get('events') or events:
                if not isinstance(ev, dict):
                    continue
                stage = (ev.get('tapas_compatible') or {}).get('stage') or ev.get('intent_stage')
                if stage in normalized:
                    normalized[stage] += 1
        self.state.stage_counts = normalized
        sequence = []
        for ev in events[-30:]:
            if not isinstance(ev, dict):
                continue
            stage = (ev.get('tapas_compatible') or {}).get('stage') or ev.get('intent_stage')
            if stage:
                sequence.append(int(stage))
        self.state.stage_sequence = sequence
        self.state.last_stage = sequence[-1] if sequence else None
        max_stage = max(sequence) if sequence else 0
        self.state.progress = round(max_stage / 5.0, 4) if max_stage else 0.0
        dist = map_distribution(events) if events else [0.2] * 5
        entropy = -sum(p * math.log(p + 1e-12) for p in dist) / math.log(5)
        if last_output is not None:
            outcome = classify_outcome(last_output, handled=last_handled)
            self.state.last_outcome = outcome
            self.state.outcomes_hist.append(outcome)
        unknown_rate = (
            self.state.outcomes_hist.count('unknown') / len(self.state.outcomes_hist)
            if self.state.outcomes_hist else 0.5
        )
        self.state.uncertainty = round(min(1.0, 0.6 * entropy + 0.4 * unknown_rate), 4)
        self.state.tapas_backend = classified.get('model_backend')
        return self.state

    def make_task_plan(self, honey, traps, topology, observations=None, candidate_changed=False):
        """Paper Planner task assignment: Environment, then Guidance, then Review."""
        from .guidance_search import host_files
        observations = observations or []
        files = host_files(honey or {})
        hosts = [h.get("name") for h in (topology or {}).get("hosts") or []]
        entry = hosts[0] if hosts else None
        reconstruction = {
            "identity": None,
            "hosts": list({e.get("host") for e in observations if e.get("host")}),
            "seen": [e.get("path") for e in observations if e.get("path")],
            "tried": [e.get("command") or e.get("action") for e in observations],
            "capabilities": [],
        }
        if self.state.last_outcome == "success":
            reconstruction["capabilities"].append("last_command_succeeded")
        gaps = []
        if entry and not files.get(entry):
            gaps.append({"host": entry, "need": "role-consistent ambient files"})
        has_loops = any((h.get("host_loops") or h.get("loops")) for h in (traps or {}).get("hosts") or [])
        has_chain = bool((traps or {}).get("chains"))
        invoke_environment = bool(gaps) or not (honey or {}).get("hosts")
        invoke_guidance = (not has_loops and not has_chain) or (
            self.state.last_outcome == "failure" and not has_chain
        )
        invoke_review = candidate_changed or invoke_environment or invoke_guidance
        retain = (
            (not invoke_environment)
            and (not invoke_guidance)
            and (not candidate_changed)
            and self.state.last_outcome in {"success", "unknown"}
        )
        if retain:
            invoke_review = False
        return {
            "reconstruction": reconstruction,
            "capability_gaps": gaps,
            "projection": {
                "objective": "Obtain operational archive material from the decoy segment.",
                "next_actions": reconstruction["tried"][-3:],
                "uncertainty": self.state.uncertainty,
                "evidence": f"stage={self.state.last_stage} outcome={self.state.last_outcome}",
            },
            "G": "Obtain operational archive material reachable from the entry host.",
            "affected": hosts,
            "constraints": ["do not rewrite exposed facts"],
            "invoke_environment": invoke_environment and not retain,
            "invoke_guidance": invoke_guidance and not retain,
            "invoke_review": invoke_review and not retain,
            "retain": retain,
            "missing_evidence": [] if observations else ["no session activity yet"],
        }


class EnvironmentAgent:
    """Honeynet state/goals, host configs, lure surface, credential links."""

    def __init__(self, topology, honey, traps, entry_host):
        self.topology = topology or {'hosts': []}
        self.honey = normalize_environment(
            harden_honey_surface(copy.deepcopy(honey or {'hosts': []}), self.topology),
            self.topology,
        )
        self.traps = copy.deepcopy(traps or {'hosts': [], 'chains': []})
        self.entry_host = entry_host
        self.route = {'host': entry_host, 'reason': 'external_entry'}
        self.credential_links = self._extract_links()

    def _extract_links(self):
        links = []
        for host in self.honey.get('hosts', []):
            for port in host.get('ports', []):
                for artifact in port.get('files', []):
                    for target in artifact.get('credential_targets') or []:
                        links.append({
                            'from_host': host['name'],
                            'path': artifact.get('path'),
                            'target': target,
                        })
        return links

    def surface_snapshot(self):
        return {
            'host': self.route['host'],
            'route_reason': self.route['reason'],
            'honey_hosts': [h['name'] for h in self.honey.get('hosts', [])],
            'credential_links': self.credential_links[:12],
            'services': [
                {'host': h['name'], 'port': p.get('port'), 'service': p.get('service')}
                for h in self.honey.get('hosts', []) for p in h.get('ports', [])
            ][:20],
        }

    def ensure_entry_route(self):
        names = {h['name'] for h in self.topology.get('hosts', [])}
        host = self.entry_host
        if host not in names and names:
            ranked = sorted(
                self.topology['hosts'],
                key=lambda h: 0 if h.get('role') in {'firewall', 'bastion', 'public-web'} else 1,
            )
            host = ranked[0]['name']
        self.route = {'host': host, 'reason': 'external_entry'}
        return self.route

    def apply_stealth(self, constraints):
        self.honey = harden_honey_surface(self.honey, self.topology)
        self.honey = resolve_directory_file_conflicts(self.honey)
        self.honey['_stealth_constraints'] = list(constraints or [])[:12]
        self.credential_links = self._extract_links()
        return self.honey

    def host_files(self, host_name):
        for host in self.honey.get('hosts', []):
            if host['name'] != host_name:
                continue
            return [f.get('path') for p in host.get('ports', []) for f in p.get('files', []) if f.get('path')]
        return []


class GuidanceAgent:
    """Trap planning (PDF AgentTrap / Guidance): Select next, Fallback, Path needed.

    Plans intra-host loops and inter-host credential paths. Can call LLM trap_agent
    when a client is available; otherwise builds deterministic traps from the surface.
    """

    def __init__(self, client=None):
        self.client = client
        self.traps = {'hosts': [], 'chains': []}
        self.cursor = {'host_loop_index': 0, 'chain_index': 0, 'step_index': 0}
        self.last_plan = None

    def _deterministic_traps(self, honey, entry_host):
        hosts_out = []
        names = []
        # Prefer the staged lure chain so attackers must issue many atomic reads.
        for host in honey.get('hosts', []):
            names.append(host['name'])
            files = [f.get('path') for p in host.get('ports', []) for f in p.get('files', []) if f.get('path')]
            files = list(dict.fromkeys(files))
            # Build host-local chain using real username home when available.
            home_notes = [p for p in files if p.endswith('/notes.txt')]
            chain = []
            if home_notes:
                chain.append(home_notes[0])
            for p in ('/etc/monit/monitrc', '/etc/monit/conf.d/sshd', '/etc/ops/maintenance.conf'):
                chain.append(p)
            admin_notes = [p for p in files if p.endswith('id_rsa.bak.notes')]
            admin_key = [p for p in files if p.endswith('id_rsa.bak') and not p.endswith('.notes')]
            if admin_notes:
                chain.append(admin_notes[0])
            if admin_key:
                chain.append(admin_key[0])
            loops = []
            if len(chain) >= 2:
                loops.append(chain)
            elif len(files) >= 2:
                loop = files[:3]
                if loop[0] != loop[-1]:
                    loop = loop + [loop[0]]
                loops.append(loop)
            hosts_out.append({'name': host['name'], 'host_loops': loops})
        chains = []
        if len(names) >= 2:
            # Prefer entry host as chain start.
            ordered = [entry_host] + [n for n in names if n != entry_host]
            ordered = [n for n in ordered if n in names][:4]
            steps = [
                {'host': n, 'tier': 'low' if i == 0 else 'mid' if i < 2 else 'high'}
                for i, n in enumerate(ordered)
            ]
            if len(steps) >= 2:
                steps = steps + [dict(steps[0])]
                chains.append({'name': 'ops-credential-loop', 'steps': steps})
        return {'hosts': hosts_out, 'chains': chains}

    def plan_traps(self, honey, entry_host, planner_state=None, preferences=None, context=None,
                   observations=None, objective=None):
        preferences = preferences or {}
        context = context or {}
        if planner_state is not None:
            context = {
                **context,
                'planner_progress': planner_state.progress,
                'planner_stage': planner_state.last_stage,
                'planner_uncertainty': planner_state.uncertainty,
            }
        from .guidance_search import search
        goal = objective or context.get("G") or "Obtain operational archive material reachable from the entry host."
        result = search(
            honey, observations or [], goal, entry_host, client=self.client,
        )
        traps = result.get("traps") or self._deterministic_traps(honey, entry_host)
        self.traps = traps
        self.cursor = {'host_loop_index': 0, 'chain_index': 0, 'step_index': 0}
        self.last_plan = {
            'source': result.get('source') or 'algorithm1',
            'traps': traps,
            'chain': result.get('chain'),
            'diagnostics': result.get('diagnostics') or [],
            'context': context,
            'preferences': preferences,
        }
        return traps

    def _active_loop(self, host_name):
        for host in self.traps.get('hosts') or []:
            if host.get('name') != host_name:
                continue
            loops = host.get('host_loops') or host.get('loops') or []
            if not loops:
                return None
            idx = self.cursor['host_loop_index'] % len(loops)
            return loops[idx]
        return None

    def select_next(self, command, entry_host, planner_state=None):
        """Select next trap step, or Fallback / Path needed."""
        text = (command or '').lower()
        loop = self._active_loop(entry_host)
        chains = self.traps.get('chains') or []

        # Probe / login / read-objective phases inferred lightly from command.
        phase = 'probe'
        if any(tok in text for tok in ('ssh ', 'login', 'passwd', 'sudo')):
            phase = 'login'
        if any(tok in text for tok in ('cat ', 'head ', 'tail ', 'less ', 'archive', 'secret', 'key')):
            phase = 'read_objective'

        decision = {
            'action': 'select_next',
            'phase': phase,
            'path_needed': False,
            'fallback': False,
            'next_path': None,
            'next_host': entry_host,
            'validated': False,
            'reason': '',
        }

        if loop:
            # Advance along intra-host trap loop.
            step = self.cursor['step_index'] % len(loop)
            decision['next_path'] = loop[step]
            decision['reason'] = 'intra_host_loop'
            # If attacker already reads current path, advance cursor.
            if decision['next_path'] and decision['next_path'] in (command or ''):
                self.cursor['step_index'] = step + 1
                if self.cursor['step_index'] >= len(loop):
                    self.cursor['step_index'] = 0
                    self.cursor['host_loop_index'] += 1
                decision['validated'] = True
                decision['next_path'] = loop[self.cursor['step_index'] % len(loop)]
                decision['reason'] = 'intra_host_loop_advanced'
        elif chains and (planner_state is None or (planner_state.last_stage or 0) >= 2):
            chain = chains[self.cursor['chain_index'] % len(chains)]
            steps = chain.get('steps') or []
            if steps:
                step = steps[self.cursor['step_index'] % len(steps)]
                decision['next_host'] = step.get('host') or entry_host
                decision['next_path'] = None
                decision['reason'] = f"inter_host_chain:{chain.get('name')}"
                decision['path_needed'] = decision['next_host'] != entry_host
                if phase == 'login' and decision['path_needed']:
                    decision['fallback'] = False
                    decision['action'] = 'path_needed'
        else:
            decision['action'] = 'fallback'
            decision['fallback'] = True
            decision['reason'] = 'no_trap_ready'
            # Fallback: expose a mundane local file hint if any.
            files = []
            for host in self.traps.get('hosts') or []:
                if host.get('name') == entry_host:
                    for loop in host.get('host_loops') or []:
                        files.extend(loop)
            decision['next_path'] = files[0] if files else None

        self.last_plan = {**(self.last_plan or {}), 'select_next': decision}
        return decision


class ReviewAgent:
    """Concealment / fingerprint audit → risk d_u + stealth constraints Δ_u."""

    def __init__(self, client=None, review_every=3):
        self.client = client
        self.review_every = max(1, int(review_every))
        self._counter = 0
        self.last_review = {
            'risk_score': 0.2,
            'issues': [],
            'stealth_constraints': list(default_ar_constraints()),
            'source': 'default',
        }

    def _deterministic_issues(self, honey):
        issues = []
        for host in (honey or {}).get('hosts', []):
            paths = []
            for port in host.get('ports', []):
                for artifact in port.get('files', []):
                    path = artifact.get('path') or ''
                    paths.append(path)
                    meta = artifact.get('metadata') or {}
                    mtime = str(meta.get('mtime') or '')
                    if len(mtime) >= 7 and mtime.startswith('2024-') and mtime[5:7] in {'10', '11', '12'}:
                        issues.append(f'future_or_lab_clock_mtime:{path}')
            for path in paths:
                parent = str(PurePosixPath(path).parent)
                if parent in paths:
                    issues.append(f'directory_file_collision:{parent}')
        return issues

    def review(self, honey, traps, force=False, topology=None, freeze=None):
        self._counter += 1
        if not force and (self._counter % self.review_every) != 0:
            return self.last_review
        from .review_loop import review_until_pass
        topo = topology or {"hosts": honey.get("hosts") or []}
        report = review_until_pass(
            honey, traps or {"hosts": [], "chains": []}, topo,
            client=self.client, freeze=freeze,
        )
        self.last_review = {
            "risk_score": report.get("risk_score", 0.2),
            "issues": report.get("issues") or [i.get("kind") for i in report.get("blocking") or []],
            "stealth_constraints": report.get("stealth_constraints") or list(default_ar_constraints()),
            "source": report.get("source"),
            "deployable": report.get("deployable", False),
            "blocking": report.get("blocking") or [],
            "uncertain": report.get("uncertain") or [],
            "honey": report.get("honey"),
            "traps": report.get("traps"),
            "repairs": report.get("repairs", 0),
        }
        return self.last_review


class ResponseRouter:
    """Response-layer routing (NOT Guidance): cache vs LLM.

    High-volume / low-aggression / fingerprint-sensitive probes → cache (World).
    Complex commands needing long-context shell memory → LLM.
    """

    def __init__(self, cache_commands=None):
        self.cache_commands = set(cache_commands or CACHE_SAFE_COMMANDS)

    def _needs_long_context(self, command):
        text = (command or '').strip()
        if not text:
            return False
        # Simple for-loops are expanded on the World/cache path.
        if re.match(r'^\s*for\s+\w+\s+in\s+.+\s*;\s*do\s+.+\s*;\s*done\s*$', text, re.S):
            return False
        scan = _mask_quoted(text)
        if _SHELL_CONTROL_RE.search(scan):
            return True
        if any(m in scan for m in _COMPLEX_MARKERS):
            return True
        if scan.count(';') >= 3:
            return True
        return False

    def _all_tokens_cacheable(self, command):
        """True when every simple command atom is cache-safe (ignore redirections)."""
        scan = _mask_quoted(command or '')
        # Normalize weak chains for token inspection only.
        scan = scan.replace('&&', ';').replace('||', ';').replace('|', ';')
        for part in scan.split(';'):
            part = part.strip()
            if not part:
                continue
            # Drop redirection tails: cmd 2>/dev/null
            cleaned = []
            for tok in part.split():
                if tok.startswith('2>') or tok.startswith('>') or tok.startswith('<'):
                    break
                cleaned.append(tok)
            if not cleaned:
                continue
            token = cleaned[0]
            if '/' in token:
                token = token.rsplit('/', 1)[-1]
            if token not in self.cache_commands:
                return False
        return True

    def route(self, command, review=None, trap_decision=None):
        token = _first_token(command)
        text = (command or '').strip()
        # World expands simple for-loops; always keep them on cache.
        if re.match(r'^\s*for\s+\w+\s+in\s+.+\s*;\s*do\s+.+\s*;\s*done\s*$', text, re.S):
            return {
                'source': 'cache',
                'prefer_llm': False,
                'reason': 'simple_for_loop_world_expand',
                'token': token,
            }
        force_llm = False
        if review and float(review.get('risk_score') or 0) >= 0.55:
            # High fingerprint risk: still prefer cache for safe probes; LLM only
            # when the line truly needs long-context shell semantics.
            force_llm = self._needs_long_context(command)
        if self._needs_long_context(command) and not self._all_tokens_cacheable(command):
            force_llm = True
        # Simple chains / pipelines of cache-safe tools stay on World cache.
        if (not force_llm) and self._all_tokens_cacheable(command):
            return {
                'source': 'cache',
                'prefer_llm': False,
                'reason': 'high_volume_low_aggression_chain',
                'token': token,
            }
        if force_llm or token not in self.cache_commands:
            return {
                'source': 'llm',
                'prefer_llm': True,
                'reason': 'long_context_or_uncovered',
                'token': token,
            }
        return {
            'source': 'cache',
            'prefer_llm': False,
            'reason': 'high_volume_low_aggression',
            'token': token,
        }


class Coordinator:
    """Planner → Environment / Guidance / Review, plus response-layer router."""

    def __init__(self, topology, honey, traps, entry_host, client=None, journal=None,
                 tapas_classifier=None, review_every=3, freeze=None):
        self.journal = journal
        self.client = client
        self.freeze = freeze
        self.planner = Planner(tapas_classifier=tapas_classifier)
        self.environment = EnvironmentAgent(topology, honey, traps, entry_host)
        self.guidance = GuidanceAgent(client=client)
        self.review_agent = ReviewAgent(client=client, review_every=review_every)
        self.router = ResponseRouter()
        self.environment.ensure_entry_route()
        self.last_task_plan = None
        # Initial trap plan from current surface (Guidance after Environment).
        self.guidance.plan_traps(
            self.environment.honey, self.environment.route['host'], self.planner.state)
        reviewed = self.review_agent.review(
            self.environment.honey, self.guidance.traps, force=True,
            topology=self.environment.topology, freeze=self.freeze)
        if reviewed.get("deployable") and reviewed.get("honey") is not None:
            self.environment.honey = reviewed["honey"]
            if reviewed.get("traps") is not None:
                self.guidance.traps = reviewed["traps"]
        self.step_count = 0

    def step(self, command, telemetry_events, last_output=None, last_handled=True):
        self.step_count += 1
        planner_state = self.planner.update(
            telemetry_events, last_output=last_output, last_handled=last_handled)
        plan = self.planner.make_task_plan(
            self.environment.honey, self.guidance.traps, self.environment.topology,
            observations=telemetry_events, candidate_changed=False,
        )
        self.last_task_plan = plan
        review = self.review_agent.last_review
        if plan.get("invoke_environment") and self.client is not None:
            from .agents import generate_environment
            generated = generate_environment(
                self.client, self.environment.topology, {},
                {"baseline_honey": self.environment.honey, "review_constraints": (review or {}).get("stealth_constraints")},
            )
            if self.freeze is not None:
                generated = self.freeze.protect(generated)
            self.environment.honey = generated
            self.environment.credential_links = self.environment._extract_links()
        if plan.get("invoke_guidance"):
            self.guidance.plan_traps(
                self.environment.honey, self.environment.route["host"], planner_state,
                observations=telemetry_events, objective=plan.get("G"),
            )
        if plan.get("invoke_review") or plan.get("invoke_guidance") or plan.get("invoke_environment"):
            review = self.review_agent.review(
                self.environment.honey, self.guidance.traps, force=True,
                topology=self.environment.topology, freeze=self.freeze)
            if review.get("deployable"):
                if review.get("honey") is not None:
                    self.environment.honey = review["honey"]
                if review.get("traps") is not None:
                    self.guidance.traps = review["traps"]
            elif float(review.get("risk_score") or 0) >= 0.5:
                self.environment.apply_stealth(review.get("stealth_constraints"))
        route = self.environment.ensure_entry_route()
        trap_decision = self.guidance.select_next(
            command, route['host'], planner_state=planner_state)
        response_route = self.router.route(
            command, review=review, trap_decision=trap_decision)
        style_hints = list(review.get('stealth_constraints') or [])[:6]
        if trap_decision.get('next_path'):
            style_hints.append(
                f"Trap guidance next_path={trap_decision['next_path']} "
                f"phase={trap_decision.get('phase')}"
            )
        payload = {
            'event': 'frame_controller_step',
            'step': self.step_count,
            'command': command,
            'planner': planner_state.to_dict(),
            'task_plan': plan,
            'environment': self.environment.surface_snapshot(),
            'guidance_trap': trap_decision,
            'review': {
                'risk_score': review.get('risk_score'),
                'issues': (review.get('issues') or [])[:8],
                'stealth_constraints': (review.get('stealth_constraints') or [])[:8],
                'source': review.get('source'),
            },
            'response_route': response_route,
            'style_hints': style_hints,
        }
        if self.journal:
            self.journal.append(payload)
        return {
            'planner': planner_state,
            'environment': self.environment,
            'guidance': trap_decision,
            'traps': self.guidance.traps,
            'review': review,
            'route': route,
            'response_route': response_route,
            'style_hints': style_hints,
            # Convenience for LiveSession: prefer_llm from response router.
            'prefer_llm': bool(response_route.get('prefer_llm')),
        }


FrameController = Coordinator
