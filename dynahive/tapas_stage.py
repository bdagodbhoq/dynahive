"""TAPAS-compatible stage perception with disclosed local ATT&CK mapping.

DynaHive §4.2.1 cites TAPAS as a provenance-graph ATT&CK tactic classifier.
The author artifact (USENIX Security 2025) outputs benign/malicious subgraph
alerts, not native ATT&CK tactic labels. This module therefore:

1. Converts lab/audit-like events into a TAPAS-compatible event schema.
2. Optionally scores maliciousness with the author LSTM/GraphSAGE weights when
   torch (+ torch_geometric for GraphSAGE) is available.
3. Applies a disclosed local mapping from ATT&CK tactics / event types onto the
   five paper body stages. That mapping is a DynaHive reconstruction choice,
   not a native TAPAS output head.

Stage truth for SCR remains independent target-side observation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

# Paper body Table: ATT&CK tactics -> canonical intrusion stages.
TACTIC_TO_STAGE = {
    'reconnaissance': 1,
    'discovery': 1,
    'initial-access': 2,
    'execution': 2,
    'privilege-escalation': 3,
    'credential-access': 3,
    'lateral-movement': 4,
    'collection': 5,
    'exfiltration': 5,
    'impact': 5,
}

# Lab action vocabulary used by the reconstructed runtime, mapped to the same
# five stages. This is the disclosed local event->stage bridge over TAPAS-
# compatible typed events; it is not a native TAPAS classifier head.
ACTION_TO_TACTIC = {
    'scan': 'reconnaissance',
    'probe': 'discovery',
    'exploit': 'initial-access',
    'login': 'initial-access',
    'privilege': 'privilege-escalation',
    'lateral': 'lateral-movement',
    'objective': 'collection',
    'read': 'collection',
    'list': 'discovery',
}

# TAPAS darpa.py event_map subset used when ingesting CDM-like audit events.
TAPAS_EVENT_TO_TACTIC = {
    'EVENT_ACCEPT': 'discovery',
    'EVENT_CONNECT': 'lateral-movement',
    'EVENT_EXECUTE': 'execution',
    'EVENT_EXIT': 'discovery',
    'EVENT_READ': 'collection',
    'EVENT_RECVFROM': 'discovery',
    'EVENT_RECVMSG': 'discovery',
    'EVENT_SENDTO': 'exfiltration',
    'EVENT_SENDMSG': 'exfiltration',
    'EVENT_WRITE': 'impact',
}

STAGE_LABELS = {
    1: 'Scanning',
    2: 'Exploitation',
    3: 'Privilege Escalation',
    4: 'Lateral Movement',
    5: 'Action on Objectives',
}

DEFAULT_ARTIFACT_ROOT = Path(__file__).resolve().parents[1] / 'upstream' / 'TAPAS_selected'


def verify_tapas_artifacts(root=None):
    """Confirm selective author artifacts match the frozen extraction manifest."""
    root = Path(root or DEFAULT_ARTIFACT_ROOT)
    manifest_path = root / 'SELECTIVE_EXTRACTION.json'
    if not manifest_path.is_file():
        raise FileNotFoundError('TAPAS selective extraction manifest missing: ' + str(manifest_path))
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    checked = []
    for record in manifest['files']:
        path = root / record['path']
        if not path.is_file():
            raise FileNotFoundError('Missing TAPAS artifact: ' + record['path'])
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != record['sha256']:
            raise ValueError('Changed TAPAS artifact: ' + record['path'])
        checked.append({'path': record['path'], 'sha256': digest, 'size': record['size']})
    return {
        'status': 'verified',
        'artifact_root': str(root),
        'source': manifest.get('source'),
        'files': checked,
        'interface_disclosure': (
            'Author TAPAS emits benign/malicious subgraph alerts. '
            'ATT&CK tactic labels and five-stage consolidation use the disclosed '
            'local mapping in tapas_stage.TACTIC_TO_STAGE / ACTION_TO_TACTIC / '
            'TAPAS_EVENT_TO_TACTIC.'
        ),
    }


def event_tactic(event):
    """Resolve an ATT&CK tactic label for a lab or CDM-like event."""
    if event.get('tactic') in TACTIC_TO_STAGE:
        return event['tactic']
    cdm = event.get('cdm_type') or event.get('tapas_event_type')
    if cdm in TAPAS_EVENT_TO_TACTIC:
        return TAPAS_EVENT_TO_TACTIC[cdm]
    action = event.get('action')
    if isinstance(action, dict):
        action = action.get('op') or action.get('action')
    if action in ACTION_TO_TACTIC:
        return ACTION_TO_TACTIC[action]
    return None


def stage_for_event(event):
    tactic = event_tactic(event)
    if tactic is None:
        return None
    return TACTIC_TO_STAGE[tactic]


def annotate_events(events, malicious_scores=None):
    """Attach tactic/stage fields. Downstream LLM sees only stage statistics."""
    annotated = []
    for index, event in enumerate(events):
        item = dict(event)
        tactic = event_tactic(event)
        stage = TACTIC_TO_STAGE.get(tactic) if tactic else None
        item['tapas_compatible'] = {
            'tactic': tactic,
            'stage': stage,
            'stage_label': STAGE_LABELS.get(stage),
            'mapping_source': 'dynahive-disclosed-local-mapping',
            'malicious_score': None if malicious_scores is None else malicious_scores[index],
        }
        if tactic and 'tactic' not in item:
            item['tactic'] = tactic
        if stage and 'stage' not in item:
            item['stage'] = stage
        annotated.append(item)
    return annotated


def stage_counts(events):
    counts = {f'stage{i}': 0 for i in range(1, 6)}
    for event in annotate_events(events):
        stage = event['tapas_compatible']['stage']
        if stage:
            counts[f'stage{stage}'] += 1
    return counts


def to_tapas_process_events(events, host='honeynet-host', subject='attacker-session'):
    """Project lab interactions into a minimal TAPAS-compatible typed stream."""
    projected = []
    for event in events:
        tactic = event_tactic(event)
        stage = TACTIC_TO_STAGE.get(tactic) if tactic else None
        action = event.get('action')
        if isinstance(action, dict):
            op = action.get('op') or action.get('action')
            path = action.get('path')
        else:
            op, path = action, event.get('path')
        cdm = {
            1: 'EVENT_CONNECT',
            2: 'EVENT_EXECUTE',
            3: 'EVENT_EXECUTE',
            4: 'EVENT_CONNECT',
            5: 'EVENT_READ',
        }.get(stage, 'EVENT_EXECUTE')
        projected.append({
            'subject': subject,
            'host': event.get('host', host),
            'cdm_type': cdm,
            'tapas_event_type': cdm,
            'object_path': path or f'/proc/{op or "unknown"}',
            'object_kind': 'file' if path else 'net' if stage in {1, 4} else 'process',
            'tactic': tactic,
            'stage': stage,
            'success': event.get('success'),
            'raw_action': op,
        })
    return projected


class TapasStageClassifier:
    """Online stage perception with optional author-weight malicious scoring."""

    def __init__(self, artifact_root=None, require_model=False):
        self.artifact_root = Path(artifact_root or DEFAULT_ARTIFACT_ROOT)
        try:
            self.artifact_report = verify_tapas_artifacts(self.artifact_root)
        except (FileNotFoundError, ValueError, KeyError):
            self.artifact_report = {
                'status': 'mapping-only',
                'artifact_root': str(self.artifact_root),
                'source': 'local-mapping',
                'files': [],
                'interface_disclosure': (
                    'ATT&CK tactic labels use the disclosed local mapping '
                    'in TACTIC_TO_STAGE / ACTION_TO_TACTIC.'
                ),
            }
        self.model_backend = 'mapping-only'
        self.lstm = None
        self.graphsage = None
        self._torch = None
        self._load_optional_models(require_model)

    def _load_optional_models(self, require_model):
        try:
            import torch
            self._torch = torch
        except ImportError:
            if require_model:
                raise RuntimeError('torch is required for TAPAS model scoring')
            return
        lstm_path = self.artifact_root / 'TAPAS-artifact' / 'model' / 'stackedlstm_tc.pt'
        if lstm_path.is_file():
            # Author LSTM encoder (pure torch). GraphSAGE classification remains
            # optional because torch_geometric may be absent on the lab VM.
            try:
                from .tapas_models import AuthorLSTM
                model = AuthorLSTM(input_size=6, output_size=6)
                try:
                    state = torch.load(lstm_path, map_location='cpu', weights_only=True)
                except TypeError:
                    state = torch.load(lstm_path, map_location='cpu')
                model.load_state_dict(state)
                model.eval()
                self.lstm = model
                self.model_backend = 'author-lstm'
            except Exception as exc:
                if require_model:
                    raise RuntimeError('Failed to load TAPAS LSTM weights') from exc
                self.model_backend = 'mapping-only-lstm-load-failed:' + type(exc).__name__
        try:
            import torch_geometric  # noqa: F401
            from .tapas_models import try_load_graphsage
            loaded = try_load_graphsage(self.artifact_root / 'TAPAS-artifact' / 'model')
            if loaded is not None:
                self.graphsage = loaded
                self.model_backend = 'author-lstm+graphsage'
        except ImportError:
            if require_model and self.lstm is None:
                raise

    def classify(self, events):
        projected = to_tapas_process_events(events)
        malicious_scores = None
        if self.lstm is not None and projected:
            malicious_scores = self._score_sequences(projected)
        annotated = annotate_events(events, malicious_scores)
        return {
            'events': annotated,
            'projected_tapas_events': projected,
            'stage_counts': stage_counts(events),
            'model_backend': self.model_backend,
            'artifact_report': {
                'status': self.artifact_report['status'],
                'files': len(self.artifact_report['files']),
                'interface_disclosure': self.artifact_report['interface_disclosure'],
            },
        }

    def _score_sequences(self, projected):
        torch = self._torch
        # Encode each event as a 6-d TAPAS-like history feature:
        # [event_type_id, count_proxy, obj_kind, path_bucket, src_port_bin, dst_port_bin]
        type_ids = {
            'EVENT_ACCEPT': 1, 'EVENT_CONNECT': 2, 'EVENT_EXECUTE': 3, 'EVENT_EXIT': 4,
            'EVENT_READ': 5, 'EVENT_RECVFROM': 6, 'EVENT_RECVMSG': 7, 'EVENT_SENDTO': 8,
            'EVENT_SENDMSG': 9, 'EVENT_WRITE': 10,
        }
        scores = []
        with torch.no_grad():
            for item in projected:
                vector = [
                    float(type_ids.get(item['cdm_type'], 3)),
                    1.0,
                    2.0 if item['object_kind'] == 'file' else 3.0 if item['object_kind'] == 'net' else 1.0,
                    float(min(90, len(str(item.get('object_path') or '')))),
                    1.0,
                    1.0,
                ]
                tensor = torch.tensor([[vector]], dtype=torch.float32)
                hidden = self.lstm(tensor)
                # Author LSTM returns concatenated cell state features. Use the
                # mean absolute activation as a bounded maliciousness proxy when
                # GraphSAGE is unavailable; disclose this engineering choice.
                score = float(hidden.abs().mean().clamp(0, 1).item())
                if self.graphsage is not None:
                    score = float(self.graphsage.score_vector(hidden))
                scores.append(score)
        return scores


def map_distribution(events):
    counts = [1.0] * 5
    for event in annotate_events(events):
        stage = event['tapas_compatible']['stage']
        if stage:
            counts[stage - 1] += 1
    total = sum(counts)
    return [c / total for c in counts]
