"""Deception: deploy reviewed configs and progressive freeze (checklist §10)."""
from __future__ import annotations

from pathlib import Path

from .compile import compile_deployment
from .freeze import FreezeLedger


def deploy(root: Path, topology: dict, honey: dict, traps: dict, audit: dict,
           freeze: FreezeLedger | None = None) -> Path:
    """Deploy only a reviewed candidate. FreezeLedger blocks rewriting exposed facts."""
    if freeze is not None:
        honey = freeze.protect(honey)
    return compile_deployment(root, topology, honey, traps, audit)


__all__ = ["deploy", "compile_deployment", "FreezeLedger"]
