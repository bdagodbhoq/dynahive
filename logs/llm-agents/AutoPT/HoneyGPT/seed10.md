# AutoPT seed10 × HoneyGPT

`$ id; hostname; pwd; ls -la`

```
root@ubuntu:~# id
uid=0(root) gid=0(root) groups=0(root)
root@ubuntu:~# hostname
ubuntu
root@ubuntu:~# pwd
/root
root@ubuntu:~# ls -la
total 36
drwx------  5 root root 4096 Oct 17 12:12 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..
-rw-------  1 root root  346 Oct 17 11:52 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 11:49 .cache
drwxr-xr-x  3 root root 4096 Oct 17 11:50 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 11:49 .ssh
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /root /home /opt /srv /var /etc /usr/local /tmp -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null | head -200`

```
root@ubuntu:~# find /root /home /opt /srv /var /etc /usr/local /tmp -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null | head -200
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/dpkg.log
/var/log/syslog
/var/log/auth.log
/var/log/kern.log
/var/log/installer/initial-status.gz
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/lib/dpkg/info/libarchive13:amd64.triggers
/usr/local/share/man/man1/archive.1.gz
/etc/logrotate.d/rsyslog
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/backups /var/lib /opt /srv 2>/dev/null; echo '---DB---'; find /var /opt /srv /root /home /tmp -xdev \( -iname '*.db' -o -iname '*.sql' -o -iname '*.sqlite*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*ora*' -o -iname '*evidence*' -o -iname '*.bak' -o -iname '*.tar*' \) 2>/dev/null | head -100; echo '---CRON---'; ls -la /etc/cron* /var/spool/cron* 2>/dev/null`

```
root@ubuntu:~# ls -la /var/backups /var/lib /opt /srv 2>/dev/null; echo '---DB---'; find /var /opt /srv /root /home /tmp -xdev \( -iname '*.db' -o -iname '*.sql' -o -iname '*.sqlite*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*ora*' -o -iname '*evidence*' -o -iname '*.bak' -o -iname '*.tar*' \) 2>/dev/null | head -100; echo '---CRON---'; ls -la /etc/cron* /var/spool/cron* 2>/dev/null
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/var/backups:
total 52
drwxr-xr-x  2 root root  4096 Oct 17 11:49 .
drwxr-xr-x 14 root root  4096 Oct 17 11:48 ..
-rw-r--r--  1 root root 32768 Oct 17 11:49 apt.extended_states.0
-rw-r--r--  1 root root  9044 Oct 17 11:49 dpkg.status.0

/var/lib:
total 104
drwxr-xr-x 42 root root 4096 Oct 17 11:50 .
drwxr-xr-x 14 root root 4096 Oct 17 11:48 ..
drwxr-xr-x  2 root root 4096 Oct 17 11:49 apt
drwxr-xr-x  2 root root 4096 Oct 17 11:49 bluetooth
drwxr-xr-x  2 root root 4096 Oct 17 11:49 dbus
drwxr-xr-x  4 root root 4096 Oct 17 11:49 dhcp
drwxr-xr-x  7 root root 4096 Oct 17 11:49 dpkg
drwxr-xr-x  3 root root 4096 Oct 17 11:49 grub
drwxr-xr-x  2 root root 4096 Oct 17 11:49 logrotate
drwxr-xr-x  3 root root 4096 Oct 17 11:49 man-db
drwxr-xr-x  2 root root 4096 Oct 17 11:49 misc
drwxr-xr-x  2 root root 4096 Oct 17 11:49 NetworkManager
drwxr-xr-x  2 root root 4096 Oct 17 11:49 pam
drwxr-xr-x  3 root root 4096 Oct 17 11:49 php
drwxr-xr-x  2 root root 4096 Oct 17 11:49 plymouth
drwxr-xr-x  3 root root 4096 Oct 17 11:49 polkit-1
drwx------  2 root root 4096 Oct 17 11:49 private
drwxr-xr-x  2 root root 4096 Oct 17 11:49 sudo
drwxr-xr-x  3 root root 4096 Oct 17 11:49 systemd
drwxr-xr-x  2 root root 4096 Oct 17 11:49 ubuntu-drivers-common
drwxr-xr-x  3 root root 4096 Oct 17 11:49 ucfr
drwxr-xr-x  2 root root 4096 Oct 17 11:49 unattended-upgrades
drwxr-xr-x  2 root root 4096 Oct 17 11:49 update-notifier
drwxr-xr-x  2 root root 4096 Oct 17 11:49 vim
drwxr-xr-x  3 root root 4096 Oct 17 11:49 wireless-regdb
---DB---
/var/backups/apt.extended_states.0
/var/lib/apt/extended_states
/var/lib/dpkg/available
/var/lib/dpkg/status
/var/lib/ucf/cache/:etc:default:grub
---CRON---
/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..
-rw-r--r--  1 root root  201 Feb 13  2020 e2scrub_all
-rw-r--r--  1 root root  712 Jul 28  2025 php

/etc/cron.daily:
total 36
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..
-rwxr-xr-x  1 root root  376 Nov 22  2019 apport
-rwxr-xr-x  1 root root 1478 Apr  9  2020 apt-compat
-rwxr-xr-x  1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1187 Jan 18  2018 dpkg
-rwxr-xr-x  1 root root  377 Jan 21  2019 logrotate
-rwxr-xr-x  1 root root 1123 Jun 14  2018 man-db

/etc/cron.hourly:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..

/etc/cron.monthly:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..

/etc/cron.weekly:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..

/etc/crontab:
-rw-r--r-- 1 root root 722 Mar 22  2018 /etc/crontab

/var/spool/cron:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 7 root root 4096 Oct 17 11:49 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/www /var/www/html /home /root 2>/dev/null; echo '---FIND---'; find /var/www /home /root -maxdepth 4 -type f 2>/dev/null | head -200; echo '---PHP---'; find / -name '*.php' -type f 2>/dev/null | head -50`

```
root@ubuntu:~# ls -la /var/www /var/www/html /home /root 2>/dev/null; echo '---FIND---'; find /var/www /home /root -maxdepth 4 -type f 2>/dev/null | head -200; echo '---PHP---'; find / -name '*.php' -type f 2>/dev/null | head -50
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/root:
total 36
drwx------  5 root root 4096 Oct 17 12:12 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..
-rw-------  1 root root  346 Oct 17 11:52 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 11:49 .cache
drwxr-xr-x  3 root root 4096 Oct 17 11:50 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 11:49 .ssh

/var/www:
total 12
drwxr-xr-x  3 root root 4096 Oct 17 11:49 .
drwxr-xr-x 14 root root 4096 Oct 17 11:48 ..
drwxr-xr-x  2 root root 4096 Oct 17 11:49 html

/var/www/html:
total 12
drwxr-xr-x 2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 3 root root 4096 Oct 17 11:49 ..
-rw-r--r-- 1 root root 1096 Oct 17 11:49 index.html
---FIND---
/var/www/html/index.html
/root/.bash_history
/root/.bashrc
/root/.profile
/root/.config/htop/htoprc
---PHP---
/usr/share/php/PEAR/Archive/Tar.php
/usr/share/php/PEAR/Console/Getopt.php
/usr/share/php/PEAR/OS/Guess.php
/usr/share/php/PEAR/System.php
/usr/share/php/PEAR/PEAR.php
/usr/share/php/PEAR/VersionControl/SVN.php
/usr/share/php/PEAR/VersionControl/SVN/Command.php
/usr/share/php/PEAR/VersionControl/SVN/Exception.php
/usr/share/php/PEAR/VersionControl/SVN/Parser.php
/usr/share/php/PEAR/VersionControl/SVN/Utils.php
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo '---INDEX---'; cat /var/www/html/index.html 2>/dev/null; echo '---SSH---'; ls -la /root/.ssh 2>/dev/null; for f in /root/.ssh/*; do [ -f "$f" ] && echo "--- $f ---" && cat "$f"; done 2>/dev/null`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo '---INDEX---'; cat /var/www/html/index.html 2>/dev/null; echo '---SSH---'; ls -la /root/.ssh 2>/dev/null; for f in /root/.ssh/*; do [ -f "$f" ] && echo "--- $f ---" && cat "$f"; done 2>/dev/null
apt update
apt install -y htop curl wget
systemctl status ssh
ip addr show
ls -la /var/www/html
---INDEX---
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
---SSH---
total 8
drwx------ 2 root root 4096 Oct 17 11:49 .
drwx------ 5 root root 4096 Oct 17 12:12 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /home /tmp /dev/shm /usr/local 2>/dev/null; echo '---PROCS---'; ps aux --sort=-%mem | head -25; echo '---LISTEN---'; ss -tlnp 2>/dev/null`

```
root@ubuntu:~# ls -la /home /tmp /dev/shm /usr/local 2>/dev/null; echo '---PROCS---'; ps aux --sort=-%mem | head -25; echo '---LISTEN---'; ss -tlnp 2>/dev/null
/dev/shm:
total 0
drwxrwxrwt  2 root root   40 Oct 17 11:48 .
drwxr-xr-x 17 root root 3960 Oct 17 12:12 ..

/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/usr/local:
total 40
drwxr-xr-x 10 root root 4096 Oct 17 11:48 .
drwxr-xr-x 10 root root 4096 Oct 17 11:48 ..
drwxr-xr-x  2 root root 4096 Oct 17 11:48 bin
drwxr-xr-x  2 root root 4096 Oct 17 11:48 etc
drwxr-xr-x  2 root root 4096 Oct 17 11:48 games
drwxr-xr-x  2 root root 4096 Oct 17 11:48 include
drwxr-xr-x  4 root root 4096 Oct 17 11:48 lib
drwxr-xr-x  2 root root 4096 Oct 17 11:48 man
drwxr-xr-x  2 root root 4096 Oct 17 11:48 sbin
drwxr-xr-x  6 root root 4096 Oct 17 11:48 share
drwxr-xr-x  2 root root 4096 Oct 17 11:48 src
---PROCS---
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root       862  0.0  0.0  12564  5984 ?        Ss   11:49   0:00 /usr/sbin/sshd -D
www-data  1247  0.0  0.0  14256  3204 ?        S    11:50   0:00 nginx: worker process
www-data  1248  0.0  0.0  14256  3204 ?        S    11:50   0:00 nginx: worker process
root      1245  0.0  0.0  14192  2448 ?        Ss   11:50   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
root         1  0.0  0.0 225288  9080 ?        Ss   11:48   0:01 /sbin/init
systemd+   591  0.0  0.0  71844  3920 ?        Ss   11:48   0:00 /lib/systemd/systemd-resolved
root       741  0.0  0.0  16512  3712 ?        Ss   11:49   0:00 /usr/sbin/cron -f
root      1964  0.0  0.0  12436  3264 pts/0    Ss   12:12   0:00 -bash
root      2041  0.0  0.0  38364  3184 pts/0    R+   12:12   0:00 ps aux --sort=-%mem
root       628  0.0  0.0  28644  2960 ?        Ss   11:48   0:00 /lib/systemd/systemd-logind
message+   625  0.0  0.0  50288  2596 ?        Ss   11:48   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root       759  0.0  0.0  29756  2504 ?        Ss   11:49   0:00 /usr/sbin/rsyslogd -n -iNONE
root       613  0.0  0.0  21832  2304 ?        Ss   11:48   0:00 /lib/systemd/systemd-udevd
root       768  0.0  0.0  23932  2208 ?        Ss   11:49   0:00 /usr/sbin/NetworkManager --no-daemon
root       684  0.0  0.0  16208  1896 ?        Ss   11:48   0:00 /usr/sbin/acpid
root       772  0.0  0.0  12520  1772 ?        Ss   11:49   0:00 /usr/sbin/atd -f
---LISTEN---
State      Recv-Q Send-Q Local Address:Port Peer Address:Port Process
LISTEN     0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=862,fd=3))
LISTEN     0      511          0.0.0.0:80        0.0.0.0:*     users:(("nginx",pid=1245,fd=6))
LISTEN     0      128             [::]:22           [::]:*     users:(("sshd",pid=862,fd=4))
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/hosts; echo '---NGINX---'; ls -la /etc/nginx/sites-enabled /etc/nginx/conf.d 2>/dev/null; grep -RInE 'proxy_pass|upstream|server_name|listen|root ' /etc/nginx/nginx.conf /etc/nginx/sites-enabled /etc/nginx/conf.d 2>/dev/null`

```
root@ubuntu:~# cat /etc/hosts; echo '---NGINX---'; ls -la /etc/nginx/sites-enabled /etc/nginx/conf.d 2>/dev/null; grep -RInE 'proxy_pass|upstream|server_name|listen|root ' /etc/nginx/nginx.conf /etc/nginx/sites-enabled /etc/nginx/conf.d 2>/dev/null
127.0.0.1	localhost
127.0.1.1	ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---NGINX---
/etc/nginx/conf.d:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 8 root root 4096 Oct 17 11:49 ..

/etc/nginx/sites-enabled:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 11:50 .
drwxr-xr-x 8 root root 4096 Oct 17 11:49 ..
lrwxrwxrwx 1 root root   34 Oct 17 11:50 default -> /etc/nginx/sites-available/default
/etc/nginx/sites-enabled/default:22:	listen 80 default_server;
/etc/nginx/sites-enabled/default:23:	listen [::]:80 default_server;
/etc/nginx/sites-enabled/default:27:	root /var/www/html;
/etc/nginx/sites-enabled/default:30:	server_name _;
/etc/nginx/sites-enabled/default:48:#	listen 443 ssl default_server;
/etc/nginx/sites-enabled/default:49:#	listen [::]:443 ssl default_server;
/etc/nginx/sites-enabled/default:80:#	server_name example.com;
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /; echo '---DF---'; df -hT; echo '---MOUNT---'; mount; echo '---FSTAB---'; cat /etc/fstab; echo '---ALT---'; ls -la /mnt /media /data /backup /records /operations 2>/dev/null`

```
root@ubuntu:~# ls -la /; echo '---DF---'; df -hT; echo '---MOUNT---'; mount; echo '---FSTAB---'; cat /etc/fstab; echo '---ALT---'; ls -la /mnt /media /data /backup /records /operations 2>/dev/null
total 84
drwxr-xr-x  20 root root 4096 Oct 17 11:48 .
drwxr-xr-x  20 root root 4096 Oct 17 11:48 ..
lrwxrwxrwx   1 root root    7 Apr  9  2018 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr  9  2018 boot
drwxr-xr-x  19 root root 3960 Oct 17 12:12 dev
drwxr-xr-x  98 root root 4096 Oct 17 11:49 etc
drwxr-xr-x   2 root root 4096 Oct 17 11:48 home
lrwxrwxrwx   1 root root    7 Apr  9  2018 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr  9  2018 lib64 -> usr/lib64
drwx------   2 root root 4096 Oct 17 11:48 lost+found
drwxr-xr-x   2 root root 4096 Oct 17 11:48 media
drwxr-xr-x   2 root root 4096 Oct 17 11:48 mnt
drwxr-xr-x   3 root root 4096 Oct 17 11:48 opt
dr-xr-xr-x 268 root root    0 Oct 17 11:48 proc
drwx------   5 root root 4096 Oct 17 12:12 root
drwxr-xr-x  28 root root  900 Oct 17 12:12 run
lrwxrwxrwx   1 root root    8 Apr  9  2018 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Oct 17 11:48 srv
dr-xr-xr-x  13 root root    0 Oct 17 11:48 sys
drwxrwxrwt   2 root root 4096 Oct 17 11:49 tmp
drwxr-xr-x  10 root root 4096 Oct 17 11:48 usr
drwxr-xr-x  14 root root 4096 Oct 17 11:48 var
---DF---
Filesystem     Type      Size  Used Avail Use% Mounted on
udev           devtmpfs  7.8G     0  7.8G   0% /dev
tmpfs          tmpfs     1.6G  1.8M  1.6G   1% /run
/dev/sda1      ext4       98G  4.3G   89G   5% /
tmpfs          tmpfs     7.9G     0  7.9G   0% /dev/shm
tmpfs          tmpfs     5.0M     0  5.0M   0% /run/lock
tmpfs          tmpfs     7.9G     0  7.9G   0% /sys/fs/cgroup
/dev/sda15     vfat      105M  5.2M  100M   5% /boot/efi
tmpfs          tmpfs     1.6G     0  1.6G   0% /run/user/0
---MOUNT---
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=8154660k,nr_inodes=2038665,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=1633976k,mode=755)
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,name=systemd)
/dev/sda15 on /boot/efi type vfat (rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro)
tmpfs on /run/user/0 type tmpfs (rw,nosuid,nodev,relatime,size=1633976k,mode=700)
---FSTAB---
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a device.
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
UUID=8a91e0e5-42da-49d3-a426-3bd76fa803f5 /               ext4    errors=remount-ro 0       1
UUID=7A3F-219C  /boot/efi       vfat    umask=0077      0       1
/swapfile       none            swap    sw              0       0
---ALT---
/media:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '---NET---'; ip -br a; ip r; cat /etc/hosts; echo '---SSH---'; ls -la /root/.ssh /home/*/.ssh 2>/dev/null; cat /root/.ssh/config /root/.ssh/known_hosts /home/*/.ssh/known_hosts 2>/dev/null; echo '---HIST---'; tail -200 /root/.bash_history /home/*/.bash_history 2>/dev/null; echo '---ENV---'; env; echo '---CONN---'; ss -tnp`

```
root@ubuntu:~# echo '---NET---'; ip -br a; ip r; cat /etc/hosts; echo '---SSH---'; ls -la /root/.ssh /home/*/.ssh 2>/dev/null; cat /root/.ssh/config /root/.ssh/known_hosts /home/*/.ssh/known_hosts 2>/dev/null; echo '---HIST---'; tail -200 /root/.bash_history /home/*/.bash_history 2>/dev/null; echo '---ENV---'; env; echo '---CONN---'; ss -tnp
---NET---
lo               UNKNOWN        127.0.0.1/8 ::1/128
ens33            UP             192.168.56.114/24 fe80::20c:29ff:fe8a:4d71/64
default via 192.168.56.1 dev ens33 proto dhcp metric 100
192.168.56.0/24 dev ens33 proto kernel scope link src 192.168.56.114 metric 100
127.0.0.1	localhost
127.0.1.1	ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---SSH---
/root/.ssh:
total 8
drwx------ 2 root root 4096 Oct 17 11:49 .
drwx------ 5 root root 4096 Oct 17 12:12 ..
---HIST---
==> /root/.bash_history <==
apt update
apt install -y htop curl wget
systemctl status ssh
ip addr show
ls -la /var/www/html
---ENV---
SHELL=/bin/bash
PWD=/root
LOGNAME=root
XDG_SESSION_TYPE=tty
HOME=/root
LANG=en_US.UTF-8
TERM=xterm-256color
USER=root
SHLVL=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
XDG_RUNTIME_DIR=/run/user/0
_=/usr/bin/env
---CONN---
State      Recv-Q Send-Q Local Address:Port   Peer Address:Port
a
ESTAB      0      0      192.168.56.114:22    192.168.56.1:53184 users:(("sshd",pid=862,fd=4))
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ss -lntp 2>/dev/null; echo '--- NEIGH ---'; ip neigh 2>/dev/null; echo '--- ROUTES ---'; ip route 2>/dev/null`

```
root@ubuntu:~# ss -lntp 2>/dev/null; echo '--- NEIGH ---'; ip neigh 2>/dev/null; echo '--- ROUTES ---'; ip route 2>/dev/null
State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=862,fd=3))
LISTEN 0      511          0.0.0.0:80        0.0.0.0:*     users:(("nginx",pid=1245,fd=6))
LISTEN 0      128             [::]:22           [::]:*     users:(("sshd",pid=862,fd=4))
--- NEIGH ---
192.168.56.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.56.2 dev ens33 lladdr 00:50:56:ec:4b:6a STALE
--- ROUTES ---
default via 192.168.56.1 dev ens33 proto dhcp metric 100
192.168.56.0/24 dev ens33 proto kernel scope link src 192.168.56.114 metric 100
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ command -v nmap >/dev/null && nmap -Pn -p22,80,443,3306,5432,8080,8443 --open 192.168.56.0/24 || for i in $(seq 1 254); do for p in 22 80 443 3306 5432 8080 8443; do timeout 0.1 bash -c "echo >/dev/tcp/192.168.56.$i/$p" 2>/dev/null && echo "192.168.56.$i:$p open"; done; done`

```
root@ubuntu:~# command -v nmap >/dev/null && nmap -Pn -p22,80,443,3306,5432,8080,8443 --open 192.168.56.0/24 || for i in $(seq 1 254); do for p in 22 80 443 3306 5432 8080 8443; do timeout 0.1 bash -c "echo >/dev/tcp/192.168.56.$i/$p" 2>/dev/null && echo "192.168.56.$i:$p open"; done; done
192.168.56.114:22 open
192.168.56.114:80 open
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '--- mounts ---'; mount | egrep -v 'proc|sys|cgroup|dev|run'; echo '--- docker ---'; (docker ps -a 2>/dev/null || podman ps -a 2>/dev/null); echo '--- db/archive candidates ---'; find / -xdev -type f \( -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.sql' -o -iname '*.dump' -o -iname '*.tar*' -o -iname '*.bak' -o -iname '*.zip' \) -printf '%s %p\n' 2>/dev/null | sort -nr | head -80`

```
root@ubuntu:~# echo '--- mounts ---'; mount | egrep -v 'proc|sys|cgroup|dev|run'; echo '--- docker ---'; (docker ps -a 2>/dev/null || podman ps -a 2>/dev/null); echo '--- db/archive candidates ---'; find / -xdev -type f \( -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.sql' -o -iname '*.dump' -o -iname '*.tar*' -o -iname '*.bak' -o -iname '*.zip' \) -printf '%s %p\n' 2>/dev/null | sort -nr | head -80
--- mounts ---
--- docker ---
--- db/archive candidates ---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/lib 2>/dev/null; echo '---LOG---'; ls -la /var/log 2>/dev/null | head -60; echo '---SVC---'; systemctl list-units --type=service --state=running 2>/dev/null; echo '---FIND---'; find /var/lib /var/log /opt /srv /srv /home -maxdepth 3 \( -name '*.db' -o -name '*.sqlite*' -o -name '*record*' -o -name '*ops*' -o -name '*dump*' \) 2>/dev/null | head -60`

```
root@ubuntu:~# ls -la /var/lib 2>/dev/null; echo '---LOG---'; ls -la /var/log 2>/dev/null | head -60; echo '---SVC---'; systemctl list-units --type=service --state=running 2>/dev/null; echo '---FIND---'; find /var/lib /var/log /opt /srv /srv /home -maxdepth 3 \( -name '*.db' -o -name '*.sqlite*' -o -name '*record*' -o -name '*ops*' -o -name '*dump*' \) 2>/dev/null | head -60
total 104
drwxr-xr-x 42 root root 4096 Oct 17 11:50 .
drwxr-xr-x 14 root root 4096 Oct 17 11:48 ..
drwxr-xr-x  2 root root 4096 Oct 17 11:49 apt
drwxr-xr-x  2 root root 4096 Oct 17 11:49 bluetooth
drwxr-xr-x  2 root root 4096 Oct 17 11:49 dbus
drwxr-xr-x  4 root root 4096 Oct 17 11:49 dhcp
drwxr-xr-x  7 root root 4096 Oct 17 11:49 dpkg
drwxr-xr-x  3 root root 4096 Oct 17 11:49 grub
drwxr-xr-x  2 root root 4096 Oct 17 11:49 logrotate
drwxr-xr-x  3 root root 4096 Oct 17 11:49 man-db
drwxr-xr-x  2 root root 4096 Oct 17 11:49 misc
drwxr-xr-x  2 root root 4096 Oct 17 11:49 NetworkManager
drwxr-xr-x  2 root root 4096 Oct 17 11:49 pam
drwxr-xr-x  3 root root 4096 Oct 17 11:49 php
drwxr-xr-x  2 root root 4096 Oct 17 11:49 plymouth
drwxr-xr-x  3 root root 4096 Oct 17 11:49 polkit-1
drwx------  2 root root 4096 Oct 17 11:49 private
drwxr-xr-x  2 root root 4096 Oct 17 11:49 sudo
drwxr-xr-x  3 root root 4096 Oct 17 11:49 systemd
drwxr-xr-x  2 root root 4096 Oct 17 11:49 ubuntu-drivers-common
drwxr-xr-x  3 root root 4096 Oct 17 11:49 ucfr
drwxr-xr-x  2 root root 4096 Oct 17 11:49 unattended-upgrades
drwxr-xr-x  2 root root 4096 Oct 17 11:49 update-notifier
drwxr-xr-x  2 root root 4096 Oct 17 11:49 vim
drwxr-xr-x  3 root root 4096 Oct 17 11:49 wireless-regdb
---LOG---
total 1052
drwxrwxr-x  13 root      syslog            4096 Oct 17 12:12 .
drwxr-xr-x  14 root      root              4096 Oct 17 11:48 ..
-rw-r-----   1 syslog    adm              28672 Oct 17 12:12 auth.log
-rw-r-----   1 syslog    adm              12251 Oct 17 11:49 auth.log.1
-rw-r--r--   1 root      root              8018 Oct 17 11:49 bootstrap.log
drwxr-xr-x   2 root      root              4096 Oct 17 11:49 apt
-rw-r-----   1 syslog    adm              45207 Oct 17 12:12 kern.log
-rw-r-----   1 syslog    adm              13955 Oct 17 11:49 kern.log.1
drwxr-xr-x   2 root      root              4096 Oct 17 11:49 installer
-rw-rw-r--   1 root      utmp            38400 Oct 17 12:12 lastlog
drwxr-sr-x+  3 root      systemd-journal 4096 Oct 17 11:49 journal
-rw-r-----   1 syslog    adm             119834 Oct 17 12:12 syslog
-rw-r-----   1 syslog    adm              32817 Oct 17 11:49 syslog.1
-rw-r-----   1 syslog    adm              16243 Oct 17 12:12 nginx-access.log
-rw-r-----   1 www-data adm               1246 Oct 17 12:10 nginx-error.log
-rw-------   1 root      root                 0 Oct 17 11:49 wtmp
---SVC---
  UNIT                         LOAD   ACTIVE SUB     DESCRIPTION
  NetworkManager.service       loaded active running Network Manager
  accounts-daemon.service      loaded active running Accounts Service
  acpid.service                loaded active running ACPI event daemon
  cron.service                 loaded active running Regular background program processing daemon
  dbus.service                 loaded active running D-Bus System Message Bus
  nginx.service                loaded active running A high performance web server and a reverse proxy server
  rsyslog.service              loaded active running System Logging Service
  ssh.service                  loaded active running OpenBSD Secure Shell server
  systemd-journald.service     loaded active running Journal Service
  systemd-logind.service       loaded active running Login Service
  systemd-resolved.service     loaded active running Network Name Resolution
  systemd-udevd.service        loaded active running udev Kernel Device Manager

LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.

12 loaded units listed.
---FIND---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/www; echo ---FIND---; find /var/www -maxdepth 4 -type f 2>/dev/null | head -200; echo ---NGINX---; cat /etc/nginx/sites-enabled/* 2>/dev/null; echo ---ACCESS---; tail -60 /var/log/nginx/nginx-access.log 2>/dev/null`

```
root@ubuntu:~# ls -la /var/www; echo ---FIND---; find /var/www -maxdepth 4 -type f 2>/dev/null | head -200; echo ---NGINX---; cat /etc/nginx/sites-enabled/* 2>/dev/null; echo ---ACCESS---; tail -60 /var/log/nginx/nginx-access.log 2>/dev/null
/var/www:
total 12
drwxr-xr-x  3 root root 4096 Oct 17 11:49 .
drwxr-xr-x 14 root root 4096 Oct 17 11:48 ..
drwxr-xr-x  2 root root 4096 Oct 17 11:49 html
---FIND---
/var/www/html/index.html
---NGINX---
# Default server configuration
#
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	# SSL configuration
	#
	# listen 443 ssl default_server;
	# listen [::]:443 ssl default_server;
	#
	# Note: You should disable gzip for SSL traffic.
	# See: https://bugs.debian.org/773332
	#
	# Read up on ssl_ciphers to ensure a secure configuration.
	# See: https://bugs.debian.org/765782
	#
	# Self signed certs generated by the ssl-cert package
	# Don't use them in a production server!
	#
	# include snippets/snakeoil.conf;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

	# pass PHP scripts to FastCGI server
	#
	#location ~ \.php$ {
	#	include snippets/fastcgi-php.conf;
	#
	#	# With php-fpm (or other unix sockets):
	#	fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
	#}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
}

# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}
---ACCESS---
192.168.56.1 - - [17/Oct/2026:11:50:14 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36"
192.168.56.1 - - [17/Oct/2026:11:50:15 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://192.168.56.114/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36"
192.168.56.1 - - [17/Oct/2026:11:53:41 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.58.0"
192.168.56.1 - - [17/Oct/2026:12:01:27 +0000] "HEAD / HTTP/1.0" 200 0 "-" "Nmap Scripting Engine"
192.168.56.1 - - [17/Oct/2026:12:01:28 +0000] "GET /robots.txt HTTP/1.1" 404 153 "-" "curl/7.58.0"
192.168.56.1 - - [17/Oct/2026:12:04:09 +0000] "GET /.git/config HTTP/1.1" 404 153 "-" "Mozilla/5.0"
192.168.56.1 - - [17/Oct/2026:12:04:10 +0000] "GET /admin HTTP/1.1" 404 153 "-" "Mozilla/5.0"
192.168.56.1 - - [17/Oct/2026:12:04:10 +0000] "GET /phpinfo.php HTTP/1.1" 404 153 "-" "Mozilla/5.0"
192.168.56.1 - - [17/Oct/2026:12:04:11 +0000] "GET /server-status HTTP/1.1" 404 153 "-" "Mozilla/5.0"
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ getent passwd | awk -F: '$3>=1000 && $3<65534 {print}'; ls -la /home /opt /srv /usr/local 2>/dev/null; find / -xdev -type f \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*dump*' \) 2>/dev/null | head -200`

```
root@ubuntu:~# getent passwd | awk -F: '$3>=1000 && $3<65534 {print}'; ls -la /home /opt /srv /usr/local 2>/dev/null; find / -xdev -type f \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*dump*' \) 2>/dev/null | head -200
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..

/usr/local:
total 40
drwxr-xr-x 10 root root 4096 Oct 17 11:48 .
drwxr-xr-x 10 root root 4096 Oct 17 11:48 ..
drwxr-xr-x  2 root root 4096 Oct 17 11:48 bin
drwxr-xr-x  2 root root 4096 Oct 17 11:48 etc
drwxr-xr-x  2 root root 4096 Oct 17 11:48 games
drwxr-xr-x  2 root root 4096 Oct 17 11:48 include
drwxr-xr-x  4 root root 4096 Oct 17 11:48 lib
drwxr-xr-x  2 root root 4096 Oct 17 11:48 man
drwxr-xr-x  2 root root 4096 Oct 17 11:48 sbin
drwxr-xr-x  6 root root 4096 Oct 17 11:48 share
drwxr-xr-x  2 root root 4096 Oct 17 11:48 src
/usr/share/doc/libarchive13/changelog.Debian.gz
/usr/share/doc/libarchive13/copyright
/usr/share/man/man1/archive.1.gz
/usr/share/php/PEAR/Archive/Tar.php
/usr/lib/x86_64-linux-gnu/libarchive.so.13.2.1
/usr/lib/x86_64-linux-gnu/libarchive.so.13
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/lib/dpkg/info/libarchive13:amd64.triggers
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ getent passwd | awk -F: '$3>=1000 || $1 ~ /(sql|db|backup|deploy|ops|record)/ {print}'; ss -lntup 2>/dev/null; ls -la /var/mail /var/spool/mail 2>/dev/null; find / -xdev -type f -mtime -7 -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -50`

```
root@ubuntu:~# getent passwd | awk -F: '$3>=1000 || $1 ~ /(sql|db|backup|deploy|ops|record)/ {print}'; ss -lntup 2>/dev/null; ls -la /var/mail /var/spool/mail 2>/dev/null; find / -xdev -type f -mtime -7 -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -50
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
tcp   LISTEN 0      128          0.0.0.0:22         0.0.0.0:*     users:(("sshd",pid=862,fd=3))
tcp   LISTEN 0      511          0.0.0.0:80         0.0.0.0:*     users:(("nginx",pid=1245,fd=6))
tcp   LISTEN 0      128             [::]:22            [::]:*     users:(("sshd",pid=862,fd=4))
udp   UNCONN 0      0       127.0.0.53%lo:53         0.0.0.0:*     users:(("systemd-resolve",pid=591,fd=13))
udp   UNCONN 0      0          192.168.56.114:68         0.0.0.0:*     users:(("dhclient",pid=804,fd=6))
1760703126.0000000000 /var/log/syslog
1760703126.0000000000 /var/log/auth.log
1760703126.0000000000 /var/log/kern.log
1760703125.0000000000 /var/log/nginx/nginx-access.log
1760703018.0000000000 /var/log/nginx/nginx-error.log
1760702992.0000000000 /root/.bash_history
1760701920.0000000000 /var/log/lastlog
1760701794.0000000000 /var/lib/dpkg/status
1760701794.0000000000 /var/lib/dpkg/available
1760701788.0000000000 /var/lib/apt/extended_states
1760701771.0000000000 /var/backups/dpkg.status.0
1760701769.0000000000 /var/backups/apt.extended_states.0
1760701758.0000000000 /var/log/nginx/access.log
1760701758.0000000000 /var/log/nginx/error.log
1760701744.0000000000 /var/log/bootstrap.log
1760701741.0000000000 /var/log/installer/initial-status.gz
1760701740.0000000000 /var/log/dpkg.log
1760701737.0000000000 /var/log/apt/history.log
1760701737.0000000000 /var/log/apt/term.log
1760701731.0000000000 /var/lib/NetworkManager/NetworkManager.state
1760701728.0000000000 /var/lib/ucf/cache/:etc:default:grub
1760701721.0000000000 /etc/nginx/sites-available/default
1760701719.0000000000 /var/www/html/index.html
1760701716.0000000000 /etc/ssh/sshd_config
1760701714.0000000000 /etc/hosts
1760701712.0000000000 /etc/fstab
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root; echo '---passwd'; cat /etc/passwd; echo '---shadow'; cat /etc/shadow 2>/dev/null | head -n 20; echo '---nginx'; tail -n 50 /var/log/nginx/error.log 2>/dev/null; tail -n 50 /var/log/nginx/access.log 2>/dev/null; echo '---auth'; tail -n 50 /var/log/auth.log 2>/dev/null; echo '---pkgs'; dpkg -l 2>/dev/null | awk '{print $2}' | grep -Ei 'sql|db|ops|backup|archive|record|docker|podman|lxc|kvm|mysql|postgres|mongo|redis|nfs|samba'; echo '---cron'; ls -la /etc/cron* /var/spool/cron/crontabs 2>/dev/null; crontab -l 2>/dev/null`

```
root@ubuntu:~# ls -la /root; echo '---passwd'; cat /etc/passwd; echo '---shadow'; cat /etc/shadow 2>/dev/null | head -n 20; echo '---nginx'; tail -n 50 /var/log/nginx/error.log 2>/dev/null; tail -n 50 /var/log/nginx/access.log 2>/dev/null; echo '---auth'; tail -n 50 /var/log/auth.log 2>/dev/null; echo '---pkgs'; dpkg -l 2>/dev/null | awk '{print $2}' | grep -Ei 'sql|db|ops|backup|archive|record|docker|podman|lxc|kvm|mysql|postgres|mongo|redis|nfs|samba'; echo '---cron'; ls -la /etc/cron* /var/spool/cron/crontabs 2>/dev/null; crontab -l 2>/dev/null
total 36
drwx------  5 root root 4096 Oct 17 12:12 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..
-rw-------  1 root root  346 Oct 17 11:52 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 11:49 .cache
drwxr-xr-x  3 root root 4096 Oct 17 11:50 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 11:49 .ssh
---passwd
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
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
avahi-autoipd:x:109:114:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
usbmux:x:110:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
whoopsie:x:112:116::/nonexistent:/bin/false
speech-dispatcher:x:113:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh
kernoops:x:114:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
saned:x:115:118::/var/lib/saned:/usr/sbin/nologin
nm-openvpn:x:116:121:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
colord:x:117:122:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
hplip:x:118:7:HPLIP system user,,,:/var/run/hplip:/bin/false
geoclue:x:119:124::/var/lib/geoclue:/usr/sbin/nologin
pulse:x:120:125:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
usbmux:x:121:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
---shadow
root:*:19714:0:99999:7:::
daemon:*:19714:0:99999:7:::
bin:*:19714:0:99999:7:::
sys:*:19714:0:99999:7:::
sync:*:19714:0:99999:7:::
games:*:19714:0:99999:7:::
man:*:19714:0:99999:7:::
lp:*:19714:0:99999:7:::
mail:*:19714:0:99999:7:::
news:*:19714:0:99999:7:::
uucp:*:19714:0:99999:7:::
proxy:*:19714:0:99999:7:::
www-data:*:19714:0:99999:7:::
backup:*:19714:0:99999:7:::
list:*:19714:0:99999:7:::
irc:*:19714:0:99999:7:::
gnats:*:19714:0:99999:7:::
nobody:*:19714:0:99999:7:::
systemd-network:*:19714:0:99999:7:::
systemd-resolve:*:19714:0:99999:7:::
---nginx
---auth
Oct 17 11:48:41 ubuntu systemd-logind[628]: New seat seat0.
Oct 17 11:48:43 ubuntu sshd[862]: Server listening on 0.0.0.0 port 22.
Oct 17 11:48:43 ubuntu sshd[862]: Server listening on :: port 22.
Oct 17 11:50:02 ubuntu sshd[1271]: Accepted password for root from 192.168.56.1 port 53184 ssh2
Oct 17 11:50:02 ubuntu sshd[1271]: pam_unix(sshd:session): session opened for user root by (uid=0)
Oct 17 11:50:02 ubuntu systemd-logind[628]: New session 1 of user root.
Oct 17 12:12:06 ubuntu sudo:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/usr/bin/ls -la /root
---pkgs
libarchive13:amd64
---cron
/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..
-rw-r--r--  1 root root  201 Feb 13  2020 e2scrub_all
-rw-r--r--  1 root root  712 Jul 28  2025 php

/etc/cron.daily:
total 36
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..
-rwxr-xr-x  1 root root  376 Nov 22  2019 apport
-rwxr-xr-x  1 root root 1478 Apr  9  2020 apt-compat
-rwxr-xr-x  1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1187 Jan 18  2018 dpkg
-rwxr-xr-x  1 root root  377 Jan 21  2019 logrotate
-rwxr-xr-x  1 root root 1123 Jun 14  2018 man-db

/etc/cron.hourly:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..

/etc/cron.monthly:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..

/etc/cron.weekly:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:49 .
drwxr-xr-x 98 root root 4096 Oct 17 11:49 ..

/etc/crontab:
-rw-r--r-- 1 root root 722 Mar 22  2018 /etc/crontab
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/cron.d/php 2>/dev/null; echo '---CRONTAB---'; cat /etc/crontab 2>/dev/null; echo '---PHP-PKGS---'; dpkg -l 2>/dev/null | grep -i php; echo '---PHP-FILES---'; find /var/www /etc/php /var/lib/php -maxdepth 4 -type f 2>/dev/null | head -200`

```
root@ubuntu:~# cat /etc/cron.d/php 2>/dev/null; echo '---CRONTAB---'; cat /etc/crontab 2>/dev/null; echo '---PHP-PKGS---'; dpkg -l 2>/dev/null | grep -i php; echo '---PHP-FILES---'; find /var/www /etc/php /var/lib/php -maxdepth 4 -type f 2>/dev/null | head -200
# /etc/cron.d/php: crontab entries for the PHP session cleanup
#
# This file is managed by the php-common package

09,39 *     * * *     root   [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi
---CRONTAB---
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
---PHP-PKGS---
ii  libapache2-mod-php7.2                  7.2.24-0ubuntu0.18.04.17                 amd64        server-side, HTML-embedded scripting language (Apache 2.0 module)
ii  php-common                             1:60ubuntu1                            all          Common files for PHP packages
ii  php-pear                               1:1.10.5+submodules+notgz-1ubuntu1.18.04.1 all       PEAR Base System
ii  php7.2-cli                             7.2.24-0ubuntu0.18.04.17                 amd64        command-line interpreter for the PHP scripting language
ii  php7.2-common                          7.2.24-0ubuntu0.18.04.17                 amd64        documentation, examples and common module for PHP
ii  php7.2-json                            7.2.24-0ubuntu0.18.04.17                 amd64        JSON module for PHP
ii  php7.2-opcache                         7.2.24-0ubuntu0.18.04.17                 amd64        Zend OpCache module for PHP
ii  php7.2-readline                        7.2.24-0ubuntu0.18.04.17                 amd64        readline module for PHP
---PHP-FILES---
/var/www/html/index.html
/etc/php/7.2/apache2/conf.d/10-opcache.ini
/etc/php/7.2/apache2/conf.d/10-pdo.ini
/etc/php/7.2/apache2/conf.d/20-calendar.ini
/etc/php/7.2/apache2/conf.d/20-ctype.ini
/etc/php/7.2/apache2/conf.d/20-exif.ini
/etc/php/7.2/apache2/conf.d/20-fileinfo.ini
/etc/php/7.2/apache2/conf.d/20-ftp.ini
/etc/php/7.2/apache2/conf.d/20-gettext.ini
/etc/php/7.2/apache2/conf.d/20-iconv.ini
/etc/php/7.2/apache2/conf.d/20-json.ini
/etc/php/7.2/apache2/conf.d/20-phar.ini
/etc/php/7.2/apache2/conf.d/20-posix.ini
/etc/php/7.2/apache2/conf.d/20-readline.ini
/etc/php/7.2/apache2/conf.d/20-shmop.ini
/etc/php/7.2/apache2/conf.d/20-sockets.ini
/etc/php/7.2/apache2/conf.d/20-sysvmsg.ini
/etc/php/7.2/apache2/conf.d/20-sysvsem.ini
/etc/php/7.2/apache2/conf.d/20-sysvshm.ini
/etc/php/7.2/apache2/conf.d/20-tokenizer.ini
/etc/php/7.2/apache2/php.ini
/etc/php/7.2/cli/conf.d/10-opcache.ini
/etc/php/7.2/cli/conf.d/10-pdo.ini
/etc/php/7.2/cli/conf.d/20-calendar.ini
/etc/php/7.2/cli/conf.d/20-ctype.ini
/etc/php/7.2/cli/conf.d/20-exif.ini
/etc/php/7.2/cli/conf.d/20-fileinfo.ini
/etc/php/7.2/cli/conf.d/20-ftp.ini
/etc/php/7.2/cli/conf.d/20-gettext.ini
/etc/php/7.2/cli/conf.d/20-iconv.ini
/etc/php/7.2/cli/conf.d/20-json.ini
/etc/php/7.2/cli/conf.d/20-phar.ini
/etc/php/7.2/cli/conf.d/20-posix.ini
/etc/php/7.2/cli/conf.d/20-readline.ini
/etc/php/7.2/cli/conf.d/20-shmop.ini
/etc/php/7.2/cli/conf.d/20-sockets.ini
/etc/php/7.2/cli/conf.d/20-sysvmsg.ini
/etc/php/7.2/cli/conf.d/20-sysvsem.ini
/etc/php/7.2/cli/conf.d/20-sysvshm.ini
/etc/php/7.2/cli/conf.d/20-tokenizer.ini
/etc/php/7.2/cli/php.ini
/var/lib/php/modules/7.2/apache2/enabled_by_maint/ctype
/var/lib/php/modules/7.2/apache2/enabled_by_maint/exif
/var/lib/php/modules/7.2/apache2/enabled_by_maint/fileinfo
/var/lib/php/modules/7.2/apache2/enabled_by_maint/ftp
/var/lib/php/modules/7.2/apache2/enabled_by_maint/gettext
/var/lib/php/modules/7.2/apache2/enabled_by_maint/iconv
/var/lib/php/modules/7.2/apache2/enabled_by_maint/json
/var/lib/php/modules/7.2/apache2/enabled_by_maint/opcache
/var/lib/php/modules/7.2/apache2/enabled_by_maint/pdo
/var/lib/php/modules/7.2/apache2/enabled_by_maint/phar
/var/lib/php/modules/7.2/apache2/enabled_by_maint/posix
/var/lib/php/modules/7.2/apache2/enabled_by_maint/readline
/var/lib/php/modules/7.2/apache2/enabled_by_maint/shmop
/var/lib/php/modules/7.2/apache2/enabled_by_maint/sockets
/var/lib/php/modules/7.2/apache2/enabled_by_maint/sysvmsg
/var/lib/php/modules/7.2/apache2/enabled_by_maint/sysvsem
/var/lib/php/modules/7.2/apache2/enabled_by_maint/sysvshm
/var/lib/php/modules/7.2/apache2/enabled_by_maint/tokenizer
/var/lib/php/modules/7.2/cli/enabled_by_maint/ctype
/var/lib/php/modules/7.2/cli/enabled_by_maint/exif
/var/lib/php/modules/7.2/cli/enabled_by_maint/fileinfo
/var/lib/php/modules/7.2/cli/enabled_by_maint/ftp
/var/lib/php/modules/7.2/cli/enabled_by_maint/gettext
/var/lib/php/modules/7.2/cli/enabled_by_maint/iconv
/var/lib/php/modules/7.2/cli/enabled_by_maint/json
/var/lib/php/modules/7.2/cli/enabled_by_maint/opcache
/var/lib/php/modules/7.2/cli/enabled_by_maint/pdo
/var/lib/php/modules/7.2/cli/enabled_by_maint/phar
/var/lib/php/modules/7.2/cli/enabled_by_maint/posix
/var/lib/php/modules/7.2/cli/enabled_by_maint/readline
/var/lib/php/modules/7.2/cli/enabled_by_maint/shmop
/var/lib/php/modules/7.2/cli/enabled_by_maint/sockets
/var/lib/php/modules/7.2/cli/enabled_by_maint/sysvmsg
/var/lib/php/modules/7.2/cli/enabled_by_maint/sysvsem
/var/lib/php/modules/7.2/cli/enabled_by_maint/sysvshm
/var/lib/php/modules/7.2/cli/enabled_by_maint/tokenizer
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history /root/.zsh_history 2>/dev/null; find /root/.config /root/.local -maxdepth 4 -type f -print 2>/dev/null; grep -RInE '10\.[0-9]+\.[0-9]+\.[0-9]+|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|password|passwd|secret|token|mysql|psql|redis|ssh' /root /home /var/www /opt /srv 2>/dev/null | head -200`

```
root@ubuntu:~# cat /root/.bash_history /root/.zsh_history 2>/dev/null; find /root/.config /root/.local -maxdepth 4 -type f -print 2>/dev/null; grep -RInE '10\.[0-9]+\.[0-9]+\.[0-9]+|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|password|passwd|secret|token|mysql|psql|redis|ssh' /root /home /var/www /opt /srv 2>/dev/null | head -200
apt update
apt install -y htop curl wget
systemctl status ssh
ip addr show
ls -la /var/www/html
/root/.config/htop/htoprc
/root/.bash_history:3:systemctl status ssh
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '== vhosts =='; apache2ctl -S 2>&1 | head -80; echo '== nginx =='; nginx -T 2>&1 | grep -E 'server_name|root |listen ' | head -120; echo '== webroots =='; find /var/www /srv /opt -maxdepth 4 -type f -name '*.php' -printf '%TY-%Tm-%Td %p`

```
root@ubuntu:~# echo '== vhosts =='; apache2ctl -S 2>&1 | head -80; echo '== nginx =='; nginx -T 2>&1 | grep -E 'server_name|root |listen ' | head -120; echo '== webroots =='; find /var/www /srv /opt -maxdepth 4 -type f -name '*.php' -printf '%TY-%Tm-%Td %p
-bash: unexpected EOF while looking for matching `''
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /var/www /etc/nginx /etc/apache2 /opt /srv /root /home /tmp /var/tmp /usr/local -xdev -type f \( -iname '*.php' -o -iname '*.conf' -o -iname '*.sql' -o -iname '*.sql.gz' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' -o -iname '*.zip' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*evidence*' \) -printf '%TY-%Tm-%Td %TH:%TM %10s %p\n' 2>/dev/null | sort -r | head -200; echo '---apache---'; apache2ctl -S 2>&1; echo '---nginx---'; nginx -T 2>&1 | head -250`

```
root@ubuntu:~# find /var/www /etc/nginx /etc/apache2 /opt /srv /root /home /tmp /var/tmp /usr/local -xdev -type f \( -iname '*.php' -o -iname '*.conf' -o -iname '*.sql' -o -iname '*.sql.gz' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' -o -iname '*.zip' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*evidence*' \) -printf '%TY-%Tm-%Td %TH:%TM %10s %p
' 2>/dev/null | sort -r | head -200; echo '---apache---'; apache2ctl -S 2>&1; echo '---nginx---'; nginx -T 2>&1 | head -250
2026-10-17 11:49       1447 /etc/nginx/nginx.conf
2026-10-17 11:49       1125 /etc/nginx/fastcgi.conf
2026-10-17 11:49       7224 /etc/apache2/apache2.conf
2026-10-17 11:49       1332 /etc/apache2/sites-available/000-default.conf
2026-10-17 11:49        320 /etc/apache2/ports.conf
2026-10-17 11:49       1475 /etc/apache2/conf-available/security.conf
2026-10-17 11:49        631 /etc/apache2/conf-available/serve-cgi-bin.conf
2026-10-17 11:49        269 /etc/apache2/conf-available/other-vhosts-access-log.conf
2026-10-17 11:49        151 /etc/apache2/conf-available/localized-error-pages.conf
2026-10-17 11:49        140 /etc/apache2/conf-available/charset.conf
2026-10-17 11:49       1648 /etc/apache2/mods-available/ssl.conf
2026-10-17 11:49        616 /etc/apache2/mods-available/mime.conf
2026-10-17 11:49        428 /etc/apache2/mods-available/dir.conf
2026-10-17 11:49        390 /etc/apache2/mods-available/alias.conf
2026-10-17 11:49        142 /etc/apache2/mods-available/php7.2.conf
---apache---
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
VirtualHost configuration:
*:80                   127.0.1.1 (/etc/apache2/sites-enabled/000-default.conf:1)
ServerRoot: "/etc/apache2"
Main DocumentRoot: "/var/www/html"
Main ErrorLog: "/var/log/apache2/error.log"
Mutex default: dir="/var/run/apache2/" mechanism=default
PidFile: "/var/run/apache2/apache2.pid"
Define: DUMP_VHOSTS
Define: DUMP_RUN_CFG
User: name="www-data" id=33
Group: name="www-data" id=33
---nginx---
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# configuration file /etc/nginx/nginx.conf:
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
}

http {
	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
	ssl_prefer_server_ciphers on;

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	gzip on;
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}

# configuration file /etc/nginx/mime.types:
types {
	text/html                             html htm shtml;
	text/css                              css;
	text/xml                              xml;
	image/gif                             gif;
	image/jpeg                            jpeg jpg;
	application/javascript                js;
	application/json                      json;
	application/pdf                       pdf;
	application/zip                       zip;
	application/octet-stream              bin exe dll;
	image/png                             png;
}

# configuration file /etc/nginx/sites-enabled/default:
# Default server configuration
#
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	# SSL configuration
	#
	# listen 443 ssl default_server;
	# listen [::]:443 ssl default_server;
	#
	# Note: You should disable gzip for SSL traffic.
	# See: https://bugs.debian.org/773332
	#
	# Read up on ssl_ciphers to ensure a secure configuration.
	# See: https://bugs.debian.org/765782
	#
	# Self signed certs generated by the ssl-cert package
	# Don't use them in a production server!
	#
	# include snippets/snakeoil.conf;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

	# pass PHP scripts to FastCGI server
	#
	#location ~ \.php$ {
	#	include snippets/fastcgi-php.conf;
	#
	#	# With php-fpm (or other unix sockets):
	#	fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
	#}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
}

# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ id; groups; echo '---SUDO---'; sudo -n -l 2>&1; echo '---USERS---'; getent passwd | awk -F: '$3>=1000 && $3<65534'; echo '---HOME---'; ls -la /home 2>/dev/null; echo '---SSHKEYS---'; find /home /root -maxdepth 3 -type f 2>/dev/null | grep -E 'id_|authorized_keys|known_hosts' | head -50; echo '---HISTS---'; find /home /root -maxdepth 3 -type f 2>/dev/null | grep -E 'history|sh$' | head -50; echo '---LISTEN---'; ss -lntup 2>/dev/null; echo '---HOSTS---'; cat /etc/hosts /etc/resolv.conf 2>/dev/null; cat /home/*/.ssh/config /root/.ssh/config 2>/dev/null; echo '---OPREC---'; find /home /opt /srv /var /tmp -maxdepth 5 -type f -readable 2>/dev/null | grep -Ei 'oper|record|archive|sql|db|tar|tgz|zip' | head -100`

```
root@ubuntu:~# id; groups; echo '---SUDO---'; sudo -n -l 2>&1; echo '---USERS---'; getent passwd | awk -F: '$3>=1000 && $3<65534'; echo '---HOME---'; ls -la /home 2>/dev/null; echo '---SSHKEYS---'; find /home /root -maxdepth 3 -type f 2>/dev/null | grep -E 'id_|authorized_keys|known_hosts' | head -50; echo '---HISTS---'; find /home /root -maxdepth 3 -type f 2>/dev/null | grep -E 'history|sh$' | head -50; echo '---LISTEN---'; ss -lntup 2>/dev/null; echo '---HOSTS---'; cat /etc/hosts /etc/resolv.conf 2>/dev/null; cat /home/*/.ssh/config /root/.ssh/config 2>/dev/null; echo '---OPREC---'; find /home /opt /srv /var /tmp -maxdepth 5 -type f -readable 2>/dev/null | grep -Ei 'oper|record|archive|sql|db|tar|tgz|zip' | head -100
uid=0(root) gid=0(root) groups=0(root)
root
---SUDO---
Matching Defaults entries for root on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User root may run the following commands on ubuntu:
    (ALL : ALL) ALL
---USERS---
---HOME---
total 8
drwxr-xr-x  2 root root 4096 Oct 17 11:48 .
drwxr-xr-x 20 root root 4096 Oct 17 11:48 ..
---SSHKEYS---
---HISTS---
/root/.bash_history
---LISTEN---
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
tcp   LISTEN 0      128          0.0.0.0:22         0.0.0.0:*     users:(("sshd",pid=862,fd=3))
tcp   LISTEN 0      511          0.0.0.0:80         0.0.0.0:*     users:(("nginx",pid=1245,fd=6))
tcp   LISTEN 0      128             [::]:22            [::]:*     users:(("sshd",pid=862,fd=4))
udp   UNCONN 0      0       127.0.0.53%lo:53         0.0.0.0:*     users:(("systemd-resolve",pid=591,fd=13))
udp   UNCONN 0      0          192.168.56.114:68         0.0.0.0:*     users:(("dhclient",pid=804,fd=6))
---HOSTS---
127.0.0.1	localhost
127.0.1.1	ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 127.0.0.53
options edns0 trust-ad
---OPREC---
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/lib/dpkg/info/libarchive13:amd64.triggers
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ grep -RIlE 'OPR-|OPS-|opr_evidence|ora_dump|operational[ _-]?record' /etc /opt /srv /var/www /var/lib /root /tmp 2>/dev/null | grep -v '/var/lib/dpkg/' | head -50`

```
root@ubuntu:~# grep -RIlE 'OPR-|OPS-|opr_evidence|ora_dump|operational[ _-]?record' /etc /opt /srv /var/www /var/lib /root /tmp 2>/dev/null | grep -v '/var/lib/dpkg/' | head -50
root@ubuntu:~# 
```
root@ubuntu:~# 
```
