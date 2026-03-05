#!/bin/bash
# hione.one 一键提交并推送脚本

set -e

echo "========== 开始发布 hione.one =========="

# 1. 构建项目
echo "1/3 - 构建项目..."
npm run build

# 2. 提交代码
echo "2/3 - 提交代码..."
git add .
git commit -m "Update website $(date '+%Y-%m-%d %H:%M:%S')" || echo "没有新的修改"

# 3. 推送到 GitHub
echo "3/3 - 推送到 GitHub..."
git push origin main

echo ""
echo "========== 发布完成！=========="
echo "服务器会在 5 分钟内自动拉取并部署"
echo "网站：http://hione.one"
