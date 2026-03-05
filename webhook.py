#!/usr/bin/env python3
"""
GitHub Webhook 接收器 - hione.one 自动部署
用 Python 写的，服务器上肯定有 Python
"""

import os
import sys
import hmac
import hashlib
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

# 配置
PORT = 3000
SECRET = b"5f613a1fe12b3a8b5bb478b776c17db3"  # 自动生成的密钥
PROJECT_DIR = "/root/hione-one"
DEPLOY_DIR = "/var/www/hione.one"

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/webhook":
            self.send_response(404)
            self.end_headers()
            return

        # 读取请求体
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        # 验证签名
        signature = self.headers.get('X-Hub-Signature-256', '')
        if not self.verify_signature(body, signature):
            print("签名验证失败")
            self.send_response(403)
            self.end_headers()
            return

        # 检查事件
        event = self.headers.get('X-GitHub-Event', '')
        if event == 'push':
            import json
            payload = json.loads(body.decode('utf-8'))
            if payload.get('ref') == 'refs/heads/main':
                print("收到 main 分支的 push 事件，开始部署...")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Deploy triggered")
                
                # 异步执行部署
                import threading
                threading.Thread(target=self.run_deploy).start()
                return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def verify_signature(self, body, signature):
        if not signature:
            return False
        hmac_obj = hmac.new(SECRET, body, hashlib.sha256)
        digest = f"sha256={hmac_obj.hexdigest()}"
        return hmac.compare_digest(digest, signature)

    def run_deploy(self):
        print("========== 开始部署 ==========")
        os.chdir(PROJECT_DIR)
        
        # 1. 拉取最新代码
        print("1/2 - 拉取最新代码...")
        subprocess.run(["git", "fetch", "origin"], check=True)
        subprocess.run(["git", "checkout", "origin/main", "--", "dist/"], check=True)
        
        # 2. 部署到 Nginx 目录
        print("2/2 - 部署到 Nginx 目录...")
        dist_dir = os.path.join(PROJECT_DIR, "dist")
        if os.path.exists(dist_dir):
            import shutil
            for item in os.listdir(dist_dir):
                src = os.path.join(dist_dir, item)
                dst = os.path.join(DEPLOY_DIR, item)
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
            print("部署完成！")
        else:
            print("警告：dist 目录不存在")
        
        print("========== 部署结束 ==========")

def main():
    server = HTTPServer(('0.0.0.0', PORT), WebhookHandler)
    print(f"Webhook 服务器运行在 http://0.0.0.0:{PORT}")
    print(f"Webhook URL: http://your-server-ip:{PORT}/webhook")
    server.serve_forever()

if __name__ == "__main__":
    main()
