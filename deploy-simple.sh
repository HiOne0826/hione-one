#!/bin/bash
# hione.one 简单部署脚本（只拉取 dist）

set -e

echo "========== 开始部署 hione.one =========="

# 1. 拉取最新代码（只拉取 dist 分支）
echo "1/2 - 拉取最新代码..."
cd /root/hione-one || (echo "错误：项目目录不存在" && exit 1)
git fetch origin
git checkout origin/dist -- dist/

# 2. 部署到 Nginx 目录
echo "2/2 - 部署到 Nginx 目录..."
cp -r dist/* /var/www/hione.one/

echo ""
echo "========== 部署完成！=========="
echo "网站已更新：http://hione.one"
