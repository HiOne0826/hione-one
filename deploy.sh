#!/bin/bash
# hione.one 自动部署脚本

set -e

echo "========== 开始部署 hione.one =========="

# 1. 拉取最新代码
echo "1/4 - 拉取最新代码..."
cd /root/hione-one || (echo "错误：项目目录不存在" && exit 1)
git pull origin main

# 2. 安装依赖
echo "2/4 - 安装依赖..."
npm install

# 3. 构建项目
echo "3/4 - 构建项目..."
npm run build

# 4. 部署到 Nginx 目录
echo "4/4 - 部署到 Nginx 目录..."
cp -r dist/* /var/www/hione.one/

echo ""
echo "========== 部署完成！=========="
echo "网站已更新：http://hione.one"
