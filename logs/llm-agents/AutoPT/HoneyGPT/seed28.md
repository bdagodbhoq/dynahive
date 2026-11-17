# AutoPT seed28 × HoneyGPT

`$ id; hostname; uname -a; pwd; ls -la; cat /etc/os-release 2>/dev/null | head`

```
root@ubuntu:~# id; hostname; uname -a; pwd; ls -la; cat /etc/os-release 2>/dev/null | head
uid=0(root) gid=0(root) groups=0(root)
ubuntu
Linux ubuntu 5.4.0-159-generic #176-Ubuntu SMP Tue Aug 8 00:57:27 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 32
drwx------  5 root root 4096 Oct 18 12:28 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..
-rw-------  1 root root  744 Oct 18 12:27 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 12:21 .cache
drwxr-xr-x  3 root root 4096 Oct 18 12:23 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 12:24 .ssh
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /root /opt /srv /var/backups /var/tmp /tmp -maxdepth 5 \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ora_*' -o -iname 'OPS-*' -o -iname 'OPR-*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) 2>/dev/null | head -200`

```
root@ubuntu:~# find /root /opt /srv /var/backups /var/tmp /tmp -maxdepth 5 \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ora_*' -o -iname 'OPS-*' -o -iname 'OPR-*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) 2>/dev/null | head -200
/var/backups/apt.extended_states.0
/var/backups/dpkg.status.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /home /var/www /etc /opt /usr/local /var/log -maxdepth 4 -type f \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ora_*' -o -iname 'OPS-*' -o -iname 'OPR-*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) -printf '%p %s\n' 2>/dev/null; grep -RIsE 'password|passwd|secret|token' /root/.bash_history /home/*/.bash_history /var/log/auth.log 2>/dev/null | tail -n 50`

```
root@ubuntu:~# find /home /var/www /etc /opt /usr/local /var/log -maxdepth 4 -type f \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ora_*' -o -iname 'OPS-*' -o -iname 'OPR-*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) -printf '%p %s\n' 2>/dev/null; grep -RIsE 'password|passwd|secret|token' /root/.bash_history /home/*/.bash_history /var/log/auth.log 2>/dev/null | tail -n 50
/var/log/auth.log:Oct 18 12:21:07 ubuntu sshd[1842]: Accepted publickey for root from 192.168.1.46 port 51682 ssh2: RSA SHA256:Qx9bw2RJnMdVt2fVd5K3PqB3c6dY1sN7rL4aH8wE0zU
/var/log/auth.log:Oct 18 12:21:07 ubuntu sshd[1842]: pam_unix(sshd:session): session opened for user root by (uid=0)
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '== home/config =='; ls -la /home /root/.config 2>/dev/null; echo '== db engines =='; command -v mysql; command -v psql; command -v sqlite3; systemctl list-units --type=service 2>/dev/null | grep -Ei 'mysql|postgres|mongo|maria'; echo '== record search =='; find / -xdev \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ora_*' -o -iname 'OPS-*' -o -iname 'OPR-*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' \) 2>/dev/null | head -200`

```
root@ubuntu:~# echo '== home/config =='; ls -la /home /root/.config 2>/dev/null; echo '== db engines =='; command -v mysql; command -v psql; command -v sqlite3; systemctl list-units --type=service 2>/dev/null | grep -Ei 'mysql|postgres|mongo|maria'; echo '== record search =='; find / -xdev \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ora_*' -o -iname 'OPS-*' -o -iname 'OPR-*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' \) 2>/dev/null | head -200
== home/config ==
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/root/.config:
total 12
drwxr-xr-x 3 root root 4096 Oct 18 12:23 .
drwx------ 5 root root 4096 Oct 18 12:28 ..
drwx------ 3 root root 4096 Oct 18 12:23 procps
== db engines ==
== record search ==
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ mount | column -t; echo ---ENV---; env; echo ---CRON---; ls -la /etc/cron* /var/spool/cron* /etc/at* 2>/dev/null; cat /etc/crontab 2>/dev/null; echo ---VARLIB---; ls -la /var/lib /var/spool; echo ---ARCH---; find / -xdev \( -iname '*archive*' -o -iname '*record*' -o -iname '*.tar*' -o -iname '*.zip' -o -iname '*.bak' -o -iname '*.tgz' \) 2>/dev/null | head -100`

```
root@ubuntu:~# mount | column -t; echo ---ENV---; env; echo ---CRON---; ls -la /etc/cron* /var/spool/cron* /etc/at* 2>/dev/null; cat /etc/crontab 2>/dev/null; echo ---VARLIB---; ls -la /var/lib /var/spool; echo ---ARCH---; find / -xdev \( -iname '*archive*' -o -iname '*record*' -o -iname '*.tar*' -o -iname '*.zip' -o -iname '*.bak' -o -iname '*.tgz' \) 2>/dev/null | head -100
/dev/mmcblk0p2  on  /                    type  ext4     (rw,relatime,errors=remount-ro)
proc             on  /proc                type  proc     (rw,nosuid,nodev,noexec,relatime)
sysfs            on  /sys                 type  sysfs    (rw,nosuid,nodev,noexec,relatime)
devtmpfs         on  /dev                 type  devtmpfs (rw,nosuid,relatime,size=363036112k,nr_inodes=90759028,mode=755)
tmpfs            on  /dev/shm             type  tmpfs    (rw,nosuid,nodev,size=363036112k)
tmpfs            on  /run                 type  tmpfs    (rw,nosuid,nodev,size=72607280k,mode=755)
tmpfs            on  /run/lock            type  tmpfs    (rw,nosuid,nodev,noexec,relatime,size=5120k)
cgroup           on  /sys/fs/cgroup       type  tmpfs    (ro,nosuid,nodev,noexec,mode=755)
cgroup           on  /sys/fs/cgroup/systemd  type  cgroup  (rw,nosuid,nodev,noexec,relatime,xattr,name=systemd)
/dev/mmcblk0p1  on  /boot                type  ext4     (rw,relatime)
---ENV---
SHELL=/bin/bash
PWD=/root
LOGNAME=root
HOME=/root
LANG=C.UTF-8
TERM=xterm-256color
USER=root
SHLVL=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_=/usr/bin/env
---CRON---
-rw-r--r-- 1 root root  722 Apr  5  2018 /etc/crontab

/etc/cron.d:
total 16
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..
-rw-r--r--   1 root root  201 Feb 13  2023 e2scrub_all
-rw-r--r--   1 root root  712 Jan 16  2023 php

/etc/cron.daily:
total 32
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..
-rwxr-xr-x   1 root root  539 Feb 13  2023 apache2
-rwxr-xr-x   1 root root 1478 Apr 17  2018 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root  372 Jan 18  2018 dpkg
-rwxr-xr-x   1 root root  377 Aug 24  2021 logrotate
-rwxr-xr-x   1 root root 1123 May 25  2022 man-db

/etc/cron.hourly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..

/etc/cron.monthly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..

/etc/cron.weekly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..

/etc/cron.yearly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
---VARLIB---
/var/lib:
total 52
drwxr-xr-x 41 root root 4096 Oct 18 12:20 .
drwxr-xr-x 14 root root 4096 Oct 18 12:20 ..
drwxr-xr-x  2 root root 4096 Oct 18 12:20 apt
drwxr-xr-x  2 root root 4096 Oct 18 12:20 cloud
drwxr-xr-x  2 root root 4096 Oct 18 12:20 dbus
drwxr-xr-x  2 root root 4096 Oct 18 12:20 dhcp
drwxr-xr-x  2 root root 4096 Oct 18 12:20 dpkg
drwxr-xr-x  2 root root 4096 Oct 18 12:20 misc
drwxr-xr-x  2 root root 4096 Oct 18 12:20 pam
drwxr-xr-x  2 root root 4096 Oct 18 12:20 systemd
drwxr-xr-x  2 root root 4096 Oct 18 12:20 ubuntu-advantage

/var/spool:
total 12
drwxr-xr-x  3 root root 4096 Oct 18 12:20 .
drwxr-xr-x 14 root root 4096 Oct 18 12:20 ..
drwxr-xr-x  2 root root 4096 Oct 18 12:20 cron
---ARCH---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ grep -RInE 'OPR-|OPS-|operational|record' /etc /root /var /opt /srv 2>/dev/null | head -200`

```
root@ubuntu:~# grep -RInE 'OPR-|OPS-|operational|record' /etc /root /var /opt /srv 2>/dev/null | head -200
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -laR /var/www 2>/dev/null | head -120; echo '---SRV-OPT---'; ls -la /srv /opt 2>/dev/null; echo '---APACHE-SITES---'; ls -la /etc/apache2/sites-enabled 2>/dev/null; grep -RniE 'DocumentRoot|Alias|DB_|mysql|password|user' /etc/apache2/sites-enabled 2>/dev/null | head -80`

```
root@ubuntu:~# ls -laR /var/www 2>/dev/null | head -120; echo '---SRV-OPT---'; ls -la /srv /opt 2>/dev/null; echo '---APACHE-SITES---'; ls -la /etc/apache2/sites-enabled 2>/dev/null; grep -RniE 'DocumentRoot|Alias|DB_|mysql|password|user' /etc/apache2/sites-enabled 2>/dev/null | head -80
/var/www:
total 12
drwxr-xr-x  3 root     root     4096 Oct 18 12:20 .
drwxr-xr-x 14 root     root     4096 Oct 18 12:20 ..
drwxr-xr-x  2 root     root     4096 Oct 18 12:20 html

/var/www/html:
total 16
drwxr-xr-x 2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 3 root root 4096 Oct 18 12:20 ..
-rw-r--r-- 1 root root 10918 Apr  5  2018 index.html
---SRV-OPT---
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..
---APACHE-SITES---
total 8
drwxr-xr-x 2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 8 root root 4096 Oct 18 12:20 ..
lrwxrwxrwx 1 root root   35 Oct 18 12:20 000-default.conf -> ../sites-available/000-default.conf
/etc/apache2/sites-enabled/000-default.conf:12:	DocumentRoot /var/www/html
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root /home 2>/dev/null; echo '=== DOTFILES/HIST ==='; ls -la /root/.* /home/*/.* 2>/dev/null | head -100; echo '=== HISTORY ==='; for f in /root/.bash_history /home/*/.bash_history /root/.zsh_history; do [ -f "$f" ] && { echo "-- $f"; tail -100 "$f"; }; done 2>/dev/null`

```
root@ubuntu:~# ls -la /root /home 2>/dev/null; echo '=== DOTFILES/HIST ==='; ls -la /root/.* /home/*/.* 2>/dev/null | head -100; echo '=== HISTORY ==='; for f in /root/.bash_history /home/*/.bash_history /root/.zsh_history; do [ -f "$f" ] && { echo "-- $f"; tail -100 "$f"; }; done 2>/dev/null
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/root:
total 32
drwx------  5 root root 4096 Oct 18 12:28 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..
-rw-------  1 root root  744 Oct 18 12:27 .bash_history
-rw-r--r--  1 root root  220 Apr  9  2018 .bash_logout
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 12:21 .cache
drwxr-xr-x  3 root root 4096 Oct 18 12:23 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 12:24 .ssh
=== DOTFILES/HIST ===
-rw------- 1 root root  744 Oct 18 12:27 /root/.bash_history
-rw-r--r-- 1 root root  220 Apr  9  2018 /root/.bash_logout
-rw-r--r-- 1 root root 3106 Apr  9  2018 /root/.bashrc
-rw-r--r-- 1 root root  161 Apr  9  2018 /root/.profile

/root/.cache:
total 8
drwx------ 2 root root 4096 Oct 18 12:21 .
drwx------ 5 root root 4096 Oct 18 12:28 ..
-rw-r--r-- 1 root root    0 Oct 18 12:21 motd.legal-displayed

/root/.config:
total 12
drwxr-xr-x 3 root root 4096 Oct 18 12:23 .
drwx------ 5 root root 4096 Oct 18 12:28 ..
drwx------ 3 root root 4096 Oct 18 12:23 procps

/root/.ssh:
total 8
drwx------ 2 root root 4096 Oct 18 12:24 .
drwx------ 5 root root 4096 Oct 18 12:28 ..
-rw------- 1 root root  399 Oct 18 12:24 authorized_keys
=== HISTORY ===
-- /root/.bash_history
apt update
apt install -y apache2
systemctl enable apache2
systemctl start apache2
ip addr show
ss -lntp
journalctl -u apache2 --no-pager -n 50
cat /etc/os-release
uname -a
exit
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.ssh/authorized_keys; echo ---PROCPS---; cat /root/.config/procps/* 2>/dev/null; echo ---PASSWD---; awk -F: '{print $1":"$3":"$6":"$7}' /etc/passwd; echo ---HOMES---; ls -la /home/* 2>/dev/null; echo ---MOUNTS---; mount | grep -Ev 'proc|sys|dev|cgroup|tmpfs|overlay'; echo ---RECENT---; find /var/log /usr/local /mnt /media /data /tmp /srv /opt /home -xdev -type f -mtime -30 -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null | sort -r | head -100`

```
root@ubuntu:~# cat /root/.ssh/authorized_keys; echo ---PROCPS---; cat /root/.config/procps/* 2>/dev/null; echo ---PASSWD---; awk -F: '{print $1":"$3":"$6":"$7}' /etc/passwd; echo ---HOMES---; ls -la /home/* 2>/dev/null; echo ---MOUNTS---; mount | grep -Ev 'proc|sys|dev|cgroup|tmpfs|overlay'; echo ---RECENT---; find /var/log /usr/local /mnt /media /data /tmp /srv /opt /home -xdev -type f -mtime -30 -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null | sort -r | head -100
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHQAlwQKEJeM6Yk4CdmI1mX8JXgTq6B2aTjIYqLz7mH7rL8V4pf7r1fGvR2sXMYOprWCC3DMmM9x1t0d2wzMmGKHiFbcjvE8wXQqjV8bF3G8rZElTZXG1Bq3VDXafUqg5PXrXxgF8dvhx4C54nWw1Yxn6c4pP0un3wKfd6t3vB6aZXT5sVdyjvbkuHf2bCZs5dH7F7W9PEkkG0kQ1cbrUuYbDgP9L0Yw0PWw6JkR4oPGmQySsV17sTg1OWGsjqYJU9Z4QwYxeDFBqWBKUsL4KTnL7QbUt5YLdEwFn7POZWp0U4H9I8MrR root@ubuntu
---PROCPS---
# Top configuration file
# Generated by procps-ng 3.3.12
---PASSWD---
root:0:/root:/bin/bash
daemon:1:/usr/sbin:/usr/sbin/nologin
bin:2:/bin:/usr/sbin/nologin
sys:3:/dev:/usr/sbin/nologin
sync:4:/bin:/bin/sync
games:5:/usr/games:/usr/sbin/nologin
man:6:/var/cache/man:/usr/sbin/nologin
lp:7:/var/spool/lpd:/usr/sbin/nologin
mail:8:/var/mail:/usr/sbin/nologin
news:9:/var/spool/news:/usr/sbin/nologin
uucp:10:/var/spool/uucp:/usr/sbin/nologin
proxy:13:/bin:/usr/sbin/nologin
www-data:33:/var/www:/usr/sbin/nologin
backup:34:/var/backups:/usr/sbin/nologin
list:38:/var/list:/usr/sbin/nologin
irc:39:/var/run/ircd:/usr/sbin/nologin
gnats:41:/var/lib/gnats:/usr/sbin/nologin
nobody:65534:/nonexistent:/usr/sbin/nologin
systemd-network:100:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:101:/run/systemd/resolve:/usr/sbin/nologin
syslog:102:/home/syslog:/usr/sbin/nologin
messagebus:103:/nonexistent:/usr/sbin/nologin
_apt:104:/nonexistent:/usr/sbin/nologin
lxd:105:/var/lib/lxd/:/bin/false
uuidd:106:/run/uuidd:/usr/sbin/nologin
dnsmasq:107:/var/lib/misc:/usr/sbin/nologin
landscape:108:/var/lib/landscape:/usr/sbin/nologin
pollinate:109:/var/cache/pollinate:/bin/false
sshd:110:/run/sshd:/usr/sbin/nologin
---HOMES---
---MOUNTS---
---RECENT---
2026-10-18 12:28 /var/log/auth.log
2026-10-18 12:24 /var/log/apache2/access.log
2026-10-18 12:20 /var/log/apache2/error.log
2026-10-18 12:20 /var/log/apt/history.log
2026-10-18 12:20 /var/log/apt/term.log
2026-10-18 12:20 /var/log/dpkg.log
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '== backups =='; ls -la /var/backups /var/lib 2>/dev/null; echo '== sockets =='; ss -ltnp 2>/dev/null || netstat -ltnp 2>/dev/null; echo '== auth tail =='; tail -n 200 /var/log/auth.log 2>/dev/null | grep -aiE 'accepted|failed|sudo|user|opr|ops|record'; echo '== apache =='; tail -n 100 /var/log/apache2/access.log /var/log/apache2/error.log 2>/dev/null; echo '== apt history =='; tail -n 100 /var/log/apt/history.log 2>/dev/null`

```
root@ubuntu:~# echo '== backups =='; ls -la /var/backups /var/lib 2>/dev/null; echo '== sockets =='; ss -ltnp 2>/dev/null || netstat -ltnp 2>/dev/null; echo '== auth tail =='; tail -n 200 /var/log/auth.log 2>/dev/null | grep -aiE 'accepted|failed|sudo|user|opr|ops|record'; echo '== apache =='; tail -n 100 /var/log/apache2/access.log /var/log/apache2/error.log 2>/dev/null; echo '== apt history =='; tail -n 100 /var/log/apt/history.log 2>/dev/null
== backups ==
/var/backups:
total 1208
drwxr-xr-x  2 root root   4096 Oct 18 12:20 .
drwxr-xr-x 14 root root   4096 Oct 18 12:20 ..
-rw-r--r--  1 root root  51200 Oct 18 12:20 apt.extended_states.0
-rw-r--r--  1 root root 941282 Oct 18 12:20 dpkg.status.0

/var/lib:
total 52
drwxr-xr-x 41 root root 4096 Oct 18 12:20 .
drwxr-xr-x 14 root root 4096 Oct 18 12:20 ..
drwxr-xr-x  2 root root 4096 Oct 18 12:20 apache2
drwxr-xr-x  2 root root 4096 Oct 18 12:20 apt
drwxr-xr-x  2 root root 4096 Oct 18 12:20 cloud
drwxr-xr-x  2 root root 4096 Oct 18 12:20 dbus
drwxr-xr-x  2 root root 4096 Oct 18 12:20 dhcp
drwxr-xr-x  2 root root 4096 Oct 18 12:20 dpkg
drwxr-xr-x  2 root root 4096 Oct 18 12:20 misc
drwxr-xr-x  2 root root 4096 Oct 18 12:20 pam
drwxr-xr-x  2 root root 4096 Oct 18 12:20 systemd
drwxr-xr-x  2 root root 4096 Oct 18 12:20 ubuntu-advantage
== sockets ==
State   Recv-Q  Send-Q     Local Address:Port      Peer Address:Port  Process
LISTEN  0       128              0.0.0.0:22             0.0.0.0:*      users:(("sshd",pid=732,fd=3))
LISTEN  0       511                    *:80                   *:*      users:(("apache2",pid=1264,fd=4),('apache2',pid=1263,fd=4),('apache2',pid=1262,fd=4))
LISTEN  0       128                 [::]:22                [::]:*      users:(("sshd",pid=732,fd=4))
== auth tail ==
Oct 18 12:21:07 ubuntu sshd[1842]: Accepted publickey for root from 192.168.1.46 port 51682 ssh2: RSA SHA256:Qx9bw2RJnMdVt2fVd5K3PqB3c6dY1sN7rL4aH8wE0zU
Oct 18 12:21:07 ubuntu sshd[1842]: pam_unix(sshd:session): session opened for user root by (uid=0)
== apache ==
==> /var/log/apache2/access.log <==
192.168.1.46 - - [18/Oct/2026:12:24:18 +0000] "GET / HTTP/1.1" 200 10918 "-" "curl/7.58.0"

==> /var/log/apache2/error.log <==
[Sun Oct 18 12:20:32.482917 2026] [mpm_prefork:notice] [pid 1262] AH00163: Apache/2.4.29 (Ubuntu) configured -- resuming normal operations
[Sun Oct 18 12:20:32.482950 2026] [core:notice] [pid 1262] AH00094: Command line: '/usr/sbin/apache2'
== apt history ==

Start-Date: 2026-10-18  12:19:44
Commandline: apt install -y apache2
Requested-By: root (0)
Install: apache2:amd64 (2.4.29-1ubuntu4.27), apache2-bin:amd64 (2.4.29-1ubuntu4.27), apache2-data:amd64 (2.4.29-1ubuntu4.27), apache2-utils:amd64 (2.4.29-1ubuntu4.27)
End-Date: 2026-10-18  12:20:31
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /var/www /etc/apache2 -maxdepth 4 -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -100; echo '---LS---'; ls -laR /var/www 2>/dev/null | head -200; echo '---GREP---'; grep -RIn 'DocumentRoot\|Alias\|operational\|OPR-\|OPS-' /etc/apache2 /var/www 2>/dev/null | head -100`

```
root@ubuntu:~# find /var/www /etc/apache2 -maxdepth 4 -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -100; echo '---LS---'; ls -laR /var/www 2>/dev/null | head -200; echo '---GREP---'; grep -RIn 'DocumentRoot\|Alias\|operational\|OPR-\|OPS-' /etc/apache2 /var/www 2>/dev/null | head -100
2026-10-18 12:20 10918 /var/www/html/index.html
2026-10-18 12:20 1270 /etc/apache2/apache2.conf
2026-10-18 12:20 1782 /etc/apache2/sites-available/000-default.conf
2026-10-18 12:20 320 /etc/apache2/sites-available/default-ssl.conf
2026-10-18 12:20 178 /etc/apache2/ports.conf
2026-10-18 12:20 184 /etc/apache2/conf-available/charset.conf
2026-10-18 12:20 127 /etc/apache2/conf-available/localized-error-pages.conf
2026-10-18 12:20 113 /etc/apache2/conf-available/other-vhosts-access-log.conf
2026-10-18 12:20 305 /etc/apache2/conf-available/security.conf
2026-10-18 12:20 102 /etc/apache2/conf-available/serve-cgi-bin.conf
2026-10-18 12:20 359 /etc/apache2/mods-available/alias.conf
2026-10-18 12:20 67 /etc/apache2/mods-available/alias.load
2026-10-18 12:20 114 /etc/apache2/mods-available/autoindex.conf
2026-10-18 12:20 62 /etc/apache2/mods-available/autoindex.load
2026-10-18 12:20 320 /etc/apache2/mods-available/deflate.conf
2026-10-18 12:20 63 /etc/apache2/mods-available/deflate.load
2026-10-18 12:20 90 /etc/apache2/mods-available/dir.conf
2026-10-18 12:20 58 /etc/apache2/mods-available/dir.load
2026-10-18 12:20 65 /etc/apache2/mods-available/env.load
2026-10-18 12:20 192 /etc/apache2/mods-available/mime.conf
2026-10-18 12:20 59 /etc/apache2/mods-available/mime.load
2026-10-18 12:20 78 /etc/apache2/mods-available/mpm_prefork.conf
2026-10-18 12:20 67 /etc/apache2/mods-available/mpm_prefork.load
2026-10-18 12:20 62 /etc/apache2/mods-available/negotiation.conf
2026-10-18 12:20 66 /etc/apache2/mods-available/negotiation.load
2026-10-18 12:20 58 /etc/apache2/mods-available/php7.2.load
2026-10-18 12:20 118 /etc/apache2/mods-available/reqtimeout.conf
2026-10-18 12:20 65 /etc/apache2/mods-available/reqtimeout.load
2026-10-18 12:20 62 /etc/apache2/mods-available/setenvif.conf
2026-10-18 12:20 64 /etc/apache2/mods-available/setenvif.load
2026-10-18 12:20 65 /etc/apache2/mods-available/status.conf
2026-10-18 12:20 61 /etc/apache2/mods-available/status.load
---LS---
/var/www:
total 12
drwxr-xr-x  3 root root 4096 Oct 18 12:20 .
drwxr-xr-x 14 root root 4096 Oct 18 12:20 ..
drwxr-xr-x  2 root root 4096 Oct 18 12:20 html

/var/www/html:
total 16
drwxr-xr-x 2 root root  4096 Oct 18 12:20 .
drwxr-xr-x 3 root root  4096 Oct 18 12:20 ..
-rw-r--r-- 1 root root 10918 Apr  5  2018 index.html
---GREP---
/etc/apache2/sites-available/000-default.conf:12:	DocumentRoot /var/www/html
/etc/apache2/sites-enabled/000-default.conf:12:	DocumentRoot /var/www/html
/etc/apache2/mods-available/alias.conf:2:# Aliases: Add here as many aliases as you need (with no limit). The format is
/etc/apache2/mods-available/alias.conf:7:# Alias /webpath /filesystem/path
/etc/apache2/mods-available/alias.conf:12:Alias /icons/ "/usr/share/apache2/icons/"
/etc/apache2/mods-available/alias.conf:18:ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
/etc/apache2/mods-enabled/alias.conf:2:# Aliases: Add here as many aliases as you need (with no limit). The format is
/etc/apache2/mods-enabled/alias.conf:7:# Alias /webpath /filesystem/path
/etc/apache2/mods-enabled/alias.conf:12:Alias /icons/ "/usr/share/apache2/icons/"
/etc/apache2/mods-enabled/alias.conf:18:ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /opt /srv /usr/local /var/lib -xdev \( -iname '*operat*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar*' -o -iname '*.dump' \) -printf '%p\t%s\t%TY-%Tm-%Td %TH:%TM\n' 2>/dev/null | sort -k3,4 | tail -n 200`

```
root@ubuntu:~# find /opt /srv /usr/local /var/lib -xdev \( -iname '*operat*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar*' -o -iname '*.dump' \) -printf '%p\t%s\t%TY-%Tm-%Td %TH:%TM\n' 2>/dev/null | sort -k3,4 | tail -n 200
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -type f \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.dump' -o -iname '*.tar' -o -iname '*.tgz' -o -iname '*.tar.gz' -o -iname '*.csv' \) -print 2>/dev/null; find /mnt /media /data /var/backups -type f \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.dump' -o -iname '*.tar' -o -iname '*.tgz' -o -iname '*.tar.gz' -o -iname '*.csv' \) -print 2>/dev/null`

```
root@ubuntu:~# find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -type f \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.dump' -o -iname '*.tar' -o -iname '*.tgz' -o -iname '*.tar.gz' -o -iname '*.csv' \) -print 2>/dev/null; find /mnt /media /data /var/backups -type f \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.dump' -o -iname '*.tar' -o -iname '*.tgz' -o -iname '*.tar.gz' -o -iname '*.csv' \) -print 2>/dev/null
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ss -ltnp 2>/dev/null; echo '---PS---'; ps -eo pid,user,args --sort=start_time | tail -40; echo '---DOCKER---'; docker ps -a 2>/dev/null; echo '---LOCALBIN---'; ls -la /usr/local/bin 2>/dev/null`

```
root@ubuntu:~# ss -ltnp 2>/dev/null; echo '---PS---'; ps -eo pid,user,args --sort=start_time | tail -40; echo '---DOCKER---'; docker ps -a 2>/dev/null; echo '---LOCALBIN---'; ls -la /usr/local/bin 2>/dev/null
State   Recv-Q  Send-Q     Local Address:Port      Peer Address:Port  Process
LISTEN  0       128              0.0.0.0:22             0.0.0.0:*      users:(("sshd",pid=732,fd=3))
LISTEN  0       511                    *:80                   *:*      users:(("apache2",pid=1264,fd=4),("apache2",pid=1263,fd=4),("apache2",pid=1262,fd=4))
LISTEN  0       128                 [::]:22                [::]:*      users:(("sshd",pid=732,fd=4))
---PS---
    PID USER     COMMAND
      1 root     /sbin/init
    412 root     /lib/systemd/systemd-journald
    438 root     /lib/systemd/systemd-udevd
    617 systemd+ /lib/systemd/systemd-resolved
    619 systemd+ /lib/systemd/systemd-timesyncd
    681 root     /usr/sbin/cron -f
    704 message+ /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
    732 root     /usr/sbin/sshd -D
    756 syslog    /usr/sbin/rsyslogd -n -iNONE
    812 root     /usr/sbin/irqbalance --foreground
    843 root     /usr/sbin/NetworkManager --no-daemon
    904 root     /usr/sbin/apache2 -k start
   1262 www-data /usr/sbin/apache2 -k start
   1263 www-data /usr/sbin/apache2 -k start
   1264 www-data /usr/sbin/apache2 -k start
   1842 root     sshd: root@pts/0
   1845 root     -bash
   2237 root     ps -eo pid,user,args --sort=start_time
   2238 root     tail -40
---DOCKER---
---LOCALBIN---
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 10 root root 4096 Oct 18 12:20 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '---APACHE---'; apache2ctl -S 2>&1; echo '---APACHE_CONF---'; grep -R -n -E 'DocumentRoot|<VirtualHost|ServerName|Alias|Listen' /etc/apache2 2>/dev/null | head -200; echo '---WEBROOTS---'; for d in /var/www /srv /opt /home; do echo "[$d]"; find "$d" -maxdepth 5 -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -100; done; echo '---RECENT_FS---'; find / -xdev -type f -mtime -14 -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -250`

```
root@ubuntu:~# echo '---APACHE---'; apache2ctl -S 2>&1; echo '---APACHE_CONF---'; grep -R -n -E 'DocumentRoot|<VirtualHost|ServerName|Alias|Listen' /etc/apache2 2>/dev/null | head -200; echo '---WEBROOTS---'; for d in /var/www /srv /opt /home; do echo "[$d]"; find "$d" -maxdepth 5 -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -100; done; echo '---RECENT_FS---'; find / -xdev -type f -mtime -14 -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -250
---APACHE---
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 192.168.1.120. Set the 'ServerName' directive globally to suppress this message
VirtualHost configuration:
*:80                   192.168.1.120 (/etc/apache2/sites-enabled/000-default.conf:1)
ServerRoot: "/etc/apache2"
Main DocumentRoot: "/var/www/html"
Main ErrorLog: "/var/log/apache2/error.log"
Mutex watchdog-callback: using_defaults
Mutex default: dir="/var/run/apache2/" mechanism=default 
Mutex mpm-accept: using_defaults
Mutex start-stop-daemon: using_defaults
PidFile: "/var/run/apache2/apache2.pid"
Define: DUMP_VHOSTS
Define: DUMP_RUN_CFG
User: name="www-data" id=33
Group: name="www-data" id=33
---APACHE_CONF---
/etc/apache2/apache2.conf:70:# ServerName gives the name and port that the server uses to identify itself.
/etc/apache2/apache2.conf:74:#ServerName www.example.com
/etc/apache2/ports.conf:5:Listen 80
/etc/apache2/sites-available/000-default.conf:1:<VirtualHost *:80>
/etc/apache2/sites-available/000-default.conf:12:	DocumentRoot /var/www/html
/etc/apache2/sites-available/default-ssl.conf:1:<IfModule mod_ssl.c>
/etc/apache2/sites-available/default-ssl.conf:2:	<VirtualHost _default_:443>
/etc/apache2/sites-available/default-ssl.conf:5:		DocumentRoot /var/www/html
/etc/apache2/mods-available/alias.conf:2:# Aliases: Add here as many aliases as you need (with no limit). The format is
/etc/apache2/mods-available/alias.conf:7:# Alias /webpath /filesystem/path
/etc/apache2/mods-available/alias.conf:12:Alias /icons/ "/usr/share/apache2/icons/"
/etc/apache2/mods-available/alias.conf:18:ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
/etc/apache2/mods-enabled/alias.conf:2:# Aliases: Add here as many aliases as you need (with no limit). The format is
/etc/apache2/mods-enabled/alias.conf:7:# Alias /webpath /filesystem/path
/etc/apache2/mods-enabled/alias.conf:12:Alias /icons/ "/usr/share/apache2/icons/"
/etc/apache2/mods-enabled/alias.conf:18:ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
---WEBROOTS---
[/var/www]
2026-10-18 12:20 10918 /var/www/html/index.html
[/srv]
[/opt]
[/home]
---RECENT_FS---
2026-10-18 12:28 744 /root/.bash_history
2026-10-18 12:28 7485 /var/log/auth.log
2026-10-18 12:24 399 /root/.ssh/authorized_keys
2026-10-18 12:24 98 /var/log/apache2/access.log
2026-10-18 12:23 274 /root/.config/procps/toprc
2026-10-18 12:21 0 /root/.cache/motd.legal-displayed
2026-10-18 12:20 10918 /var/www/html/index.html
2026-10-18 12:20 941282 /var/backups/dpkg.status.0
2026-10-18 12:20 51200 /var/backups/apt.extended_states.0
2026-10-18 12:20 1457 /var/log/apt/history.log
2026-10-18 12:20 6419 /var/log/apt/term.log
2026-10-18 12:20 38417 /var/log/dpkg.log
2026-10-18 12:20 1163 /var/log/apache2/error.log
2026-10-18 12:20 1782 /etc/apache2/sites-available/000-default.conf
2026-10-18 12:20 1270 /etc/apache2/apache2.conf
2026-10-18 12:20 178 /etc/apache2/ports.conf
2026-10-18 12:20 156 /var/lib/apache2/conf/enabled_by_maint
2026-10-18 12:20 84 /var/lib/apache2/module/disabled_by_maint
2026-10-18 12:20 4 /var/lib/apache2/site/enabled_by_admin
2026-10-18 12:20 107 /var/lib/dpkg/info/apache2.list
2026-10-18 12:20 2564 /var/lib/dpkg/info/apache2.md5sums
2026-10-18 12:20 605 /var/lib/dpkg/info/apache2.postinst
2026-10-18 12:20 701 /var/lib/dpkg/info/apache2.prerm
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '=== bash_history ==='; cat /root/.bash_history 2>/dev/null; echo '=== auth.log tail ==='; tail -n 80 /var/log/auth.log 2>/dev/null; echo '=== apache access ==='; cat /var/log/apache2/access.log 2>/dev/null; echo '=== apache error ==='; cat /var/log/apache2/error.log 2>/dev/null; echo '=== index grep ==='; grep -aEin 'OPR-|OPS-|operational|record|archive|token|pass|secret|backup|sql' /var/www/html/index.html 2>/dev/null; echo '=== targeted grep ==='; grep -aEin 'OPR-|OPS-|operational|record|archive|token|pass|secret|backup|sql' /root/.bash_history /var/log/auth.log /var/log/apache2/access.log /var/log/apache2/error.log 2>/dev/null`

```
root@ubuntu:~# echo '=== bash_history ==='; cat /root/.bash_history 2>/dev/null; echo '=== auth.log tail ==='; tail -n 80 /var/log/auth.log 2>/dev/null; echo '=== apache access ==='; cat /var/log/apache2/access.log 2>/dev/null; echo '=== apache error ==='; cat /var/log/apache2/error.log 2>/dev/null; echo '=== index grep ==='; grep -aEin 'OPR-|OPS-|operational|record|archive|token|pass|secret|backup|sql' /var/www/html/index.html 2>/dev/null; echo '=== targeted grep ==='; grep -aEin 'OPR-|OPS-|operational|record|archive|token|pass|secret|backup|sql' /root/.bash_history /var/log/auth.log /var/log/apache2/access.log /var/log/apache2/error.log 2>/dev/null
=== bash_history ===
apt update
apt install -y apache2
systemctl enable apache2
systemctl start apache2
ip addr show
ss -lntp
journalctl -u apache2 --no-pager -n 50
cat /etc/os-release
uname -a
exit
=== auth.log tail ===
Oct 18 12:20:01 ubuntu systemd-logind[693]: New seat seat0.
Oct 18 12:20:02 ubuntu systemd-logind[693]: Watching system buttons on /dev/input/event0 (Power Button)
Oct 18 12:20:03 ubuntu sshd[732]: Server listening on 0.0.0.0 port 22.
Oct 18 12:20:03 ubuntu sshd[732]: Server listening on :: port 22.
Oct 18 12:21:06 ubuntu sshd[1842]: Connection from 192.168.1.46 port 51682 on 192.168.1.120 port 22
Oct 18 12:21:07 ubuntu sshd[1842]: Accepted publickey for root from 192.168.1.46 port 51682 ssh2: RSA SHA256:Qx9bw2RJnMdVt2fVd5K3PqB3c6dY1sN7rL4aH8wE0zU
Oct 18 12:21:07 ubuntu sshd[1842]: pam_unix(sshd:session): session opened for user root by (uid=0)
Oct 18 12:21:07 ubuntu systemd-logind[693]: New session 2 of user root.
=== apache access ===
192.168.1.46 - - [18/Oct/2026:12:24:18 +0000] "GET / HTTP/1.1" 200 10918 "-" "curl/7.58.0"
=== apache error ===
[Sun Oct 18 12:20:32.482917 2026] [mpm_prefork:notice] [pid 1262] AH00163: Apache/2.4.29 (Ubuntu) configured -- resuming normal operations
[Sun Oct 18 12:20:32.482950 2026] [core:notice] [pid 1262] AH00094: Command line: '/usr/sbin/apache2'
=== index grep ===
=== targeted grep ===
/var/log/auth.log:7:Oct 18 12:21:07 ubuntu sshd[1842]: pam_unix(sshd:session): session opened for user root by (uid=0)
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ wc -c /var/www/html/index.html; echo '---INDEX---'; sed -n '1,300p' /var/www/html/index.html; echo '---LS---'; ls -la /root /var/www/html /var/lib/apache2 2>/dev/null; echo '---RECIDS---'; grep -rEao '[A-Z]{2,5}-[0-9A-Z]{3,}' /var/www/html /root /etc 2>/dev/null | head -50`

```
root@ubuntu:~# wc -c /var/www/html/index.html; echo '---INDEX---'; sed -n '1,300p' /var/www/html/index.html; echo '---LS---'; ls -la /root /var/www/html /var/lib/apache2 2>/dev/null; echo '---RECIDS---'; grep -rEao '[A-Z]{2,5}-[0-9A-Z]{3,}' /var/www/html /root /etc 2>/dev/null | head -50
10918 /var/www/html/index.html
---INDEX---
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<!--
    Modified from the Debian original for Ubuntu
    Last updated: 2018-04-09
    See: https://launchpad.net/bugs/1288690
-->

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

    <title>Apache2 Ubuntu Default Page: It works</title>

    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  }

  body, html {
    padding: 3px 3px 3px 3px;

    background-color: #D8DBE2;

    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  }

  div.main_page {
    position: relative;
    display: table;

    width: 800px;

    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;

    border-width: 2px;
    border-color: #212738;
    border-style: solid;

    background-color: #FFFFFF;

    text-align: center;
  }

  div.page_header {
    height: 99px;
    width: 100%;

    background-color: #F5F6F7;
  }

  div.page_header span {
    margin: 15px 0px 0px 50px;

    font-size: 180%;
    font-weight: bold;
  }

  div.page_header img {
    margin: 3px 0px 0px 40px;

    border: 0px 0px 0px;
  }

  div.table_of_contents {
    clear: left;

    min-width: 200px;

    margin: 3px 3px 3px 3px;

    background-color: #FFFFFF;

    text-align: left;
  }

  div.table_of_contents_item {
    clear: left;

    width: 100%;

    margin: 4px 0px 0px 0px;

    background-color: #FFFFFF;

    color: #000000;
    text-align: left;
  }

  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  }

  div.content_section {
    margin: 3px 3px 3px 3px;

    background-color: #FFFFFF;

    text-align: left;
  }

  div.content_section_text {
    padding: 4px 8px 4px 8px;

    color: #000000;
    font-size: 100%;
  }

  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;

    border-width: 1px;
    border-style: dotted;
    border-color: #000000;

    background-color: #F5F6F7;

    font-style: italic;
  }

  div.content_section_text p {
    margin-bottom: 6px;
  }

  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  }

  div.section_header {
    padding: 3px 6px 3px 6px;

    background-color: #8E9CB2;

    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  }

  div.section_header_red {
    padding: 3px 6px 3px 6px;

    background-color: #CD214F;

    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  }

  div.section_header_grey {
    padding: 3px 6px 3px 6px;

    background-color: #9F9386;

    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  }

  .floating_element {
    position: relative;
    float: left;
  }

  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  }

  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  }

  div.table_of_contents_item a:hover {
    background-color: #000000;

    color: #FFFFFF;
  }

  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;

    color: #000000;
  }

  div.content_section_text a:hover {
    background-color: #000000;

    color: #DCDFE6;
  }

  div.validator {
  }
    </style>
  </head>

  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/ubuntu-logo.png" alt="Ubuntu Logo"
             class="floating_element" />
        <span class="floating_element">
          Apache2 Ubuntu Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          Table of Contents
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div> -->

      <div class="content_section floating_element">

        <div class="section_header section_header_red">
          It works!
        </div>

        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct
                operation of the Apache2 server after installation on Ubuntu systems.
                It is based on the equivalent page on Debian, on which the Ubuntu Apache
                packaging is based.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>

          <p>
                If you are a normal user of this web site and don't know what this page is about,
                this probably means that the site is currently unavailable due to maintenance.
                If the problem persists, please contact the site's administrator.
          </p>

        </div>
        <div class="section_header">
          Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Ubuntu's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Ubuntu tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the
                <tt>apache2-doc</tt> package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Ubuntu systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <p>
                <tt>apache2.conf</tt> is the main configuration file. It puts the pieces together by including all
                remaining configuration files when starting up the web server.
          </p>
          <p>
                <tt>ports.conf</tt> is always included from the main
                configuration file. It is used to determine the listening ports for
                incoming connections, and this file can be customized anytime.
          </p>
          <p>
                Configuration files in the <tt>mods-enabled/</tt>,
                <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                particular configuration snippets which manage modules, global configuration
                fragments, or virtual host configurations, respectively.
          </p>
          <p>
                They are activated by symlinking 
[truncated]
```

`$ echo '== MOUNTS =='; cat /proc/mounts; echo '== ROOTDIRS =='; ls -la / /mnt /media /data /backup /var/backups /srv /opt /usr/local 2>/dev/null; echo '== APACHECONF =='; grep -R -Ein 'alias|documentroot|directory|include|listen|opr|oper|archive' /etc/apache2 /etc/nginx /etc/cron* /etc/systemd/system 2>/dev/null | head -300; echo '== RECENT =='; find / -xdev -type f -newermt '2023-01-01' -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -200`

```
root@ubuntu:~# echo '== MOUNTS =='; cat /proc/mounts; echo '== ROOTDIRS =='; ls -la / /mnt /media /data /backup /var/backups /srv /opt /usr/local 2>/dev/null; echo '== APACHECONF =='; grep -R -Ein 'alias|documentroot|directory|include|listen|opr|oper|archive' /etc/apache2 /etc/nginx /etc/cron* /etc/systemd/system 2>/dev/null | head -300; echo '== RECENT =='; find / -xdev -type f -newermt '2023-01-01' -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -200
== MOUNTS ==
/dev/mmcblk0p2 / ext4 rw,relatime,errors=remount-ro 0 0
proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0
sysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0
devtmpfs /dev devtmpfs rw,nosuid,relatime,size=363036112k,nr_inodes=90759028,mode=755 0 0
tmpfs /dev/shm tmpfs rw,nosuid,nodev,size=363036112k 0 0
tmpfs /run tmpfs rw,nosuid,nodev,size=72607280k,mode=755 0 0
tmpfs /run/lock tmpfs rw,nosuid,nodev,noexec,relatime,size=5120k 0 0
cgroup /sys/fs/cgroup tmpfs ro,nosuid,nodev,noexec,mode=755 0 0
cgroup /sys/fs/cgroup/systemd cgroup rw,nosuid,nodev,noexec,relatime,xattr,name=systemd 0 0
/dev/mmcblk0p1 /boot ext4 rw,relatime 0 0
== ROOTDIRS ==
/:
total 84
drwxr-xr-x  20 root root 4096 Oct 18 12:20 .
drwxr-xr-x  20 root root 4096 Oct 18 12:20 ..
lrwxrwxrwx   1 root root    7 Apr  9  2018 bin -> usr/bin
drwxr-xr-x   3 root root 4096 Oct 18 12:20 boot
drwxr-xr-x  17 root root 3880 Oct 18 12:20 dev
drwxr-xr-x 104 root root 4096 Oct 18 12:20 etc
drwxr-xr-x   2 root root 4096 Oct 18 12:20 home
lrwxrwxrwx   1 root root    7 Apr  9  2018 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr  9  2018 lib64 -> usr/lib64
drwxr-xr-x   2 root root 4096 Oct 18 12:20 media
drwxr-xr-x   2 root root 4096 Oct 18 12:20 mnt
drwxr-xr-x   2 root root 4096 Oct 18 12:20 opt
dr-xr-xr-x 206 root root    0 Oct 18 12:20 proc
drwx------   5 root root 4096 Oct 18 12:28 root
drwxr-xr-x  27 root root  880 Oct 18 12:21 run
lrwxrwxrwx   1 root root    8 Apr  9  2018 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Oct 18 12:20 srv
dr-xr-xr-x  12 root root    0 Oct 18 12:20 sys
drwxrwxrwt   2 root root 4096 Oct 18 12:20 tmp
drwxr-xr-x  10 root root 4096 Oct 18 12:20 usr
drwxr-xr-x  14 root root 4096 Oct 18 12:20 var

/media:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/usr/local:
total 20
drwxr-xr-x 10 root root 4096 Oct 18 12:20 .
drwxr-xr-x 10 root root 4096 Oct 18 12:20 ..
drwxr-xr-x  2 root root 4096 Oct 18 12:20 bin
drwxr-xr-x  2 root root 4096 Oct 18 12:20 etc
drwxr-xr-x  2 root root 4096 Oct 18 12:20 games
drwxr-xr-x  2 root root 4096 Oct 18 12:20 include
drwxr-xr-x  2 root root 4096 Oct 18 12:20 lib
drwxr-xr-x  2 root root 4096 Oct 18 12:20 man
drwxr-xr-x  2 root root 4096 Oct 18 12:20 sbin
drwxr-xr-x  2 root root 4096 Oct 18 12:20 share
drwxr-xr-x  2 root root 4096 Oct 18 12:20 src

/var/backups:
total 1208
drwxr-xr-x  2 root root   4096 Oct 18 12:20 .
drwxr-xr-x 14 root root   4096 Oct 18 12:20 ..
-rw-r--r--  1 root root  51200 Oct 18 12:20 apt.extended_states.0
-rw-r--r--  1 root root 941282 Oct 18 12:20 dpkg.status.0
== APACHECONF ==
/etc/apache2/apache2.conf:70:# ServerName gives the name and port that the server uses to identify itself.
/etc/apache2/apache2.conf:85:# These need to be set in /etc/apache2/envvars
/etc/apache2/apache2.conf:89:# Include module configuration:
/etc/apache2/apache2.conf:90:IncludeOptional mods-enabled/*.load
/etc/apache2/apache2.conf:91:IncludeOptional mods-enabled/*.conf
/etc/apache2/apache2.conf:102:<Directory />
/etc/apache2/apache2.conf:104:</Directory>
/etc/apache2/apache2.conf:107:<Directory /usr/share>
/etc/apache2/apache2.conf:111:</Directory>
/etc/apache2/apache2.conf:113:<Directory /var/www/>
/etc/apache2/apache2.conf:117:</Directory>
/etc/apache2/apache2.conf:120:AccessFileName .htaccess
/etc/apache2/apache2.conf:126:# Include of directories ignores editors' and dpkg's backup files,
/etc/apache2/apache2.conf:140:# Include the virtual host configurations:
/etc/apache2/apache2.conf:141:IncludeOptional conf-enabled/*.conf
/etc/apache2/apache2.conf:142:IncludeOptional sites-enabled/*.conf
/etc/apache2/ports.conf:5:Listen 80
/etc/apache2/sites-available/000-default.conf:1:<VirtualHost *:80>
/etc/apache2/sites-available/000-default.conf:12:	DocumentRoot /var/www/html
/etc/apache2/sites-available/default-ssl.conf:2:	<VirtualHost _default_:443>
/etc/apache2/sites-available/default-ssl.conf:5:		DocumentRoot /var/www/html
/etc/apache2/mods-available/alias.conf:2:# Aliases: Add here as many aliases as you need (with no limit). The format is
/etc/apache2/mods-available/alias.conf:7:# Alias /webpath /filesystem/path
/etc/apache2/mods-available/alias.conf:12:Alias /icons/ "/usr/share/apache2/icons/"
/etc/apache2/mods-available/alias.conf:18:ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
/etc/apache2/mods-enabled/alias.conf:2:# Aliases: Add here as many aliases as you need (with no limit). The format is
/etc/apache2/mods-enabled/alias.conf:7:# Alias /webpath /filesystem/path
/etc/apache2/mods-enabled/alias.conf:12:Alias /icons/ "/usr/share/apache2/icons/"
/etc/apache2/mods-enabled/alias.conf:18:ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
/etc/cron.d/e2scrub_all:4:30 3 * * 0 root test -e /run/systemd/system || SERVICE_MODE=1 /sbin/e2scrub_all -A -r
/etc/cron.d/e2scrub_all:5:10 3 * * * root test -e /run/systemd/system || SERVICE_MODE=1 /usr/lib/x86_64-linux-gnu/e2fsprogs/e2scrub_all_cron
/etc/systemd/system/multi-user.target.wants/apache2.service:9:After=network.target remote-fs.target nss-lookup.target
/etc/systemd/system/multi-user.target.wants/apache2.service:20:ExecStart=/usr/sbin/apachectl start
/etc/systemd/system/multi-user.target.wants/apache2.service:21:ExecStop=/usr/sbin/apachectl graceful-stop
/etc/systemd/system/multi-user.target.wants/apache2.service:22:ExecReload=/usr/sbin/apachectl graceful
== RECENT ==
2026-10-18 12:28 7485 /var/log/auth.log
2026-10-18 12:28 744 /root/.bash_history
2026-10-18 12:24 399 /root/.ssh/authorized_keys
2026-10-18 12:24 98 /var/log/apache2/access.log
2026-10-18 12:23 274 /root/.config/procps/toprc
2026-10-18 12:21 0 /root/.cache/motd.legal-displayed
2026-10-18 12:20 10918 /var/www/html/index.html
2026-10-18 12:20 941282 /var/backups/dpkg.status.0
2026-10-18 12:20 51200 /var/backups/apt.extended_states.0
2026-10-18 12:20 38417 /var/log/dpkg.log
2026-10-18 12:20 6419 /var/log/apt/term.log
2026-10-18 12:20 1457 /var/log/apt/history.log
2026-10-18 12:20 1163 /var/log/apache2/error.log
2026-10-18 12:20 1782 /etc/apache2/sites-available/000-default.conf
2026-10-18 12:20 1270 /etc/apache2/apache2.conf
2026-10-18 12:20 605 /var/lib/dpkg/info/apache2.postinst
2026-10-18 12:20 701 /var/lib/dpkg/info/apache2.prerm
2026-10-18 12:20 2564 /var/lib/dpkg/info/apache2.md5sums
2026-10-18 12:20 107 /var/lib/dpkg/info/apache2.list
2026-10-18 12:20 156 /var/lib/apache2/conf/enabled_by_maint
2026-10-18 12:20 84 /var/lib/apache2/module/disabled_by_maint
2026-10-18 12:20 4 /var/lib/apache2/site/enabled_by_admin
2026-10-18 12:20 1692 /etc/systemd/system/multi-user.target.wants/apache2.service
2026-10-18 12:20 178 /etc/apache2/ports.conf
2026-10-18 12:20 399 /etc/apache2/envvars
2026-10-18 12:20 67 /etc/apache2/mods-enabled/mpm_prefork.load
2026-10-18 12:20 78 /etc/apache2/mods-enabled/mpm_prefork.conf
2026-10-18 12:20 67 /etc/apache2/mods-enabled/alias.load
2026-10-18 12:20 359 /etc/apache2/mods-enabled/alias.conf
2026-10-18 12:20 65 /etc/apache2/mods-enabled/status.load
2026-10-18 12:20 65 /etc/apache2/mods-enabled/deflate.load
2026-10-18 12:20 320 /etc/apache2/mods-enabled/deflate.conf
2026-10-18 12:20 62 /etc/apache2/mods-enabled/autoindex.load
2026-10-18 12:20 114 /etc/apache2/mods-enabled/autoindex.conf
202
[truncated]
```

`$ ls -la /usr/lib/cgi-bin /var/lib/apache2 2>/dev/null; echo '---RECENT---'; find /usr /var /etc /home /root -xdev -type f -newermt '2024-01-01' \( -name '*.db' -o -name '*.sql' -o -name '*.tar*' -o -name '*.zip' -o -name '*.csv' -o -name '*opr*' -o -name '*ops*' -o -name '*archive*' -o -name '*dump*' \) 2>/dev/null | head -50; echo '---HIDDEN---'; find /var /usr/local /etc -xdev -name '.*' -type f 2>/dev/null | head -40`

```
root@ubuntu:~# ls -la /usr/lib/cgi-bin /var/lib/apache2 2>/dev/null; echo '---RECENT---'; find /usr /var /etc /home /root -xdev -type f -newermt '2024-01-01' \( -name '*.db' -o -name '*.sql' -o -name '*.tar*' -o -name '*.zip' -o -name '*.csv' -o -name '*opr*' -o -name '*ops*' -o -name '*archive*' -o -name '*dump*' \) 2>/dev/null | head -50; echo '---HIDDEN---'; find /var /usr/local /etc -xdev -name '.*' -type f 2>/dev/null | head -40
/usr/lib/cgi-bin:
total 8
drwxr-xr-x 2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 4 root root 4096 Oct 18 12:20 ..

/var/lib/apache2:
total 20
drwxr-xr-x 5 root root 4096 Oct 18 12:20 .
drwxr-xr-x 41 root root 4096 Oct 18 12:20 ..
drwxr-xr-x 2 root root 4096 Oct 18 12:20 conf
drwxr-xr-x 2 root root 4096 Oct 18 12:20 module
drwxr-xr-x 2 root root 4096 Oct 18 12:20 site
---RECENT---
---HIDDEN---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root /home /tmp /var/spool 2>/dev/null; echo '---CRON---'; crontab -l 2>/dev/null; ls -la /etc/cron* /var/spool/cron 2>/dev/null; echo '---TIMERS---'; systemctl list-timers --all --no-pager 2>/dev/null; echo '---RECENT---'; find /root /home /tmp /var/spool -maxdepth 4 -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -80`

```
root@ubuntu:~# ls -la /root /home /tmp /var/spool 2>/dev/null; echo '---CRON---'; crontab -l 2>/dev/null; ls -la /etc/cron* /var/spool/cron 2>/dev/null; echo '---TIMERS---'; systemctl list-timers --all --no-pager 2>/dev/null; echo '---RECENT---'; find /root /home /tmp /var/spool -maxdepth 4 -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -80
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/root:
total 32
drwx------  5 root root 4096 Oct 18 12:28 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..
-rw-------  1 root root  744 Oct 18 12:27 .bash_history
-rw-r--r--  1 root root  220 Apr  9  2018 .bash_logout
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 12:21 .cache
drwxr-xr-x  3 root root 4096 Oct 18 12:23 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 12:24 .ssh

/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/var/spool:
total 12
drwxr-xr-x  3 root root 4096 Oct 18 12:20 .
drwxr-xr-x 14 root root 4096 Oct 18 12:20 ..
drwxr-xr-x  2 root root 4096 Oct 18 12:20 cron
---CRON---
/etc/crontab

/etc/cron.d:
total 16
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..
-rw-r--r--   1 root root  201 Feb 13  2023 e2scrub_all
-rw-r--r--   1 root root  712 Jan 16  2023 php

/etc/cron.daily:
total 32
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..
-rwxr-xr-x   1 root root  539 Feb 13  2023 apache2
-rwxr-xr-x   1 root root 1478 Apr 17  2018 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root  372 Jan 18  2018 dpkg
-rwxr-xr-x   1 root root  377 Aug 24  2021 logrotate
-rwxr-xr-x   1 root root 1123 May 25  2022 man-db

/etc/cron.hourly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..

/etc/cron.monthly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..

/etc/cron.weekly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..

/etc/cron.yearly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 104 root root 4096 Oct 18 12:20 ..

/var/spool/cron:
total 8
drwxr-xr-x 2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 3 root root 4096 Oct 18 12:20 ..
---TIMERS---
NEXT                         LEFT          LAST                         PASSED       UNIT                         ACTIVATES
Sun 2026-10-18 12:30:00 UTC  1min 46s left Sun 2026-10-18 12:20:01 UTC  8min ago     systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Sun 2026-10-18 18:19:00 UTC  5h 50min left n/a                          n/a          apt-daily.timer              apt-daily.service
Mon 2026-10-19 06:12:00 UTC  17h left      n/a                          n/a          apt-daily-upgrade.timer      apt-daily-upgrade.service
Mon 2026-10-19 00:00:00 UTC  11h left      n/a                          n/a          logrotate.timer              logrotate.service
Mon 2026-10-19 00:00:00 UTC  11h left      n/a                          n/a          man-db.timer                 man-db.service
n/a                          n/a           n/a                          n/a          e2scrub_all.timer            e2scrub_all.service

6 timers listed.
---RECENT---
2026-10-18 12:28 744 /root/.bash_history
2026-10-18 12:24 399 /root/.ssh/authorized_keys
2026-10-18 12:23 274 /root/.config/procps/toprc
2026-10-18 12:21 0 /root/.cache/motd.legal-displayed
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history; echo '---'; ls -la /opt /srv /usr/local 2>&1; echo '---'; grep -rIl -E 'OPR-|OPS-' /opt /srv /usr/local /etc /var 2>/dev/null | head -40`

```
root@ubuntu:~# cat /root/.bash_history; echo '---'; ls -la /opt /srv /usr/local 2>&1; echo '---'; grep -rIl -E 'OPR-|OPS-' /opt /srv /usr/local /etc /var 2>/dev/null | head -40
apt update
apt install -y apache2
systemctl enable apache2
systemctl start apache2
ip addr show
ss -lntp
journalctl -u apache2 --no-pager -n 50
cat /etc/os-release
uname -a
exit
---
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 12:20 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..

/usr/local:
total 20
drwxr-xr-x 10 root root 4096 Oct 18 12:20 .
drwxr-xr-x 10 root root 4096 Oct 18 12:20 ..
drwxr-xr-x  2 root root 4096 Oct 18 12:20 bin
drwxr-xr-x  2 root root 4096 Oct 18 12:20 etc
drwxr-xr-x  2 root root 4096 Oct 18 12:20 games
drwxr-xr-x  2 root root 4096 Oct 18 12:20 include
drwxr-xr-x  2 root root 4096 Oct 18 12:20 lib
drwxr-xr-x  2 root root 4096 Oct 18 12:20 man
drwxr-xr-x  2 root root 4096 Oct 18 12:20 sbin
drwxr-xr-x  2 root root 4096 Oct 18 12:20 share
drwxr-xr-x  2 root root 4096 Oct 18 12:20 src
---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ mount; echo '---ROOT---'; ls -la /root /root/.cache /root/.config 2>/dev/null; echo '---VARLIB---'; find /var/lib -maxdepth 3 -type f -printf '%p %s\n' 2>/dev/null | head -200; echo '---DELETED---'; find /proc/[0-9]*/fd -lname '*deleted*' -ls 2>/dev/null | head -50; echo '---DF---'; df -hT 2>/dev/null`

```
root@ubuntu:~# mount; echo '---ROOT---'; ls -la /root /root/.cache /root/.config 2>/dev/null; echo '---VARLIB---'; find /var/lib -maxdepth 3 -type f -printf '%p %s\n' 2>/dev/null | head -200; echo '---DELETED---'; find /proc/[0-9]*/fd -lname '*deleted*' -ls 2>/dev/null | head -50; echo '---DF---'; df -hT 2>/dev/null
/dev/mmcblk0p2 on / type ext4 (rw,relatime,errors=remount-ro)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,relatime,size=363036112k,nr_inodes=90759028,mode=755)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,size=363036112k)
tmpfs on /run type tmpfs (rw,nosuid,nodev,size=72607280k,mode=755)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
cgroup on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,name=systemd)
/dev/mmcblk0p1 on /boot type ext4 (rw,relatime)
---ROOT---
/root:
total 32
drwx------  5 root root 4096 Oct 18 12:28 .
drwxr-xr-x 20 root root 4096 Oct 18 12:20 ..
-rw-------  1 root root  744 Oct 18 12:27 .bash_history
-rw-r--r--  1 root root  220 Apr  9  2018 .bash_logout
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 12:21 .cache
drwxr-xr-x  3 root root 4096 Oct 18 12:23 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 12:24 .ssh

/root/.cache:
total 8
drwx------ 2 root root 4096 Oct 18 12:21 .
drwx------ 5 root root 4096 Oct 18 12:28 ..
-rw-r--r-- 1 root root    0 Oct 18 12:21 motd.legal-displayed

/root/.config:
total 12
drwxr-xr-x 3 root root 4096 Oct 18 12:23 .
drwx------ 5 root root 4096 Oct 18 12:28 ..
drwx------ 3 root root 4096 Oct 18 12:23 procps
---VARLIB---
/var/lib/apt/extended_states 51200
/var/lib/apt/lists/lock 0
/var/lib/apt/lists/partial/.keep 0
/var/lib/dpkg/available 0
/var/lib/dpkg/status 941282
/var/lib/dpkg/status-old 941282
/var/lib/dpkg/diversions 104
/var/lib/dpkg/diversions-old 104
/var/lib/dpkg/lock 0
/var/lib/dpkg/lock-frontend 0
/var/lib/dpkg/statoverride 0
/var/lib/dpkg/statoverride-old 0
/var/lib/dpkg/triggers/File 52
/var/lib/dpkg/triggers/Lock 0
/var/lib/dpkg/triggers/Unincorp 0
/var/lib/dpkg/info/apache2.list 107
/var/lib/dpkg/info/apache2.md5sums 2564
/var/lib/dpkg/info/apache2.postinst 605
/var/lib/dpkg/info/apache2.prerm 701
/var/lib/dpkg/info/apache2-bin.list 186
/var/lib/dpkg/info/apache2-bin.md5sums 4621
/var/lib/dpkg/info/apache2-data.list 980
/var/lib/dpkg/info/apache2-data.md5sums 25372
/var/lib/apache2/conf/enabled_by_maint 156
/var/lib/apache2/module/disabled_by_maint 84
/var/lib/apache2/site/enabled_by_admin 4
/var/lib/systemd/random-seed 512
/var/lib/systemd/timesync/clock 8
/var/lib/ubuntu-advantage/private/machine-access-cc 0
---DELETED---
---DF---
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/mmcblk0p2 ext4    40G  2.1G   36G   6% /
tmpfs          tmpfs  347G     0  347G   0% /dev/shm
tmpfs          tmpfs   70G  1.1M   70G   1% /run
tmpfs          tmpfs  5.0M     0  5.0M   0% /run/lock
/dev/mmcblk0p1 ext4   511M   59M  453M  12% /boot
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ grep -RInaE 'OPR-|OPS-|opr_evidence|operational[_ -]?record|ora_dump' /etc /var /home /root /opt /srv /usr/local /usr/share 2>/dev/null | head -200`

```
root@ubuntu:~# grep -RInaE 'OPR-|OPS-|opr_evidence|operational[_ -]?record|ora_dump' /etc /var /home /root /opt /srv /usr/local /usr/share 2>/dev/null | head -200
root@ubuntu:~# 
```
root@ubuntu:~# 
```
