# python-https-server

Serves up the folder this script is run from on a https server on the specified port
By default runs on port 443, but can be used as below to open on port 9000 (or any other port):

```bash
# Serves the /home/watchdog/htb/boxname directory on port 9000 as a https server
/home/watchdog/htb/boxname$ python3 /opt/httpsServer.py 9000
```

