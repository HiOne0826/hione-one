#!/usr/bin/env python3
# 简单的 Webhook 测试脚本

import time
from http.server import HTTPServer, BaseHTTPRequestHandler

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Webhook server is running!\n')
        print(f"[{time.ctime()}] Received GET request")

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK\n')
        print(f"[{time.ctime()}] Received POST request")

def main():
    server = HTTPServer(('0.0.0.0', 3000), TestHandler)
    print("Test Webhook server running on http://0.0.0.0:3000")
    print("Test with: curl http://124.156.136.199:3000")
    server.serve_forever()

if __name__ == "__main__":
    main()
