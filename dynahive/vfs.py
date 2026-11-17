"""First-class virtual filesystem for DynaHive World (route B).

Directories and files are real nodes with owner/mode/mtime/size. All of
ls / cat / stat / find / read share the same tree, so list-vs-read and
file-vs-directory contradictions cannot appear by construction.
"""
from __future__ import annotations

import fnmatch
import hashlib
import re
from dataclasses import dataclass, field
from pathlib import PurePosixPath
from typing import Dict, Iterable, List, Optional

from .anti_fingerprint import format_ls_mtime, format_mode, parse_mtime


LAB_CLOCK = '2024-10-13T09:15:01Z'


@dataclass
class VNode:
    path: str
    is_dir: bool
    owner: str = 'root'
    group: str = 'root'
    mode: str = '0644'
    mtime: str = '2024-03-01T09:00:00Z'
    content: str = ''
    size_override: Optional[int] = None
    target: Optional[str] = None  # symlink target
    children: Dict[str, 'VNode'] = field(default_factory=dict)

    @property
    def size(self) -> int:
        if self.is_dir:
            return 4096
        if self.target is not None:
            return len(self.target)
        if self.size_override is not None:
            return int(self.size_override)
        return len((self.content or '').encode())

    def mode_bits(self) -> str:
        if self.target is not None:
            return 'lrwxrwxrwx'
        return format_mode(self.mode, is_dir=self.is_dir)


class VirtualFS:
    """POSIX-like path tree rooted at '/'."""

    def __init__(self, host: str, username: str):
        self.host = host
        self.username = username
        self.root = VNode(path='/', is_dir=True, owner='root', group='root', mode='0755',
                          mtime='2024-01-15T08:00:00Z')

    def _clamp_mtime(self, value, key: str) -> str:
        stamp = parse_mtime(value)
        lab = parse_mtime(LAB_CLOCK)
        if stamp is not None and lab is not None and stamp < lab:
            if hasattr(stamp, 'isoformat'):
                return stamp.strftime('%Y-%m-%dT%H:%M:%SZ')
            return str(value)
        digest = hashlib.sha256(f'{self.host}|{key}|{value}'.encode()).hexdigest()
        month = 1 + (int(digest[0:2], 16) % 9)
        day = 1 + (int(digest[2:4], 16) % 27)
        hour = int(digest[4:6], 16) % 24
        minute = int(digest[6:8], 16) % 60
        return f'2024-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:00Z'

    def ensure_dir(self, path: str, owner='root', mode='0755', mtime=None) -> VNode:
        path = self._norm(path)
        if path == '/':
            return self.root
        node = self.root
        built = ''
        for part in PurePosixPath(path).parts[1:]:
            built = built + '/' + part
            if part not in node.children:
                node.children[part] = VNode(
                    path=built, is_dir=True, owner=owner, group=owner, mode=mode,
                    mtime=self._clamp_mtime(mtime, built),
                )
            child = node.children[part]
            if not child.is_dir:
                # Promote file→dir if children are required (conflict resolution).
                child.is_dir = True
                child.content = ''
                child.mode = mode
                child.owner = owner
                child.group = owner
            node = child
        return node

    def put_file(self, path: str, content: str, owner=None, mode='0640', mtime=None,
                 size=None, target=None) -> VNode:
        path = self._norm(path)
        parent_path = str(PurePosixPath(path).parent)
        name = PurePosixPath(path).name
        # Ownership from /home/<user>/...
        parts = PurePosixPath(path).parts
        if owner is None:
            if len(parts) >= 3 and parts[1] == 'home':
                owner = parts[2]
            else:
                owner = self.username
        parent = self.ensure_dir(parent_path, owner='root' if parent_path.startswith('/etc') else owner)
        # If a directory already exists at this path, keep it as dir (never demote).
        if name in parent.children and parent.children[name].is_dir:
            return parent.children[name]
        node = VNode(
            path=path, is_dir=False, owner=owner, group=owner, mode=mode,
            mtime=self._clamp_mtime(mtime, path), content=content or '',
            size_override=size, target=target,
        )
        parent.children[name] = node
        return node

    def get(self, path: str) -> Optional[VNode]:
        path = self._norm(path)
        if path == '/':
            return self.root
        node = self.root
        for part in PurePosixPath(path).parts[1:]:
            if part not in node.children:
                return None
            node = node.children[part]
        return node

    def exists(self, path: str) -> bool:
        return self.get(path) is not None

    def remove(self, path: str, recursive: bool = False) -> bool:
        path = self._norm(path)
        if path == '/':
            return False
        parent_path = str(PurePosixPath(path).parent)
        name = PurePosixPath(path).name
        parent = self.get(parent_path)
        if parent is None or name not in parent.children:
            return False
        node = parent.children[name]
        if node.is_dir and node.children and not recursive:
            return False
        del parent.children[name]
        return True

    def is_dir(self, path: str) -> bool:
        node = self.get(path)
        return bool(node and node.is_dir)

    def is_file(self, path: str) -> bool:
        node = self.get(path)
        return bool(node and not node.is_dir)

    def listdir(self, path: str) -> List[VNode]:
        node = self.get(path)
        if node is None or not node.is_dir:
            return []
        return [node.children[k] for k in sorted(node.children)]

    def read(self, path: str) -> Optional[str]:
        node = self.get(path)
        if node is None or node.is_dir:
            return None
        return node.content

    def walk_files(self, root: str = '/') -> Iterable[VNode]:
        node = self.get(root)
        if node is None:
            return []
        out = []

        def _walk(n: VNode):
            if n.is_dir:
                for child in n.children.values():
                    _walk(child)
            else:
                out.append(n)

        _walk(node)
        return out

    def format_ls(self, path: str, long_format=False, directory_only=False,
                  show_all=False, human=False) -> str:
        path = self._norm(path)
        # /proc/*/exe symlink presentation
        if re.match(r'^/proc/(self|\d+)/exe$', path):
            target = '/bin/bash' if not path.endswith('/1/exe') else '/sbin/init'
            when = format_ls_mtime('2024-03-01T09:00:00Z')
            name = 'exe'
            if long_format:
                return f'lrwxrwxrwx 1 root root {len(target)} {when} {name} -> {target}\n'
            return name + '\n'
        node = self.get(path)
        if node is None:
            return f'ls: cannot access {path}: No such file or directory\n'
        if directory_only or not node.is_dir:
            return self._format_entry(node, long_format=long_format,
                                      name=PurePosixPath(path).name or path, human=human)
        entries = self.listdir(path)
        visible = []
        for child in entries:
            name = PurePosixPath(child.path).name
            if not show_all and name.startswith('.'):
                continue
            visible.append(child)
        if not long_format:
            names = [PurePosixPath(c.path).name for c in visible]
            return self._columnize(names)
        lines = [f'total {max(4, len(visible) * 4)}']
        when = format_ls_mtime(node.mtime)
        size_dot = '4.0K' if human else '4096'
        lines.append(f'{node.mode_bits()} 1 {node.owner} {node.group} {size_dot} {when} .')
        parent = self.get(str(PurePosixPath(path).parent)) or node
        when_p = format_ls_mtime(parent.mtime)
        lines.append(f'{parent.mode_bits()} 1 {parent.owner} {parent.group} {size_dot} {when_p} ..')
        for child in visible:
            name = PurePosixPath(child.path).name
            lines.append(self._format_entry(child, long_format=True, name=name, human=human).rstrip('\n'))
        return ('\n'.join(lines) + '\n') if lines else '\n'

    @staticmethod
    def _columnize(names, width=80):
        if not names:
            return '\n'
        colw = max(len(n) for n in names) + 2
        cols = max(1, width // max(colw, 1))
        rows = (len(names) + cols - 1) // cols
        lines = []
        for r in range(rows):
            cells = []
            for c in range(cols):
                i = c * rows + r
                if i < len(names):
                    cells.append(names[i].ljust(colw))
            lines.append(''.join(cells).rstrip())
        return '\n'.join(lines) + '\n'

    def format_stat(self, path: str, fmt: Optional[str] = None) -> str:
        node = self.get(path)
        if node is None:
            return f"stat: cannot statx '{path}': No such file or directory\n"
        stamp = format_ls_mtime(node.mtime)
        # GNU %y-like
        mt = parse_mtime(node.mtime)
        y = mt.strftime('%Y-%m-%d %H:%M:%S.000000000 +0000') if mt else '2024-03-01 09:00:00.000000000 +0000'
        values = {
            '%n': path,
            '%F': 'directory' if node.is_dir else 'regular file',
            '%a': ''.join(ch for ch in str(node.mode) if ch.isdigit())[-3:] or ('755' if node.is_dir else '644'),
            '%A': node.mode_bits(),
            '%U': node.owner,
            '%G': node.group,
            '%s': str(node.size),
            '%y': y,
            '%i': str(10000 + (abs(hash(path)) % 50000)),
        }
        if fmt:
            out = fmt
            for key in sorted(values.keys(), key=len, reverse=True):
                out = out.replace(key, values[key])
            return out + '\n'
        return (
            f"  File: {values['%n']}\n"
            f"  Size: {values['%s']}\tBlocks: 8 IO Block: 4096 {values['%F']}\n"
            f"Access: ({values['%a']}/)  Uid: ({values['%U']})  Gid: ({values['%G']})\n"
            f"Modify: {values['%y']}\n"
        )

    def find(self, root: str, name=None, iname=None, user=None, type_filter=None, max_results=200,
             maxdepth=None, name_neg=False) -> List[str]:
        root = self._norm(root)
        node = self.get(root)
        if node is None:
            return []
        matches = []

        def _walk(n: VNode, depth: int):
            if len(matches) >= max_results:
                return
            if maxdepth is not None and depth > maxdepth:
                return
            base = PurePosixPath(n.path).name
            ok = True
            if name is not None:
                hit = fnmatch.fnmatch(base, name)
                if name_neg:
                    hit = not hit
                if not hit:
                    ok = False
            if iname is not None and not fnmatch.fnmatch(base.lower(), iname.lower()):
                ok = False
            if user is not None and n.owner != user:
                ok = False
            if type_filter == 'f' and n.is_dir:
                ok = False
            if type_filter == 'd' and not n.is_dir:
                ok = False
            if ok:
                matches.append(n.path)
            if n.is_dir and (maxdepth is None or depth < maxdepth):
                for child in n.children.values():
                    _walk(child, depth + 1)

        _walk(node, 0)
        return matches

    def _format_entry(self, node: VNode, long_format=False, name='.', human=False) -> str:
        if not long_format:
            return name + '\n'
        when = format_ls_mtime(node.mtime)
        shown = name
        if node.target:
            shown = f'{name} -> {node.target}'
        size = node.size
        if human:
            size = '4.0K' if node.is_dir or size >= 1024 else str(size)
        return f'{node.mode_bits()} 1 {node.owner} {node.group} {size} {when} {shown}\n'

    @staticmethod
    def _norm(path: str) -> str:
        if not path:
            return '/'
        p = PurePosixPath(path)
        text = str(p)
        if not text.startswith('/'):
            text = '/' + text
        return text if text != '//' else '/'


def seed_ubuntu_skeleton(vfs: VirtualFS, username: str, enterprise_lures: bool = True) -> None:
    """Install a minimal but consistent Ubuntu-like directory skeleton."""
    dirs = [
        '/', '/bin', '/sbin', '/usr', '/usr/bin', '/usr/sbin', '/etc', '/etc/ssh',
        '/etc/monit', '/etc/monit/conf.d', '/etc/cron.d', '/etc/cron.daily',
        '/etc/cron.weekly', '/etc/cron.monthly', '/etc/logrotate.d',
        '/home', f'/home/{username}', f'/home/{username}/.ssh',
        '/var', '/var/log', '/var/backups', '/var/tmp', '/var/run', '/tmp',
        '/opt', '/srv', '/proc', '/dev', '/dev/shm', '/dev/pts',
        '/sys', '/run', '/run/lock', '/boot', '/lib', '/lib64', '/root',
    ]
    for d in dirs:
        owner = username if d.startswith(f'/home/{username}') else 'root'
        vfs.ensure_dir(d, owner=owner, mode='0755')

    # Coreutils: store ELF-like size without allocating megabyte bodies.
    bins = {
        '/bin/bash': 1396520, '/bin/dash': 125686, '/bin/ls': 138208, '/bin/cat': 39232,
        '/usr/bin/head': 43936, '/usr/bin/tail': 43936, '/usr/bin/env': 35000,
        '/usr/bin/file': 66248, '/usr/bin/sed': 80472,
    }
    for path, size in bins.items():
        vfs.put_file(path, '\x7fELF', owner='root', mode='0755',
                     mtime='2024-02-01T08:00:00Z', size=size)
    vfs.put_file('/bin/sh', '', owner='root', mode='0777',
                 mtime='2024-02-01T08:00:00Z', target='dash')

    vfs.put_file('/etc/hostname', vfs.host + '\n', owner='root', mode='0644', mtime='2024-01-10T08:00:00Z')
    vfs.put_file(
        '/etc/os-release',
        'PRETTY_NAME="Ubuntu 22.04.4 LTS"\nNAME="Ubuntu"\nVERSION_ID="22.04"\n'
        'VERSION="22.04.4 LTS (Jammy Jellyfish)"\nID=ubuntu\nID_LIKE=debian\n'
        'HOME_URL="https://www.ubuntu.com/"\n',
        owner='root', mode='0644', mtime='2024-02-01T08:00:00Z',
    )
    vfs.put_file(
        '/etc/group',
        'root:x:0:\ndaemon:x:1:\nbin:x:2:\nsys:x:3:\nadm:x:4:\n'
        f'{username}:x:1000:\n'
        + ('admin:x:1001:\n' if username != 'admin' else ''),
        owner='root', mode='0644', mtime='2024-03-01T09:00:00Z',
    )
    vfs.ensure_dir('/etc/ssh', owner='root', mode='0755')
    vfs.put_file(
        '/etc/ssh/sshd_config',
        'Port 22\nProtocol 2\nPermitRootLogin no\nPasswordAuthentication yes\n'
        'ChallengeResponseAuthentication no\nUsePAM yes\nX11Forwarding yes\n'
        'PrintMotd no\nAcceptEnv LANG LC_*\nSubsystem sftp /usr/lib/openssh/sftp-server\n',
        owner='root', mode='0644', mtime='2024-02-12T09:00:00Z',
    )
    vfs.put_file(
        '/etc/crontab',
        'SHELL=/bin/sh\nPATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\n'
        '17 *\t* * *\troot    cd / && run-parts --report /etc/cron.hourly\n'
        '25 6\t* * *\troot\ttest -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )\n',
        owner='root', mode='0644', mtime='2024-02-01T08:00:00Z',
    )
    vfs.ensure_dir('/etc/ops', owner='root', mode='0755')
    if not enterprise_lures:
        vfs.put_file(f'/home/{username}/.bashrc',
                     '# ~/.bashrc: executed by bash(1) for non-login shells.\n'
                     '# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)\n'
                     '# for examples\n\n'
                     '# If not running interactively, don\'t do anything\n'
                     'case $- in\n'
                     '    *i*) ;;\n'
                     '      *) return;;\n'
                     'esac\n',
                     owner=username, mode='0644', mtime='2014-04-21T23:22:00Z')
        vfs.put_file(f'/home/{username}/.profile',
                     '# ~/.profile: executed by the command interpreter for login shells.\n'
                     '# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login\n'
                     '# exists.\n'
                     '# see /usr/share/doc/bash/examples/startup-files for examples.\n'
                     '# the files are located in the bash-doc package.\n\n'
                     '# the default umask is set in /etc/profile; for setting the umask\n'
                     '# for ssh logins, install and configure the libpam-umask package.\n'
                     '#umask 022\n\n'
                     '# if running bash\n'
                     'if [ -n "$BASH_VERSION" ]; then\n'
                     '    # include .bashrc if it exists\n'
                     '    if [ -f "$HOME/.bashrc" ]; then\n'
                     '	. "$HOME/.bashrc"\n'
                     '    fi\n'
                     'fi\n',
                     owner=username, mode='0644', mtime='2014-04-21T23:22:00Z')
        seed_jessie_lab_files(vfs, username)
        seed_halle_runtime_dirs(vfs, username)
        return
    # Layered lure chain (one hop per file) to induce multi-step exploration.
    vfs.put_file(
        f'/home/{username}/notes.txt',
        f'{vfs.host} shift notes\n'
        f'- next: read /etc/monit/monitrc\n'
        f'- do not batch; verify each path before following links\n',
        owner=username, mode='0644', mtime='2024-02-06T10:00:00Z',
    )
    vfs.put_file(
        '/etc/monit/monitrc',
        'set daemon 60\n'
        'set logfile /var/log/monit.log\n'
        'include /etc/monit/conf.d/*\n'
        '# ops follow-up: /etc/monit/conf.d/sshd\n',
        owner='root', mode='0644', mtime='2024-02-03T09:00:00Z',
    )
    vfs.put_file(
        '/etc/monit/conf.d/sshd',
        'check process sshd with pidfile /run/sshd.pid\n'
        '    start program = "/usr/sbin/service ssh start"\n'
        '    stop program  = "/usr/sbin/service ssh stop"\n'
        '# maintenance window file: /etc/ops/maintenance.conf\n',
        owner='root', mode='0644', mtime='2024-02-03T09:00:00Z',
    )
    vfs.put_file(
        '/etc/ops/maintenance.conf',
        f'# {vfs.host} maintenance window\n'
        'owner=firewall-oncall\n'
        'revision=2024-03-18\n'
        'ticket=CHG2916\n'
        'services=ssh,monit\n'
        'next_window=Sun 02:00-04:00 local\n'
        '# related ticket notes: /home/admin/.ssh/ticket-CHG2916.txt\n',
        owner='root', mode='0644', mtime='2024-03-18T02:00:00Z',
    )
    vfs.ensure_dir('/home/admin', owner='admin', mode='0755')
    vfs.ensure_dir('/home/admin/.ssh', owner='admin', mode='0700')
    vfs.put_file(
        '/home/admin/.ssh/authorized_keys',
        'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGthLWx0aWNrZXQtbm90ZS1wdWJrZXk admin@ops\n',
        owner='admin', mode='0600', mtime='2024-03-18T09:00:00Z',
    )
    vfs.put_file(
        '/home/admin/.ssh/ticket-CHG2916.txt',
        'CHG2916 follow-up\n'
        'window: Sun 02:00-04:00 local\n'
        'check: systemctl status ssh\n'
        'check: journalctl -u ssh -n 20\n'
        'next: cat /var/log/auth.log\n',
        owner='admin', mode='0644', mtime='2024-03-18T02:10:00Z',
    )
    for name in ('auth.log', 'syslog', 'kern.log'):
        vfs.put_file(f'/var/log/{name}', f'Jul 10 04:17:01 {vfs.host} systemd[1]: started\n',
                     owner='root', mode='0640', mtime='2024-07-10T04:17:01Z')
    vfs.put_file(f'/home/{username}/.bashrc',
                 '# ~/.bashrc: executed by bash(1) for non-login shells.\n',
                 owner=username, mode='0644', mtime='2024-05-08T10:35:00Z')
    vfs.put_file(f'/home/{username}/.profile',
                 '# ~/.profile\n# set PATH so it includes user private bins\n',
                 owner=username, mode='0644', mtime='2024-04-21T23:22:00Z')
    vfs.put_file(
        f'/home/{username}/.bash_history',
        'ls\nid\ncat notes.txt\nsystemctl status monit\n'
        'journalctl -u ssh -n 20\ncat /etc/ops/maintenance.conf\n'
        'cat /home/admin/.ssh/ticket-CHG2916.txt\n',
        owner=username, mode='0600', mtime='2024-09-12T18:40:00Z',
    )
    # /proc/self and session bash pid stubs used by fingerprint probes.
    vfs.ensure_dir('/proc/self', owner='root', mode='0555')
    vfs.ensure_dir('/proc/2145', owner=username, mode='0555')
    for pid in ('self', '2145', '1'):
        base = f'/proc/{pid}'
        vfs.ensure_dir(base, owner='root', mode='0555')
        vfs.put_file(f'{base}/cmdline', '-bash\0' if pid != '1' else '/sbin/init\0',
                     owner='root', mode='0444')
        vfs.put_file(f'{base}/comm', 'bash\n' if pid != '1' else 'systemd\n',
                     owner='root', mode='0444')
        # Represent exe as a tiny symlink-like file content for cat; ls uses mode.
        exe = vfs.put_file(f'{base}/exe', '', owner='root', mode='0777')
        exe.mode = '0777'  # shown specially by format_ls if needed


def seed_halle_runtime_dirs(vfs: VirtualFS, username: str) -> None:
    """Writable runtime dirs used by Halle attacker one-liners."""
    home = '/root' if username == 'root' else f'/home/{username}'
    for d in (
        '/var/tmp', '/var/run', '/dev/shm', '/run', '/sys', '/proc',
        '/dev/pts', '/tmp', f'{home}/.ssh',
    ):
        owner = username if d.startswith(home) else 'root'
        vfs.ensure_dir(d, owner=owner, mode='0755')


def seed_jessie_lab_files(vfs: VirtualFS, username: str) -> None:
    """Debian Jessie vagrant lab tree used by Weber NL2Bash/Prague commands."""
    home = f'/home/{username}'
    for d in (
        f'{home}/a', f'{home}/destdir', f'{home}/dir1', f'{home}/directory2',
        f'{home}/directory3', f'{home}/dirname', f'{home}/folder1', f'{home}/inode',
        f'{home}/inode/directory', f'{home}/newdir', f'{home}/files_and_folders',
        f'{home}/Desktop', f'{home}/Documents', f'{home}/Downloads', f'{home}/Music',
        f'{home}/Pictures', f'{home}/Public', f'{home}/Templates', f'{home}/Videos',
        f'{home}/tmp', f'{home}/some', f'{home}/subdirectory',
        f'{home}/empty',
        '/var/log', '/var/log/apt', '/cpuset',
        '/etc/acpi', '/etc/profile.d', '/etc/network', '/etc/apt',
        '/etc/default', '/etc/init.d', '/etc/insserv.conf.d',
    ):
        owner = username if d.startswith(home) else 'root'
        vfs.ensure_dir(d, owner=owner, mode='0755')
    files = {
        f'{home}/alpha_real': '',
        f'{home}/application': '',
        f'{home}/backup': '',
        f'{home}/bar': '',
        f'{home}/d': '',
        f'{home}/e': '',
        f'{home}/file1': 'x\n',
        f'{home}/filesOfInterest.txt': 'interest\n',
        f'{home}/output.txt': 'out\n',
        f'{home}/log.txt': 'log\n',
        f'{home}/found.lst': 'found\n',
        f'{home}/myfile.sh': '#!/bin/sh\n',
        f'{home}/path2': '',
        f'{home}/play': '',
        f'{home}/practice': '',
        f'{home}/text': 'y\ny\ny\n',
        f'{home}/x': '',
        f'{home}/.bash_history': 'ls\nfind .\ncat text.txt\n',
        f'{home}/index.html': '<html></html>\n',
        f'{home}/index.html.1': '<html></html>\n',
        f'{home}/index.html.2': '<html></html>\n',
        f'{home}/index.html.3': '<html></html>\n',
        f'{home}/index.html.4': '<html></html>\n',
        f'{home}/test.txt': 'test\n',
        f'{home}/test2.txt': 'test2\n',
        f'{home}/test.list': 'a\n',
        f'{home}/new_file.txt': 'new\n',
        f'{home}/yes.txt': 'y\n',
        f'{home}/file': 'file\n',
        f'{home}/file.json': '{}\n',
        f'{home}/wget-log': '\n',
        f'{home}/wget-log.3': '\n',
        f'{home}/compressedP.list': 'p\n',
        '/tmp/checkold.txt': '',
        '/tmp/a': '',
        '/tmp/BACKUP.LOG': '',
        '/etc/motd': 'Debian GNU/Linux 8\n',
        '/etc/adduser.conf': '# /etc/adduser.conf\n',
        '/etc/insserv.conf': '$local_fs\n',
        '/etc/protocols': 'ip\t0\tIP\n',
        '/etc/adjtime': '0.0 0 0.0\n0\nUTC\n',
        '/etc/hosts': '127.0.0.1 localhost\n',
        '/etc/os-release': (
            'PRETTY_NAME="Debian GNU/Linux 8 (jessie)"\n'
            'NAME="Debian GNU/Linux"\nVERSION_ID="8"\nVERSION="8 (jessie)"\n'
            'ID=debian\nHOME_URL="http://www.debian.org/"\n'
        ),
        '/etc/debian_version': '8.7\n',
        '/proc/version': (
            'Linux version 3.16.0-4-amd64 (debian-kernel@lists.debian.org) '
            '(gcc version 4.8.4 (Debian 4.8.4-1) ) '
            '#1 SMP Debian 3.16.39-1 (2016-12-30)\n'
        ),
        '/var/log/faillog': '',
        '/var/log/debug': '',
        '/var/log/messages': '',
        '/var/log/apt/history.log': '',
        '/var/log/syslog': 'Feb 21 16:41:01 jessie systemd[1]: Started Session.\n',
        '/usr/lib/ssl/misc/CA.sh': '#!/bin/sh\n# OpenSSL CA helper\n',
        '/usr/share/file': '',
        '/tmp/foo.txt': 'foo\n',
        '/var/run/acpid.pid': '1\n',
        '/var/run/sshd.pid': '512\n',
        '/var/run/utmp': '',
        '/var/run/initctl': '',
        '/proc/1/cmdline': '/sbin/init\n',
        '/proc/1/status': 'Name:\tinit\n',
    }
    for path, body in files.items():
        owner = username if path.startswith(home) else 'root'
        mode = '0644'
        if path.endswith('/index.html'):
            owner, mode = 'root', '0600'
        if path == '/var/log/syslog':
            owner, mode = 'root', '0640'
        vfs.put_file(path, body, owner=owner, mode=mode, mtime='2024-02-06T15:00:00Z')
    vfs.ensure_dir('/proc/1', owner='root', mode='0555')
    vfs.ensure_dir('/var/run', owner='root', mode='0755')
