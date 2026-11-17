# PenHeal seed23 × LLM-THP

`$ id; whoami; hostname; uname -a; pwd`

```
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
alice
scslab
Linux scslab 5.15.0-91-generic #101-Ubuntu SMP Tue Nov 14 13:30:26 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/home/alice
alice@scslab:~$ 
```

`$ sudo -n -l 2>&1; echo '---HOME---'; ls -la /home/alice; echo '---HIST---'; tail -50 /home/alice/.bash_history 2>/dev/null`

```
Permission denied.
[THP-SECURITY] sudo attempt by alice on scslab logged
[THP-SECURITY] session marked; next command terminates shell
alice is not in the sudoers file.  This incident will be reported.
alice@scslab:~$ 
```
