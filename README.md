# DynaHive

Adaptive honeynet prototype: **observe → plan → build environment → generate guidance paths → review → deploy → freeze exposed facts**.

This package is the core system used in the paper experiments. It does not include experiment traces, result tables, or attacker-engine workloads.

## Layout

```
dynahive/           core library
examples/           three-host decoy topology
prompts/            agent runtime prompts
scripts/            mock and live closed-loop runners
tests/              closed-loop tests
logs/               human and LLM-attacker command transcripts
```

## Configure

Copy `.env.example`. Keys stay in the environment; they are never written into decoy hosts.

```
DYNHIVE_BASE_URL=
DYNHIVE_API_KEY=
DYNHIVE_MODEL=
DYNHIVE_WIRE_API=responses
```

## Mock closed loop (no API)

```bash
python -m pytest tests -q
python scripts/run_mock.py
```

## Live model

```bash
export DYNHIVE_BASE_URL=https://example.invalid/v1
export DYNHIVE_API_KEY=
export DYNHIVE_MODEL=
export DYNHIVE_WIRE_API=responses
export DYNHIVE_REASONING_EFFORT=high
python scripts/run_paper_flow.py --live
```

## Docker

```bash
docker compose up --build
```

The compose network is `internal: true`. The controller does not publish management ports to decoy nodes.

## Reset

Delete `work/` and rerun `scripts/run_mock.py`.
