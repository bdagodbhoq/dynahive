"""Load the runtime system prompts used by each agent."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "prompts"


def load(name: str) -> str:
    path = ROOT / name
    text = path.read_text(encoding="utf-8").strip()
    if len(text) < 400:
        raise ValueError(f"prompt {name} is too short to be the paper runtime prompt")
    return text


def environment_system() -> str:
    return load("environment.txt")


def guidance_expand() -> str:
    return load("guidance_expand.txt")


def guidance_assess() -> str:
    return load("guidance_assess.txt")


def guidance_select() -> str:
    return load("guidance_select.txt")


def review_system() -> str:
    return load("review.txt")


def planner_system() -> str:
    return load("planner.txt")


def perception_system() -> str:
    return load("perception.txt")
