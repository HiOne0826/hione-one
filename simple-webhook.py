#!/usr/bin/env python3
import os
import time
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
        print(f"[{time.ctime()}] Deploy trigger received!")
        os.chdir("/root/hione-one")
        subprocess.run(["git", "fetch", "origin"], check=True)
        subprocess.run(["git", "checkout", "origin/main", "--", "dist/"], check=True)
        subprocess.run(["cp", "-r", "dist/.", "/www/wwwroot/hione.one/"], check=True)
        print(f"[{time.ctime()}] Deploy complete!")

def main():
    print("Starting webhook server on port 3000...")
    server = HTTPServer(("0.0.0.0", 3000), WebhookHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
