#!/usr/bin/env python3 

'''
HTTPSSERVER.py
Serves up the folder this script is run from on a https server on the specified port
By default runs on port 443, but can be used as below to open on port 9000 (or any other port):

'/home/watchdog/htb/boxname$ python3 /opt/httpsServer.py 9000'

The above serves the /home/watchdog/htb/boxname directory on port 9000 as a https server
'''
import http.server, ssl
import sys
import os

CERTPATH = "/tmp/localhost.pem"
if not os.path.exists(CERTPATH):
    os.system(f"openssl req -new -x509 -keyout {CERTPATH} -out {CERTPATH} -days 365 -nodes -subj \"/C=UK/O=https-server/OU=https-server/CN=https.server.py\" >/dev/null")

port = 443
if len(sys.argv) > 1:
    try:
        p = int(sys.argv[1])
        if p < 1 or p > 65535:
            raise ValueError()

        port = p  
    except ValueError:
        print("[-] - Not a valid port number")
        sys.exit(-1)


server_address = ('0.0.0.0', port)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile=CERTPATH,ssl_version=ssl.PROTOCOL_TLSv1_2)

os.remove(CERTPATH)
print(f"[+] - Serving HTTPS Server on port {port} - [+]")
httpd.serve_forever()
