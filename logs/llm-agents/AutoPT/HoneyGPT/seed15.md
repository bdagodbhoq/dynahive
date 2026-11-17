# AutoPT seed15 × HoneyGPT

`$ id; whoami; pwd; hostname; uname -a; ls -la; sudo -n -l 2>/dev/null; cat /etc/os-release 2>/dev/null`

```
root@ubuntu:~# id; whoami; pwd; hostname; uname -a; ls -la; sudo -n -l 2>/dev/null; cat /etc/os-release 2>/dev/null
uid=0(root) gid=0(root) groups=0(root)
root
/root
ubuntu
Linux ubuntu 5.4.0-159-generic #176-Ubuntu SMP Fri Aug 11 08:37:18 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
total 32
drwx------  5 root root 4096 Oct 17 17:23 .
drwxr-xr-x 20 root root 4096 Oct 17 17:23 ..
-rw-------  1 root root  623 Oct 17 17:23 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 17:23 .cache
drwxr-xr-x  3 root root 4096 Oct 17 17:23 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 17:23 .ssh
User root may run the following commands on ubuntu:
    (ALL : ALL) ALL
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
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /root /home /opt /srv /var /etc -maxdepth 4 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*archive*' -o -iname '*record*' \) 2>/dev/null | head -60`

```
root@ubuntu:~# find /root /home /opt /srv /var /etc -maxdepth 4 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*archive*' -o -iname '*record*' \) 2>/dev/null | head -60
/var/cache/apt/archives
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/lib/dpkg/info/libarchive13:amd64.triggers
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.sqlite*' -o -iname '*.db' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -300`

```
root@ubuntu:~# find / \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.sqlite*' -o -iname '*.db' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -300
/var/cache/apt/archives/libsqlite3-0_3.22.0-1ubuntu0.7_amd64.deb
/var/cache/apt/archives/sqlite3_3.22.0-1ubuntu0.7_amd64.deb
/usr/lib/x86_64-linux-gnu/libsqlite3.so.0.8.6
/usr/lib/x86_64-linux-gnu/libsqlite3.so.0
/usr/share/doc/sqlite3/changelog.Debian.gz
/usr/share/doc/sqlite3/copyright
/usr/share/man/man1/sqlite3.1.gz
/usr/share/man/man3/sqlite3_backup.3.gz
/usr/share/man/man3/sqlite3_blob.3.gz
/usr/share/man/man3/sqlite3_changes.3.gz
/usr/share/man/man3/sqlite3_close.3.gz
/usr/share/man/man3/sqlite3_open.3.gz
/usr/share/man/man3/sqlite3_prepare.3.gz
/usr/share/man/man3/sqlite3_exec.3.gz
/usr/share/man/man3/sqlite3_wal_checkpoint.3.gz
/usr/share/man/man3/sqlite3.3.gz
/usr/share/mime/application/vnd.sqlite3.xml
/var/lib/dpkg/info/libsqlite3-0:amd64.list
/var/lib/dpkg/info/libsqlite3-0:amd64.md5sums
/var/lib/dpkg/info/libsqlite3-0:amd64.shlibs
/var/lib/dpkg/info/libsqlite3-0:amd64.symbols
/var/lib/dpkg/info/libsqlite3-0:amd64.triggers
/var/lib/dpkg/info/sqlite3.list
/var/lib/dpkg/info/sqlite3.md5sums
/var/lib/dpkg/info/sqlite3.postinst
/var/lib/dpkg/info/sqlite3.postrm
/var/lib/dpkg/info/sqlite3.preinst
/var/lib/dpkg/info/sqlite3.prerm
/var/lib/dpkg/info/sqlite3:amd64.list
/var/lib/dpkg/info/sqlite3:amd64.md5sums
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo ===HOSTS===; cat /etc/hosts; echo ===IFACE===; ip -o addr 2>/dev/null | awk '{print $2,$4}'; echo ===MOUNTS===; mount | grep -v -E 'proc|sys|cgroup|dev/pts'; echo ===SEARCH===; find / -maxdepth 4 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' \) -not -path '/usr/*' -not -path '/var/lib/dpkg/*' -not -path '/proc/*' 2>/dev/null | head -50`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo ===HOSTS===; cat /etc/hosts; echo ===IFACE===; ip -o addr 2>/dev/null | awk '{print $2,$4}'; echo ===MOUNTS===; mount | grep -v -E 'proc|sys|cgroup|dev/pts'; echo ===SEARCH===; find / -maxdepth 4 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' \) -not -path '/usr/*' -not -path '/var/lib/dpkg/*' -not -path '/proc/*' 2>/dev/null | head -50
id; whoami; pwd; hostname; uname -a; ls -la; sudo -n -l 2>/dev/null; cat /etc/os-release 2>/dev/null
find /root /home /opt /srv /var /etc -maxdepth 4 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*archive*' -o -iname '*record*' \) 2>/dev/null | head -60
find / \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.sqlite*' -o -iname '*.db' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -300
===HOSTS===
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
===IFACE===
lo 127.0.0.1/8
lo ::1/128
ens33 192.168.122.47/24
ens33 fe80::20c:29ff:fe8a:3d71/64
===MOUNTS===
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro,data=ordered)
tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /run/user/0 type tmpfs (rw,nosuid,nodev,relatime,size=148672000k,mode=700)
===SEARCH===
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ip neigh; arp -a; ip route; cat /etc/resolv.conf; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/known_hosts 2>/dev/null; grep -rIl -E '192\.168\.|10\.' /etc 2>/dev/null | head -20`

```
root@ubuntu:~# ip neigh; arp -a; ip route; cat /etc/resolv.conf; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/known_hosts 2>/dev/null; grep -rIl -E '192\.168\.|10\.' /etc 2>/dev/null | head -20
192.168.122.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.122.2 dev ens33 lladdr 00:50:56:e4:48:15 STALE
? (192.168.122.1) at 00:50:56:c0:00:08 [ether] on ens33
? (192.168.122.2) at 00:50:56:e4:48:15 [ether] on ens33
default via 192.168.122.1 dev ens33 proto dhcp metric 100 
192.168.122.0/24 dev ens33 proto kernel scope link src 192.168.122.47 metric 100 
192.168.122.1 dev ens33 proto dhcp scope link src 192.168.122.47 metric 100 
nameserver 192.168.122.2
search localdomain
total 8
drwx------ 2 root root 4096 Oct 17 17:23 .
drwx------ 5 root root 4096 Oct 17 17:23 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ip neigh; ss -tlnp; for p in 21 22 23 25 53 80 110 139 143 443 445 993 995 3306 3389 5432 5900 8080 8443; do timeout 1 bash -c "echo > /dev/tcp/192.168.122.1/$p" 2>/dev/null && echo "192.168.122.1:$p open"; done`

```
root@ubuntu:~# ip neigh; ss -tlnp; for p in 21 22 23 25 53 80 110 139 143 443 445 993 995 3306 3389 5432 5900 8080 8443; do timeout 1 bash -c "echo > /dev/tcp/192.168.122.1/$p" 2>/dev/null && echo "192.168.122.1:$p open"; done
192.168.122.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.122.2 dev ens33 lladdr 00:50:56:e4:48:15 STALE
State      Recv-Q Send-Q Local Address:Port               Peer Address:Port              
LISTEN     0      128    127.0.0.1:53                    0.0.0.0:*                  users:(("systemd-resolve",pid=614,fd=13))
LISTEN     0      128    0.0.0.0:22                      0.0.0.0:*                  users:(("sshd",pid=872,fd=3))
LISTEN     0      128    [::]:22                         [::]:*                     users:(("sshd",pid=872,fd=4))
192.168.122.1:53 open
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ip -brief addr; ip route; cat /etc/resolv.conf; timeout 5 dig @192.168.122.1 version.bind CH TXT +short; timeout 5 dig @192.168.122.1 axfr . +short 2>&1 | head -50; timeout 5 dig @192.168.122.1 ANY . +short 2>&1 | head -50`

```
root@ubuntu:~# ip -brief addr; ip route; cat /etc/resolv.conf; timeout 5 dig @192.168.122.1 version.bind CH TXT +short; timeout 5 dig @192.168.122.1 axfr . +short 2>&1 | head -50; timeout 5 dig @192.168.122.1 ANY . +short 2>&1 | head -50
lo               UNKNOWN        127.0.0.1/8 ::1/128
ens33            UP             192.168.122.47/24 fe80::20c:29ff:fe8a:3d71/64
default via 192.168.122.1 dev ens33 proto dhcp metric 100
192.168.122.0/24 dev ens33 proto kernel scope link src 192.168.122.47 metric 100
192.168.122.1 dev ens33 proto dhcp scope link src 192.168.122.47 metric 100
nameserver 192.168.122.2
search localdomain
"dnsmasq-2.79"
; Transfer failed.
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ip neigh; cat /etc/resolv.conf; cat /etc/hosts; for ip in 192.168.122.1 192.168.122.2; do for p in 22 80 443 53 3306 5432 6379 8080 9000; do timeout 1 bash -c "</dev/tcp/$ip/$p" 2>/dev/null && echo "$ip:$p open"; done; done`

```
root@ubuntu:~# ip neigh; cat /etc/resolv.conf; cat /etc/hosts; for ip in 192.168.122.1 192.168.122.2; do for p in 22 80 443 53 3306 5432 6379 8080 9000; do timeout 1 bash -c "</dev/tcp/$ip/$p" 2>/dev/null && echo "$ip:$p open"; done; done
192.168.122.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.122.2 dev ens33 lladdr 00:50:56:e4:48:15 STALE
nameserver 192.168.122.2
search localdomain
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
192.168.122.1:53 open
192.168.122.2:53 open
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ip -br a; ip route; ip neigh; mount | grep -vE 'proc|sys|dev|cgroup'; ss -lntup; ls -la /mnt /media /opt /srv /var/backups /root 2>/dev/null`

```
root@ubuntu:~# ip -br a; ip route; ip neigh; mount | grep -vE 'proc|sys|dev|cgroup'; ss -lntup; ls -la /mnt /media /opt /srv /var/backups /root 2>/dev/null
lo               UNKNOWN        127.0.0.1/8 ::1/128
ens33            UP             192.168.122.47/24 fe80::20c:29ff:fe8a:3d71/64
default via 192.168.122.1 dev ens33 proto dhcp metric 100
192.168.122.0/24 dev ens33 proto kernel scope link src 192.168.122.47 metric 100
192.168.122.1 dev ens33 proto dhcp scope link src 192.168.122.47 metric 100
192.168.122.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.122.2 dev ens33 lladdr 00:50:56:e4:48:15 STALE
tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /run/user/0 type tmpfs (rw,nosuid,nodev,relatime,size=148672000k,mode=700)
Netid  State   Recv-Q  Send-Q      Local Address:Port   Peer Address:Port  Process
tcp    LISTEN  0       128         127.0.0.1:53         0.0.0.0:*          users:(("systemd-resolve",pid=614,fd=13))
tcp    LISTEN  0       128         0.0.0.0:22           0.0.0.0:*          users:(("sshd",pid=872,fd=3))
tcp    LISTEN  0       128         [::]:22              [::]:*          users:(("sshd",pid=872,fd=4))
udp    UNCONN  0       0           127.0.0.1:53         0.0.0.0:*          users:(("systemd-resolve",pid=614,fd=12))
/mnt:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 17 17:23 ..

/media:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 17 17:23 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 17 17:23 ..

/root:
total 32
drwx------  5 root root 4096 Oct 17 17:23 .
drwxr-xr-x 20 root root 4096 Oct 17 17:23 ..
-rw-------  1 root root  623 Oct 17 17:23 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 17:23 .cache
drwxr-xr-x  3 root root 4096 Oct 17 17:23 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 17:23 .ssh

/srv:
total 8
drwxr-xr-x  2 root root 4096 Apr  9  2018 .
drwxr-xr-x 20 root root 4096 Oct 17 17:23 ..

/var/backups:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 17:23 .
drwxr-xr-x 1 root root 4096 Oct 17 17:23 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '---BASHRC-HISTORY---'; sed -n '1,200p' /root/.bash_history 2>/dev/null; echo '---SSH-DIR---'; ls -la /root/.ssh 2>/dev/null; echo '---SSH-CONFIG---'; cat /root/.ssh/config 2>/dev/null; echo '---KNOWN-HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null; echo '---ROOT-CONFIG-FILES---'; find /root/.config -maxdepth 4 -type f -print -exec sh -c 'echo "### $1"; sed -n "1,120p" "$1" 2>/dev/null' _ {} \; 2>/dev/null`

```
root@ubuntu:~# echo '---BASHRC-HISTORY---'; sed -n '1,200p' /root/.bash_history 2>/dev/null; echo '---SSH-DIR---'; ls -la /root/.ssh 2>/dev/null; echo '---SSH-CONFIG---'; cat /root/.ssh/config 2>/dev/null; echo '---KNOWN-HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null; echo '---ROOT-CONFIG-FILES---'; find /root/.config -maxdepth 4 -type f -print -exec sh -c 'echo "### $1"; sed -n "1,120p" "$1" 2>/dev/null' _ {} \; 2>/dev/null
---BASHRC-HISTORY---
id; whoami; pwd; hostname; uname -a; ls -la; sudo -n -l 2>/dev/null; cat /etc/os-release 2>/dev/null
find /root /home /opt /srv /var /etc -maxdepth 4 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*archive*' -o -iname '*record*' \) 2>/dev/null | head -60
find / \( -path /proc -o -path /sys -o -path /dev \) -prune -o -type f \( -iname '*operational*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*.sql' -o -iname '*.sqlite*' -o -iname '*.db' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.tgz' \) -print 2>/dev/null | head -300
---SSH-DIR---
total 8
drwx------ 2 root root 4096 Oct 17 17:23 .
drwx------ 5 root root 4096 Oct 17 17:23 ..
---SSH-CONFIG---
---KNOWN-HOSTS---
---ROOT-CONFIG-FILES---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root; echo '--- .bashrc ---'; cat /root/.bashrc 2>/dev/null; echo '--- .profile ---'; cat /root/.profile 2>/dev/null; echo '--- .cache ---'; find /root/.cache -maxdepth 2 -type f 2>/dev/null | while read f; do echo "== $f =="; cat "$f"; done | head -300`

```
root@ubuntu:~# ls -la /root; echo '--- .bashrc ---'; cat /root/.bashrc 2>/dev/null; echo '--- .profile ---'; cat /root/.profile 2>/dev/null; echo '--- .cache ---'; find /root/.cache -maxdepth 2 -type f 2>/dev/null | while read f; do echo "== $f =="; cat "$f"; done | head -300
total 32
drwx------  5 root root 4096 Oct 17 17:23 .
drwxr-xr-x 20 root root 4096 Oct 17 17:23 ..
-rw-------  1 root root  623 Oct 17 17:23 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 17:23 .cache
drwxr-xr-x  3 root root 4096 Oct 17 17:23 .config
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 17 17:23 .ssh
--- .bashrc ---
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
        color_prompt=yes
    else
        color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
--- .profile ---
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin directories
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
--- .cache ---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/resolv.conf; echo '---'; cat /etc/hosts; echo '---'; ip neigh show`

```
root@ubuntu:~# cat /etc/resolv.conf; echo '---'; cat /etc/hosts; echo '---'; ip neigh show
nameserver 192.168.122.2
search localdomain
---
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---
192.168.122.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.122.2 dev ens33 lladdr 00:50:56:e4:48:15 STALE
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ for i in $(seq 1 254); do dig +short -x 192.168.122.$i @192.168.122.2; done | sort -u`

```
root@ubuntu:~# for i in $(seq 1 254); do dig +short -x 192.168.122.$i @192.168.122.2; done | sort -u
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /var/lib/misc/dnsmasq.leases 2>/dev/null; echo '---'; cat /etc/dnsmasq.d/* 2>/dev/null | grep -v '^#'; echo '---'; for h in internal opr ops record archive db sql fileserver backup; do timeout 1 nslookup $h.localdomain 192.168.122.2 2>/dev/null | grep -E '^Name:|^Address:'; done`

```
root@ubuntu:~# cat /var/lib/misc/dnsmasq.leases 2>/dev/null; echo '---'; cat /etc/dnsmasq.d/* 2>/dev/null | grep -v '^#'; echo '---'; for h in internal opr ops record archive db sql fileserver backup; do timeout 1 nslookup $h.localdomain 192.168.122.2 2>/dev/null | grep -E '^Name:|^Address:'; done
---
---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ for i in $(seq 1 254); do ping -c1 -W1 192.168.122.$i >/dev/null 2>&1 & done; wait; ip neigh show; ip route show`

```
root@ubuntu:~# for i in $(seq 1 254); do ping -c1 -W1 192.168.122.$i >/dev/null 2>&1 & done; wait; ip neigh show; ip route show
192.168.122.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.122.2 dev ens33 lladdr 00:50:56:e4:48:15 STALE
default via 192.168.122.1 dev ens33 proto dhcp metric 100
192.168.122.0/24 dev ens33 proto kernel scope link src 192.168.122.47 metric 100
192.168.122.1 dev ens33 proto dhcp scope link src 192.168.122.47 metric 100
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ for p in 22 80 111 443 2049 2375 3000 3306 5432 6379 8000 8080 8081 8443 9000 9200 27017; do timeout 1 bash -c "echo >/dev/tcp/192.168.122.1/$p" 2>/dev/null && echo "$p open"; done`

```
root@ubuntu:~# for p in 22 80 111 443 2049 2375 3000 3306 5432 6379 8000 8080 8081 8443 9000 9200 27017; do timeout 1 bash -c "echo >/dev/tcp/192.168.122.1/$p" 2>/dev/null && echo "$p open"; done
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ command -v nmap >/dev/null && timeout 180 nmap -Pn -p- --min-rate 5000 -T4 192.168.122.1 || echo NMAP_MISSING`

```
root@ubuntu:~# command -v nmap >/dev/null && timeout 180 nmap -Pn -p- --min-rate 5000 -T4 192.168.122.1 || echo NMAP_MISSING
NMAP_MISSING
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ python3 -c "import socket,concurrent.futures; c=lambda p: p if (lambda s: (s.settimeout(0.2), s.connect_ex(('192.168.122.1',p)), s.close())[1])(socket.socket())==0 else None; print([r for r in concurrent.futures.ThreadPoolExecutor(max_workers=1000).map(c, range(1,65536)) if r])"`

```
root@ubuntu:~# python3 -c "import socket,concurrent.futures; c=lambda p: p if (lambda s: (s.settimeout(0.2), s.connect_ex(('192.168.122.1',p)), s.close())[1])(socket.socket())==0 else None; print([r for r in concurrent.futures.ThreadPoolExecutor(max_workers=1000).map(c, range(1,65536)) if r])"
[53]
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ which dig || which nslookup || which host; dig @192.168.122.1 version.bind chaos txt +short; dig @192.168.122.1 hostname.bind chaos txt +short; dig @192.168.122.1 axfr . +noall +answer; dig @192.168.122.1 -x 192.168.122.1 +short`

```
root@ubuntu:~# which dig || which nslookup || which host; dig @192.168.122.1 version.bind chaos txt +short; dig @192.168.122.1 hostname.bind chaos txt +short; dig @192.168.122.1 axfr . +noall +answer; dig @192.168.122.1 -x 192.168.122.1 +short
/usr/bin/dig
"dnsmasq-2.79"
; Transfer failed.
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/lib/misc/ /var/lib/dnsmasq/ 2>/dev/null; grep -vE '^\s*#|^\s*$' /etc/dnsmasq.conf 2>/dev/null | head -40; find / -xdev \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname '*ora_dump*' -o -iname '*opr_evidence*' \) -not -path '/proc/*' -not -path '/sys/*' 2>/dev/null | head -40`

```
root@ubuntu:~# ls -la /var/lib/misc/ /var/lib/dnsmasq/ 2>/dev/null; grep -vE '^\s*#|^\s*$' /etc/dnsmasq.conf 2>/dev/null | head -40; find / -xdev \( -iname '*operational*' -o -iname 'opr_*' -o -iname 'ops_*' -o -iname '*ora_dump*' -o -iname '*opr_evidence*' \) -not -path '/proc/*' -not -path '/sys/*' 2>/dev/null | head -40
/var/lib/misc/:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 17:23 .
drwxr-xr-x 44 root root 4096 Oct 17 17:23 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```
