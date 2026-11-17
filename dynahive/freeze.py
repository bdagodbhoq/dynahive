"""Progressive freeze: exposed facts stay stable; unexposed resources may change."""
from __future__ import annotations

import copy
from pathlib import PurePosixPath


class FreezeLedger:
    def __init__(self):
        self.exposed = set()  # (host, path)
        self.history = []

    def mark_read(self, host: str, path: str) -> None:
        path = str(PurePosixPath(path or "/"))
        self.exposed.add((host, path))
        self.history.append({"event": "expose", "host": host, "path": path})

    def is_exposed(self, host: str, path: str) -> bool:
        return (host, str(PurePosixPath(path or "/"))) in self.exposed

    def protect(self, honey: dict) -> dict:
        """Keep content of already-exposed artifacts; allow other edits."""
        snapshot = getattr(self, "_last_honey", None)
        honey = copy.deepcopy(honey)
        if snapshot is None:
            self._last_honey = copy.deepcopy(honey)
            return honey
        index = {}
        for host in snapshot.get("hosts", []):
            for port in host.get("ports", []):
                for artifact in port.get("files", []):
                    index[(host["name"], artifact.get("path"))] = artifact
        for host in honey.get("hosts", []):
            for port in host.get("ports", []):
                for artifact in port.get("files", []):
                    key = (host["name"], artifact.get("path"))
                    if key in self.exposed and key in index:
                        artifact["content"] = index[key].get("content")
                        artifact["metadata"] = copy.deepcopy(index[key].get("metadata") or {})
        self._last_honey = copy.deepcopy(honey)
        return honey
