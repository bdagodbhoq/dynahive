# AutoPT seed27 × HoneyGPT

`$ id; whoami; pwd; uname -a; ls -la`

```
root@ubuntu:~# id; whoami; pwd; uname -a; ls -la
uid=0(root) gid=0(root) groups=0(root)
root
/root
Linux user 5.4.0-159-generic #176-Ubuntu SMP Thu Aug 24 13:16:44 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
total 36
drwx------  5 root root 4096 Oct 18 10:37 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..
-rw-------  1 root root  728 Oct 18 10:36 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  3 root root 4096 Oct 18 10:36 .cache
drwx------  3 root root 4096 Oct 18 10:36 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 10:36 .ssh
-rw-------  1 root root  872 Oct 18 10:37 .viminfo
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null | tail -60; echo '---'; ls -la /opt /srv /var/backups 2>/dev/null`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null | tail -60; echo '---'; ls -la /opt /srv /var/backups 2>/dev/null
whoami
pwd
uname -a
ls -la /
cat /etc/os-release
df -h
free -h
ip addr show
ip route show
ls -la /etc
systemctl --failed
ls -la /var/log
uptime
ls -la /root
---
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..

/var/backups:
total 320
drwxr-xr-x  2 root root   4096 Oct 18 10:36 .
drwxr-xr-x 14 root root   4096 Oct 18 10:36 ..
-rw-r--r--  1 root root  32867 Oct 18 10:36 apt.extended_states.0
-rw-r--r--  1 root root 282714 Oct 18 10:36 dpkg.status.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*operational*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar' -o -iname '*.tar.gz' \) -printf '%p\t%s bytes\n' 2>/dev/null | head -300`

```
root@ubuntu:~# find / -xdev -type f \( -iname '*opr*' -o -iname '*ops*' -o -iname '*operational*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar' -o -iname '*.tar.gz' \) -printf '%p\t%s bytes\n' 2>/dev/null | head -300
/usr/bin/oprofiled	150560 bytes
/usr/bin/opreport	36376 bytes
/usr/bin/opannotate	40512 bytes
/usr/bin/oparchive	14368 bytes
/usr/lib/x86_64-linux-gnu/libopcodes-2.30-system.so	1694856 bytes
/usr/lib/x86_64-linux-gnu/libpython3.6m.so.1.0	4553984 bytes
/usr/lib/python3/dist-packages/apt/cache.py	39744 bytes
/usr/lib/python3/dist-packages/apt/progress/base.py	16850 bytes
/usr/lib/python3/dist-packages/apt/progress/text.py	9266 bytes
/usr/lib/python3/dist-packages/command_not_found/CommandNotFound.py	11142 bytes
/usr/lib/python3/dist-packages/command_not_found/db/creator.py	25437 bytes
/usr/lib/python3/dist-packages/command_not_found/db/__init__.py	464 bytes
/usr/lib/python3/dist-packages/command_not_found/db/__pycache__/creator.cpython-36.pyc	18761 bytes
/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py	49821 bytes
/usr/share/doc/oprofile/changelog.Debian.gz	2578 bytes
/usr/share/doc/oprofile/copyright	11341 bytes
/usr/share/man/man1/opannotate.1.gz	1236 bytes
/usr/share/man/man1/oparchive.1.gz	887 bytes
/usr/share/man/man1/opreport.1.gz	1294 bytes
/usr/share/man/man1/oprofile.1.gz	1740 bytes
/usr/share/man/man1/oprofiled.1.gz	1229 bytes
/usr/share/man/man8/operf.8.gz	1189 bytes
/usr/share/vim/vim80/doc/recording.txt	7080 bytes
/var/cache/debconf/config.dat	18436 bytes
/var/cache/debconf/templates.dat	267503 bytes
/var/lib/dpkg/info/oprofile.list	1036 bytes
/var/lib/dpkg/info/oprofile.md5sums	1146 bytes
/var/lib/dpkg/info/oprofile.postinst	447 bytes
/var/lib/dpkg/info/oprofile.postrm	444 bytes
/var/lib/dpkg/info/oprofile.prerm	438 bytes
/var/lib/dpkg/status	282714 bytes
/var/backups/dpkg.status.0	282714 bytes
/var/backups/apt.extended_states.0	32867 bytes
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /home /tmp /mnt /media 2>/dev/null; echo '---MOUNTS---'; mount; echo '---RECENT---'; find /home /tmp /mnt /media /opt /srv /var/backups -xdev -type f -mmin -1440 -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -100`

```
root@ubuntu:~# ls -la /home /tmp /mnt /media 2>/dev/null; echo '---MOUNTS---'; mount; echo '---RECENT---'; find /home /tmp /mnt /media /opt /srv /var/backups -xdev -type f -mmin -1440 -printf '%TY-%Tm-%Td %TH:%TM %s %p\n' 2>/dev/null | sort -r | head -100
/home:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..

/media:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..

/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..
---MOUNTS---
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=362000000k,nr_inodes=90500000,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=72593836k,mode=755)
/dev/mmcblk0p2 on / type ext4 (rw,relatime,errors=remount-ro)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,name=systemd)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
mqueue on /dev/mqueue type mqueue (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
configfs on /sys/kernel/config type configfs (rw,relatime)
tmpfs on /run/user/0 type tmpfs (rw,nosuid,nodev,relatime,size=72593836k,mode=700)
---RECENT---
2026-10-18 10:36 32867 /var/backups/apt.extended_states.0
2026-10-18 10:36 282714 /var/backups/dpkg.status.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ for d in /root /var/www /var/lib /data; do echo "== $d =="; ls -la "$d" 2>/dev/null; done; echo "== listening =="; ss -ltnp 2>/dev/null || netstat -ltnp 2>/dev/null; echo "== processes =="; ps -eo pid,user,args --sort=pid | head -80`

```
root@ubuntu:~# for d in /root /var/www /var/lib /data; do echo "== $d =="; ls -la "$d" 2>/dev/null; done; echo "== listening =="; ss -ltnp 2>/dev/null || netstat -ltnp 2>/dev/null; echo "== processes =="; ps -eo pid,user,args --sort=pid | head -80
== /root ==
total 36
drwx------  5 root root 4096 Oct 18 10:37 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..
-rw-------  1 root root  728 Oct 18 10:36 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  3 root root 4096 Oct 18 10:36 .cache
drwx------  3 root root 4096 Oct 18 10:36 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 10:36 .ssh
-rw-------  1 root root  872 Oct 18 10:37 .viminfo
== /var/www ==
== /var/lib ==
total 80
drwxr-xr-x 20 root root 4096 Oct 18 10:36 .
drwxr-xr-x 14 root root 4096 Oct 18 10:36 ..
drwxr-xr-x  5 root root 4096 Oct 18 10:36 apt
drwxr-xr-x  2 root root 4096 Oct 18 10:36 command-not-found
drwxr-xr-x  2 root root 4096 Oct 18 10:36 dbus
drwxr-xr-x  7 root root 4096 Oct 18 10:36 dpkg
drwxr-xr-x  2 root root 4096 Oct 18 10:36 git
drwxr-xr-x  2 root root 4096 Oct 18 10:36 logrotate
drwxr-xr-x  2 root root 4096 Oct 18 10:36 misc
drwxr-xr-x  2 root root 4096 Oct 18 10:36 pam
drwxr-xr-x  2 root root 4096 Oct 18 10:36 polkit-1
drwx------  2 root root 4096 Oct 18 10:36 private
drwxr-xr-x  2 root root 4096 Oct 18 10:36 python
drwxr-xr-x  2 root root 4096 Oct 18 10:36 sgml-base
drwxr-xr-x  2 root root 4096 Oct 18 10:36 snapd
drwxr-xr-x  2 root root 4096 Oct 18 10:36 sudo
drwxr-xr-x  6 root root 4096 Oct 18 10:36 systemd
drwxr-xr-x  2 root root 4096 Oct 18 10:36 ubuntu-release-upgrader
drwxr-xr-x  3 root root 4096 Oct 18 10:36 ucf
drwxr-xr-x  2 root root 4096 Oct 18 10:36 update-notifier
drwxr-xr-x  2 root root 4096 Oct 18 10:36 xml-core
== /data ==
== listening ==
State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
LISTEN 0      128    127.0.0.53%lo:53        0.0.0.0:*     users:(("systemd-resolve",pid=456,fd=13))
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=712,fd=3))
LISTEN 0      128             [::]:22           [::]:*     users:(("sshd",pid=712,fd=4))
== processes ==
  PID USER     COMMAND
    1 root     /sbin/init
    2 root     [kthreadd]
    3 root     [rcu_gp]
    4 root     [rcu_par_gp]
    6 root     [kworker/0:0H-kblockd]
    9 root     [mm_percpu_wq]
   10 root     [ksoftirqd/0]
   11 root     [rcu_sched]
   12 root     [migration/0]
  298 root     /lib/systemd/systemd-journald
  329 root     /lib/systemd/systemd-udevd
  456 systemd+ /lib/systemd/systemd-resolved
  481 systemd+ /lib/systemd/systemd-timesyncd
  598 root     /usr/sbin/cron -f
  604 message+ /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  635 root     /usr/sbin/rsyslogd -n
  712 root     /usr/sbin/sshd -D
  831 root     sshd: root@pts/0
  842 root     -bash
 1267 root     ps -eo pid,user,args --sort=pid
 1268 root     head -80
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ printf '%s\n' '--- root history ---'; tail -n 200 /root/.bash_history 2>/dev/null; printf '%s\n' '--- root ssh ---'; ls -la /root/.ssh 2>/dev/null; printf '%s\n' '--- record search ---'; find / -xdev \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) -type f 2>/dev/null | head -200`

```
root@ubuntu:~# printf '%s\n' '--- root history ---'; tail -n 200 /root/.bash_history 2>/dev/null; printf '%s\n' '--- root ssh ---'; ls -la /root/.ssh 2>/dev/null; printf '%s\n' '--- record search ---'; find / -xdev \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) -type f 2>/dev/null | head -200
--- root history ---
whoami
pwd
uname -a
ls -la /
cat /etc/os-release
df -h
free -h
ip addr show
ip route show
ls -la /etc
systemctl --failed
ls -la /var/log
uptime
ls -la /root
--- root ssh ---
total 8
drwx------ 2 root root 4096 Oct 18 10:36 .
drwx------ 5 root root 4096 Oct 18 10:37 ..
--- record search ---
/usr/bin/oprofiled
/usr/bin/opreport
/usr/bin/opannotate
/usr/bin/oparchive
/usr/lib/x86_64-linux-gnu/libopcodes-2.30-system.so
/usr/lib/python3/dist-packages/apt/cache.py
/usr/lib/python3/dist-packages/apt/progress/base.py
/usr/lib/python3/dist-packages/apt/progress/text.py
/usr/lib/python3/dist-packages/command_not_found/CommandNotFound.py
/usr/lib/python3/dist-packages/command_not_found/db/creator.py
/usr/lib/python3/dist-packages/command_not_found/db/__init__.py
/usr/lib/python3/dist-packages/command_not_found/db/__pycache__/creator.cpython-36.pyc
/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py
/usr/share/doc/oprofile/changelog.Debian.gz
/usr/share/doc/oprofile/copyright
/usr/share/man/man1/opannotate.1.gz
/usr/share/man/man1/oparchive.1.gz
/usr/share/man/man1/opreport.1.gz
/usr/share/man/man1/oprofile.1.gz
/usr/share/man/man1/oprofiled.1.gz
/usr/share/man/man8/operf.8.gz
/usr/share/vim/vim80/doc/recording.txt
/var/lib/dpkg/info/oprofile.list
/var/lib/dpkg/info/oprofile.md5sums
/var/lib/dpkg/info/oprofile.postinst
/var/lib/dpkg/info/oprofile.postrm
/var/lib/dpkg/info/oprofile.prerm
/var/lib/dpkg/status
/var/backups/dpkg.status.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '== mounts =='; findmnt -rno TARGET,SOURCE,FSTYPE | grep -vE '^/(proc|sys|dev|run) '; echo '== targeted search =='; find /mnt /media /opt /srv /var/backups /var/lib /home /root /tmp /var/tmp -type f \( -iname '*oper*' -o -iname '*opr*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*.dump' \) 2>/dev/null | head -300`

```
root@ubuntu:~# echo '== mounts =='; findmnt -rno TARGET,SOURCE,FSTYPE | grep -vE '^/(proc|sys|dev|run) '; echo '== targeted search =='; find /mnt /media /opt /srv /var/backups /var/lib /home /root /tmp /var/tmp -type f \( -iname '*oper*' -o -iname '*opr*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*evidence*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*.dump' \) 2>/dev/null | head -300
== mounts ==
/ /dev/mmcblk0p2 ext4
== targeted search ==
/var/lib/dpkg/info/oprofile.list
/var/lib/dpkg/info/oprofile.md5sums
/var/lib/dpkg/info/oprofile.postinst
/var/lib/dpkg/info/oprofile.postrm
/var/lib/dpkg/info/oprofile.prerm
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /root /home /opt /srv /var/backups /var/tmp /tmp /mnt /media /data -xdev -type f \( -iname '*record*' -o -iname '*operat*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.dump' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -printf '%s %p\n' 2>/dev/null | sort -nr | head -50`

```
root@ubuntu:~# find /root /home /opt /srv /var/backups /var/tmp /tmp /mnt /media /data -xdev -type f \( -iname '*record*' -o -iname '*operat*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.dump' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -printf '%s %p\n' 2>/dev/null | sort -nr | head -50
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root; echo '---HISTORY---'; cat /root/.bash_history 2>/dev/null | tail -100; echo '---CANDIDATES---'; find /var/www /usr/local /opt /srv /var/lib /var/opt /var/backups /var/tmp /tmp /mnt /media /data -maxdepth 5 -type f 2>/dev/null | grep -Ei 'oper|opr|ops|record|archive|dump|backup' | head -200; echo '---DIRS---'; ls -la /var/www /usr/local /opt /srv /var/lib /var/opt 2>/dev/null`

```
root@ubuntu:~# ls -la /root; echo '---HISTORY---'; cat /root/.bash_history 2>/dev/null | tail -100; echo '---CANDIDATES---'; find /var/www /usr/local /opt /srv /var/lib /var/opt /var/backups /var/tmp /tmp /mnt /media /data -maxdepth 5 -type f 2>/dev/null | grep -Ei 'oper|opr|ops|record|archive|dump|backup' | head -200; echo '---DIRS---'; ls -la /var/www /usr/local /opt /srv /var/lib /var/opt 2>/dev/null
total 36
drwx------  5 root root 4096 Oct 18 10:37 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..
-rw-------  1 root root  728 Oct 18 10:36 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  3 root root 4096 Oct 18 10:36 .cache
drwx------  3 root root 4096 Oct 18 10:36 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 18 10:36 .ssh
-rw-------  1 root root  872 Oct 18 10:37 .viminfo
---HISTORY---
whoami
pwd
uname -a
ls -la /
cat /etc/os-release
df -h
free -h
ip addr show
ip route show
ls -la /etc
systemctl --failed
ls -la /var/log
uptime
ls -la /root
---CANDIDATES---
/var/lib/dpkg/info/oprofile.list
/var/lib/dpkg/info/oprofile.md5sums
/var/lib/dpkg/info/oprofile.postinst
/var/lib/dpkg/info/oprofile.postrm
/var/lib/dpkg/info/oprofile.prerm
---DIRS---
/usr/local:
total 40
drwxr-xr-x 10 root root 4096 Oct 18 10:36 .
drwxr-xr-x 10 root root 4096 Oct 18 10:36 ..
drwxr-xr-x  2 root root 4096 Oct 18 10:36 bin
drwxr-xr-x  2 root root 4096 Oct 18 10:36 etc
drwxr-xr-x  2 root root 4096 Oct 18 10:36 games
drwxr-xr-x  2 root root 4096 Oct 18 10:36 include
drwxr-xr-x  2 root root 4096 Oct 18 10:36 lib
drwxr-xr-x  2 root root 4096 Oct 18 10:36 man
drwxr-xr-x  2 root root 4096 Oct 18 10:36 sbin
drwxr-xr-x  3 root root 4096 Oct 18 10:36 share
drwxr-xr-x  2 root root 4096 Oct 18 10:36 src

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 18 10:36 .
drwxr-xr-x 20 root root 4096 Oct 18 10:36 ..

/var/lib:
total 80
drwxr-xr-x 20 root root 4096 Oct 18 10:36 .
drwxr-xr-x 14 root root 4096 Oct 18 10:36 ..
drwxr-xr-x  5 root root 4096 Oct 18 10:36 apt
drwxr-xr-x  2 root root 4096 Oct 18 10:36 command-not-found
drwxr-xr-x  2 root root 4096 Oct 18 10:36 dbus
drwxr-xr-x  7 root root 4096 Oct 18 10:36 dpkg
drwxr-xr-x  2 root root 4096 Oct 18 10:36 git
drwxr-xr-x  2 root root 4096 Oct 18 10:36 logrotate
drwxr-xr-x  2 root root 4096 Oct 18 10:36 misc
drwxr-xr-x  2 root root 4096 Oct 18 10:36 pam
drwxr-xr-x  2 root root 4096 Oct 18 10:36 polkit-1
drwx------  2 root root 4096 Oct 18 10:36 private
drwxr-xr-x  2 root root 4096 Oct 18 10:36 python
drwxr-xr-x  2 root root 4096 Oct 18 10:36 sgml-base
drwxr-xr-x  2 root root 4096 Oct 18 10:36 snapd
drwxr-xr-x  2 root root 4096 Oct 18 10:36 sudo
drwxr-xr-x  6 root root 4096 Oct 18 10:36 systemd
drwxr-xr-x  2 root root 4096 Oct 18 10:36 ubuntu-release-upgrader
drwxr-xr-x  3 root root 4096 Oct 18 10:36 ucf
drwxr-xr-x  2 root root 4096 Oct 18 10:36 update-notifier
drwxr-xr-x  2 root root 4096 Oct 18 10:36 xml-core
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '==HOSTS=='; cat /etc/hosts 2>/dev/null; echo '==ADDR=='; ip -br addr 2>/dev/null; echo '==ROUTE=='; ip route 2>/dev/null; echo '==LISTEN=='; ss -lntup 2>/dev/null; echo '==PROCS=='; ps auxww --sort=-%mem 2>/dev/null | head -50; echo '==FSTAB=='; cat /etc/fstab 2>/dev/null; echo '==MOUNT=='; mount 2>/dev/null | grep -v -E 'proc|sysfs|devtmpfs|cgroup|tmpfs|overlay|securityfs|pstore|bpf|debugfs|tracefs|configfs|fusectl|mqueue|hugetlbfs'`

```
root@ubuntu:~# echo '==HOSTS=='; cat /etc/hosts 2>/dev/null; echo '==ADDR=='; ip -br addr 2>/dev/null; echo '==ROUTE=='; ip route 2>/dev/null; echo '==LISTEN=='; ss -lntup 2>/dev/null; echo '==PROCS=='; ps auxww --sort=-%mem 2>/dev/null | head -50; echo '==FSTAB=='; cat /etc/fstab 2>/dev/null; echo '==MOUNT=='; mount 2>/dev/null | grep -v -E 'proc|sysfs|devtmpfs|cgroup|tmpfs|overlay|securityfs|pstore|bpf|debugfs|tracefs|configfs|fusectl|mqueue|hugetlbfs'
==HOSTS==
127.0.0.1	localhost
127.0.1.1	user

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
==ADDR==
lo               UNKNOWN        127.0.0.1/8 ::1/128
ens33            UP             192.168.1.128/24 fe80::20c:29ff:fe7a:4d91/64
==ROUTE==
default via 192.168.1.1 dev ens33 proto dhcp metric 100
192.168.1.0/24 dev ens33 proto kernel scope link src 192.168.1.128 metric 100
==LISTEN==
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
udp   UNCONN 0      0      127.0.0.53%lo:53         0.0.0.0:*     users:(("systemd-resolve",pid=456,fd=12))
tcp   LISTEN 0      128    127.0.0.53%lo:53         0.0.0.0:*     users:(("systemd-resolve",pid=456,fd=13))
tcp   LISTEN 0      128          0.0.0.0:22         0.0.0.0:*     users:(("sshd",pid=712,fd=3))
tcp   LISTEN 0      128             [::]:22            [::]:*     users:(("sshd",pid=712,fd=4))
==PROCS==
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0 225764  9420 ?        Ss   10:36   0:01 /sbin/init
root         298  0.0  0.0  50392  6856 ?        Ss   10:36   0:00 /lib/systemd/systemd-journald
root         842  0.0  0.0  21784  5384 pts/0    Ss   10:37   0:00 -bash
root         712  0.0  0.0  72304  5040 ?        Ss   10:36   0:00 /usr/sbin/sshd -D
root         635  0.0  0.0  71732  4784 ?        Ssl  10:36   0:00 /usr/sbin/rsyslogd -n
root         831  0.0  0.0  72680  4256 ?        Ss   10:37   0:00 sshd: root@pts/0
systemd+     456  0.0  0.0  89072  4164 ?        Ssl  10:36   0:00 /lib/systemd/systemd-resolved
root         598  0.0  0.0  43356  3704 ?        Ss   10:36   0:00 /usr/sbin/cron -f
message+     604  0.0  0.0  50276  3628 ?        Ss   10:36   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
systemd+     481  0.0  0.0  70820  3488 ?        Ssl  10:36   0:00 /lib/systemd/systemd-timesyncd
root        1314  0.0  0.0  38312  3276 pts/0    R+   10:37   0:00 ps auxww --sort=-%mem
root        1315  0.0  0.0  14820  1080 pts/0    S+   10:37   0:00 head -50
==FSTAB==
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a device; this may
# be used with UUID= as a more robust way to name devices that works even if
# disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
/dev/mmcblk0p2  /               ext4    errors=remount-ro 0       1
==MOUNT==
/dev/mmcblk0p2 on / type ext4 (rw,relatime,errors=remount-ro)
root@ubuntu:~# 
```
root@ubuntu:~# 
```
