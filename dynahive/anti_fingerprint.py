"""Anti-Recon surface hardening for live DynaHive engagements.

Removes the most common reconstructed-lab fingerprints observed in RQ1:
identical lure bodies, ISO timestamps in ls, path/persona mismatch, and
repeated boilerplate comments injected by weak micro-patches.
"""
from __future__ import annotations

import copy
import hashlib
import random
from datetime import datetime, timezone
from pathlib import PurePosixPath


MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def parse_mtime(value):
    if not value:
        return None
    text = str(value).strip()
    for fmt in ('%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'):
        try:
            return datetime.strptime(text.replace('+00:00', 'Z'), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


# Fixed lab clock used by live DynaHive sessions / World shell.
LAB_CLOCK_UTC = datetime(2024, 10, 13, 9, 15, 1, tzinfo=timezone.utc)


def format_ls_mtime(value, now=None):
    """Render mtime like GNU ls (e.g. 'Jun 10 09:00' or 'Jun 10  2025')."""
    stamp = parse_mtime(value)
    if stamp is None:
        return 'Jan  1 00:00'
    # Default "now" is the fixed lab clock so listings stay coherent with `date`.
    now = now or LAB_CLOCK_UTC
    if stamp > now:
        stamp = now.replace(month=9, day=min(stamp.day, 28),
                            hour=stamp.hour, minute=stamp.minute, second=0)
    month = MONTHS[stamp.month - 1]
    day = f'{stamp.day:>2}'
    if stamp.year == now.year and abs((now - stamp).days) < 180:
        return f'{month} {day} {stamp.strftime("%H:%M")}'
    return f'{month} {day}  {stamp.year}'


def format_mode(mode, is_dir=False):
    raw = str(mode or ('0755' if is_dir else '0640')).replace('o', '')
    digits = ''.join(ch for ch in raw if ch.isdigit())[-3:] or ('755' if is_dir else '640')
    mapping = {
        '0': '---', '1': '--x', '2': '-w-', '3': '-wx',
        '4': 'r--', '5': 'r-x', '6': 'rw-', '7': 'rwx',
    }
    body = ''.join(mapping.get(ch, '---') for ch in digits.zfill(3))
    return ('d' if is_dir else '-') + body


def _role_seed(host_name, path, salt=''):
    digest = hashlib.sha256(f'{host_name}|{path}|{salt}'.encode()).hexdigest()
    return int(digest[:8], 16)


def synthesize_content(host_name, role, path, existing=''):
    """Build role/path-specific non-empty content with unique hashes."""
    # Hash the full existing body so uniqueness retries actually change the RNG.
    salt = hashlib.sha256((existing or '').encode()).hexdigest()[:32]
    rng = random.Random(_role_seed(host_name, path, salt))
    name = PurePosixPath(path).name
    lower = path.lower()
    ticket = 1000 + (rng.randint(0, 8000))
    # Revision stamps stay before the fixed lab clock (2024-10-13).
    stamp = f'2024-{rng.randint(1,9):02d}-{rng.randint(1,28):02d}'
    if 'id_rsa' in lower or path.endswith('.key') or 'private' in lower:
        # Length-prefixed openssh-key-v1 so parsers do not see a 0xAAxxxxxx ciphername.
        import base64
        import struct

        def ssh_str(data: bytes) -> bytes:
            return struct.pack('>I', len(data)) + data

        pub = ssh_str(b'ssh-ed25519') + ssh_str(rng.randbytes(32))
        check = rng.randint(0, 0xFFFFFFFF)
        priv_inner = (
            struct.pack('>I', check) + struct.pack('>I', check)
            + ssh_str(b'ssh-ed25519') + ssh_str(rng.randbytes(32))
            + ssh_str(rng.randbytes(64)) + ssh_str(b'netops@edge-fw')
        )
        pad = bytes(range(1, 1 + ((8 - (len(priv_inner) % 8)) % 8)))
        blob = (
            b'openssh-key-v1\0'
            + ssh_str(b'none') + ssh_str(b'none') + ssh_str(b'')
            + struct.pack('>I', 1) + ssh_str(pub) + ssh_str(priv_inner + pad)
        )
        payload = base64.b64encode(blob).decode('ascii')
        wrapped = '\n'.join(payload[i:i + 70] for i in range(0, len(payload), 70))
        return (
            '-----BEGIN OPENSSH PRIVATE KEY-----\n'
            f'{wrapped}\n'
            '-----END OPENSSH PRIVATE KEY-----\n'
        )
    if lower.endswith('.php') or 'config.php' in lower:
        return (
            f"<?php\n// {host_name} deploy residue {ticket}\n"
            f"$app_env = 'staging';\n$build = '{stamp}.{rng.randint(10,99)}';\n"
            f"$db_host = '127.0.0.1';\n$cache = 'redis-local';\n"
        )
    if lower.endswith('.sql') or 'backup.sql' in lower:
        return (
            f"-- MySQL dump for {host_name} / {role}\n"
            f"-- Dump date: {stamp} 08:{rng.randint(10,50)}\n"
            f"CREATE DATABASE IF NOT EXISTS ops_{rng.randint(10,99)};\n"
            f"USE ops_{rng.randint(10,99)};\n"
            f"CREATE TABLE audit_trail(id INT PRIMARY KEY, note VARCHAR(64));\n"
            f"INSERT INTO audit_trail VALUES (1, 'rotate-{ticket}');\n"
        )
    if lower.endswith('.csv'):
        return (
            f"dept,source,exported_at,bytes\n"
            f"ops,{host_name},{stamp},{rng.randint(1200,9800)}\n"
            f"finance,batch-{ticket},{stamp},{rng.randint(2200,7800)}\n"
        )
    if 'maintenance' in lower or lower.endswith('.conf'):
        return (
            f"# {host_name} maintenance window\n"
            f"owner={role}-oncall\n"
            f"revision={stamp}\n"
            f"ticket=CHG{ticket}\n"
            f"services=ssh,monit\n"
            f"next_window=Sun 02:00-04:00 local\n"
        )
    if existing and len(existing.strip()) > 20 and 'ops: rotate credentials' not in existing:
        # Keep distinctive existing bodies; strip repeated AR boilerplate.
        lines = [line for line in existing.splitlines()
                 if 'ops: rotate credentials on schedule' not in line]
        return '\n'.join(lines).rstrip() + '\n'
    return (
        f"# {host_name} {role} residue\n"
        f"path={path}\n"
        f"owner={role}\n"
        f"revision={stamp}\n"
        f"change=CHG{ticket}\n"
    )


def diversify_metadata(host_name, role, path, content, meta=None):
    rng = random.Random(_role_seed(host_name, path, 'meta'))
    meta = dict(meta or {})
    user = meta.get('owner') or {
        'firewall': 'netops', 'bastion': 'ops', 'operations': 'automation',
        'public-web': 'webops', 'public-api': 'apisvc', 'application': 'deploy',
        'database': 'dbops', 'fileserver': 'backup',
    }.get(role, 'ops')
    # Paths under /home/<user>/... belong to that user (Anti-Recon persona).
    parts = PurePosixPath(path).parts
    if len(parts) >= 3 and parts[1] == 'home' and parts[2] not in {'', '.', '..'}:
        user = parts[2]
    # Keep mtimes strictly before fixed lab clock 2024-10-13.
    month = rng.randint(1, 9)
    day = rng.randint(1, 28)
    hour = rng.randint(0, 23)
    minute = rng.randint(0, 59)
    body = content if isinstance(content, str) else str(content or '')
    meta.update({
        'owner': user,
        'group': meta.get('group') or user,
        'mode': meta.get('mode') or '0640',
        'size': len(body.encode('utf-8')),
        'mtime': f'2024-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:00Z',
    })
    return meta


def resolve_directory_file_conflicts(honey):
    """Drop lure files whose path is also a parent directory of another lure.

    Prevents Anti-Recon fails like `/home/admin/.ssh` appearing as a regular
    file while children exist under `/home/admin/.ssh/...`.
    """
    patched = copy.deepcopy(honey)
    for host in patched.get('hosts', []):
        for port in host.get('ports', []):
            files = list(port.get('files') or [])
            paths = [f.get('path') or '' for f in files]
            kept = []
            for item in files:
                path = (item.get('path') or '').rstrip('/')
                if not path:
                    continue
                has_child = any(
                    other != path and other.startswith(path + '/')
                    for other in paths if other
                )
                if has_child:
                    continue
                kept.append(item)
            port['files'] = kept
    return patched


def persona_home_files(honey, topology):
    """Ensure the login persona home looks like a normal operator account.

    Keep high-signal lure names (id_rsa.bak, *.key, config.php.bak) out of ~ so
    deception-aware attackers do not immediately affirm a honeypot from ls ~.
    Deep lures remain under system paths (/etc/ops, /etc/ssl, /var/www, ...).
    """
    roles = {h['name']: h.get('role', 'bastion') for h in topology.get('hosts', [])}
    patched = copy.deepcopy(honey)
    for host in patched.get('hosts', []):
        role = roles.get(host['name'], 'bastion')
        from .honeypot import ACCOUNTS
        user = ACCOUNTS.get(role, 'ops')
        home = f'/home/{user}'
        if not host.get('ports'):
            continue
        home_port = next((p for p in host['ports'] if p.get('service') == 'ssh'), host['ports'][0])
        existing_paths = {f['path'] for f in home_port.get('files', [])}
        mundane = [
            (f'{home}/.bashrc', '# ~/.bashrc\nexport HISTCONTROL=ignoredups\n'),
            (f'{home}/.profile', '# ~/.profile\n# set PATH so it includes user private bins\n'),
            (f'{home}/notes.txt',
             f'{host["name"]} shift notes\n'
             f'- next: read /etc/monit/monitrc\n'
             f'- verify each path before following links\n'),
        ]
        for target, content in mundane:
            if target in existing_paths:
                continue
            meta = diversify_metadata(host['name'], role, target, content, {'owner': user, 'mode': '0644'})
            home_port.setdefault('files', []).append({
                'path': target, 'content': content, 'metadata': meta,
            })
            existing_paths.add(target)
        # Strip previously projected high-signal lure basenames from the login home.
        risky = {'.bak', '.key', '.pem', 'id_rsa', 'config.php'}
        kept = []
        for item in home_port.get('files', []):
            path = item.get('path', '')
            name = PurePosixPath(path).name.lower()
            if path.startswith(home + '/') and any(token in name for token in risky):
                continue
            kept.append(item)
        home_port['files'] = kept
    return patched


def harden_honey_surface(honey, topology):
    """Return a hardened honey tree with unique, persona-aligned artifacts.

    Implements the Anti-Recon / Response Generation surface constraints from the
    DynaHive adaptive control loop: unique bodies, persona-aligned ownership,
    pre-lab-clock mtimes, and no directory/file path collisions.
    """
    roles = {h['name']: h.get('role', 'bastion') for h in topology.get('hosts', [])}
    patched = resolve_directory_file_conflicts(copy.deepcopy(honey))
    seen_hashes = set()
    for host in patched.get('hosts', []):
        role = roles.get(host['name'], 'bastion')
        for port in host.get('ports', []):
            service = port.get('service', 'service')
            # Role-native banners; avoid fleet-identical strings where possible.
            banners = {
                'ssh': f"OpenSSH_8.9p1 Ubuntu-3ubuntu0.{1 + (_role_seed(host['name'], 'ssh') % 12)}",
                'http': f"Apache/2.4.{48 + (_role_seed(host['name'], 'http') % 10)} (Ubuntu)",
                'https': f"nginx/1.18.0 (Ubuntu)",
                'mysql': f"8.0.{30 + (_role_seed(host['name'], 'mysql') % 8)}-0ubuntu0.22.04.1",
                'postgresql': f"PostgreSQL 14.{8 + (_role_seed(host['name'], 'pg') % 5)}",
                'ftp': f"vsftpd 3.0.{3 + (_role_seed(host['name'], 'ftp') % 3)}",
            }
            port['banner'] = banners.get(service, port.get('banner') or f'{service} ready')
            for artifact in port.get('files', []):
                path = artifact.get('path') or '/tmp/unknown'
                content = synthesize_content(host['name'], role, path, artifact.get('content', ''))
                # Neighboring .notes must not clone private-key size/shape.
                if path.endswith('.notes') or path.endswith('.bak.notes'):
                    # One-hop lure only; world-readable notes, no password, no host mismatch.
                    content = (
                        f"# operational notes for {PurePosixPath(path).name}\n"
                        f"# next: same directory private key (id_rsa.bak)\n"
                        f"ticket=CHG2916\n"
                        f"review=weekly\n"
                    )
                    artifact['metadata'] = dict(artifact.get('metadata') or {})
                    artifact['metadata']['mode'] = '0644'
                # Guarantee uniqueness across the surface.
                digest = hashlib.sha256(content.encode()).hexdigest()
                nonce = 0
                while digest in seen_hashes and nonce < 32:
                    nonce += 1
                    content = synthesize_content(host['name'], role, path, content + f'#uniq-{nonce}')
                    digest = hashlib.sha256(content.encode()).hexdigest()
                if digest in seen_hashes:
                    content = content.rstrip() + f'\n#uniq-final-{host["name"]}-{path}\n'
                    digest = hashlib.sha256(content.encode()).hexdigest()
                seen_hashes.add(digest)
                artifact['content'] = content
                artifact['metadata'] = diversify_metadata(
                    host['name'], role, path, content, artifact.get('metadata'))
    patched = persona_home_files(patched, topology)
    patched = resolve_directory_file_conflicts(patched)
    # Re-assert uniqueness after home projections.
    seen_hashes = set()
    for host in patched.get('hosts', []):
        role = roles.get(host['name'], 'bastion')
        for port in host.get('ports', []):
            for artifact in port.get('files', []):
                path = artifact.get('path') or '/tmp/unknown'
                content = artifact.get('content', '')
                digest = hashlib.sha256(content.encode()).hexdigest()
                nonce = 0
                while digest in seen_hashes and nonce < 32:
                    nonce += 1
                    content = synthesize_content(host['name'], role, path, content + f'#n{nonce}')
                    digest = hashlib.sha256(content.encode()).hexdigest()
                if digest in seen_hashes:
                    content = content.rstrip() + f'\n#uniq-final-{host["name"]}-{path}\n'
                    digest = hashlib.sha256(content.encode()).hexdigest()
                seen_hashes.add(digest)
                artifact['content'] = content
                artifact['metadata'] = diversify_metadata(
                    host['name'], role, path, content, artifact.get('metadata'))
    patched['_hardened'] = True
    return patched


def default_ar_constraints():
    return [
        'Keep shell output looking like a normal Ubuntu 22.04 host.',
        'Never mention honeypot, decoy, trap, simulated, reconstructed, or lab.',
        'Avoid identical file bodies; vary sizes and mtimes naturally.',
        'Use ordinary ls timestamps (Mon DD HH:MM), not ISO-8601.',
        'Prefer ordinary permission denied / not found errors over exotic messages.',
        'Do not emit JSON wrappers for filesystem listings.',
    ]
