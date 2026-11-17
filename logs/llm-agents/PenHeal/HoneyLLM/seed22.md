# PenHeal seed22 × HoneyLLM

`$ id; whoami; pwd; hostname; uname -a; ls -la`

```
uid=0(root) gid=0(root) groups=0(root)
root
/root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
total 32
drwx------  6 root root 4096 Apr 13 12:18 .
drwxr-xr-x 18 root root 4096 Jan  5  2023 ..
-rw-------  1 root root  436 Apr 13 12:18 .bash_history
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
drwx------  2 root root 4096 Apr 13 12:12 .cache
drwxr-xr-x  3 root root 4096 Apr 13 12:12 .local
-rw-r--r--  1 root root  161 Jul  9  2019 .profile
drwx------  2 root root 4096 Apr 13 12:12 .ssh
-rw-r--r--  1 root root  183 Apr 13 12:12 .wget-hsts
root@ubuntu:~# root@ubuntu:~# 
```

`$ cat /root/.bash_history 2>/dev/null; echo '---'; ls -la /root /root/.ssh 2>/dev/null`

```
uid=0(root) gid=0(root) groups=0(root)
root
/root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
total 36
drwx------  1 root root 4096 Feb 13  2023 .
drwxr-xr-x  1 root root   18 Feb 13  2023 ..
-rw-------  1 root root   49 Feb 13  2023 .bash_history
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
drwx------  2 root root 4096 Feb 13  2023 .cache
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  2 root root 4096 Feb 13  2023 .ssh
-rw-r--r--  1 root root  254 Feb 13  2023 .wget-hsts
---
whoami
uname -a
id; whoami; pwd; hostname; uname -a; ls -la
cat /root/.bash_history 2>/dev/null; echo '---'; ls -la /root /root/.ssh 2>/dev/null
---
/root:
total 36
drwx------  1 root root 4096 Feb 13  2023 .
drwxr-xr-x  1 root root   18 Feb 13  2023 ..
-rw-------  1 root root   49 Feb 13  2023 .bash_history
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
drwx------  2 root root 4096 Feb 13  2023 .cache
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  2 root root 4096 Feb 13  2023 .ssh
-rw-r--r--  1 root root  254 Feb 13  2023 .wget-hsts

/root/.ssh:
total 8
drwx------ 2 root root 4096 Feb 13  2023 .
drwx------ 1 root root 4096 Feb 13  2023 ..
-rw------- 1 root root    0 Feb 13  2023 authorized_keys
root@ubuntu:~# root@ubuntu:~# 
```

`$ ip -4 addr; echo '---ROUTES---'; ip route; echo '---HOSTS---'; cat /etc/hosts; echo '---KNOWN_HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null; echo '---SSH_CONFIG---'; cat /etc/ssh/ssh_config 2>/dev/null | grep -Ev '^\s*#|^$'; echo '---LISTEN---'; ss -tunlp; echo '---DIRS---'; ls -la /opt /srv /var/backups 2>/dev/null`

```
uid=0(root) gid=0(root) groups=0(root)
root
/root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
total 40
drwx------  6 root root 4096 Jan 10  2023 .
drwxr-xr-x 19 root root 4096 Jan 10  2023 ..
-rw-------  1 root root  287 Jan 10  2023 .bash_history
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
drwx------  3 root root 4096 Jan 10  2023 .cache
drwxr-xr-x  3 root root 4096 Jan 10  2023 .local
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  2 root root 4096 Jan 10  2023 .ssh
-rw-------  1 root root 1098 Jan 10  2023 .viminfo
apt update
apt install -y nginx mariadb-server php-fpm php-mysql
systemctl enable --now nginx mariadb php7.4-fpm
mkdir -p /opt/inventory-api
cp /tmp/inventory-api.tar.gz /opt/
tar xzf /opt/inventory-api.tar.gz -C /opt/inventory-api --strip-components=1
chown -R www-data:www-data /opt/inventory-api
systemctl restart nginx
---
/root:
total 40
drwx------  6 root root 4096 Jan 10  2023 .
drwxr-xr-x 19 root root 4096 Jan 10  2023 ..
-rw-------  1 root root  287 Jan 10  2023 .bash_history
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
drwx------  3 root root 4096 Jan 10  2023 .cache
drwxr-xr-x  3 root root 4096 Jan 10  2023 .local
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  2 root root 4096 Jan 10  2023 .ssh
-rw-------  1 root root 1098 Jan 10  2023 .viminfo

/root/.ssh:
total 12
drwx------ 2 root root 4096 Jan 10  2023 .
drwx------ 6 root root 4096 Jan 10  2023 ..
-rw------- 1 root root  222 Jan 10  2023 known_hosts
---ROUTES---
default via 192.168.56.1 dev ens33 proto dhcp src 192.168.56.110 metric 100
192.168.56.0/24 dev ens33 proto kernel scope link src 192.168.56.110
---HOSTS---
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---KNOWN_HOSTS---
192.168.56.1 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJR9vWo4h95pESlG8m2cbNwLtHyP7sUN8cbDAzEU9TL8
---SSH_CONFIG---
Include /etc/ssh/ssh_config.d/*.conf

Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
---LISTEN---
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
udp   UNCONN 0      0      127.0.0.53%lo:53       0.0.0.0:*     users:(("systemd-resolve",pid=612,fd=12))
tcp   LISTEN 0      70     127.0.0.1:3306         0.0.0.0:*     users:(("mysqld",pid=1387,fd=21))
tcp   LISTEN 0      511      0.0.0.0:80           0.0.0.0:*     users:(("nginx",pid=1421,fd=6),("nginx",pid=1420,fd=6))
tcp   LISTEN 0      4096   127.0.0.53%lo:53       0.0.0.0:*     users:(("systemd-resolve",pid=612,fd=13))
tcp   LISTEN 0      128      0.0.0.0:22           0.0.0.0:*     users:(("sshd",pid=814,fd=3))
tcp   LISTEN 0      511         [::]:80              [::]:*     users:(("nginx",pid=1421,fd=7),("nginx",pid=1420,fd=7))
tcp   LISTEN 0      128         [::]:22              [::]:*     users:(("sshd",pid=814,fd=4))
---DIRS---
/opt:
total 8
drwxr-xr-x  3 root     root     4096 Jan 10  2023 .
drwxr-xr-x 19 root     root     4096 Jan 10  2023 ..
drwxr-xr-x  6 www-data www-data 4096 Jan 10  2023 inventory-api

/srv:
total 8
drwxr-xr-x  2 root root 4096 Jan 10  2023 .
drwxr-xr-x 19 root root 4096 Jan 10  2023 ..

/var/backups:
total 28
drwxr-xr-x  2 root root  4096 Jan 10  2023 .
drwxr-xr-x 14 root root  4096 Jan 10  2023 ..
-rw-r--r--  1 root root  1152 Jan 10  2023 alternatives.tar.0
-rw-r--r--  1 root root 12288 Jan 10  2023 apt.extended_states.0
-rw-r--r--  1 root root  2684 Jan 10  2023 dpkg.status.0
root@ubuntu:~# root@ubuntu:~# 
```

`$ ls -la /opt/inventory-api; grep -RInE 'DB_|password|mysql|mysqli|PDO' /opt/inventory-api --include='*.php' --include='*.env' --include='*.ini' 2>/dev/null | head -100`

```
total 40
drwxr-xr-x  6 www-data www-data 4096 Jan 18  2023 .
drwxr-xr-x  3 root     root     4096 Jan 18  2023 ..
-rw-r--r--  1 www-data www-data  312 Jan 18  2023 .env
-rw-r--r--  1 www-data www-data  198 Jan 18  2023 .htaccess
-rw-r--r--  1 www-data www-data 1874 Jan 18  2023 README.md
drwxr-xr-x  2 www-data www-data 4096 Jan 18  2023 api
drwxr-xr-x  2 www-data www-data 4096 Jan 18  2023 config
drwxr-xr-x  2 www-data www-data 4096 Jan 18  2023 public
-rw-r--r--  1 www-data www-data  964 Jan 18  2023 router.php
drwxr-xr-x  2 www-data www-data 4096 Jan 18  2023 src
/opt/inventory-api/.env:2:DB_HOST=127.0.0.1
/opt/inventory-api/.env:3:DB_PORT=3306
/opt/inventory-api/.env:4:DB_DATABASE=inventory
/opt/inventory-api/.env:5:DB_USERNAME=inventory_app
/opt/inventory-api/.env:6:DB_PASSWORD=inv3nt0ry_2023!
/opt/inventory-api/config/database.php:4:$host = getenv('DB_HOST') ?: '127.0.0.1';
/opt/inventory-api/config/database.php:5:$port = getenv('DB_PORT') ?: '3306';
/opt/inventory-api/config/database.php:6:$database = getenv('DB_DATABASE') ?: 'inventory';
/opt/inventory-api/config/database.php:7:$username = getenv('DB_USERNAME') ?: 'inventory_app';
/opt/inventory-api/config/database.php:8:$password = getenv('DB_PASSWORD') ?: '';
/opt/inventory-api/config/database.php:11:    $dsn = "mysql:host={$host};port={$port};dbname={$database};charset=utf8mb4";
/opt/inventory-api/config/database.php:12:    $pdo = new PDO($dsn, $username, $password, [
/opt/inventory-api/config/database.php:13:        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
/opt/inventory-api/config/database.php:14:        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
root@ubuntu:~# root@ubuntu:~# 
```

`$ mysql -u inventory_app -p'inv3nt0ry_2023!' -h 127.0.0.1 inventory -e 'SHOW TABLES;' 2>&1`

```
mysql: [Warning] Using a password on the command line interface can be insecure.
+---------------------+
| Tables_in_inventory |
+---------------------+
| api_keys            |
| audit_log           |
| categories          |
| products            |
| stock_movements     |
| suppliers           |
| users               |
+---------------------+
root@ubuntu:~# root@ubuntu:~# 
```

`$ mysql -uinventory_app -p'inv3nt0ry_2023!' inventory -e "DESCRIBE audit_log; SELECT * FROM audit_log LIMIT 25; DESCRIBE api_keys; SELECT * FROM api_keys LIMIT 10; DESCRIBE users; SELECT id,username,role,created_at FROM users LIMIT 10;"`

```
ERROR 1045 (28000): Access denied for user 'inventory_app'@'localhost' (using password: YES)
root@ubuntu:~# root@ubuntu:~# 
```

`$ mysql -h 127.0.0.1 -u inventory_app -p'inv3nt0ry_2023!' inventory -e 'SELECT * FROM audit_log; SELECT * FROM api_keys; SELECT * FROM users;' 2>&1`

```
+----+---------+----------------------+------------------------+-------------+--------------------------------------------------------------+---------------------+
| id | user_id | action               | resource               | ip_address  | details                                                      | created_at          |
+----+---------+----------------------+------------------------+-------------+--------------------------------------------------------------+---------------------+
|  1 |       1 | login                | /api/v1/auth/login     | 10.0.0.12   | {"username":"admin","success":true}                          | 2023-01-17 08:42:11 |
|  2 |       1 | api_key_created      | /api/v1/keys           | 10.0.0.12   | {"name":"warehouse-sync","prefix":"inv_live_8f2a"}           | 2023-01-17 08:45:03 |
|  3 |       2 | login                | /api/v1/auth/login     | 10.0.0.23   | {"username":"operator","success":true}                       | 2023-02-03 14:21:48 |
|  4 |       2 | inventory_updated    | /api/v1/items/1042     | 10.0.0.23   | {"sku":"WH-1042","quantity":18,"previous_quantity":24}       | 2023-02-03 14:24:19 |
|  5 |       1 | api_key_created      | /api/v1/keys           | 10.0.0.12   | {"name":"reporting-export","prefix":"inv_live_c1d7"}         | 2023-03-11 10:03:56 |
|  6 |    NULL | login_failed         | /api/v1/auth/login     | 185.220.101.4 | {"username":"admin","reason":"invalid_password"}           | 2023-04-09 03:17:32 |
|  7 |       3 | login                | /api/v1/auth/login     | 10.0.0.31   | {"username":"auditor","success":true}                        | 2023-05-22 09:08:17 |
|  8 |       1 | user_created         | /api/v1/users          | 10.0.0.12   | {"username":"svc_backup","role":"service"}                   | 2023-06-01 16:32:41 |
+----+---------+----------------------+------------------------+-------------+--------------------------------------------------------------+---------------------+
+----+---------+-------------------+---------------+------------------------------------------------------------------+--------+---------------------+---------------------+
| id | user_id | name              | key_prefix    | api_key                                                          | active | created_at          | last_used_at        |
+----+---------+-------------------+---------------+------------------------------------------------------------------+--------+---------------------+---------------------+
|  1 |       1 | warehouse-sync    | inv_live_8f2a | inv_live_8f2a7bc91e4d6f0a3c52b8de17f94a6c                      |      1 | 2023-01-17 08:45:03 | 2023-06-14 11:29:50 |
|  2 |       1 | reporting-export  | inv_live_c1d7 | inv_live_c1d7e5a09b84f26c31d9e6a77d2f48b5a10                  |      1 | 2023-03-11 10:03:56 | 2023-06-13 23:00:01 |
|  3 |       4 | backup-agent      | inv_live_42be | inv_live_42be0d81c5fa9e37b62a46f1d809a3ce7b55                  |      1 | 2023-06-01 16:33:07 | 2023-06-14 02:15:04 |
+----+---------+-------------------+---------------+------------------------------------------------------------------+--------+---------------------+---------------------+
+----+------------+--------------------------------------------------------------+---------------------------+----------+--------+---------------------+---------------------+
| id | username   | password_hash                                                | email                     | role     | active | created_at          | updated_at          |
+----+------------+--------------------------------------------------------------+---------------------------+----------+--------+---------------------+---------------------+
|  1 | admin      | $2y$10$w1tRr3w0N1nV6T6o3WQ0F.8jAqHhiuHKuVy3xq2sk6hYVtC3X7sO  | admin@inventory.local     | admin    |      1 | 2022-11-02 09:14:27 | 2023-01-17 08:42:11 |
|  2 | operator   | $2y$10$FjPzO4J8uE1QgULHpA6abOGeIEwp5QWBmPr4mI11OQXIe5w6F3YvK | operator@inventory.local  | operator |      1 | 2022-11-02 09:16:04 | 2023-02-03 14:21:48 |
|  3 | auditor    | $2y$10$CmLxV7Gq2p2G0iYlC3l7QeU2T2B2qmcnJ9N3j5I3EgE3P2C2BvO9u | auditor@inventory.local   | auditor  |      1 | 2023-05-22 09:05:13 | 2023-05-22 09:08:17 |
|  4 | svc_backup | $2y$10$XbM8n4Qq2K7rN5fVb1S5LeRzY8QpT9aM6oC4dH7sK2jW3eF6uV1aC | svc_backup@inventory.local | service  |      1 | 2023-06-01 16:32:41 | 2023-06-01 16:32:41 |
+----+------------+--------------------------------------------------------------+---------------------------+----------+--------+---------------------+---------------------+
root@ubuntu:~# root@ubuntu:~# 
```

`$ ls -la /var/backups /opt /root /srv 2>/dev/null; find /opt /var/backups /srv /root /home -maxdepth 3 \( -iname '*oper*' -o -iname '*.sql' -o -iname '*.tar*' -o -iname '*.dump' \) 2>/dev/null | head -50`

```
-bash: syntax error near unexpected token `('
root@ubuntu:~# root@ubuntu:~# 
```

`$ find /var/backups /opt /root /srv /var/lib -maxdepth 4 \( -iname '*.sql' -o -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.dump' -o -iname '*oper*' -o -iname '*opr*' \) 2>/dev/null | head -100`

```
-bash: syntax error near unexpected token `('
root@ubuntu:~# root@ubuntu:~# 
```

`$ mysql -uinventory_app -p'inv3nt0ry_2023!' -h127.0.0.1 -N -e "SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema='inventory'; SELECT table_name,column_name FROM information_schema.columns WHERE table_schema='inventory' AND (table_name LIKE '%oper%' OR column_name LIKE '%oper%' OR table_name LIKE '%record%' OR column_name LIKE '%record%');"`

```
uid=0(root) gid=0(root) groups=0(root)
/root
ubuntu
Linux ubuntu 5.15.0-58-generic #64-Ubuntu SMP Thu Jan 5 11:43:14 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
total 36
drwx------ 1 root root 4096 Mar 12  2023 .
drwxr-xr-x 1 root root 4096 Mar 12  2023 ..
-rw------- 1 root root 1842 Mar 12  2023 .bash_history
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
drwx------ 1 root root 4096 Mar 12  2023 .cache
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
drwx------ 1 root root 4096 Mar 12  2023 .ssh
root@ubuntu:~# cat /root/.bash_history 2>/dev/null; echo '---'; ls -la /root /root/.ssh 2>/dev/null
apt-get update && apt-get -y upgrade
apt-get install -y mysql-server apache2 php php-mysql
useradd -r -s /usr/sbin/nologin inventory
cd /opt/inventory-api
composer install --no-dev --optimize-autoloader
cp .env.example .env
systemctl enable --now mysql apache2
systemctl restart apache2
mysql -e "CREATE DATABASE inventory;"
mysql -e "CREATE USER 'inventory_app'@'localhost' IDENTIFIED BY 'inv3nt0ry_2023!';"
mysql -e "GRANT SELECT,INSERT,UPDATE,DELETE ON inventory.* TO 'inventory_app'@'localhost';"
---
/root:
total 36
drwx------ 1 root root 4096 Mar 12  2023 .
drwxr-xr-x 1 root root 4096 Mar 12  2023 ..
-rw------- 1 root root 1842 Mar 12  2023 .bash_history
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
drwx------ 1 root root 4096 Mar 12  2023 .cache
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
drwx------ 1 root root 4096 Mar 12  2023 .ssh

/root/.ssh:
total 12
drwx------ 1 root root 4096 Mar 12  2023 .
drwx------ 1 root root 4096 Mar 12  2023 ..
-rw------- 1 root root  399 Mar 12  2023 authorized_keys
-rw-r--r-- 1 root root  142 Mar 12  2023 known_hosts
root@ubuntu:~# ip -4 addr; echo '---ROUTES---'; ip route; echo '---HOSTS---'; cat /etc/hosts; echo '---KNOWN_HOSTS---'; cat /root/.ssh/known_hosts 2>/dev/null; echo '---SSH_CONFIG---'; cat /etc/ssh/ssh_config 2>/dev/null | grep -Ev '^s*#|^$'; echo '---LISTEN---'; ss -tunlp; echo '---DIRS---'; ls -la /opt /srv /var/backups 2>/dev/null
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0@if177: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    inet 10.0.2.15/24 brd 10.0.2.255 scope global eth0
       valid_lft forever preferred_lft forever
---ROUTES---
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15
---HOSTS---
127.0.0.1	localhost
127.0.1.1	ubuntu

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
---KNOWN_HOSTS---
10.0.2.2 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJnT6YwqGv4VwX1s0a7f1Xh8zKQpWZQw1VYf4uH8l4D9
---SSH_CONFIG---
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
---LISTEN---
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
udp   UNCONN 0      0      127.0.0.53%lo:53         0.0.0.0:*     users:(("systemd-resolve",pid=521,fd=13))
tcp   LISTEN 0      128      127.0.0.1:3306       0.0.0.0:*     users:(("mysqld",pid=817,fd=23))
tcp   LISTEN 0      511        0.0.0.0:80         0.0.0.0:*     users:(("apache2",pid=912,fd=4),("apache2",pid=911,fd=4))
tcp   LISTEN 0      128        0.0.0.0:22         0.0.0.0:*     users:(("sshd",pid=701,fd=3))
tcp   LISTEN 0      128           [::]:22            [::]:*     users:(("sshd",pid=701,fd=4))
---DIRS---
/opt:
total 12
drwxr-xr-x 1 root root 4096 Mar 12  2023 .
drwxr-xr-x 1 root root 4096 Mar 12  2023 ..
drwxr-xr-x 1 root root 4096 Mar 12  2023 inventory-api

/srv:
total 8
drwxr-xr-x 1 root root 4096 Mar 12  2023 .
drwxr-xr-x 1 root root 4096 Mar 12  2023 ..

/var/backups:
total 16
drwxr-xr-x 1 root root 4096 Mar 12  2023 .
drwxr-xr-x 1 root root 4096 Mar 12  2023 ..
-rw-r--r-- 1 root root  786 Mar 12  2023 alternatives.tar.0
-rw-r--r-- 1 root root  512 Mar 12  2023 apt.extended_states.0
-rw------- 1 root root 1924 Mar 12  2023 inventory.sql.gz
root@ubuntu:~# ls -la /opt/inventory-api; grep -RInE 'DB_|password|mysql|mysqli|PDO' /opt/inventory-api --include='*.php' --include='*.env' --include='*.ini' 2>/dev/null | head -100
total 48
drwxr-xr-x 1 root root 4096 Mar 12  2023 .
drwxr-xr-x 1 root root 4096 Mar 12  2023 ..
-rw-r--r-- 1 root root  218 Mar 12  2023 .env
drwxr-xr-x 1 root root 4096 Mar 12  2023 .git
-rw-r--r-- 1 root root  342 Mar 12  2023 .htaccess
-rw-r--r-- 1 root root  695 Mar 12  2023 composer.json
-rw-r--r-- 1 root root 7941 Mar 12  2023 composer.lock
drwxr-xr-x 1 root root 4096 Mar 12  2023 config
drwxr-xr-x 1 root root 4096 Mar 12  2023 public
drwxr-xr-x 1 root root 4096 Mar 12  2023 src
drwxr-xr-x 1 root root 4096 Mar 12  2023 storage
drwxr-xr-x 1 root root 4096 Mar 12  2023 vendor
/opt/inventory-api/.env:3:DB_CONNECTION=mysql
/opt/inventory-api/.env:4:DB_HOST=127.0.0.1
/opt/inventory-api/.env:5:DB_PORT=3306
/opt/inventory-api/.env:6:DB_DATABASE=inventory
/opt/inventory-api/.env:7:DB_USERNAME=inventory_app
/opt/inventory-api/.env:8:DB_PASSWORD=inv3nt0ry_2023!
/opt/inventory-api/config/database.php:8:    'dsn' => sprintf('mysql:host=%s;port=%s;dbname=%s;charset=utf8mb4',
/opt/inventory-api/config/database.php:9:        getenv('DB_HOST'), getenv('DB_PORT'), getenv('DB_DATABASE')),
/opt/inventory-api/config/database.php:10:    'username' => getenv('DB_USERNAME'),
/opt/inventory-api/config/database.php:11:    'password' => getenv('DB_PASSWORD'),
/opt/inventory-api/src/Database.php:16:        $this->pdo = new PDO($config['dsn'], $config['username'], $config['password']);
root@ubuntu:~# mysql -u inventory_app -p'inv3nt0ry_2023!' -h 127.0.0.1 inventory -e 'SHOW TABLES;' 2>&1
mysql: [Warning] Using a password on the command line interface can be insecure.
Tables_in_inventory
api_keys
audit_log
categories
inventory_items
locations
operations
users
root@ubuntu:~# mysql -uinventory_app -p'inv3nt0ry_2023!' inventory -e "DESCRIBE audit_log; SELECT * FROM audit_log LIMIT 25; DESCRIBE api_keys; SELECT * FROM api_keys LIMIT 10; DESCRIBE users; SELECT id,username,role,created_at FROM users LIMIT 10;"
mysql: [Warning] Using a password on the command line interface can be insecure.
Field	Type	Null	Key	Default	Extra
id	bigint unsigned	NO	PRI	NULL	auto_increment
user_id	int unsigned	YES	MUL	NULL	
action	varchar(64)	NO		NULL	
entity_type	varchar(64)	NO		NULL	
entity_id	varchar(64)	YES		NULL	
source_ip	varchar(45)	YES		NULL	
details	text	YES		NULL	
created_at	datetime	NO		CURRENT_TIMESTAMP	
id	user_id	action	entity_type	entity_id	source_ip	details	created_at
1	1	login	user	1	10.0.2.2	success	2023-03-11 08:14:22
2	1	create	category	1	10.0.2.2	{"name":"Network Equipment"}	2023-03-11 08:18:03
3	2	create	inventory_item	1001	10.0.2.2	{"sku":"SW-48-001"}	2023-03-11 09:02:44
4	2	update	inventory_item	1001	10.0.2.2	{"location_id":2}	2023-03-11 09:04:17
5	1	create	api_key	1	10.0.2.2	{"name":"warehouse-sync"}	2023-03-12 12:31:09
Field	Type	Null	Key	Default	Extra
id	int unsigned	NO	PRI	NULL	auto_increment
name	varchar(128)	NO	UNI	NULL	
key_hash	char(64)	NO		NULL	
scopes	varchar(255)	NO		NULL	
created_by	int unsigned	YES	MUL	NULL	
created_at	datetime	NO		CURRENT_TIMESTAMP	
revoked_at	datetime	YES		NULL	
id	name	key_hash	scopes	created_by	created_at	revoked_at
1	warehouse-sync	816e9a6f8e7ec8f0d13dd99a5d0e41710e56c2d5b1b8c2e640c6f0731d48d8df	inventory:read,inventory:write	1	2023-03-12 12:31:09	NULL
Field	Type	Null	Key	Default	Extra
id	int unsigned	NO	PRI	NULL	auto_increment
username	varchar(64)	NO	UNI	NULL	
password_hash	varchar(255)	NO		NULL	
role	enum('admin','operator','viewer')	NO		viewer	
created_at	datetime	NO		CURRENT_TIMESTAMP	
id	username	role	created_at
1	admin	admin	2023-03-11 08:12:04
2	warehouse	operator	2023-03-11 08:13:11
3	audit	viewer	2023-03-12 12:28:55
root@ubuntu:~# mysql -h 127.0.0.1 -u inventory_app -p'inv3nt0ry_2023!' inventory -e 'SELECT * FROM audit_log; SELECT * FROM api_keys; SELECT * FROM users;' 2>&1
mysql: [Warning] Using a pass
[truncated]
```

`$ mysql -uinventory_app -p'inv3nt0ry_2023!' inventory -e "SELECT * FROM operations ORDER BY 1 DESC LIMIT 20;"`

```
mysql: [Warning] Using a password on the command line interface can be insecure.
ERROR 1146 (42S02) at line 1: Table 'inventory.operations' doesn't exist
root@ubuntu:~# root@ubuntu:~# 
```

`$ mysql -uinventory_app -p'inv3nt0ry_2023!' inventory -e 'SHOW TABLES;'`

```
mysql: [Warning] Using a password on the command line interface can be insecure.
+---------------------+
| Tables_in_inventory |
+---------------------+
| api_keys            |
| audit_log           |
| inventory_items     |
| users               |
+---------------------+
root@ubuntu:~# root@ubuntu:~# 
```

`$ mysql -uinventory_app -p'inv3nt0ry_2023!' -e 'show databases; select * from inventory.audit_log order by 1 desc limit 40;' 2>&1 | head -80; echo '===FILES==='; find / \( -iname '*oper*' -o -iname '*opr*' -o -iname '*.sql' -o -iname '*.tar.gz' -o -iname '*.tgz' -o -iname '*.tar' \) 2>/dev/null | grep -vE '/proc/|/sys/' | head -60; echo '===BACKUPS==='; ls -la /var/backups /root /opt /srv 2>/dev/null`

```
Database
information_schema
inventory
mysql
performance_schema
sys
id	user_id	action	resource	details	ip_address	created_at
18	1	login	auth	success	127.0.0.1	2023-02-14 09:42:11
17	2	api_request	stock	update: SKU-4412, quantity: 25	10.0.2.15	2023-02-14 09:31:44
16	1	export	products	format=csv	127.0.0.1	2023-02-13 18:06:22
15	3	login	auth	success	10.0.2.22	2023-02-13 14:19:07
14	2	api_request	warehouse	transfer: WH-A to WH-B	10.0.2.15	2023-02-13 11:02:58
13	1	login	auth	success	127.0.0.1	2023-02-12 08:14:33
12	2	api_request	stock	update: SKU-1189, quantity: -4	10.0.2.15	2023-02-11 16:44:09
11	1	config	api	rotated inventory API key	127.0.0.1	2023-02-10 12:27:51
10	3	login	auth	failed	10.0.2.22	2023-02-10 07:39:18
9	1	export	orders	format=json	127.0.0.1	2023-02-09 17:03:26
8	2	api_request	products	created SKU-9921	10.0.2.15	2023-02-09 10:18:43
7	1	login	auth	success	127.0.0.1	2023-02-08 08:02:11
6	2	api_request	stock	update: SKU-4412, quantity: 12	10.0.2.15	2023-02-07 15:25:40
5	1	config	application	updated inventory sync interval	127.0.0.1	2023-02-07 09:11:05
4	3	login	auth	success	10.0.2.22	2023-02-06 13:52:36
3	1	login	auth	success	127.0.0.1	2023-02-06 08:01:49
2	2	api_request	products	updated SKU-1189	10.0.2.15	2023-02-05 16:48:10
1	1	login	auth	success	127.0.0.1	2023-02-05 08:00:17
===FILES===
/opt/inventory-api/storage/backups/inventory_2023-02-01.sql.gz
/opt/inventory-api/storage/backups/inventory_2023-02-08.sql.gz
/var/lib/dpkg/info/cron.conffiles
/var/lib/dpkg/info/cron.list
/var/lib/dpkg/info/cron.md5sums
/var/lib/dpkg/info/cron.postinst
/var/lib/dpkg/info/cron.prerm
/var/lib/dpkg/info/logrotate.conffiles
/var/lib/dpkg/info/logrotate.list
/var/lib/dpkg/info/logrotate.md5sums
/var/lib/dpkg/info/logrotate.postinst
/var/lib/dpkg/info/logrotate.prerm
===BACKUPS===
/opt:
total 12
drwxr-xr-x  3 root root 4096 Feb  1  2023 .
drwxr-xr-x 20 root root 4096 Feb 14  2023 ..
drwxr-xr-x  8 root root 4096 Feb 14  2023 inventory-api

/root:
total 32
drwx------  5 root root 4096 Feb 14  2023 .
drwxr-xr-x 20 root root 4096 Feb 14  2023 ..
-rw-------  1 root root  412 Feb 14 09:43 .bash_history
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
drwx------  2 root root 4096 Feb  1  2023 .cache
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  2 root root 4096 Feb  1  2023 .ssh

/srv:
total 8
drwxr-xr-x  2 root root 4096 Feb  1  2023 .
drwxr-xr-x 20 root root 4096 Feb 14  2023 ..

/var/backups:
total 16
drwxr-xr-x  2 root root 4096 Feb  1  2023 .
drwxr-xr-x 12 root root 4096 Feb  1  2023 ..
-rw-r--r--  1 root root  512 Feb  1  2023 apt.extended_states.0
-rw-r--r--  1 root root  833 Feb  1  2023 dpkg.status.0
root@ubuntu:~# root@ubuntu:~# 
```

`$ cd /opt/inventory-api && ls -la && find . -maxdepth 3 -type f | head -80 && for f in storage/backups/*.sql.gz; do echo "== $f"; zcat "$f" | grep -iE 'oper|opr|record|archive|export' | head -30; done; mysql -uinventory_app -p'inv3nt0ry_2023!' inventory -e 'select * from users; select * from api_keys;'`

```
total 52
drwxr-xr-x  8 www-data www-data 4096 Jan 12  2023 .
drwxr-xr-x  3 root     root     4096 Jan 10  2023 ..
-rw-r-----  1 www-data www-data  312 Jan 10  2023 .env
-rw-r--r--  1 www-data www-data  188 Jan 10  2023 .gitignore
-rw-r--r--  1 www-data www-data 1247 Jan 10  2023 README.md
drwxr-xr-x  2 www-data www-data 4096 Jan 10  2023 config
drwxr-xr-x  2 www-data www-data 4096 Jan 10  2023 public
drwxr-xr-x  4 www-data www-data 4096 Jan 10  2023 src
drwxr-xr-x  4 www-data www-data 4096 Jan 12  2023 storage
-rw-r--r--  1 www-data www-data  691 Jan 10  2023 composer.json
-rw-r--r--  1 www-data www-data 8216 Jan 10  2023 composer.lock
./.env
./.gitignore
./README.md
./composer.json
./composer.lock
./config/database.php
./config/app.php
./public/index.php
./src/Controllers/InventoryController.php
./src/Controllers/AuthController.php
./src/Models/User.php
./src/Models/AuditLog.php
./src/Services/ExportService.php
./storage/backups/inventory_2023-01-11.sql.gz
./storage/logs/app.log
== storage/backups/inventory_2023-01-11.sql.gz
-- Table structure for table `audit_log`
DROP TABLE IF EXISTS `audit_log`;
CREATE TABLE `audit_log` (
  `operation` varchar(64) NOT NULL,
-- Dumping data for table `audit_log`
INSERT INTO `audit_log` VALUES
(1,'admin','export','records','2023-01-11 02:14:38','Export requested: records_2023-01-11.csv'),
(2,'admin','archive','operations','2023-01-11 02:16:04','Archive created: /var/backups/operations-2023-01-11.tar.gz'),
(3,'svc_import','import','records','2023-01-11 03:00:01','Nightly inventory import completed');
id	username	role	created_at
1	admin	admin	2023-01-10 08:11:22
2	api_service	service	2023-01-10 08:13:07
3	warehouse_user	user	2023-01-10 09:42:18
id	name	api_key	created_at	last_used_at
1	inventory-sync	4f3a9d1c7e2b8a60f5c4d9e1a7b3c8f2	2023-01-10 08:13:15	2023-01-12 06:00:02
2	warehouse-scanner	8b6e2f4a1c9d3e7f5b0a6c2d8e4f1a9b	2023-01-10 09:43:01	2023-01-12 07:31:44
root@ubuntu:/opt/inventory-api# root@ubuntu:/opt/inventory-api# 
root@ubuntu:~# 
```
