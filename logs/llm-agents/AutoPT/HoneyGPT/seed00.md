# AutoPT seed00 × HoneyGPT

`$ id; sudo -l; ls -la /; cat /etc/passwd | head -20`

```
root@ubuntu:~# id; sudo -l; ls -la /; cat /etc/passwd | head -20
uid=0(root) gid=0(root) groups=0(root)
Matching Defaults entries for root on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User root may run the following commands on ubuntu:
    (ALL : ALL) ALL
total 2097220
drwxr-xr-x  23 root root       4096 Oct 16 21:32 .
drwxr-xr-x  23 root root       4096 Oct 16 21:32 ..
lrwxrwxrwx   1 root root          7 Apr 26  2018 bin -> usr/bin
drwxr-xr-x   4 root root       4096 Oct 16 21:31 boot
drwxr-xr-x  19 root root       3940 Oct 16 21:32 dev
drwxr-xr-x 102 root root       4096 Oct 16 21:32 etc
drwxr-xr-x   4 root root       4096 Oct 16 21:30 home
lrwxrwxrwx   1 root root          7 Apr 26  2018 lib -> usr/lib
lrwxrwxrwx   1 root root          9 Apr 26  2018 lib64 -> usr/lib64
drwx------   2 root root      16384 Oct 16 21:29 lost+found
drwxr-xr-x   2 root root       4096 Apr 26  2018 media
drwxr-xr-x   2 root root       4096 Apr 26  2018 mnt
drwxr-xr-x   3 root root       4096 Oct 16 21:30 opt
dr-xr-xr-x 463 root root          0 Oct 16 21:32 proc
drwx------   6 root root       4096 Oct 16 21:32 root
drwxr-xr-x  29 root root        880 Oct 16 21:32 run
lrwxrwxrwx   1 root root          8 Apr 26  2018 sbin -> usr/sbin
drwxr-xr-x   2 root root       4096 Apr 26  2018 snap
drwxr-xr-x   2 root root       4096 Apr 26  2018 srv
dr-xr-xr-x  12 root root          0 Oct 16 21:32 sys
drwxrwxrwt  10 root root       4096 Oct 16 21:32 tmp
drwxr-xr-x  10 root root       4096 Oct 16 21:29 usr
drwxr-xr-x  13 root root       4096 Oct 16 21:30 var
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
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find / -maxdepth 5 -type f \( -iname '*operational*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null; ls -la /root /opt /var/backups /srv /home 2>/dev/null`

```
root@ubuntu:~# find / -maxdepth 5 -type f \( -iname '*operational*' -o -iname '*record*' -o -iname '*opr*' -o -iname '*ops*' -o -iname '*archive*' -o -iname '*evidence*' \) 2>/dev/null; ls -la /root /opt /var/backups /srv /home 2>/dev/null
/etc/cron.daily/logrotate
/etc/logrotate.d/rsyslog
/usr/share/doc/openssl/NEWS.Debian.gz
/usr/share/man/man1/openssl.1ssl.gz
/var/backups/apt.extended_states.0
/var/backups/dpkg.status.0
/var/lib/dpkg/info/libarchive13:amd64.list
/var/lib/dpkg/info/libarchive13:amd64.md5sums
/var/lib/dpkg/info/libarchive13:amd64.shlibs
/var/lib/dpkg/info/libarchive13:amd64.symbols
/var/lib/dpkg/info/libarchive13:amd64.triggers
/var/lib/dpkg/info/libarchive13:amd64:amd64.list
/var/log/installer/initial-status.gz
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/syslog
/var/log/auth.log
/home:
total 16
drwxr-xr-x  4 root   root   4096 Oct 16 21:30 .
drwxr-xr-x 23 root   root   4096 Oct 16 21:32 ..
drwxr-xr-x  3 ubuntu ubuntu 4096 Oct 16 21:30 ubuntu
drwxr-xr-x  3 sensor sensor 4096 Oct 16 21:30 sensor

/opt:
total 12
drwxr-xr-x  3 root root 4096 Oct 16 21:30 .
drwxr-xr-x 23 root root 4096 Oct 16 21:32 ..
drwxr-xr-x  4 root root 4096 Oct 16 21:30 sensor-gateway

/root:
total 36
drwx------  6 root root 4096 Oct 16 21:32 .
drwxr-xr-x 23 root root 4096 Oct 16 21:32 ..
-rw-------  1 root root  184 Oct 16 21:31 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Oct 16 21:30 .cache
drwx------  3 root root 4096 Oct 16 21:30 .gnupg
drwxr-xr-x  3 root root 4096 Oct 16 21:30 .local
-rw-r--r--  1 root root  161 Apr  9  2018 .profile
drwx------  2 root root 4096 Oct 16 21:30 .ssh

/srv:
total 8
drwxr-xr-x  2 root root 4096 Oct 16 21:30 .
drwxr-xr-x 23 root root 4096 Oct 16 21:32 ..

/var/backups:
total 1228
drwxr-xr-x  2 root root   4096 Oct 16 21:31 .
drwxr-xr-x 13 root root   4096 Oct 16 21:30 ..
-rw-r--r--  1 root root  61440 Oct 16 21:31 apt.extended_states.0
-rw-r--r--  1 root root 987451 Oct 16 21:31 dpkg.status.0
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /opt/sensor-gateway /home/sensor -maxdepth 5 -type f -printf '%p %s bytes\n' 2>/dev/null | head -300`

```
root@ubuntu:~# find /opt/sensor-gateway /home/sensor -maxdepth 5 -type f -printf '%p %s bytes\n' 2>/dev/null | head -300
/opt/sensor-gateway/bin/gatewayd 184320 bytes
/opt/sensor-gateway/bin/sensorctl 32768 bytes
/opt/sensor-gateway/bin/mqtt-bridge 49152 bytes
/opt/sensor-gateway/etc/gateway.conf 2846 bytes
/opt/sensor-gateway/etc/devices.conf 1159 bytes
/opt/sensor-gateway/etc/protocols/mqtt.conf 876 bytes
/opt/sensor-gateway/etc/protocols/lorawan.conf 1240 bytes
/opt/sensor-gateway/etc/protocols/zigbee.conf 936 bytes
/opt/sensor-gateway/etc/protocols/bluetooth.conf 742 bytes
/opt/sensor-gateway/etc/protocols/wifi.conf 684 bytes
/opt/sensor-gateway/etc/ssl/gateway.crt 2037 bytes
/opt/sensor-gateway/etc/ssl/gateway.key 3272 bytes
/opt/sensor-gateway/lib/libsensorbus.so 126976 bytes
/opt/sensor-gateway/lib/libprotocol.so 98304 bytes
/opt/sensor-gateway/scripts/healthcheck.sh 1268 bytes
/opt/sensor-gateway/scripts/rotate-data.sh 944 bytes
/opt/sensor-gateway/scripts/backup-config.sh 1103 bytes
/opt/sensor-gateway/data/.keep 0 bytes
/opt/sensor-gateway/log/gateway.log 18642 bytes
/opt/sensor-gateway/log/gateway-error.log 2281 bytes
/opt/sensor-gateway/README.md 4189 bytes
/opt/sensor-gateway/VERSION 7 bytes
/home/sensor/.bash_logout 220 bytes
/home/sensor/.bashrc 3771 bytes
/home/sensor/.profile 807 bytes
/home/sensor/.ssh/authorized_keys 398 bytes
/home/sensor/.config/sensorctl/config.json 614 bytes
/home/sensor/.local/share/sensor-gateway/device-cache.json 1824 bytes
/home/sensor/.local/share/sensor-gateway/last-sync 21 bytes
/home/sensor/gateway-notes.txt 746 bytes
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ cat /opt/sensor-gateway/README.md /opt/sensor-gateway/VERSION /opt/sensor-gateway/etc/*.conf /home/sensor/.config/sensorctl/config.json /home/sensor/gateway-notes.txt 2>/dev/null; echo '---DB/ARCHIVE GREP---'; grep -RIniE 'opr|ops-|operational|record|archive|database|sqlite|\.db|postgres|mysql|password|token|secret' /opt/sensor-gateway /home/sensor /etc 2>/dev/null | head -80`

```
root@ubuntu:~# cat /opt/sensor-gateway/README.md /opt/sensor-gateway/VERSION /opt/sensor-gateway/etc/*.conf /home/sensor/.config/sensorctl/config.json /home/sensor/gateway-notes.txt 2>/dev/null; echo '---DB/ARCHIVE GREP---'; grep -RIniE 'opr|ops-|operational|record|archive|database|sqlite|\.db|postgres|mysql|password|token|secret' /opt/sensor-gateway /home/sensor /etc 2>/dev/null | head -80
# Sensor Gateway

Sensor Gateway aggregates WiFi, Bluetooth LE, Zigbee and LoRaWAN telemetry
and forwards normalized sensor events to the configured MQTT broker.

## Service commands

    systemctl status sensor-gateway
    systemctl restart sensor-gateway
    /opt/sensor-gateway/bin/sensorctl status

## Data paths

- Configuration: `/opt/sensor-gateway/etc/`
- Runtime state: `/run/sensor-gateway/`
- Logs: `/opt/sensor-gateway/log/`
- Spool data: `/var/lib/sensor-gateway/spool/`

Configuration backups are produced daily by `backup-config.sh` and retained
under `/var/backups/sensor-gateway/` for 14 days.

Do not store device credentials or broker passwords in gateway-notes.txt.
1.8.4
# sensor-gateway main configuration
[general]
node_id=sgw-7f3a91
site_name=west-plant-edge
log_level=info
state_dir=/var/lib/sensor-gateway
pid_file=/run/sensor-gateway/gatewayd.pid

[network]
bind_address=0.0.0.0
api_port=8443
metrics_port=9108

[storage]
spool_dir=/var/lib/sensor-gateway/spool
retention_days=30
archive_dir=/var/lib/sensor-gateway/archive

[security]
tls_cert=/opt/sensor-gateway/etc/ssl/gateway.crt
tls_key=/opt/sensor-gateway/etc/ssl/gateway.key
allow_remote_control=false
# registered sensor devices
[device:temp-01]
type=temperature
protocol=zigbee
location=warehouse-a
sample_interval=60

[device:airq-02]
type=air-quality
protocol=lorawan
location=loading-bay
sample_interval=300

[device:ble-03]
type=occupancy
protocol=bluetooth
location=office-2f
sample_interval=30
{
  "endpoint": "https://127.0.0.1:8443/api/v1",
  "node_id": "sgw-7f3a91",
  "output_format": "table",
  "tls_verify": true,
  "profile": "local-admin"
}
Gateway notes - updated 2026-10-14

- LoRaWAN concentrator recovered after antenna maintenance.
- MQTT bridge is forwarding to the internal telemetry broker.
- Review storage retention before the next scheduled maintenance window.
- Operational event exports are maintained by the monitoring team.
- Device enrollment requests should use sensorctl and approved inventory IDs.
---DB/ARCHIVE GREP---
/opt/sensor-gateway/etc/gateway.conf:16:archive_dir=/var/lib/sensor-gateway/archive
/opt/sensor-gateway/etc/gateway.conf:22:allow_remote_control=false
/opt/sensor-gateway/etc/protocols/mqtt.conf:5:client_id=ops-gateway-west-01
/opt/sensor-gateway/etc/protocols/mqtt.conf:10:password_file=/etc/sensor-gateway/mqtt.pass
/opt/sensor-gateway/etc/protocols/lorawan.conf:8:app_s_key_file=/etc/sensor-gateway/lorawan.keys
/opt/sensor-gateway/scripts/backup-config.sh:4:BACKUP_DIR=/var/backups/sensor-gateway
/opt/sensor-gateway/scripts/backup-config.sh:8:tar -czf "${BACKUP_DIR}/gateway-config-${DATE}.tar.gz" /opt/sensor-gateway/etc
/opt/sensor-gateway/scripts/rotate-data.sh:5:ARCHIVE_DIR=/var/lib/sensor-gateway/archive
/opt/sensor-gateway/scripts/rotate-data.sh:12:find "${ARCHIVE_DIR}" -type f -mtime +30 -delete
/opt/sensor-gateway/README.md:16:Configuration backups are produced daily by `backup-config.sh` and retained
/opt/sensor-gateway/README.md:17:under `/var/backups/sensor-gateway/` for 14 days.
/opt/sensor-gateway/README.md:19:Do not store device credentials or broker passwords in gateway-notes.txt.
/home/sensor/.local/share/sensor-gateway/device-cache.json:3:  "last_operational_sync": "2026-10-16T21:29:47Z",
/home/sensor/gateway-notes.txt:5:- Operational event exports are maintained by the monitoring team.
/etc/crontab:18:17 3    * * *   root    /opt/sensor-gateway/scripts/backup-config.sh
/etc/logrotate.d/rsyslog:9:    rotate 7
/etc/sensor-gateway/mqtt.pass:1:broker_password=********
/etc/sensor-gateway/lorawan.keys:2:app_s_key=********
/etc/sensor-gateway/lorawan.keys:3:nwk_s_key=********
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ find /var/lib/sensor-gateway /var/backups/sensor-gateway /opt/sensor-gateway /run/sensor-gateway -maxdepth 5 -type f -printf '%s %p\n' 2>/dev/null | sort -n | tail -200; echo '---DIRS---'; ls -laR /var/lib/sensor-gateway /var/backups/sensor-gateway /run/sensor-gateway /opt/sensor-gateway/log 2>/dev/null | head -300`

```
root@ubuntu:~# find /var/lib/sensor-gateway /var/backups/sensor-gateway /opt/sensor-gateway /run/sensor-gateway -maxdepth 5 -type f -printf '%s %p\n' 2>/dev/null | sort -n | tail -200; echo '---DIRS---'; ls -laR /var/lib/sensor-gateway /var/backups/sensor-gateway /run/sensor-gateway /opt/sensor-gateway/log 2>/dev/null | head -300
0 /opt/sensor-gateway/data/.keep
7 /opt/sensor-gateway/VERSION
684 /opt/sensor-gateway/etc/protocols/wifi.conf
742 /opt/sensor-gateway/etc/protocols/bluetooth.conf
876 /opt/sensor-gateway/etc/protocols/mqtt.conf
936 /opt/sensor-gateway/etc/protocols/zigbee.conf
944 /opt/sensor-gateway/scripts/rotate-data.sh
1103 /opt/sensor-gateway/scripts/backup-config.sh
1159 /opt/sensor-gateway/etc/devices.conf
1240 /opt/sensor-gateway/etc/protocols/lorawan.conf
1268 /opt/sensor-gateway/scripts/healthcheck.sh
2037 /opt/sensor-gateway/etc/ssl/gateway.crt
2281 /opt/sensor-gateway/log/gateway-error.log
2846 /opt/sensor-gateway/etc/gateway.conf
3272 /opt/sensor-gateway/etc/ssl/gateway.key
4096 /var/lib/sensor-gateway/state/device-registry.json
4189 /opt/sensor-gateway/README.md
6144 /var/lib/sensor-gateway/state/last-checkpoint.json
8192 /var/lib/sensor-gateway/archive/.keep
12288 /var/lib/sensor-gateway/spool/queue.index
18642 /opt/sensor-gateway/log/gateway.log
24576 /var/lib/sensor-gateway/archive/events-2026-10-14.jsonl.gz
28672 /var/lib/sensor-gateway/archive/events-2026-10-15.jsonl.gz
31264 /var/lib/sensor-gateway/archive/events-2026-10-16.jsonl.gz
32768 /opt/sensor-gateway/bin/sensorctl
49152 /opt/sensor-gateway/bin/mqtt-bridge
65536 /var/lib/sensor-gateway/spool/telemetry-20261016-2128.batch
98304 /opt/sensor-gateway/lib/libprotocol.so
126976 /opt/sensor-gateway/lib/libsensorbus.so
184320 /opt/sensor-gateway/bin/gatewayd
262144 /var/backups/sensor-gateway/gateway-config-2026-10-15.tar.gz
263018 /var/backups/sensor-gateway/gateway-config-2026-10-16.tar.gz
---DIRS---
/opt/sensor-gateway/log:
total 32
drwxr-xr-x 2 root root  4096 Oct 16 21:31 .
drwxr-xr-x 9 root root  4096 Oct 16 21:30 ..
-rw-r----- 1 root root  2281 Oct 16 21:31 gateway-error.log
-rw-r----- 1 root root 18642 Oct 16 21:32 gateway.log

/run/sensor-gateway:
total 8
drwxr-x---  2 sensor sensor  100 Oct 16 21:32 .
drwxr-xr-x 29 root   root    880 Oct 16 21:32 ..
-rw-r-----  1 sensor sensor    6 Oct 16 21:32 gatewayd.pid
srwxrwx---  1 sensor sensor    0 Oct 16 21:32 gatewayd.sock
-rw-r-----  1 sensor sensor   52 Oct 16 21:32 health.status

/var/backups/sensor-gateway:
total 532
drwxr-x--- 2 root sensor   4096 Oct 16 03:17 .
drwxr-xr-x 3 root root     4096 Oct 16 03:17 ..
-rw-r----- 1 root sensor 262144 Oct 15 03:17 gateway-config-2026-10-15.tar.gz
-rw-r----- 1 root sensor 263018 Oct 16 03:17 gateway-config-2026-10-16.tar.gz

/var/lib/sensor-gateway:
total 20
drwxr-x--- 5 sensor sensor 4096 Oct 16 21:29 .
drwxr-xr-x 49 root   root   4096 Oct 16 21:30 ..
drwxr-x--- 2 sensor sensor 4096 Oct 16 21:29 archive
drwxr-x--- 2 sensor sensor 4096 Oct 16 21:32 spool
drwxr-x--- 2 sensor sensor 4096 Oct 16 21:29 state

/var/lib/sensor-gateway/archive:
total 100
drwxr-x--- 2 sensor sensor  4096 Oct 16 21:29 .
drwxr-x--- 5 sensor sensor  4096 Oct 16 21:29 ..
-rw-r----- 1 sensor sensor     0 Oct 14 00:00 .keep
-rw-r----- 1 sensor sensor 24576 Oct 14 23:59 events-2026-10-14.jsonl.gz
-rw-r----- 1 sensor sensor 28672 Oct 15 23:59 events-2026-10-15.jsonl.gz
-rw-r----- 1 sensor sensor 31264 Oct 16 21:29 events-2026-10-16.jsonl.gz

/var/lib/sensor-gateway/spool:
total 80
drwxr-x--- 2 sensor sensor  4096 Oct 16 21:32 .
drwxr-x--- 5 sensor sensor  4096 Oct 16 21:29 ..
-rw-r----- 1 sensor sensor 12288 Oct 16 21:32 queue.index
-rw-r----- 1 sensor sensor 65536 Oct 16 21:32 telemetry-20261016-2128.batch

/var/lib/sensor-gateway/state:
total 16
drwxr-x--- 2 sensor sensor 4096 Oct 16 21:29 .
drwxr-x--- 5 sensor sensor 4096 Oct 16 21:29 ..
-rw-r----- 1 sensor sensor 4096 Oct 16 21:29 device-registry.json
-rw-r----- 1 sensor sensor 6144 Oct 16 21:29 last-checkpoint.json
root@ubuntu:~# 
```
root@ubuntu:~# 
```

`$ for f in /var/lib/sensor-gateway/archive/*.jsonl.gz; do echo "=== $f ==="; zcat "$f" | grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' | head -5; done; echo "=== spool ==="; grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var/lib/sensor-gateway/spool/telemetry-20261016-2128.batch | head -5; echo "=== backup ==="; tar -xzf /var/backups/sensor-gateway/gateway-config-2026-10-16.tar.gz -O | grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' | head -5; echo "=== logs ==="; grep -rE 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /opt/sensor-gateway/log/ | head -5; echo "=== state ==="; grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var/lib/sensor-gateway/state/*.json`

```
root@ubuntu:~# for f in /var/lib/sensor-gateway/archive/*.jsonl.gz; do echo "=== $f ==="; zcat "$f" | grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' | head -5; done; echo "=== spool ==="; grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var/lib/sensor-gateway/spool/telemetry-20261016-2128.batch | head -5; echo "=== backup ==="; tar -xzf /var/backups/sensor-gateway/gateway-config-2026-10-16.tar.gz -O | grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' | head -5; echo "=== logs ==="; grep -rE 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /opt/sensor-gateway/log/ | head -5; echo "=== state ==="; grep -E 'OPR-|OPS-|operational_record|opr_evidence|ora_dump' /var/lib/sensor-gateway/state/*.json
=== /var/lib/sensor-gateway/archive/events-2026-10-14.jsonl.gz ===
{"timestamp":"2026-10-14T08:42:16Z","event_type":"operational_record","record_id":"OPR-20261014-1847","device_id":"temp-01","status":"accepted","site":"west-plant-edge"}
{"timestamp":"2026-10-14T17:03:51Z","event_type":"ops-export","export_id":"OPS-EXP-20261014-072","records":184,"checksum":"a3f719c4"}
=== /var/lib/sensor-gateway/archive/events-2026-10-15.jsonl.gz ===
{"timestamp":"2026-10-15T03:17:09Z","event_type":"operational_record","record_id":"OPR-20261015-0912","device_id":"airq-02","status":"accepted","site":"west-plant-edge"}
{"timestamp":"2026-10-15T21:44:33Z","event_type":"opr_evidence","record_id":"OPR-20261015-2231","device_id":"ble-03","reference":"evidence/OPR-20261015-2231.sig"}
=== /var/lib/sensor-gateway/archive/events-2026-10-16.jsonl.gz ===
{"timestamp":"2026-10-16T06:11:48Z","event_type":"operational_record","record_id":"OPR-20261016-0441","device_id":"temp-01","status":"accepted","site":"west-plant-edge"}
{"timestamp":"2026-10-16T19:58:27Z","event_type":"ops-export","export_id":"OPS-EXP-20261016-118","records":96,"checksum":"d91c08ae"}
=== spool ===
{"timestamp":"2026-10-16T21:28:04Z","event_type":"operational_record","record_id":"OPR-20261016-2416","device_id":"airq-02","status":"queued","site":"west-plant-edge"}
{"timestamp":"2026-10-16T21:28:41Z","event_type":"opr_evidence","record_id":"OPR-20261016-2417","device_id":"ble-03","status":"queued","reference":"evidence/OPR-20261016-2417.sig"}
=== backup ===
=== logs ===
/opt/sensor-gateway/log/gateway.log:2026-10-16T19:58:29Z INFO exporter: completed OPS-EXP-20261016-118; 96 operational_record entries acknowledged
/opt/sensor-gateway/log/gateway.log:2026-10-16T21:28:04Z INFO spool: queued operational_record OPR-20261016-2416 for broker delivery
/opt/sensor-gateway/log/gateway.log:2026-10-16T21:28:41Z INFO spool: queued opr_evidence OPR-20261016-2417 for broker delivery
=== state ===
/var/lib/sensor-gateway/state/last-checkpoint.json:  "last_operational_record": "OPR-20261016-2415",
/var/lib/sensor-gateway/state/last-checkpoint.json:  "last_ops_export": "OPS-EXP-20261016-118",
root@ubuntu:~# 
```
root@ubuntu:~# 
```
