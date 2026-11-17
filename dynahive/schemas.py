"""Structured objects persisted across the closed loop (checklist §3)."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class Host:
    name: str
    role: str
    ip: str | None = None
    os: str = "Ubuntu 22.04"


@dataclass
class Credential:
    username: str
    secret: str
    host: str
    condition: str = "ssh"


@dataclass
class ObservedFact:
    session: str
    host: str
    identity: str
    operation: str
    result: str
    success: bool
    path: str | None = None


@dataclass
class GuidanceStep:
    clue: str
    action: str
    result: str
    host: str
    preconditions: list[str] = field(default_factory=list)


@dataclass
class ReviewIssue:
    kind: str
    evidence: str
    blocking: bool = True


def dump(obj) -> dict[str, Any]:
    return asdict(obj)
