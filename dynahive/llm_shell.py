"""LLM-primary shell with structured world-state and consistency gate (route C).

Almost all interactive commands are answered by the defender LLM, but every
turn is conditioned on a compact, authoritative WorldState snapshot. A local
ConsistencyGate rejects impossible outputs; on rejection we regenerate once,
then fall back to the World artifact executor.
"""
from __future__ import annotations

import re
from pathlib import PurePosixPath

from .honeypot import filesystem_metadata

BUILTINS = {
    'echo', 'printf', 'pwd', 'cd', 'test', '[', 'true', 'false', 'type',
    'command', 'export', 'set', 'unset', 'history', 'alias', 'ulimit', 'umask',
    'read', 'wait', 'times', 'getopts', 'source', '.', 'builtin', ':',
}

LEAK_RE = re.compile(r'(honeypot|decoy|trap|simulated|reconstructed|\blab\b|fake)', re.I)


def build_world_state(world, host, session_id, recent=None, max_files=48, max_content=400):
    """Authoritative snapshot the LLM must obey."""
    state = world._session_state(session_id, host)
    user = world.hosts[host]['credential']['username']
    files = world._host_files(host)
    entries = []
    dirs = set()
    for path, item in sorted(files.items())[:max_files]:
        meta = filesystem_metadata(item)
        content = item.get('content') or ''
        owner = meta.get('owner') or user
        parts = PurePosixPath(path).parts
        if len(parts) >= 3 and parts[1] == 'home':
            owner = parts[2]
        parent = str(PurePosixPath(path).parent)
        dirs.add(parent)
        entries.append({
            'path': path,
            'kind': 'file',
            'owner': owner,
            'mode': meta.get('mode', '0640'),
            'size': len(content.encode()),
            'mtime': meta.get('mtime'),
            'content_preview': content[:max_content],
        })
    # Virtual dirs that World serves.
    virtual_dirs = [
        '/', '/home', f'/home/{user}', '/etc', '/etc/monit', '/etc/monit/conf.d',
        '/var', '/var/log', '/proc', '/bin', '/usr/bin', '/tmp',
    ]
    for d in virtual_dirs:
        dirs.add(d)
    # Passwd humans for identity consistency.
    passwd = world._system_file(host, '/etc/passwd') or ''
    human = [ln for ln in passwd.splitlines() if re.search(r':x:10\d\d:', ln)]
    env = {
        k: v for k, v in (state.get('env') or {}).items()
        if k not in {'0', '$', '?', '_'}
    }
    return {
        'host': host,
        'username': user,
        'uid': 1000,
        'gid': 1000,
        'cwd': state.get('cwd') or f'/home/{user}',
        'os': world.hosts[host].get('os') or 'Ubuntu 22.04.4 LTS',
        'kernel': world.hosts[host].get('kernel') or 'Linux 5.15.0-97-generic #107-Ubuntu SMP x86_64 GNU/Linux',
        'lab_clock_utc': 'Sun Oct 13 09:15:01 UTC 2024',
        'env': env,
        'passwd_humans': human[:12],
        'directories': sorted(dirs)[:80],
        'files': entries,
        'facts': [
            f'Login user {user} is uid/gid 1000.',
            'Directories exist as directories: never list them as regular files.',
            '/etc/monit/conf.d is a directory containing sshd config file.',
            'Coreutils (ls,cat,head,tail,echo) exist; never print command not found for them.',
            'OpenSSH private keys begin with magic openssh-key-v1 inside base64 body.',
            'Do not invent plaintext passwords in notes; secrets live in vault refs only.',
        ],
        'recent': list(recent or [])[-6:],
    }


class ConsistencyGate:
    """Reject LLM outputs that contradict WorldState or bash reality."""

    def check(self, command, output, world_state):
        text = output or ''
        low = text.lower()
        reasons = []
        cmd = (command or '').strip()
        token = cmd.split(maxsplit=1)[0] if cmd.split() else ''
        if '/' in token:
            token = token.rsplit('/', 1)[-1]

        if LEAK_RE.search(text):
            reasons.append('self_disclosure')
        if re.search(r'(?:^|\n)(?:0|\$)=', text):
            reasons.append('leaked_shell_specials')

        # Builtins / coreutils must never be "command not found".
        for name in BUILTINS | {'ls', 'cat', 'head', 'tail', 'id', 'uname', 'hostname',
                                'grep', 'find', 'ps', 'env', 'stat', 'ss', 'ip'}:
            if f'bash: {name}: command not found' in low:
                reasons.append(f'missing_coreutil:{name}')

        files = {f['path']: f for f in (world_state or {}).get('files') or []}
        dirs = set((world_state or {}).get('directories') or [])

        # cat/ls of known paths.
        m = re.match(r'^(?:/bin/|/usr/bin/)?cat\s+(\S+)', cmd)
        if m:
            path = m.group(1)
            if path.startswith('~/'):
                path = f"/home/{world_state.get('username')}/{path[2:]}"
            if path in files and ('no such file' in low or 'is a directory' in low and files[path]['kind'] == 'file'):
                reasons.append(f'cat_contradicts_existing_file:{path}')
            if path in dirs and 'no such file' in low:
                reasons.append(f'cat_dir_missing:{path}')
            if path in dirs and 'no such file' not in low and 'is a directory' not in low and text.strip():
                # Reading a directory without Is a directory is suspicious if body looks like file content.
                if not text.strip().startswith('cat:'):
                    reasons.append(f'cat_dir_without_is_a_directory:{path}')

        m = re.match(r'^(?:/bin/|/usr/bin/)?ls(?:\s+\S+)*\s+(\S+)\s*$', cmd)
        if not m and cmd.strip() in {'ls', 'ls -la', 'ls -l', 'ls -al'}:
            path = world_state.get('cwd')
        elif m:
            path = m.group(1)
        else:
            path = None
        if path:
            if path.startswith('~/'):
                path = f"/home/{world_state.get('username')}/{path[2:]}"
            if path in dirs and 'no such file' in low:
                reasons.append(f'ls_missing_known_dir:{path}')
            # conf.d listed as regular file is a classic tell.
            if path.rstrip('/') == '/etc/monit' and re.search(r'-rw.+\s+conf\.d\b', text) and 'drwx' not in text.split('conf.d')[0][-20:]:
                # Heuristic: line for conf.d should start with d
                for line in text.splitlines():
                    if line.strip().endswith('conf.d') and line.startswith('-'):
                        reasons.append('monit_conf_d_listed_as_file')

        if 'head: missing file operand' in low and '|' in cmd:
            # Often means pipeline stdin was dropped.
            reasons.append('head_missing_operand_on_pipeline')

        return {'ok': not reasons, 'reasons': reasons}


class LLMPrimaryShell:
    """Complete one command via LLM with world-state + gate + World fallback."""

    def __init__(self, client, world, journal=None, ar_constraints=None):
        self.client = client
        self.world = world
        self.journal = journal
        self.ar_constraints = list(ar_constraints or [])
        self.gate = ConsistencyGate()

    def set_constraints(self, constraints):
        self.ar_constraints = [str(x) for x in (constraints or []) if str(x).strip()][:12]

    def complete(self, session_id, host, command, recent=None, style_hints=None):
        world_state = build_world_state(self.world, host, session_id, recent=recent)
        hints = list(style_hints or []) + list(self.ar_constraints)
        os_name = world_state.get('os') or 'Ubuntu 22.04.4 LTS'
        kernel = world_state.get('kernel') or 'Linux 5.15.0-97-generic'
        user = world_state.get('username') or 'user'
        host_name = world_state.get('host') or 'localhost'
        system = (
            f'You are GNU bash on a real {os_name} host named {host_name} '
            f'(login user {user}; kernel {kernel}). '
            'Return ONLY raw terminal stdout/stderr for ONE command line. No markdown. '
            'Never say honeypot/decoy/trap/simulated/lab/fake. '
            'OBEY world_state exactly: file existence, directory vs file, sizes, owners, '
            'uid/gid, env, hostname, os, kernel, and facts. '
            'If a path is listed under directories, ls must show it as a directory (drwx...). '
            'If a path is listed under files, cat must return its content_preview (or a '
            'faithful continuation), never No such file. '
            'Never print command not found for bash builtins or coreutils in PATH. '
            'Pipelines must consume stdin (cat file | head must not say missing file operand). '
            'Keep outputs boring and internally consistent across recent turns. '
            'Match the declared OS/kernel/user; do not invent Ubuntu 22.04 if the host is Debian.'
        )
        payload = {
            'command': command,
            'world_state': world_state,
            'style_hints': hints[:16],
        }
        text = self._call(system, payload)
        check = self.gate.check(command, text, world_state)
        if check['ok']:
            return {'output': text, 'source': 'llm_primary', 'gate': check, 'retried': False}

        if self.journal:
            self.journal.append({
                'event': 'llm_shell_gate_reject',
                'command': command,
                'reasons': check['reasons'],
                'output_preview': text[:300],
            })
        # One constrained regenerate.
        retry_payload = {
            **payload,
            'previous_bad_output': text[:800],
            'violations': check['reasons'],
            'instruction': 'Regenerate a corrected shell output that fixes every violation.',
        }
        text2 = self._call(system, retry_payload)
        check2 = self.gate.check(command, text2, world_state)
        if check2['ok']:
            return {'output': text2, 'source': 'llm_primary_retry', 'gate': check2, 'retried': True}

        # Fall back to World artifact executor.
        result = self.world.execute_command(session_id, host, command)
        if result.get('handled'):
            out = result.get('output') or ''
            return {
                'output': out,
                'source': 'world_fallback',
                'gate': check2,
                'retried': True,
                'trap_trigger': bool(result.get('trap_trigger')),
            }
        token = command.split()[0] if command.split() else 'command'
        if '/' in token:
            token = token.rsplit('/', 1)[-1]
        return {
            'output': f'bash: {token}: command not found\n',
            'source': 'world_unhandled',
            'gate': check2,
            'retried': True,
        }

    def _call(self, system, payload):
        try:
            text = self.client.complete(system, payload, task='dynahive.llm_primary.shell',
                                        json_output=False)
        except Exception as exc:
            if self.journal:
                self.journal.append({
                    'event': 'llm_primary_error',
                    'error': type(exc).__name__ + ': ' + str(exc)[:200],
                })
            return 'bash: command not found\n'
        if not isinstance(text, str):
            text = str(text)
        text = text.strip('\r\n') + '\n'
        if LEAK_RE.search(text):
            return 'bash: permission denied\n'
        if len(text) > 16000:
            text = text[:16000] + '\n'
        return text
