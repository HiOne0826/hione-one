#!/bin/bash
# 服务器上的自动部署脚本

set -e

# 项目目录
PROJECT_DIR="/root/hione-one"
DEPLOY_DIR="/www/wwwroot/hione.one"

cd $PROJECT_DIR

# 获取当前和远程的 commit hash
LOCAL_HASH=$(git rev-parse HEAD)
git fetch origin
REMOTE_HASH=$(git rev-parse origin/main)

# 如果有更新，就拉取并部署
if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
  echo "[$(date)] 发现新提交，开始部署..."
  
  # 拉取最新代码
  git pull origin main
  
  # 如果 dist 目录存在，就部署
  if [ -d "dist" ]; then
    echo "部署 dist 目录到 $DEPLOY_DIR..."
    cp -r dist/* $DEPLOY_DIR/
    echo "部署完成！"
  else
    echo "警告：dist 目录不存在"
  fi
else
  echo "[$(date)] 没有新提交"
fi
