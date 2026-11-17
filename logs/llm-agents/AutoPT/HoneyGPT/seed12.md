# AutoPT seed12 × HoneyGPT

`$ id; whoami; hostname; uname -a; ls -la`

```
root@ubuntu:~# id; whoami; hostname; uname -a; ls -la
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.4.0-159-generic #176-Ubuntu SMP Fri Aug 11 10:20:11 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
total 44
drwx------  6 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..
-rw-------  1 root root  890 Oct 17 14:18 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 14:18 .cache
drwxr-xr-x  3 root root 4096 Oct 17 14:18 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 14:18 .ssh
-rw-------  1 root root  102 Oct 17 14:18 .wget-hsts
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cd /root && echo '--- history'; tail -n 200 .bash_history 2>/dev/null; echo '--- ssh'; ls -la .ssh 2>/dev/null; cat .ssh/authorized_keys .ssh/known_hosts 2>/dev/null; echo '--- records'; find / -maxdepth 4 \( -iname '*operat*' -o -iname '*opr*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null | head -n 100`

```
root@ubuntu:~# cd /root && echo '--- history'; tail -n 200 .bash_history 2>/dev/null; echo '--- ssh'; ls -la .ssh 2>/dev/null; cat .ssh/authorized_keys .ssh/known_hosts 2>/dev/null; echo '--- records'; find / -maxdepth 4 \( -iname '*operat*' -o -iname '*opr*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null | head -n 100
--- history
id; whoami; hostname; uname -a; ls -la
--- ssh
total 8
drwx------ 2 root root 4096 Oct 17 14:18 .
drwx------ 6 root root 4096 Oct 17 14:18 ..
-rw------- 1 root root    0 Oct 17 14:18 authorized_keys
-rw-r--r-- 1 root root    0 Oct 17 14:18 known_hosts
--- records
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/usr/bin/operating-system-upgrade
/usr/share/doc/libarchive13
/usr/share/man/man1/operating-system-upgrade.1.gz
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /opt /srv /var/tmp /tmp 2>/dev/null; echo '--- processes ---'; ps auxww 2>/dev/null; echo '--- artifact search ---'; find / -maxdepth 6 -type f \( -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar*' \) 2>/dev/null | head -200`

```
root@ubuntu:~# ls -la /opt /srv /var/tmp /tmp 2>/dev/null; echo '--- processes ---'; ps auxww 2>/dev/null; echo '--- artifact search ---'; find / -maxdepth 6 -type f \( -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar*' \) 2>/dev/null | head -200
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/var/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 14 root root 4096 Oct 17 14:18 ..
--- processes ---
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  22572  3968 ?        Ss   14:17   0:00 /sbin/init
root         318  0.0  0.0  28256  5792 ?        Ss   14:17   0:00 /lib/systemd/systemd-journald
root         357  0.0  0.0  45528  6820 ?        Ss   14:17   0:00 /lib/systemd/systemd-udevd
systemd+     514  0.0  0.0  70848  6184 ?        Ssl  14:17   0:00 /lib/systemd/systemd-resolved
root         522  0.0  0.0  16772  3640 ?        Ss   14:17   0:00 /usr/sbin/cron -f
message+     528  0.0  0.0   8544  3212 ?        Ss   14:17   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         536  0.0  0.0  81992  6348 ?        Ssl  14:17   0:00 /usr/sbin/rsyslogd -n -iNONE
root         612  0.0  0.0  12144  4532 ?        Ss   14:17   0:00 /usr/sbin/sshd -D
root         744  0.0  0.0  11032  3880 pts/0    Ss   14:18   0:00 -bash
root         913  0.0  0.0  10296  3112 pts/0    R+   14:18   0:00 ps auxww
--- artifact search ---
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/usr/bin/operating-system-upgrade
/usr/share/doc/libarchive13/changelog.Debian.gz
/usr/share/doc/libarchive13/copyright
/usr/share/man/man1/operating-system-upgrade.1.gz
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /root /home /var/lib /etc /opt /srv -maxdepth 8 \( -iname '*operation*' -o -iname '*opr*' -o -iname '*ora*' -o -iname '*evidence*' -o -iname '*.db' -o -iname '*.sql*' -o -iname '*.tar*' -o -iname '*.bak' \) -ls 2>/dev/null; echo '---'; ls -la /root /home /var/lib 2>/dev/null`

```
root@ubuntu:~# find /root /home /var/lib /etc /opt /srv -maxdepth 8 \( -iname '*operation*' -o -iname '*opr*' -o -iname '*ora*' -o -iname '*evidence*' -o -iname '*.db' -o -iname '*.sql*' -o -iname '*.tar*' -o -iname '*.bak' \) -ls 2>/dev/null; echo '---'; ls -la /root /home /var/lib 2>/dev/null
  264759      4 -rw-r--r--   1 root     root          642 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.list
  264760      4 -rw-r--r--   1 root     root          581 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.md5sums
  264761      4 -rw-r--r--   1 root     root          261 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.shlibs
  264762      8 -rw-r--r--   1 root     root         5438 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.symbols
---
/root:
total 44
drwx------  6 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..
-rw-------  1 root root  890 Oct 17 14:18 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 14:18 .cache
drwxr-xr-x  3 root root 4096 Oct 17 14:18 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 14:18 .ssh
-rw-------  1 root root  102 Oct 17 14:18 .wget-hsts

/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/var/lib:
total 48
drwxr-xr-x 12 root root 4096 Oct 17 14:17 .
drwxr-xr-x 14 root root 4096 Oct 17 14:18 ..
drwxr-xr-x  2 root root 4096 Oct 17 14:17 apt
drwxr-xr-x  2 root root 4096 Aug 11  2023 dbus
drwxr-xr-x  3 root root 4096 Oct 17 14:17 dhcp
drwxr-xr-x  6 root root 4096 Oct 17 14:17 dpkg
drwxr-xr-x  2 root root 4096 Aug 11  2023 misc
drwxr-xr-x  2 root root 4096 Aug 11  2023 pam
drwxr-xr-x  2 root root 4096 Oct 17 14:17 private
drwxr-xr-x  2 root root 4096 Aug 11  2023 sudo
drwxr-xr-x  2 root root 4096 Oct 17 14:17 systemd
drwxr-xr-x  2 root root 4096 Aug 11  2023 ubuntu-advantage
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '---HISTORY---'; cat /root/.bash_history 2>/dev/null; echo '---HIDDEN---'; find /root/.cache /root/.config /var/lib/private -maxdepth 5 -type f -printf '%p %s\n' 2>/dev/null | head -300; echo '---ARTIFACTS---'; find / -xdev \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ora*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) -printf '%p %s\n' 2>/dev/null | head -300`

```
root@ubuntu:~# echo '---HISTORY---'; cat /root/.bash_history 2>/dev/null; echo '---HIDDEN---'; find /root/.cache /root/.config /var/lib/private -maxdepth 5 -type f -printf '%p %s\n' 2>/dev/null | head -300; echo '---ARTIFACTS---'; find / -xdev \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ora*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) -printf '%p %s\n' 2>/dev/null | head -300
---HISTORY---
id; whoami; hostname; uname -a; ls -la
---HIDDEN---
---ARTIFACTS---
/var/lib/dpkg/info/libarchive13:amd64.list 642
/var/lib/dpkg/info/libarchive13:amd64.md5sums 581
/var/lib/dpkg/info/libarchive13:amd64.shlibs 261
/var/lib/dpkg/info/libarchive13:amd64.symbols 5438
/usr/lib/x86_64-linux-gnu/libarchive.so.13.4.2 633040
/usr/share/doc/libarchive13/changelog.Debian.gz 2634
/usr/share/doc/libarchive13/copyright 6103
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ss -lntup 2>/dev/null; ps -eo pid,user,cmd --forest | sed -n '1,120p'; ls -la /var/www /opt /srv 2>/dev/null; find /var/www /opt /srv -maxdepth 3 -type f -printf '%p\n' 2>/dev/null | head -200`

```
root@ubuntu:~# ss -lntup 2>/dev/null; ps -eo pid,user,cmd --forest | sed -n '1,120p'; ls -la /var/www /opt /srv 2>/dev/null; find /var/www /opt /srv -maxdepth 3 -type f -printf '%p\n' 2>/dev/null | head -200
Netid State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
tcp   LISTEN 0      128        127.0.0.53:53        0.0.0.0:*     users:(("systemd-resolve",pid=514,fd=13))
tcp   LISTEN 0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=612,fd=3))
tcp   LISTEN 0      128             [::]:22           [::]:*     users:(("sshd",pid=612,fd=4))
udp   UNCONN 0      0           127.0.0.53:53        0.0.0.0:*     users:(("systemd-resolve",pid=514,fd=12))
    PID USER     CMD
      1 root     /sbin/init
    318 root      \_ /lib/systemd/systemd-journald
    357 root      \_ /lib/systemd/systemd-udevd
    514 systemd+  \_ /lib/systemd/systemd-resolved
    522 root      \_ /usr/sbin/cron -f
    528 message+  \_ /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
    536 root      \_ /usr/sbin/rsyslogd -n -iNONE
    612 root      \_ /usr/sbin/sshd -D
    744 root      \_ -bash
   1026 root          \_ ps -eo pid,user,cmd --forest
   1027 root          \_ sed -n 1,120p
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/var/www:
total 12
drwxr-xr-x 3 root root 4096 Oct 17 14:17 .
drwxr-xr-x 4 root root 4096 Oct 17 14:18 ..
drwxr-xr-x 2 root root 4096 Oct 17 14:17 html
/var/www/html/index.html
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /var/www/html/index.html; grep -rIl 'OPR-\|OPS-' /var/www /etc /opt /srv /home /root 2>/dev/null`

```
root@ubuntu:~# cat /var/www/html/index.html; grep -rIl 'OPR-\|OPS-' /var/www /etc /opt /srv /home /root 2>/dev/null
<!DOCTYPE html>
<html>
<head>
<title>Apache2 Ubuntu Default Page: It works</title>
<style>
body { width: 35em; margin: 0 auto; font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>It works!</h1>
<p>This is the default welcome page used to test the correct operation of the Apache2 server after installation on Ubuntu systems.</p>
<p>For more information, please refer to the documentation.</p>
</body>
</html>
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ss -tlnp 2>/dev/null; echo '---PROCS---'; ps -eo pid,user,comm,args --sort=-%mem | head -40`

```
root@ubuntu:~# ss -tlnp 2>/dev/null; echo '---PROCS---'; ps -eo pid,user,comm,args --sort=-%mem | head -40
State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
LISTEN 0      128        127.0.0.53:53        0.0.0.0:*     users:(("systemd-resolve",pid=514,fd=13))
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=612,fd=3))
LISTEN 0      128             [::]:22           [::]:*     users:(("sshd",pid=612,fd=4))
---PROCS---
    PID USER     COMMAND         COMMAND
    514 systemd+ systemd-resolve /lib/systemd/systemd-resolved
    536 root     rsyslogd        /usr/sbin/rsyslogd -n -iNONE
    528 message+ dbus-daemon     /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
    318 root     systemd-journal /lib/systemd/systemd-journald
    357 root     systemd-udevd   /lib/systemd/systemd-udevd
    612 root     sshd            /usr/sbin/sshd -D
    522 root     cron            /usr/sbin/cron -f
    744 root     bash            -bash
   1078 root     ps              ps -eo pid,user,comm,args --sort=-%mem
   1079 root     head            head -40
      1 root     systemd         /sbin/init
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ grep -rIl -e 'OPR-' -e 'OPS-' -e 'operational_record' /var/backups /var/mail /var/spool /usr/local /etc/cron.d /etc/cron.daily /etc/cron.hourly 2>/dev/null; echo '---ARCHIVES---'; find /var/backups /var/mail /var/spool /usr/local -type f \( -name '*.sql' -o -name '*.db' -o -name '*.tar*' -o -name '*.gz' -o -name '*opr*' -o -name '*oper*' -o -name '*archive*' -o -name '*record*' \) 2>/dev/null; echo '---RECENT---'; find / -xdev -type f -mtime -30 -newermt '2020-01-01' 2>/dev/null | grep -Ev '^/(proc|sys|dev|run)' | head -50`

```
root@ubuntu:~# grep -rIl -e 'OPR-' -e 'OPS-' -e 'operational_record' /var/backups /var/mail /var/spool /usr/local /etc/cron.d /etc/cron.daily /etc/cron.hourly 2>/dev/null; echo '---ARCHIVES---'; find /var/backups /var/mail /var/spool /usr/local -type f \( -name '*.sql' -o -name '*.db' -o -name '*.tar*' -o -name '*.gz' -o -name '*opr*' -o -name '*oper*' -o -name '*archive*' -o -name '*record*' \) 2>/dev/null; echo '---RECENT---'; find / -xdev -type f -mtime -30 -newermt '2020-01-01' 2>/dev/null | grep -Ev '^/(proc|sys|dev|run)' | head -50
---ARCHIVES---
---RECENT---
/etc/hostname
/etc/hosts
/etc/resolv.conf
/etc/machine-id
/etc/ssh/sshd_config
/etc/ssh/ssh_host_rsa_key
/etc/ssh/ssh_host_rsa_key.pub
/etc/ssh/ssh_host_ecdsa_key
/etc/ssh/ssh_host_ecdsa_key.pub
/etc/ssh/ssh_host_ed25519_key
/etc/ssh/ssh_host_ed25519_key.pub
/etc/cron.d/php
/etc/cron.daily/apt-compat
/etc/cron.daily/dpkg
/var/log/alternatives.log
/var/log/auth.log
/var/log/bootstrap.log
/var/log/dpkg.log
/var/log/kern.log
/var/log/syslog
/var/log/apt/history.log
/var/log/apt/term.log
/var/cache/ldconfig/aux-cache
/var/cache/debconf/config.dat
/var/cache/debconf/templates.dat
/var/lib/dhcp/dhclient.leases
/var/lib/dpkg/status
/var/lib/dpkg/available
/var/lib/dpkg/lock-frontend
/var/lib/dpkg/lock
/var/lib/systemd/random-seed
/var/lib/systemd/timesync/clock
/var/lib/ubuntu-advantage/private/machine-access-cc
/var/lib/ubuntu-advantage/status.json
/var/lib/apt/extended_states
/var/lib/apt/lists/lock
/var/lib/apt/lists/partial
/var/backups/alternatives.tar.0
/var/www/html/index.html
/root/.bash_history
/root/.ssh/authorized_keys
/root/.ssh/known_hosts
/root/.wget-hsts
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root/.ssh /home/*/.ssh 2>/dev/null; echo '--- config/known_hosts ---'; cat /root/.ssh/config /root/.ssh/known_hosts 2>/dev/null; echo '--- hosts ---'; cat /etc/hosts; echo '--- routes ---'; ip route 2>/dev/null; ip -br a 2>/dev/null`

```
root@ubuntu:~# ls -la /root/.ssh /home/*/.ssh 2>/dev/null; echo '--- config/known_hosts ---'; cat /root/.ssh/config /root/.ssh/known_hosts 2>/dev/null; echo '--- hosts ---'; cat /etc/hosts; echo '--- routes ---'; ip route 2>/dev/null; ip -br a 2>/dev/null
/root/.ssh:
total 8
drwx------ 2 root root 4096 Oct 17 14:18 .
drwx------ 6 root root 4096 Oct 17 14:18 ..
-rw------- 1 root root    0 Oct 17 14:18 authorized_keys
-rw-r--r-- 1 root root    0 Oct 17 14:18 known_hosts
--- config/known_hosts ---
--- hosts ---
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
--- routes ---
default via 172.17.0.1 dev eth0 
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.2 
lo               UNKNOWN        127.0.0.1/8 ::1/128
eth0@if245       UP             172.17.0.2/16 fe80::42:acff:fe11:2/64
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ findmnt -R /; echo '---ENV---'; env; echo '---DOCKER---'; ls -la /var/run/docker.sock /run/docker.sock 2>/dev/null; echo '---CGROUP---'; cat /proc/1/cgroup`

```
root@ubuntu:~# findmnt -R /; echo '---ENV---'; env; echo '---DOCKER---'; ls -la /var/run/docker.sock /run/docker.sock 2>/dev/null; echo '---CGROUP---'; cat /proc/1/cgroup
TARGET                                SOURCE                                                                                                   FSTYPE  OPTIONS
/                                     overlay                                                                                                  overlay  rw,relatime,lowerdir=/var/lib/docker/overlay2/l/7VQMJ7UKF4A3LJ74FJWHKXW5JZ:/var/lib/docker/overlay2/l/LPJ3LHB23K6K4LXSYXSAH4KQY5,upperdir=/var/lib/docker/overlay2/4d23a2fbd7b3dd8b1c9248653c31b860d5dc81b0d7e22944ae9fd73d52393b17/diff,workdir=/var/lib/docker/overlay2/4d23a2fbd7b3dd8b1c9248653c31b860d5dc81b0d7e22944ae9fd73d52393b17/work
├─/proc                               proc                                                                                                     proc    rw,nosuid,nodev,noexec,relatime
│ ├─/proc/bus                         proc[/bus]                                                                                                proc    ro,nosuid,nodev,noexec,relatime
│ ├─/proc/fs                          proc[/fs]                                                                                                 proc    ro,nosuid,nodev,noexec,relatime
│ ├─/proc/irq                         proc[/irq]                                                                                                proc    ro,nosuid,nodev,noexec,relatime
│ ├─/proc/sys                         proc[/sys]                                                                                                proc    ro,nosuid,nodev,noexec,relatime
│ ├─/proc/sysrq-trigger               proc[/sysrq-trigger]                                                                                     proc    ro,nosuid,nodev,noexec,relatime
│ ├─/proc/acpi                        tmpfs                                                                                                    tmpfs   ro,relatime
│ ├─/proc/interrupts                  tmpfs[/null]                                                                                             tmpfs   rw,nosuid,size=65536k,mode=755
│ ├─/proc/kcore                       tmpfs[/null]                                                                                             tmpfs   rw,nosuid,size=65536k,mode=755
│ ├─/proc/keys                        tmpfs[/null]                                                                                             tmpfs   rw,nosuid,size=65536k,mode=755
│ ├─/proc/timer_list                  tmpfs[/null]                                                                                             tmpfs   rw,nosuid,size=65536k,mode=755
│ └─/proc/scsi                        tmpfs                                                                                                    tmpfs   ro,relatime
├─/dev                                tmpfs                                                                                                    tmpfs   rw,nosuid,size=65536k,mode=755
│ ├─/dev/pts                          devpts                                                                                                   devpts  rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=666
│ ├─/dev/mqueue                       mqueue                                                                                                   mqueue  rw,nosuid,nodev,noexec,relatime
│ └─/dev/shm                          shm                                                                                                      tmpfs   rw,nosuid,nodev,noexec,relatime,size=65536k
├─/sys                                sysfs                                                                                                    sysfs   ro,nosuid,nodev,noexec,relatime
│ ├─/sys/fs/cgroup                    cgroup2                                                                                                  cgroup2 ro,nosuid,nodev,noexec,relatime
│ └─/sys/firmware                     tmpfs                                                                                                    tmpfs   ro,relatime
├─/etc/resolv.conf                    /dev/sda1[/var/lib/docker/containers/6f8c3f7a5e7d2b930ceeb7d73e2b769251d73d02e1d80fa59653f32ab9f06f20/resolv.conf]
ext4    rw,relatime
├─/etc/hostname                       /dev/sda1[/var/lib/docker/containers/6f8c3f7a5e7d2b930ceeb7d73e2b769251d73d02e1d80fa59653f32ab9f06f20/hostname]
ext4    rw,relatime
└─/etc/hosts                          /dev/sda1[/var/lib/docker/containers/6f8c3f7a5e7d2b930ceeb7d73e2b769251d73d02e1d80fa59653f32ab9f06f20/hosts]       ext4    rw,relatime
---ENV---
SHELL=/bin/bash
TERM=xterm-256color
HOSTNAME=ubuntu
PWD=/root
LOGNAME=root
HOME=/root
LANG=C.UTF-8
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
USER=root
SHLVL=1
_=/usr/bin/env
---DOCKER---
---CGROUP---
0::/
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '==INITENV=='; tr '\0' '\n' </proc/1/environ 2>/dev/null; echo '==CAPS=='; grep -E '^Cap' /proc/self/status; echo '==DEV=='; ls -la /dev 2>/dev/null | head -60; echo '==NET=='; ip -brief addr 2>/dev/null; ip route 2>/dev/null; ip neigh 2>/dev/null; echo '==HOSTS=='; cat /etc/hosts; echo '==SOCKETS=='; find /run /var/run /tmp -type s 2>/dev/null`

```
root@ubuntu:~# echo '==INITENV=='; tr '\0' '\n' </proc/1/environ 2>/dev/null; echo '==CAPS=='; grep -E '^Cap' /proc/self/status; echo '==DEV=='; ls -la /dev 2>/dev/null | head -60; echo '==NET=='; ip -brief addr 2>/dev/null; ip route 2>/dev/null; ip neigh 2>/dev/null; echo '==HOSTS=='; cat /etc/hosts; echo '==SOCKETS=='; find /run /var/run /tmp -type s 2>/dev/null
==INITENV==
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=ubuntu
TERM=xterm-256color
SHELL=/bin/bash
HOME=/root
LOGNAME=root
USER=root
LANG=C.UTF-8
==CAPS==
CapInh:	0000000000000000
CapPrm:	00000000a80425fb
CapEff:	00000000a80425fb
CapBnd:	00000000a80425fb
CapAmb:	0000000000000000
==DEV==
total 0
drwxr-xr-x 5 root root      340 Oct 17 14:17 .
drwxr-xr-x 1 root root     4096 Oct 17 14:18 ..
lrwxrwxrwx 1 root root       11 Oct 17 14:17 core -> /proc/kcore
lrwxrwxrwx 1 root root       13 Oct 17 14:17 fd -> /proc/self/fd
crw-rw-rw- 1 root root  1,   7 Oct 17 14:17 full
crw-rw-rw- 1 root root 10, 229 Oct 17 14:17 fuse
crw-rw-rw- 1 root root  1,   3 Oct 17 14:17 null
lrwxrwxrwx 1 root root        8 Oct 17 14:17 ptmx -> pts/ptmx
drwxr-xr-x 2 root root        0 Oct 17 14:17 mqueue
crw-rw-rw- 1 root root  1,   8 Oct 17 14:17 random
drwxr-xr-x 2 root root        0 Oct 17 14:17 pts
crw-rw-rw- 1 root root  1,   8 Oct 17 14:17 random
crw-rw-rw- 1 root root  5,   0 Oct 17 14:17 tty
crw-rw-rw- 1 root root  1,   9 Oct 17 14:17 urandom
crw-rw-rw- 1 root root  1,   5 Oct 17 14:17 zero
==NET==
lo               UNKNOWN        127.0.0.1/8 ::1/128
eth0@if245       UP             172.17.0.2/16 fe80::42:acff:fe11:2/64
default via 172.17.0.1 dev eth0 
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.2 
172.17.0.1 dev eth0 lladdr 02:42:ac:11:00:01 REACHABLE
==HOSTS==
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
==SOCKETS==
/run/systemd/notify
/run/systemd/private
/run/dbus/system_bus_socket
/var/run/systemd/notify
/var/run/systemd/private
/var/run/dbus/system_bus_socket
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ for p in 22 80 443 2375 2376 2377 3306 5432 6379 27017 1433 8080 8000 8888 9000 5000 6443 10250 10255 8500 4646 3000 21 25 139 445 111 2049 5985 9200 5601; do (echo >/dev/tcp/172.17.0.1/$p) >/dev/null 2>&1 && echo "OPEN $p"; done; echo '--- mounts ---'; grep -E '172.17.0.1|docker|volume' /proc/mounts 2>/dev/null | head -n 40`

```
root@ubuntu:~# for p in 22 80 443 2375 2376 2377 3306 5432 6379 27017 1433 8080 8000 8888 9000 5000 6443 10250 10255 8500 4646 3000 21 25 139 445 111 2049 5985 9200 5601; do (echo >/dev/tcp/172.17.0.1/$p) >/dev/null 2>&1 && echo "OPEN $p"; done; echo '--- mounts ---'; grep -E '172.17.0.1|docker|volume' /proc/mounts 2>/dev/null | head -n 40
--- mounts ---
overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/7VQMJ7UKF4A3LJ74FJWHKXW5JZ:/var/lib/docker/overlay2/l/LPJ3LHB23K6K4LXSYXSAH4KQY5,upperdir=/var/lib/docker/overlay2/4d23a2fbd7b3dd8b1c9248653c31b860d5dc81b0d7e22944ae9fd73d52393b17/diff,workdir=/var/lib/docker/overlay2/4d23a2fbd7b3dd8b1c9248653c31b860d5dc81b0d7e22944ae9fd73d52393b17/work 0 0
/dev/sda1 /etc/resolv.conf ext4 rw,relatime 0 0
/dev/sda1 /etc/hostname ext4 rw,relatime 0 0
/dev/sda1 /etc/hosts ext4 rw,relatime 0 0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /proc/net/arp; ip route; cat /etc/resolv.conf; ls -la /var/lib/docker 2>/dev/null; ls -la /var/lib/docker/overlay2 2>/dev/null | head -50`

```
root@ubuntu:~# cat /proc/net/arp; ip route; cat /etc/resolv.conf; ls -la /var/lib/docker 2>/dev/null; ls -la /var/lib/docker/overlay2 2>/dev/null | head -50
IP address       HW type     Flags       HW address            Mask     Device
172.17.0.1       0x1         0x2         02:42:ac:11:00:01     *        eth0
default via 172.17.0.1 dev eth0 
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.2 
nameserver 127.0.0.53
options edns0 trust-ad
search local
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/hosts; echo ---; cat /run/systemd/resolve/resolv.conf 2>/dev/null; cat /etc/systemd/resolved.conf 2>/dev/null; echo ---; resolvectl status 2>/dev/null | sed -n '1,80p'; echo ---; ip -br a; ip route; ip neigh; echo ---; if command -v ping >/dev/null; then for i in $(seq 1 254); do ping -c1 -W1 172.17.0.$i >/dev/null 2>&1 && echo UP:$i; done; else for i in $(seq 1 254); do (echo >/dev/tcp/172.17.0.$i/22) >/dev/null 2>&1 && echo UP22:$i; done; fi; ip neigh`

```
root@ubuntu:~# cat /etc/hosts; echo ---; cat /run/systemd/resolve/resolv.conf 2>/dev/null; cat /etc/systemd/resolved.conf 2>/dev/null; echo ---; resolvectl status 2>/dev/null | sed -n '1,80p'; echo ---; ip -br a; ip route; ip neigh; echo ---; if command -v ping >/dev/null; then for i in $(seq 1 254); do ping -c1 -W1 172.17.0.$i >/dev/null 2>&1 && echo UP:$i; done; else for i in $(seq 1 254); do (echo >/dev/tcp/172.17.0.$i/22) >/dev/null 2>&1 && echo UP22:$i; done; fi; ip neigh
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---
# This is /run/systemd/resolve/resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
#
# This file might be symlinked as /etc/resolv.conf. If you're looking at
# /etc/resolv.conf and seeing this text, you have followed the symlink.
#
# This is a dynamic resolv.conf file for connecting local clients directly to
# all known uplink DNS servers. This file lists all configured search domains.

nameserver 127.0.0.53
search local
#  This file is part of systemd.
#
#  This file is distributed under the LGPLv2.1+.
#
# See resolved.conf(5) for details

[Resolve]
#DNS=
#FallbackDNS=
#Domains=
#LLMNR=yes
#MulticastDNS=no
#DNSSEC=no
#Cache=yes
#DNSStubListener=yes
#ReadEtcHosts=yes
---
Global
       LLMNR setting: yes
MulticastDNS setting: no
  DNSOverTLS setting: no
      DNSSEC setting: no
    DNSSEC supported: no

Link 2 (eth0)
      Current Scopes: DNS
       LLMNR setting: yes
MulticastDNS setting: no
  DNSOverTLS setting: no
      DNSSEC setting: no
    DNSSEC supported: no
  Current DNS Server: 172.17.0.1
         DNS Servers: 172.17.0.1
          DNS Domain: local
---
lo               UNKNOWN        127.0.0.1/8 ::1/128
eth0@if245       UP             172.17.0.2/16 fe80::42:acff:fe11:2/64
default via 172.17.0.1 dev eth0 
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.2 
172.17.0.1 dev eth0 lladdr 02:42:ac:11:00:01 REACHABLE
---
UP:1
UP:2
172.17.0.1 dev eth0 lladdr 02:42:ac:11:00:01 REACHABLE
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '==DNS=='; for h in host.docker.internal gateway.docker.internal db database mysql postgres redis app api internal ops archive records operational backup files; do getent hosts "$h" && echo "HIT $h"; done; echo '==LISTEN=='; ss -lntup; echo '==TMP/MNT=='; find /tmp /var/tmp /run /dev/shm /mnt /media /srv /opt -maxdepth 5 -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar*' \) 2>/dev/null`

```
root@ubuntu:~# echo '==DNS=='; for h in host.docker.internal gateway.docker.internal db database mysql postgres redis app api internal ops archive records operational backup files; do getent hosts "$h" && echo "HIT $h"; done; echo '==LISTEN=='; ss -lntup; echo '==TMP/MNT=='; find /tmp /var/tmp /run /dev/shm /mnt /media /srv /opt -maxdepth 5 -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar*' \) 2>/dev/null
==DNS==
==LISTEN==
Netid State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
tcp   LISTEN 0      128        127.0.0.53:53        0.0.0.0:*     users:(("systemd-resolve",pid=514,fd=13))
tcp   LISTEN 0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=612,fd=3))
tcp   LISTEN 0      128             [::]:22           [::]:*     users:(("sshd",pid=612,fd=4))
udp   UNCONN 0      0           127.0.0.53:53        0.0.0.0:*     users:(("systemd-resolve",pid=514,fd=12))
==TMP/MNT==
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/hosts; echo '---NEIGH---'; ip neigh 2>/dev/null; echo '---HIST---'; cat /root/.bash_history 2>/dev/null | tail -60; echo '---ROOTLS---'; ls -la /root 2>/dev/null`

```
root@ubuntu:~# cat /etc/hosts; echo '---NEIGH---'; ip neigh 2>/dev/null; echo '---HIST---'; cat /root/.bash_history 2>/dev/null | tail -60; echo '---ROOTLS---'; ls -la /root 2>/dev/null
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---NEIGH---
172.17.0.1 dev eth0 lladdr 02:42:ac:11:00:01 REACHABLE
---HIST---
id; whoami; hostname; uname -a; ls -la
---ROOTLS---
total 44
drwx------  6 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..
-rw-------  1 root root  890 Oct 17 14:18 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 14:18 .cache
drwxr-xr-x  3 root root 4096 Oct 17 14:18 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 14:18 .ssh
-rw-------  1 root root  102 Oct 17 14:18 .wget-hsts
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.wget-hsts; echo '--- CRON ---'; ls -la /etc/cron* /var/spool/cron 2>/dev/null; cat /etc/crontab 2>/dev/null; echo '--- TIMERS ---'; systemctl list-timers --all 2>/dev/null | head -40`

```
root@ubuntu:~# cat /root/.wget-hsts; echo '--- CRON ---'; ls -la /etc/cron* /var/spool/cron 2>/dev/null; cat /etc/crontab 2>/dev/null; echo '--- TIMERS ---'; systemctl list-timers --all 2>/dev/null | head -40
# HSTS 1.0 Known Hosts database for GNU Wget.
# Edit at your own risk.
# <hostname>\t<port>\t<include subdomains>\t<created>\t<max-age>
--- CRON ---
-rw-r--r-- 1 root root 1042 Apr  5  2018 /etc/crontab

/etc/cron.d:
total 20
drwxr-xr-x 1 root root 4096 Oct 17 14:17 .
drwxr-xr-x 1 root root 4096 Oct 17 14:18 ..
-rw-r--r-- 1 root root  201 Mar  5  2020 e2scrub_all
-rw-r--r-- 1 root root  712 Jul 28  2023 php
-rw-r--r-- 1 root root  102 Feb 13  2020 .placeholder

/etc/cron.daily:
total 24
drwxr-xr-x 1 root root 4096 Oct 17 14:17 .
drwxr-xr-x 1 root root 4096 Oct 17 14:18 ..
-rwxr-xr-x 1 root root  539 Mar  5  2020 apache2
-rwxr-xr-x 1 root root 1478 Apr  9  2018 apt-compat
-rwxr-xr-x 1 root root  355 Feb 13  2020 dpkg
-rwxr-xr-x 1 root root  377 Jan 18  2018 logrotate
-rwxr-xr-x 1 root root 1123 Nov  7  2019 man-db

/etc/cron.hourly:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 14:17 .
drwxr-xr-x 1 root root 4096 Oct 17 14:18 ..

/etc/cron.monthly:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 14:17 .
drwxr-xr-x 1 root root 4096 Oct 17 14:18 ..

/etc/cron.weekly:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 14:17 .
drwxr-xr-x 1 root root 4096 Oct 17 14:18 ..

/var/spool/cron:
total 8
drwxr-xr-x 3 root root 4096 Oct 17 14:17 .
drwxr-xr-x 1 root root 4096 Oct 17 14:17 ..
drwx-wx--T 2 root crontab 4096 Oct 17 14:17 crontabs
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 7) (Sunday=0 or 7) OR sun,mon,tue,wed,thu...
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root	cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
--- TIMERS ---
NEXT                         LEFT          LAST                         PASSED       UNIT                         ACTIVATES
Sat 2026-10-17 15:00:00 UTC  41min left    Sat 2026-10-17 14:00:00 UTC  18min ago    logrotate.timer              logrotate.service
Sun 2026-10-18 00:00:00 UTC  9h left       n/a                          n/a          apt-daily.timer              apt-daily.service
Sun 2026-10-18 06:00:00 UTC  15h left      n/a                          n/a          apt-daily-upgrade.timer      apt-daily-upgrade.service
Mon 2026-10-19 00:00:00 UTC  1 day 9h left n/a                          n/a          man-db.timer                 man-db.service
n/a                          n/a           n/a                          n/a          fstrim.timer                 fstrim.service
n/a                          n/a           n/a                          n/a          systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service

6 timers listed.
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/cron.d/php 2>/dev/null; echo '---WWW---'; ls -laR /var/www 2>/dev/null | head -80; echo '---SSH---'; cat /root/.ssh/authorized_keys 2>/dev/null; ls -la /home/*/.ssh 2>/dev/null; echo '---USERS---'; awk -F: '$3>=1000{print $1,$3,$6,$7}' /etc/passwd`

```
root@ubuntu:~# cat /etc/cron.d/php 2>/dev/null; echo '---WWW---'; ls -laR /var/www 2>/dev/null | head -80; echo '---SSH---'; cat /root/.ssh/authorized_keys 2>/dev/null; ls -la /home/*/.ssh 2>/dev/null; echo '---USERS---'; awk -F: '$3>=1000{print $1,$3,$6,$7}' /etc/passwd
# /etc/cron.d/php: crontab fragment for PHP
# This purges session files that are older than the configured
# session.gc_maxlifetime value.
09,39 *     * *     root   [ -x /usr/lib/php/sessionclean ] && /usr/lib/php/sessionclean
---WWW---
/var/www:
total 12
drwxr-xr-x 3 root root 4096 Oct 17 14:17 .
drwxr-xr-x 4 root root 4096 Oct 17 14:18 ..
drwxr-xr-x 2 root root 4096 Oct 17 14:17 html

/var/www/html:
total 16
drwxr-xr-x 2 root root 4096 Oct 17 14:17 .
drwxr-xr-x 3 root root 4096 Oct 17 14:17 ..
-rw-r--r-- 1 root root 10918 Oct 17 14:17 index.html
---SSH---
---USERS---
nobody 65534 /nonexistent /usr/sbin/nologin
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /var/www/html/index.html | head -n 60; echo '--- SEARCH ---'; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) 2>/dev/null | grep -v -E '^/(proc|sys|usr|lib|snap|boot)' | head -n 120`

```
root@ubuntu:~# cat /var/www/html/index.html | head -n 60; echo '--- SEARCH ---'; find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) 2>/dev/null | grep -v -E '^/(proc|sys|usr|lib|snap|boot)' | head -n 120
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<meta http-equiv="Content-Language" content="en" />
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
--- SEARCH ---
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/backups/alternatives.tar.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ps auxww; echo '---SOCKETS---'; ss -lntup 2>/dev/null; echo '---GREP---'; grep -rIil -e 'operational' -e 'opr_' -e 'ops-' -e 'evidence' /etc /opt /srv /root /usr/local /home 2>/dev/null | head -80`

```
root@ubuntu:~# ps auxww; echo '---SOCKETS---'; ss -lntup 2>/dev/null; echo '---GREP---'; grep -rIil -e 'operational' -e 'opr_' -e 'ops-' -e 'evidence' /etc /opt /srv /root /usr/local /home 2>/dev/null | head -80
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  22572  3968 ?        Ss   14:17   0:00 /sbin/init
root         318  0.0  0.0  28256  5792 ?        Ss   14:17   0:00 /lib/systemd/systemd-journald
root         357  0.0  0.0  45528  6820 ?        Ss   14:17   0:00 /lib/systemd/systemd-udevd
systemd+     514  0.0  0.0  70848  6184 ?        Ssl  14:17   0:00 /lib/systemd/systemd-resolved
root         522  0.0  0.0  16772  3640 ?        Ss   14:17   0:00 /usr/sbin/cron -f
message+     528  0.0  0.0   8544  3212 ?        Ss   14:17   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         536  0.0  0.0  81992  6348 ?        Ssl  14:17   0:00 /usr/sbin/rsyslogd -n -iNONE
root         612  0.0  0.0  12144  4532 ?        Ss   14:17   0:00 /usr/sbin/sshd -D
root         744  0.0  0.0  11032  3880 pts/0    Ss   14:18   0:00 -bash
root        1324  0.0  0.0  10296  3104 pts/0    R+   14:18   0:00 ps auxww
---SOCKETS---
Netid State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
tcp   LISTEN 0      128        127.0.0.53:53        0.0.0.0:*     users:(("systemd-resolve",pid=514,fd=13))
tcp   LISTEN 0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=612,fd=3))
tcp   LISTEN 0      128             [::]:22           [::]:*     users:(("sshd",pid=612,fd=4))
udp   UNCONN 0      0           127.0.0.53:53        0.0.0.0:*     users:(("systemd-resolve",pid=514,fd=12))
---GREP---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*opr*' -o -iname '*ops-*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) -print 2>/dev/null | head -200`

```
root@ubuntu:~# find / -xdev \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*opr*' -o -iname '*ops-*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) -print 2>/dev/null | head -200
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/usr/lib/x86_64-linux-gnu/libarchive.so.13.4.2
/usr/share/doc/libarchive13/changelog.Debian.gz
/usr/share/doc/libarchive13/copyright
/var/backups/alternatives.tar.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /opt /srv /usr/local /root /home 2>/dev/null; find /opt /srv /usr/local /root /home -maxdepth 3 -type f \( -iname '*record*' -o -iname '*archive*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) 2>/dev/null`

```
root@ubuntu:~# ls -la /opt /srv /usr/local /root /home 2>/dev/null; find /opt /srv /usr/local /root /home -maxdepth 3 -type f \( -iname '*record*' -o -iname '*archive*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' \) 2>/dev/null
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/root:
total 44
drwx------  6 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..
-rw-------  1 root root  890 Oct 17 14:18 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 14:18 .cache
drwxr-xr-x  3 root root 4096 Oct 17 14:18 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 14:18 .ssh
-rw-------  1 root root  102 Oct 17 14:18 .wget-hsts

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 20 root root 4096 Oct 17 14:18 ..

/usr/local:
total 36
drwxr-xr-x 10 root root 4096 Aug 11  2023 .
drwxr-xr-x 10 root root 4096 Aug 11  2023 ..
drwxr-xr-x  2 root root 4096 Aug 11  2023 bin
drwxr-xr-x  2 root root 4096 Aug 11  2023 etc
drwxr-xr-x  2 root root 4096 Aug 11  2023 games
drwxr-xr-x  2 root root 4096 Aug 11  2023 include
drwxr-xr-x  2 root root 4096 Aug 11  2023 lib
drwxr-xr-x  2 root root 4096 Aug 11  2023 sbin
drwxr-xr-x  4 root root 4096 Aug 11  2023 share
drwxr-xr-x  2 root root 4096 Aug 11  2023 src
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/backups 2>/dev/null; find /var/backups /var/lib /var/log -maxdepth 3 -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*record*' \) -ls 2>/dev/null | head -80`

```
root@ubuntu:~# ls -la /var/backups 2>/dev/null; find /var/backups /var/lib /var/log -maxdepth 3 -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*record*' \) -ls 2>/dev/null | head -80
total 20
drwxr-xr-x  2 root root 4096 Oct 17 14:18 .
drwxr-xr-x 14 root root 4096 Oct 17 14:18 ..
-rw-r--r--  1 root root  131 Oct 17 14:17 alternatives.tar.0
  524524      4 -rw-r--r--   1 root     root          642 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.list
  524525      4 -rw-r--r--   1 root     root          581 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.md5sums
  524526      4 -rw-r--r--   1 root     root          261 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.shlibs
  524527      8 -rw-r--r--   1 root     root         5438 Aug 11  2023 /var/lib/dpkg/info/libarchive13:amd64.symbols
  393261      4 -rw-r--r--   1 root     root          131 Oct 17 14:17 /var/backups/alternatives.tar.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ (find /var /usr/share /dev/shm /tmp /run /root -xdev -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*operational*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' \) -printf '%p %s\n' 2>/dev/null | head -200; echo '---GREP---'; grep -RIl --binary-files=without-match -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var /usr/share /dev/shm /tmp /run /root 2>/dev/null | head -100)`

```
root@ubuntu:~# (find /var /usr/share /dev/shm /tmp /run /root -xdev -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*operational*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' \) -printf '%p %s\n' 2>/dev/null | head -200; echo '---GREP---'; grep -RIl --binary-files=without-match -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var /usr/share /dev/shm /tmp /run /root 2>/dev/null | head -100)
/var/lib/dpkg/info/libarchive13:amd64.list 642
/var/lib/dpkg/info/libarchive13:amd64.md5sums 581
/var/lib/dpkg/info/libarchive13:amd64.shlibs 261
/var/lib/dpkg/info/libarchive13:amd64.symbols 5438
---GREP---
root@ubuntu:~# 
```
root@ubuntu:~# 
```
