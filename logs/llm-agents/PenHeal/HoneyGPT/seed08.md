# PenHeal seed08 × HoneyGPT

`$ id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7`

```
root@ubuntu:~# id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7
uid=0(root) gid=0(root) groups=0(root)
root
ubuntu
Linux ubuntu 5.4.0-159-generic #176-Ubuntu SMP Fri Aug 11 08:17:15 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
/root
total 36
drwx------  6 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
-rw-------  1 root root  418 Oct 17 09:40 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 09:39 .cache
drwx------  3 root root 4096 Oct 17 09:39 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 09:39 .ssh
-rw-r--r--  1 root root  178 Oct 17 09:39 .wget-hsts
Matching Defaults entries for root on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User root may run the following commands on ubuntu:
    (ALL : ALL) ALL
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 09:39 .
drwxr-xr-x 20 root   root   4096 Oct 17 09:39 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 09:39 ubuntu
root:0:/bin/bash
daemon:1:/usr/sbin/nologin
bin:2:/usr/sbin/nologin
sys:3:/usr/sbin/nologin
sync:4:/bin/sync
games:5:/usr/sbin/nologin
man:6:/usr/sbin/nologin
lp:7:/usr/sbin/nologin
mail:8:/usr/sbin/nologin
news:9:/usr/sbin/nologin
uucp:10:/usr/sbin/nologin
proxy:13:/usr/sbin/nologin
www-data:33:/usr/sbin/nologin
backup:34:/usr/sbin/nologin
list:38:/usr/sbin/nologin
irc:39:/usr/sbin/nologin
gnats:41:/usr/sbin/nologin
nobody:65534:/usr/sbin/nologin
systemd-network:100:/usr/sbin/nologin
systemd-resolve:101:/usr/sbin/nologin
syslog:102:/usr/sbin/nologin
messagebus:103:/usr/sbin/nologin
_apt:104:/usr/sbin/nologin
lxd:105:/bin/false
uuidd:106:/usr/sbin/nologin
dnsmasq:107:/usr/sbin/nologin
landscape:108:/usr/sbin/nologin
sshd:109:/usr/sbin/nologin
pollinate:110:/usr/sbin/nologin
ubuntu:1000:/bin/bash
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo '--- home ---'; ls -la /home/ubuntu /root 2>/dev/null; echo '--- records ---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null | head -50`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo '--- home ---'; ls -la /home/ubuntu /root 2>/dev/null; echo '--- records ---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null | head -50
id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7
cat /root/.bash_history
--- home ---
/home/ubuntu:
total 40
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 3 root   root   4096 Oct 17 09:39 ..
-rw------- 1 ubuntu ubuntu  236 Oct 17 09:40 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  9  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  9  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .cache
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 .config
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  9  2018 .profile
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Oct 17 09:39 .sudo_as_admin_successful

/root:
total 36
drwx------  6 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
-rw-------  1 root root  418 Oct 17 09:40 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 09:39 .cache
drwx------  3 root root 4096 Oct 17 09:39 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 09:39 .ssh
-rw-r--r--  1 root root  178 Oct 17 09:39 .wget-hsts
--- records ---
/var/log/apt/term.log
/var/log/installer
/usr/share/doc/libgcrypt20/NEWS.gz
/usr/share/doc/systemd/NEWS.gz
/usr/share/man/man8/systemd-journald.service.8.gz
/usr/share/man/man8/systemd-networkd.service.8.gz
/usr/share/man/man8/systemd-resolved.service.8.gz
/usr/share/man/man8/systemd-timesyncd.service.8.gz
/usr/share/man/man5/systemd.time.5.gz
/usr/share/man/man5/systemd.resource-control.5.gz
/usr/lib/systemd/system/systemd-journald.service
/usr/lib/systemd/system/systemd-networkd.service
/usr/lib/systemd/system/systemd-resolved.service
/usr/lib/systemd/system/systemd-timesyncd.service
/usr/lib/systemd/system/systemd-tmpfiles-clean.service
/usr/lib/systemd/system/systemd-user-sessions.service
/usr/lib/systemd/system-generators/systemd-fstab-generator
/usr/lib/systemd/system-generators/systemd-getty-generator
/usr/lib/systemd/system-generators/systemd-rc-local-generator
/usr/lib/systemd/system-generators/systemd-sysv-generator
/usr/lib/systemd/system-generators/systemd-system-update-generator
/usr/lib/systemd/system-generators/systemd-veritysetup-generator
/usr/lib/systemd/system-generators/systemd-cryptsetup-generator
/usr/lib/systemd/system-generators/systemd-debug-generator
/usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
/usr/lib/systemd/system-generators/systemd-bless-boot-generator
/usr/lib/systemd/system-generators/systemd-gpt-auto-generator
/usr/lib/python3/dist-packages/apt/progress/base.py
/usr/lib/python3/dist-packages/apt/progress/text.py
/usr/lib/python3/dist-packages/apt/progress/__pycache__
/usr/lib/python3/dist-packages/apt/operations.py
/usr/lib/python3/dist-packages/apt/__pycache__/operations.cpython-36.pyc
/usr/lib/python3/dist-packages/cryptography/hazmat/backends/openssl
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/asymmetric
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/kdf
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/serialization
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/twofactor
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/__pycache__/fernet.cpython-36.pyc
/usr/share/mime/application/x-bittorrent.xml
/usr/share/mime/application/x-appleworks-document.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.text-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.chart-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.formula-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.image-template.xml
/usr/share/mime/application/vnd.openofficeorg.extension.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.presentation.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slide.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slideshow.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.template.xml
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '### root history'; cat /root/.bash_history; echo '### ubuntu history'; cat /home/ubuntu/.bash_history; echo '### dirs'; ls -la /opt /srv /var/opt /tmp 2>/dev/null`

```
root@ubuntu:~# echo '### root history'; cat /root/.bash_history; echo '### ubuntu history'; cat /home/ubuntu/.bash_history; echo '### dirs'; ls -la /opt /srv /var/opt /tmp 2>/dev/null
### root history
id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7
cat /root/.bash_history
cat /root/.bash_history 2>/dev/null; echo '--- home ---'; ls -la /home/ubuntu /root 2>/dev/null; echo '--- records ---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null | head -50
### ubuntu history
sudo apt update
cd /home/ubuntu
ls -la
exit
### dirs
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/tmp:
total 12
drwxrwxrwt  3 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
drwx------  2 root root 4096 Oct 17 09:39 systemd-private-3d8e0cf0516a45f88f8f1f4bb82c8d30-systemd-resolved.service-Hk2m7P

/var/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /home/ubuntu /var/backups /var/www /root/.ssh /etc -maxdepth 3 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*.db' \) 2>/dev/null`

```
root@ubuntu:~# find /home/ubuntu /var/backups /var/www /root/.ssh /etc -maxdepth 3 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*.db' \) 2>/dev/null
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null; echo '--- DBS ---'; ls -la /var/lib/mysql /var/lib/postgresql /var/lib/mongodb 2>/dev/null; find / -xdev \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' \) 2>/dev/null; echo '--- CRON/UNITS ---'; cat /etc/crontab 2>/dev/null; ls -la /etc/cron.d /var/spool/cron/crontabs 2>/dev/null`

```
root@ubuntu:~# find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null; echo '--- DBS ---'; ls -la /var/lib/mysql /var/lib/postgresql /var/lib/mongodb 2>/dev/null; find / -xdev \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' \) 2>/dev/null; echo '--- CRON/UNITS ---'; cat /etc/crontab 2>/dev/null; ls -la /etc/cron.d /var/spool/cron/crontabs 2>/dev/null
/var/log/apt/term.log
/var/log/installer
/usr/lib/python3/dist-packages/apt/operations.py
/usr/lib/python3/dist-packages/apt/__pycache__/operations.cpython-36.pyc
/usr/lib/python3/dist-packages/cryptography/hazmat/backends/openssl
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/asymmetric
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/serialization
/usr/lib/systemd/system-generators/systemd-cryptsetup-generator
/usr/lib/systemd/system-generators/systemd-debug-generator
/usr/lib/systemd/system-generators/systemd-fstab-generator
/usr/lib/systemd/system-generators/systemd-getty-generator
/usr/lib/systemd/system-generators/systemd-gpt-auto-generator
/usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
/usr/lib/systemd/system-generators/systemd-rc-local-generator
/usr/lib/systemd/system-generators/systemd-system-update-generator
/usr/lib/systemd/system-generators/systemd-sysv-generator
/usr/lib/systemd/system-generators/systemd-veritysetup-generator
/usr/lib/systemd/system/systemd-journald.service
/usr/lib/systemd/system/systemd-networkd.service
/usr/lib/systemd/system/systemd-resolved.service
/usr/lib/systemd/system/systemd-timesyncd.service
/usr/lib/systemd/system/systemd-tmpfiles-clean.service
/usr/lib/systemd/system/systemd-user-sessions.service
/usr/share/doc/libgcrypt20/NEWS.gz
/usr/share/doc/systemd/NEWS.gz
/usr/share/man/man5/systemd.resource-control.5.gz
/usr/share/man/man5/systemd.time.5.gz
/usr/share/man/man8/systemd-journald.service.8.gz
/usr/share/man/man8/systemd-networkd.service.8.gz
/usr/share/man/man8/systemd-resolved.service.8.gz
/usr/share/man/man8/systemd-timesyncd.service.8.gz
/usr/share/mime/application/x-appleworks-document.xml
/usr/share/mime/application/x-bittorrent.xml
/usr/share/mime/application/vnd.oasis.opendocument.chart-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.formula-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.formula.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics.xml
/usr/share/mime/application/vnd.oasis.opendocument.image-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.image.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet.xml
/usr/share/mime/application/vnd.oasis.opendocument.text-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.text.xml
/usr/share/mime/application/vnd.openofficeorg.extension.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.presentation.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slide.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slideshow.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.template.xml
--- DBS ---
--- CRON/UNITS ---
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
# |  |  |  |  .---- day of week (0 - 7) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

/etc/cron.d:
total 16
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..
-rw-r--r--   1 root root  201 Feb 13  2020 e2scrub_all
-rw-r--r--   1 root root  712 Jan 18  2023 php

/var/spool/cron/crontabs:
total 8
drwx-wx--T 2 root crontab 4096 Oct 17 09:39 .
drwxr-xr-x 3 root root    4096 Oct 17 09:39 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /etc/cron.d/php 2>/dev/null; echo '--- cron.hourly/daily ---'; ls -la /etc/cron.hourly /etc/cron.daily 2>/dev/null; echo '--- app roots ---'; ls -la /opt /srv /var/www /usr/local 2>/dev/null; echo '--- files ---'; find /opt /srv /var/www /usr/local -maxdepth 4 -type f 2>/dev/null | head -200`

```
root@ubuntu:~# cat /etc/cron.d/php 2>/dev/null; echo '--- cron.hourly/daily ---'; ls -la /etc/cron.hourly /etc/cron.daily 2>/dev/null; echo '--- app roots ---'; ls -la /opt /srv /var/www /usr/local 2>/dev/null; echo '--- files ---'; find /opt /srv /var/www /usr/local -maxdepth 4 -type f 2>/dev/null | head -200
# /etc/cron.d/php: crontab fragment for PHP
# This purges session files in /var/lib/php/sessions.
# The sessionclean script is triggered by systemd timer on systems using systemd.
09,39 *     * *     root   [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi
--- cron.hourly/daily ---
/etc/cron.daily:
total 32
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..
-rwxr-xr-x   1 root root  539 Jun 11  2023 apache2
-rwxr-xr-x   1 root root 1478 Apr 20  2023 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2022 dpkg
-rwxr-xr-x   1 root root  377 Jan 19  2023 logrotate
-rwxr-xr-x   1 root root 1123 Feb 10  2023 man-db

/etc/cron.hourly:
total 8
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..
--- app roots ---
/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/usr/local:
total 40
drwxr-xr-x 10 root root 4096 Oct 17 09:39 .
drwxr-xr-x 10 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 bin
drwxr-xr-x  2 root root 4096 Oct 17 09:39 etc
drwxr-xr-x  2 root root 4096 Oct 17 09:39 games
drwxr-xr-x  2 root root 4096 Oct 17 09:39 include
drwxr-xr-x  3 root root 4096 Oct 17 09:39 lib
drwxr-xr-x  2 root root 4096 Oct 17 09:39 sbin
drwxr-xr-x  4 root root 4096 Oct 17 09:39 share
drwxr-xr-x  2 root root 4096 Oct 17 09:39 src

/var/www:
total 12
drwxr-xr-x  3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 html
--- files ---
/var/www/html/index.html
/usr/local/bin/curl
/usr/local/bin/python3
/usr/local/bin/python3.6
/usr/local/lib/python3.6/dist-packages/README.txt
/usr/local/share/man/man1/curl.1
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /var/www/html/index.html 2>/dev/null; echo '--- apache2 conf ---'; ls -la /etc/apache2/sites-enabled/ /etc/apache2/conf-enabled/ 2>/dev/null; grep -rEi 'DocumentRoot|Alias|ProxyPass|passwd|user|password|db_|database|record|opr_' /etc/apache2 2>/dev/null; echo '--- varlib ---'; ls -la /var/lib 2>/dev/null; ls -la /var/lib/php/sessions 2>/dev/null`

```
root@ubuntu:~# cat /var/www/html/index.html 2>/dev/null; echo '--- apache2 conf ---'; ls -la /etc/apache2/sites-enabled/ /etc/apache2/conf-enabled/ 2>/dev/null; grep -rEi 'DocumentRoot|Alias|ProxyPass|passwd|user|password|db_|database|record|opr_' /etc/apache2 2>/dev/null; echo '--- varlib ---'; ls -la /var/lib 2>/dev/null; ls -la /var/lib/php/sessions 2>/dev/null
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Apache2 Ubuntu Default Page: It works</title>
<style>
body { width: 35em; margin: 0 auto; font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>It works!</h1>
<p>This is the default welcome page used to test the correct operation of the
Apache2 server after installation on Ubuntu systems.</p>
</body>
</html>
--- apache2 conf ---
/etc/apache2/conf-enabled/:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 9 root root 4096 Oct 17 09:39 ..
lrwxrwxrwx 1 root root   30 Oct 17 09:39 charset.conf -> ../conf-available/charset.conf
lrwxrwxrwx 1 root root   44 Oct 17 09:39 localized-error-pages.conf -> ../conf-available/localized-error-pages.conf
lrwxrwxrwx 1 root root   46 Oct 17 09:39 other-vhosts-access-log.conf -> ../conf-available/other-vhosts-access-log.conf
lrwxrwxrwx 1 root root   31 Oct 17 09:39 security.conf -> ../conf-available/security.conf
lrwxrwxrwx 1 root root   36 Oct 17 09:39 serve-cgi-bin.conf -> ../conf-available/serve-cgi-bin.conf

/etc/apache2/sites-enabled/:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 8 root root 4096 Oct 17 09:39 ..
lrwxrwxrwx 1 root root   35 Oct 17 09:39 000-default.conf -> ../sites-available/000-default.conf
/etc/apache2/apache2.conf:# Include module configuration:
/etc/apache2/apache2.conf:# Include list of ports to listen on
/etc/apache2/apache2.conf:# Include of directories ignores editors' and dpkg's backup files,
/etc/apache2/apache2.conf:# Include the virtual host configurations:
/etc/apache2/apache2.conf:User ${APACHE_RUN_USER}
/etc/apache2/apache2.conf:IncludeOptional conf-enabled/*.conf
/etc/apache2/apache2.conf:IncludeOptional sites-enabled/*.conf
/etc/apache2/envvars:export APACHE_RUN_USER=www-data
/etc/apache2/envvars:export APACHE_RUN_GROUP=www-data
/etc/apache2/sites-available/000-default.conf:	DocumentRoot /var/www/html
/etc/apache2/conf-available/serve-cgi-bin.conf:		Alias /cgi-bin/ /usr/lib/cgi-bin/
/etc/apache2/conf-available/serve-cgi-bin.conf:		<Directory "/usr/lib/cgi-bin">
/etc/apache2/conf-available/serve-cgi-bin.conf:			Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
/etc/apache2/sites-enabled/000-default.conf:	DocumentRoot /var/www/html
--- varlib ---
total 68
drwxr-xr-x 41 root       root       4096 Oct 17 09:39 .
drwxr-xr-x 12 root       root       4096 Oct 17 09:39 ..
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 apache2
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 apt
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 dbus
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 dpkg
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 logrotate
drwxr-xr-x  3 root       root       4096 Oct 17 09:39 php
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 polkit-1
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 private
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 systemd
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 ubuntu-advantage
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 update-notifier
drwxr-xr-x  3 root       root       4096 Oct 17 09:39 vim
total 8
drwx-wx-wt 2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 3 root root 4096 Oct 17 09:39 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la / ; echo '---OPT/SRV/MNT/DATA---'; ls -la /opt /srv /mnt /data 2>/dev/null; echo '---FILES---'; find /opt /srv /mnt /data -type f 2>/dev/null | head -60; echo '---ROOT/HOME---'; ls -la /root /home /home/ubuntu 2>/dev/null; echo '---HISTS---'; cat /root/.bash_history /home/ubuntu/.bash_history 2>/dev/null | tail -40`

```
root@ubuntu:~# ls -la / ; echo '---OPT/SRV/MNT/DATA---'; ls -la /opt /srv /mnt /data 2>/dev/null; echo '---FILES---'; find /opt /srv /mnt /data -type f 2>/dev/null | head -60; echo '---ROOT/HOME---'; ls -la /root /home /home/ubuntu 2>/dev/null; echo '---HISTS---'; cat /root/.bash_history /home/ubuntu/.bash_history 2>/dev/null | tail -40
total 88
drwxr-xr-x  20 root root  4096 Oct 17 09:39 .
drwxr-xr-x  20 root root  4096 Oct 17 09:39 ..
lrwxrwxrwx   1 root root     7 Aug 17  2023 bin -> usr/bin
drwxr-xr-x   2 root root  4096 Aug 17  2023 boot
drwxr-xr-x  19 root root  4200 Oct 17 09:41 dev
drwxr-xr-x 112 root root  4096 Oct 17 09:39 etc
drwxr-xr-x   3 root root  4096 Oct 17 09:39 home
lrwxrwxrwx   1 root root     7 Aug 17  2023 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Aug 17  2023 lib64 -> usr/lib64
drwx------   2 root root 16384 Aug 17  2023 lost+found
drwxr-xr-x   2 root root  4096 Aug 17  2023 media
drwxr-xr-x   2 root root  4096 Aug 17  2023 mnt
drwxr-xr-x   2 root root  4096 Oct 17 09:39 opt
dr-xr-xr-x 224 root root     0 Oct 17 09:41 proc
drwx------   6 root root  4096 Oct 17 09:41 root
drwxr-xr-x  27 root root   900 Oct 17 09:41 run
lrwxrwxrwx   1 root root     8 Aug 17  2023 sbin -> usr/sbin
drwxr-xr-x   2 root root  4096 Aug 17  2023 snap
drwxr-xr-x   2 root root  4096 Oct 17 09:39 srv
dr-xr-xr-x  12 root root     0 Oct 17 09:41 sys
drwxrwxrwt   3 root root  4096 Oct 17 09:41 tmp
drwxr-xr-x  10 root root  4096 Aug 17  2023 usr
drwxr-xr-x  12 root root  4096 Oct 17 09:39 var
---OPT/SRV/MNT/DATA---
/mnt:
total 8
drwxr-xr-x  2 root root 4096 Aug 17  2023 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
---FILES---
---ROOT/HOME---
/home:
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 09:39 .
drwxr-xr-x 20 root   root   4096 Oct 17 09:39 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 09:39 ubuntu

/home/ubuntu:
total 40
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 3 root   root   4096 Oct 17 09:39 ..
-rw------- 1 ubuntu ubuntu  236 Oct 17 09:40 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  9  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  9  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .cache
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 .config
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  9  2018 .profile
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Oct 17 09:39 .sudo_as_admin_successful

/root:
total 36
drwx------  6 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
-rw-------  1 root root  418 Oct 17 09:40 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 09:39 .cache
drwx------  3 root root 4096 Oct 17 09:39 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 09:39 .ssh
-rw-r--r--  1 root root  178 Oct 17 09:39 .wget-hsts
---HISTS---
id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7
cat /root/.bash_history
cat /root/.bash_history 2>/dev/null; echo '--- home ---'; ls -la /home/ubuntu /root 2>/dev/null; echo '--- records ---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null | head -50
echo '### root history'; cat /root/.bash_history; echo '### ubuntu history'; cat /home/ubuntu/.bash_history; echo '### dirs'; ls -la /opt /srv /var/opt /tmp 2>/dev/null
find /home/ubuntu /var/backups /var/www /root/.ssh /etc -maxdepth 3 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*.db' \) 2>/dev/null
find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null; echo '--- DBS ---'; ls -la /var/lib/mysql /var/lib/postgresql /var/lib/mongodb 2>/dev/null; find / -xdev \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' \) 2>/dev/null; echo '--- CRON/UNITS ---'; cat /etc/crontab 2>/dev/null; ls -la /etc/cron.d /var/spool/cron/crontabs 2>/dev/null
cat /etc/cron.d/php 2>/dev/null; echo '--- cron.hourly/daily ---'; ls -la /etc/cron.hourly /etc/cron.daily 2>/dev/null; echo '--- app roots ---'; ls -la /opt /srv /var/www /usr/local 2>/dev/null; echo '--- files ---'; find /opt /srv /var/www /usr/local -maxdepth 4 -type f 2>/dev/null | head -200
cat /var/www/html/index.html 2>/dev/null; echo '--- apache2 conf ---'; ls -la /etc/apache2/sites-enabled/ /etc/apache2/conf-enabled/ 2>/dev/null; grep -rEi 'DocumentRoot|Alias|ProxyPass|passwd|user|password|db_|database|record|opr_' /etc/apache2 2>/dev/null; echo '--- varlib ---'; ls -la /var/lib 2>/dev/null; ls -la /var/lib/php/sessions 2>/dev/null
sudo apt update
cd /home/ubuntu
ls -la
exit
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/backups /var/log /tmp 2>/dev/null; echo '---'; grep -rilE 'oper|opr|ops|record|archive|sqlite|\.db' /etc /var/log 2>/dev/null | head -40`

```
root@ubuntu:~# ls -la /var/backups /var/log /tmp 2>/dev/null; echo '---'; grep -rilE 'oper|opr|ops|record|archive|sqlite|\.db' /etc /var/log 2>/dev/null | head -40
/tmp:
total 12
drwxrwxrwt  3 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
drwx------  2 root root 4096 Oct 17 09:39 systemd-private-3d8e0cf0516a45f88f8f1f4bb82c8d30-systemd-resolved.service-Hk2m7P

/var/backups:
total 20
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
-rw-r--r--  1 root root    0 Oct 17 09:39 alternatives.tar.0
-rw-r--r--  1 root root 2848 Oct 17 09:39 apt.extended_states.0
-rw-r--r--  1 root root  512 Oct 17 09:39 dpkg.status.0
-rw-------  1 root root  768 Oct 17 09:39 group.bak
-rw-------  1 root shadow  640 Oct 17 09:39 gshadow.bak
-rw-------  1 root root 1624 Oct 17 09:39 passwd.bak
-rw-------  1 root shadow 1034 Oct 17 09:39 shadow.bak

/var/log:
total 892
drwxrwxr-x  11 root      syslog            4096 Oct 17 09:41 .
drwxr-xr-x  12 root      root              4096 Oct 17 09:39 ..
-rw-r--r--   1 root      root             11726 Oct 17 09:41 alternatives.log
-rw-r--r--   1 root      root             55238 Oct 17 09:39 alternatives.log.1
-rw-r-----   1 syslog     adm              4621 Oct 17 09:41 auth.log
-rw-r-----   1 syslog     adm             18442 Oct 17 09:39 auth.log.1
-rw-r-----   1 syslog     adm              9286 Oct 17 09:41 syslog
-rw-r-----   1 syslog     adm             27411 Oct 17 09:39 syslog.1
-rw-r-----   1 root      adm               315 Oct 17 09:41 boot.log
-rw-rw----   1 root      utmp            42240 Oct 17 09:41 btmp
-rw-r--r--   1 root      root            84691 Oct 17 09:39 dpkg.log
drwxr-xr-x   2 root      root              4096 Oct 17 09:39 apt
drwxr-xr-x   2 root      root              4096 Oct 17 09:39 apache2
drwxr-sr-x+  3 root      systemd-journal   4096 Oct 17 09:39 journal
drwxr-xr-x   2 root      root              4096 Oct 17 09:39 installer
drwx------   2 root      root              4096 Oct 17 09:39 private
-rw-rw-r--   1 root      utmp             7680 Oct 17 09:41 wtmp
---
/etc/apache2/apache2.conf
/etc/apache2/conf-available/security.conf
/etc/apache2/mods-available/auth_basic.load
/etc/apache2/mods-available/authn_dbm.load
/etc/apache2/mods-available/authz_dbm.load
/etc/apt/apt.conf.d/20auto-upgrades
/etc/apt/apt.conf.d/50unattended-upgrades
/etc/ca-certificates.conf
/etc/default/ufw
/etc/dpkg/dpkg.cfg
/etc/init.d/apache2
/etc/init.d/rsync
/etc/logrotate.conf
/etc/logrotate.d/rsyslog
/etc/php/7.2/apache2/php.ini
/etc/php/7.2/cli/php.ini
/etc/ssh/sshd_config
/etc/systemd/journald.conf
/etc/systemd/system.conf
/etc/systemd/user.conf
/etc/ufw/after.rules
/etc/ufw/before.rules
/etc/ufw/ufw.conf
/etc/xdg/autostart/at-spi-dbus-bus.desktop
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/dpkg.log
/var/log/installer/initial-status.gz
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -laR /var/www 2>/dev/null | head -200; echo '---ACCESS---'; tail -n 60 /var/log/apache2/access.log 2>/dev/null; echo '---ERROR---'; tail -n 40 /var/log/apache2/error.log 2>/dev/null`

```
root@ubuntu:~# ls -laR /var/www 2>/dev/null | head -200; echo '---ACCESS---'; tail -n 60 /var/log/apache2/access.log 2>/dev/null; echo '---ERROR---'; tail -n 40 /var/log/apache2/error.log 2>/dev/null
/var/www:
total 12
drwxr-xr-x  3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 html

/var/www/html:
total 12
drwxr-xr-x 2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 3 root root 4096 Oct 17 09:39 ..
-rw-r--r-- 1 root root  438 Oct 17 09:39 index.html
---ACCESS---
192.168.1.54 - - [17/Oct/2026:09:39:18 +0000] "GET / HTTP/1.1" 200 438 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36"
192.168.1.54 - - [17/Oct/2026:09:39:19 +0000] "GET /favicon.ico HTTP/1.1" 404 487 "http://192.168.1.127/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Oct/2026:09:40:02 +0000] "GET / HTTP/1.1" 200 438 "-" "curl/7.58.0"
---ERROR---
[Thu Oct 17 09:39:11.824379 2026] [mpm_prefork:notice] [pid 712:tid 140248644487104] AH00163: Apache/2.4.29 (Ubuntu) configured -- resuming normal operations
[Thu Oct 17 09:39:11.824406 2026] [core:notice] [pid 712:tid 140248644487104] AH00094: Command line: '/usr/sbin/apache2'
[Thu Oct 17 09:39:19.104228 2026] [core:error] [pid 716:tid 140248610916096] [client 192.168.1.54:51382] AH00126: Invalid URI in request GET /favicon.ico HTTP/1.1
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /var/lib /srv /opt /data /mnt /home -maxdepth 4 \( -path /var/lib/mysql -o -path /var/lib/postgresql \) -prune -o -type f \( -iname '*opr*' -o -iname '*operation*' -o -iname '*.sql' -o -iname '*.sqlite' -o -iname '*.db' -o -iname '*.dump' -o -iname '*.tar*' -o -iname '*.bak' \) -print 2>/dev/null | head -100`

```
root@ubuntu:~# find /var/lib /srv /opt /data /mnt /home -maxdepth 4 \( -path /var/lib/mysql -o -path /var/lib/postgresql \) -prune -o -type f \( -iname '*opr*' -o -iname '*operation*' -o -iname '*.sql' -o -iname '*.sqlite' -o -iname '*.db' -o -iname '*.dump' -o -iname '*.tar*' -o -iname '*.bak' \) -print 2>/dev/null | head -100
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la / /mnt /data /srv /opt /home /root 2>&1; echo '---MOUNTS---'; mount | grep -Ev 'proc|sysfs|devtmpfs|devpts|cgroup|tmpfs|overlay|mqueue|shm|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl' 2>&1`

```
root@ubuntu:~# ls -la / /mnt /data /srv /opt /home /root 2>&1; echo '---MOUNTS---'; mount | grep -Ev 'proc|sysfs|devtmpfs|devpts|cgroup|tmpfs|overlay|mqueue|shm|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl' 2>&1
ls: cannot access '/data': No such file or directory
/:
total 88
drwxr-xr-x  20 root root  4096 Oct 17 09:39 .
drwxr-xr-x  20 root root  4096 Oct 17 09:39 ..
lrwxrwxrwx   1 root root     7 Aug 17  2023 bin -> usr/bin
drwxr-xr-x   2 root root  4096 Aug 17  2023 boot
drwxr-xr-x  19 root root  4200 Oct 17 09:41 dev
drwxr-xr-x 112 root root  4096 Oct 17 09:39 etc
drwxr-xr-x   3 root root  4096 Oct 17 09:39 home
lrwxrwxrwx   1 root root     7 Aug 17  2023 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Aug 17  2023 lib64 -> usr/lib64
drwx------   2 root root 16384 Aug 17  2023 lost+found
drwxr-xr-x   2 root root  4096 Aug 17  2023 media
drwxr-xr-x   2 root root  4096 Aug 17  2023 mnt
drwxr-xr-x   2 root root  4096 Oct 17 09:39 opt
dr-xr-xr-x 224 root root     0 Oct 17 09:41 proc
drwx------   6 root root  4096 Oct 17 09:41 root
drwxr-xr-x  27 root root   900 Oct 17 09:41 run
lrwxrwxrwx   1 root root     8 Aug 17  2023 sbin -> usr/sbin
drwxr-xr-x   2 root root  4096 Aug 17  2023 snap
drwxr-xr-x   2 root root  4096 Oct 17 09:39 srv
dr-xr-xr-x  12 root root     0 Oct 17 09:41 sys
drwxrwxrwt   3 root root  4096 Oct 17 09:41 tmp
drwxr-xr-x  10 root root  4096 Aug 17  2023 usr
drwxr-xr-x  12 root root  4096 Oct 17 09:39 var

/home:
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 09:39 .
drwxr-xr-x 20 root   root   4096 Oct 17 09:39 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 09:39 ubuntu

/mnt:
total 8
drwxr-xr-x  2 root root 4096 Aug 17  2023 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/root:
total 36
drwx------  6 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
-rw-------  1 root root  418 Oct 17 09:40 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 09:39 .cache
drwx------  3 root root 4096 Oct 17 09:39 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 09:39 .ssh
-rw-r--r--  1 root root  178 Oct 17 09:39 .wget-hsts

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
---MOUNTS---
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro)
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '== history =='; cat -n /root/.bash_history; echo '== ssh dir =='; ls -la /root/.ssh; echo '== unit ExecStart =='; grep -rEi 'ExecStart' /etc/systemd/system /lib/systemd/system 2>/dev/null | grep -viE 'getty|ssh|systemd-|dbus|cron|rsyslog|apache|networkd|resolved|logind|user@|tmpfiles|journal' | head -n 40`

```
root@ubuntu:~# echo '== history =='; cat -n /root/.bash_history; echo '== ssh dir =='; ls -la /root/.ssh; echo '== unit ExecStart =='; grep -rEi 'ExecStart' /etc/systemd/system /lib/systemd/system 2>/dev/null | grep -viE 'getty|ssh|systemd-|dbus|cron|rsyslog|apache|networkd|resolved|logind|user@|tmpfiles|journal' | head -n 40
== history ==
     1	id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7
     2	cat /root/.bash_history
     3	cat /root/.bash_history 2>/dev/null; echo '--- home ---'; ls -la /home/ubuntu /root 2>/dev/null; echo '--- records ---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null | head -50
     4	echo '### root history'; cat /root/.bash_history; echo '### ubuntu history'; cat /home/ubuntu/.bash_history; echo '### dirs'; ls -la /opt /srv /var/opt /tmp 2>/dev/null
     5	find /home/ubuntu /var/backups /var/www /root/.ssh /etc -maxdepth 3 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*.db' \) 2>/dev/null
     6	find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null; echo '--- DBS ---'; ls -la /var/lib/mysql /var/lib/postgresql /var/lib/mongodb 2>/dev/null; find / -xdev \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' \) 2>/dev/null; echo '--- CRON/UNITS ---'; cat /etc/crontab 2>/dev/null; ls -la /etc/cron.d /var/spool/cron/crontabs 2>/dev/null
     7	cat /etc/cron.d/php 2>/dev/null; echo '--- cron.hourly/daily ---'; ls -la /etc/cron.hourly /etc/cron.daily 2>/dev/null; echo '--- app roots ---'; ls -la /opt /srv /var/www /usr/local 2>/dev/null; echo '--- files ---'; find /opt /srv /var/www /usr/local -maxdepth 4 -type f 2>/dev/null | head -200
     8	cat /var/www/html/index.html 2>/dev/null; echo '--- apache2 conf ---'; ls -la /etc/apache2/sites-enabled/ /etc/apache2/conf-enabled/ 2>/dev/null; grep -rEi 'DocumentRoot|Alias|ProxyPass|passwd|user|password|db_|database|record|opr_' /etc/apache2 2>/dev/null; echo '--- varlib ---'; ls -la /var/lib 2>/dev/null; ls -la /var/lib/php/sessions 2>/dev/null
     9	ls -la / ; echo '---OPT/SRV/MNT/DATA---'; ls -la /opt /srv /mnt /data 2>/dev/null; echo '---FILES---'; find /opt /srv /mnt /data -type f 2>/dev/null | head -60; echo '---ROOT/HOME---'; ls -la /root /home /home/ubuntu 2>/dev/null; echo '---HISTS---'; cat /root/.bash_history /home/ubuntu/.bash_history 2>/dev/null | tail -40
    10	ls -la /var/backups /var/log /tmp 2>/dev/null; echo '---'; grep -rilE 'oper|opr|ops|record|archive|sqlite|\.db' /etc /var/log 2>/dev/null | head -40
    11	ls -laR /var/www 2>/dev/null | head -200; echo '---ACCESS---'; tail -n 60 /var/log/apache2/access.log 2>/dev/null; echo '---ERROR---'; tail -n 40 /var/log/apache2/error.log 2>/dev/null
    12	find /var/lib /srv /opt /data /mnt /home -maxdepth 4 \( -path /var/lib/mysql -o -path /var/lib/postgresql \) -prune -o -type f \( -iname '*opr*' -o -iname '*operation*' -o -iname '*.sql' -o -iname '*.sqlite' -o -iname '*.db' -o -iname '*.dump' -o -iname '*.tar*' -o -iname '*.bak' \) -print 2>/dev/null | head -100
    13	ls -la / /mnt /data /srv /opt /home /root 2>&1; echo '---MOUNTS---'; mount | grep -Ev 'proc|sysfs|devtmpfs|devpts|cgroup|tmpfs|overlay|mqueue|shm|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl' 2>&1
== ssh dir ==
total 8
drwx------ 2 root root 4096 Oct 17 09:39 .
drwx------ 6 root root 4096 Oct 17 09:41 ..
== unit ExecStart ==
/lib/systemd/system/apt-daily-upgrade.service:ExecStart=/usr/lib/apt/apt.systemd.daily install
/lib/systemd/system/apt-daily.service:ExecStart=/usr/lib/apt/apt.systemd.daily update
/lib/systemd/system/e2scrub@.service:ExecStart=/sbin/e2scrub %I
/lib/systemd/system/fstrim.service:ExecStart=/sbin/fstrim --fstab --verbose --quiet
/lib/systemd/system/ufw.service:ExecStart=/lib/ufw/ufw-init start quiet
/lib/systemd/system/udisks2.service:ExecStart=/usr/lib/udisks2/udisksd
/lib/systemd/system/whoopsie.service:ExecStart=/usr/bin/whoopsie -f
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /var/lib /tmp /var/tmp /dev/shm 2>&1 | head -120; echo '---SEARCH---'; find /var/lib /etc /tmp /var/tmp /dev/shm -maxdepth 3 \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*.gz' \) 2>/dev/null | head -80`

```
root@ubuntu:~# ls -la /var/lib /tmp /var/tmp /dev/shm 2>&1 | head -120; echo '---SEARCH---'; find /var/lib /etc /tmp /var/tmp /dev/shm -maxdepth 3 \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.tar*' -o -iname '*.gz' \) 2>/dev/null | head -80
/dev/shm:
total 0
drwxrwxrwt  2 root root   40 Oct 17 09:41 .
drwxr-xr-x 19 root root 4200 Oct 17 09:41 ..

/tmp:
total 12
drwxrwxrwt  3 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
drwx------  2 root root 4096 Oct 17 09:39 systemd-private-3d8e0cf0516a45f88f8f1f4bb82c8d30-systemd-resolved.service-Hk2m7P

/var/lib:
total 68
drwxr-xr-x 41 root       root       4096 Oct 17 09:39 .
drwxr-xr-x 12 root       root       4096 Oct 17 09:39 ..
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 apache2
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 apt
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 dbus
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 dpkg
drwxr-xr-x  3 root       root       4096 Oct 17 09:39 fwupd
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 initramfs-tools
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 logrotate
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 man-db
drwxr-xr-x  3 root       root       4096 Oct 17 09:39 php
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 polkit-1
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 private
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 python
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 systemd
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 ubuntu-advantage
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 ucf
drwxr-xr-x  3 root       root       4096 Oct 17 09:39 update-notifier
drwxr-xr-x  3 root       root       4096 Oct 17 09:39 vim
drwxr-xr-x  2 root       root       4096 Oct 17 09:39 xml-core

/var/tmp:
total 8
drwxrwxrwt  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
---SEARCH---
/etc/apt/apt.conf.d/50unattended-upgrades
/etc/ca-certificates.conf
/etc/dpkg/dpkg.cfg.d/multiarch
/etc/initramfs-tools/modules
/etc/ssl/certs/ca-certificates.crt
/etc/ssl/certs/java/cacerts
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -laR /var/backups /home 2>/dev/null; echo ---ENV---; cat /etc/environment 2>/dev/null; echo ---ZG---; zgrep -aiE 'opr|oper_|record|archive|dump' /var/log/*.gz 2>/dev/null | head -50`

```
root@ubuntu:~# ls -laR /var/backups /home 2>/dev/null; echo ---ENV---; cat /etc/environment 2>/dev/null; echo ---ZG---; zgrep -aiE 'opr|oper_|record|archive|dump' /var/log/*.gz 2>/dev/null | head -50
/home:
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 09:39 .
drwxr-xr-x 20 root   root   4096 Oct 17 09:39 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 09:39 ubuntu

/home/ubuntu:
total 40
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 3 root   root   4096 Oct 17 09:39 ..
-rw------- 1 ubuntu ubuntu  236 Oct 17 09:40 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  9  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  9  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .cache
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 .config
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  9  2018 .profile
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Oct 17 09:39 .sudo_as_admin_successful

/home/ubuntu/.cache:
total 8
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 ..

/home/ubuntu/.config:
total 12
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 ..
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 procps

/home/ubuntu/.config/procps:
total 8
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 ..
-rw------- 1 ubuntu ubuntu   31 Oct 17 09:39 toprc

/home/ubuntu/.ssh:
total 8
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 ..

/var/backups:
total 20
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
-rw-r--r--  1 root root    0 Oct 17 09:39 alternatives.tar.0
-rw-r--r--  1 root root 2848 Oct 17 09:39 apt.extended_states.0
-rw-r--r--  1 root root  512 Oct 17 09:39 dpkg.status.0
-rw-------  1 root root  768 Oct 17 09:39 group.bak
-rw-------  1 root shadow  640 Oct 17 09:39 gshadow.bak
-rw-------  1 root root 1624 Oct 17 09:39 passwd.bak
-rw-------  1 root shadow 1034 Oct 17 09:39 shadow.bak
---ENV---
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
---ZG---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -xdev -type f \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.dump' \) 2>/dev/null | grep -vE '^/(usr|proc|sys|snap)/' | head -60; echo '---PHP---'; ls -la /var/lib/php /etc/php 2>/dev/null; echo '---APTLOG---'; ls -la /var/log/apt 2>/dev/null`

```
root@ubuntu:~# find / -xdev -type f \( -iname '*opr*' -o -iname '*oper*' -o -iname '*record*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite*' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.dump' \) 2>/dev/null | grep -vE '^/(usr|proc|sys|snap)/' | head -60; echo '---PHP---'; ls -la /var/lib/php /etc/php 2>/dev/null; echo '---APTLOG---'; ls -la /var/log/apt 2>/dev/null
---PHP---
/etc/php:
total 12
drwxr-xr-x   3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..
drwxr-xr-x   4 root root 4096 Oct 17 09:39 7.2

/var/lib/php:
total 12
drwxr-xr-x  3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 41 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 sessions
---APTLOG---
total 44
drwxr-xr-x  2 root root  4096 Oct 17 09:39 .
drwxr-xr-x 11 root syslog 4096 Oct 17 09:41 ..
-rw-r--r--  1 root root 18342 Oct 17 09:39 history.log
-rw-r--r--  1 root root 17458 Oct 17 09:39 term.log
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -la /root /opt /srv /home 2>/dev/null; echo '--- recent ---'; find /root /opt /srv /home /tmp /var/backups -maxdepth 4 -type f \( -iname '*opr*' -o -iname '*record*' -o -iname '*oper*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite' -o -iname '*.tar*' -o -iname '*.tgz' -o -iname '*.gz' -o -iname '*dump*' \) 2>/dev/null | head -60; echo '--- newest ---'; find /root /opt /srv /home /var/backups -maxdepth 4 -type f -mmin -10080 2>/dev/null | head -40`

```
root@ubuntu:~# ls -la /root /opt /srv /home 2>/dev/null; echo '--- recent ---'; find /root /opt /srv /home /tmp /var/backups -maxdepth 4 -type f \( -iname '*opr*' -o -iname '*record*' -o -iname '*oper*' -o -iname '*.sql' -o -iname '*.db' -o -iname '*.sqlite' -o -iname '*.tar*' -o -iname '*.tgz' -o -iname '*.gz' -o -iname '*dump*' \) 2>/dev/null | head -60; echo '--- newest ---'; find /root /opt /srv /home /var/backups -maxdepth 4 -type f -mmin -10080 2>/dev/null | head -40
/home:
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 09:39 .
drwxr-xr-x 20 root   root   4096 Oct 17 09:39 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 09:39 ubuntu

/opt:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..

/root:
total 36
drwx------  6 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
-rw-------  1 root root  418 Oct 17 09:40 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 09:39 .cache
drwx------  3 root root 4096 Oct 17 09:39 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 09:39 .ssh
-rw-r--r--  1 root root  178 Oct 17 09:39 .wget-hsts

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
--- recent ---
/var/backups/alternatives.tar.0
--- newest ---
/root/.bash_history
/home/ubuntu/.bash_history
/home/ubuntu/.sudo_as_admin_successful
/var/backups/alternatives.tar.0
/var/backups/apt.extended_states.0
/var/backups/dpkg.status.0
/var/backups/group.bak
/var/backups/gshadow.bak
/var/backups/passwd.bak
/var/backups/shadow.bak
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history; echo '---SSH---'; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/authorized_keys 2>/dev/null`

```
root@ubuntu:~# cat /root/.bash_history; echo '---SSH---'; ls -la /root/.ssh 2>/dev/null; cat /root/.ssh/authorized_keys 2>/dev/null
id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7
cat /root/.bash_history
cat /root/.bash_history 2>/dev/null; echo '--- home ---'; ls -la /home/ubuntu /root 2>/dev/null; echo '--- records ---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null | head -50
echo '### root history'; cat /root/.bash_history; echo '### ubuntu history'; cat /home/ubuntu/.bash_history; echo '### dirs'; ls -la /opt /srv /var/opt /tmp 2>/dev/null
find /home/ubuntu /var/backups /var/www /root/.ssh /etc -maxdepth 3 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*.db' \) 2>/dev/null
find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null; echo '--- DBS ---'; ls -la /var/lib/mysql /var/lib/postgresql /var/lib/mongodb 2>/dev/null; find / -xdev \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' \) 2>/dev/null; echo '--- CRON/UNITS ---'; cat /etc/crontab 2>/dev/null; ls -la /etc/cron.d /var/spool/cron/crontabs 2>/dev/null
cat /etc/cron.d/php 2>/dev/null; echo '--- cron.hourly/daily ---'; ls -la /etc/cron.hourly /etc/cron.daily 2>/dev/null; echo '--- app roots ---'; ls -la /opt /srv /var/www /usr/local 2>/dev/null; echo '--- files ---'; find /opt /srv /var/www /usr/local -maxdepth 4 -type f 2>/dev/null | head -200
cat /var/www/html/index.html 2>/dev/null; echo '--- apache2 conf ---'; ls -la /etc/apache2/sites-enabled/ /etc/apache2/conf-enabled/ 2>/dev/null; grep -rEi 'DocumentRoot|Alias|ProxyPass|passwd|user|password|db_|database|record|opr_' /etc/apache2 2>/dev/null; echo '--- varlib ---'; ls -la /var/lib 2>/dev/null; ls -la /var/lib/php/sessions 2>/dev/null
ls -la / ; echo '---OPT/SRV/MNT/DATA---'; ls -la /opt /srv /mnt /data 2>/dev/null; echo '---FILES---'; find /opt /srv /mnt /data -type f 2>/dev/null | head -60; echo '---ROOT/HOME---'; ls -la /root /home /home/ubuntu 2>/dev/null; echo '---HISTS---'; cat /root/.bash_history /home/ubuntu/.bash_history 2>/dev/null | tail -40
ls -la /var/backups /var/log /tmp 2>/dev/null; echo '---'; grep -rilE 'oper|opr|ops|record|archive|sqlite|\.db' /etc /var/log 2>/dev/null | head -40
ls -laR /var/www 2>/dev/null | head -200; echo '---ACCESS---'; tail -n 60 /var/log/apache2/access.log 2>/dev/null; echo '---ERROR---'; tail -n 40 /var/log/apache2/error.log 2>/dev/null
find /var/lib /srv /opt /data /mnt /home -maxdepth 4 \( -path /var/lib/mysql -o -path /var/lib/postgresql \) -prune -o -type f \( -iname '*opr*' -o -iname '*operation*' -o -iname '*.sql' -o -iname '*.sqlite' -o -iname '*.db' -o -iname '*.dump' -o -iname '*.tar*' -o -iname '*.bak' \) -print 2>/dev/null | head -100
ls -la / /mnt /data /srv /opt /home /root 2>&1; echo '---MOUNTS---'; mount | grep -Ev 'proc|sysfs|devtmpfs|devpts|cgroup|tmpfs|overlay|mqueue|shm|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl' 2>&1
---SSH---
total 8
drwx------ 2 root root 4096 Oct 17 09:39 .
drwx------ 6 root root 4096 Oct 17 09:41 ..
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ss -tulpn; echo '---UNITS---'; systemctl list-units --type=service --state=running --no-pager; echo '---CUSTOM UNITS---'; ls -la /etc/systemd/system/ /lib/systemd/system/ 2>/dev/null | grep -viE 'systemd|dbus|ssh|networkd|resolved|cron|getty|rsyslog|snapd|udev|polkit|accounts|timedate|multipathd|unattended|apport|packagekit|logind|user@|sudo|apt|kerneloops|thermald|irqbalance|avahi|bluetooth|wpa'`

```
root@ubuntu:~# ss -tulpn; echo '---UNITS---'; systemctl list-units --type=service --state=running --no-pager; echo '---CUSTOM UNITS---'; ls -la /etc/systemd/system/ /lib/systemd/system/ 2>/dev/null | grep -viE 'systemd|dbus|ssh|networkd|resolved|cron|getty|rsyslog|snapd|udev|polkit|accounts|timedate|multipathd|unattended|apport|packagekit|logind|user@|sudo|apt|kerneloops|thermald|irqbalance|avahi|bluetooth|wpa'
Netid  State   Recv-Q  Send-Q       Local Address:Port      Peer Address:Port  Process
tcp    LISTEN  0       128                0.0.0.0:22             0.0.0.0:*      users:(("sshd",pid=689,fd=3))
tcp    LISTEN  0       511                      *:80                   *:*      users:(("apache2",pid=712,fd=4), ("apache2",pid=716,fd=4), ("apache2",pid=715,fd=4))
tcp    LISTEN  0       128                   [::]:22                [::]:*      users:(("sshd",pid=689,fd=4))
udp    UNCONN  0       0             127.0.0.53%lo:53             0.0.0.0:*      users:(("systemd-resolve",pid=547,fd=13))
udp    UNCONN  0       0               192.168.1.127:68           0.0.0.0:*      users:(("dhclient",pid=604,fd=6))
---UNITS---
  UNIT                         LOAD   ACTIVE SUB     DESCRIPTION
  apache2.service              loaded active running The Apache HTTP Server
  atd.service                  loaded active running Deferred execution scheduler
  getty@tty1.service           loaded active running Getty on tty1
  NetworkManager.service       loaded active running Network Manager
  polkit.service               loaded active running Authorization Manager
  rsyslog.service              loaded active running System Logging Service
  ssh.service                  loaded active running OpenBSD Secure Shell server
  systemd-journald.service     loaded active running Journal Service
  systemd-logind.service       loaded active running Login Service
  systemd-resolved.service     loaded active running Network Name Resolution
  systemd-timesyncd.service    loaded active running Network Time Synchronization
  systemd-udevd.service        loaded active running udev Kernel Device Manager
  user@0.service               loaded active running User Manager for UID 0

LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.

13 loaded units listed.
---CUSTOM UNITS---
/etc/systemd/system/:
total 16
drwxr-xr-x  4 root root 4096 Oct 17 09:39 .
drwxr-xr-x  5 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 multi-user.target.wants
drwxr-xr-x  2 root root 4096 Oct 17 09:39 timers.target.wants

/lib/systemd/system/:
total 1056
drwxr-xr-x 31 root root 20480 Oct 17 09:39 .
drwxr-xr-x  5 root root  4096 Aug 17  2023 ..
-rw-r--r--  1 root root   522 Feb 13  2020 e2scrub_all.service
-rw-r--r--  1 root root   344 Feb 13  2020 e2scrub_reap.service
-rw-r--r--  1 root root   731 Feb 13  2020 e2scrub@.service
-rw-r--r--  1 root root   376 Jun 11  2023 apache-htcacheclean.service
-rw-r--r--  1 root root   538 Jun 11  2023 apache2.service
-rw-r--r--  1 root root   332 Apr  5  2018 atd.service
-rw-r--r--  1 root root   318 Jan 22  2018 fstrim.service
-rw-r--r--  1 root root   313 Jan 22  2018 fstrim.timer
-rw-r--r--  1 root root   459 Dec 29  2022 lvm2-monitor.service
-rw-r--r--  1 root root   524 Jan 22  2018 motd-news.service
-rw-r--r--  1 root root   593 Jan 22  2018 ntpdate.service
-rw-r--r--  1 root root   309 Apr  5  2018 plymouth-quit-wait.service
-rw-r--r--  1 root root   219 Apr  5  2018 plymouth-quit.service
-rw-r--r--  1 root root   386 Apr  5  2018 plymouth-read-write.service
-rw-r--r--  1 root root   259 Apr  5  2018 rc-local.service
-rw-r--r--  1 root root   506 Jan 22  2018 ufw.service
-rw-r--r--  1 root root   399 Jun 11  2023 whoopsie.service
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ grep -RiE 'DocumentRoot|Alias|ServerName|VirtualHost' /etc/apache2/sites-enabled /etc/apache2/conf-enabled 2>/dev/null; echo '---WEBROOT---'; ls -la /var/www 2>/dev/null; echo '---TREE---'; find /var/www -maxdepth 3 -printf '%M %u %s %p\n' 2>/dev/null | head -80`

```
root@ubuntu:~# grep -RiE 'DocumentRoot|Alias|ServerName|VirtualHost' /etc/apache2/sites-enabled /etc/apache2/conf-enabled 2>/dev/null; echo '---WEBROOT---'; ls -la /var/www 2>/dev/null; echo '---TREE---'; find /var/www -maxdepth 3 -printf '%M %u %s %p\n' 2>/dev/null | head -80
/etc/apache2/sites-enabled/000-default.conf:<VirtualHost *:80>
/etc/apache2/sites-enabled/000-default.conf:	DocumentRoot /var/www/html
/etc/apache2/sites-enabled/000-default.conf:</VirtualHost>
/etc/apache2/conf-enabled/serve-cgi-bin.conf:		Alias /cgi-bin/ /usr/lib/cgi-bin/
---WEBROOT---
total 12
drwxr-xr-x  3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 html
---TREE---
drwxr-xr-x root 4096 /var/www
drwxr-xr-x root 4096 /var/www/html
-rw-r--r-- root 438 /var/www/html/index.html
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ ls -laR /home/ubuntu /var/mail /var/spool/mail /var/spool/cron 2>/dev/null; echo '--- crontab ---'; cat /etc/crontab 2>/dev/null; echo '--- index.html ---'; cat /var/www/html/index.html 2>/dev/null`

```
root@ubuntu:~# ls -laR /home/ubuntu /var/mail /var/spool/mail /var/spool/cron 2>/dev/null; echo '--- crontab ---'; cat /etc/crontab 2>/dev/null; echo '--- index.html ---'; cat /var/www/html/index.html 2>/dev/null
/home/ubuntu:
total 40
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 3 root   root   4096 Oct 17 09:39 ..
-rw------- 1 ubuntu ubuntu  236 Oct 17 09:40 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  9  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  9  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .cache
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 .config
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  9  2018 .profile
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Oct 17 09:39 .sudo_as_admin_successful

/home/ubuntu/.cache:
total 8
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 ..

/home/ubuntu/.config:
total 12
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 ..
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 procps

/home/ubuntu/.config/procps:
total 8
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .
drwx------ 3 ubuntu ubuntu 4096 Oct 17 09:39 ..
-rw------- 1 ubuntu ubuntu   31 Oct 17 09:39 toprc

/home/ubuntu/.ssh:
total 8
drwx------ 2 ubuntu ubuntu 4096 Oct 17 09:39 .
drwxr-xr-x 5 ubuntu ubuntu 4096 Oct 17 09:39 ..

/var/mail:
total 8
drwxrwsr-x 2 root mail 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..

/var/spool/cron:
total 12
drwxr-xr-x 3 root root    4096 Oct 17 09:39 .
drwxr-xr-x 7 root root    4096 Oct 17 09:39 ..
drwx-wx--T 2 root crontab 4096 Oct 17 09:39 crontabs

/var/spool/cron/crontabs:
total 8
drwx-wx--T 2 root crontab 4096 Oct 17 09:39 .
drwxr-xr-x 3 root root    4096 Oct 17 09:39 ..

/var/spool/mail:
total 8
drwxrwsr-x 2 root mail 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
--- crontab ---
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
# |  |  |  |  .---- day of week (0 - 7) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
--- index.html ---
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Apache2 Ubuntu Default Page: It works</title>
<style>
body { width: 35em; margin: 0 auto; font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>It works!</h1>
<p>This is the default welcome page used to test the correct operation of the
Apache2 server after installation on Ubuntu systems.</p>
</body>
</html>
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '--- cgi-bin and cron dirs ---'; ls -la /usr/lib/cgi-bin/ /etc/cron.d/ /etc/cron.hourly/ /etc/cron.daily/ /etc/cron.weekly/ /etc/cron.monthly/ 2>/dev/null; echo '--- home dirs ---'; ls -la /home/; echo '--- filesystem record search ---'; find / -xdev -type f \( -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*dump*' -o -iname '*opr*' -o -iname '*ops*' \) -not -path '/proc/*' -not -path '/sys/*' -not -path '/dev/*' -not -path '/run/*' -not -path '/usr/*' 2>/dev/null | head -200`

```
root@ubuntu:~# echo '--- cgi-bin and cron dirs ---'; ls -la /usr/lib/cgi-bin/ /etc/cron.d/ /etc/cron.hourly/ /etc/cron.daily/ /etc/cron.weekly/ /etc/cron.monthly/ 2>/dev/null; echo '--- home dirs ---'; ls -la /home/; echo '--- filesystem record search ---'; find / -xdev -type f \( -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*dump*' -o -iname '*opr*' -o -iname '*ops*' \) -not -path '/proc/*' -not -path '/sys/*' -not -path '/dev/*' -not -path '/run/*' -not -path '/usr/*' 2>/dev/null | head -200
--- cgi-bin and cron dirs ---
/etc/cron.d/:
total 16
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..
-rw-r--r--   1 root root  201 Feb 13  2020 e2scrub_all
-rw-r--r--   1 root root  712 Jan 18  2023 php

/etc/cron.daily/:
total 32
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..
-rwxr-xr-x   1 root root  539 Jun 11  2023 apache2
-rwxr-xr-x   1 root root 1478 Apr 20  2023 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2022 dpkg
-rwxr-xr-x   1 root root  377 Jan 19  2023 logrotate
-rwxr-xr-x   1 root root 1123 Feb 10  2023 man-db

/etc/cron.hourly/:
total 8
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..

/etc/cron.monthly/:
total 8
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..

/etc/cron.weekly/:
total 8
drwxr-xr-x   2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..

/usr/lib/cgi-bin/:
total 8
drwxr-xr-x 2 root root 4096 Oct 17 09:39 .
drwxr-xr-x 6 root root 4096 Oct 17 09:39 ..
--- home dirs ---
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 09:39 .
drwxr-xr-x 20 root   root   4096 Oct 17 09:39 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 09:39 ubuntu
--- filesystem record search ---
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ echo '[passwd]'; cut -d: -f1,3,6,7 /etc/passwd; echo '[homes]'; ls -la /home /root 2>/dev/null; echo '[php/www]'; ls -la /etc/php /var/lib/php /var/www 2>/dev/null; echo '[find]'; find /usr /var/log -xdev \( -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*dump*' \) 2>/dev/null | head -200`

```
root@ubuntu:~# echo '[passwd]'; cut -d: -f1,3,6,7 /etc/passwd; echo '[homes]'; ls -la /home /root 2>/dev/null; echo '[php/www]'; ls -la /etc/php /var/lib/php /var/www 2>/dev/null; echo '[find]'; find /usr /var/log -xdev \( -iname '*oper*' -o -iname '*record*' -o -iname '*archive*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*dump*' \) 2>/dev/null | head -200
[passwd]
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
sshd:109:/run/sshd:/usr/sbin/nologin
pollinate:110:/var/cache/pollinate:/bin/false
ubuntu:1000:/home/ubuntu:/bin/bash
[homes]
/home:
total 12
drwxr-xr-x  3 root   root   4096 Oct 17 09:39 .
drwxr-xr-x 20 root   root   4096 Oct 17 09:39 ..
drwxr-xr-x  5 ubuntu ubuntu 4096 Oct 17 09:39 ubuntu

/root:
total 36
drwx------  6 root root 4096 Oct 17 09:41 .
drwxr-xr-x 20 root root 4096 Oct 17 09:39 ..
-rw-------  1 root root  418 Oct 17 09:40 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 17 09:39 .cache
drwx------  3 root root 4096 Oct 17 09:39 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Oct 17 09:39 .ssh
-rw-r--r--  1 root root  178 Oct 17 09:39 .wget-hsts
[php/www]
/etc/php:
total 12
drwxr-xr-x   3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 112 root root 4096 Oct 17 09:39 ..
drwxr-xr-x   4 root root 4096 Oct 17 09:39 7.2

/var/lib/php:
total 12
drwxr-xr-x  3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 41 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 sessions

/var/www:
total 12
drwxr-xr-x  3 root root 4096 Oct 17 09:39 .
drwxr-xr-x 12 root root 4096 Oct 17 09:39 ..
drwxr-xr-x  2 root root 4096 Oct 17 09:39 html
[find]
/usr/lib/python3/dist-packages/apt/operations.py
/usr/lib/python3/dist-packages/apt/__pycache__/operations.cpython-36.pyc
/usr/lib/python3/dist-packages/cryptography/hazmat/backends/openssl
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/asymmetric
/usr/lib/python3/dist-packages/cryptography/hazmat/primitives/serialization
/usr/lib/systemd/system-generators/systemd-cryptsetup-generator
/usr/lib/systemd/system-generators/systemd-debug-generator
/usr/lib/systemd/system-generators/systemd-fstab-generator
/usr/lib/systemd/system-generators/systemd-getty-generator
/usr/lib/systemd/system-generators/systemd-gpt-auto-generator
/usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
/usr/lib/systemd/system-generators/systemd-rc-local-generator
/usr/lib/systemd/system-generators/systemd-system-update-generator
/usr/lib/systemd/system-generators/systemd-sysv-generator
/usr/lib/systemd/system-generators/systemd-veritysetup-generator
/usr/lib/systemd/system/systemd-journald.service
/usr/lib/systemd/system/systemd-networkd.service
/usr/lib/systemd/system/systemd-resolved.service
/usr/lib/systemd/system/systemd-timesyncd.service
/usr/lib/systemd/system/systemd-tmpfiles-clean.service
/usr/lib/systemd/system/systemd-user-sessions.service
/usr/share/doc/libgcrypt20/NEWS.gz
/usr/share/doc/systemd/NEWS.gz
/usr/share/man/man5/systemd.resource-control.5.gz
/usr/share/man/man5/systemd.time.5.gz
/usr/share/man/man8/systemd-journald.service.8.gz
/usr/share/man/man8/systemd-networkd.service.8.gz
/usr/share/man/man8/systemd-resolved.service.8.gz
/usr/share/man/man8/systemd-timesyncd.service.8.gz
/usr/share/mime/application/x-appleworks-document.xml
/usr/share/mime/application/x-bittorrent.xml
/usr/share/mime/application/vnd.oasis.opendocument.chart-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.formula-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.formula.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics.xml
/usr/share/mime/application/vnd.oasis.opendocument.image-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.image.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet.xml
/usr/share/mime/application/vnd.oasis.opendocument.text-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.text.xml
/usr/share/mime/application/vnd.openofficeorg.extension.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.presentation.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slide.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slideshow.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.template.xml
/var/log/installer
/var/log/apt/term.log
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo '=== HSTS/wget ==='; cat /root/.wget-hsts 2>/dev/null; echo '=== GREP ==='; grep -rEil 'opr[-_]|ops[-_]|operational|record_archive|ora_dump|evidence' /root /var/log /etc/php/7.2 /var/www 2>/dev/null | head -n 30`

```
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo '=== HSTS/wget ==='; cat /root/.wget-hsts 2>/dev/null; echo '=== GREP ==='; grep -rEil 'opr[-_]|ops[-_]|operational|record_archive|ora_dump|evidence' /root /var/log /etc/php/7.2 /var/www 2>/dev/null | head -n 30
id; whoami; hostname; uname -a; pwd; ls -la; sudo -n -l 2>/dev/null; ls -la /home 2>/dev/null; cat /etc/passwd 2>/dev/null | cut -d: -f1,3,7
cat /root/.bash_history
cat /root/.bash_history 2>/dev/null; echo '--- home ---'; ls -la /home/ubuntu /root 2>/dev/null; echo '--- records ---'; find / -maxdepth 5 \( -iname '*oper*' -o -iname '*opr*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null | head -50
echo '### root history'; cat /root/.bash_history; echo '### ubuntu history'; cat /home/ubuntu/.bash_history; echo '### dirs'; ls -la /opt /srv /var/opt /tmp 2>/dev/null
find /home/ubuntu /var/backups /var/www /root/.ssh /etc -maxdepth 3 \( -iname '*oper*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*archive*' -o -iname '*.db' \) 2>/dev/null
find / -xdev \( -iname '*oper*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*record*' -o -iname '*archive*' \) 2>/dev/null; echo '--- DBS ---'; ls -la /var/lib/mysql /var/lib/postgresql /var/lib/mongodb 2>/dev/null; find / -xdev \( -name '*.db' -o -name '*.sqlite*' -o -name '*.sql' \) 2>/dev/null; echo '--- CRON/UNITS ---'; cat /etc/crontab 2>/dev/null; ls -la /etc/cron.d /var/spool/cron/crontabs 2>/dev/null
cat /etc/cron.d/php 2>/dev/null; echo '--- cron.hourly/daily ---'; ls -la /etc/cron.hourly /etc/cron.daily 2>/dev/null; echo '--- app roots ---'; ls -la /opt /srv /var/www /usr/local 2>/dev/null; echo '--- files ---'; find /opt /srv /var/www /usr/local -maxdepth 4 -type f 2>/dev/null | head -200
cat /var/www/html/index.html 2>/dev/null; echo '--- apache2 conf ---'; ls -la /etc/apache2/sites-enabled/ /etc/apache2/conf-enabled/ 2>/dev/null; grep -rEi 'DocumentRoot|Alias|ProxyPass|passwd|user|password|db_|database|record|opr_' /etc/apache2 2>/dev/null; echo '--- varlib ---'; ls -la /var/lib 2>/dev/null; ls -la /var/lib/php/sessions 2>/dev/null
ls -la / ; echo '---OPT/SRV/MNT/DATA---'; ls -la /opt /srv /mnt /data 2>/dev/null; echo '---FILES---'; find /opt /srv /mnt /data -type f 2>/dev/null | head -60; echo '---ROOT/HOME---'; ls -la /root /home /home/ubuntu 2>/dev/null; echo '---HISTS---'; cat /root/.bash_history /home/ubuntu/.bash_history 2>/dev/null | tail -40
ls -la /var/backups /var/log /tmp 2>/dev/null; echo '---'; grep -rilE 'oper|opr|ops|record|archive|sqlite|\.db' /etc /var/log 2>/dev/null | head -40
ls -laR /var/www 2>/dev/null | head -200; echo '---ACCESS---'; tail -n 60 /var/log/apache2/access.log 2>/dev/null; echo '---ERROR---'; tail -n 40 /var/log/apache2/error.log 2>/dev/null
find /var/lib /srv /opt /data /mnt /home -maxdepth 4 \( -path /var/lib/mysql -o -path /var/lib/postgresql \) -prune -o -type f \( -iname '*opr*' -o -iname '*operation*' -o -iname '*.sql' -o -iname '*.sqlite' -o -iname '*.db' -o -iname '*.dump' -o -iname '*.tar*' -o -iname '*.bak' \) -print 2>/dev/null | head -100
ls -la / /mnt /data /srv /opt /home /root 2>&1; echo '---MOUNTS---'; mount | grep -Ev 'proc|sysfs|devtmpfs|devpts|cgroup|tmpfs|overlay|mqueue|shm|securityfs|debugfs|tracefs|pstore|bpf|configfs|fusectl' 2>&1
=== HSTS/wget ===
# HSTS 1.0 Known Hosts database for GNU Wget.
# Edit at your own risk.
# <hostname> <port> <incl. subdomains> <created> <max-age>
=== GREP ===
root@ubuntu:~# 
```
root@ubuntu:~# 
```
