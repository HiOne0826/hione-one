#!/bin/bash
# 启动 hione.one Webhook 服务

cd /root/hione-one

# 杀掉旧进程
pkill -f 'python3 webhook.py' 2>/dev/null
sleep 1

# 启动新进程
nohup python3 webhook.py > webhook.log 2>&1 &
PID=$!

echo "Webhook 服务已启动，PID: $PID"
echo "日志文件: /root/hione-one/webhook.log"
echo ""
echo "查看日志: tail -f /root/hione-one/webhook.log"
echo "停止服务: pkill -f 'python3 webhook.py'"

# 验证
sleep 2
if ps aux | grep -q 'python3 webhook.py' | grep -v grep; then
    echo ""
    echo "✅ Webhook 服务运行正常"
else
    echo ""
    echo "❌ Webhook 服务启动失败，请检查日志"
fi
