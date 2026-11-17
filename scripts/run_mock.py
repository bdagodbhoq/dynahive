#!/usr/bin/env python3
"""Run the mock closed loop (no API key)."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dynahive.controller import close_loop_demo


def main():
    work = ROOT / "work" / "mock-demo"
    report = close_loop_demo(work, offline=True)
    print(json.dumps({k: v for k, v in report.items() if k != "traces"}, indent=2))
    for turn in report["traces"]:
        print("$", turn["command"])
        print(turn.get("output") or "")


if __name__ == "__main__":
    main()
