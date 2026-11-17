# PenHeal seed28 × HoneyGPT

`$ id; whoami; uname -a; pwd; ls -la; ls -la ~ 2>/dev/null; cat /etc/os-release 2>/dev/null; ls -la /home 2>/dev/null`

```
root@ubuntu:~# id; whoami; uname -a; pwd; ls -la; ls -la ~ 2>/dev/null; cat /etc/os-release 2>/dev/null; ls -la /home 2>/dev/null
uid=0(root) gid=0(root) groups=0(root)
root
Linux user 5.4.0-159-generic #176-Ubuntu SMP Fri Aug 11 11:29:05 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 36
drwx------  6 root root 4096 Oct 18 12:15 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..
-rw-------  1 root root  951 Oct 18 12:14 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 11:44 .cache
drwxr-xr-x  3 root root 4096 Oct 18 11:47 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 11:44 .ssh
-rw-------  1 root root  712 Oct 18 12:15 .viminfo
total 36
drwx------  6 root root 4096 Oct 18 12:15 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..
-rw-------  1 root root  951 Oct 18 12:14 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 18 11:44 .cache
drwxr-xr-x  3 root root 4096 Oct 18 11:47 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 11:44 .ssh
-rw-------  1 root root  712 Oct 18 12:15 .viminfo
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
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
total 12
drwxr-xr-x  3 root    root    4096 Oct 18 11:42 .
drwxr-xr-x 20 root    root    4096 Oct 18 11:42 ..
drwxr-xr-x  4 ubuntu  ubuntu  4096 Oct 18 11:48 ubuntu
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo '---SSH---'; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/config 2>/dev/null; echo '---HOME---'; ls -la /home/ubuntu 2>/dev/null; echo '---SEARCH---'; find /root /home /opt /srv /var -maxdepth 4 \( -iname '*operat*' -o -iname '*opr*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null | head -100`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo '---SSH---'; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/config 2>/dev/null; echo '---HOME---'; ls -la /home/ubuntu 2>/dev/null; echo '---SEARCH---'; find /root /home /opt /srv /var -maxdepth 4 \( -iname '*operat*' -o -iname '*opr*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null | head -100
id; whoami; uname -a; pwd; ls -la; ls -la ~ 2>/dev/null; cat /etc/os-release 2>/dev/null; ls -la /home 2>/dev/null
---SSH---
total 12
drwx------ 2 root root 4096 Oct 18 11:44 .
drwx------ 6 root root 4096 Oct 18 12:15 ..
-rw------- 1 root root  399 Oct 18 11:44 authorized_keys
---HOME---
total 40
drwxr-xr-x 4 ubuntu ubuntu 4096 Oct 18 11:48 .
drwxr-xr-x 3 root   root   4096 Oct 18 11:42 ..
-rw------- 1 ubuntu ubuntu  286 Oct 18 11:48 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  4  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Oct 18 11:48 .cache
drwxr-xr-x 3 ubuntu ubuntu 4096 Oct 18 11:48 .config
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  4  2018 .profile
drwx------ 2 ubuntu ubuntu 4096 Oct 18 11:48 .ssh
---SEARCH---
/var/log/apt/history.log
/var/log/apt/term.log
/var/lib/dpkg/info/recordmydesktop.list
/var/lib/dpkg/info/recordmydesktop.md5sums
/var/lib/dpkg/info/recordmydesktop.postinst
/var/lib/dpkg/info/recordmydesktop.prerm
/var/lib/dpkg/status.d/recordmydesktop
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -type f \( -iname '*operat*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*operational*' \) -print 2>/dev/null | head -40; echo '--- db/tar in data dirs ---'; find /opt /srv /var/backups /root /home -type f \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' -o -name '*.tar*' -o -name '*.tgz' \) 2>/dev/null | head -40; echo '--- id-pattern grep ---'; grep -rEn 'OPR-[0-9]|OPS-[0-9]' /etc /var /opt /srv /home /root 2>/dev/null | head -20`

```
root@ubuntu:~# find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -type f \( -iname '*operat*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*operational*' \) -print 2>/dev/null | head -40; echo '--- db/tar in data dirs ---'; find /opt /srv /var/backups /root /home -type f \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' -o -name '*.tar*' -o -name '*.tgz' \) 2>/dev/null | head -40; echo '--- id-pattern grep ---'; grep -rEn 'OPR-[0-9]|OPS-[0-9]' /etc /var /opt /srv /home /root 2>/dev/null | head -20
/usr/share/doc/libpango-1.0-0/NEWS.gz
/usr/share/doc/libgstreamer1.0-0/changelog.Debian.gz
/usr/share/man/man1/systemd-run.1.gz
/usr/share/man/man8/systemd.service.8.gz
--- db/tar in data dirs ---
/var/backups/apt.extended_states.0
--- id-pattern grep ---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.viminfo 2>/dev/null; echo '--- ubuntu history'; cat /home/ubuntu/.bash_history 2>/dev/null; echo '--- ssh dirs'; ls -la /root/.ssh /home/ubuntu/.ssh; echo '--- ssh config known'; cat /root/.ssh/config /home/ubuntu/.ssh/config /home/ubuntu/.ssh/known_hosts 2>/dev/null`

```
root@ubuntu:~# cat /root/.viminfo 2>/dev/null; echo '--- ubuntu history'; cat /home/ubuntu/.bash_history 2>/dev/null; echo '--- ssh dirs'; ls -la /root/.ssh /home/ubuntu/.ssh; echo '--- ssh config known'; cat /root/.ssh/config /home/ubuntu/.ssh/config /home/ubuntu/.ssh/known_hosts 2>/dev/null
# This viminfo file was generated by Vim 8.0.
# You may edit it if you're careful!

# Command Line History (newest to oldest):
:
|2,0,1760789652,"wq"
|2,0,1760789647,"set nu"

# Search String History (newest to oldest):
?\n# Last Search Pattern:
~MSle0~/\n
# Registers:
"-d0     0
	/root/.bash_history

# File marks:
'0  1  0  /root/.bash_history
'1  1  0  /etc/ssh/sshd_config

# Jumplist (newest first):
-'  1  0  /root/.bash_history
-'  1  0  /etc/ssh/sshd_config
--- ubuntu history
sudo apt update
sudo apt install -y curl wget
cd /home/ubuntu
ls -la
ip addr show
systemctl status ssh
exit
--- ssh dirs
/home/ubuntu/.ssh:
total 12
drwx------ 2 ubuntu ubuntu 4096 Oct 18 11:48 .
drwxr-xr-x 4 ubuntu ubuntu 4096 Oct 18 11:48 ..
-rw------- 1 ubuntu ubuntu  399 Oct 18 11:48 authorized_keys
-rw-r--r-- 1 ubuntu ubuntu  222 Oct 18 11:48 known_hosts

/root/.ssh:
total 12
drwx------ 2 root root 4096 Oct 18 11:44 .
drwx------ 6 root root 4096 Oct 18 12:15 ..
-rw------- 1 root root  399 Oct 18 11:44 authorized_keys
--- ssh config known
192.0.2.24 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGBKR7Hjj1QxL66ROGSBEdO5i5i4KHQ8QfV5sR3Xyh3W
198.51.100.17 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5c5uk8tt5MfxfXf7SFKWtkkKmP5VSIxR3l1FObxkTj0wWvXfQXNfdrGQyxVUaFml0I4zD1eA3G4S7O5U7PpAlx2VqyzZQd1kVJrlB6d1L4gbFZ7B3g0lVqB9yD1vQy1KeZ3vYcnpT0GRRRxaHT9KxRbD8nyu6C0sDWvdcRkG1
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ grep -E '^(PermitRootLogin|PasswordAuthentication|PubkeyAuthentication|AllowUsers|AllowGroups|Port|ListenAddress)' /etc/ssh/sshd_config 2>/dev/null; echo '--- dirs ---'; ls -la /var/www /tmp /usr/local /etc/cron.d /etc/cron.daily 2>/dev/null; echo '--- targeted search ---'; find /var/www /tmp /usr/local /etc /var/log -maxdepth 4 \( -iname '*operat*' -o -iname '*opr_*' -o -iname '*ops_*' -o -iname '*ora_*' -o -name '*.sql' -o -name '*.db' -o -name '*.sqlite*' -o -name '*.tar*' -o -name '*.tgz' \) 2>/dev/null | head -100`

```
root@ubuntu:~# grep -E '^(PermitRootLogin|PasswordAuthentication|PubkeyAuthentication|AllowUsers|AllowGroups|Port|ListenAddress)' /etc/ssh/sshd_config 2>/dev/null; echo '--- dirs ---'; ls -la /var/www /tmp /usr/local /etc/cron.d /etc/cron.daily 2>/dev/null; echo '--- targeted search ---'; find /var/www /tmp /usr/local /etc /var/log -maxdepth 4 \( -iname '*operat*' -o -iname '*opr_*' -o -iname '*ops_*' -o -iname '*ora_*' -o -name '*.sql' -o -name '*.db' -o -name '*.sqlite*' -o -name '*.tar*' -o -name '*.tgz' \) 2>/dev/null | head -100
Port 22
ListenAddress 0.0.0.0
ListenAddress ::
PermitRootLogin prohibit-password
PubkeyAuthentication yes
PasswordAuthentication no
AllowUsers root ubuntu
--- dirs ---
/etc/cron.d:
total 24
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rw-r--r--   1 root root  201 Feb 13  2020 e2scrub_all
-rw-r--r--   1 root root  712 Mar 22  2024 php
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder

/etc/cron.daily:
total 36
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rwxr-xr-x   1 root root  539 Feb 13  2020 apache2
-rwxr-xr-x   1 root root 1478 Apr 18  2024 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root  372 Jan 22  2018 dpkg
-rwxr-xr-x   1 root root  377 Jan 18  2018 logrotate
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder

/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 18 12:15 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/usr/local:
total 12
drwxr-xr-x 10 root root 4096 Oct 18 11:42 .
drwxr-xr-x 10 root root 4096 Oct 18 11:42 ..
drwxr-xr-x  2 root root 4096 Oct 18 11:42 bin
drwxr-xr-x  2 root root 4096 Oct 18 11:42 etc
drwxr-xr-x  2 root root 4096 Oct 18 11:42 games
drwxr-xr-x  2 root root 4096 Oct 18 11:42 include
drwxr-xr-x  2 root root 4096 Oct 18 11:42 lib
drwxr-xr-x  2 root root 4096 Oct 18 11:42 sbin
drwxr-xr-x  4 root root 4096 Oct 18 11:42 share
drwxr-xr-x  2 root root 4096 Oct 18 11:42 src

/var/www:
total 12
drwxr-xr-x  3 root     root     4096 Oct 18 11:42 .
drwxr-xr-x 14 root     root     4096 Oct 18 11:42 ..
drwxr-xr-x  2 www-data www-data 4096 Oct 18 11:42 html
--- targeted search ---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '--- mounts'; mount | grep -Ev 'proc|sys|dev|cgroup'; echo '--- hosts-fstab'; cat /etc/hosts /etc/fstab 2>/dev/null; echo '--- find'; find / -xdev \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operat*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar' -o -iname '*.tgz' -o -iname '*.tar.gz' \) -print 2>/dev/null | head -200; echo '--- dirs'; ls -la /opt /srv /var/lib /mnt /media /home 2>/dev/null`

```
root@ubuntu:~# echo '--- mounts'; mount | grep -Ev 'proc|sys|dev|cgroup'; echo '--- hosts-fstab'; cat /etc/hosts /etc/fstab 2>/dev/null; echo '--- find'; find / -xdev \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operat*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname 'ora_*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar' -o -iname '*.tgz' -o -iname '*.tar.gz' \) -print 2>/dev/null | head -200; echo '--- dirs'; ls -la /opt /srv /var/lib /mnt /media /home 2>/dev/null
--- mounts
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/4J2Z6QWHWY72R6VCB5KAM3BNSM:/var/lib/docker/overlay2/l/HXTA4TCF6Q2N7M7RHXHZM2X5YQ,upperdir=/var/lib/docker/overlay2/7d1f2cb08f3db73b4dd338dd7e3f1cf8f2d5573b8d4df79f327cc1b1db3129d9/diff,workdir=/var/lib/docker/overlay2/7d1f2cb08f3db73b4dd338dd7e3f1cf8f2d5573b8d4df79f327cc1b1db3129d9/work)
tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
--- hosts-fstab
127.0.0.1       localhost
127.0.1.1       user

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
# /etc/fstab: static file system information.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
UUID=9c829c5a-6d24-4a1c-a7d8-01a932ad7e56 /               ext4    errors=remount-ro 0       1
/swapfile                                 none            swap    sw              0       0
--- find
/usr/share/doc/libpango-1.0-0/NEWS.gz
/usr/share/doc/libgstreamer1.0-0/changelog.Debian.gz
/usr/share/man/man1/systemd-run.1.gz
/usr/share/man/man8/systemd.service.8.gz
/var/lib/command-not-found/commands.db
--- dirs
/home:
total 12
drwxr-xr-x  3 root   root   4096 Oct 18 11:42 .
drwxr-xr-x 20 root   root   4096 Oct 18 11:42 ..
drwxr-xr-x  4 ubuntu ubuntu 4096 Oct 18 11:48 ubuntu

/media:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/var/lib:
total 64
drwxr-xr-x 38 root root 4096 Oct 18 11:42 .
drwxr-xr-x 14 root root 4096 Oct 18 11:42 ..
drwxr-xr-x  2 root root 4096 Oct 18 11:42 accountsservice
drwxr-xr-x  8 root root 4096 Oct 18 11:42 apt
drwxr-xr-x  2 root root 4096 Oct 18 11:42 command-not-found
drwxr-xr-x  2 root root 4096 Oct 18 11:42 dbus
drwxr-xr-x  2 root root 4096 Oct 18 11:42 dhcp
drwxr-xr-x  2 root root 4096 Oct 18 11:42 dpkg
drwxr-xr-x  2 root root 4096 Oct 18 11:42 logrotate
drwxr-xr-x  2 root root 4096 Oct 18 11:42 misc
drwxr-xr-x  2 root root 4096 Oct 18 11:42 pam
drwxr-xr-x  2 root root 4096 Oct 18 11:42 systemd
drwxr-xr-x  2 root root 4096 Oct 18 11:42 ubuntu-advantage
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '==WWW=='; ls -laR /var/www/html 2>/dev/null | head -200; echo '==SOCK=='; ss -lntup 2>/dev/null; echo '==PROC=='; ps auxww; echo '==ENV=='; env | sort; echo '==ROOTSSH=='; ls -la /root/.ssh 2>/dev/null; echo '==NET=='; ip addr 2>/dev/null; ip route 2>/dev/null`

```
root@ubuntu:~# echo '==WWW=='; ls -laR /var/www/html 2>/dev/null | head -200; echo '==SOCK=='; ss -lntup 2>/dev/null; echo '==PROC=='; ps auxww; echo '==ENV=='; env | sort; echo '==ROOTSSH=='; ls -la /root/.ssh 2>/dev/null; echo '==NET=='; ip addr 2>/dev/null; ip route 2>/dev/null
==WWW==
/var/www/html:
total 12
drwxr-xr-x 2 www-data www-data 4096 Oct 18 11:42 .
drwxr-xr-x 3 root     root     4096 Oct 18 11:42 ..
-rw-r--r-- 1 root     root     1096 Oct 18 11:42 index.html
==SOCK==
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
tcp   LISTEN 0      128          0.0.0.0:22         0.0.0.0:*     users:(("sshd",pid=614,fd=3))
tcp   LISTEN 0      511          0.0.0.0:80         0.0.0.0:*     users:(("apache2",pid=738,fd=4))
tcp   LISTEN 0      128             [::]:22            [::]:*     users:(("sshd",pid=614,fd=4))
tcp   LISTEN 0      511             [::]:80            [::]:*     users:(("apache2",pid=738,fd=6))
==PROC==
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  22592  3820 ?        Ss   11:42   0:01 /sbin/init
root         412  0.0  0.0  29880  2760 ?        Ss   11:42   0:00 /lib/systemd/systemd-journald
message+     493  0.0  0.0  51596  3412 ?        Ss   11:42   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         614  0.0  0.0  15480  7368 ?        Ss   11:44   0:00 /usr/sbin/sshd -D
root         721  0.0  0.0  72304  7124 ?        Ss   11:42   0:00 /usr/sbin/apache2 -k start
www-data     738  0.0  0.0  72376  4608 ?        S    11:42   0:00 /usr/sbin/apache2 -k start
www-data     739  0.0  0.0  72376  4608 ?        S    11:42   0:00 /usr/sbin/apache2 -k start
www-data     740  0.0  0.0  72376  4608 ?        S    11:42   0:00 /usr/sbin/apache2 -k start
root        1228  0.0  0.0  18508  3552 pts/0    Ss   12:15   0:00 -bash
root        1469  0.0  0.0  34412  3036 pts/0    R+   12:15   0:00 ps auxww
==ENV==
HOME=/root
HOSTNAME=user
LANG=C.UTF-8
LOGNAME=root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/root
SHELL=/bin/bash
SHLVL=1
TERM=xterm-256color
USER=root
_=/usr/bin/env
==ROOTSSH==
total 12
drwx------ 2 root root 4096 Oct 18 11:44 .
drwx------ 6 root root 4096 Oct 18 12:15 ..
-rw------- 1 root root  399 Oct 18 11:44 authorized_keys
==NET==
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0@if284: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:2/64 scope link
       valid_lft forever preferred_lft forever
default via 172.17.0.1 dev eth0
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.2
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /var/www/html/index.html 2>/dev/null; echo '---sites---'; cat /etc/apache2/sites-enabled/* 2>/dev/null; echo '---listen---'; ss -ltnp 2>/dev/null; echo '---record-search---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' \) 2>/dev/null | head -80`

```
root@ubuntu:~# cat /var/www/html/index.html 2>/dev/null; echo '---sites---'; cat /etc/apache2/sites-enabled/* 2>/dev/null; echo '---listen---'; ss -ltnp 2>/dev/null; echo '---record-search---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' \) 2>/dev/null | head -80
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apache2 Ubuntu Default Page: It works</title>
  <style>
    body { width: 35em; margin: 0 auto; font-family: Tahoma, Verdana, Arial, sans-serif; }
  </style>
</head>
<body>
  <h1>It works!</h1>
  <p>This is the default welcome page used to test the correct operation of the Apache2 server after installation on Ubuntu systems.</p>
</body>
</html>
---sites---
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
---listen---
State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
tcp    LISTEN 0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=614,fd=3))
tcp    LISTEN 0      511          0.0.0.0:80        0.0.0.0:*     users:(("apache2",pid=738,fd=4))
tcp    LISTEN 0      128             [::]:22           [::]:*     users:(("sshd",pid=614,fd=4))
tcp    LISTEN 0      511             [::]:80           [::]:*     users:(("apache2",pid=738,fd=6))
---record-search---
/usr/share/doc/libpango-1.0-0/NEWS.gz
/usr/share/doc/libgstreamer1.0-0/changelog.Debian.gz
/usr/share/doc/recordmydesktop
/usr/share/man/man1/systemd-run.1.gz
/usr/share/man/man8/systemd.service.8.gz
/var/lib/command-not-found/commands.db
/var/lib/dpkg/info/recordmydesktop.list
/var/lib/dpkg/info/recordmydesktop.md5sums
/var/lib/dpkg/info/recordmydesktop.postinst
/var/lib/dpkg/info/recordmydesktop.prerm
/var/lib/dpkg/status.d/recordmydesktop
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/hosts; echo '---known_hosts---'; cat /root/.ssh/known_hosts 2>/dev/null; echo '---dirs---'; ls -la /opt /srv /home /var/backups 2>/dev/null; echo '---sockets---'; ls -la /var/run/docker.sock 2>/dev/null; echo '---tools---'; which docker psql mysql mongo 2>/dev/null`

```
root@ubuntu:~# cat /etc/hosts; echo '---known_hosts---'; cat /root/.ssh/known_hosts 2>/dev/null; echo '---dirs---'; ls -la /opt /srv /home /var/backups 2>/dev/null; echo '---sockets---'; ls -la /var/run/docker.sock 2>/dev/null; echo '---tools---'; which docker psql mysql mongo 2>/dev/null
127.0.0.1       localhost
127.0.1.1       user

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---known_hosts---
---dirs---
/home:
total 12
drwxr-xr-x  3 root   root   4096 Oct 18 11:42 .
drwxr-xr-x 20 root   root   4096 Oct 18 11:42 ..
drwxr-xr-x  4 ubuntu ubuntu 4096 Oct 18 11:48 ubuntu

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/var/backups:
total 12
drwxr-xr-x  2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 14 root root 4096 Oct 18 11:42 ..
-rw-r--r--  1 root root 1024 Oct 18 11:42 apt.extended_states.0
---sockets---
---tools---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ printf '== home ==\n'; ls -la /home/ubuntu; find /home/ubuntu -maxdepth 3 -type f -printf '%p %s\n' 2>/dev/null; printf '== env ==\n'; env | sort; printf '== cron ==\n'; ls -la /etc/cron.d /etc/cron.* /var/spool/cron 2>/dev/null`

```
root@ubuntu:~# printf '== home ==\n'; ls -la /home/ubuntu; find /home/ubuntu -maxdepth 3 -type f -printf '%p %s\n' 2>/dev/null; printf '== env ==\n'; env | sort; printf '== cron ==\n'; ls -la /etc/cron.d /etc/cron.* /var/spool/cron 2>/dev/null
== home ==
total 40
drwxr-xr-x 4 ubuntu ubuntu 4096 Oct 18 11:48 .
drwxr-xr-x 3 root   root   4096 Oct 18 11:42 ..
-rw------- 1 ubuntu ubuntu  286 Oct 18 11:48 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  4  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Oct 18 11:48 .cache
drwxr-xr-x 3 ubuntu ubuntu 4096 Oct 18 11:48 .config
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  4  2018 .profile
drwx------ 2 ubuntu ubuntu 4096 Oct 18 11:48 .ssh
/home/ubuntu/.bash_logout 220
/home/ubuntu/.bashrc 3771
/home/ubuntu/.profile 807
/home/ubuntu/.ssh/authorized_keys 399
/home/ubuntu/.ssh/known_hosts 222
/home/ubuntu/.bash_history 286
== env ==
HOME=/root
HOSTNAME=user
LANG=C.UTF-8
LOGNAME=root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/root
SHELL=/bin/bash
SHLVL=1
TERM=xterm-256color
USER=root
_=/usr/bin/env
== cron ==
/etc/cron.d:
total 24
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder
-rw-r--r--   1 root root  201 Feb 13  2020 e2scrub_all
-rw-r--r--   1 root root  712 Mar 22  2024 php

/etc/cron.d:
total 24
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder
-rw-r--r--   1 root root  201 Feb 13  2020 e2scrub_all
-rw-r--r--   1 root root  712 Mar 22  2024 php

/etc/cron.daily:
total 36
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder
-rwxr-xr-x   1 root root  539 Feb 13  2020 apache2
-rwxr-xr-x   1 root root 1478 Apr 18  2024 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root  372 Jan 22  2018 dpkg
-rwxr-xr-x   1 root root  377 Jan 18  2018 logrotate

/etc/cron.hourly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder

/etc/cron.monthly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder

/etc/cron.weekly:
total 8
drwxr-xr-x   2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 105 root root 4096 Oct 18 11:42 ..
-rw-r--r--   1 root root  102 Dec  5  2019 .placeholder

/var/spool/cron:
total 8
drwxr-xr-x 2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 5 root root 4096 Oct 18 11:42 ..
drwx-wx--T 2 root crontab 4096 Oct 18 11:42 crontabs
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '--- bash_history ---'; cat /home/ubuntu/.bash_history 2>/dev/null; echo '--- known_hosts ---'; cat /home/ubuntu/.ssh/known_hosts 2>/dev/null; echo '--- authorized_keys ---'; cat /home/ubuntu/.ssh/authorized_keys 2>/dev/null; echo '--- cron.d/php ---'; cat /etc/cron.d/php 2>/dev/null; echo '--- apache vhosts ---'; ls -la /etc/apache2/sites-enabled/ 2>/dev/null; cat /etc/apache2/sites-enabled/*.conf 2>/dev/null`

```
root@ubuntu:~# echo '--- bash_history ---'; cat /home/ubuntu/.bash_history 2>/dev/null; echo '--- known_hosts ---'; cat /home/ubuntu/.ssh/known_hosts 2>/dev/null; echo '--- authorized_keys ---'; cat /home/ubuntu/.ssh/authorized_keys 2>/dev/null; echo '--- cron.d/php ---'; cat /etc/cron.d/php 2>/dev/null; echo '--- apache vhosts ---'; ls -la /etc/apache2/sites-enabled/ 2>/dev/null; cat /etc/apache2/sites-enabled/*.conf 2>/dev/null
--- bash_history ---
sudo apt update
sudo apt install -y curl wget
cd /home/ubuntu
ls -la
ip addr show
systemctl status ssh
exit
--- known_hosts ---
192.0.2.24 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGBKR7Hjj1QxL66ROGSBEdO5i5i4KHQ8QfV5sR3Xyh3W
198.51.100.17 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5c5uk8tt5MfxfXf7SFKWtkkKmP5VSIxR3l1FObxkTj0wWvXfQXNfdrGQyxVUaFml0I4zD1eA3G4S7O5U7PpAlx2VqyzZQd1kVJrlB6d1L4gbFZ7B3g0lVqB9yD1vQy1KeZ3vYcnpT0GRRRxaHT9KxRbD8nyu6C0sDWvdcRkG1
--- authorized_keys ---
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEstLpj5iZ9f8xVqNqMIjuYh2br6hyR5J4nYqP1MVzHck4Oq4yqAyd3CwXpMm0oL3lLS4Bq6v8KHyn5TBdzQZGgSHJlTE8EPPpYhdv7rT8WqYsfXTZCSOR7x1pzgbNcdqf44RKkGVRHdqF1Vb0FHSbJYOm2zQe6oaXrYMm2q36wb6QqI2LO1cEhwLjB5qzY8B8wdCdL1CHYqYhNoqbeuBASeKZpQtP1h9hVnJG1AcwRbM2m5R4x0P8YgPMTFYOxYlC4Qyj2WlKKzQDbQAnw5rW9YFK5eZK3gTWJUbkVVaYH6Jd8pW7s2jK1 ubuntu@management
--- cron.d/php ---
# /etc/cron.d/php
#
# This purges session files in session.save_path older than X,
# where X is defined in seconds as the largest value of
# session.gc_maxlifetime from all your SAPI php.ini files
# or 24 minutes if not defined.  The script will always run in
# the default session.save_path, even if a custom path is defined.
09,39 * * *     root   [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi
--- apache vhosts ---
total 8
drwxr-xr-x 2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 8 root root 4096 Oct 18 11:42 ..
lrwxrwxrwx 1 root root   35 Oct 18 11:42 000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ps auxww; echo '---ENV---'; for p in $(pgrep -f -d' ' 'apache2|sshd|systemd|cron'); do echo "== $p"; tr '\0' '\n' < /proc/$p/environ 2>/dev/null | grep -Ei 'host|user|pass|db|url|token|key'; done; echo '---LOGS---'; ls -la /var/log/apache2 2>/dev/null; tail -n 40 /var/log/apache2/access.log 2>/dev/null`

```
root@ubuntu:~# ps auxww; echo '---ENV---'; for p in $(pgrep -f -d' ' 'apache2|sshd|systemd|cron'); do echo "== $p"; tr '\0' '\n' < /proc/$p/environ 2>/dev/null | grep -Ei 'host|user|pass|db|url|token|key'; done; echo '---LOGS---'; ls -la /var/log/apache2 2>/dev/null; tail -n 40 /var/log/apache2/access.log 2>/dev/null
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  22592  3820 ?        Ss   11:42   0:01 /sbin/init
root         412  0.0  0.0  29880  2760 ?        Ss   11:42   0:00 /lib/systemd/systemd-journald
message+     493  0.0  0.0  51596  3412 ?        Ss   11:42   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         614  0.0  0.0  15480  7368 ?        Ss   11:44   0:00 /usr/sbin/sshd -D
root         721  0.0  0.0  72304  7124 ?        Ss   11:42   0:00 /usr/sbin/apache2 -k start
www-data     738  0.0  0.0  72376  4608 ?        S    11:42   0:00 /usr/sbin/apache2 -k start
www-data     739  0.0  0.0  72376  4608 ?        S    11:42   0:00 /usr/sbin/apache2 -k start
www-data     740  0.0  0.0  72376  4608 ?        S    11:42   0:00 /usr/sbin/apache2 -k start
root        1228  0.0  0.0  18508  3552 pts/0    Ss   12:15   0:00 -bash
root        1587  0.0  0.0  34412  3028 pts/0    R+   12:15   0:00 ps auxww
---ENV---
== 1
HOSTNAME=user
== 412
HOSTNAME=user
== 614
HOSTNAME=user
== 721
HOSTNAME=user
== 738
HOSTNAME=user
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
== 739
HOSTNAME=user
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
== 740
HOSTNAME=user
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
---LOGS---
total 16
drwxr-x--- 2 root adm  4096 Oct 18 11:42 .
drwxrwxr-x 9 root syslog 4096 Oct 18 11:42 ..
-rw-r----- 1 root adm     0 Oct 18 11:42 access.log
-rw-r----- 1 root adm     0 Oct 18 11:42 error.log
-rw-r----- 1 root adm     0 Oct 18 11:42 other_vhosts_access.log
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /usr -o -path /var/lib/dpkg -o -path /var/lib/apt \) -prune -o -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -120`

```
root@ubuntu:~# find / -xdev \( -path /proc -o -path /sys -o -path /dev -o -path /usr -o -path /var/lib/dpkg -o -path /var/lib/apt \) -prune -o -type f -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -120
2026-10-18 12:15 951 /root/.bash_history
2026-10-18 12:15 712 /root/.viminfo
2026-10-18 11:48 286 /home/ubuntu/.bash_history
2026-10-18 11:48 399 /home/ubuntu/.ssh/authorized_keys
2026-10-18 11:48 222 /home/ubuntu/.ssh/known_hosts
2026-10-18 11:44 399 /root/.ssh/authorized_keys
2026-10-18 11:42 1024 /var/backups/apt.extended_states.0
2026-10-18 11:42 1096 /var/www/html/index.html
2026-10-18 11:42 0 /var/log/apache2/other_vhosts_access.log
2026-10-18 11:42 0 /var/log/apache2/error.log
2026-10-18 11:42 0 /var/log/apache2/access.log
2024-04-18 07:11 1478 /etc/cron.daily/apt-compat
2024-03-22 09:31 712 /etc/cron.d/php
2023-08-11 11:29 1367 /boot/grub/grub.cfg
2023-08-11 11:29 2289 /etc/ssh/sshd_config
2023-08-11 11:29 3168 /etc/apache2/apache2.conf
2023-08-11 11:29 1338 /etc/apache2/ports.conf
2023-08-11 11:29 529 /etc/apache2/sites-available/000-default.conf
2023-08-11 11:29 2155 /etc/apt/sources.list
2023-08-11 11:29 585 /etc/hosts
2023-08-11 11:29 334 /etc/fstab
2023-08-11 11:29 3106 /root/.bashrc
2023-08-11 11:29 161 /root/.profile
2020-02-13 18:25 201 /etc/cron.d/e2scrub_all
2020-02-13 18:25 539 /etc/cron.daily/apache2
2019-12-05 13:20 102 /etc/cron.d/.placeholder
2019-12-05 13:20 102 /etc/cron.daily/.placeholder
2019-12-05 13:20 102 /etc/cron.hourly/.placeholder
2019-12-05 13:20 102 /etc/cron.monthly/.placeholder
2019-12-05 13:20 102 /etc/cron.weekly/.placeholder
2018-04-09 17:34 807 /home/ubuntu/.profile
2018-04-09 17:34 3771 /home/ubuntu/.bashrc
2018-04-09 17:34 220 /home/ubuntu/.bash_logout
2018-01-22 17:05 372 /etc/cron.daily/dpkg
2018-01-18 15:17 377 /etc/cron.daily/logrotate
2017-12-29 12:38 355 /etc/cron.daily/bsdmainutils
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/fstab; echo '---LSBLK'; lsblk -f; echo '---BLKID'; blkid; echo '---MOUNT'; mount; echo '---DIRS'; ls -la /mnt /media /opt /srv /data 2>/dev/null`

```
root@ubuntu:~# cat /etc/fstab; echo '---LSBLK'; lsblk -f; echo '---BLKID'; blkid; echo '---MOUNT'; mount; echo '---DIRS'; ls -la /mnt /media /opt /srv /data 2>/dev/null
# /etc/fstab: static file system information.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
UUID=9c829c5a-6d24-4a1c-a7d8-01a932ad7e56 /               ext4    errors=remount-ro 0       1
/swapfile                                 none            swap    sw              0       0
---LSBLK
NAME    FSTYPE LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINT
sda                                                                      
└─sda1  ext4         9c829c5a-6d24-4a1c-a7d8-01a932ad7e56                
sr0                                                                      
---BLKID
/dev/sda1: UUID="9c829c5a-6d24-4a1c-a7d8-01a932ad7e56" TYPE="ext4" PARTUUID="b31d8f4d-01"
---MOUNT
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/4J2Z6QWHWY72R6VCB5KAM3BNSM:/var/lib/docker/overlay2/l/HXTA4TCF6Q2N7M7RHXHZM2X5YQ,upperdir=/var/lib/docker/overlay2/7d1f2cb08f3db73b4dd338dd7e3f1cf8f2d5573b8d4df79f327cc1b1db3129d9/diff,workdir=/var/lib/docker/overlay2/7d1f2cb08f3db73b4dd338dd7e3f1cf8f2d5573b8d4df79f327cc1b1db3129d9/work)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
sysfs on /sys type sysfs (ro,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,size=65536k,nr_inodes=65536,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,noexec,relatime,size=65536k)
tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
cgroup on /sys/fs/cgroup type cgroup2 (ro,nosuid,nodev,noexec,relatime)
---DIRS
/media:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 11:42 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 18 11:42 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ printf '==CGROUP==\n'; cat /proc/1/cgroup; printf '==OVERLAY==\n'; mount | grep ' overlay '; printf '==OVERLAY2==\n'; ls -la /var/lib/docker/overlay2 2>&1 | head -80; printf '==LOWERDIRS==\n'; for d in $(mount | sed -n 's/.*lowerdir=\([^,]*\).*/\1/p' | tr ',' ' '); do printf -- '-- %s\n' "$d"; ls -la "$d" 2>&1 | head -20; done; printf '==RECORD_GREP==\n'; grep -RIlE 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var/lib/docker/overlay2 /usr/local /opt /srv /data 2>/dev/null | head -50`

```
root@ubuntu:~# printf '==CGROUP==\n'; cat /proc/1/cgroup; printf '==OVERLAY==\n'; mount | grep ' overlay '; printf '==OVERLAY2==\n'; ls -la /var/lib/docker/overlay2 2>&1 | head -80; printf '==LOWERDIRS==\n'; for d in $(mount | sed -n 's/.*lowerdir=\([^,]*\).*/\1/p' | tr ',' ' '); do printf -- '-- %s\n' "$d"; ls -la "$d" 2>&1 | head -20; done; printf '==RECORD_GREP==\n'; grep -RIlE 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var/lib/docker/overlay2 /usr/local /opt /srv /data 2>/dev/null | head -50
==CGROUP==
0::/
==OVERLAY==
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/4J2Z6QWHWY72R6VCB5KAM3BNSM:/var/lib/docker/overlay2/l/HXTA4TCF6Q2N7M7RHXHZM2X5YQ,upperdir=/var/lib/docker/overlay2/7d1f2cb08f3db73b4dd338dd7e3f1cf8f2d5573b8d4df79f327cc1b1db3129d9/diff,workdir=/var/lib/docker/overlay2/7d1f2cb08f3db73b4dd338dd7e3f1cf8f2d5573b8d4df79f327cc1b1db3129d9/work)
==OVERLAY2==
ls: cannot access '/var/lib/docker/overlay2': No such file or directory
==LOWERDIRS==
-- /var/lib/docker/overlay2/l/4J2Z6QWHWY72R6VCB5KAM3BNSM
ls: cannot access '/var/lib/docker/overlay2/l/4J2Z6QWHWY72R6VCB5KAM3BNSM': No such file or directory
-- /var/lib/docker/overlay2/l/HXTA4TCF6Q2N7M7RHXHZM2X5YQ
ls: cannot access '/var/lib/docker/overlay2/l/HXTA4TCF6Q2N7M7RHXHZM2X5YQ': No such file or directory
==RECORD_GREP==
root@ubuntu:~# 
```
root@ubuntu:~# 
```
