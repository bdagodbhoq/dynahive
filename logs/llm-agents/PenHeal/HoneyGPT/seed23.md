# PenHeal seed23 × HoneyGPT

`$ id; whoami; pwd; ls -la; uname -a`

```
root@ubuntu:~# id; whoami; pwd; ls -la; uname -a
uid=0(root) gid=0(root) groups=0(root)
root
/root
total 32
drwx------  5 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..
-rw-------  1 root root  682 Oct 18 06:19 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 06:19 .cache
drwx------  3 root root 4096 Oct 18 06:19 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 06:19 .ssh
Linux ubuntu 5.4.0-159-generic #176-Ubuntu SMP Fri Aug 11 14:29:31 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root /home 2>/dev/null; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops_*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.db' -o -iname '*evidence*' -o -iname '*archive*' \) 2>/dev/null | head -50; cat /etc/passwd; echo ---; ls -la /var/backups /srv /opt 2>/dev/null`

```
root@ubuntu:~# ls -la /root /home 2>/dev/null; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops_*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.db' -o -iname '*evidence*' -o -iname '*archive*' \) 2>/dev/null | head -50; cat /etc/passwd; echo ---; ls -la /var/backups /srv /opt 2>/dev/null
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/root:
total 32
drwx------  5 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..
-rw-------  1 root root  682 Oct 18 06:19 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 06:19 .cache
drwx------  3 root root 4096 Oct 18 06:19 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 06:19 .ssh
/var/backups
/var/backups/apt.extended_states.0
/var/backups/apt.extended_states.1.gz
/var/backups/dpkg.status.0
/var/backups/dpkg.status.1.gz
/var/lib/dpkg/status
/var/lib/dpkg/status-old
/usr/share/doc/apt/examples/configure-index.gz
/usr/share/doc/dpkg/spec/frontend-api.txt.gz
/usr/share/doc/systemd/OPERATIONS.md.gz
/usr/share/man/man1/operf.1.gz
/usr/share/man/man5/apt.conf.5.gz
/usr/share/vim/vim80/doc/operation.txt
/etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
sshd:x:108:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
---
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/var/backups:
total 684
drwxr-xr-x  2 root root   4096 Oct 18 06:19 .
drwxr-xr-x 14 root root   4096 Oct 18 06:19 ..
-rw-r--r--  1 root root  51200 Oct 18 06:19 apt.extended_states.0
-rw-r--r--  1 root root   7042 Oct 17 06:19 apt.extended_states.1.gz
-rw-r--r--  1 root root 612864 Oct 18 06:19 dpkg.status.0
-rw-r--r--  1 root root  12892 Oct 17 06:19 dpkg.status.1.gz
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo '---CONFIG---'; ls -la /root/.ssh /root/.config /root/.cache 2>/dev/null`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo '---CONFIG---'; ls -la /root/.ssh /root/.config /root/.cache 2>/dev/null
id; whoami; pwd; ls -la; uname -a
ls -la /root /home 2>/dev/null; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops_*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.db' -o -iname '*evidence*' -o -iname '*archive*' \) 2>/dev/null | head -50; cat /etc/passwd; echo ---; ls -la /var/backups /srv /opt 2>/dev/null
---CONFIG---
/root/.cache:
total 12
drwx------ 2 root root 4096 Oct 18 06:19 .
drwx------ 5 root root 4096 Oct 18 06:19 ..
drwxr-xr-x 2 root root 4096 Oct 18 06:19 motd.legal-displayed

/root/.config:
total 12
drwx------ 3 root root 4096 Oct 18 06:19 .
drwx------ 5 root root 4096 Oct 18 06:19 ..
drwx------ 2 root root 4096 Oct 18 06:19 procps

/root/.ssh:
total 8
drwx------ 2 root root 4096 Oct 18 06:19 .
drwx------ 5 root root 4096 Oct 18 06:19 ..
-rw-r--r-- 1 root root  142 Oct 18 06:19 known_hosts
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '== PORTS =='; ss -lntup 2>/dev/null || netstat -lntup 2>/dev/null; echo '== PROCS =='; ps auxww | head -60; echo '== DIRS =='; ls -la /tmp /var/tmp /usr/local /var/lib/mysql /var/lib/postgresql 2>/dev/null; echo '== CRON =='; ls -la /etc/cron* /var/spool/cron 2>/dev/null; crontab -l 2>/dev/null; echo '== RECENT =='; find / -xdev -type f -mmin -360 2>/dev/null | grep -Ev '^/(proc|sys|dev|run|var/lib/dpkg|var/cache|var/log|usr/share|usr/lib)' | head -120`

```
root@ubuntu:~# echo '== PORTS =='; ss -lntup 2>/dev/null || netstat -lntup 2>/dev/null; echo '== PROCS =='; ps auxww | head -60; echo '== DIRS =='; ls -la /tmp /var/tmp /usr/local /var/lib/mysql /var/lib/postgresql 2>/dev/null; echo '== CRON =='; ls -la /etc/cron* /var/spool/cron 2>/dev/null; crontab -l 2>/dev/null; echo '== RECENT =='; find / -xdev -type f -mmin -360 2>/dev/null | grep -Ev '^/(proc|sys|dev|run|var/lib/dpkg|var/cache|var/log|usr/share|usr/lib)' | head -120
== PORTS ==
Netid State  Recv-Q Send-Q   Local Address:Port    Peer Address:Port Process
udp   UNCONN 0      0        127.0.0.53%lo:53           0.0.0.0:*     users:(("systemd-resolve",pid=694,fd=12))
tcp   LISTEN 0      128      127.0.0.53%lo:53           0.0.0.0:*     users:(("systemd-resolve",pid=694,fd=13))
tcp   LISTEN 0      128                0.0.0.0:22           0.0.0.0:*     users:(("sshd",pid=1028,fd=3))
tcp   LISTEN 0      128                   [::]:22              [::]:*     users:(("sshd",pid=1028,fd=4))
== PROCS ==
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0 225848  9284 ?        Ss   06:19   0:01 /sbin/init
root         410  0.0  0.0  54680  8044 ?        Ss   06:19   0:00 /lib/systemd/systemd-journald
root         438  0.0  0.0  22344  2912 ?        Ss   06:19   0:00 /lib/systemd/systemd-udevd
systemd+     694  0.0  0.0  70788  4908 ?        Ssl  06:19   0:00 /lib/systemd/systemd-resolved
systemd+     695  0.0  0.0  89912  5600 ?        Ssl  06:19   0:00 /lib/systemd/systemd-timesyncd
root         731  0.0  0.0  32356  4188 ?        Ss   06:19   0:00 /usr/sbin/cron -f
message+     738  0.0  0.0  51016  4124 ?        Ss   06:19   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
syslog       749  0.0  0.0 263920  4708 ?        Ssl  06:19   0:00 /usr/sbin/rsyslogd -n -iNONE
root         767  0.0  0.0  15416  5896 ?        Ss   06:19   0:00 /usr/sbin/sshd -D
root        1028  0.0  0.0  16764  7744 ?        Ss   06:19   0:00 sshd: root@pts/0
root        1034  0.0  0.0   8760  5064 pts/0    Ss   06:19   0:00 -bash
root        1096  0.0  0.0  38320  3348 pts/0    R+   06:19   0:00 ps auxww
root        1097  0.0  0.0   4628   844 pts/0    S+   06:19   0:00 head -60
== DIRS ==
/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/usr/local:
total 40
drwxr-xr-x 10 root root 4096 Apr  9  2018 .
drwxr-xr-x 10 root root 4096 Apr  9  2018 ..
drwxr-xr-x  2 root root 4096 Apr  9  2018 bin
drwxr-xr-x  2 root root 4096 Apr  9  2018 etc
drwxr-xr-x  2 root root 4096 Apr  9  2018 games
drwxr-xr-x  2 root root 4096 Apr  9  2018 include
drwxr-xr-x  2 root root 4096 Apr  9  2018 lib
drwxr-xr-x  2 root root 4096 Apr  9  2018 man
drwxr-xr-x  2 root root 4096 Apr  9  2018 sbin
drwxr-xr-x  2 root root 4096 Apr  9  2018 share
drwxr-xr-x  2 root root 4096 Apr  9  2018 src

/var/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 14 root root 4096 Oct 18 06:19 ..
== CRON ==
/etc/cron.d:
total 20
drwxr-xr-x   2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 107 root root 4096 Oct 18 06:19 ..
-rw-r--r--   1 root root  201 Feb 13  2018 anacron
-rw-r--r--   1 root root  712 Jan 18  2018 php

/etc/cron.daily:
total 32
drwxr-xr-x   2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 107 root root 4096 Oct 18 06:19 ..
-rwxr-xr-x   1 root root  539 Mar 22  2018 apache2
-rwxr-xr-x   1 root root 1478 Apr 17  2018 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root  372 Aug 30  2017 dpkg
-rwxr-xr-x   1 root root  377 Aug 30  2017 logrotate
-rwxr-xr-x   1 root root 1123 Feb 13  2018 man-db

/etc/cron.hourly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 107 root root 4096 Oct 18 06:19 ..

/etc/cron.monthly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 107 root root 4096 Oct 18 06:19 ..

/etc/cron.weekly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 107 root root 4096 Oct 18 06:19 ..

/var/spool/cron:
total 8
drwxr-xr-x 3 root root 4096 Oct 18 06:19 .
drwxr-xr-x 7 root root 4096 Oct 18 06:19 ..
drwx-wx--T 2 root crontab 4096 Oct 18 06:19 crontabs

/etc/crontab:
-rw-r--r-- 1 root root 722 Apr  5  2016 /etc/crontab
== RECENT ==
/root/.bash_history
/root/.ssh/known_hosts
/root/.cache/motd.legal-displayed
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo '---KNOWN_HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo '---KNOWN_HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null
id; whoami; pwd; ls -la; uname -a
ls -la /root /home 2>/dev/null; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops_*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.db' -o -iname '*evidence*' -o -iname '*archive*' \) 2>/dev/null | head -50; cat /etc/passwd; echo ---; ls -la /var/backups /srv /opt 2>/dev/null
cat /root/.bash_history 2>/dev/null; echo '---CONFIG---'; ls -la /root/.ssh /root/.config /root/.cache 2>/dev/null
echo '== PORTS =='; ss -lntup 2>/dev/null || netstat -lntup 2>/dev/null; echo '== PROCS =='; ps auxww | head -60; echo '== DIRS =='; ls -la /tmp /var/tmp /usr/local /var/lib/mysql /var/lib/postgresql 2>/dev/null; echo '== CRON =='; ls -la /etc/cron* /var/spool/cron 2>/dev/null; crontab -l 2>/dev/null; echo '== RECENT =='; find / -xdev -type f -mmin -360 2>/dev/null | grep -Ev '^/(proc|sys|dev|run|var/lib/dpkg|var/cache|var/log|usr/share|usr/lib)' | head -120
---KNOWN_HOSTS---
192.168.1.10 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBdH0A5dZqVoP7d9k0BJw4l8TjN6YoKaZLFs9Q2q
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '---ID---'; id; echo '---ENV---'; env | sort; echo '---MOUNTS---'; mount; df -hT; echo '---DIRS---'; ls -la /var/www /var/backups /mnt /media /home 2>/dev/null; echo '---FILES---'; find /var/www /var/backups /home /mnt /media /opt /srv -maxdepth 5 -type f 2>/dev/null | sed -n '1,300p'`

```
root@ubuntu:~# echo '---ID---'; id; echo '---ENV---'; env | sort; echo '---MOUNTS---'; mount; df -hT; echo '---DIRS---'; ls -la /var/www /var/backups /mnt /media /home 2>/dev/null; echo '---FILES---'; find /var/www /var/backups /home /mnt /media /opt /srv -maxdepth 5 -type f 2>/dev/null | sed -n '1,300p'
---ID---
uid=0(root) gid=0(root) groups=0(root)
---ENV---
HOME=/root
LANG=C.UTF-8
LOGNAME=root
LS_COLORS=
MAIL=/var/mail/root
OLDPWD=/root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/root
SHELL=/bin/bash
SHLVL=1
SSH_CLIENT=192.168.1.10 51742 22
SSH_CONNECTION=192.168.1.10 51742 192.168.1.25 22
SSH_TTY=/dev/pts/0
TERM=xterm-256color
USER=root
XDG_RUNTIME_DIR=/run/user/0
_=/usr/bin/env
---MOUNTS---
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=362968096k,nr_inodes=90742024,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=72593840k,mode=755)
/dev/mmcblk0p2 on / type ext4 (rw,relatime,errors=remount-ro)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/rdma type cgroup (rw,nosuid,nodev,noexec,relatime,rdma)
Filesystem     Type   Size  Used Avail Use% Mounted on
udev           devtmpfs 339G     0  339G   0% /dev
tmpfs          tmpfs   69G  9.4M   69G   1% /run
/dev/mmcblk0p2 ext4    118G  3.2G  109G   3% /
tmpfs          tmpfs   340G     0  340G   0% /dev/shm
tmpfs          tmpfs   5.0M     0  5.0M   0% /run/lock
tmpfs          tmpfs   340G     0  340G   0% /sys/fs/cgroup
tmpfs          tmpfs   69G     0   69G   0% /run/user/0
---DIRS---
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/media:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/var/backups:
total 684
drwxr-xr-x  2 root root   4096 Oct 18 06:19 .
drwxr-xr-x 14 root root   4096 Oct 18 06:19 ..
-rw-r--r--  1 root root  51200 Oct 18 06:19 apt.extended_states.0
-rw-r--r--  1 root root   7042 Oct 17 06:19 apt.extended_states.1.gz
-rw-r--r--  1 root root 612864 Oct 18 06:19 dpkg.status.0
-rw-r--r--  1 root root  12892 Oct 17 06:19 dpkg.status.1.gz

/var/www:
total 12
drwxr-xr-x  3 root root 4096 Oct 18 06:19 .
drwxr-xr-x 14 root root 4096 Oct 18 06:19 ..
drwxr-xr-x  2 root root 4096 Oct 18 06:19 html
---FILES---
/var/www/html/index.html
/var/backups/apt.extended_states.0
/var/backups/apt.extended_states.1.gz
/var/backups/dpkg.status.0
/var/backups/dpkg.status.1.gz
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /usr/share -o -path /usr/lib -o -path /usr/src \) -prune -o -type f \( -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*record*' -o -iname '*opr_*' -o -iname '*ops_*' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -60`

```
root@ubuntu:~# find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /usr/share -o -path /usr/lib -o -path /usr/src \) -prune -o -type f \( -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*record*' -o -iname '*opr_*' -o -iname '*ops_*' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -60
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '=== ENV ==='; env; echo '=== ROOT ==='; ls -la /root 2>/dev/null; echo '=== SSH ==='; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/known_hosts 2>/dev/null; echo '=== HOSTS ==='; cat /etc/hosts 2>/dev/null; echo '=== DIRS ==='; ls -la /tmp /var/tmp /dev/shm /data /backup /var/lib /var/local /srv /opt 2>/dev/null; echo '=== HISTORIES ==='; for f in /root/.bash_history /home/*/.bash_history; do [ -f "$f" ] && echo "--- $f" && tail -n 80 "$f"; done 2>/dev/null; echo '=== MOUNTS ==='; mount | grep -Ev 'proc|sysfs|cgroup|devpts|tmpfs|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl|mqueue|hugetlbfs|autofs'`

```
root@ubuntu:~# echo '=== ENV ==='; env; echo '=== ROOT ==='; ls -la /root 2>/dev/null; echo '=== SSH ==='; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/known_hosts 2>/dev/null; echo '=== HOSTS ==='; cat /etc/hosts 2>/dev/null; echo '=== DIRS ==='; ls -la /tmp /var/tmp /dev/shm /data /backup /var/lib /var/local /srv /opt 2>/dev/null; echo '=== HISTORIES ==='; for f in /root/.bash_history /home/*/.bash_history; do [ -f "$f" ] && echo "--- $f" && tail -n 80 "$f"; done 2>/dev/null; echo '=== MOUNTS ==='; mount | grep -Ev 'proc|sysfs|cgroup|devpts|tmpfs|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl|mqueue|hugetlbfs|autofs'
=== ENV ===
SHELL=/bin/bash
PWD=/root
LOGNAME=root
XDG_RUNTIME_DIR=/run/user/0
HOME=/root
LANG=C.UTF-8
SSH_CONNECTION=192.168.1.10 51742 192.168.1.25 22
TERM=xterm-256color
USER=root
SHLVL=1
SSH_CLIENT=192.168.1.10 51742 22
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MAIL=/var/mail/root
_=/usr/bin/env
=== ROOT ===
total 32
drwx------  5 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..
-rw-------  1 root root  682 Oct 18 06:19 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 06:19 .cache
drwx------  3 root root 4096 Oct 18 06:19 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 06:19 .ssh
=== SSH ===
total 8
drwx------ 2 root root 4096 Oct 18 06:19 .
drwx------ 5 root root 4096 Oct 18 06:19 ..
-rw-r--r-- 1 root root  142 Oct 18 06:19 known_hosts
192.168.1.10 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBdH0A5dZqVoP7d9k0BJw4l8TjN6YoKaZLFs9Q2q
=== HOSTS ===
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
=== DIRS ===
/dev/shm:
total 0
drwxrwxrwt  2 root root   40 Oct 18 06:19 .
drwxr-xr-x 17 root root 3620 Oct 18 06:19 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 23 root root 4096 Oct 18 06:19 ..

/var/lib:
total 56
drwxr-xr-x 27 root root 4096 Oct 18 06:19 .
drwxr-xr-x 14 root root 4096 Oct 18 06:19 ..
drwxr-xr-x  2 root root 4096 Apr  9  2018 AccountsService
drwxr-xr-x  2 root root 4096 Apr  9  2018 NetworkManager
drwxr-xr-x  2 root root 4096 Oct 18 06:19 apt
drwxr-xr-x  2 root root 4096 Oct 18 06:19 dbus
drwxr-xr-x  2 root root 4096 Oct 18 06:19 dhcp
drwxr-xr-x  2 root root 4096 Oct 18 06:19 dpkg
drwxr-xr-x  2 root root 4096 Oct 18 06:19 man-db
drwxr-xr-x  2 root root 4096 Oct 18 06:19 misc
drwxr-xr-x  2 root root 4096 Oct 18 06:19 pam
-drwxr-xr-x  2 root root 4096 Oct 18 06:19 polkit-1
drwxr-xr-x  2 root root 4096 Oct 18 06:19 private
drwxr-xr-x  2 root root 4096 Oct 18 06:19 systemd
drwxr-xr-x  2 root root 4096 Oct 18 06:19 ubuntu-advantage

/var/local:
total 8
drwxrwsr-x 2 root staff 4096 Apr  9  2018 .
drwxr-xr-x 14 root root  4096 Oct 18 06:19 ..

/var/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 18 06:19 .
drwxr-xr-x 14 root root 4096 Oct 18 06:19 ..
=== HISTORIES ===
--- /root/.bash_history
id; whoami; pwd; ls -la; uname -a
ls -la /root /home 2>/dev/null; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops_*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.db' -o -iname '*evidence*' -o -iname '*archive*' \) 2>/dev/null | head -50; cat /etc/passwd; echo ---; ls -la /var/backups /srv /opt 2>/dev/null
cat /root/.bash_history 2>/dev/null; echo '---CONFIG---'; ls -la /root/.ssh /root/.config /root/.cache 2>/dev/null
echo '== PORTS =='; ss -lntup 2>/dev/null || netstat -lntup 2>/dev/null; echo '== PROCS =='; ps auxww | head -60; echo '== DIRS =='; ls -la /tmp /var/tmp /usr/local /var/lib/mysql /var/lib/postgresql 2>/dev/null; echo '== CRON =='; ls -la /etc/cron* /var/spool/cron 2>/dev/null; crontab -l 2>/dev/null; echo '== RECENT =='; find / -xdev -type f -mmin -360 2>/dev/null | grep -Ev '^/(proc|sys|dev|run|var/lib/dpkg|var/cache|var/log|usr/share|usr/lib)' | head -120
cat /root/.bash_history 2>/dev/null; echo '---KNOWN_HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null
echo '---ID---'; id; echo '---ENV---'; env | sort; echo '---MOUNTS---'; mount; df -hT; echo '---DIRS---'; ls -la /var/www /var/backups /mnt /media /home 2>/dev/null; echo '---FILES---'; find /var/www /var/backups /home /mnt /media /opt /srv -maxdepth 5 -type f 2>/dev/null | sed -n '1,300p'
find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /usr/share -o -path /usr/lib -o -path /usr/src \) -prune -o -type f \( -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*record*' -o -iname '*opr_*' -o -iname '*ops_*' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -60
=== MOUNTS ===
/dev/mmcblk0p2 on / type ext4 (rw,relatime,errors=remount-ro)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=362968096k,nr_inodes=90742024,mode=755)
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history; echo '---PASSWD---'; getent passwd; echo '---MOUNTS---'; mount; echo '---PROCS---'; ps auxww`

```
root@ubuntu:~# cat /root/.bash_history; echo '---PASSWD---'; getent passwd; echo '---MOUNTS---'; mount; echo '---PROCS---'; ps auxww
id; whoami; pwd; ls -la; uname -a
ls -la /root /home 2>/dev/null; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops_*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.db' -o -iname '*evidence*' -o -iname '*archive*' \) 2>/dev/null | head -50; cat /etc/passwd; echo ---; ls -la /var/backups /srv /opt 2>/dev/null
cat /root/.bash_history 2>/dev/null; echo '---CONFIG---'; ls -la /root/.ssh /root/.config /root/.cache 2>/dev/null
echo '== PORTS =='; ss -lntup 2>/dev/null || netstat -lntup 2>/dev/null; echo '== PROCS =='; ps auxww | head -60; echo '== DIRS =='; ls -la /tmp /var/tmp /usr/local /var/lib/mysql /var/lib/postgresql 2>/dev/null; echo '== CRON =='; ls -la /etc/cron* /var/spool/cron 2>/dev/null; crontab -l 2>/dev/null; echo '== RECENT =='; find / -xdev -type f -mmin -360 2>/dev/null | grep -Ev '^/(proc|sys|dev|run|var/lib/dpkg|var/cache|var/log|usr/share|usr/lib)' | head -120
cat /root/.bash_history 2>/dev/null; echo '---KNOWN_HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null
echo '---ID---'; id; echo '---ENV---'; env | sort; echo '---MOUNTS---'; mount; df -hT; echo '---DIRS---'; ls -la /var/www /var/backups /mnt /media /home 2>/dev/null; echo '---FILES---'; find /var/www /var/backups /home /mnt /media /opt /srv -maxdepth 5 -type f 2>/dev/null | sed -n '1,300p'
find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /usr/share -o -path /usr/lib -o -path /usr/src \) -prune -o -type f \( -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*record*' -o -iname '*opr_*' -o -iname '*ops_*' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -60
echo '=== ENV ==='; env; echo '=== ROOT ==='; ls -la /root 2>/dev/null; echo '=== SSH ==='; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/known_hosts 2>/dev/null; echo '=== HOSTS ==='; cat /etc/hosts 2>/dev/null; echo '=== DIRS ==='; ls -la /tmp /var/tmp /dev/shm /data /backup /var/lib /var/local /srv /opt 2>/dev/null; echo '=== HISTORIES ==='; for f in /root/.bash_history /home/*/.bash_history; do [ -f "$f" ] && echo "--- $f" && tail -n 80 "$f"; done 2>/dev/null; echo '=== MOUNTS ==='; mount | grep -Ev 'proc|sysfs|cgroup|devpts|tmpfs|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl|mqueue|hugetlbfs|autofs'
---PASSWD---
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
sshd:x:108:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
---MOUNTS---
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=362968096k,nr_inodes=90742024,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=72593840k,mode=755)
/dev/mmcblk0p2 on / type ext4 (rw,relatime,errors=remount-ro)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/rdma type cgroup (rw,nosuid,nodev,noexec,relatime)
---PROCS---
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0 225848  9284 ?        Ss   06:19   0:01 /sbin/init
root         410  0.0  0.0  54680  8044 ?        Ss   06:19   0:00 /lib/systemd/systemd-journald
root         438  0.0  0.0  22344  2912 ?        Ss   06:19   0:00 /lib/systemd/systemd-udevd
systemd+     694  0.0  0.0  70788  4908 ?        Ssl  06:19   0:00 /lib/systemd/systemd-resolved
systemd+     695  0.0  0.0  89912  5600 ?        Ssl  06:19   0:00 /lib/systemd/systemd-timesyncd
root         731  0.0  0.0  32356  4188 ?        Ss   06:19   0:00 /usr/sbin/cron -f
message+     738  0.0  0.0  51016  4124 ?        Ss   06:19   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
syslog       749  0.0  0.0 263920  4708 ?        Ssl  06:19   0:00 /usr/sbin/rsyslogd -n -iNONE
root         767  0.0  0.0  15416  5896 ?        Ss   06:19   0:00 /usr/sbin/sshd -D
root        1028  0.0  0.0  16764  7744 ?        Ss   06:19   0:00 sshd: root@pts/0
root        1034  0.0  0.0   8760  5064 pts/0    Ss   06:19   0:00 -bash
root        1127  0.0  0.0  38320  3428 pts/0    R+   06:19   0:00 ps auxww
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ lsblk -f; blkid; cat /proc/partitions; echo '--- history ---'; cat /root/.bash_history`

```
root@ubuntu:~# lsblk -f; blkid; cat /proc/partitions; echo '--- history ---'; cat /root/.bash_history
NAME        FSTYPE LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINT
mmcblk0
├─mmcblk0p1 vfat         2A4C-8F31                             508.7M     1% /boot/efi
└─mmcblk0p2 ext4         7d01b8fa-3a64-44eb-a176-4f42b89e54d1  109.1G     3% /
/dev/mmcblk0p2: UUID="7d01b8fa-3a64-44eb-a176-4f42b89e54d1" TYPE="ext4" PARTUUID="48e61c92-02"
/dev/mmcblk0p1: UUID="2A4C-8F31" TYPE="vfat" PARTUUID="48e61c92-01"
major minor  #blocks  name
 179        0  125829120 mmcblk0
 179        1     524288 mmcblk0p1
 179        2  125302784 mmcblk0p2
--- history ---
id; whoami; pwd; ls -la; uname -a
ls -la /root /home 2>/dev/null; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops_*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.db' -o -iname '*evidence*' -o -iname '*archive*' \) 2>/dev/null | head -50; cat /etc/passwd; echo ---; ls -la /var/backups /srv /opt 2>/dev/null
cat /root/.bash_history 2>/dev/null; echo '---CONFIG---'; ls -la /root/.ssh /root/.config /root/.cache 2>/dev/null
echo '== PORTS =='; ss -lntup 2>/dev/null || netstat -lntup 2>/dev/null; echo '== PROCS =='; ps auxww | head -60; echo '== DIRS =='; ls -la /tmp /var/tmp /usr/local /var/lib/mysql /var/lib/postgresql 2>/dev/null; echo '== CRON =='; ls -la /etc/cron* /var/spool/cron 2>/dev/null; crontab -l 2>/dev/null; echo '== RECENT =='; find / -xdev -type f -mmin -360 2>/dev/null | grep -Ev '^/(proc|sys|dev|run|var/lib/dpkg|var/cache|var/log|usr/share|usr/lib)' | head -120
cat /root/.bash_history 2>/dev/null; echo '---KNOWN_HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null
echo '---ID---'; id; echo '---ENV---'; env | sort; echo '---MOUNTS---'; mount; df -hT; echo '---DIRS---'; ls -la /var/www /var/backups /mnt /media /home 2>/dev/null; echo '---FILES---'; find /var/www /var/backups /home /mnt /media /opt /srv -maxdepth 5 -type f 2>/dev/null | sed -n '1,300p'
find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /usr/share -o -path /usr/lib -o -path /usr/src \) -prune -o -type f \( -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*record*' -o -iname '*opr_*' -o -iname '*ops_*' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -60
echo '=== ENV ==='; env; echo '=== ROOT ==='; ls -la /root 2>/dev/null; echo '=== SSH ==='; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/known_hosts 2>/dev/null; echo '=== HOSTS ==='; cat /etc/hosts 2>/dev/null; echo '=== DIRS ==='; ls -la /tmp /var/tmp /dev/shm /data /backup /var/lib /var/local /srv /opt 2>/dev/null; echo '=== HISTORIES ==='; for f in /root/.bash_history /home/*/.bash_history; do [ -f "$f" ] && echo "--- $f" && tail -n 80 "$f"; done 2>/dev/null; echo '=== MOUNTS ==='; mount | grep -Ev 'proc|sysfs|cgroup|devpts|tmpfs|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl|mqueue|hugetlbfs|autofs'
cat /root/.bash_history; echo '---PASSWD---'; getent passwd; echo '---MOUNTS---'; mount; echo '---PROCS---'; ps auxww
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /opt /srv /var/backups /home /root /var/lib -maxdepth 5 -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*.zip' -o -iname '*.bak' \) -ls 2>/dev/null | head -200`

```
root@ubuntu:~# find /opt /srv /var/backups /home /root /var/lib -maxdepth 5 -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*.zip' -o -iname '*.bak' \) -ls 2>/dev/null | head -200
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev \( -path /usr -o -path /lib -o -path /lib64 -o -path /boot -o -path /proc -o -path /sys -o -path /dev -o -path /var/lib/dpkg -o -path /var/cache \) -prune -o -type f \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar' -o -iname '*.tar.*' -o -iname '*.zip' \) -print 2>/dev/null | head -80; timeout 30 grep -Ral --exclude-dir={proc,sys,dev,usr,lib,lib64,boot,var/lib/dpkg,var/cache} -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' / 2>/dev/null | head -40`

```
root@ubuntu:~# find / -xdev \( -path /usr -o -path /lib -o -path /lib64 -o -path /boot -o -path /proc -o -path /sys -o -path /dev -o -path /var/lib/dpkg -o -path /var/cache \) -prune -o -type f \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar' -o -iname '*.tar.*' -o -iname '*.zip' \) -print 2>/dev/null | head -80; timeout 30 grep -Ral --exclude-dir={proc,sys,dev,usr,lib,lib64,boot,var/lib/dpkg,var/cache} -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' / 2>/dev/null | head -40
root@ubuntu:~# 
```
root@ubuntu:~# 
```
