## EMQ Cert setup

* Get certs `sudo certbot certonly --cert-name api.akriya.co.in `
* locate certs   
`cd /etc/letsencrypt/live/keys`

* Update EMQ Config   
Goto `cd /etc/emqttd/ `

`sudo vi emq.conf`

* Restart to confirm : sudo service emqttd restart       

* For Logs   
`cd /var/log/emqttd/`
`tail *.log`

  
## Snaps of old
`ls -al` in `/etc/letsencrypt`

```
drwxr-xr-x   9 root root 4096 May 28 12:03 .
drwxr-xr-x 106 root root 4096 Nov 22  2019 ..
drwx------   4 root root 4096 Feb 13  2018 accounts
drwx------   9 root root 4096 Jan  1  2019 archive
-rw-r--r--   1 root root  121 Jan 31  2018 cli.ini
drwxr-xr-x   2 root root 4096 Feb 22 18:45 csr
drwx------   2 root root 4096 Feb 22 18:45 keys
drwx------   9 root root 4096 Jan  1  2019 live
-rw-r--r--   1 root root 1143 Feb 12  2018 options-ssl-nginx.conf
drwxr-xr-x   2 root root 4096 Feb 22 18:45 renewal
drwxr-xr-x   5 root root 4096 Feb 12  2018 renewal-hooks
-rw-r--r--   1 root root  424 Feb 12  2018 ssl-dhparams.pem
-rw-r--r--   1 root root   64 Feb 12  2018 .updated-options-ssl-nginx-conf-digest.txt
-rw-r--r--   1 root root   64 Feb 12  2018 .updated-ssl-dhparams-pem-digest.txt
```
