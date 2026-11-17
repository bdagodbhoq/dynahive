"""Offline LLM stand-in so the closed loop can run without an API key."""
from __future__ import annotations

import json
from pathlib import Path

from .runtime import LLMClient


class MockClient(LLMClient):
    def __init__(self, journal: Path | None = None):
        super().__init__(api_key="offline", offline=True, journal=journal, model="mock")

    def complete(self, system, user, fallback=None, task="unspecified", json_output=True):
        if fallback is not None:
            return super().complete(system, user, fallback=fallback, task=task, json_output=json_output)
        if json_output:
            return {"ok": True, "task": task, "note": "mock-empty"}
        return ""
