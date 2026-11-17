from __future__ import annotations

import asyncio
import copy
import csv
import io
import calendar
import datetime
import hashlib
import json
import random
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from urllib.parse import parse_qs, urlparse
import fnmatch
import re

from .anti_fingerprint import format_ls_mtime, format_mode
from .runtime import Journal

BANNERS = {"http": "Apache/2.4.52 (Ubuntu)", "https": "nginx/1.18.0 (Ubuntu)",
    "ssh": "OpenSSH_8.9p1 Ubuntu-3ubuntu0.13", "mysql": "8.0.36-0ubuntu0.22.04.1",
    "postgresql": "PostgreSQL 14.11", "ftp": "vsftpd 3.0.5", "smb": "Samba 4.15.13"}

ACCOUNTS = {'firewall': 'netops', 'bastion': 'ops', 'operations': 'automation',
            'public-web': 'webops', 'public-api': 'apisvc', 'application': 'deploy',
            'database': 'dbops', 'fileserver': 'backup'}


def filesystem_metadata(artifact):
    """Filesystem attributes; provenance belongs in controller records only."""
    return {k:v for k,v in artifact.get('metadata', {}).items() if k in {'owner','group','mode','mtime','size'}}


def _add_reference(item, fields, note):
    """Keep JSON/CSV valid when injecting operational references.

Private keys cannot contain configuration lines. Put references into a
neighboring notes artifact instead (selected by materialize).
"""
    content = item['content']
    path = item['path'].lower()
    if path.endswith('.json'):
        value = json.loads(content)
        if isinstance(value, dict):
            value.setdefault('operational_references', []).append(fields)
        elif isinstance(value, list): value.append({'operational_reference':fields})
        else: raise ValueError(f'Cannot inject a reference into JSON scalar: {item["path"]}')
        item['content'] = json.dumps(value, indent=2)+'\n'
        return
    if path.endswith('.csv'):
        reader = csv.reader(io.StringIO(content)); rows = list(reader)
        if rows and len(rows[0]) > 1:
            width = len(rows[0])
            if any(len(row)!=width for row in rows): raise ValueError(f'Inconsistent CSV: {item["path"]}')
            column = 'maintenance_reference'
            if column not in rows[0]:
                rows[0].append(column)
                for row in rows[1:]: row.append('')
            index = rows[0].index(column)
            if len(rows)>1:
                rows[1][index] = (rows[1][index]+'; ' if rows[1][index] else '')+json.dumps(fields)
            else:
                rows.append(['']*len(rows[0]));rows[1][index]=json.dumps(fields)
            stream = io.StringIO(); csv.writer(stream).writerows(rows)
            item['content'] = stream.getvalue()
            return
    item['content'] = content.rstrip() + '\n# ' + note + '\n' + ''.join(
        f'# {key}={value}\n' for key, value in fields.items())


def _reference_file(files, item):
    path = item['path'].lower()
    if 'PRIVATE KEY' in item['content'] or path.endswith(('.pem', '.key')) or '/.ssh/id_' in path:
        notes = next((f for f in files if f['path'] == item['path']+'.notes'), None)
        if notes is None:
            notes = {'path': item['path']+'.notes', 'content': '# Key rotation and maintenance record\n',
                     'metadata': copy.deepcopy(item['metadata'])}
            files.append(notes)
        return notes
    return item


class World:
    """Stateful virtual services. This is a reconstructed benchmark, not a production OS."""
    def __init__(self, spec: dict, journal: Journal, seed=0):
        self.spec, self.journal = spec, journal
        self.hosts = {h["name"]: h for h in spec["hosts"]}
        self.sessions = {}
        self.lock = threading.RLock()
        self.random = random.Random(seed)
        # Route B: first-class VFS per host (dirs/files share one tree).
        self.vfs = {}
        self.rebuild_all_vfs()

    def rebuild_all_vfs(self):
        for host in list(self.hosts):
            self.rebuild_vfs(host)

    def rebuild_vfs(self, host):
        from .vfs import VirtualFS, seed_ubuntu_skeleton
        user = self.hosts[host]['credential']['username']
        vfs = VirtualFS(host, user)
        seed_ubuntu_skeleton(vfs, user, enterprise_lures=(self.hosts[host].get('os_id') != 'debian'))
        # Materialize lure files into the tree (dirs promoted automatically).
        for path, item in self._host_files(host).items():
            meta = filesystem_metadata(item)
            content = item.get('content') or ''
            owner = meta.get('owner')
            mode = meta.get('mode', '0640')
            mtime = meta.get('mtime')
            vfs.put_file(path, content, owner=owner, mode=mode, mtime=mtime)
        # Authoritative system files.
        for sys_path in (
            '/etc/passwd', '/etc/shadow', '/etc/group', '/etc/crontab',
            '/etc/os-release', '/etc/issue', '/etc/hostname', '/etc/debian_version',
            '/etc/resolv.conf', '/etc/ssh/sshd_config', '/proc/uptime',
            '/proc/cmdline', '/proc/meminfo', '/proc/cpuinfo',
            '/var/log/auth.log', '/var/log/syslog', '/var/log/kern.log',
            '/etc/monit/monitrc', '/etc/monit/conf.d/sshd', '/etc/ops/maintenance.conf',
        ):
            body = self._system_file(host, sys_path)
            if body is not None:
                mode = '0640' if sys_path.endswith('shadow') else '0644'
                vfs.put_file(sys_path, body, owner='root', mode=mode, mtime='2024-03-01T09:00:00Z')
        # Ensure admin home exists when admin lures are present.
        extra_groups = []
        for path in list(self._host_files(host)):
            parts = PurePosixPath(path).parts
            if len(parts) >= 3 and parts[1] == 'home':
                vfs.ensure_dir('/home/' + parts[2], owner=parts[2], mode='0755')
                if parts[2] not in extra_groups and parts[2] != user:
                    extra_groups.append(parts[2])
        # Homes seeded by the Ubuntu skeleton (e.g. /home/admin) also need NSS rows.
        home_node = vfs.get('/home')
        if home_node is not None and home_node.is_dir:
            for child in home_node.children.values():
                name = PurePosixPath(child.path).name
                if name and name != user and name not in extra_groups:
                    extra_groups.append(name)
        if extra_groups:
            group = vfs.read('/etc/group') or ''
            gid = 1001
            for name in extra_groups:
                if f'{name}:x:' not in group:
                    group += f'{name}:x:{gid}:\n'
                    gid += 1
            vfs.put_file('/etc/group', group, owner='root', mode='0644', mtime='2024-03-01T09:00:00Z')
            passwd = vfs.read('/etc/passwd') or self._system_file(host, '/etc/passwd') or ''
            uid = 1001
            for name in extra_groups:
                if not any(line.startswith(name + ':') for line in passwd.splitlines()):
                    passwd += f'{name}:x:{uid}:{uid}:{name}:/home/{name}:/bin/bash\n'
                    uid += 1
            vfs.put_file('/etc/passwd', passwd, owner='root', mode='0644', mtime='2024-03-01T09:00:00Z')
            shadow = vfs.read('/etc/shadow') or self._system_file(host, '/etc/shadow') or ''
            for name in extra_groups:
                if not any(line.startswith(name + ':') for line in shadow.splitlines()):
                    shadow += f'{name}:*:19600:0:99999:7:::\n'
            vfs.put_file('/etc/shadow', shadow, owner='root', mode='0640', mtime='2024-03-01T09:00:00Z')
        # Standard files attackers expect on Ubuntu sshd.
        vfs.put_file('/etc/hosts', self._system_file(host, '/etc/hosts') or '',
                     owner='root', mode='0644', mtime='2024-01-10T08:00:00Z')
        vfs.put_file('/etc/ssh/ssh_host_ed25519_key.pub',
                     'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGhvc3Qta2V5LWVkMjU1MTktZGVtbyBob3N0IGtleQ host\n',
                     owner='root', mode='0644', mtime='2024-02-12T09:00:00Z')
        vfs.put_file('/var/log/monit.log',
                     f'[{host}] monit: starting\n[{host}] monit: monit daemon at 1234\n',
                     owner='root', mode='0640', mtime='2024-07-10T04:17:01Z')
        self.vfs[host] = vfs

    def _state(self, session):
        return self.sessions.setdefault(session, {"access": set(), "root": set(), "hosts": set()})

    def interact(self, session: str, action: dict, source="gateway") -> dict:
        started = time.perf_counter()
        op, name = action.get("op"), action.get("host")
        if not isinstance(session, str) or len(session) > 100: raise ValueError("Invalid session")
        if op not in {"scan", "probe", "exploit", "login", "list", "read", "privilege", "objective", "query"}:
            raise ValueError("Unknown operation")
        if name not in self.hosts: raise ValueError("Unknown lab host")
        host = self.hosts[name]
        with self.lock:
            state = self._state(session)
            reply = {"ok": False, "output": "Access denied"}
            success_stage = None
            if op == "scan":
                reply = {"ok": True, "ports": [{"port": p["port"], "service": p["service"],
                    "banner": p["banner"]} for p in host["ports"]]}
                success_stage = 1
            elif op == "probe":
                reply = {"ok": True, "hostname": name, "os": host.get('os', "Ubuntu 22.04.4 LTS"), "uptime_days": host.get('uptime_days', 37),
                    "ports": [{"port": p["port"], "service": p["service"], "banner": p["banner"]} for p in host["ports"]]}
                success_stage = 1
            elif op == "exploit":
                port = action.get("port")
                service = next((p for p in host['ports'] if p['port']==port), None)
                files = {f['path']:f for f in service.get('files', [])} if service else {}
                matched = [v for v in host.get('vulnerabilities', [])
                    if v.get('target_port')==port or v.get('target_file') in files]
                leak_types = {'config leak','path traversal'}
                leak_paths = [v['target_file'] for v in matched if v.get('type','').lower() in leak_types
                              and v.get('target_file') in files]
                if leak_paths and (service['service'].lower() in {'http','https'} or name in state['access']):
                    # A declared file leak exposes its artifact, not a shell.
                    # Foothold/lateral stages require a later successful login.
                    items = [files[path] for path in dict.fromkeys(leak_paths)]
                    reply = {'ok':True, 'content':'\n'.join(f['content'] for f in items),
                             'files':[{'path':f['path'],'metadata':filesystem_metadata(f)} for f in items]}
                elif any(v.get('type','').lower() in {'rce','file upload','outdated ssh'} and
                         v.get('target_port')==port for v in matched):
                    state["access"].add(name)
                    username = host['credential']['username']
                    reply = {"ok": True, "output": f"uid=1000({username}) gid=1000({username}) host={name}"}
                    success_stage = 2
                else: reply = {"ok": False, "output": "No unauthenticated entry point; leaked credentials require login"}
            elif op == "login":
                if action.get("username") == host["credential"]["username"] and action.get("password") == host["credential"]["password"]:
                    prior = bool(state["access"] - {name})
                    state["access"].add(name)
                    reply = {"ok": True, "output": f"Authenticated to {name}"}
                    success_stage = 4 if prior else 2
                else: reply = {"ok": False, "output": "Authentication failed"}
            elif name in state["access"]:
                files = {f["path"]: f for p in host["ports"] for f in p.get("files", [])}
                if op == "list":
                    reply = {"ok": True, "files": list(files), "users": [host['credential']['username'], "root"]}
                elif op == "read":
                    item = files.get(action.get("path"))
                    reply = {"ok": bool(item), "content": item.get("content", "") if item else "No such file"}
                    if item: reply['metadata'] = filesystem_metadata(item)
                elif op == "privilege":
                    if action.get("evidence_path") in files:
                        state["root"].add(name)
                        reply = {"ok": True, "output": "uid=0(root) gid=0(root)"}
                        success_stage = 3
                    else: reply = {"ok": False, "output": "Privilege evidence required"}
                elif op == "query":
                    reply = {"ok": True, "output": "database: operations_archive; tables: audit_events, exports, users"}
                elif op == "objective":
                    item = files.get(action.get("path"))
                    if item and name in state["root"] and host.get('role') in {'application', 'database', 'fileserver'}:
                        reply = {"ok": True, "content": item.get("content", ""), "archive_sha256":
                            hashlib.sha256(item.get("content", "").encode()).hexdigest()}
                        success_stage = 5
                    else: reply = {"ok": False, "output": "Privileged archive access on the internal tier required"}
            if reply["ok"]: state["hosts"].add(name)
            event = {"event": "interaction", "session_id": session, "host": name, "source": source,
                "action": {"login": "lateral"}.get(op, op), "request": action, "response": reply,
                "success": reply["ok"], "stage": success_stage,
                "decoy_contact": True, "trap_trigger": op == "read" and bool(reply.get("ok")) and
                bool(next((f.get('runtime_links') for p in host['ports'] for f in p.get('files', [])
                           if f['path'] == action.get('path')), False)),
                "latency_ms": (time.perf_counter() - started) * 1000}
            self.journal.append(event)
            return reply

    def _session_state(self, session, host):
        state = self._state(session)
        user = self.hosts[host]['credential']['username']
        debian = (self.hosts[host].get('os_id') == 'debian')
        home = '/root' if user == 'root' else '/home/' + user
        # RQ1 decoy bind address is always 10.77.0.10; keep SSH_* aligned with that
        # entry so env fingerprinting does not contradict the declared service.
        ip = '10.77.0.10' if not debian else (self.hosts[host].get('ip') or '10.0.2.15')
        path = ('/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games' if debian
                else '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin')
        state.setdefault('cwd', home)
        state.setdefault('env', {
            'USER': user, 'HOME': home, 'SHELL': '/bin/bash',
            'PATH': path,
            'LOGNAME': user, 'PWD': home,
            'BASH_VERSION': '5.1.16(1)-release',
            'BASH': '/bin/bash',
            '0': 'bash',
            '$': '2145',
            # Realistic sshd-exported variables for an already-open interactive session.
            'SSH_CONNECTION': f'10.77.0.250 51234 {ip} 22',
            'SSH_CLIENT': '10.77.0.250 51234 22',
            'SSH_TTY': '/dev/pts/0',
            'TERM': 'xterm-256color',
        })
        state['env'].setdefault('PWD', state['cwd'])
        state.setdefault('lab_clock_offset', 0.0)
        if host not in state['access']:
            state['access'].add(host)
        return state

    def _expand_shell_vars(self, text, env, session=None, host=None):
        """Expand $VAR / ${VAR} / $RANDOM / $((arith)) / $(cmd) / $? for interactive atoms."""
        def repl_arith(match):
            expr = match.group(1).replace(' ', '')
            if re.fullmatch(r'[0-9+\-*/()]+', expr):
                try:
                    return str(int(eval(expr, {'__builtins__': {}}, {})))
                except Exception:
                    return match.group(0)
            return match.group(0)
        text = re.sub(r'\$\(\(([^)]*)\)\)', repl_arith, text)

        def repl_subst(match):
            inner = match.group(1).strip()
            if session is None or host is None or not inner:
                return ''
            # Recurse for simple substitutions used in fingerprinting.
            result = self.execute_command(session, host, inner)
            out = result.get('output', '') if result.get('handled') else ''
            return out.rstrip('\n')
        # Expand $(...) after arithmetic so $((...)) is not stolen.
        text = re.sub(r'\$\(([^)]*)\)', repl_subst, text)
        text = re.sub(r'`([^`]*)`', repl_subst, text)
        text = text.replace('$?', str(env.get('?', '0')))
        # Interactive bash PID used by ps /proc fingerprints.
        text = text.replace('$$', str(env.get('$', '2145')))
        text = text.replace('$!', str(env.get('!', '')))
        text = text.replace('$0', str(env.get('0', 'bash')))
        text = text.replace('$#', str(env.get('#', '0')))
        text = re.sub(r'\$[1-9][0-9]*', '', text)

        def repl_braced(match):
            name = match.group(1)
            if name == 'RANDOM':
                return str(random.randint(0, 32767))
            return str(env.get(name, ''))
        def repl_plain(match):
            name = match.group(1)
            if name == 'RANDOM':
                return str(random.randint(0, 32767))
            return str(env.get(name, ''))
        text = re.sub(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}', repl_braced, text)
        text = re.sub(r'\$([A-Za-z_][A-Za-z0-9_]*)', repl_plain, text)
        return text

    def _host_files(self, host):
        return {f['path']: f for p in self.hosts[host]['ports'] for f in p.get('files', [])}

    def _resolve_path(self, cwd, raw, home=None):
        raw = (raw or '').strip().strip('"').strip("'")
        if not raw or raw == '.':
            return cwd
        if raw.startswith('~'):
            if not home:
                home = getattr(self, '_tilde_home', None)
            if not home:
                home = '/home/' + cwd.strip('/').split('/')[1] if cwd.startswith('/home/') else '/root'
            if raw == '~' or raw.startswith('~/'):
                raw = home + raw[1:]
            else:
                raw = '/home/' + raw[1:]
        if not raw.startswith('/'):
            raw = cwd.rstrip('/') + '/' + raw
        parts = []
        for item in raw.split('/'):
            if not item or item == '.':
                continue
            if item == '..':
                if parts:
                    parts.pop()
                continue
            parts.append(item)
        return '/' + '/'.join(parts)

    def _format_ls(self, host, path, long_format=False, directory_only=False):
        path = self._normalize_proc_path(path)
        files = self._host_files(host)
        user = self.hosts[host]['credential']['username']
        home = '/home/' + user
        entries = []
        # /proc/<pid>/{exe,cwd,root} are symlinks on a real host.
        proc_link = re.match(r'^/proc/(\d+)/(exe|cwd|root)$', path or '')
        if proc_link:
            pid, kind = proc_link.group(1), proc_link.group(2)
            target = {
                'exe': '/bin/bash' if pid not in {'1', '512', '2140'} else (
                    '/sbin/init' if pid == '1' else '/usr/sbin/sshd'),
                'cwd': home if pid not in {'1', '512', '2140'} else '/',
                'root': '/',
            }[kind]
            when = format_ls_mtime(self._clamp_mtime(None, host, path))
            name = PurePosixPath(path).name
            if long_format:
                return f'lrwxrwxrwx 1 root root {len(target)} {when} {name} -> {target}\n'
            return name + '\n'
        # Ubuntu 22.04: /bin and /sbin are symlinks into /usr.
        if directory_only and path in {'/bin', '/sbin'}:
            target = 'usr/bin' if path == '/bin' else 'usr/sbin'
            when = format_ls_mtime('2024-02-01T08:00:00Z')
            mode = 'lrwxrwxrwx'
            if long_format:
                return f'{mode} 1 root root {len(target)} {when} {PurePosixPath(path).name} -> {target}\n'
            return PurePosixPath(path).name + '\n'
        if directory_only and self._is_directory(host, path):
            mode = format_mode('0755', is_dir=True)
            when = format_ls_mtime(self._clamp_mtime(None, host, path))
            name = PurePosixPath(path).name or path
            if long_format:
                return f'{mode} 1 root root 4096 {when} {name}\n'
            return name + '\n'
        if path == '/':
            # Always render a normal Linux root directory, never dump lure absolute paths.
            mode = format_mode('0755', is_dir=True)
            names = ['bin', 'boot', 'dev', 'etc', 'home', 'lib', 'media', 'mnt',
                     'opt', 'proc', 'root', 'run', 'sbin', 'srv', 'sys', 'tmp', 'usr', 'var']
            # Include first-level lure parents that exist under /.
            for fpath in files:
                top = fpath.strip('/').split('/', 1)[0]
                if top and top not in names:
                    names.append(top)
            lines = []
            if long_format:
                lines.append('total ' + str(max(32, len(names) * 4)))
            for name in sorted(set(names)):
                if long_format:
                    # Irregular mtimes (hash-based) so the root listing does not look sequenced.
                    digest = hashlib.sha256(f'{host}|root|{name}'.encode()).hexdigest()
                    # Months 1-9 only: keep strictly before fixed lab clock 2024-10-13.
                    month = 1 + (int(digest[0:2], 16) % 9)
                    day = 1 + (int(digest[2:4], 16) % 28)
                    hour = int(digest[4:6], 16) % 24
                    minute = int(digest[6:8], 16) % 60
                    when = format_ls_mtime(f'2024-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:00Z')
                    owner = 'root'
                    lines.append(f"{mode} 1 {owner} {owner} 4096 {when} {name}")
                else:
                    lines.append(name)
            return '\n'.join(lines) + '\n'
        if path in {'/etc/ssh', '/etc/cron.d', '/etc/cron.daily', '/etc/cron.weekly', '/etc/cron.monthly'}:
            mode = format_mode('0755', is_dir=True)
            when = format_ls_mtime('2024-03-01T09:00:00Z')
            if path == '/etc/ssh':
                # Realistic OpenSSH install sizes: moduli is large, configs are small.
                entries = [
                    ('ssh_config', 1580, '2024-01-12T08:10:00Z'),
                    ('sshd_config', 3264, '2024-02-03T11:22:00Z'),
                    ('moduli', 276264, '2023-11-18T06:40:00Z'),
                ]
            else:
                entries = [('placeholder', 0, '2024-03-01T09:00:00Z')]
            lines = ['total ' + str(max(4, len(entries) * 4))] if long_format else []
            for name, size, stamp in entries:
                if name == 'placeholder' and path != '/etc/ssh':
                    if not long_format:
                        return '\n'
                    continue
                if long_format:
                    file_mode = format_mode('0644')
                    lines.append(f"{file_mode} 1 root root {size} {format_ls_mtime(stamp)} {name}")
                else:
                    lines.append(name)
            return ('\n'.join(lines) + '\n') if lines else '\n'
        if path in {'/home', home, '.'}:
            scoped = []
            for fpath, item in files.items():
                parent = str(PurePosixPath(fpath).parent)
                if path == '/home' and (fpath.startswith('/home/') or parent == '/home'):
                    # Only first-level home usernames.
                    scoped.append((fpath.strip('/').split('/')[1], item))
                elif path == home and (parent == home or fpath.startswith(home + '/')):
                    scoped.append((PurePosixPath(fpath).name, item))
                elif path == fpath or parent == path:
                    scoped.append((PurePosixPath(fpath).name, item))
            # Deduplicate directory names for /home.
            if path == '/home':
                uniq = {}
                for name, item in scoped:
                    uniq.setdefault(name, item)
                scoped = list(uniq.items())
            if path == home and not scoped:
                scoped = [(PurePosixPath(p).name, item) for p, item in files.items()
                          if str(PurePosixPath(p).parent) == home]
            lines = []
            if long_format:
                lines.append('total ' + str(max(4, len(scoped) * 4)))
            for name, item in sorted(scoped, key=lambda row: row[0]):
                meta = filesystem_metadata(item)
                full = (path.rstrip('/') + '/' + name) if path != '/' else '/' + name
                # If children exist under this name, it is a directory even when a
                # lure also materializes the same path as a file (e.g. /.ssh).
                is_dir = (path == '/home') or self._is_directory(host, full) or any(
                    f.startswith(full.rstrip('/') + '/') for f in files)
                owner = name if path == '/home' else self._path_owner(host, full, meta)
                mode_digits = '0755' if (path == '/home' or is_dir) else self._display_mode(user, full, meta)
                mode = format_mode(mode_digits, is_dir=(path == '/home' or is_dir))
                size = 4096 if (path == '/home' or is_dir) else len((item.get('content') or '').encode())
                when = format_ls_mtime(
                    self._clamp_mtime(meta.get('mtime') or '2024-06-10T09:00:00Z', host, full))
                if long_format:
                    lines.append(f"{mode} 1 {owner} {owner} {size} {when} {name}")
                else:
                    lines.append(name)
            if not lines:
                mode = format_mode('0755', is_dir=True)
                when = format_ls_mtime('2024-03-01T09:00:00Z')
                if path == '/home':
                    return f"total 4\n{mode} 1 root root 4096 {when} {user}\n"
                return f"total 8\n{format_mode('0644')} 1 {user} {user} 0 {when} .bashrc\n"
            return '\n'.join(lines) + '\n'
        # Prefer directory view when children exist, even if a lure file reuses the path.
        if self._is_directory(host, path) and (
                path not in files or any(f.startswith(path.rstrip('/') + '/') for f in files)):
            # Fall through to virtual/prefix directory rendering below when applicable.
            pass
        elif path in files:
            item = files[path]
            meta = filesystem_metadata(item)
            owner = meta.get('owner', user)
            # Paths under /home/<name>/ belong to that account, even if lure metadata drifts.
            parts = PurePosixPath(path).parts
            if len(parts) >= 3 and parts[1] == 'home' and parts[2] not in {'', '.', '..'}:
                owner = parts[2]
            mode = format_mode(meta.get('mode', '0640'))
            size = meta.get('size', len(item.get('content', '')))
            when = format_ls_mtime(self._clamp_mtime(meta.get('mtime'), host, path))
            name = PurePosixPath(path).name
            if long_format:
                return f"{mode} 1 {owner} {owner} {size} {when} {name}\n"
            return name + '\n'
        # Virtual kernel/system directories that must exist on a real Ubuntu rootfs.
        if path in {'/proc', '/sys', '/dev', '/run', '/tmp', '/var', '/var/log', '/var/backups',
                    '/opt', '/srv', '/mnt', '/media', '/boot', '/usr', '/usr/bin', '/usr/sbin',
                    '/bin', '/sbin', '/lib', '/lib64', '/etc/monit', '/etc/monit/conf.d',
                    '/etc/cron.d', '/etc/cron.daily', '/etc/cron.weekly', '/etc/cron.monthly',
                    '/etc/logrotate.d'}:
            return self._format_virtual_dir(host, path, long_format=long_format)
        common_bins = {
            '/bin/bash', '/bin/sh', '/bin/ls', '/bin/cat',
            '/usr/bin/sed', '/usr/bin/head', '/usr/bin/cat', '/usr/bin/stat', '/usr/bin/ls',
        }
        if path in common_bins:
            mode = format_mode('0755')
            digest = hashlib.sha256(f'{host}|bin|{path}'.encode()).hexdigest()
            when = format_ls_mtime(
                f'2024-{1 + int(digest[0:2], 16) % 9:02d}-{1 + int(digest[2:4], 16) % 27:02d}'
                f'T{8 + int(digest[4], 16) % 10:02d}:{int(digest[5:7], 16) % 60:02d}:00Z'
            )
            name = PurePosixPath(path).name
            size = 1396520 if name == 'bash' else (35000 + int(digest[8:12], 16) % 20000)
            if long_format:
                return f"{mode} 1 root root {size} {when} {name}\n"
            return name + '\n'
        # Directory prefix match
        children = []
        prefix = path.rstrip('/') + '/'
        for fpath, item in files.items():
            if fpath.startswith(prefix):
                rest = fpath[len(prefix):]
                name = rest.split('/', 1)[0]
                children.append((name, item))
        if children:
            uniq = {}
            for name, item in children:
                uniq.setdefault(name, item)
            lines = []
            if long_format:
                lines.append('total ' + str(max(4, len(uniq) * 4)))
            for name, item in sorted(uniq.items()):
                meta = filesystem_metadata(item)
                full = path.rstrip('/') + '/' + name
                is_dir = self._is_directory(host, full) or any(
                    f.startswith(full.rstrip('/') + '/') for f in files)
                owner = self._path_owner(host, full, meta)
                mode_digits = '0755' if is_dir else self._display_mode(user, full, meta)
                mode = format_mode(mode_digits, is_dir=is_dir)
                size = 4096 if is_dir else len((item.get('content') or '').encode())
                when = format_ls_mtime(self._clamp_mtime(meta.get('mtime'), host, full))
                if long_format:
                    lines.append(f"{mode} 1 {owner} {owner} {size} {when} {name}")
                else:
                    lines.append(name)
            if long_format and lines:
                # Prepend . and .. like GNU ls -la.
                when = format_ls_mtime(self._clamp_mtime(None, host, path))
                owner = self._path_owner(host, path)
                dot = f"{format_mode('0755', is_dir=True)} 1 {owner} {owner} 4096 {when}"
                lines.insert(1, f"{dot} .")
                lines.insert(2, f"{dot} ..")
                # Fix total to include dots.
                lines[0] = 'total ' + str(max(4, (len(lines) - 1) * 4))
            return '\n'.join(lines) + '\n'
        return f'ls: cannot access {path}: No such file or directory\n'

    def _clamp_mtime(self, value, host, key):
        """Force displayed mtimes strictly before the fixed lab clock 2024-10-13."""
        from .anti_fingerprint import parse_mtime
        lab = datetime.datetime(2024, 10, 13, 9, 15, 1, tzinfo=datetime.timezone.utc)
        stamp = parse_mtime(value)
        if stamp is not None and stamp < lab:
            return value
        digest = hashlib.sha256(f'{host}|mtime|{key}|{value}'.encode()).hexdigest()
        month = 1 + (int(digest[0:2], 16) % 9)
        day = 1 + (int(digest[2:4], 16) % 27)
        hour = int(digest[4:6], 16) % 24
        minute = int(digest[6:8], 16) % 60
        return f'2024-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:00Z'

    def _format_virtual_dir(self, host, path, long_format=False):
        mode = format_mode('0755', is_dir=True)
        digest = hashlib.sha256(f'{host}|vdir|{path}'.encode()).hexdigest()
        when = format_ls_mtime(self._clamp_mtime(None, host, path))
        if path == '/proc':
            names = ['1', 'self', 'cpuinfo', 'meminfo', 'mounts', 'net', 'stat',
                     'uptime', 'version', 'filesystems', 'loadavg']
        elif path == '/dev':
            names = ['null', 'zero', 'urandom', 'random', 'tty', 'pts', 'shm']
        elif path == '/sys':
            names = ['block', 'bus', 'class', 'devices', 'fs', 'kernel']
        elif path == '/run':
            names = ['sshd', 'systemd', 'user']
        elif path in {'/tmp', '/var/backups', '/opt', '/srv', '/mnt', '/media'}:
            names = []
        elif path == '/var':
            names = ['backups', 'cache', 'lib', 'log', 'tmp']
        elif path == '/var/log':
            names = ['auth.log', 'syslog', 'kern.log']
        elif path == '/etc/monit':
            names = ['monitrc', 'conf.d']
        elif path == '/etc/monit/conf.d':
            names = ['sshd']
        elif path in {'/etc/cron.d', '/etc/cron.daily', '/etc/cron.weekly', '/etc/cron.monthly'}:
            names = ['.placeholder']
        elif path == '/etc/logrotate.d':
            names = ['rsyslog', 'apt']
        elif path == '/boot':
            names = ['grub', 'vmlinuz', 'initrd.img']
        elif path in {'/usr', '/usr/bin', '/usr/sbin', '/bin', '/sbin', '/lib', '/lib64'}:
            # Ubuntu 22.04 merged /bin -> usr/bin; keep a shallow but sized listing.
            names = ['bash', 'sh', 'ls', 'cat', 'dash', 'sleep', 'uname'] if path.endswith('bin') else [
                'bin', 'lib', 'share', 'local']
            if path in {'/lib', '/lib64'}:
                names = ['x86_64-linux-gnu']
            if path == '/usr':
                names = ['bin', 'sbin', 'lib', 'local', 'share']
            if path == '/sbin':
                names = ['init', 'sshd', 'agetty']
        else:
            names = []
        bin_sizes = {
            'bash': 1396520, 'sh': 125686, 'dash': 125686, 'ls': 138208, 'cat': 39232,
            'sleep': 35000, 'uname': 39520, 'init': 948576, 'sshd': 892000, 'agetty': 51200,
        }
        lines = []
        if long_format:
            lines.append('total ' + str(max(4, sum(max(4, bin_sizes.get(n, 4) // 1024) for n in names) or 4)))
            for i, name in enumerate(names):
                entry_mode = format_mode('0755', is_dir=name.isdigit() or name in {
                    'self', 'net', 'pts', 'shm', 'sshd', 'systemd', 'user', 'block', 'bus',
                    'class', 'devices', 'fs', 'kernel', 'backups', 'cache', 'lib', 'log',
                    'tmp', 'grub', 'bin', 'sbin', 'share', 'local', 'x86_64-linux-gnu',
                    'conf.d', 'conf-enabled'})
                # /etc/monit/conf.d/sshd is a small config file, not the sshd binary.
                if path == '/etc/monit/conf.d' and name == 'sshd':
                    entry_mode = format_mode('0644')
                    size = len((self._system_file(host, '/etc/monit/conf.d/sshd') or '').encode())
                elif name.endswith('.log') or name in {'vmlinuz', 'initrd.img'}:
                    entry_mode = format_mode('0644' if name.endswith('.log') else '0755')
                    size = 4096 if entry_mode.startswith('d') else bin_sizes.get(
                        name, 120 + (int(digest[i % 16:(i % 16) + 2], 16) % 800))
                elif name in bin_sizes and path.endswith('bin'):
                    entry_mode = format_mode('0755')
                    size = bin_sizes.get(name)
                else:
                    size = 4096 if entry_mode.startswith('d') else bin_sizes.get(
                        name, 120 + (int(digest[i % 16:(i % 16) + 2], 16) % 800))
                if path == '/etc/monit' and name == 'monitrc':
                    entry_mode = format_mode('0644')
                    size = len((self._system_file(host, '/etc/monit/monitrc') or '').encode())
                entry_when = when
                if path == '/var/log' and name.endswith('.log'):
                    body = self._system_file(host, f'/var/log/{name}') or ''
                    size = len(body.encode())
                    # Match the Jul 10 stamps used in synthetic log bodies.
                    entry_when = format_ls_mtime('2024-07-10T04:17:01Z')
                owner = 'root'
                lines.append(f'{entry_mode} 1 {owner} {owner} {size} {entry_when} {name}')
        else:
            lines.extend(names)
        return ('\n'.join(lines) + '\n') if lines else '\n'

    def _system_file(self, host, path):
        """Ordinary OS files that attackers probe for fingerprinting."""
        user = self.hosts[host]['credential']['username']
        ip = self.hosts[host].get('ip', '10.77.0.10')
        if path == '/etc/hosts':
            return (
                '127.0.0.1\tlocalhost\n'
                f'{ip}\t{host}\n'
                '::1\tlocalhost ip6-localhost ip6-loopback\n'
            )
        if path == '/etc/hostname':
            return host + '\n'
        if path == '/etc/os-release':
            custom = self.hosts[host].get('os_release')
            if custom:
                return custom if str(custom).endswith('\n') else str(custom) + '\n'
            os_name = self.hosts[host].get('os') or 'Ubuntu 22.04.4 LTS'
            if 'Debian' in str(os_name) or str(self.hosts[host].get('os_id') or '') == 'debian':
                return (
                    'PRETTY_NAME="%s"\n'
                    'NAME="Debian GNU/Linux"\n'
                    'VERSION_ID="8"\n'
                    'VERSION="8 (jessie)"\n'
                    'ID=debian\n'
                    'HOME_URL="https://www.debian.org/"\n'
                    'SUPPORT_URL="https://www.debian.org/support"\n'
                ) % os_name
            return (
                'PRETTY_NAME="%s"\n'
                'NAME="Ubuntu"\n'
                'VERSION_ID="22.04"\n'
                'VERSION="22.04.4 LTS (Jammy Jellyfish)"\n'
                'VERSION_CODENAME=jammy\n'
                'ID=ubuntu\n'
                'ID_LIKE=debian\n'
                'HOME_URL="https://www.ubuntu.com/"\n'
                'SUPPORT_URL="https://help.ubuntu.com/"\n'
            ) % os_name
        if path == '/proc/version':
            return (
                f'Linux version 5.15.0-97-generic (buildd@lcy02-amd64-001) '
                f'(gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) '
                f'#107-Ubuntu SMP {host}\n'
            )
        if path == '/proc/1/cgroup':
            return (
                '0::/init.scope\n'
                '1:name=systemd:/init.scope\n'
            )
        if path == '/proc/mounts':
            return (
                'sysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0\n'
                'proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0\n'
                'udev /dev devtmpfs rw,nosuid,relatime 0 0\n'
                '/dev/sda1 / ext4 rw,relatime 0 0\n'
            )
        if path == '/proc/net/tcp':
            return (
                '  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode\n'
                '   0: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 12345 1 0000000000000000 100 0 0 10 0\n'
            )
        if path == '/proc/uptime':
            return '1046701.12 3988211.45\n'
        proc_file = re.match(r'^/proc/(self|\d+)/(exe|cmdline|cwd|comm|status)$', path or '')
        if proc_file:
            pid = proc_file.group(1)
            kind = proc_file.group(2)
            if pid == 'self':
                pid = '2145'
            if kind == 'cmdline':
                if pid in {'1'}:
                    return '/sbin/init\0'
                if pid in {'512', '2140'}:
                    return 'sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\0'
                return '-bash\0'
            if kind == 'comm':
                if pid == '1':
                    return 'systemd\n'
                if pid in {'512', '2140', '2144'}:
                    return 'sshd\n'
                return 'bash\n'
            if kind == 'cwd':
                return f'/home/{user}\n' if pid not in {'1', '512'} else '/\n'
            if kind == 'status':
                name = 'bash' if pid not in {'1', '512', '2140', '2144'} else ('systemd' if pid == '1' else 'sshd')
                ppid = '2144' if name == 'bash' else ('1' if name == 'sshd' else '0')
                return (
                    f'Name:\t{name}\n'
                    f'State:\tS (sleeping)\n'
                    f'Tgid:\t{pid}\n'
                    f'Pid:\t{pid}\n'
                    f'PPid:\t{ppid}\n'
                    f'Uid:\t{0 if name != "bash" else 1000}\t{0 if name != "bash" else 1000}\t'
                    f'{0 if name != "bash" else 1000}\t{0 if name != "bash" else 1000}\n'
                )
            # exe is a symlink; cat follows to binary and typically permission-denies for ELF.
            return 'cat: %s: Permission denied\n' % path
        if path == '/etc/group':
            return (
                'root:x:0:\n'
                'daemon:x:1:\n'
                'bin:x:2:\n'
                'sys:x:3:\n'
                'adm:x:4:\n'
                f'{user}:x:1000:\n'
            )
        if path == '/etc/ops/maintenance.conf':
            return (
                f'# {host} maintenance window\n'
                'owner=firewall-oncall\n'
                'revision=2024-03-18\n'
                'ticket=CHG2916\n'
                'services=ssh,monit\n'
                'next_window=Sun 02:00-04:00 local\n'
                '# related ticket notes: /home/admin/.ssh/ticket-CHG2916.txt\n'
            )
        if path in {'/etc/monit/monitrc', '/etc/monit/conf.d/sshd'}:
            # Notes mention monit; keep list/read consistent with systemctl stub.
            if path.endswith('monitrc'):
                return (
                    'set daemon 60\n'
                    'set logfile /var/log/monit.log\n'
                    'include /etc/monit/conf.d/*\n'
                    '# ops follow-up: /etc/monit/conf.d/sshd\n'
                )
            return (
                'check process sshd with pidfile /run/sshd.pid\n'
                '    start program = "/usr/sbin/service ssh start"\n'
                '    stop program  = "/usr/sbin/service ssh stop"\n'
                '# maintenance window file: /etc/ops/maintenance.conf\n'
            )
        if path in {'/var/log/auth.log', '/var/log/syslog', '/var/log/kern.log'}:
            # Must stay readable after ls /var/log so list-vs-read cannot diverge.
            stamp = 'Jul 10 04:17:01'
            if path.endswith('auth.log'):
                return (
                    f'{stamp} {host} sshd[1422]: Accepted password for {user} '
                    f'from 10.77.0.5 port 52114 ssh2\n'
                    f'{stamp} {host} sshd[1422]: pam_unix(sshd:session): '
                    f'session opened for user {user}(uid=1000) by (uid=0)\n'
                    f'{stamp} {host} systemd-logind[811]: New session 12 of user {user}.\n'
                )
            if path.endswith('syslog'):
                return (
                    f'{stamp} {host} systemd[1]: Started Session 12 of User {user}.\n'
                    f'{stamp} {host} CRON[2201]: (root) CMD (cd / && run-parts '
                    f'--report /etc/cron.hourly)\n'
                )
            return (
                f'{stamp} {host} kernel: [    0.000000] Linux version 5.15.0-97-generic\n'
                f'{stamp} {host} kernel: [    0.000000] Command line: BOOT_IMAGE=/vmlinuz '
                f'root=/dev/sda1\n'
            )
        if path == '/etc/ssh/sshd_config':
            return (
                'Port 22\n'
                'PermitRootLogin no\n'
                'PasswordAuthentication yes\n'
                'ChallengeResponseAuthentication no\n'
                'UsePAM yes\n'
                'X11Forwarding yes\n'
                'PrintMotd no\n'
                'AcceptEnv LANG LC_*\n'
                'Subsystem sftp /usr/lib/openssh/sftp-server\n'
            )
        if path == '/etc/ssh/moduli':
            # Large-enough placeholder so ls size does not look identical to configs.
            rows = []
            for i in range(40):
                rows.append(f'20230312000000 {2048 + i} 2 100 {1000 + i} 5 {i} moduli-placeholder-{i:04d}-{"ab"*32}')
            return '\n'.join(rows) + '\n'
        if path == '/etc/ssh/ssh_config':
            return (
                'Host *\n'
                '    SendEnv LANG LC_*\n'
                '    HashKnownHosts yes\n'
                '    GSSAPIAuthentication yes\n'
            )
        if path == '/etc/debian_version':
            if (self.hosts[host].get('os_id') == 'debian'
                    or 'Debian' in str(self.hosts[host].get('os') or '')):
                return '8.11\n'
            return None
        if path == '/etc/resolv.conf':
            if self.hosts[host].get('os_id') == 'debian':
                return 'nameserver 10.0.2.3\n'
            return 'nameserver 127.0.0.53\noptions edns0\n'
        if path == '/proc/cmdline':
            kernel = str(self.hosts[host].get('kernel') or '5.15.0-97-generic')
            if ' ' in kernel:
                kernel = kernel.split()[0]
            return f'BOOT_IMAGE=/boot/vmlinuz-{kernel} root=/dev/sda1 ro quiet\n'
        if path == '/proc/meminfo':
            if self.hosts[host].get('os_id') == 'debian' and host != 'userdb':
                return (
                    'MemTotal:         505880 kB\n'
                    'MemFree:          307912 kB\n'
                    'MemAvailable:     452592 kB\n'
                    'Buffers:           22108 kB\n'
                    'Cached:           122572 kB\n'
                    'SwapCached:            0 kB\n'
                    'Active:            88760 kB\n'
                    'Inactive:          64100 kB\n'
                    'SwapTotal:        524284 kB\n'
                    'SwapFree:         524284 kB\n'
                )
            return (
                'MemTotal:         513628 kB\n'
                'MemFree:          301204 kB\n'
                'MemAvailable:     410112 kB\n'
                'Buffers:           22108 kB\n'
                'Cached:            98044 kB\n'
                'SwapCached:            0 kB\n'
                'Active:            88760 kB\n'
                'Inactive:          64100 kB\n'
                'SwapTotal:        524284 kB\n'
                'SwapFree:         524284 kB\n'
            )
        if path == '/proc/cpuinfo':
            def _cpu(idx, vendor, family, model, model_name, stepping, microcode):
                return (
                    f'processor\t: {idx}\n'
                    f'vendor_id\t: {vendor}\n'
                    f'cpu family\t: {family}\n'
                    f'model\t\t: {model}\n'
                    f'model name\t: {model_name}\n'
                    f'stepping\t: {stepping}\n'
                    f'microcode\t: {microcode}\n'
                    'cpu MHz\t\t: 2194.918\n'
                    'cache size\t: 4096 KB\n'
                    f'physical id\t: {idx}\n'
                    'siblings\t: 1\n'
                    'core id\t\t: 0\n'
                    'cpu cores\t: 1\n'
                    f'apicid\t\t: {idx}\n'
                    f'initial apicid\t: {idx}\n'
                    'fpu\t\t: yes\n'
                    'fpu_exception\t: yes\n'
                    'cpuid level\t: 13\n'
                    'wp\t\t: yes\n'
                    'bogomips\t: 4389.83\n'
                    '\n'
                )
            if self.hosts[host].get('os_id') == 'debian' and host != 'userdb':
                block = _cpu(0, 'GenuineIntel', '6', '94', 'Intel(R) Xeon(R) CPU E3-1270 v5 @ 3.60GHz', '3', '0x1')
                return block
            model = ('Common KVM processor'
                     if self.hosts[host].get('os_id') == 'debian'
                     else 'Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz')
            return _cpu(0, 'GenuineIntel', '6', '6', model, '3', '0x1') + _cpu(1, 'GenuineIntel', '6', '6', model, '3', '0x1')
        if path == '/etc/issue':
            issue = self.hosts[host].get('issue')
            if issue:
                return issue if str(issue).endswith('\n') else str(issue) + '\n'
            os_name = self.hosts[host].get('os') or 'Ubuntu 22.04.4 LTS'
            if 'Debian' in str(os_name):
                return 'Debian GNU/Linux 8 \\n \\l\n'
            return 'Ubuntu 22.04.4 LTS \\n \\l\n'
        if path == '/etc/motd':
            return ''
        if path == '/etc/passwd':
            # /home/<user>/... -> parts ('/', 'home', '<user>', ...); use parts[2].
            homes = sorted({
                PurePosixPath(p).parts[2]
                for p in self._host_files(host)
                if p.startswith('/home/') and len(PurePosixPath(p).parts) >= 3
                and PurePosixPath(p).parts[2] not in {'', '.', '..'}
            })
            lines = [
                'root:x:0:0:root:/root:/bin/bash\n',
                'daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n',
                'bin:x:2:2:bin:/bin:/usr/sbin/nologin\n',
                'sys:x:3:3:sys:/dev:/usr/sbin/nologin\n',
                'sync:x:4:65534:sync:/bin:/bin/sync\n',
                'games:x:5:60:games:/usr/games:/usr/sbin/nologin\n',
                'man:x:6:12:man:/var/cache/man:/usr/sbin/nologin\n',
                'lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\n',
                'mail:x:8:8:mail:/var/mail:/usr/sbin/nologin\n',
                'news:x:9:9:news:/var/spool/news:/usr/sbin/nologin\n',
                'uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\n',
                'proxy:x:13:13:proxy:/bin:/usr/sbin/nologin\n',
                'www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\n',
                'backup:x:34:34:backup:/var/backups:/usr/sbin/nologin\n',
                'list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\n',
                'irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\n',
                'gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\n',
                'nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n',
                'systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin\n',
                'systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin\n',
                'messagebus:x:102:105::/nonexistent:/usr/sbin/nologin\n',
                'syslog:x:103:106::/home/syslog:/usr/sbin/nologin\n',
                '_apt:x:104:65534::/nonexistent:/usr/sbin/nologin\n',
                'tss:x:105:111:TPM software stack,,,:/var/lib/tpm:/bin/false\n',
                'uuidd:x:106:112::/run/uuidd:/usr/sbin/nologin\n',
                'tcpdump:x:107:113::/nonexistent:/usr/sbin/nologin\n',
                'sshd:x:108:65534::/run/sshd:/usr/sbin/nologin\n',
            ]
            # Session user is always the first human account (uid/gid 1000), matching `id`.
            uid = 1000
            seen = {'root'}
            for name in [user] + [h for h in homes if h != user]:
                if name in seen:
                    continue
                seen.add(name)
                gecos = ('Vagrant Default User,,,'
                         if self.hosts[host].get('os_id') == 'debian' and name == 'vagrant'
                         else name)
                lines.append(f'{name}:x:{uid}:{uid}:{gecos}:/home/{name}:/bin/bash\n')
                uid += 1
            return ''.join(lines)
        if path == '/etc/crontab':
            return (
                '# /etc/crontab: system-wide crontab\n'
                'SHELL=/bin/sh\n'
                'PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\n'
                '17 *\t* * *\troot    cd / && run-parts --report /etc/cron.hourly\n'
                '25 6\t* * *\troot\ttest -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )\n'
            )
        if path == '/etc/shadow':
            homes = sorted({
                PurePosixPath(p).parts[2]
                for p in self._host_files(host)
                if p.startswith('/home/') and len(PurePosixPath(p).parts) >= 3
                and PurePosixPath(p).parts[2] not in {'', '.', '..', user}
            })
            lines = [
                'root:*:19600:0:99999:7:::\n',
                f'{user}:*:19600:0:99999:7:::\n',
            ]
            for name in homes:
                lines.append(f'{name}:*:19600:0:99999:7:::\n')
            return ''.join(lines)
        if path in {f'/home/{user}/.bashrc', '/root/.bashrc'}:
            return '# ~/.bashrc: executed by bash(1) for non-login shells.\n'
        return None

    def _known_dirs(self, host):
        files = self._host_files(host)
        dirs = {
            '/', '/bin', '/sbin', '/usr', '/usr/bin', '/usr/sbin', '/etc', '/home', '/var',
            '/var/log', '/var/backups', '/tmp', '/opt', '/srv', '/mnt', '/media', '/boot',
            '/dev', '/proc', '/sys', '/run', '/lib', '/lib64', '/root',
        }
        for path in files:
            parent = str(PurePosixPath(path).parent)
            while parent and parent != '/':
                dirs.add(parent)
                parent = str(PurePosixPath(parent).parent)
            # Also treat first-level lure parents as directories.
            parts = PurePosixPath(path).parts
            if len(parts) >= 3:
                dirs.add('/' + '/'.join(parts[1:3]))
        return dirs

    def _is_directory(self, host, path):
        path = path.rstrip('/') or '/'
        if path in self._known_dirs(host):
            return True
        files = self._host_files(host)
        prefix = path.rstrip('/') + '/'
        return any(f.startswith(prefix) for f in files)

    def _normalize_proc_path(self, path):
        if path == '/proc/self' or path.startswith('/proc/self/'):
            return '/proc/2145' + path[len('/proc/self'):]
        return path

    def _path_owner(self, host, path, meta=None):
        parts = PurePosixPath(path).parts
        if len(parts) >= 3 and parts[1] == 'home' and parts[2] not in {'', '.', '..'}:
            return parts[2]
        if meta and meta.get('owner'):
            return meta.get('owner')
        if host and host in self.hosts:
            return self.hosts[host]['credential']['username']
        return 'root'

    def _display_mode(self, session_user, path, meta):
        """Mode shown in ls/stat; cross-home served lures look 644 so mode matches access."""
        raw = str((meta or {}).get('mode', '0640'))
        owner = self._path_owner('', path, meta)
        digits = ''.join(ch for ch in raw if ch.isdigit())[-3:] or '640'
        if owner != session_user and path.startswith('/home/') and len(PurePosixPath(path).parts) >= 4:
            return '0644'
        return digits

    def _mtime_for(self, host, path, meta=None):
        """Single source of truth for ls/stat mtimes (always before lab clock)."""
        meta = meta or {}
        clamped = self._clamp_mtime(meta.get('mtime'), host, path)
        from .anti_fingerprint import parse_mtime
        stamp = parse_mtime(clamped)
        if stamp is None:
            return '2024-03-01 09:00:00.000000000 +0000'
        return stamp.strftime('%Y-%m-%d %H:%M:%S') + '.000000000 +0000'

    def _mode_human(self, digits):
        digits = ''.join(ch for ch in str(digits) if ch.isdigit())[-3:].zfill(3)
        mapping = {
            '0': '---', '1': '--x', '2': '-w-', '3': '-wx',
            '4': 'r--', '5': 'r-x', '6': 'rw-', '7': 'rwx',
        }
        return ''.join(mapping.get(ch, '---') for ch in digits)

    def _read_file(self, session, host, path, display=None):
        path = self._normalize_proc_path(path)
        shown = display or path
        vfs = self.vfs.get(host)
        if vfs is not None:
            node = vfs.get(path)
            if node is None:
                return {'handled': True, 'output': f'cat: {shown}: {self._enoent(host)}\n',
                        'trap_trigger': False}
            if node.is_dir:
                return {'handled': True, 'output': f'cat: {shown}: Is a directory\n',
                        'trap_trigger': False}
            session_user = self.hosts[host]['credential']['username']
            digits = ''.join(ch for ch in str(node.mode) if ch.isdigit())[-3:]
            if (path in {'/var/log/syslog', '/var/log/auth.log', '/var/log/kern.log'}
                    and session_user != 'root'):
                return {'handled': True,
                        'output': f'cat: {path}: Permission denied\n',
                        'trap_trigger': False}
            if node.owner != session_user and digits in {'600', '0600', '640', '0640'}:
                return {'handled': True,
                        'output': f'cat: {path}: Permission denied\n',
                        'trap_trigger': False}
            content = node.content or ''
            return {'handled': True,
                    'output': content if content.endswith('\n') else content + '\n',
                    'trap_trigger': False}
        synthetic = self._system_file(host, path)
        if synthetic is not None:
            return {'handled': True, 'output': synthetic, 'trap_trigger': False}
        if self._is_directory(host, path):
            return {'handled': True, 'output': f'cat: {path}: Is a directory\n',
                    'trap_trigger': False}
        files = self._host_files(host)
        item = files.get(path)
        if item is None:
            return {'handled': True, 'output': f'cat: {path}: {self._enoent(host)}\n',
                    'trap_trigger': False}
        reply = self.interact(session, {'op': 'read', 'host': host, 'path': path}, source='ssh')
        content = reply.get('content', '')
        links = item.get('runtime_links') or []
        # Avoid dumping controller-facing hop comments that look synthetic.
        # Keep lure content; lateral clues stay inside ordinary config language.
        if links:
            for link in links:
                if link.get('kind') == 'credential' and 'maintenance hop' not in content:
                    content = content.rstrip() + (
                        f"\n# peer={link.get('host')} account=service-rotate\n")
                elif link.get('path') and link['path'] not in content:
                    content = content.rstrip() + f"\n# include {link['path']}\n"
        return {'handled': True, 'output': content if content.endswith('\n') else content + '\n',
                'trap_trigger': bool(links)}

    def _tokenize(self, text):
        """Quote-aware tokenization for simple interactive commands."""
        tokens, buf, quote = [], [], None
        i = 0
        n = len(text or '')
        while i < n:
            ch = text[i]
            if quote:
                if ch == quote:
                    quote = None
                else:
                    buf.append(ch)
                i += 1
                continue
            if ch in {'"', "'"}:
                quote = ch
                i += 1
                continue
            if ch.isspace():
                if buf:
                    tokens.append(''.join(buf))
                    buf = []
                i += 1
                continue
            if ch in {'>', '<'}:
                if buf:
                    tokens.append(''.join(buf))
                    buf = []
                if i + 1 < n and text[i + 1] == ch:
                    tokens.append(ch + ch)
                    i += 2
                    continue
                if i + 1 < n and text[i + 1] == '&':
                    tokens.append(ch + '&')
                    i += 2
                    continue
                tokens.append(ch)
                i += 1
                continue
            buf.append(ch)
            i += 1
        if buf:
            tokens.append(''.join(buf))
        return tokens

    @staticmethod
    def _shell_join(tokens):
        out = []
        for t in tokens:
            if any(ch in t for ch in ' \t;|&<>$`"\'()'):
                out.append("'" + str(t).replace("'", "'\\''") + "'")
            else:
                out.append(str(t))
        return ' '.join(out)

    def _strip_redirections(self, text):
        """Drop common interactive redirections so args are not eaten as filenames."""
        text = re.sub(r'(?:^|\s)(?:2>&1|&>/dev/null|2>/dev/null|>/dev/null|</dev/null)\b', ' ', text)
        return re.sub(r'\s+', ' ', text).strip()

    def _rewrite_for_loops(self, session, host, text):
        pattern = re.compile(r'for\s+[A-Za-z_][A-Za-z0-9_]*\s+in\s+.+?;\s*do\s+.+?;\s*done', re.S)
        def repl(match):
            cmds = self._expand_simple_for_loop(match.group(0), session=session, host=host)
            if not cmds:
                return match.group(0)
            return '; '.join(cmds)
        return pattern.sub(repl, text or '')

    def _expand_simple_for_loop(self, text, session=None, host=None):
        """Expand `for x in a b; do CMD; done` into sequential commands when simple."""
        m = re.match(
            r'^\s*for\s+([A-Za-z_][A-Za-z0-9_]*)\s+in\s+(.+?)\s*;\s*do\s+(.+?)\s*;\s*done\s*$',
            (text or '').strip(),
            re.S,
        )
        if not m:
            return None
        var, values_raw, body = m.group(1), m.group(2).strip(), m.group(3).strip()
        # Values: whitespace-separated tokens or glob-like paths already expanded by attacker.
        values = []
        quote = None
        buf = []
        for ch in values_raw:
            if quote:
                buf.append(ch)
                if ch == quote:
                    quote = None
                continue
            if ch in {'"', "'"}:
                quote = ch
                continue
            if ch.isspace():
                if buf:
                    values.append(''.join(buf))
                    buf = []
                continue
            buf.append(ch)
        if buf:
            values.append(''.join(buf))
        if not values or len(values) > 40:
            return None
        # Expand globs like ~/.ssh/* against VFS when possible.
        expanded_values = []
        cwd = '/home/' + (self.hosts[host]['credential']['username'] if host else 'ops')
        if session and host:
            cwd = self._session_state(session, host).get('cwd') or cwd
        for value in values:
            if '*' in value or '?' in value:
                path = value
                if path.startswith('~/') and host:
                    user = self.hosts[host]['credential']['username']
                    path = f'/home/{user}/{path[2:]}'
                elif host and not path.startswith('/'):
                    path = str(PurePosixPath(cwd) / path)
                parent = str(PurePosixPath(path).parent)
                pat = PurePosixPath(path).name
                vfs = self.vfs.get(host) if host else None
                if vfs is not None and vfs.is_dir(parent):
                    hits = [child.path for child in vfs.listdir(parent)
                            if fnmatch.fnmatch(PurePosixPath(child.path).name, pat)]
                    expanded_values.extend(hits or [value])
                else:
                    expanded_values.append(value)
            else:
                expanded_values.append(value)
        values = expanded_values[:40]
        cmds = []
        for value in values:
            piece = body
            piece = piece.replace(f'"${var}"', value).replace(f"'${var}'", value)
            piece = piece.replace(f'${{{var}}}', value).replace(f'${var}', value)
            cmds.append(piece)
        return cmds

    @staticmethod
    def _new_shell_scan():
        return {'quote': None, 'subst': 0, 'tick': False, 'brace': 0}

    @staticmethod
    def _shell_scan_push(state, text, i):
        """Consume quoted / $(...) / `...` / ${...} regions. Returns (new_i, nested)."""
        n = len(text)
        ch = text[i]
        if state['quote']:
            if ch == state['quote']:
                state['quote'] = None
            return i + 1, True
        if state['tick']:
            if ch == '`':
                state['tick'] = False
            return i + 1, True
        if state['subst']:
            if ch == '(':
                state['subst'] += 1
            elif ch == ')':
                state['subst'] -= 1
            return i + 1, True
        if state['brace']:
            if ch == '{':
                state['brace'] += 1
            elif ch == '}':
                state['brace'] -= 1
            return i + 1, True
        if ch in {'"', "'"}:
            state['quote'] = ch
            return i + 1, True
        if ch == '`':
            state['tick'] = True
            return i + 1, True
        if ch == '$' and i + 1 < n and text[i + 1] == '(':
            state['subst'] = 1
            return i + 2, True
        if ch == '$' and i + 1 < n and text[i + 1] == '{':
            state['brace'] = 1
            return i + 2, True
        return i, False

    def _unset_redirect_var(self, text, env):
        """Return `$NAME` when a redirect target is an empty/unset variable."""
        env = env or {}
        i = 0
        n = len(text or '')
        state = self._new_shell_scan()
        while i < n:
            new_i, nested = self._shell_scan_push(state, text, i)
            if nested:
                i = new_i
                continue
            ch = text[i]
            if ch in {'>', '<'} and not (ch == '<' and i + 1 < n and text[i + 1] in {'(', '>', '&'}):
                j = i
                if j + 1 < n and text[j + 1] == ch:
                    j += 1
                j += 1
                while j < n and text[j].isspace():
                    j += 1
                if j < n and text[j] == '$':
                    m = re.match(r'\$([A-Za-z_][A-Za-z0-9_]*)', text[j:])
                    if m and not str(env.get(m.group(1) or '', '')).strip():
                        return m.group(0)
                i = j if j > i else i + 1
                continue
            i += 1
        return None

    def _input_redirect_file(self, text):
        """Filename of `< file` outside quotes / $() / process substitution."""
        i = 0
        n = len(text or '')
        state = self._new_shell_scan()
        while i < n:
            new_i, nested = self._shell_scan_push(state, text, i)
            if nested:
                i = new_i
                continue
            ch = text[i]
            if ch == '<' and not (i + 1 < n and text[i + 1] in {'<', '>', '(', '&'}):
                j = i + 1
                while j < n and text[j].isspace():
                    j += 1
                if j < n and text[j] not in {'<', '>', '(', '&', ';', '|'}:
                    k = j
                    while k < n and not text[k].isspace() and text[k] not in {';', '|', '&', '>', '<'}:
                        k += 1
                    name = text[j:k].strip('\'"')
                    if name and not name.startswith('$(') and not name.startswith('<'):
                        return name
                i = j if j > i else i + 1
                continue
            i += 1
        return None

    def _proc_subst_inners(self, text):
        """Inner commands of `<(...)` process substitutions."""
        inners = []
        i = 0
        n = len(text or '')
        state = self._new_shell_scan()
        while i < n:
            new_i, nested = self._shell_scan_push(state, text, i)
            if nested:
                i = new_i
                continue
            if text.startswith('<(', i):
                depth = 1
                j = i + 2
                while j < n and depth:
                    if text[j] == '(':
                        depth += 1
                    elif text[j] == ')':
                        depth -= 1
                    j += 1
                inners.append(text[i + 2:j - 1].strip())
                i = j
                continue
            i += 1
        return inners

    def _split_semicolons(self, text):
        """Split on ; outside quotes / $() so awk/find -exec scripts keep their semicolons."""
        parts, buf = [], []
        i = 0
        n = len(text or '')
        state = self._new_shell_scan()
        while i < n:
            new_i, nested = self._shell_scan_push(state, text, i)
            if nested:
                buf.append(text[i:new_i])
                i = new_i
                continue
            ch = text[i]
            if ch == ';':
                if buf and buf[-1] == '\\':
                    buf.append(ch)
                    i += 1
                    continue
                part = ''.join(buf).strip()
                if part:
                    parts.append(part)
                buf = []
                i += 1
                continue
            buf.append(ch)
            i += 1
        tail = ''.join(buf).strip()
        if tail:
            parts.append(tail)
        return parts or [text]

    def _split_pipeline(self, text):
        """Split on | / |& outside quotes and $(), so `cmd $(a | b)` stays one atom."""
        stages, buf = [], []
        i = 0
        n = len(text or '')
        state = self._new_shell_scan()
        while i < n:
            new_i, nested = self._shell_scan_push(state, text, i)
            if nested:
                buf.append(text[i:new_i])
                i = new_i
                continue
            ch = text[i]
            if ch == '|' and not (i + 1 < n and text[i + 1] == '|'):
                stage = ''.join(buf).strip()
                if stage:
                    stages.append(stage)
                buf = []
                i += 2 if i + 1 < n and text[i + 1] == '&' else 1
                continue
            buf.append(ch)
            i += 1
        tail = ''.join(buf).strip()
        if tail:
            stages.append(tail)
        return stages

    def _split_bool_ops(self, text):
        """Split on && / || outside quotes / $(). Returns [(op, chunk), ...] left-to-right."""
        parts, buf = [], []
        pending = 'then'
        i = 0
        n = len(text or '')
        state = self._new_shell_scan()
        while i < n:
            new_i, nested = self._shell_scan_push(state, text, i)
            if nested:
                buf.append(text[i:new_i])
                i = new_i
                continue
            if text.startswith('&&', i):
                parts.append((pending, ''.join(buf).strip()))
                pending = 'and'
                buf = []
                i += 2
                continue
            if text.startswith('||', i):
                parts.append((pending, ''.join(buf).strip()))
                pending = 'or'
                buf = []
                i += 2
                continue
            buf.append(text[i])
            i += 1
        parts.append((pending, ''.join(buf).strip()))
        return [(op, chunk) for op, chunk in parts if chunk]

    @staticmethod
    def _output_failed(result):
        if not result or result.get('handled') is False:
            return True
        if result.get('exit_code'):
            return True
        text = (result.get('output') or '').lower()
        return any(m in text for m in (
            'command not found', 'no such file', 'permission denied',
            'not found', 'cannot access', 'syntax error',
            "can't open", 'missing operand', 'missing file operand',
            'is not the name of a known user', 'file exists',
            'cannot create directory', 'datei oder verzeichnis',
            'keine berechtigung',
            'option requires an argument', 'ambiguous redirect',
            'invalid option', 'illegal option',
        ))

    def _bash_prefix(self, host):
        if self.hosts[host].get('os_id') == 'debian':
            hn = str(self.hosts[host].get('hostname') or host)
            if 'halle' in hn.lower() or host == 'userdb' or hn == 'userdb':
                return 'bash'
            return '-bash'
        return 'bash'

    def _enoent(self, host):
        loc = str(self.hosts[host].get('locale') or '')
        if loc.startswith('de'):
            return 'Datei oder Verzeichnis nicht gefunden'
        return 'No such file or directory'

    def _find_quote(self, host, raw):
        if self.hosts[host].get('os_id') == 'debian':
            return f'`{raw}\''
        return f"'{raw}'"

    def _od_named(self, raw: bytes) -> str:
        named = {0: 'nul', 7: 'bel', 8: 'bs', 9: 'ht', 10: 'nl', 11: 'vt',
                 12: 'ff', 13: 'cr', 32: 'sp'}
        lines = []
        for i in range(0, len(raw), 16):
            chunk = raw[i:i + 16]
            parts = []
            for b in chunk:
                if b in named:
                    parts.append(f'{named[b]:>3s}')
                elif 32 < b < 127:
                    parts.append(f'{chr(b):>3s}')
                else:
                    parts.append(f'{b:03o}')
            lines.append(f'{i:07o} ' + ' '.join(parts))
        return ('\n'.join(lines) + '\n') if lines else '\n'

    def _cut_stdin(self, tokens, current):
        text = current if current.endswith('\n') or current == '' else current + '\n'
        charset = None
        fieldset = None
        delim = '\t'
        i = 1
        while i < len(tokens):
            tok = tokens[i]
            if tok in {'-c', '-f', '-d', '-b'} and i + 1 < len(tokens):
                val = tokens[i + 1]
                if tok in {'-c', '-b'}:
                    charset = val
                elif tok == '-f':
                    fieldset = val
                else:
                    delim = val[:1] if val else '\t'
                i += 2
                continue
            if tok.startswith('-c') and len(tok) > 2:
                charset = tok[2:]
            elif tok.startswith('-b') and len(tok) > 2:
                charset = tok[2:]
            elif tok.startswith('-f') and len(tok) > 2:
                fieldset = tok[2:]
            elif tok.startswith('-d') and len(tok) > 2:
                delim = tok[2:3] or '\t'
            i += 1

        def slice_spec(spec, seq):
            out = []
            for part in str(spec).split(','):
                part = part.strip()
                if not part:
                    continue
                try:
                    if '-' in part:
                        a, b = part.split('-', 1)
                        start = int(a or '1')
                        end = int(b or str(len(seq)))
                        out.extend(seq[start - 1:end])
                    else:
                        idx = int(part) - 1
                        if 0 <= idx < len(seq):
                            out.append(seq[idx])
                except ValueError:
                    continue
            return out

        lines = []
        for line in text.splitlines(True):
            ended = line.endswith('\n')
            body = line[:-1] if ended else line
            if charset:
                chars = list(body)
                body = ''.join(slice_spec(charset, chars))
            elif fieldset:
                fields = body.split(delim)
                body = delim.join(slice_spec(fieldset, fields))
            lines.append(body + ('\n' if ended else ''))
        return ''.join(lines)

    def _tr_stdin(self, tokens, current):
        args = [t for t in tokens[1:] if t != '-s']
        squeeze = '-s' in tokens
        delete = '-d' in tokens or any(t.startswith('-d') for t in tokens[1:])

        def unescape(s):
            return (s or '').replace(r'\n', '\n').replace(r'\t', '\t').replace(r'\r', '\r')

        if delete:
            drop = unescape(args[-1] if args else '')
            drop = drop.replace('[:space:]', ' \t\n').replace('[:graph:]', '')
            table = {ch: '' for ch in drop}
            return ''.join(table.get(ch, ch) for ch in current)
        if len(args) >= 2:
            src, dst = unescape(args[-2]), unescape(args[-1])
            if src.startswith("'") or dst.startswith("'"):
                src, dst = src.strip("'"), dst.strip("'")
            trans = {}
            for i, ch in enumerate(src):
                trans[ch] = dst[i] if i < len(dst) else (dst[-1] if dst else ch)
            out = ''.join(trans.get(ch, ch) for ch in current)
            if squeeze and dst:
                keep, prev = [], object()
                for ch in out:
                    if ch == dst[0] and ch == prev:
                        continue
                    keep.append(ch)
                    prev = ch
                return ''.join(keep)
            return out
        return current

    def _filter_pipeline_stage(self, session, host, stage_cmd, stage_tokens, current):
        """Apply stdin filters. Returns (new_current, consumed)."""
        if stage_cmd == 'tac':
            lines = current.splitlines(True)
            return ''.join(reversed(lines)), True
        if stage_cmd in {'more', 'less'}:
            return current, True
        if stage_cmd == 'paste':
            delim = '\t'
            serial = any(t == '-s' or str(t).startswith('-s') for t in stage_tokens[1:])
            for tok in stage_tokens[1:]:
                if tok.startswith('-d') and len(tok) > 2:
                    delim = tok[2:] or '\t'
                elif tok == '-d':
                    idx = stage_tokens.index(tok)
                    if idx + 1 < len(stage_tokens):
                        delim = stage_tokens[idx + 1]
            lines = [ln.rstrip('\n') for ln in current.splitlines()]
            if serial:
                body = delim.join(lines)
                return (body + '\n') if body else '', True
            return current, True
        if stage_cmd == 'nl':
            out = []
            for i, line in enumerate(current.splitlines(True), 1):
                out.append(f'{i:6d}\t{line}')
            return ''.join(out) if out else current, True
        if stage_cmd == 'od':
            raw = current.encode('latin1', 'replace')
            to2 = any(t in {'-to2', '-o2'} or t.endswith('o2') for t in stage_tokens[1:])
            if to2:
                data = raw if len(raw) >= 2 else raw + b'\x00'
                val = data[0] | (data[1] << 8)
                return f'0000000 {val:06o}\n', True
            if any(t in {'-a', '-ta', '-t'} or t.startswith('-a') for t in stage_tokens[1:]):
                return self._od_named(raw[:256]), True
            hexes = ' '.join(f'{b:02x}' for b in raw[:64])
            return ' ' + hexes + '\n', True
        if stage_cmd in {'head', 'tail'}:
            byte_mode = '-c' in stage_tokens or any(t.startswith('-c') and t != '-c' for t in stage_tokens)
            try:
                n = 10
                if '-n' in stage_tokens:
                    n = int(stage_tokens[stage_tokens.index('-n') + 1])
                elif any(t.startswith('-n') and t != '-n' and t[2:].isdigit() for t in stage_tokens):
                    n = int(next(t[2:] for t in stage_tokens if t.startswith('-n') and t != '-n'))
                elif '-c' in stage_tokens:
                    n = int(stage_tokens[stage_tokens.index('-c') + 1])
                elif len(stage_tokens) >= 2 and stage_tokens[1].lstrip('-').isdigit():
                    n = int(stage_tokens[1].lstrip('-'))
            except Exception:
                n = 10
            if byte_mode:
                data = current.encode('latin1', 'replace')
                data = data[:n] if stage_cmd == 'head' else data[-n:]
                return data.decode('latin1', 'replace'), True
            lines = current.splitlines(True)
            out = ''.join(lines[:n] if stage_cmd == 'head' else lines[-n:])
            if out and not out.endswith('\n'):
                out += '\n'
            return out, True
        if stage_cmd in {'grep', 'egrep', 'fgrep'}:
            invert = any(tok in {'-v', '-vE', '-Ev', '-iv', '-vi'} or (
                tok.startswith('-') and 'v' in tok[1:] and tok.isalpha())
                for tok in stage_tokens[1:])
            ignore = any(tok in {'-i', '-iE', '-Ei', '-iv', '-vi'} or (
                tok.startswith('-') and 'i' in tok[1:] and tok.isalpha())
                for tok in stage_tokens[1:])
            pattern = next((tok for tok in stage_tokens[1:] if not tok.startswith('-')), '')
            if not pattern:
                name = stage_cmd if stage_cmd != 'egrep' else 'grep'
                return (
                    f"Usage: {name} [OPTION]... PATTERN [FILE]...\n"
                    f"Try '{name} --help' for more information.\n"
                ), True
            flags = re.I if ignore else 0
            rx = None
            if pattern:
                try:
                    rx = re.compile(pattern, flags)
                except re.error:
                    rx = None
            kept = []
            for line in current.splitlines(True):
                if rx is not None:
                    hit = bool(rx.search(line))
                else:
                    needle = pattern.lower() if ignore else pattern
                    hay = line.lower() if ignore else line
                    hit = needle in hay if pattern else False
                if invert:
                    if not hit:
                        kept.append(line)
                elif hit:
                    kept.append(line)
            return ''.join(kept), True
        if stage_cmd == 'cat':
            if any(t in {'-n', '-b'} for t in stage_tokens[1:]):
                numbered = []
                for i, line in enumerate(current.splitlines(True), 1):
                    numbered.append(f'{i}\t{line}')
                return ''.join(numbered), True
            return current, True
        if stage_cmd == 'wc':
            if '-c' in stage_tokens:
                return f'{len(current.encode())}\n', True
            if '-w' in stage_tokens:
                return f'{len(current.split())}\n', True
            nlines = len(current.splitlines()) if current else 0
            return f'{nlines}\n', True
        if stage_cmd == 'tee':
            return current, True
        if stage_cmd == 'tr':
            return self._tr_stdin(stage_tokens, current), True
        if stage_cmd == 'cut':
            return self._cut_stdin(stage_tokens, current), True
        if stage_cmd in {'awk', 'sed', 'column', 'rev'}:
            if stage_cmd == 'rev':
                lines = [line.rstrip('\n')[::-1] + ('\n' if line.endswith('\n') else '')
                         for line in current.splitlines(True)]
                return ''.join(lines), True
            if stage_cmd == 'sed':
                prog = ' '.join(t for t in stage_tokens[1:] if not str(t).startswith('-'))
                stripped_prog = prog.strip().strip("'\"")
                m = re.match(r"s/([^/]*)/([^/]*)/[gi]*", stripped_prog)
                if m:
                    return current.replace(m.group(1), m.group(2)), True
                qm = re.match(r'^(\d+)q$', stripped_prog)
                if qm:
                    n = int(qm.group(1))
                    return ''.join(current.splitlines(True)[:n]), True
                return current, True
            if stage_cmd == 'awk':
                prog = ' '.join(t for t in stage_tokens[1:] if not str(t).startswith('-F'))
                fields = [int(x) for x in re.findall(r'\$(\d+)', prog)]
                if 'print' in prog and fields:
                    out_lines = []
                    for line in current.splitlines():
                        cols = line.split()
                        vals = [cols[i - 1] if 0 < i <= len(cols) else '' for i in fields]
                        out_lines.append(' '.join(vals))
                    body = '\n'.join(out_lines)
                    if body:
                        body += '\n'
                    return body, True
            return current, True
        if stage_cmd == 'sort':
            lines = current.splitlines(True)
            return ''.join(sorted(lines)), True
        if stage_cmd == 'uniq':
            out, prev = [], object()
            for line in current.splitlines(True):
                if line != prev:
                    out.append(line)
                prev = line
            return ''.join(out), True
        if stage_cmd == 'bc':
            expr = current.strip().replace(' ', '')
            if re.fullmatch(r'[0-9+\-*/().]+', expr):
                try:
                    return str(int(eval(expr, {'__builtins__': {}}, {}))) + '\n', True
                except Exception:
                    return current, True
            return current, True
        if stage_cmd == 'xargs':
            rest = []
            skip_next = False
            for tok in stage_tokens[1:]:
                if skip_next:
                    skip_next = False
                    continue
                if tok in {'-0', '-r', '-t'}:
                    continue
                if tok in {'-I', '-i', '-n', '-L', '-P'}:
                    skip_next = True
                    continue
                rest.append(tok)
            lines = [ln for ln in (current or '').replace('\0', '\n').splitlines() if ln]
            if not lines:
                inner = ' '.join(rest)
                if not inner:
                    return '', True
                result = self.execute_command(session, host, inner)
                if not result.get('handled'):
                    prefix = self._bash_prefix(host)
                    return f'{prefix}: {rest[0]}: command not found\n', True
                return result.get('output') or '', True
            inner = ' '.join(rest + lines[:40])
            result = self.execute_command(session, host, inner)
            if not result.get('handled'):
                prefix = self._bash_prefix(host)
                token = rest[0] if rest else 'xargs'
                return f'{prefix}: {token}: command not found\n', True
            return result.get('output') or '', True
        return current, False

    def _run_assignment(self, session, host, text):
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)=(.*)$', text, re.S)
        if not m:
            return None
        name, val = m.group(1), m.group(2).strip()
        if val.startswith('"') and val.endswith('"') and len(val) >= 2:
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'") and len(val) >= 2:
            val = val[1:-1]
        inner = None
        if val.startswith('$(') and val.endswith(')'):
            inner = val[2:-1]
        elif val.startswith('`') and val.endswith('`'):
            inner = val[1:-1]
        state = self._session_state(session, host)
        if inner:
            result = self.execute_command(session, host, inner)
            out = result.get('output') or ''
            failed = self._output_failed(result) or not result.get('handled')
            state['env'][name] = '' if failed else out.rstrip('\n')
            if failed:
                if not result.get('handled'):
                    prefix = self._bash_prefix(host)
                    token = inner.strip().split(maxsplit=1)[0] if inner.strip() else name
                    return {'handled': True, 'output': f'{prefix}: {token}: command not found\n',
                            'trap_trigger': False}
                return result
            if out.strip() and any(s in out.lower() for s in (
                    'option requires an argument', 'try \'', 'invalid option',
                    'illegal option', 'no such file')):
                return result
            return {'handled': True, 'output': '', 'trap_trigger': result.get('trap_trigger', False)}
        state['env'][name] = val
        return {'handled': True, 'output': '', 'trap_trigger': False}

    def execute_command(self, session, host, command):
        """Execute one shell atom. handled=False means caller may LLM-fallback."""
        text = command.strip()
        if not text:
            return {'handled': True, 'output': '', 'trap_trigger': False}
        background = False
        if text.endswith('&'):
            background = True
            text = text[:-1].strip()
        # Strip wrapping subshell `( cmd )` even when inner contains $().
        stripped = text.strip()
        if stripped.startswith('(') and stripped.endswith(')') and len(stripped) > 2:
            text = stripped[1:-1].strip()
        # Rewrite `for ...; do ...; done` blocks in mixed compounds, then split.
        text = self._rewrite_for_loops(session, host, text)
        state0 = self._session_state(session, host)
        unset_redir = self._unset_redirect_var(text, state0.get('env'))
        if unset_redir:
            return {'handled': True, 'output': (
                f'{self._bash_prefix(host)}: {unset_redir}: ambiguous redirect\n'
            ), 'trap_trigger': False}
        if '<(' in text:
            collected = []
            for inner in self._proc_subst_inners(text):
                if not inner:
                    continue
                result = self.execute_command(session, host, inner)
                if not result.get('handled'):
                    tok = inner.strip().split()[0] if inner.strip() else 'command'
                    collected.append(f'{self._bash_prefix(host)}: {tok}: command not found\n')
                elif self._output_failed(result):
                    collected.append(result.get('output') or '')
            if collected:
                return {'handled': True, 'output': ''.join(collected), 'trap_trigger': False}
        in_file = self._input_redirect_file(text)
        if in_file and not self._split_pipeline(text)[1:]:
            path = self._resolve_path(state0.get('cwd') or '/', in_file)
            vfs = self.vfs.get(host)
            if vfs is None or vfs.get(path) is None:
                return {'handled': True, 'output': (
                    f'{self._bash_prefix(host)}: {in_file}: {self._enoent(host)}\n'
                ), 'trap_trigger': False}
        expanded = self._expand_simple_for_loop(text, session=session, host=host)
        if expanded is not None:
            pieces, trap = [], False
            for piece_cmd in expanded:
                result = self.execute_command(session, host, piece_cmd)
                if not result['handled']:
                    return {'handled': False, 'output': ''.join(pieces),
                            'trap_trigger': trap, 'unhandled_command': piece_cmd}
                pieces.append(result['output'])
                trap = trap or result.get('trap_trigger', False)
            return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': trap}
        # Strip simple redirections / noise for routing; keep original for echo.
        chunks = [part.strip() for part in self._split_semicolons(text) if part.strip()]
        if len(chunks) > 1:
            pieces, trap = [], False
            for chunk in chunks:
                result = self.execute_command(session, host, chunk)
                if not result['handled']:
                    tok = chunk.strip().split()[0] if chunk.strip() else 'command'
                    if '/' in tok:
                        tok = PurePosixPath(tok).name
                    pieces.append(f'{self._bash_prefix(host)}: {tok}: command not found\n')
                    continue
                pieces.append(result.get('output') or '')
                trap = trap or result.get('trap_trigger', False)
            return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': trap}
        bool_parts = self._split_bool_ops(text)
        if len(bool_parts) > 1:
            pieces, trap = [], False
            prev_failed = False
            last_unhandled = None
            for index, (op, chunk) in enumerate(bool_parts):
                if index > 0:
                    if op == 'and' and prev_failed:
                        continue
                    if op == 'or' and not prev_failed:
                        continue
                result = self.execute_command(session, host, chunk)
                if not result['handled']:
                    prev_failed = True
                    last_unhandled = result
                    continue
                pieces.append(result['output'])
                trap = trap or result.get('trap_trigger', False)
                prev_failed = self._output_failed(result)
                last_unhandled = None
            if not pieces and last_unhandled is not None:
                return last_unhandled
            return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': trap}
        assigned = self._run_assignment(session, host, text)
        if assigned is not None:
            return assigned
        # For fingerprinting pipes, execute stages left-to-right with limited builtins.
        # Only treat as a pipeline when | appears outside quotes; otherwise
        # grep -E 'a|b' would recurse forever on the same atom.
        if '|' in text:
            stages = [self._strip_redirections(part) for part in self._split_pipeline(text) if part.strip()]
            if len(stages) <= 1:
                text = stages[0] if stages else text
            else:
                current = ''
                stderr = []
                trap = False
                stdin_filters = {
                    'od', 'head', 'tail', 'grep', 'egrep', 'fgrep', 'wc', 'tee',
                    'tr', 'cut', 'awk', 'sed', 'column', 'rev', 'sort', 'uniq',
                    'bc', 'xargs', 'cat', 'tac', 'nl', 'more', 'less', 'paste',
                }
                env_state = self._session_state(session, host)
                for index, stage in enumerate(stages):
                    fname = self._input_redirect_file(stage)
                    if fname:
                        path = self._resolve_path(env_state.get('cwd') or '/', fname)
                        vfs = self.vfs.get(host)
                        if vfs is None or vfs.get(path) is None:
                            stderr.append(
                                f'{self._bash_prefix(host)}: {fname}: {self._enoent(host)}\n')
                            current = ''
                            continue
                    if '$(' in stage or '`' in stage:
                        stage = self._expand_shell_vars(
                            stage, env_state['env'], session=session, host=host)
                    stage_tokens = self._tokenize(stage)
                    stage_cmd = stage_tokens[0] if stage_tokens else ''
                    if index > 0 and stage_cmd in stdin_filters:
                        current, _consumed = self._filter_pipeline_stage(
                            session, host, stage_cmd, stage_tokens, current)
                        continue
                    if stage_cmd in {'sh', 'bash'} and index > 0:
                        continue
                    result = self.execute_command(session, host, stage)
                    prefix = self._bash_prefix(host)
                    if not result['handled']:
                        stderr.append(f'{prefix}: {stage_cmd}: command not found\n')
                        current = ''
                        continue
                    if self._output_failed(result):
                        stderr.append(result.get('output') or '')
                        current = ''
                        trap = trap or result.get('trap_trigger', False)
                        continue
                    current = result['output']
                    trap = trap or result.get('trap_trigger', False)
                out = ''.join(stderr) + current
                if background and text.lstrip().startswith('sleep'):
                    pid = int(self._session_state(session, host)['env'].get('$') or 2145) + 20
                    out = f'[1] {pid}\n' + out
                return {'handled': True, 'output': out, 'trap_trigger': trap}
        text = self._strip_redirections(text)

        state = self._session_state(session, host)
        cwd = state['cwd']
        user = self.hosts[host]['credential']['username']
        self._tilde_home = '/root' if user == 'root' else f'/home/{user}'
        # Expand substitutions before tokenization so `echo $(id -un)` works.
        if ('$(' in text or '$?' in text or '$RANDOM' in text or '${' in text or '$' in text
                or '`' in text):
            text = self._expand_shell_vars(text, state['env'], session=session, host=host)
        tokens = self._tokenize(text)
        if not tokens:
            return {'handled': True, 'output': '', 'trap_trigger': False}
        cmd = tokens[0]
        # Allow absolute coreutils paths: /usr/bin/head -> head
        if '/' in cmd:
            base = PurePosixPath(cmd).name
            if base:
                cmd = base
        # Bash keywords must not look like missing external commands.
        if cmd in {'for', 'while', 'if', 'then', 'else', 'elif', 'fi', 'do', 'done', 'case', 'esac', 'function'}:
            return {'handled': True,
                    'output': f'bash: -c: line 1: syntax error near unexpected token `{cmd}\'\n',
                    'trap_trigger': False}
        args = tokens[1:]
        if cmd == 'ls' and any('(' in a or ')' in a for a in tokens):
            shown = next((a for a in tokens if '(' in a), '(')
            return {'handled': True,
                    'output': f'{self._bash_prefix(host)}: syntax error near unexpected token `{shown}\'\n',
                    'trap_trigger': False}
        # `time CMD` is a shell keyword wrapper used in fingerprint latency probes.
        if cmd == 'time' and args:
            return self.execute_command(session, host, ' '.join(args))
        if cmd == 'command':
            # Builtin: `command -v NAME` / `command -V NAME`.
            names = [a for a in args if not a.startswith('-')]
            if not names:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            return self.execute_command(
                session, host, ('type -a ' if '-V' in args or '-v' in args else 'which ') + names[0])
        if cmd == 'yes':
            token = next((a for a in args if not str(a).startswith('-')), 'y')
            return {'handled': True, 'output': (token + '\n') * 120, 'trap_trigger': False}
        if cmd == 'set':
            valid = set('abefhkmnptuvxBCHP')
            for flag in args:
                if not str(flag).startswith('-') or flag in {'--', '-'}:
                    continue
                for ch in str(flag)[1:]:
                    if ch not in valid:
                        return {'handled': True, 'output': (
                            f'{self._bash_prefix(host)}: set: -{ch}: invalid option\n'
                            'set: usage: set [-abefhkmnptuvxBCHP] [-o option-name] [--] [arg ...]\n'
                        ), 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'read':
            prompt = ''
            if '-p' in args:
                try:
                    prompt = args[args.index('-p') + 1]
                except Exception:
                    prompt = ''
            if prompt:
                if not str(prompt).endswith('\n'):
                    prompt = str(prompt) + '\n'
                return {'handled': True, 'output': prompt, 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'tac':
            files = [a for a in args if not str(a).startswith('-')]
            if files:
                raw = files[-1]
                path = self._resolve_path(cwd, raw)
                vfs = self.vfs.get(host)
                node = vfs.get(path) if vfs is not None else None
                if node is None:
                    return {'handled': True, 'output': (
                        f"tac: failed to open ‘{raw}’ for reading: No such file or directory\n"
                    ), 'trap_trigger': False}
                content = node.content or ''
                return {'handled': True, 'output': ''.join(reversed(content.splitlines(True))),
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'nl':
            files = [a for a in args if not str(a).startswith('-')]
            if files:
                raw = files[-1]
                vfs = self.vfs.get(host)
                if vfs is None or vfs.get(self._resolve_path(cwd, raw)) is None:
                    return {'handled': True, 'output': f'nl: {raw}: No such file or directory\n',
                            'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'pushd':
            return {'handled': True, 'output': '~ ~\n', 'trap_trigger': False}
        if cmd == 'popd':
            return {'handled': True, 'output': '~\n', 'trap_trigger': False}
        if cmd == 'true':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'false':
            return {'handled': True, 'output': '', 'trap_trigger': False, 'exit_code': 1}
        if cmd == 'unset':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'sleep':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'kill':
            pids = [a for a in args if not str(a).startswith('-')]
            if not pids:
                return {'handled': True, 'output': (
                    'kill: usage: kill [-s sigspec | -n signum | -sigspec] '
                    'pid | jobspec ... or kill -l [sigspec]\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'chpasswd':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'useradd', 'userdel', 'usermod', 'groupadd', 'groupdel',
                   'adduser', 'deluser'}:
            name = next((a for a in args if not str(a).startswith('-')), '')
            if cmd == 'useradd' and name in {'butter', 'test', 'admin', 'ubuntu', 'guest'}:
                return {'handled': True,
                        'output': f"useradd: user '{name}' already exists\n",
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'passwd':
            if any(a in {'--stdin', '-stdin'} or str(a).startswith('--stdin') for a in args):
                return {'handled': True, 'output': (
                    "passwd: unrecognized option '--stdin'\n"
                    "Usage: passwd [options] [LOGIN]\n"
                    "\n"
                    "Options:\n"
                    "  -a, --all                     report password status on all accounts\n"
                    "  -d, --delete                  delete the password for the named account\n"
                    "  -h, --help                    display this help message and exit\n"
                    "  -k, --keep-tokens             change password only if expired\n"
                    "  -i, --inactive INACTIVE       set password inactive after expiration\n"
                    "  -l, --lock                    lock the password of the named account\n"
                    "  -n, --mindays MIN_DAYS        set minimum number of days before password change\n"
                    "  -q, --quiet                   quiet mode\n"
                    "  -r, --repository REPOSITORY   change password in REPOSITORY repository\n"
                    "  -S, --status                  report password status on the named account\n"
                    "  -u, --unlock                  unlock the password of the named account\n"
                    "  -w, --warndays WARN_DAYS      set expiration warning days\n"
                    "  -x, --maxdays MAX_DAYS        set maximum number of days before password change\n"
                ), 'trap_trigger': False}
            loc = str(self.hosts[host].get('locale') or '')
            if loc.startswith('de'):
                return {'handled': True, 'output': '(aktuelles) UNIX-Passwort:\n',
                        'trap_trigger': False}
            return {'handled': True, 'output': (
                '(current) UNIX password: \n'
                'Enter new UNIX password: Retype new UNIX password: \n'
                'passwd: password updated successfully\n'
            ), 'trap_trigger': False}
        if cmd == 'base64':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'python3':
            if self.hosts[host].get('os_id') == 'debian':
                return {'handled': True,
                        'output': f'{self._bash_prefix(host)}: python3: command not found\n',
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'python':
            if any(a == '-c' or str(a).startswith('-c') for a in args):
                return {'handled': True, 'output': '', 'trap_trigger': False}
            if any(a in {'-V', '--version'} or str(a).startswith('-V') for a in args):
                return {'handled': True, 'output': 'Python 2.7.9\n', 'trap_trigger': False}
            script = next((a for a in args if not str(a).startswith('-')), '')
            if script:
                return {'handled': True, 'output': (
                    f"python: can't open file '{script}': [Errno 2] No such file or directory\n"
                ), 'trap_trigger': False}
            if self.hosts[host].get('os_id') == 'debian':
                return {'handled': True, 'output': (
                    'Python 2.7.9 (default, Sep 25 2018, 20:42:16) \n'
                    '[GCC 4.9.2] on linux2\n'
                    'Type "help", "copyright", "credits" or "license" for more information.\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'tftp':
            return {'handled': True,
                    'output': f'{self._bash_prefix(host)}: tftp: command not found\n',
                    'trap_trigger': False}
        if cmd == 'dmidecode':
            return {'handled': True, 'output': (
                '# dmidecode 2.12\n'
                'SMBIOS 2.8 present.\n'
                '\n'
                'Handle 0x0000, DMI type 0, 24 bytes\n'
                'BIOS Information\n'
                '\tVendor: SeaBIOS\n'
                '\tVersion: 1.7.5-20140709_153310-el6\n'
                '\tRelease Date: 04/01/2014\n'
            ), 'trap_trigger': False}
        if cmd == 'lspci':
            return {'handled': True, 'output': (
                '00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)\n'
                '00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]\n'
                '00:01.1 IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]\n'
                '00:01.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 03)\n'
                '00:02.0 VGA compatible controller: Device 1234:1111 (rev 02)\n'
                '00:03.0 Ethernet controller: Intel Corporation 82540EM Gigabit Ethernet Controller (rev 03)\n'
            ), 'trap_trigger': False}
        if cmd == 'apt':
            return {'handled': True, 'output': (
                'apt 1.0.9.8.4 for amd64 compiled on Dec 16 2016 21:42:33\n'
                'Usage: apt [options] command\n'
                '\n'
                'CLI for apt.\n'
                'Basic commands: \n'
                ' list - list packages based on package names\n'
                ' search - search in package descriptions\n'
                ' show - show package details\n'
                '\n'
                ' update - retrieve new lists of packages\n'
                ' install - install new packages\n'
                ' remove - remove packages\n'
                '\n'
                ' upgrade - perform an upgrade\n'
                ' full-upgrade - perform an upgrade, possibly installing and removing packages\n'
            ), 'trap_trigger': False}
        if cmd in {'apt-get', 'apt-cache'}:
            if user == 'vagrant':
                return {'handled': True, 'output': (
                    'E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)\n'
                    'E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': (
                'Reading package lists...\n'
                'Building dependency tree...\n'
                'Reading state information...\n'
            ), 'trap_trigger': False}
        if cmd == 'whois':
            whois_args = [a for a in args if not str(a).startswith('-')]
            if not whois_args:
                return {'handled': True, 'output': (
                    '.ripe.net and some RIPE-like servers:\n'
                    '-l                     find the one level less specific match\n'
                    '-L                     find all One level less specific matches\n'
                    '-m                     find all One level more specific matches\n'
                    '-M                     find all More specific matches\n'
                ), 'trap_trigger': False}
            query = whois_args[0]
            if re.match(r'^\d+(?:\.\d+){3}$', query):
                return {'handled': True,
                        'output': 'No whois server is known for this kind of object.\n',
                        'trap_trigger': False}
            tld = query.rsplit('.', 1)[-1].lower() if '.' in query else ''
            if tld and tld not in {'com', 'net', 'org', 'info', 'io', 'edu'}:
                return {'handled': True, 'output': (
                    'This TLD has no whois server, but you can access the whois database at\n'
                    f'http://www.nic.{tld}/\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': (
                f'   Domain Name: {query.upper()}\n'
                '   Registry Domain ID: 1923710_DOMAIN_COM-VRSN\n'
                '   Registrar WHOIS Server: whois.godaddy.com\n'
            ), 'trap_trigger': False}
        if cmd == 'nohup':
            rest = [a for a in args if a not in {'&'}]
            if rest:
                return self.execute_command(session, host, self._shell_join(rest))
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'busybox':
            if not args:
                return {'handled': True, 'output': (
                    'BusyBox v1.22.1 (Debian 1:1.22.0-9+deb8u1) multi-call binary.\n'
                ), 'trap_trigger': False}
            applet = args[0]
            rest = args[1:]
            if applet == 'cp' and not rest:
                return {'handled': True, 'output': (
                    '\nBusyBox v1.22.1 (Debian 1:1.22.0-9+deb8u1) multi-call binary.\n'
                    '\nUsage: cp [OPTIONS] SOURCE DEST\n'
                ), 'trap_trigger': False}
            return self.execute_command(session, host, ' '.join(args))
        if cmd == 'lscpu':
            return {'handled': True, 'output': (
                'Architecture:          x86_64\n'
                'CPU op-mode(s):        32-bit, 64-bit\n'
                'Byte Order:            Little Endian\n'
                'CPU(s):                2\n'
                'On-line CPU(s) list:   0,1\n'
                'Thread(s) per core:    1\n'
                'Core(s) per socket:    1\n'
                'Socket(s):             2\n'
                'Vendor ID:             GenuineIntel\n'
                'CPU family:            6\n'
                'Model:                 6\n'
                'Model name:            Common KVM processor\n'
                'Stepping:              3\n'
                'CPU MHz:               2194.918\n'
                'BogoMIPS:              4389.83\n'
                'Hypervisor vendor:     KVM\n'
                'Virtualization type:   full\n'
            ), 'trap_trigger': False}
        # Drop common flags for routing decisions.
        bare_args = [a for a in args if not a.startswith('-')]

        if cmd == 'cd':
            raw = bare_args[0] if bare_args else (state['env'].get('HOME') or self._tilde_home)
            target = self._resolve_path(cwd, raw)
            vfs = self.vfs.get(host)
            node = vfs.get(target) if vfs is not None else None
            known = {
                '/', '/home', '/home/' + user, '/root', '/etc', '/var', '/opt', '/tmp',
                '/var/tmp', '/var/run', '/dev', '/dev/shm', '/dev/pts', '/run', '/proc', '/sys',
            }
            if node is not None and node.is_dir:
                state['cwd'] = target
                state['env']['PWD'] = target
                return {'handled': True, 'output': '', 'trap_trigger': False}
            if target in known or (vfs is not None and vfs.is_dir(target)):
                if vfs is not None:
                    vfs.ensure_dir(target, owner='root' if not target.startswith('/home/') else user,
                                   mode='0755')
                state['cwd'] = target
                state['env']['PWD'] = target
                return {'handled': True, 'output': '', 'trap_trigger': False}
            files = self._host_files(host)
            if target in files or any(path.startswith(target.rstrip('/') + '/') for path in files):
                state['cwd'] = target
                state['env']['PWD'] = target
                return {'handled': True, 'output': '', 'trap_trigger': False}
            shown = raw if raw else target
            return {'handled': True,
                    'output': f'{self._bash_prefix(host)}: cd: {shown}: {self._enoent(host)}\n',
                    'trap_trigger': False}

        if cmd == 'pwd':
            return {'handled': True, 'output': state['cwd'] + '\n', 'trap_trigger': False}
        if cmd == 'basename':
            if not bare_args:
                return {'handled': True, 'output': 'basename: missing operand\n', 'trap_trigger': False}
            raw = bare_args[0].strip().strip('"').strip("'").strip('`')
            if raw in {'', 'pwd', '$(pwd)'} or raw in {
                    state.get('cwd'), state.get('env', {}).get('PWD'), state.get('env', {}).get('HOME')}:
                return {'handled': True, 'output': user + '\n', 'trap_trigger': False}
            name = PurePosixPath(raw.rstrip('/') or raw).name
            return {'handled': True, 'output': (name or raw) + '\n', 'trap_trigger': False}
        if cmd == 'whoami':
            return {'handled': True, 'output': user + '\n', 'trap_trigger': False}
        if cmd == 'hostname':
            full = self.hosts[host].get('hostname') or host
            return {'handled': True, 'output': str(full) + '\n', 'trap_trigger': False}
        if cmd == 'id':
            uid = int(self.hosts[host]['credential'].get('uid', 1000))
            loc = str(self.hosts[host].get('locale') or '')
            flag = ''.join(a[1:] for a in args if str(a).startswith('-') and a != '--')
            if 'u' in flag and 'n' in flag:
                return {'handled': True, 'output': user + '\n', 'trap_trigger': False}
            if 'g' in flag and 'n' in flag:
                return {'handled': True, 'output': user + '\n', 'trap_trigger': False}
            if 'u' in flag:
                return {'handled': True, 'output': f'{uid}\n', 'trap_trigger': False}
            if 'g' in flag:
                return {'handled': True, 'output': f'{uid}\n', 'trap_trigger': False}
            if loc.startswith('de'):
                out = f'u={uid}({user}) g={uid}({user}) Gruppen={uid}({user})\n'
            else:
                out = f'uid={uid}({user}) gid={uid}({user}) groups={uid}({user})\n'
            return {'handled': True, 'output': out, 'trap_trigger': False}
        if cmd == 'groups':
            name = next((a for a in args if not str(a).startswith('-')), user)
            if self.hosts[host].get('os_id') == 'debian':
                return {'handled': True, 'output': (
                    f'{name} : {name} cdrom floppy sudo audio dip video plugdev netdev\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': f'{name}\n', 'trap_trigger': False}
        if cmd == 'history':
            if any(str(a).startswith('-') for a in args):
                return {'handled': True, 'output': '', 'trap_trigger': False}
            return {'handled': True, 'output': (
                '    1  ls\n'
                '    2  id\n'
                '    3  cat notes.txt\n'
                '    4  systemctl status monit\n'
                '    5  journalctl -u ssh -n 20\n'
                '    6  cat /etc/ops/maintenance.conf\n'
                '    7  cat /home/admin/.ssh/ticket-CHG2916.txt\n'
            ), 'trap_trigger': False}
        if cmd == 'which':
            if not bare_args:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            name = bare_args[0]
            builtins = {'echo', 'printf', 'pwd', 'cd', 'test', '[', 'type', 'command', 'true',
                        'false', 'history', 'groups'}
            if name in builtins:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            path = f'/usr/bin/{name}' if name not in {'bash', 'sh', 'dash'} else f'/bin/{name}'
            known = {
                'ls', 'cat', 'id', 'uname', 'groups', 'head', 'stat', 'sudo', 'find',
                'sed', 'awk', 'grep', 'ps', 'ss', 'ip', 'systemctl', 'monit', 'getent',
                'which', 'file', 'stat', 'tail', 'wc', 'cut', 'tr', 'sort', 'uniq',
                'dash', 'bash', 'sh', 'netstat', 'journalctl', 'free', 'df', 'last',
                'ssh', 'scp', 'sftp', 'nc', 'rename',
            }
            if name in known:
                return {'handled': True, 'output': path + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'file':
            targets = bare_args or []
            if not targets:
                return {'handled': True, 'output': 'file: expected an argument\n', 'trap_trigger': False}
            vfs = self.vfs.get(host)
            lines = []
            for raw in targets:
                path = self._resolve_path(cwd, raw)
                node = vfs.get(path) if vfs is not None else None
                if node is None:
                    if (path.startswith('/usr/bin/') or path.startswith('/bin/')
                            or path.startswith('/usr/sbin/')):
                        shown = raw if raw.startswith('/') else path
                        if shown.endswith('rename') or raw.endswith('rename'):
                            lines.append(f'{shown}: C source, ASCII text')
                        else:
                            lines.append(f'{shown}: ELF 64-bit LSB executable, x86-64')
                    else:
                        lines.append(f'{path}: cannot open `{path}\' (No such file or directory)')
                elif node.is_dir:
                    lines.append(f'{path}: directory')
                elif node.target:
                    lines.append(f'{path}: symbolic link to {node.target}')
                elif 'BEGIN OPENSSH' in (node.content or ''):
                    lines.append(f'{path}: OpenSSH private key')
                elif (node.content or '').startswith('\x7fELF') or (node.size_override or 0) > 1000:
                    lines.append(f'{path}: ELF 64-bit LSB executable, x86-64')
                else:
                    lines.append(f'{path}: ASCII text')
            return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
        if cmd == 'sed':
            # Enough of GNU sed for `sed -n '1,80p' FILE`.
            path = bare_args[-1] if bare_args else None
            if not path:
                return {'handled': True, 'output': 'sed: no input files\n', 'trap_trigger': False}
            if len(bare_args) == 1 and (
                    path.startswith('s') or path[:1].isdigit() or '/' in path[:4]):
                return {'handled': True,
                        'output': "sed: can't read : No such file or directory\n",
                        'trap_trigger': False}
            read = self._read_file(session, host, self._resolve_path(cwd, path))
            if not read['handled']:
                return read
            body = read['output']
            if body.startswith('cat:') or 'No such file' in body or 'Permission denied' in body or 'Is a directory' in body:
                return {'handled': True, 'output': body.replace('cat:', 'sed:'), 'trap_trigger': False}
            start, end = 1, 10 ** 9
            for tok in args:
                m = re.match(r"^['\"]?(\d+),(\d+)p['\"]?$", tok)
                if m:
                    start, end = int(m.group(1)), int(m.group(2))
            lines = body.splitlines(True)
            sliced = ''.join(lines[start - 1:end])
            return {'handled': True, 'output': sliced, 'trap_trigger': False}
        if cmd == 'curl':
            if user == 'vagrant':
                prefix = self._bash_prefix(host)
                if not args:
                    return {'handled': True, 'output': ': command not found\n',
                            'trap_trigger': False}
                return {'handled': True,
                        'output': f'{prefix}: curl: command not found\n',
                        'trap_trigger': False}
            return {'handled': True, 'output': (
                '  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n'
                '                                 Dload  Upload   Total   Spent    Left  Speed\n'
            ), 'trap_trigger': False}
        if cmd == 'uname':
            hn = str(self.hosts[host].get('hostname') or host)
            kernel = self.hosts[host].get('kernel') or '5.15.0-97-generic'
            uname_a = self.hosts[host].get('uname_a') or (
                f'Linux {hn} {kernel} #1 SMP x86_64 GNU/Linux')
            flags = ''.join(a[1:] for a in args if str(a).startswith('-') and a != '--')
            if not flags:
                flags = 's'
            if 'a' in flags:
                out = uname_a if str(uname_a).endswith('\n') else str(uname_a) + '\n'
                return {'handled': True, 'output': out, 'trap_trigger': False}
            mapping = {
                's': 'Linux',
                'n': hn.split('.')[0] if self.hosts[host].get('os_id') == 'debian' else hn,
                'r': kernel,
                'v': '#1 SMP Debian 3.16.39-1 (2016-12-30)' if self.hosts[host].get('os_id') == 'debian'
                     else '#107-Ubuntu SMP',
                'm': 'x86_64',
                'p': 'unknown',
                'i': 'unknown',
                'o': 'GNU/Linux',
            }
            parts = [mapping[ch] for ch in flags if ch in mapping]
            return {'handled': True, 'output': (' '.join(parts) if parts else 'Linux') + '\n',
                    'trap_trigger': False}
        if cmd == 'sudo':
            list_ok = (not args or args[0] == '-l' or args[:2] == ['-n', '-l']
                       or (args and args[0] == '-n' and len(args) > 1 and args[1] == '-l'))
            u_flag = any(a in {'-u', '-su', '-us'} or (a.startswith('-') and 'u' in a[1:] and 'l' not in a[1:])
                         for a in args)
            u_has_value = False
            if '-u' in args:
                i = args.index('-u')
                u_has_value = i + 1 < len(args) and not str(args[i + 1]).startswith('-')
            if u_flag and not u_has_value:
                return {'handled': True, 'output': (
                    "sudo: option requires an argument -- 'u'\n"
                    "usage: sudo -h | -K | -k | -V\n"
                    "usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]\n"
                    "usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]\n"
                    "usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] [VAR=value] [-i|-s] [<command>]\n"
                    "usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] file ...\n"
                ), 'trap_trigger': False}
            if self.hosts[host].get('os_id') == 'debian':
                rest = [a for a in args if a not in {'-n', '-E', '-S'}]
                if rest and rest[0] == '-u':
                    rest = rest[2:]
                if rest and rest[0] not in {'-l', '-k', '-K', '-V', '-h'}:
                    return self.execute_command(session, host, ' '.join(rest))
            return {'handled': True,
                    'output': f'Sorry, user {user} may not run sudo on {host}.\n',
                    'trap_trigger': False}
        if cmd == 'ping':
            target = bare_args[-1] if bare_args else ''
            if not target or target.startswith('-'):
                return {'handled': True, 'output': 'Usage: ping [-c count] destination\n',
                        'trap_trigger': False}
            debian = self.hosts[host].get('os_id') == 'debian'
            # Cowrie/Halle unprivileged users; Jessie vagrant has CAP_NET_RAW.
            if debian and user not in {'root', 'vagrant'}:
                return {'handled': True,
                        'output': 'ping: icmp open socket: Operation not permitted\n',
                        'trap_trigger': False, 'exit_code': 2}
            is_ip = all(ch.isdigit() or ch == '.' for ch in target) and target.count('.') >= 1
            if not is_ip and '.' not in target and target not in {'localhost'}:
                return {'handled': True, 'output': f'ping: unknown host {target}\n',
                        'trap_trigger': False}
            dest_ip = target if is_ip else target
            out = f'PING {target} ({dest_ip}) 56(84) bytes of data.\n'
            if target == '8.8.8.8':
                out += f'64 bytes from {target}: icmp_seq=1 ttl=63 time=14.3 ms\n'
            elif target.endswith('.1') and is_ip:
                out += f'64 bytes from {target}: icmp_seq=1 ttl=63 time=3.44 ms\n'
            return {'handled': True, 'output': out, 'trap_trigger': False}
        if cmd == 'ssh':
            dest = None
            i = 0
            while i < len(args):
                a = args[i]
                if a in {'-l', '-p', '-o', '-i', '-F', '-w', '-b', '-c', '-D', '-e', '-L', '-R'}:
                    i += 2
                    continue
                if str(a).startswith('-'):
                    i += 1
                    continue
                dest = a
                break
            dest = dest or 'localhost'
            if dest not in {'localhost', '127.0.0.1', '::1'} and '.' not in dest and not dest[0].isdigit():
                return {'handled': True, 'output': (
                    f'ssh: Could not resolve hostname {dest}: '
                    f'No address associated with hostname\n'
                ), 'trap_trigger': False, 'exit_code': 255}
            return {'handled': True, 'output': (
                f"The authenticity of host '{dest} (::1)' can't be established.\n"
                "ECDSA key fingerprint is 63:e1:14:55:c9:2d:8a:7b:01:9f:44:22:11:08:3c:7a.\n"
                "Are you sure you want to continue connecting (yes/no)? "
            ), 'trap_trigger': False}
        if cmd == 'wget':
            quiet = any(
                a in {'-q', '--quiet'} or (str(a).startswith('-') and not str(a).startswith('--') and 'q' in a[1:])
                for a in args)
            url = next((a for a in args if not str(a).startswith('-')), '')
            if not url:
                return {'handled': True, 'output': '' if quiet else 'wget: missing URL\n',
                        'trap_trigger': False}
            if quiet:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            display = url if url.startswith(('http://', 'https://', 'ftp://')) else 'http://' + url
            rest = display.split('://', 1)[-1]
            hostpart = rest.split('/')[0]
            scheme = 'https' if display.startswith('https') else 'http'
            port = 443 if scheme == 'https' else 80
            hostonly = hostpart
            if hostpart.count(':') == 1:
                maybe_host, maybe_port = hostpart.rsplit(':', 1)
                if maybe_port.isdigit():
                    hostonly, port = maybe_host, int(maybe_port)
            shown = display if '/' in rest else display + '/'
            now = datetime.datetime(2024, 2, 21, 16, 41, 32)
            stamp = now.strftime('%Y-%m-%d %H:%M:%S')
            is_ip = all(ch.isdigit() or ch == '.' for ch in hostonly) and hostonly.count('.') >= 1
            if is_ip:
                body = (
                    f'--{stamp}--  {shown}\n'
                    f'Connecting to {hostonly}:{port}... connected.\n'
                    f'HTTP request sent, awaiting response... '
                )
            else:
                body = (
                    f'--{stamp}--  {shown}\n'
                    f'Resolving {hostonly} ({hostonly})... 66.102.1.102, 66.102.1.139, 66.102.1.113, ...\n'
                    f'Connecting to {hostonly} ({hostonly})|66.102.1.102|:{port}... connected.\n'
                )
            return {'handled': True, 'output': body, 'trap_trigger': False}
        if cmd == 'rm':
            force = any(a in {'-f', '-rf', '-fr'} or (
                str(a).startswith('-') and 'f' in a[1:] and not str(a).startswith('--')) for a in args)
            recursive = any(a in {'-r', '-R', '-rf', '-fr', '--recursive'} or (
                str(a).startswith('-') and ('r' in a[1:] or 'R' in a[1:]) and not str(a).startswith('--'))
                for a in args)
            targets = [a for a in args if not str(a).startswith('-')]
            if not targets:
                if force:
                    return {'handled': True, 'output': '', 'trap_trigger': False}
                return {'handled': True, 'output': (
                    "rm: missing operand\nTry 'rm --help' for more information.\n"
                ), 'trap_trigger': False}
            vfs = self.vfs.get(host)
            lines = []
            for t in targets:
                path = self._resolve_path(cwd, t)
                node = vfs.get(path) if vfs is not None else None
                if node is None:
                    if not force:
                        lines.append(f"rm: cannot remove ‘{t}’: {self._enoent(host)}")
                    continue
                if node.is_dir and not recursive:
                    if not force:
                        lines.append(f"rm: cannot remove ‘{t}’: Is a directory")
                    continue
                if vfs is not None:
                    vfs.remove(path, recursive=recursive)
            if lines:
                return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'tar':
            creating = any(
                (str(a).startswith('-') and 'c' in str(a)[1:] and not str(a).startswith('--'))
                or a in {'-c', '--create'}
                for a in args
            )
            saw_f = any(
                (str(a).startswith('-') and 'f' in str(a)[1:] and not str(a).startswith('--'))
                or a in {'-f', '--file'}
                for a in args
            )
            files = []
            pending_archive = saw_f
            skip_next = False
            for a in args:
                if skip_next:
                    skip_next = False
                    continue
                if a in {'-f', '--file'}:
                    skip_next = True
                    continue
                if str(a).startswith('-'):
                    continue
                if pending_archive:
                    pending_archive = False
                    continue
                files.append(a)
            if creating and not files:
                return {'handled': True, 'output': (
                    "tar: Cowardly refusing to create an empty archive\n"
                    "Try 'tar --help' or 'tar --usage' for more information.\n"
                ), 'trap_trigger': False}
            vfs = self.vfs.get(host)
            miss = []
            for f in files:
                if vfs is None or vfs.get(self._resolve_path(cwd, f)) is None:
                    miss.append(f'tar: {f}: Cannot stat: No such file or directory')
            if miss:
                miss.append('tar: Exiting with failure status due to previous errors')
                return {'handled': True, 'output': '\n'.join(miss) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'chmod':
            if len(bare_args) < 2:
                after = bare_args[0] if bare_args else ''
                return {'handled': True, 'output': (
                    f"chmod: missing operand after ‘{after}’\n"
                    "Try 'chmod --help' for more information.\n"
                ), 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'chown':
            if len(bare_args) < 2:
                return {'handled': True, 'output': (
                    "chown: missing operand after ‘" + (bare_args[0] if bare_args else '') + "’\n"
                    "Try 'chown --help' for more information.\n"
                ), 'trap_trigger': False}
            spec = bare_args[0]
            target = bare_args[-1]
            vfs = self.vfs.get(host)
            path = self._resolve_path(cwd, target)
            if spec in {'user:group', 'user'} or spec.endswith(':') and spec.rstrip(':') in {'', '${JBOSS_USER}'}:
                if 'root' not in spec.split(':'):
                    return {'handled': True, 'output': f"chown: invalid user: ‘{spec}’\n",
                            'trap_trigger': False}
            if vfs is None or vfs.get(path) is None:
                out = f"chown: cannot access ‘{target}’: No such file or directory\n"
                if '-v' in args:
                    out += f"failed to change ownership of ‘{target}’ to {spec}\n"
                return {'handled': True, 'output': out, 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'chgrp':
            if len(bare_args) < 2:
                return {'handled': True, 'output': (
                    "chgrp: missing operand\nTry 'chgrp --help' for more information.\n"
                ), 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'cp':
            files = [a for a in args if not str(a).startswith('-')]
            if len(files) < 2:
                return {'handled': True, 'output': (
                    "cp: missing file operand\nTry 'cp --help' for more information.\n"
                ), 'trap_trigger': False}
            missing = []
            vfs = self.vfs.get(host)
            for f in files[:-1]:
                path = self._resolve_path(cwd, f)
                if vfs is None or vfs.get(path) is None:
                    missing.append(f"cp: cannot stat ‘{f}’: No such file or directory")
            if missing:
                return {'handled': True, 'output': '\n'.join(missing) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'diff':
            if '-X' in args:
                try:
                    xfile = args[args.index('-X') + 1]
                except Exception:
                    xfile = None
                if xfile:
                    xpath = self._resolve_path(cwd, xfile)
                    xvfs = self.vfs.get(host)
                    if xvfs is None or xvfs.get(xpath) is None:
                        return {'handled': True,
                                'output': f'diff: {xfile}: No such file or directory\n',
                                'trap_trigger': False}
            files = []
            skip = False
            for a in args:
                if skip:
                    skip = False
                    continue
                if a in {'-U', '-C', '-I', '-X', '-F', '-W'}:
                    skip = True
                    continue
                if str(a).startswith('-'):
                    continue
                files.append(a)
            if len(files) < 2:
                return {'handled': True, 'output': 'diff: missing operand after diff\n',
                        'trap_trigger': False}
            vfs = self.vfs.get(host)
            lines = []
            for f in files:
                path = self._resolve_path(cwd, f)
                if vfs is None or vfs.get(path) is None:
                    lines.append(f'diff: {f}: No such file or directory')
            if lines:
                return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'bash', 'sh'} and not bare_args:
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'bash', 'sh'} and bare_args:
            script = bare_args[0]
            if script.startswith('-'):
                return {'handled': True, 'output': '', 'trap_trigger': False}
            path = self._resolve_path(cwd, script)
            vfs = self.vfs.get(host)
            if vfs is None or vfs.get(path) is None:
                if cmd == 'sh':
                    return {'handled': True, 'output': f"sh: 0: Can't open {script}\n",
                            'trap_trigger': False}
                return {'handled': True,
                        'output': f'bash: {script}: No such file or directory\n',
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'bzip2', 'bunzip2'}:
            files = [a for a in args if not str(a).startswith('-')]
            if not files:
                return {'handled': True, 'output': f'{cmd}: missing operand\n', 'trap_trigger': False}
            lines = [f"{cmd}: Can't open input file {f}: No such file or directory." for f in files]
            return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
        if cmd == 'bg':
            jobs = bare_args or ['%1']
            lines = [f'-bash: bg: {j}: no such job' for j in jobs]
            return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
        if cmd == 'chsh':
            if '-s' in args:
                i = args.index('-s')
                if i + 1 >= len(args):
                    return {'handled': True, 'output': (
                        "chsh: option requires an argument -- 's'\n"
                        "Usage: chsh [options] [LOGIN]\n"
                    ), 'trap_trigger': False}
            return {'handled': True, 'output': 'chsh: PAM: Authentication failure\n',
                    'trap_trigger': False}
        if cmd == 'bind':
            if '-p' in args or not args:
                keys = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
                        ',', '-', '.', '/', '0', '1', 'E', 'P', 'e', 'p']
                lines = [f'"{k}": self-insert' for k in keys]
                return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'join':
            files = [a for a in args if not str(a).startswith('-') and not str(a).startswith('<')]
            names = [f for f in files if f not in {'sort'}]
            if names:
                lines = [f'sort: cannot read: {f}: No such file or directory' for f in names]
                return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': (
                "join: missing operand\nTry 'join --help' for more information.\n"
            ), 'trap_trigger': False}
        if cmd == 'comm':
            files = [a for a in args if not str(a).startswith('-') and not str(a).startswith('<')]
            if len(files) < 2:
                return {'handled': True, 'output': 'comm: missing operand\n', 'trap_trigger': False}
            lines = [f'sort: cannot read: {f}: No such file or directory' for f in files]
            return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
        if cmd == 'telnet':
            dest = ' '.join(bare_args) if bare_args else 'localhost'
            port = '23'
            if len(bare_args) >= 2:
                dest, port = bare_args[0], bare_args[1]
            elif bare_args:
                dest = bare_args[0]
            if str(port) == '22' and str(dest) in {'localhost', '127.0.0.1', '::1'}:
                return {'handled': True, 'output': (
                    "Trying ::1...\n"
                    "Connected to localhost.\n"
                    "Escape character is '^]'.\n"
                    "SSH-2.0-OpenSSH_6.7p1 Debian-5+deb8u8\n"
                ), 'trap_trigger': False}
            if str(dest) in {'localhost', '127.0.0.1', '::1'} or str(port) == '631':
                return {'handled': True, 'output': (
                    'Trying ::1...\n'
                    'Trying 127.0.0.1...\n'
                    'telnet: Unable to connect to remote host: Connection refused\n'
                ), 'trap_trigger': False}
            banner = 'SSH-2.0-OpenSSH_6.7p1 Debian-5+deb8u8' if str(port) == '22' else ''
            out = f"Trying {dest}...\nConnected to {dest}.\nEscape character is '^]'.\n"
            if banner:
                out += banner + '\n'
            return {'handled': True, 'output': out, 'trap_trigger': False}
        if cmd == 'env':
            rest = []
            taking = True
            for a in args:
                if taking and '=' in a and not str(a).startswith('-'):
                    key, val = a.split('=', 1)
                    state['env'][key] = val
                    continue
                taking = False
                rest.append(a)
            if rest:
                result = self.execute_command(session, host, ' '.join(rest))
                if not result.get('handled'):
                    return {'handled': True,
                            'output': f"env: {rest[0]}: No such file or directory\n",
                            'trap_trigger': False, 'exit_code': 127}
                return result
            hidden = {'0', '$', '?', '_'}
            lines = [f'{k}={v}' for k, v in state['env'].items() if k not in hidden]
            return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
        if cmd == 'ps':
            u_val = None
            if '-u' in args:
                try:
                    u_val = args[args.index('-u') + 1]
                except Exception:
                    u_val = None
            elif any(str(a).startswith('-u') and len(a) > 2 for a in args):
                u_val = next((a[2:] for a in args if str(a).startswith('-u') and len(a) > 2), None)
            if u_val and u_val not in {user, 'root'} and not str(u_val).isdigit():
                return {'handled': True, 'output': (
                    "error: user name does not exist\n\n"
                    "Usage:\n ps [options]\n\n"
                    " Try 'ps --help <simple|list|output|threads|misc|all>'\n"
                    "  or 'ps --help <s|l|o|t|m|a>'\n"
                    " for additional help text.\n\n"
                    "For more details see ps(1).\n"
                ), 'trap_trigger': False}
            if any(str(a).startswith('--ppid') for a in args):
                return {'handled': True, 'output': (
                    "error: list of process IDs must follow --ppid\n\n"
                    "Usage:\n ps [options]\n\n"
                    " Try 'ps --help <simple|list|output|threads|misc|all>'\n"
                    "  or 'ps --help <s|l|o|t|m|a>'\n"
                    " for additional help text.\n\n"
                    "For more details see ps(1).\n"
                ), 'trap_trigger': False}
            # Support common long listings used by fingerprinting attackers.
            # Match aux / auxww / -aux / eax etc. (flag tokens may append w).
            joined = ' '.join(args)
            long_list = (
                any(flag in args for flag in ('-ef', '-e', '-aux'))
                or any(a.lstrip('-').startswith('aux') for a in args)
                or any(set(a.lstrip('-')) <= set('aefljmx') and ('a' in a or 'e' in a)
                       for a in args if a.lstrip('-').isalpha())
                or 'aux' in joined
            )
            # Process table used by both long and pid-filtered views.
            # Diversified VSZ/RSS so identical canned metrics cannot fingerprint us.
            table = [
                ('root', 1, 0, '/sbin/init', '?', 'Ss', 168124, 12384),
                ('root', 412, 1, '/lib/systemd/systemd-journald', '?', 'Ss', 78920, 9216),
                ('root', 512, 1, '/usr/sbin/sshd -D', '?', 'Ss', 15432, 8764),
                ('root', 880, 1, '/usr/sbin/cron -f', '?', 'Ss', 7064, 2688),
                ('message+', 901, 1, '@dbus-daemon --system', '?', 'Ss', 8896, 4224),
                ('systemd+', 940, 1, '/lib/systemd/systemd-networkd', '?', 'Ss', 16244, 6784),
                ('root', 2140, 512, f'sshd: {user} [priv]', '?', 'Ss', 17288, 10240),
                (user, 2144, 2140, f'sshd: {user}@pts/0', '?', 'S', 17288, 5632),
                (user, 2145, 2144, '-bash', 'pts/0', 'Ss', 9876, 5120),
                (user, 2410, 2145, 'ps ' + ' '.join(args), 'pts/0', 'R+', 11740, 3456),
            ]
            pid_filter = None
            if '-p' in args:
                try:
                    pid_filter = int(args[args.index('-p') + 1])
                except Exception:
                    pid_filter = None
            rows = [row for row in table if pid_filter is None or row[1] == pid_filter]
            if long_list and pid_filter is None:
                return {'handled': True, 'output': (
                    'USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\n'
                    + ''.join(
                        f'{uname:10s} {pid:5d}  0.0  0.1 {vsz:6d} {rss:5d} {tty:7s} {stat}   '
                        f'{"Oct01" if pid < 2000 else "09:01"}   0:00 {cmd}\n'
                        for uname, pid, _ppid, cmd, tty, stat, vsz, rss in rows
                    )
                ), 'trap_trigger': False}
            x_style = any(a in {'-x', 'x'} or (str(a).lstrip('-') == 'x') for a in args) or (
                any(str(a).lstrip('-') == 'x' or str(a) == '-x' for a in args))
            if (not long_list) and ('x' in ''.join(a.lstrip('-') for a in args if not str(a).startswith('--'))):
                body = 'PID TTY      STAT   TIME COMMAND\n'
                for uname, pid, _ppid, cmdn, tty, stat, _vsz, _rss in rows:
                    body += f'{pid:5d} {tty:8s} {stat:6s} 0:00 {cmdn}\n'
                return {'handled': True, 'output': body, 'trap_trigger': False}
            # Short / filtered view (ps -p 1 -o ... falls back to columns we know).
            body = '  PID TTY          TIME CMD\n'
            for row in rows:
                pid, cmdn, tty = row[1], row[3], row[4]
                body += f'{pid:5d} {tty:8s} 00:00:00 {cmdn.split()[0].lstrip("-")}\n'
            if pid_filter is not None and not rows:
                body = '  PID TTY          TIME CMD\n'
            return {'handled': True, 'output': body, 'trap_trigger': False}
        if cmd in {'ss', 'netstat'}:
            # Distinct ss vs netstat layouts; keep listen table non-identical.
            if cmd == 'ss':
                return {'handled': True, 'output': (
                    'Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process\n'
                    'udp   UNCONN 0      0      127.0.0.53%lo:53          0.0.0.0:*\n'
                    'tcp   LISTEN 0      128          0.0.0.0:22          0.0.0.0:*\n'
                    'tcp   LISTEN 0      128             [::]:22             [::]:*\n'
                ), 'trap_trigger': False}
            uid = int(self.hosts[host]['credential'].get('uid', 1000))
            prefix = ''
            if any((str(a).startswith('-') and not str(a).startswith('--') and 'p' in a[1:])
                   or a in {'-p', '-anp', '-nap'} for a in args) and uid != 0:
                prefix = f'(No info could be read for "-p": geteuid()={uid} but you should be root.)\n'
            return {'handled': True, 'output': (
                prefix +
                'Active Internet connections (servers and established)\n'
                'Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name\n'
                'tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -\n'
                'tcp6       0      0 :::22                   :::*                    LISTEN      -\n'
                'udp        0      0 0.0.0.0:68              0.0.0.0:*                           -\n'
            ), 'trap_trigger': False}
        if cmd == 'tty':
            return {'handled': True, 'output': '/dev/pts/0\n', 'trap_trigger': False}
        if cmd == 'uptime':
            if self.hosts[host].get('os_id') == 'debian' and host != 'userdb':
                return {'handled': True, 'output': (
                    ' 16:41:36 up  1:03,  1 user,  load average: 0.23, 0.05, 0.02\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': ' 09:15:01 up 12 days,  3:45,  1 user,  load average: 0.02, 0.05, 0.01\n',
                    'trap_trigger': False}
        if cmd == 'who':
            if self.hosts[host].get('os_id') == 'debian' and host != 'userdb':
                return {'handled': True, 'output': (
                    f'{user}  pts/1        2024-02-21 16:41 (10.0.2.2)\n'
                ), 'trap_trigger': False}
            if self.hosts[host].get('os_id') == 'debian':
                return {'handled': True, 'output': (
                    f'{user}  pts/0        2024-02-06 15:10 (10.0.2.2)\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': f'{user} pts/0        2024-10-13 09:01 (10.77.0.250)\n',
                    'trap_trigger': False}
        if cmd == 'top':
            if any(a == '-l' or str(a).startswith('-l') for a in args):
                return {'handled': True, 'output': (
                    "top: unknown option 'l'\n"
                    "Usage:\n  top -hv | -bcHiOSs -d secs -n max -u|U user -p pid(s) -o field -w [cols]\n"
                ), 'trap_trigger': False}
            batch = any(a in {'-b', '-n'} or str(a).startswith('-n') or (
                str(a).startswith('-') and 'b' in a[1:] and not str(a).startswith('--')) for a in args)
            if self.hosts[host].get('os_id') == 'debian' and not batch:
                return {'handled': True, 'output': 'TERM environment variable not set.\n',
                        'trap_trigger': False}
            if not state.get('env', {}).get('TERM'):
                return {'handled': True, 'output': 'TERM environment variable not set.\n',
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'w':
            if self.hosts[host].get('os_id') == 'debian':
                return {'handled': True, 'output': (
                    ' 14:12:20 up 10 days,  3:54,  0 users,  load average: 0.00, 0.00, 0.00\n'
                    'USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': (
                ' 09:15:01 up 12 days,  3:45,  1 user,  load average: 0.02, 0.05, 0.01\n'
                f'USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT\n'
                f'{user}    pts/0    10.77.0.250      09:01    0.00s  0.02s  0.00s w\n'
            ), 'trap_trigger': False}
        if cmd in {'type', 'command'}:
            # Builtin lookups used heavily by deception-aware fingerprinting.
            names = [a for a in args if a not in {'-a', '-t', '-p', '-v', '-V', '--'}]
            if not names:
                return {'handled': True, 'output': f'{cmd}: usage error\n', 'trap_trigger': False}
            target = names[0]
            builtins = {'echo', 'printf', 'pwd', 'cd', 'test', '[', 'type', 'command', 'true', 'false'}
            core = {'head', 'cat', 'ls', 'stat', 'sed', 'od', 'id', 'uname', 'hostname', 'whoami',
                    'ps', 'df', 'date', 'mount', 'tty', 'uptime', 'w', 'bash', 'sh', 'dash',
                    'ss', 'netstat', 'ip', 'journalctl', 'free', 'last', 'monit',
                    'ssh', 'scp', 'sftp', 'nc'}
            lines = []
            for name in names:
                if name in builtins:
                    if '-t' in args:
                        lines.append('builtin')
                    elif cmd == 'type' and '-a' in args:
                        lines.append(f'{name} is a shell builtin')
                    else:
                        lines.append(f'{name} is a shell builtin')
                elif name in core or name in {'ssh-keygen', 'ifconfig', 'ip', 'find', 'sudo'}:
                    path = f'/usr/bin/{name}' if name not in {'bash', 'sh'} else f'/bin/{name}'
                    if name == 'bash':
                        path = '/bin/bash'
                    if '-t' in args:
                        lines.append('file')
                    elif cmd == 'command' and '-V' in args:
                        lines.append(f'{name} is {path}')
                    else:
                        lines.append(path if ('-v' in args or cmd == 'command') else f'{name} is {path}')
                else:
                    lines.append(f'bash: type: {name}: not found' if cmd == 'type' else '')
            return {'handled': True, 'output': '\n'.join(line for line in lines if line) + '\n',
                    'trap_trigger': False}
        if cmd in {'test', '['}:
            # Minimal file tests for fingerprinting.
            expr = args[:-1] if cmd == '[' and args and args[-1] == ']' else args
            code = 1
            if len(expr) >= 2 and expr[0] in {'-e', '-f', '-d', '-x', '-r', '-w'}:
                path = self._resolve_path(cwd, expr[1])
                files = self._host_files(host)
                exists = (
                    path in files
                    or path in {'/', '/bin', '/usr', '/usr/bin', '/etc', '/home', '/var', '/tmp', '/proc', '/dev', '/bin/bash', '/bin/sh', '/usr/bin/sed', '/usr/bin/head', '/usr/bin/cat', '/usr/bin/stat', '/usr/bin/ls'}
                    or any(f.startswith(path.rstrip('/') + '/') for f in files)
                )
                if expr[0] == '-d':
                    code = 0 if (exists and path not in files) or path in {'/', '/bin', '/usr', '/usr/bin', '/etc', '/home', '/var', '/tmp', '/proc', '/dev'} else 1
                else:
                    code = 0 if exists else 1
            # Bash `test` in a compound command usually contributes no stdout.
            return {'handled': True, 'output': '', 'trap_trigger': False, 'exit_code': code}
        if cmd == 'mount':
            wants_opt = any(
                a in {'-t', '-o'} or str(a).startswith('-t') or str(a).startswith('-o')
                for a in args)
            if wants_opt and user != 'root':
                if any(a == '-o' or str(a).startswith('-o') for a in args):
                    return {'handled': True, 'output': (
                        'mount: only root can use "--options" option\n'
                    ), 'trap_trigger': False}
                return {'handled': True, 'output': 'mount: only root can do that\n',
                        'trap_trigger': False}
            return {'handled': True, 'output': (
                'sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)\n'
                'proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)\n'
                'udev on /dev type devtmpfs (rw,nosuid,relatime)\n'
                'tmpfs on /run type tmpfs (rw,nosuid,nodev,noexec,relatime,size=1638400k,mode=755)\n'
                f'/dev/sda1 on / type ext4 (rw,relatime)\n'
            ), 'trap_trigger': False}
        if cmd == 'ip':
            ip = self.hosts[host].get('ip', '10.77.0.10')
            if not args or args[0] in {'a', 'addr', 'address'}:
                return {'handled': True, 'output': (
                    '1: lo: <LOOPBACK,UP> mtu 65536\n'
                    '    inet 127.0.0.1/8 scope host lo\n'
                    f'2: eth0: <BROADCAST,MULTICAST,UP> mtu 1500\n'
                    f'    inet {ip}/24 scope global eth0\n'), 'trap_trigger': False}
            if args[0] in {'r', 'route'}:
                return {'handled': True, 'output': (
                    'default via 10.77.0.1 dev eth0\n'
                    f'10.77.0.0/24 dev eth0 proto kernel scope link src {ip}\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'ssh', 'scp', 'sftp', 'nc', 'netcat', 'ncat'}:
            # Never LLM-fallback outbound SSH/netcat: that invents extra hosts
            # (root@user / 192.168.1.50) which Mode A then cites as canned templates.
            dest = '0.0.0.0'
            port = '22'
            for tok in reversed(args):
                if tok.startswith('-'):
                    continue
                if cmd in {'nc', 'netcat', 'ncat'} and tok.isdigit():
                    port = tok
                    continue
                dest = tok.split('@')[-1].split(':')[0] or dest
                if ':' in tok.split('@')[-1]:
                    maybe = tok.split('@')[-1].split(':')[-1]
                    if maybe.isdigit():
                        port = maybe
                break
            if '-p' in args:
                try:
                    port = args[args.index('-p') + 1]
                except Exception:
                    pass
            if cmd in {'nc', 'netcat', 'ncat'}:
                return {'handled': True,
                        'output': f'{cmd}: connect to {dest} port {port} (tcp) failed: Connection refused\n',
                        'trap_trigger': False, 'exit_code': 1}
            looks_ip = dest.count('.') == 3 and all(p.isdigit() for p in dest.split('.'))
            if not looks_ip and dest not in {'localhost', '127.0.0.1'} and '.' not in dest:
                return {'handled': True,
                        'output': (
                            f'ssh: Could not resolve hostname {dest}: '
                            f'No address associated with hostname\n'
                        ), 'trap_trigger': False, 'exit_code': 255}
            return {'handled': True,
                    'output': f'ssh: connect to host {dest} port {port}: Connection refused\n',
                    'trap_trigger': False, 'exit_code': 255}
        if cmd == 'sed':
            # Minimal passthrough for fingerprint pipelines.
            if bare_args:
                read = self._read_file(session, host, self._resolve_path(cwd, bare_args[-1]))
                return {'handled': True, 'output': read['output'],
                        'trap_trigger': read.get('trap_trigger', False)}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'grep', 'egrep', 'fgrep'}:
            if not bare_args:
                return {'handled': True, 'output': 'Usage: grep [OPTION]... PATTERN [FILE]...\n',
                        'trap_trigger': False}
            pattern = bare_args[0]
            files = bare_args[1:] or []
            vfs = self.vfs.get(host)
            expanded = []
            for raw in files:
                if '*' in raw or '?' in raw:
                    path = self._resolve_path(cwd, raw)
                    parent = str(PurePosixPath(path).parent)
                    pat = PurePosixPath(path).name
                    if vfs is not None:
                        node = vfs.get(parent)
                        if node is not None and node.is_dir:
                            hits = [child.path for child in vfs.listdir(parent)
                                    if fnmatch.fnmatch(PurePosixPath(child.path).name, pat)]
                            expanded.extend(hits or [raw])
                            continue
                    expanded.append(raw)
                else:
                    expanded.append(raw)
            files = expanded
            if not files:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            # Support simple alternation and anchors used in recon greps.
            flat = pattern.strip()
            if flat.startswith('(') and flat.endswith(')') and flat.count('(') == 1:
                flat = flat[1:-1]
            alts = [p for p in re.split(r'(?<!\\)\|', flat) if p]
            cleaned = []
            for alt in alts:
                alt = re.sub(r'^\^', '', re.sub(r'\$$', '', alt))
                alt = alt.strip('()')
                if alt:
                    cleaned.append(alt)
            alts = cleaned or [pattern]
            recursive = any(a in {'-r', '-R', '-ri', '-ir', '-riE', '-iEr', '-Er', '-rE'}
                            or (a.startswith('-') and 'r' in a[1:]) for a in args)
            lines = []
            trap = False
            targets = []
            vfs = self.vfs.get(host)
            for raw in files:
                path = self._resolve_path(cwd, raw)
                if recursive and vfs is not None and vfs.is_dir(path):
                    targets.extend(vfs.find(path, type_filter='f', max_results=80))
                    continue
                if vfs is not None and vfs.get(path) is None:
                    prefix = 'grep' if cmd == 'egrep' else cmd
                    lines.append(f'{prefix}: {raw}: No such file or directory')
                    continue
                targets.append(path)
            for path in targets:
                read = self._read_file(session, host, path)
                trap = trap or read.get('trap_trigger', False)
                if 'No such file' in (read.get('output') or '') and read.get('output', '').startswith('cat:'):
                    lines.append(f"grep: {path}: No such file or directory")
                    continue
                for line in read['output'].splitlines():
                    if any(alt.lower() in line.lower() for alt in alts):
                        lines.append(line if not recursive else f'{path}:{line}')
            return {'handled': True, 'output': ('\n'.join(lines) + ('\n' if lines else '')),
                    'trap_trigger': trap}
        if cmd == 'last':
            if self.hosts[host].get('os_id') == 'debian' and host != 'userdb':
                return {'handled': True, 'output': (
                    f'{user}  pts/1        10.0.2.2         Wed Feb 21 16:41   still logged in   \n'
                    f'{user}  pts/0        10.0.2.2         Wed Feb 21 16:41 - 16:41  (00:00)    \n'
                ), 'trap_trigger': False}
            if self.hosts[host].get('os_id') == 'debian':
                return {'handled': True, 'output': (
                    f'{user}  pts/1        10.0.2.2         Wed Feb 21 16:41   still logged in   \n'
                    f'{user}  pts/0        10.0.2.2         Wed Feb 21 16:41 - 16:41  (00:00)    \n'
                    f'{user}  pts/0        10.0.2.2         Wed Feb 21 16:40 - 16:41  (00:00)    \n'
                    f'{user}  pts/0        10.0.2.2         Wed Feb 21 16:39 - 16:40  (00:00)    \n'
                    '\n'
                    'wtmp begins Wed Feb 21 16:30:01 2024\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': (
                f'{user}   pts/0        10.77.0.250      Sun Oct 13 09:01   still logged in\n'
                f'reboot   system boot  5.15.0-97-generi Sat Oct 12 04:12   still running\n'
            ), 'trap_trigger': False}
        if cmd in {'echo', 'printf'}:
            dest, append, clean = None, False, []
            skip_next = False
            for i, a in enumerate(args):
                if skip_next:
                    skip_next = False
                    continue
                if a in {'>', '>>', '1>', '1>>'}:
                    append = a.endswith('>>')
                    dest = args[i + 1] if i + 1 < len(args) else ''
                    skip_next = True
                    continue
                if a.startswith('>>') and len(a) > 2:
                    append, dest = True, a[2:]
                    continue
                if a.startswith('>') and not a.startswith('>&') and len(a) > 1:
                    dest = a[1:]
                    continue
                clean.append(a)
            nl, interpret, body_args = True, False, list(clean)
            if cmd == 'echo':
                while body_args and body_args[0] in {'-e', '-n', '-en', '-ne', '-ee', '-E'}:
                    flag = body_args.pop(0)
                    if 'n' in flag:
                        nl = False
                    if 'e' in flag and 'E' not in flag:
                        interpret = True
            body = ' '.join(body_args) if cmd == 'echo' else ''.join(body_args)
            if cmd == 'printf':
                fmt = body_args[0] if body_args else ''
                try:
                    fmt_u = bytes(fmt, 'utf-8').decode('unicode_escape')
                except Exception:
                    fmt_u = fmt.replace(r'\r', '\r').replace(r'\n', '\n').replace(r'\t', '\t')
                vals = body_args[1:]
                nfields = 0
                k = 0
                while k < len(fmt_u):
                    if fmt_u[k] == '%':
                        if k + 1 < len(fmt_u) and fmt_u[k + 1] == '%':
                            k += 2
                            continue
                        nfields += 1
                        k += 1
                        while k < len(fmt_u) and fmt_u[k] not in 'diouxXeEfFgGaAcs%':
                            k += 1
                    k += 1
                if vals and nfields > 0:
                    chunks = []
                    idx = 0
                    while idx < len(vals):
                        piece = list(vals[idx:idx + nfields])
                        if len(piece) < nfields:
                            piece.extend([''] * (nfields - len(piece)))
                        try:
                            chunks.append(fmt_u % tuple(piece))
                        except Exception:
                            chunks.append(fmt_u)
                            break
                        idx += nfields
                    body = ''.join(chunks)
                else:
                    body = fmt_u
            elif interpret:
                try:
                    body = bytes(body, 'utf-8').decode('unicode_escape')
                except Exception:
                    body = body.replace(r'\r', '\r').replace(r'\n', '\n').replace(r'\t', '\t')
            if dest:
                path = self._resolve_path(cwd, dest)
                parent = str(PurePosixPath(path).parent)
                vfs = self.vfs.get(host)
                parent_ok = vfs is not None and vfs.get(parent) is not None and vfs.get(parent).is_dir
                if not parent_ok:
                    return {'handled': True,
                            'output': f'{self._bash_prefix(host)}: {dest}: {self._enoent(host)}\n',
                            'trap_trigger': False}
                payload = body + ('\n' if cmd == 'echo' and nl else '')
                if append and vfs.get(path) is not None and not vfs.get(path).is_dir:
                    payload = (vfs.get(path).content or '') + payload
                vfs.put_file(path, payload, owner=user, mode='0644')
                return {'handled': True, 'output': '', 'trap_trigger': False}
            if cmd == 'echo':
                return {'handled': True, 'output': body + ('\n' if nl else ''),
                        'trap_trigger': False}
            return {'handled': True, 'output': body + ('\n' if not body.endswith('\n') else ''),
                    'trap_trigger': False}
        if cmd == 'sleep':
            raw = (bare_args[0] if bare_args else '1').strip()
            unit = 1.0
            if raw and raw[-1] in {'s', 'm', 'h'} and raw[:-1]:
                unit = {'s': 1.0, 'm': 60.0, 'h': 3600.0}[raw[-1]]
                raw = raw[:-1]
            try:
                secs = float(raw) * unit if raw else 1.0
            except Exception:
                return {'handled': True, 'output': 'sleep: invalid time interval\n',
                        'trap_trigger': False}
            secs = max(0.0, min(secs, 30.0))
            state['lab_clock_offset'] = float(state.get('lab_clock_offset') or 0.0) + secs
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'date':
            debian = self.hosts[host].get('os_id') == 'debian'
            jessie = debian and host != 'userdb'
            if jessie:
                now = datetime.datetime(2024, 2, 21, 16, 41, 42, tzinfo=datetime.timezone.utc)
                tz = 'GMT'
            else:
                now = datetime.datetime(2024, 10, 13, 9, 15, 1, tzinfo=datetime.timezone.utc)
                tz = 'UTC'
            now = now + datetime.timedelta(seconds=float(state.get('lab_clock_offset') or 0.0))
            fmt_tok = next((a for a in args if str(a).startswith('+')), None)
            if fmt_tok:
                fmt = fmt_tok[1:]
                if fmt == '%s':
                    rendered = str(int(now.timestamp()))
                elif fmt == '%s.%N':
                    rendered = f'{int(now.timestamp())}.000000000'
                else:
                    try:
                        rendered = now.strftime(fmt)
                    except Exception:
                        rendered = now.strftime(f'%a %b %d %H:%M:%S {tz} %Y')
                return {'handled': True, 'output': rendered + '\n', 'trap_trigger': False}
            return {'handled': True,
                    'output': now.strftime(f'%a %b %d %H:%M:%S {tz} %Y') + '\n',
                    'trap_trigger': False}
        if cmd == 'df':
            flag = ''.join(a[1:] for a in args if str(a).startswith('-') and a != '--')
            debian = self.hosts[host].get('os_id') == 'debian'
            if 'i' in flag:
                if debian:
                    return {'handled': True, 'output': (
                        'Filesystem     Inodes IUsed IFree IUse% Mounted on\n'
                        '/dev/sda1        1.2M   38K  1.2M    4% /\n'
                        'udev              60K   284   60K    1% /dev\n'
                        'tmpfs             62K    13   62K    1% /run\n'
                        'tmpfs             62K    13   62K    1% /sys/fs/cgroup\n'
                    ), 'trap_trigger': False}
                return {'handled': True, 'output': (
                    'Filesystem     Inodes IUsed IFree IUse% Mounted on\n'
                    '/dev/sda1        1.2M   38K  1.2M    4% /\n'
                    'tmpfs            124K     1  124K    1% /run\n'
                ), 'trap_trigger': False}
            if 'k' in flag and 'h' not in flag:
                return {'handled': True, 'output': (
                    'Filesystem     1K-blocks    Used Available Use% Mounted on\n'
                    '/dev/sda1       19428636 1113132  17305536   7% /\n'
                ), 'trap_trigger': False}
            if debian and host != 'userdb':
                return {'handled': True, 'output': (
                    'Filesystem      Size  Used Avail Use% Mounted on\n'
                    '/dev/sda1        19G  1.1G   17G   7% /\n'
                    'udev             10M     0   10M   0% /dev\n'
                    'tmpfs           197M  5.4M  192M   3% /run\n'
                    'tmpfs           985M     0  985M   0% /dev/shm\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': (
                'Filesystem      Size  Used Avail Use% Mounted on\n'
                'udev            7.8G     0  7.8G   0% /dev\n'
                'tmpfs           1.6G  1.2M  1.6G   1% /run\n'
                '/dev/sda1        98G   42G   51G  46% /\n'
                'tmpfs           7.8G     0  7.8G   0% /dev/shm\n'
            ), 'trap_trigger': False}
        if cmd == 'free':
            debian = self.hosts[host].get('os_id') == 'debian'
            human = any(a in {'-h', '--human'} or (str(a).startswith('-') and 'h' in a[1:] and not str(a).startswith('--')) for a in args)
            meg = any(a in {'-m', '--mega'} or (str(a).startswith('-') and 'm' in a[1:] and not str(a).startswith('--')) for a in args)
            gig = any(a in {'-g', '--giga'} or (str(a).startswith('-') and 'g' in a[1:]
                       and not str(a).startswith('--')) for a in args)
            if debian and gig:
                return {'handled': True, 'output': (
                    'total       used       free     shared    buffers     cached\n'
                    'Mem:             7          0          7          0          0          0\n'
                    '-/+ buffers/cache:          0          7\n'
                    'Swap:            1          0          1\n'
                ), 'trap_trigger': False}
            if debian and (meg or not human):
                return {'handled': True, 'output': (
                    'total       used       free     shared    buffers     cached\n'
                    'Mem:          8005        643       7362        105        137        340\n'
                    '-/+ buffers/cache:        165       7840\n'
                    'Swap:         1375          0       1375\n'
                ), 'trap_trigger': False}
            if human:
                return {'handled': True, 'output': (
                    '               total        used        free      shared  buff/cache   available\n'
                    'Mem:            15Gi       2.3Gi       8.0Gi        18Mi       5.2Gi        12Gi\n'
                    'Swap:          2.0Gi          0B       2.0Gi\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': (
                '               total        used        free      shared  buff/cache   available\n'
                'Mem:        16384000     2456780     8390124      18432     5537096    13587220\n'
                'Swap:        2097148           0     2097148\n'
            ), 'trap_trigger': False}
        if cmd == 'ls':
            long_format = any(a in {'-l', '-la', '-al', '-ld', '-dl', '-alh', '-lah', '-lha'}
                              or (a.startswith('-') and 'l' in a[1:] and not a.startswith('--')) for a in args)
            directory_only = any(a == '-d' or (a.startswith('-') and 'd' in a[1:] and a not in {'--'}) for a in args)
            show_all = any(a in {'-a', '-la', '-al', '-alh', '-lah', '-lha', '-A'}
                           or (a.startswith('-') and 'a' in a[1:] and not a.startswith('--')) for a in args)
            human = any(a in {'-h', '-lh', '-hl', '-alh', '-lah', '-lha'}
                        or (a.startswith('-') and 'h' in a[1:] and not a.startswith('--')) for a in args)
            targets = bare_args or [cwd]
            vfs = self.vfs.get(host)
            if len(targets) == 1 and ('*' in str(targets[0]) or '?' in str(targets[0])):
                pattern = self._resolve_path(cwd, targets[0])
                known_dirs = ['/etc/cron.d', '/etc/cron.daily', '/etc/cron.weekly',
                              '/etc/cron.monthly', '/etc/ssh', '/etc/monit', '/etc/logrotate.d']
                matches = [path for path in known_dirs if fnmatch.fnmatch(path, pattern)]
                if not matches:
                    return {'handled': True,
                            'output': f'ls: cannot access {targets[0]}: No such file or directory\n',
                            'trap_trigger': False}
                if vfs is not None:
                    pieces = [vfs.format_ls(path, long_format=long_format, directory_only=directory_only,
                                            show_all=show_all, human=human)
                              for path in matches]
                else:
                    pieces = [self._format_ls(host, path, long_format=long_format,
                                              directory_only=directory_only) for path in matches]
                return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': False}
            pieces = []
            for raw_target in targets:
                if directory_only and raw_target in {'.', './'}:
                    pieces.append('.\n')
                    continue
                path = self._resolve_path(cwd, raw_target)
                if path == '/root' and user != 'root' and not directory_only:
                    pieces.append('ls: cannot open directory /root: Permission denied\n')
                    continue
                if vfs is not None:
                    body = vfs.format_ls(path, long_format=long_format, directory_only=directory_only,
                                         show_all=show_all, human=human)
                else:
                    body = self._format_ls(host, path, long_format=long_format,
                                           directory_only=directory_only)
                if len(targets) > 1 and not body.startswith('ls:') and not directory_only:
                    pieces.append(f'{path}:\n{body}')
                else:
                    pieces.append(body)
            return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': False}
        if cmd == 'head':
            # Support fingerprint probes like: head -c 16 /dev/urandom / head -n 5 file
            count = 10
            skip = set()
            if '-c' in args:
                try:
                    idx = args.index('-c')
                    count = int(args[idx + 1])
                    skip.update({args[idx + 1]})
                except Exception:
                    count = 16
            elif '-n' in args:
                try:
                    idx = args.index('-n')
                    count = int(args[idx + 1])
                    skip.update({args[idx + 1]})
                except Exception:
                    count = 10
            targets = [a for a in bare_args if a not in skip]
            target = targets[0] if targets else ''
            if target in {'/dev/urandom', '/dev/random'}:
                data = bytes(random.randint(0, 255) for _ in range(max(1, min(count, 4096))))
                return {'handled': True, 'output': data.decode('latin1'), 'trap_trigger': False}
            if not target:
                # No FILE: GNU head reads stdin. Non-tty empty stdin → empty output.
                return {'handled': True, 'output': '', 'trap_trigger': False}
            read = self._read_file(session, host, self._resolve_path(cwd, target))
            lines = read['output'].splitlines(True)
            return {'handled': True, 'output': ''.join(lines[:count]),
                    'trap_trigger': read.get('trap_trigger', False)}
        if cmd == 'tail':
            count = 10
            skip = set()
            if '-n' in args:
                try:
                    idx = args.index('-n')
                    count = int(args[idx + 1])
                    skip.add(args[idx + 1])
                except Exception:
                    count = 10
            targets = [a for a in bare_args if a not in skip]
            target = targets[0] if targets else ''
            if not target:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            read = self._read_file(session, host, self._resolve_path(cwd, target))
            if 'Permission denied' in (read.get('output') or '') or 'Keine Berechtigung' in (read.get('output') or ''):
                return {'handled': True, 'output': (
                    f"tail: cannot open ‘{target}’ for reading: Permission denied\n"
                ), 'trap_trigger': False}
            lines = read['output'].splitlines(True)
            return {'handled': True, 'output': ''.join(lines[-count:]),
                    'trap_trigger': read.get('trap_trigger', False)}
        if cmd == 'od':
            # Best-effort hex dump when used after a pipe; alone, read a file if provided.
            if bare_args:
                read = self._read_file(session, host, self._resolve_path(cwd, bare_args[0]))
                raw = read['output'].encode('latin1', 'replace')[:64]
                hexes = ' '.join(f'{b:02x}' for b in raw)
                return {'handled': True, 'output': ' ' + hexes + '\n',
                        'trap_trigger': read.get('trap_trigger', False)}
            return {'handled': True, 'output': '\n', 'trap_trigger': False}
        if cmd == 'stat':
            # Minimal GNU stat -c support for fingerprinting.
            fmt = None
            # Accept both `stat -c %F` and glued `stat -c%F`.
            cleaned_args = []
            for a in args:
                if a.startswith('-c') and a != '-c':
                    fmt = a[2:]
                    continue
                cleaned_args.append(a)
            args = cleaned_args
            if '-c' in args:
                try:
                    fmt = args[args.index('-c') + 1]
                except Exception:
                    fmt = fmt
            targets = [a for a in args if not a.startswith('-') and a != fmt]
            if not targets:
                return {'handled': True, 'output': 'stat: missing operand\n', 'trap_trigger': False}
            vfs = self.vfs.get(host)
            if vfs is not None:
                pieces = []
                for raw in targets:
                    path = self._resolve_path(cwd, raw)
                    pieces.append(vfs.format_stat(path, fmt=fmt))
                return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': False}
            lines = []
            for raw in targets:
                path = self._resolve_path(cwd, raw)
                files = self._host_files(host)
                digest = hashlib.sha256(f'{host}|stat|{path}'.encode()).hexdigest()
                # Keep mtimes before the fixed lab clock (2024-10-13 09:15:01).
                stamp = (
                    f'2024-'
                    f'{1 + int(digest[1:3], 16) % 9:02d}-'
                    f'{1 + int(digest[3:5], 16) % 27:02d} '
                    f'{int(digest[5:7], 16) % 24:02d}:{int(digest[7:9], 16) % 60:02d}:00.000000000 +0000'
                )
                has_children = any(f.startswith(path.rstrip('/') + '/') for f in files)
                if path in files and not (self._is_directory(host, path) and has_children):
                    item = files[path]
                    meta = filesystem_metadata(item)
                    owner = self._path_owner(host, path, meta)
                    mode_digits = self._display_mode(user, path, meta)
                    values = {
                        '%n': path,
                        '%F': 'regular file',
                        '%a': mode_digits.lstrip('0') or mode_digits,
                        '%A': '-' + self._mode_human(mode_digits),
                        '%U': owner,
                        '%G': owner,
                        '%i': str(10000 + (abs(hash(path)) % 50000)),
                        '%s': str(len((item.get('content') or '').encode())),
                        '%y': self._mtime_for(host, path, meta),
                    }
                else:
                    synthetic = self._system_file(host, path)
                    common_bins = {'/bin/bash', '/bin/sh', '/bin/cat', '/usr/bin/sed', '/usr/bin/head',
                                   '/usr/bin/cat', '/usr/bin/stat', '/usr/bin/ls', '/bin/ls'}
                    if synthetic is not None:
                        values = {
                            '%n': path, '%F': 'regular file', '%a': '644',
                            '%A': '-rw-r--r--',
                            '%U': 'root', '%G': 'root',
                            '%i': str(31000 + (abs(hash(path)) % 50000)),
                            '%s': str(len(synthetic.encode())),
                            '%y': stamp,
                        }
                    elif path in common_bins:
                        size = 1396520 if path.endswith('bash') else (35000 + (abs(hash(path)) % 20000))
                        values = {
                            '%n': path, '%F': 'regular file', '%a': '755',
                            '%A': '-rwxr-xr-x',
                            '%U': 'root', '%G': 'root',
                            '%i': str(30000 + (abs(hash(path)) % 50000)), '%s': str(size),
                            '%y': stamp,
                        }
                    elif self._is_directory(host, path):
                        owner = self._path_owner(host, path)
                        values = {
                            '%n': path, '%F': 'directory', '%a': '755',
                            '%A': 'drwxr-xr-x',
                            '%U': owner, '%G': owner,
                            '%i': str(20000 + (abs(hash(path)) % 50000)), '%s': '4096',
                            '%y': self._mtime_for(host, path),
                        }
                    else:
                        lines.append(f"stat: cannot statx '{path}': No such file or directory")
                        continue
                if fmt:
                    out = fmt
                    # Longer tokens first so %A is not partially eaten by %a.
                    for key in sorted(values.keys(), key=len, reverse=True):
                        out = out.replace(key, values[key])
                    lines.append(out)
                else:
                    lines.append(
                        f"  File: {values['%n']}\n"
                        f"  Size: {values['%s']}\tBlocks: 8 IO Block: 4096 {values['%F']}\n"
                        f"Access: ({values['%a']}/)  Uid: ({values['%U']})  Gid: ({values['%G']})\n"
                        f"Modify: {values.get('%y', '2024-03-01 09:00:00.000000000 +0000')}"
                    )
            return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
        if cmd in {'cat', 'less', 'more'}:
            if not bare_args:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            # Expand a trailing basename glob against VFS (then lure files).
            target = bare_args[0]
            if '*' in target or '?' in target:
                pattern = self._resolve_path(cwd, target)
                parent = str(PurePosixPath(pattern).parent)
                pat = PurePosixPath(pattern).name
                vfs = self.vfs.get(host)
                matches = []
                parent_exists = False
                if vfs is not None:
                    parent_node = vfs.get(parent)
                    parent_exists = parent_node is not None and parent_node.is_dir
                    if parent_exists:
                        matches = [child.path for child in vfs.listdir(parent)
                                   if fnmatch.fnmatch(PurePosixPath(child.path).name, pat)
                                   and not child.is_dir]
                if not matches:
                    files = self._host_files(host)
                    matches = [path for path in sorted(files) if fnmatch.fnmatch(path, pattern)]
                    parent_exists = parent_exists or (
                        parent in files
                        or parent in {'/', '/home', '/etc', '/var', '/tmp', '/opt'}
                        or any(f.startswith(parent.rstrip('/') + '/') for f in files)
                    )
                if not matches:
                    # Bash without nullglob cats the unexpanded glob as a path.
                    msg = (f'{cmd}: {target}: No such file or directory\n'
                           if parent_exists else
                           f'{cmd}: {parent}: No such file or directory\n')
                    return {'handled': True, 'output': msg, 'trap_trigger': False}
                pieces, trap = [], False
                for path in matches:
                    result = self._read_file(session, host, path)
                    pieces.append(result['output'])
                    trap = trap or result.get('trap_trigger', False)
                return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': trap}
            path = self._resolve_path(cwd, target)
            display = target if '/' not in target else None
            result = self._read_file(session, host, path, display=display)
            if cmd in {'less', 'more'} and 'No such file' in (result.get('output') or ''):
                out = (result.get('output') or '').replace('cat: ', '', 1)
                return {'handled': True, 'output': out, 'trap_trigger': False}
            return result
        if cmd == 'file':
            if not bare_args:
                return {'handled': True, 'output': 'file: missing operand\n', 'trap_trigger': False}
            path = self._resolve_path(cwd, bare_args[0])
            files = self._host_files(host)
            if path not in files:
                return {'handled': True, 'output': f'{path}: cannot open `{path}\' (No such file or directory)\n',
                        'trap_trigger': False}
            content = files[path].get('content', '')
            lower = path.lower()
            if 'BEGIN OPENSSH PRIVATE KEY' in content or lower.endswith(('.key', '.pem')):
                kind = 'OpenSSH private key'
            elif lower.endswith('.php'):
                kind = 'PHP script, ASCII text'
            elif lower.endswith('.sql'):
                kind = 'ASCII text'
            elif lower.endswith('.csv'):
                kind = 'CSV text'
            else:
                kind = 'ASCII text'
            return {'handled': True, 'output': f'{path}: {kind}\n', 'trap_trigger': False}
        if cmd == 'which':
            if not bare_args:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            known = {'ls', 'cat', 'find', 'id', 'whoami', 'uname', 'hostname', 'pwd', 'ps', 'ss',
                     'ip', 'env', 'sudo', 'file', 'head', 'tail', 'bash', 'sh', 'groups', 'stat', 'wc'}
            if bare_args[0] in known:
                return {'handled': True, 'output': f'/usr/bin/{bare_args[0]}\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'groups':
            return {'handled': True, 'output': f'{user}\n', 'trap_trigger': False}
        if cmd == 'stat':
            if not bare_args:
                return {'handled': True, 'output': 'stat: missing operand\n', 'trap_trigger': False}
            vfs = self.vfs.get(host)
            pieces = []
            for raw in bare_args:
                path = self._resolve_path(cwd, raw)
                if vfs is not None:
                    fmt = None
                    if '-c' in args:
                        try:
                            fmt = args[args.index('-c') + 1]
                        except Exception:
                            fmt = None
                    pieces.append(vfs.format_stat(path, fmt=fmt))
                    continue
                files = self._host_files(host)
                if path not in files and self._system_file(host, path) is None:
                    pieces.append(f"stat: cannot statx '{path}': No such file or directory\n")
                    continue
                item = files.get(path) or {'content': self._system_file(host, path) or '', 'metadata': {}}
                meta = filesystem_metadata(item) if path in files else {
                    'owner': 'root', 'group': 'root', 'mode': '0644',
                    'size': len((item.get('content') or '').encode()), 'mtime': '2024-03-01T09:00:00Z'}
                owner = meta.get('owner', user)
                size = meta.get('size', len((item.get('content') or '').encode()))
                pieces.append(
                    f'  File: {path}\n'
                    f'  Size: {size}\tBlocks: {max(8, size // 512 + 1)} IO Block: 4096\n'
                    f'Access: ({meta.get("mode", "0644")}/{format_mode(meta.get("mode", "0644"))})  '
                    f'Uid: ({owner})  Gid: ({owner})\n'
                    f'Modify: {meta.get("mtime", "2024-03-01T09:00:00Z")}\n'
                )
            return {'handled': True, 'output': ''.join(pieces), 'trap_trigger': False}
        if cmd == 'wc':
            if not bare_args:
                if '-l' in args and '-c' not in args and '-w' not in args:
                    return {'handled': True, 'output': '0\n', 'trap_trigger': False}
                if '-c' in args and '-l' not in args and '-w' not in args:
                    return {'handled': True, 'output': '0\n', 'trap_trigger': False}
                if '-w' in args and '-l' not in args and '-c' not in args:
                    return {'handled': True, 'output': '0\n', 'trap_trigger': False}
                return {'handled': True, 'output': '0 0 0\n', 'trap_trigger': False}
            path = self._resolve_path(cwd, bare_args[-1])
            result = self._read_file(session, host, path)
            if 'No such file' in result['output']:
                shown = bare_args[-1]
                return {'handled': True, 'output': f'wc: {shown}: No such file or directory\n',
                        'trap_trigger': False}
            text = result['output']
            lines = text.count('\n')
            words = len(text.split())
            chars = len(text.encode())
            if '-c' in args and '-l' not in args and '-w' not in args:
                return {'handled': True, 'output': f'{chars} {path}\n', 'trap_trigger': False}
            return {'handled': True, 'output': f'{lines} {words} {chars} {path}\n', 'trap_trigger': False}
        if cmd == 'find':
            start_paths = []
            i = 0
            while i < len(args) and not str(args[i]).startswith('-') and args[i] not in {'(', ')', '!', ','}:
                start_paths.append(args[i])
                i += 1
            if not start_paths:
                start_paths = ['.']
            find_pred = {
                '-name', '-iname', '-type', '-user', '-perm', '-mtime', '-mmin', '-newer',
                '-newerct', '-newermt', '-cmin', '-amin', '-cnewer', '-anewer', '-exec',
                '-execdir', '-print', '-print0', '-printf', '-fprintf', '-fprint', '-ls',
                '-fls', '-maxdepth', '-mindepth', '-o', '-or', '-a', '-and', '-not', '!',
                '(', ')', ',', '-path', '-ipath', '-wholename', '-iwholename', '-prune',
                '-follow', '-xdev', '-size', '-empty', '-nogroup', '-nouser', '-readable',
                '-writable', '-daystart', '-regex', '-iregex', '-lname', '-ilname', '-links',
                '-inum', '-samefile', '-used', '-true', '-false', '-ok', '-okdir', '-delete',
                '-quit', '-noleaf', '-mount', '-warn', '-nowarn', '-version', '-help',
                '-H', '-L', '-P', '-group', '-uid', '-gid', '-fstype', '-xtype', '-regextype',
            }
            takes_arg = {
                '-name', '-iname', '-type', '-user', '-perm', '-mtime', '-mmin', '-newer',
                '-newerct', '-newermt', '-cmin', '-amin', '-cnewer', '-anewer', '-path',
                '-ipath', '-wholename', '-regex', '-iregex', '-lname', '-ilname', '-size',
                '-maxdepth', '-mindepth', '-group', '-uid', '-gid', '-fstype', '-links',
                '-inum', '-samefile', '-used', '-printf', '-fprintf', '-fprint', '-regextype',
            }
            j = 0
            while j < len(args):
                st = str(args[j])
                if st in {'-exec', '-execdir', '-ok', '-okdir'}:
                    break
                if st.startswith('-') and st not in find_pred and not st.startswith('-O') and not st.startswith('-D'):
                    return {'handled': True,
                            'output': f"find: unknown predicate `{st}'\n",
                            'trap_trigger': False}
                if st in takes_arg:
                    j += 2
                    continue
                j += 1
            for flag in ('-nogroup', '-nouser', '-empty', '-true', '-false'):
                if flag in args:
                    idx = args.index(flag)
                    if idx + 1 < len(args):
                        nxt = args[idx + 1]
                        if not str(nxt).startswith('-') and nxt not in {'!', '(', ')', ','}:
                            return {'handled': True, 'output': (
                                f'find: paths must precede expression: {nxt}\n'
                                'Usage: find [-H] [-L] [-P] [-Olevel] [-D '
                                'help|tree|search|stat|rates|opt|exec] [path...] [expression]\n'
                            ), 'trap_trigger': False}
            def _expand_find_path(raw):
                text = str(raw)
                if text.startswith('~/'):
                    return f'{state["env"]["HOME"]}/{text[2:]}'
                if text.startswith('~') and len(text) > 1:
                    body = text[1:]
                    if '/' in body:
                        who, rest = body.split('/', 1)
                        return f'/home/{who}/{rest}'
                    return f'/home/{body}' if body else state['env']['HOME']
                return text
            if '-newer' in args:
                try:
                    ref = args[args.index('-newer') + 1]
                except Exception:
                    ref = ''
                if ref:
                    rpath = self._resolve_path(cwd, _expand_find_path(ref))
                    xvfs = self.vfs.get(host)
                    if xvfs is None or xvfs.get(rpath) is None:
                        return {'handled': True, 'output': (
                            f"find: {self._find_quote(host, ref)}: No such file or directory\n"
                        ), 'trap_trigger': False}
            if '-user' in args:
                try:
                    want = args[args.index('-user') + 1]
                except Exception:
                    want = ''
                known = {user, 'root', 'daemon', 'bin', 'sys', 'nobody', 'www-data',
                         'message+', 'messagebus', 'sshd', 'backup', 'list'}
                if want and want not in known:
                    return {'handled': True, 'output': (
                        f"find: {self._find_quote(host, want)} is not the name of a known user\n"
                    ), 'trap_trigger': False}
            if '-exec' in args:
                rest = args[args.index('-exec') + 1:]
                if rest and not any(t in {';', '\\;', '+'} for t in rest):
                    return {'handled': True,
                            'output': "find: missing argument to `-exec'\n",
                            'trap_trigger': False}
            perm = args[args.index('-perm') + 1] if '-perm' in args and args.index('-perm') + 1 < len(args) else ''
            suid_probe = bool(perm) and any(x in str(perm) for x in ('4000', '2000', 'u=s', 'g=s', '/4000', '-4000'))
            type_filter = None
            if '-type' in args:
                try:
                    type_filter = args[args.index('-type') + 1]
                except Exception:
                    type_filter = None
            name = args[args.index('-name') + 1].strip('\'"') if '-name' in args else None
            iname = args[args.index('-iname') + 1].strip('\'"') if '-iname' in args else None
            want_user = args[args.index('-user') + 1] if '-user' in args else None
            name_neg = False
            if '-name' in args:
                ni = args.index('-name')
                if ni > 0 and str(args[ni - 1]) in {'!', '-not'}:
                    name_neg = True
            maxdepth = None
            if '-maxdepth' in args:
                try:
                    maxdepth = int(args[args.index('-maxdepth') + 1])
                except Exception:
                    maxdepth = None
            vfs = self.vfs.get(host)
            err, hits = [], []
            for raw in start_paths:
                resolved = self._resolve_path(cwd, _expand_find_path(raw))
                node = vfs.get(resolved) if vfs is not None else None
                if node is None:
                    err.append(f"find: {self._find_quote(host, raw)}: No such file or directory")
                    continue
                if suid_probe:
                    suid = ['/usr/bin/sudo', '/usr/bin/passwd', '/usr/bin/newgrp', '/bin/su',
                            '/usr/bin/chsh', '/usr/bin/chfn']
                    hits.extend([p for p in suid if resolved == '/' or p.startswith(resolved.rstrip('/') + '/')])
                    continue
                paths = vfs.find(resolved, name=name, iname=iname, user=want_user,
                                 type_filter=type_filter, maxdepth=maxdepth,
                                 name_neg=name_neg) if vfs is not None else []
                if '-name' not in args and '-iname' not in args and '-user' not in args and resolved == '/':
                    paths = paths[:40]
                for path in paths:
                    if raw in {'.', './'}:
                        if path == resolved or path == resolved.rstrip('/'):
                            hits.append('.' if raw == '.' else './')
                        else:
                            restp = path[len(resolved.rstrip('/')):].lstrip('/')
                            hits.append('./' + restp if restp else '.')
                    else:
                        hits.append(path)
            if (self.hosts[host].get('os_id') == 'debian'
                    and any(self._resolve_path(cwd, r) == '/' for r in start_paths)
                    and (name or iname)):
                err.extend([
                    "find: `/proc/tty/driver': Permission denied",
                    "find: `/proc/1/task/1/fd': Permission denied",
                ])
            if '-exec' in args or '-execdir' in args:
                flag = '-exec' if '-exec' in args else '-execdir'
                rest = args[args.index(flag) + 1:]
                exec_cmd = rest[0] if rest else ''
                known_exec = {
                    'split', 'grep', 'egrep', 'fgrep', 'cat', 'chmod', 'chown', 'rm', 'cp',
                    'mv', 'sort', 'sh', 'bash', 'sleep', 'md5sum', 'sha1sum', 'file', 'wc',
                    'sed', 'awk', 'head', 'tail', 'ls', 'echo', 'true', 'false',
                }
                if exec_cmd and exec_cmd not in {';', '\\;', '+', '{}'} and exec_cmd not in known_exec:
                    n = max(4, min(12, len(hits) or 4))
                    msg = f"find: {self._find_quote(host, exec_cmd)}: No such file or directory"
                    return {'handled': True, 'output': '\n'.join([msg] * n) + '\n',
                            'trap_trigger': False}
            body = ''
            if err:
                body += '\n'.join(err) + '\n'
            if hits:
                mtime_tok = None
                if '-mtime' in args:
                    try:
                        mtime_tok = str(args[args.index('-mtime') + 1])
                    except Exception:
                        mtime_tok = None
                recent = bool(mtime_tok and str(mtime_tok).startswith('-'))
                if '-inum' in args:
                    hits = []
                elif ((recent or '-newerct' in args or '-newermt' in args or '-cmin' in args)
                      and type_filter == 'd'):
                    hits = [h for h in hits if h in {'.', './'}] or (
                        ['.'] if any(s in {'.', './'} for s in start_paths) else [])
                elif (maxdepth == 1 and type_filter == 'd'
                      and all(s in {'.', './'} for s in start_paths)):
                    hits = [h for h in hits if h in {'.', './'}] or ['.']
                body += '\n'.join(hits) + '\n'
            return {'handled': True, 'output': body, 'trap_trigger': False}
        if cmd == 'awk':
            files = [a for a in args if not str(a).startswith('-')
                     and not str(a).startswith('{')
                     and 'print' not in a and 'NR' not in a and 'FNR' not in a and '$' not in a]
            vfs = self.vfs.get(host)
            for raw in files:
                if vfs is None or vfs.get(self._resolve_path(cwd, raw)) is None:
                    return {'handled': True,
                            'output': f'awk: cannot open file {raw} (No such file or directory)\n',
                            'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'cal':
            now = datetime.datetime(2024, 10, 13, 9, 15, 1)
            return {'handled': True, 'output': calendar.month(now.year, now.month),
                    'trap_trigger': False}
        if cmd == 'dpkg':
            if ('-S' in args or '--search' in args) and not bare_args:
                return {'handled': True, 'output': (
                    "dpkg-query: error: --search needs at least one file name pattern argument\n"
                    "\nUse --help for help about querying packages.\n"
                ), 'trap_trigger': False}
            if '-l' in args or '--list' in args:
                return {'handled': True, 'output': (
                    'Desired=Unknown/Install/Remove/Purge/Hold\n'
                    '| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend\n'
                    '|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)\n'
                    '||/ Name                           Version                         Architecture Description\n'
                    '+++-==============================-===============================-============-=================================\n'
                    'ii  acpi                           1.7-1                           amd64        displays information on ACPI devices\n'
                    'ii  dmsetup                        2:1.02.90-2.2+deb8u1            amd64        Linux Kernel Device Mapper userspace library\n'
                    'ii  vim                            2:7.4.488-7+deb8u3              amd64        Vi IMproved - enhanced vi editor\n'
                    'ii  vim-common                     2:7.4.488-7+deb8u3              amd64        Vi IMproved - Common files\n'
                    'ii  vim-tiny                       2:7.4.488-7+deb8u3              amd64        Vi IMproved - enhanced vi editor - compact version\n'
                ), 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'du':
            targets = bare_args or ['.']
            vfs = self.vfs.get(host)
            missing = []
            for t in targets:
                if vfs is None or vfs.get(self._resolve_path(cwd, t)) is None:
                    missing.append(f"du: cannot access ‘{t}’: No such file or directory")
            if missing:
                return {'handled': True, 'output': '\n'.join(missing) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '4096\t.\n', 'trap_trigger': False}
        if cmd == 'exec':
            name = bare_args[0] if bare_args else '1'
            return {'handled': True,
                    'output': f'{self._bash_prefix(host)}: exec: {name}: not found\n',
                    'trap_trigger': False}
        if cmd == 'exit':
            return {'handled': True, 'output': 'logout\n', 'trap_trigger': False}
        if cmd == 'fg':
            job = bare_args[0] if bare_args else 'current'
            return {'handled': True, 'output': f'-bash: fg: {job}: no such job\n',
                    'trap_trigger': False}
        if cmd == 'jobs':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'seq':
            try:
                nums = [int(x) for x in bare_args]
            except Exception:
                return {'handled': True, 'output': 'seq: invalid floating point argument\n',
                        'trap_trigger': False}
            if not nums:
                return {'handled': True, 'output': 'seq: missing operand\n', 'trap_trigger': False}
            start, end = (1, nums[0]) if len(nums) == 1 else (nums[0], nums[1])
            step = 1 if end >= start else -1
            return {'handled': True,
                    'output': ''.join(f'{i}\n' for i in range(start, end + step, step)),
                    'trap_trigger': False}
        if cmd == 'yes':
            token = bare_args[0] if bare_args else 'y'
            return {'handled': True, 'output': (token + '\n') * 120, 'trap_trigger': False}
        if cmd == 'xargs':
            rest = []
            skip_next = False
            for tok in args:
                if skip_next:
                    skip_next = False
                    continue
                if tok in {'-0', '-r', '-t'}:
                    continue
                if tok in {'-I', '-i', '-n', '-L', '-P'}:
                    skip_next = True
                    continue
                if tok.startswith('-n') and tok != '-n':
                    continue
                rest.append(tok)
            inner = ' '.join(rest)
            if inner:
                return self.execute_command(session, host, inner)
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'zless', 'zcat', 'zmore', 'gzcat'}:
            raw = bare_args[0] if bare_args else ''
            gz = raw if str(raw).endswith('.gz') else (f'{raw}.gz' if raw else '')
            lines = []
            if gz:
                lines.append(f'gzip: {gz}: No such file or directory')
            if raw and not str(raw).endswith('.gz'):
                lines.append(f'{raw}: No such file or directory')
            body = ('\n'.join(lines) + '\n') if lines else ''
            return {'handled': True, 'output': body, 'trap_trigger': False}
        if cmd == 'ln':
            files = [a for a in args if not str(a).startswith('-')]
            if len(files) < 2:
                return {'handled': True, 'output': 'ln: missing file operand\n', 'trap_trigger': False}
            dest = files[-1]
            path = self._resolve_path(cwd, dest)
            vfs = self.vfs.get(host)
            parent = str(PurePosixPath(path).parent)
            if vfs is not None and vfs.get(path) is not None:
                return {'handled': True,
                        'output': f"ln: failed to create symbolic link ‘{dest}’: File exists\n",
                        'trap_trigger': False}
            if vfs is not None and vfs.get(parent) is None:
                return {'handled': True, 'output': (
                    f"ln: failed to create symbolic link ‘{dest}’: No such file or directory\n"
                ), 'trap_trigger': False}
            if user != 'root' and (path.startswith('/usr/') or path.startswith('/bin')):
                return {'handled': True,
                        'output': f"ln: failed to create symbolic link ‘{dest}’: Permission denied\n",
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'mkdir':
            if not bare_args:
                return {'handled': True, 'output': (
                    "mkdir: missing operand\nTry 'mkdir --help' for more information.\n"
                ), 'trap_trigger': False}
            parents = any(
                a in {'-p', '--parents'} or (
                    str(a).startswith('-') and not str(a).startswith('--') and 'p' in a[1:])
                for a in args)
            vfs = self.vfs.get(host)
            lines = []
            for t in bare_args:
                path = self._resolve_path(cwd, t)
                node = vfs.get(path) if vfs is not None else None
                if node is not None:
                    if node.is_dir:
                        if parents:
                            continue
                        lines.append(f"mkdir: cannot create directory ‘{t}’: File exists")
                    else:
                        lines.append(f"mkdir: cannot create directory ‘{t}’: File exists")
                    continue
                if vfs is not None:
                    parent = str(PurePosixPath(path).parent)
                    if vfs.get(parent) is None and not parents:
                        lines.append(
                            f"mkdir: cannot create directory ‘{t}’: {self._enoent(host)}")
                    else:
                        vfs.ensure_dir(path, owner=user, mode='0755')
            if lines:
                return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'mktemp':
            if '-p' in args:
                i = args.index('-p')
                if i + 1 >= len(args) or str(args[i + 1]).startswith('-'):
                    return {'handled': True, 'output': (
                        "mktemp: option requires an argument -- 'p'\n"
                        "Try 'mktemp --help' for more information.\n"
                    ), 'trap_trigger': False}
            return {'handled': True, 'output': '/tmp/tmp.XXXXXX\n', 'trap_trigger': False}
        if cmd == 'killall':
            name = bare_args[-1] if bare_args else ''
            return {'handled': True, 'output': f'{name}: no process found\n', 'trap_trigger': False}
        if cmd == 'su':
            target = next((a for a in args if not str(a).startswith('-')), 'root')
            if target not in {user, 'root'}:
                return {'handled': True, 'output': f"No passwd entry for user '{target}'\n",
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'alias':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'export':
            blob = ' '.join(args)
            if '=' in blob:
                assigned = self._run_assignment(session, host, blob)
                if assigned is not None:
                    return assigned
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'eval':
            inner = ' '.join(args)
            if inner:
                return self.execute_command(session, host, inner)
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'man':
            topic = bare_args[0] if bare_args else ''
            if not topic:
                return {'handled': True, 'output': 'What manual page do you want?\n',
                        'trap_trigger': False}
            t = topic.upper()
            return {'handled': True, 'output': (
                f'{t}(1)                     General Commands Manual                    {t}(1)\n\n'
                f'NAME\n       {topic} - {topic}\n'
            ), 'trap_trigger': False}
        if cmd == 'bc':
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'crontab':
            if '-r' in args:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            return {'handled': True, 'output': 'no crontab for %s\n' % user, 'trap_trigger': False}
        if cmd == 'journalctl':
            stamp = 'Jul 10 04:17:01'
            body = (
                f'{stamp} {host} sshd[1422]: Accepted password for {user} '
                f'from 10.77.0.5 port 52114 ssh2\n'
                f'{stamp} {host} sshd[1422]: pam_unix(sshd:session): '
                f'session opened for user {user}(uid=1000) by (uid=0)\n'
                f'{stamp} {host} systemd-logind[811]: New session 12 of user {user}.\n'
            )
            n = 20
            if '-n' in args:
                try:
                    n = int(args[args.index('-n') + 1])
                except Exception:
                    n = 20
            lines = body.splitlines(True)[:max(1, n)]
            return {'handled': True, 'output': ''.join(lines), 'trap_trigger': False}
        if cmd == 'systemctl':
            # Soft stub: services mentioned in notes are inactive, not missing.
            unit = next((a for a in bare_args if a not in {
                'status', 'is-active', 'is-enabled', 'list-units', '--no-pager'}), 'unknown')
            if 'status' in args or (bare_args and bare_args[0] == 'status'):
                return {'handled': True, 'output': (
                    f'○ {unit}.service - {unit}\n'
                    '     Loaded: loaded (/lib/systemd/system/' + unit + '.service; disabled)\n'
                    '     Active: inactive (dead)\n'
                ), 'trap_trigger': False}
            if 'is-active' in args or (bare_args and bare_args[0] == 'is-active'):
                return {'handled': True, 'output': 'inactive\n', 'trap_trigger': False}
            op = next((a for a in bare_args if not str(a).startswith('-') and a not in {
                'status', 'is-active', 'is-enabled', 'list-units', 'start', 'stop'}), None)
            if op:
                return {'handled': True, 'output': f"Unknown operation '{op}'.\n",
                        'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd == 'monit':
            return {'handled': True, 'output': 'monit: cannot connect to the monit daemon\n',
                    'trap_trigger': False}
        if cmd in {'getent', 'sort', 'cut', 'tr', 'uniq', 'awk', 'basename', 'dirname'}:
            # Lightweight presence for stock Ubuntu fingerprinting.
            if cmd == 'getent' and bare_args:
                if bare_args[0] == 'passwd':
                    passwd = self.execute_command(session, host, 'cat /etc/passwd')['output']
                    if len(bare_args) >= 2:
                        name = bare_args[1]
                        for line in passwd.splitlines():
                            if line.startswith(name + ':'):
                                return {'handled': True, 'output': line + '\n', 'trap_trigger': False}
                        return {'handled': True, 'output': '', 'trap_trigger': False}
                    return {'handled': True, 'output': passwd, 'trap_trigger': False}
                if bare_args[0] == 'group':
                    group = self.execute_command(session, host, 'cat /etc/group')['output']
                    if len(bare_args) >= 2:
                        name = bare_args[1]
                        for line in group.splitlines():
                            if line.startswith(name + ':'):
                                return {'handled': True, 'output': line + '\n',
                                        'trap_trigger': False}
                        return {'handled': True, 'output': '', 'trap_trigger': False}
                    return {'handled': True, 'output': group, 'trap_trigger': False}
            if cmd == 'dirname':
                if not bare_args:
                    return {'handled': True, 'output': (
                        "dirname: missing operand\nTry 'dirname --help' for more information.\n"
                    ), 'trap_trigger': False}
                raw = bare_args[0].rstrip('/') or '/'
                parent = str(PurePosixPath(raw).parent)
                return {'handled': True, 'output': parent + '\n', 'trap_trigger': False}
            if cmd == 'sort':
                files = [a for a in bare_args if not str(a).startswith('-')]
                vfs = self.vfs.get(host)
                miss = []
                for f in files:
                    if vfs is None or vfs.get(self._resolve_path(cwd, f)) is None:
                        miss.append(f'sort: cannot read: {f}: No such file or directory')
                if miss:
                    return {'handled': True, 'output': '\n'.join(miss) + '\n', 'trap_trigger': False}
                return {'handled': True, 'output': '', 'trap_trigger': False}
            if cmd == 'cut':
                targets = [a for a in bare_args if not str(a).startswith('-')]
                if targets:
                    raw = targets[-1]
                    path = self._resolve_path(cwd, raw)
                    vfs = self.vfs.get(host)
                    node = vfs.get(path) if vfs is not None else None
                    if node is not None and node.is_dir:
                        return {'handled': True, 'output': f'cut: {raw}: Is a directory\n',
                                'trap_trigger': False}
                    if node is None:
                        return {'handled': True,
                                'output': f'cut: {raw}: No such file or directory\n',
                                'trap_trigger': False}
                return {'handled': True, 'output': '', 'trap_trigger': False}
            return {'handled': True, 'output': '', 'trap_trigger': False}
        if cmd in {'md5sum', 'sha256sum', 'sha1sum'}:
            if '-c' in args or '--check' in args:
                targets = bare_args or []
                lines = []
                for raw in targets:
                    path = self._resolve_path(cwd, raw)
                    read = self._read_file(session, host, path)
                    if 'No such file' in (read.get('output') or ''):
                        lines.append(f'{cmd}: {raw}: No such file or directory')
                        continue
                    body = read.get('output') or ''
                    if not re.search(r'^[0-9a-fA-F]{32,}', body, re.M):
                        kind = 'MD5' if cmd == 'md5sum' else ('SHA256' if cmd == 'sha256sum' else 'SHA1')
                        lines.append(f'{cmd}: {raw}: no properly formatted {kind} checksum lines found')
                if lines:
                    return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': False}
                return {'handled': True, 'output': '', 'trap_trigger': False}
            if not bare_args:
                return {'handled': True, 'output': '', 'trap_trigger': False}
            lines = []
            trap = False
            for raw in bare_args:
                path = self._resolve_path(cwd, raw)
                read = self._read_file(session, host, path)
                if 'No such file' in read['output']:
                    lines.append(f'{cmd}: {path}: No such file or directory')
                    continue
                digest = hashlib.md5(read['output'].encode()).hexdigest()
                if cmd == 'sha256sum':
                    digest = hashlib.sha256(read['output'].encode()).hexdigest()
                elif cmd == 'sha1sum':
                    digest = hashlib.sha1(read['output'].encode()).hexdigest()
                lines.append(f'{digest}  {path}')
                trap = trap or read.get('trap_trigger', False)
            return {'handled': True, 'output': '\n'.join(lines) + '\n', 'trap_trigger': trap}

        return {'handled': False, 'output': '', 'trap_trigger': False, 'unhandled_command': text}

    def shell(self, session, host, command):
        # Attackers often send semicolon-chained recon. Execute supported atoms
        # sequentially so compound input does not collapse to the unsupported stub.
        result = self.execute_command(session, host, command)
        if result['handled']:
            return result['output']
        token = command.strip().split(maxsplit=1)[0] if command.strip() else 'command'
        if '/' in token:
            token = token.rsplit('/', 1)[-1]
        return f"bash: {token}: command not found\n"


def materialize(honey, traps, topology, seed=0):
    result = copy.deepcopy(honey)
    roles = {h["name"]: h for h in topology["hosts"]}
    hosts = {h["name"]: h for h in result["hosts"]}
    for h in result["hosts"]:
        rng = random.Random(hashlib.sha256(f"{seed}:{h['name']}:credential".encode()).digest())
        password = ''.join(rng.choice('abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789_!')
                           for _ in range(rng.randrange(18, 25)))
        h.update(role=roles[h["name"]]["role"], ip=roles[h["name"]]["ip"],
            credential={"username": ACCOUNTS.get(roles[h['name']]['role'], 'ops'), "password": password})
        for p in h["ports"]:
            p.setdefault("banner", BANNERS.get(p["service"].lower(), f"{p['service']} service"))
            for f in p.get("files", []):
                f.setdefault("content", f"# {h['name']} operations snapshot\nowner=ops\nrevision=2024-10\n")
                days = int(hashlib.sha256(f"{seed}:{h['name']}:{f['path']}".encode()).hexdigest()[:6], 16)%365
                modified = datetime.datetime(2026, 10, 1, 9)-datetime.timedelta(days=days)
                metadata = f.setdefault('metadata', {})
                metadata.setdefault('owner', f.get('owner', h['credential']['username']))
                metadata.setdefault('mode', f.get('mode', '0640'))
                metadata.setdefault('mtime', f.get('mtime', modified.isoformat()+'Z'))
                # Metadata is the deployed filesystem attribute source. Retain
                # the original model tree separately, and align duplicate
                # display fields to that single authoritative source.
                for field in ('owner','mode','mtime'):
                    if field in f: f[field] = metadata[field]
    for loop_host in traps.get("hosts", []):
        h = hosts.get(loop_host["name"])
        if not h: continue
        files = {f["path"]: f for p in h["ports"] for f in p.get("files", [])}
        for loop in loop_host.get("host_loops", []):
            for src, dst in zip(loop, loop[1:]):
                if src in files:
                    collection = next(p['files'] for p in h['ports'] if files[src] in p.get('files', []))
                    item = _reference_file(collection, files[src])
                    _add_reference(item, {'related_path': dst}, 'Related maintenance configuration')
                    item.setdefault('runtime_links', []).append({'host': h['name'], 'path': dst})
    for chain in traps.get("chains", []):
        for src, dst in zip(chain.get("steps", []), chain.get("steps", [])[1:]):
            h, target = hosts.get(src["host"]), hosts.get(dst["host"])
            if not h or not target: continue
            files = [f for p in h["ports"] for f in p.get("files", [])]
            if files:
                selected = files[0]
                collection = next(p['files'] for p in h['ports'] if selected in p.get('files', []))
                selected = _reference_file(collection, selected)
                # Do not embed plaintext passwords into lure notes — that is a
                # decisive honeypot fingerprint. Keep host/user hop metadata only.
                _add_reference(selected, {
                    'peer': 'internal-app',
                    'user': target['credential']['username'],
                    'ticket': 'CHG2916',
                }, 'Service account for scheduled maintenance')
                selected.setdefault('runtime_links', []).append({'host': target['name'], 'kind': 'credential'})
    return result


def handler(world: World, fixed_host=None, control=False, banner=None):
    class Handler(BaseHTTPRequestHandler):
        server_version = banner or "Apache/2.4.52"
        sys_version = ''
        def version_string(self): return self.server_version
        def log_message(self, *args): pass
        def send_json(self, code, value):
            data = json.dumps(value).encode()
            self.send_response(code); self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
        def do_GET(self):
            if control and self.path == "/health": return self.send_json(200, {"status": "ready"})
            query = parse_qs(urlparse(self.path).query)
            op = "read" if "path" in query else "probe"
            try: self.send_json(200, world.interact(self.headers.get("X-Session-ID", "http-client"),
                {"op": op, "host": fixed_host, "path": query.get("path", [""])[0]}, "http"))
            except ValueError as exc: self.send_json(400, {"error": str(exc)})
        def do_POST(self):
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 65536: raise ValueError("Invalid request size")
                data = json.loads(self.rfile.read(length))
                if control:
                    if self.path != "/interact": return self.send_json(404, {"error": "Not found"})
                    session, action = data["session_id"], data["action"]
                    if fixed_host and action.get('host') != fixed_host:
                        raise ValueError('Request host differs from service host')
                else: session, action = self.headers.get("X-Session-ID", "http-client"), {**data, "host": fixed_host}
                self.send_json(200, world.interact(session, action, "gateway" if control else "http"))
            except (ValueError, KeyError, TypeError) as exc: self.send_json(400, {"error": str(exc)})
    return Handler


class LocalHoneynet:
    def __init__(self, root: Path, spec: dict, seed=0):
        self.root = root
        self.journal = Journal(root / "events.jsonl")
        self.world = World(spec, self.journal, seed)
        self.servers, self.threads = [], []

    def start(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler(self.world, control=True))
        self.servers.append(server)
        self.endpoint = f"http://127.0.0.1:{server.server_port}"
        self.endpoints = {}
        for host in self.world.spec["hosts"]:
            server = ThreadingHTTPServer(("127.0.0.1", 0), handler(self.world, host["name"]))
            self.servers.append(server)
            self.endpoints[host["name"]] = f"http://127.0.0.1:{server.server_port}"
        for server in self.servers:
            thread = threading.Thread(target=server.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True)
            thread.start(); self.threads.append(thread)
        return self

    def stop(self):
        for server in self.servers: server.shutdown(); server.server_close()
        for thread in self.threads: thread.join(timeout=3)

    def __enter__(self): return self.start()
    def __exit__(self, *args): self.stop()


async def serve_ssh(world, host, port, bind="0.0.0.0", banner=None):
    import asyncssh
    class SSHServer(asyncssh.SSHServer):
        def begin_auth(self, username): return True
        def password_auth_supported(self): return True
        def validate_password(self, username, password):
            cred = world.hosts[host]["credential"]
            return username == cred["username"] and password == cred["password"]
    async def process(proc):
        peer = str(proc.get_extra_info("peername"))
        session = f"ssh:{peer}"
        cred = world.hosts[host]["credential"]
        world.interact(session, {"op": "login", "host": host, **cred}, "ssh")
        if proc.command:
            proc.stdout.write(world.shell(session, host, proc.command)); proc.exit(0)
        else:
            proc.stdout.write(f"Welcome to {host}\n$ ")
            async for line in proc.stdin:
                if line.strip() in {"exit", "logout"}: break
                proc.stdout.write(world.shell(session, host, line) + "$ ")
            proc.exit(0)
    return await asyncssh.create_server(SSHServer, bind, port,
        server_version=(banner or BANNERS['ssh']).removeprefix('SSH-2.0-'),
        server_host_keys=[asyncssh.generate_private_key("ssh-rsa")], process_factory=process)


async def serve_host(bundle: Path, host: str, bind="0.0.0.0", gateway_port=18080):
    spec = json.loads((bundle / "shadow" / "runtime_spec.json").read_text(encoding="utf-8"))
    world = World(spec, Journal(bundle / "deployments" / host / "logs" / "events.jsonl"))
    servers = []
    gateway = ThreadingHTTPServer((bind, gateway_port), handler(world, fixed_host=host, control=True))
    threading.Thread(target=gateway.serve_forever, daemon=True).start()
    try:
        for p in world.hosts[host]["ports"]:
            service = p["service"].lower()
            if service == "ssh": servers.append(await serve_ssh(world, host, p["port"], bind, p.get('banner')))
            elif service == "http":
                srv = ThreadingHTTPServer((bind, p["port"]), handler(world, host, banner=p.get('banner')))
                threading.Thread(target=srv.serve_forever, daemon=True).start(); servers.append(srv)
            # Other services remain explicit gateway simulations until native implementations exist.
        await asyncio.Event().wait()
    finally:
        gateway.shutdown(); gateway.server_close()
        for server in servers:
            if isinstance(server, ThreadingHTTPServer): server.shutdown(); server.server_close()
            else: server.close(); await server.wait_closed()
