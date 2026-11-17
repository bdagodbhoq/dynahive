# PenHeal seed13 × HoneyGPT

`$ id; whoami; hostname; pwd; ls -la; ls -la /home 2>/dev/null`

```
root@ubuntu:~# id; whoami; hostname; pwd; ls -la; ls -la /home 2>/dev/null
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
/root
total 36
drwx------  5 root root 4096 Oct 17 15:20 .
drwxr-xr-x 20 root root 4096 Oct 17 15:18 ..
-rw-------  1 root root  232 Oct 17 15:19 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 15:18 .cache
drwx------  3 root root 4096 Oct 17 15:18 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 15:18 .ssh
-rw-r--r--  1 root root  183 Oct 17 15:20 .wget-hsts
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 15:18 .
drwxr-xr-x 20 root   root   4096 Oct 17 15:18 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 15:18 ubuntu
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root /home/ubuntu /opt /srv /var/backups 2>/dev/null; echo ---; find / -xdev \( -iname '*opr*' -o -iname '*operational*' -o -iname '*ops_*' -o -iname '*evidence*' \) 2>/dev/null | head -50`

```
root@ubuntu:~# ls -la /root /home/ubuntu /opt /srv /var/backups 2>/dev/null; echo ---; find / -xdev \( -iname '*opr*' -o -iname '*operational*' -o -iname '*ops_*' -o -iname '*evidence*' \) 2>/dev/null | head -50
/home/ubuntu:
total 32
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 15:18 .
drwxr-xr-x 3 root   root   4096 Oct 17 15:18 ..
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  4  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Oct 17 15:18 .cache
drwx------ 3 ubuntu ubuntu 4096 Oct 17 15:18 .config
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  4  2018 .profile
-rw-r--r-- 1 ubuntu ubuntu    0 Oct 17 15:18 .sudo_as_admin_successful

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 15:18 .
drwxr-xr-x 20 root root 4096 Oct 17 15:18 ..

/root:
total 36
drwx------  5 root root 4096 Oct 17 15:20 .
drwxr-xr-x 20 root root 4096 Oct 17 15:18 ..
-rw-------  1 root root  232 Oct 17 15:19 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 15:18 .cache
drwx------  3 root root 4096 Oct 17 15:18 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 15:18 .ssh
-rw-r--r--  1 root root  183 Oct 17 15:20 .wget-hsts

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 15:18 .
drwxr-xr-x 20 root root 4096 Oct 17 15:18 ..

/var/backups:
total 20
drwxr-xr-x  2 root root 4096 Oct 17 15:18 .
drwxr-xr-x 14 root root 4096 Oct 17 15:18 ..
-rw-r--r--  1 root root  512 Oct 17 15:18 apt.extended_states.0
-rw-r--r--  1 root root  463 Oct 17 15:18 dpkg.status.0
---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ tail -n 50 /root/.bash_history 2>/dev/null; echo ===MOUNTS===; mount | grep -Ev 'proc|sys|cgroup|dev|tmpfs'; echo ===LISTEN===; ss -tlnp 2>/dev/null`

```
root@ubuntu:~# tail -n 50 /root/.bash_history 2>/dev/null; echo ===MOUNTS===; mount | grep -Ev 'proc|sys|cgroup|dev|tmpfs'; echo ===LISTEN===; ss -tlnp 2>/dev/null
ls -la /root /home/ubuntu /opt /srv /var/backups 2>/dev/null; echo ---; find / -xdev \( -iname '*opr*' -o -iname '*operational*' -o -iname '*ops_*' -o -iname '*evidence*' \) 2>/dev/null | head -50
id; whoami; hostname; pwd; ls -la; ls -la /home 2>/dev/null
===MOUNTS===
===LISTEN===
State     Recv-Q Send-Q Local Address:Port Peer Address:Port Process
LISTEN    0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=742,fd=3))
LISTEN    0      128             [::]:22           [::]:*     users:(("sshd",pid=742,fd=4))
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ grep -RIlE 'opr_evidence|ora_dump|OPS-[0-9]+|OPR-[0-9]+|operational[_ -]?record' /etc /var /root /home /opt /srv 2>/dev/null | head -50`

```
root@ubuntu:~# grep -RIlE 'opr_evidence|ora_dump|OPS-[0-9]+|OPR-[0-9]+|operational[_ -]?record' /etc /var /root /home /opt /srv 2>/dev/null | head -50
root@ubuntu:~# 
```
root@ubuntu:~# 
```
