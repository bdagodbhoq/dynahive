"""Storage guard for the Ubuntu deployment, not an experimental metric."""
from __future__ import annotations

import shutil
import os
import errno
from pathlib import Path

MIN_FREE_BYTES = 20*1024**3


class StorageBudgetError(RuntimeError):
    pass


def storage_snapshot(path):
    root = Path(path).resolve()
    while not root.exists():
        root = root.parent
    usage = shutil.disk_usage(root)
    snapshot = {'path': str(root), 'total_bytes': usage.total,
                'used_bytes': usage.used, 'free_bytes': usage.free}
    if hasattr(os, 'statvfs'):
        stats = os.statvfs(root)
        snapshot.update(total_inodes=stats.f_files, free_inodes=stats.f_favail)
    return snapshot


def ensure_free_space(path, required_bytes=0, reserve_bytes=MIN_FREE_BYTES, journal=None):
    for value in (required_bytes, reserve_bytes):
        if type(value) is not int or value < 0:
            raise ValueError('Storage budgets must be nonnegative integer byte counts')
    snapshot = storage_snapshot(path)
    free = snapshot['free_bytes']
    allowed = free >= required_bytes+reserve_bytes
    # Inode exhaustion can fail writes even when byte capacity is sufficient.
    if snapshot.get('total_inodes', 0) and not snapshot['free_inodes']:
        allowed = False
    if journal:
        try:
            journal.append({'event': 'storage_check', **snapshot, 'required_bytes': required_bytes,
                            'reserve_bytes': reserve_bytes, 'allowed': allowed})
        except OSError as exc:
            if exc.errno not in {errno.ENOSPC, errno.EDQUOT}:
                raise
            raise StorageBudgetError('Storage journal write failed: space, inode or quota exhausted') from exc
    if not allowed:
        raise StorageBudgetError(f'Insufficient disk headroom: {free/1024**3:.2f} GiB free; '
                                 f'{(required_bytes+reserve_bytes)/1024**3:.2f} GiB required; '
                                 f'free inodes={snapshot.get("free_inodes", "unavailable")}')
    return free
