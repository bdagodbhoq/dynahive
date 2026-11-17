# AutoPT seed26 × HoneyLLM

`$ id; whoami; hostname; uname -a; pwd; ls -la /home 2>/dev/null; cat /etc/os-release 2>/dev/null`

```
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
root@ubuntu:~# root@ubuntu:~# 
```

`$ ls -la /root /opt /srv /var/backups 2>/dev/null; echo '---'; find /root /opt /srv /var /home -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*.tar' -o -iname '*.sql' \) 2>/dev/null | head -60`

```
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 8
drwxr-xr-x 2 root root 4096 Jan 26  2023 .
drwxr-xr-x 1 root root 4096 Jan 26  2023 ..
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
root@ubuntu:~# bash: syntax error near unexpected token `('
root@ubuntu:~# root@ubuntu:~# 
```

`$ find / -xdev -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*evidence*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.tar' -o -iname '*.db' \) 2>/dev/null | head -300`

```
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 20 root root 4096 Jan  5  2023 ..
PRETTY_NAME="Ubuntu 20.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="20.04"
VERSION="20.04.5 LTS (Focal Fossa)"
VERSION_CODENAME=focal
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=focal
-bash: syntax error near unexpected token `('
-bash: syntax error near unexpected token `('
root@ubuntu:~# root@ubuntu:~# 
```

`$ find / -iname '*operational*' 2>/dev/null | head -30; find / -iname '*opr*' 2>/dev/null | head -30; find / -iname '*archive*' 2>/dev/null | head -30; find / -iname '*record*' 2>/dev/null | grep -v -E '/(proc|sys)/' | head -30`

```
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
root@ubuntu:~# ls -la /root /opt /srv /var/backups 2>/dev/null; echo '---'; find /root /opt /srv /var /home -maxdepth 5 ( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*.tar' -o -iname '*.sql' ) 2>/dev/null | head -60
/bin/bash: -c: line 1: syntax error near unexpected token `('
/bin/bash: -c: line 1: `ls -la /root /opt /srv /var/backups 2>/dev/null; echo '---'; find /root /opt /srv /var /home -maxdepth 5 ( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*.tar' -o -iname '*.sql' ) 2>/dev/null | head -60'
root@ubuntu:~# find / -xdev -type f ( -iname '*operational*' -o -iname '*opr*' -o -iname '*evidence*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.tar' -o -iname '*.db' ) 2>/dev/null | head -300
/bin/bash: -c: line 1: syntax error near unexpected token `('
/bin/bash: -c: line 1: `find / -xdev -type f ( -iname '*operational*' -o -iname '*opr*' -o -iname '*evidence*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.tar' -o -iname '*.db' ) 2>/dev/null | head -300'
root@ubuntu:~# find / -iname '*operational*' 2>/dev/null | head -30; find / -iname '*opr*' 2>/dev/null | head -30; find / -iname '*archive*' 2>/dev/null | head -30; find / -iname '*record*' 2>/dev/null | grep -v -E '/(proc|sys)/' | head -30
/usr/lib/x86_64-linux-gnu/libarchive.so.13
/usr/lib/x86_64-linux-gnu/libarchive.so.13.6.2
/usr/share/doc/libarchive13
/usr/share/doc/libarchive13/changelog.Debian.gz
/usr/share/doc/libarchive13/copyright
/usr/share/doc/libarchive13/NEWS.gz
/usr/share/man/man5/libarchive-formats.5.gz
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/lib/dpkg/info/libarchive13:amd64.triggers
/usr/src/linux-headers-5.15.0-58/scripts/recordmcount.pl
/usr/src/linux-headers-5.15.0-58-generic/scripts/recordmcount.pl
root@ubuntu:~# root@ubuntu:~# 
```

`$ find /opt /srv /var/www /tmp /mnt /data /app /root /home -type f 2>/dev/null | grep -Ei 'oper|opr|archive|evidence|record|dump|\.sql|\.db|\.tar' | head -200`

```
root@ubuntu:~# root@ubuntu:~# 
```

`$ ss -lntp; echo '---PS---'; ps aux | grep -Ei 'mysql|maria|postgres|mongo|redis|apache|nginx|httpd|docker|java|python|node' | grep -v grep; echo '---DIRS---'; ls -la /var/lib/mysql /var/lib/postgresql /var/www /srv /opt /data /app 2>/dev/null; echo '---HIST---'; tail -n 40 /root/.bash_history 2>/dev/null`

```
State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess
LISTEN 0      4096      127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=531,fd=13))
LISTEN 0      128               0.0.0.0:22       0.0.0.0:*    users:(("sshd",pid=802,fd=3))
LISTEN 0      128                  [::]:22          [::]:*    users:(("sshd",pid=802,fd=4))
---PS---
root         531  0.0  0.2  25236  5512 ?        Ss   Jan05   0:00 /lib/systemd/systemd-resolved
root         802  0.0  0.3  15444  7284 ?        Ss   Jan05   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
---DIRS---
/opt:
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 20 root root 4096 Jan  5  2023 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 20 root root 4096 Jan  5  2023 ..

/var/www:
total 12
drwxr-xr-x  3 root root 4096 Jan  5  2023 .
drwxr-xr-x 14 root root 4096 Jan  5  2023 ..
drwxr-xr-x  2 root root 4096 Jan  5  2023 html
---HIST---
root@ubuntu:~# root@ubuntu:~# 
```

`$ ls -la /tmp /mnt /media /var/backups /usr/local /etc /var/lib 2>/dev/null; find / -xdev -type f 2>/dev/null | grep -Ei 'oper|opr|archive|evidence|record|dump|\.sql|\.db|\.tar' | head -50`

```
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 8
drwxr-xr-x 1 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
total 28
drwx------ 1 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
-rw-r--r-- 1 root root  571 Apr 10  2021 .bashrc
drwx------ 2 root root 4096 Jan  5  2023 .cache
drwxr-xr-x 3 root root 4096 Jan  5  2023 .local
-rw-r--r-- 1 root root  161 Jul  9  2019 .profile
drwx------ 2 root root 4096 Jan  5  2023 .ssh

/opt:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..

/srv:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..

/var/backups:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
---
bash: -c: line 1: syntax error near unexpected token `('
bash: -c: line 1: syntax error near unexpected token `('
---
State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
LISTEN 0      4096         0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=529,fd=3))
LISTEN 0      4096            [::]:22           [::]:*     users:(("sshd",pid=529,fd=4))
---PS---
root         529  0.0  0.2  15428  8420 ?        Ss   Jan05   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         812  0.0  0.2  17048  9152 ?        Ss   00:00   0:00 sshd: root@notty
---DIRS---
/opt:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..

/srv:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..

/var/www:
total 12
drwxr-xr-x 3 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
drwxr-xr-x 2 root root 4096 Jan  5  2023 html
---HIST---
total 8
drwxrwxrwt 1 root root 4096 Jan  5  2023 /tmp

/mnt:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..

/media:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..

/var/backups:
total 8
drwxr-xr-x 2 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..

/usr/local:
total 28
drwxr-xr-x 1 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
drwxr-xr-x 2 root root 4096 Jan  5  2023 bin
drwxr-xr-x 2 root root 4096 Jan  5  2023 etc
drwxr-xr-x 2 root root 4096 Jan  5  2023 games
drwxr-xr-x 2 root root 4096 Jan  5  2023 include
drwxr-xr-x 2 root root 4096 Jan  5  2023 lib
lrwxrwxrwx 1 root root    9 Jan  5  2023 man -> share/man
drwxr-xr-x 2 root root 4096 Jan  5  2023 sbin
drwxr-xr-x 3 root root 4096 Jan  5  2023 share
drwxr-xr-x 2 root root 4096 Jan  5  2023 src

/etc:
total 408
drwxr-xr-x 1 root root  4096 Jan  5  2023 .
drwxr-xr-x 1 root root  4096 Jan  5  2023 ..
-rw-r--r-- 1 root root  3040 Jan  5  2023 adduser.conf
drwxr-xr-x 1 root root  4096 Jan  5  2023 alternatives
drwxr-xr-x 1 root root  4096 Jan  5  2023 apt
-rw-r--r-- 1 root root  1994 Jan  5  2023 bash.bashrc
drwxr-xr-x 2 root root  4096 Jan  5  2023 bash_completion.d
-rw-r--r-- 1 root root    45 Jan  5  2023 bash_logout
-rw-r--r-- 1 root root   367 Jan  5  2023 bindresvport.blacklist
drwxr-xr-x 2 root root  4096 Jan  5  2023 ca-certificates
-rw-r--r-- 1 root root  6301 Jan  5  2023 ca-certificates.conf
drwxr-xr-x 1 root root  4096 Jan  5  2023 cron.d
drwxr-xr-x 1 root root  4096 Jan  5  2023 cron.daily
drwxr-xr-x 1 root root  4096 Jan  5  2023 dbus-1
drwxr-xr-x 1 root root  4096 Jan  5  2023 default
-rw-r--r-- 1 root root   296 Jan  5  2023 debconf.conf
-rw-r--r-- 1 root root     5 Jan  5  2023 debian_version
drwxr-xr-x 1 root root  4096 Jan  5  2023 dpkg
-rw-r--r-- 1 root root   685 Jan  5  2023 environment
-rw-r--r-- 1 root root    37 Jan  5  2023 fstab
-rw-r--r-- 1 root root  2584 Jan  5  2023 gai.conf
-rw-r--r-- 1 root root    33 Jan  5  2023 hostname
-rw-r--r-- 1 root root   249 Jan  5  2023 hosts
drwxr-xr-x 1 root root  4096 Jan  5  2023 init.d
-rw-r--r-- 1 root root  1748 Jan  5  2023 inputrc
drwxr-xr-x 1 root root  4096 Jan  5  2023 iproute2
-rw-r--r-- 1 root root    27 Jan  5  2023 issue
-rw-r--r-- 1 root root    20 Jan  5  2023 issue.net
drwxr-xr-x 1 root root  4096 Jan  5  2023 kernel
drwxr-xr-x 1 root root  4096 Jan  5  2023 ld.so.conf.d
-rw-r--r-- 1 root root   191 Jan  5  2023 legal
lrwxrwxrwx 1 root root    27 Jan  5  2023 localtime -> /usr/share/zoneinfo/Etc/UTC
drwxr-xr-x 1 root root  4096 Jan  5  2023 logrotate.d
-rw-r--r-- 1 root root    54 Jan  5  2023 lsb-release
drwxr-xr-x 1 root root  4096 Jan  5  2023 modprobe.d
-rw-r--r-- 1 root root   523 Jan  5  2023 nsswitch.conf
drwxr-xr-x 2 root root  4096 Jan  5  2023 opt
lrwxrwxrwx 1 root root    21 Jan  5  2023 os-release -> ../usr/lib/os-release
-rw-r--r-- 1 root root   552 Jan  5  2023 pam.conf
drwxr-xr-x 1 root root  4096 Jan  5  2023 pam.d
-rw-r--r-- 1 root root  1071 Jan  5  2023 passwd
-rw-r--r-- 1 root root  1048 Jan  5  2023 profile
drwxr-xr-x 1 root root  4096 Jan  5  2023 profile.d
drwxr-xr-x 1 root root  4096 Jan  5  2023 python3
drwxr-xr-x 1 root root  4096 Jan  5  2023 resolvconf
-rw-r--r-- 1 root root    35 Jan  5  2023 resolv.conf
drwxr-xr-x 1 root root  4096 Jan  5  2023 security
drwxr-xr-x 1 root root  4096 Jan  5  2023 selinux
drwxr-xr-x 1 root root  4096 Jan  5  2023 skel
drwxr-xr-x 1 root root  4096 Jan  5  2023 ssh
drwxr-xr-x 1 root root  4096 Jan  5  2023 ssl
-rw-r--r-- 1 root root     0 Jan  5  2023 subgid
-rw-r--r-- 1 root root     0 Jan  5  2023 subuid
drwxr-xr-x 1 root root  4096 Jan  5  2023 systemd
drwxr-xr-x 1 root root  4096 Jan  5  2023 terminfo
-rw-r--r-- 1 root root    13 Jan  5  2023 timezone
drwxr-xr-x 1 root root  4096 Jan  5  2023 udev
drwxr-xr-x 1 root root  4096 Jan  5  2023 ufw
drwxr-xr-x 1 root root  4096 Jan  5  2023 update-motd.d

/var/lib:
total 52
drwxr-xr-x 1 root root 4096 Jan  5  2023 .
drwxr-xr-x 1 root root 4096 Jan  5  2023 ..
drwxr-xr-x 2 root root 4096 Jan  5  2023 apt
drwxr-xr-x 2 root root 4096 Jan  5  2023 dbus
drwxr-xr-x 1 root root 4096 Jan  5  2023 dpkg
drwxr-xr-x 2 root root 4096 Jan  5  2023 misc
drwxr-xr-x 1 root root 4096 Jan  5  2023 pam
drwxr-xr-x 2 root root 4096 Jan  5  2023 private
drwxr-xr-x 2 root root 4096 Jan  5  2023 python
drwxr-xr-x 2 root root 4096 Jan  5  2023 systemd
drwxr-xr-x 2 root root 4096 Jan  5  2023 ubuntu-advantage
/var/lib/dpkg/available
/var/lib/dpkg/status
/var/lib/dpkg/status-old
/var/lib/dpkg/info/dbus.conffiles
/var/lib/dpkg/info/dbus.list
/var/lib/dpkg/info/dbus.md5sums
/var/lib/dpkg/info/dbus.postinst
/var/lib/dpkg/info/dbus.postrm
/var/lib/dpkg/info/dbus.preinst
/var/lib/dpkg/info/dbus.prerm
/var/lib/dpkg/info/dbus-system-bus-common.conffiles
/var/lib/dpkg/info/dbus-system-bus-common.list
/var/lib/dpkg/info/dbus-system-bus-common.md5sums
/var/lib/dpkg/info/dbus-user-session.list
/var/lib/dpkg/info/dbus-user-session.md5sums
/etc/default/dbus
/etc/init.d/dbus
/etc/dbus-1/session.conf
/etc/dbus-1/system.conf
/usr/bin/dbus-cleanup-sockets
/usr/bin/dbus-daemon
/usr/bin/dbus-launch
/usr/bin/dbus-monitor
/usr/bin/dbus-run-session
/usr/bin/dbus-send
/usr/bin/dbus-update-activation-environment
/usr/lib/systemd/system/dbus-org.freedesktop.timesync1.service
/usr/lib/systemd/system/dbus.service
/usr/lib/systemd/system/dbus.socket
/usr/share/doc/dbus/README.Debian.gz
/usr/share/doc/dbus/changelog.Debian.gz
/usr/share/doc/dbus/copyright
root@ubuntu:~# root@ubuntu:~# 
```

`$ find / -xdev -type f 2>/dev/null | grep -Ei 'oper|opr|archiv|evid|record|dump|[.]sql|[.]db|[.]tar' | head -200`

```
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/lib/dpkg/info/libarchive13:amd64.triggers
/usr/lib/x86_64-linux-gnu/libarchive.so.13.5.2
/usr/share/doc/libarchive13/changelog.Debian.gz
/usr/share/doc/libarchive13/copyright
/usr/share/man/man1/bsdtar.1.gz
/usr/share/man/man5/archive_entry.5.gz
/usr/share/man/man5/archive_read.5.gz
/usr/share/man/man5/archive_write.5.gz
/usr/share/man/man5/archive_write_disk.5.gz
/usr/share/perl5/Archive/Tar.pm
/usr/share/perl5/Archive/Tar/Constant.pm
/usr/share/perl5/Archive/Tar/File.pm
/usr/share/perl5/Archive/Tar/Wrapper.pm
/usr/share/perl5/Archive/Zip.pm
/usr/share/perl5/Archive/Zip/Archive.pm
/usr/share/perl5/Archive/Zip/Member.pm
/usr/share/perl5/Archive/Zip/Tree.pm
/usr/share/perl5/Archive/Zip/FAQ.pod
/usr/share/perl5/Archive/Zip/MemberRead.pm
/usr/share/perl5/Archive/Zip/NewFileMember.pm
/usr/share/perl5/Archive/Zip/FileMember.pm
/usr/share/perl5/Archive/Zip/ZipFileMember.pm
/usr/share/perl5/Archive/Zip/StringMember.pm
/usr/share/perl5/Archive/Zip/DirectoryMember.pm
/usr/share/perl5/Archive/Zip/MemberRead.pm
/usr/share/perl5/Archive/Zip/MockFile.pm
/usr/share/perl5/Archive/Zip/BufferedFileMember.pm
/usr/share/perl5/Archive/Zip/FAQ.pod
/usr/share/perl5/Archive/Zip/Member.pm
/usr/share/perl5/Archive/Zip/ZipFileMember.pm
/usr/share/perl5/Archive/Zip/Tree.pm
/usr/share/perl5/Archive/Zip/Archive.pm
/usr/share/perl5/Archive/Zip/MemberRead.pm
/usr/share/perl5/Archive/Zip/DirectoryMember.pm
/usr/share/perl5/Archive/Zip/StringMember.pm
/usr/share/perl5/Archive/Zip/NewFileMember.pm
/usr/share/perl5/Archive/Zip/FileMember.pm
/usr/share/perl5/Archive/Zip/MockFile.pm
/usr/share/perl5/Archive/Zip/BufferedFileMember.pm
root@ubuntu:~# root@ubuntu:~# 
```

`$ find /home /root /srv /opt /var/www /data /app /etc /var/lib /var/log -type f \( -iname '*.sql' -o -iname '*.sqlite*' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*.gz' -o -iname '*record*' -o -iname '*evid*' -o -iname '*opr*' \) 2>/dev/null | head -200; echo '---PASSWD---'; cat /etc/passwd; echo '---HOME---'; ls -la /home 2>/dev/null; echo '---LOG---'; ls -la /var/log 2>/dev/null`

```
/var/log/apt/eipp.log.xz
/var/log/apt/history.log.1.gz
/var/log/apt/term.log.1.gz
/var/log/dpkg.log.1.gz
/var/log/alternatives.log.1.gz
/var/log/auth.log.1.gz
/var/log/bootstrap.log
/var/log/cloud-init.log.1.gz
/var/log/kern.log.1.gz
/var/log/syslog.1.gz
/var/log/ufw.log.1.gz
---PASSWD---
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/usr/sbin:/usr/sbin/nologin
sys:x:3:3:sys:/usr/sbin:/usr/sbin/nologin
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
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management:/:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver:/:/usr/sbin/nologin
messagebus:x:102:105::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:103:106:systemd Time Synchronization:/:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
sshd:x:111:65534::/run/sshd:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
---HOME---
total 12
drwxr-xr-x  3 root   root   4096 Jan  5  2023 .
drwxr-xr-x 20 root   root   4096 Jan  5  2023 ..
drwxr-x---  4 ubuntu ubuntu 4096 Jan  5  2023 ubuntu
---LOG---
total 844
drwxrwxr-x  11 root      syslog            4096 Jan  5  2023 .
drwxr-xr-x  13 root      root              4096 Jan  5  2023 ..
-rw-r--r--   1 root      root                 0 Jan  5  2023 alternatives.log
-rw-r--r--   1 root      root              5263 Jan  5  2023 alternatives.log.1
-rw-r-----   1 syslog    adm              1807 Jan  5  2023 auth.log
-rw-r-----   1 syslog    adm              1498 Jan  5  2023 auth.log.1
-rw-r--r--   1 root      root                 0 Jan  5  2023 bootstrap.log
drwxr-xr-x   2 root      root              4096 Jan  5  2023 dist-upgrade
-rw-r-----   1 syslog    adm             19430 Jan  5  2023 dpkg.log
-rw-r-----   1 syslog    adm             16927 Jan  5  2023 kern.log
-rw-r-----   1 syslog    adm             25182 Jan  5  2023 syslog
-rw-r-----   1 syslog    adm                 0 Jan  5  2023 ufw.log
drwxr-xr-x   2 root      root              4096 Jan  5  2023 apt
drwxr-xr-x   2 root      root              4096 Jan  5  2023 journal
drwxr-xr-x   2 root      root              4096 Jan  5  2023 private
root@ubuntu:~# root@ubuntu:~# 
```

`$ ip a 2>/dev/null; echo ---ROUTE---; ip route 2>/dev/null; echo ---HOSTS---; cat /etc/hosts; echo ---RESOLV---; cat /etc/resolv.conf; echo ---ENV---; env; echo ---HISTROOT---; cat /root/.bash_history 2>/dev/null | tail -n 80; echo ---HISTUBU---; cat /home/ubuntu/.bash_history 2>/dev/null | tail -n 80`

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:8d:2a:71 brd ff:ff:ff:ff:ff:ff
    inet 192.168.56.101/24 brd 192.168.56.255 scope global dynamic eth0
       valid_lft 83412sec preferred_lft 83412sec
    inet6 fe80::a00:27ff:fe8d:2a71/64 scope link
       valid_lft forever preferred_lft forever
---ROUTE---
default via 192.168.56.1 dev eth0 proto dhcp metric 100
192.168.56.0/24 dev eth0 proto kernel scope link src 192.168.56.101 metric 100
192.168.56.1 dev eth0 proto dhcp scope link src 192.168.56.101 metric 100
---HOSTS---
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---RESOLV---
# This file is managed by systemd-resolved(8). Do not edit.
#
# This is a dynamic resolv.conf file for connecting local clients directly to
# the local DNS stub resolver.
nameserver 127.0.0.53
options edns0 trust-ad
search local
---ENV---
SHELL=/bin/bash
PWD=/root
LOGNAME=root
XDG_RUNTIME_DIR=/run/user/0
HOME=/root
LANG=C.UTF-8
TERM=dumb
USER=root
SHLVL=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SSH_CLIENT=192.168.56.1 49628 22
SSH_CONNECTION=192.168.56.1 49628 192.168.56.101 22
_=/usr/bin/env
---HISTROOT---
apt update
apt install -y openssh-server
systemctl enable --now ssh
adduser ubuntu
usermod -aG sudo ubuntu
---HISTUBU---
root@ubuntu:~# root@ubuntu:~# 
```

`$ mount | grep -vE 'proc|sysfs|devtmpfs|cgroup|tmpfs|devpts|mqueue|hugetlbfs|debugfs|securityfs|pstore|bpf|tracefs|configfs|fusectl|ramfs' ; echo '=== CRON ==='; ls -la /etc/cron* 2>/dev/null; cat /etc/crontab 2>/dev/null; echo '=== DOCKER ==='; which docker podman 2>/dev/null; docker ps -a 2>/dev/null; docker volume ls 2>/dev/null; echo '=== HIDDEN ==='; find /home /root /srv /opt /var/backups /mnt /media -maxdepth 3 -name '.*' -type d 2>/dev/null | head -50`

```
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro)
=== CRON ===
-rw-r--r-- 1 root root 1042 Feb 13  2023 /etc/crontab

/etc/cron.d:
total 24
drwxr-xr-x   2 root root 4096 Jan  5  2023 .
drwxr-xr-x 101 root root 4096 Jan  5  2023 ..
-rw-r--r--   1 root root  201 Feb 13  2023 e2scrub_all
-rw-r--r--   1 root root  712 Jan 17  2023 php
-rw-r--r--   1 root root  191 Dec  5  2022 popularity-contest

/etc/cron.daily:
total 44
drwxr-xr-x   2 root root 4096 Jan  5  2023 .
drwxr-xr-x 101 root root 4096 Jan  5  2023 ..
-rwxr-xr-x   1 root root  539 Jan 17  2023 apache2
-rwxr-xr-x   1 root root 1478 Apr  8  2022 apt-compat
-rwxr-xr-x   1 root root  123 Dec  5  2022 dpkg
-rwxr-xr-x   1 root root  377 Jan 17  2023 logrotate
-rwxr-xr-x   1 root root 1123 Jan 17  2023 man-db
-rwxr-xr-x   1 root root  539 Dec  5  2022 popularity-contest

/etc/cron.hourly:
total 8
drwxr-xr-x   2 root root 4096 Jan  5  2023 .
drwxr-xr-x 101 root root 4096 Jan  5  2023 ..

/etc/cron.monthly:
total 8
drwxr-xr-x   2 root root 4096 Jan  5  2023 .
drwxr-xr-x 101 root root 4096 Jan  5  2023 ..

/etc/cron.weekly:
total 8
drwxr-xr-x   2 root root 4096 Jan  5  2023 .
drwxr-xr-x 101 root root 4096 Jan  5  2023 ..

# /etc/crontab: system-wide crontab
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
=== DOCKER ===
=== HIDDEN ===
/root/.cache
/root/.cache/apt
/root/.cache/fontconfig
/root/.config
/root/.config/procps
/root/.local
/root/.local/share
/root/.ssh
/home/ubuntu/.cache
/home/ubuntu/.cache/motd.legal-displayed
/home/ubuntu/.config
/home/ubuntu/.config/procps
/home/ubuntu/.ssh
root@ubuntu:~# root@ubuntu:~# 
```

`$ mount | grep -Ev 'proc|sysfs|cgroup|devpts|tmpfs|overlay'; echo '--- fstab'; cat /etc/fstab; echo '--- dirs'; ls -la /mnt /media /srv /var/backups 2>/dev/null; echo '--- archives'; find / -xdev \( -name '*.tar*' -o -name '*.tgz' -o -name '*.sql' -o -name '*.db' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*oper*' \) -not -path '/proc/*' -not -path '/sys/*' -not -path '/usr/*' 2>/dev/null | head -80`

```
-bash: syntax error near unexpected token `('
root@ubuntu:~# root@ubuntu:~# 
```

`$ mount; echo ---FSTAB---; cat /etc/fstab 2>/dev/null; echo ---DF---; df -hT; echo ---MOUNTDIRS---; ls -la /mnt /media /srv /opt /var/backups 2>/dev/null`

```
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,relatime,size=1956000k,nr_inodes=489000,mode=755,inode64)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,nodev,size=398180k,mode=755,inode64)
/dev/sda15 on /boot/efi type vfat (rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=mixed,errors=remount-ro)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
efivarfs on /sys/firmware/efi/efivars type efivarfs (rw,nosuid,nodev,noexec,relatime)
bpf on /sys/fs/bpf type bpf (rw,nosuid,nodev,noexec,relatime,mode=700)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=48,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=18862)
mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,nosuid,nodev,noexec,relatime)
tracefs on /sys/kernel/tracing type tracefs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /run/user/0 type tmpfs (rw,nosuid,nodev,relatime,size=398176k,nr_inodes=99544,mode=700,inode64)
---FSTAB---
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
UUID=2f86fa55-7a9c-4c6c-9c1e-64f5c8250a12 /               ext4    defaults        0       1
UUID=8B31-7A72  /boot/efi       vfat    umask=0077      0       1
---DF---
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sda1      ext4    20G  2.3G   17G  13% /
tmpfs          tmpfs  389M  1.2M  388M   1% /run
devtmpfs       devtmpfs 1.9G     0  1.9G   0% /dev
tmpfs          tmpfs  1.9G     0  1.9G   0% /dev/shm
tmpfs          tmpfs  5.0M     0  5.0M   0% /run/lock
/dev/sda15     vfat   105M  6.1M   99M   6% /boot/efi
tmpfs          tmpfs  389M  4.0K  389M   1% /run/user/0
---MOUNTDIRS---
/media:
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 20 root root 4096 Jan  5  2023 ..

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 20 root root 4096 Jan  5  2023 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 20 root root 4096 Jan  5  2023 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 20 root root 4096 Jan  5  2023 ..

/var/backups:
total 8
drwxr-xr-x  2 root root 4096 Jan  5  2023 .
drwxr-xr-x 14 root root 4096 Jan  5  2023 ..
root@ubuntu:~# root@ubuntu:~# 
```

`$ id; whoami; hostname; uname -a; echo '=== CWD ==='; pwd; ls -la; echo '=== HOME ==='; ls -la ~ 2>/dev/null; echo '=== RECORDS ==='; grep -rIl -e 'OPR-' -e 'OPS-' -e 'operational_record' /home /srv /opt /var/lib 2>/dev/null | head -20`

```
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
=== CWD ===
/root
total 32
drwx------  5 root root 4096 Jan 12  2023 .
drwxr-xr-x 19 root root 4096 Jan  5  2023 ..
-rw-------  1 root root  312 Jan 12  2023 .bash_history
-rw-r--r--  1 root root 3106 Dec  5  2019 .bashrc
drwx------  2 root root 4096 Jan  5  2023 .cache
drwx------  3 root root 4096 Jan  5  2023 .config
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwxr-xr-x  2 root root 4096 Jan 12  2023 scripts
=== HOME ===
total 32
drwx------  5 root root 4096 Jan 12  2023 .
drwxr-xr-x 19 root root 4096 Jan  5  2023 ..
-rw-------  1 root root  312 Jan 12  2023 .bash_history
-rw-r--r--  1 root root 3106 Dec  5  2019 .bashrc
drwx------  2 root root 4096 Jan  5  2023 .cache
drwx------  3 root root 4096 Jan  5  2023 .config
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwxr-xr-x  2 root root 4096 Jan 12  2023 scripts
=== RECORDS ===
/var/lib/ops/archive/operational_records_2022.sql
root@ubuntu:~# root@ubuntu:~# 
```
