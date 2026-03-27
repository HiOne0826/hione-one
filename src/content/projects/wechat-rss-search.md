---
title: 微信公众号订阅搜索
description: 自助搭建微信公众号 RSS 订阅服务，支持全文搜索、时间范围筛选和 AI 主题相关性分析
status: 已完成
techStack:
  - Node.js
  - TypeScript
  - Express
  - Docker
  - OpenAI
  - WeWe RSS
image: /images/projects/wechat-rss-search.png
demoUrl: https://rss.hione.one/
repoUrl: https://github.com/your-username/wechat-rss-subscriber
publishDate: 2026-03-27
updatedDate: 2026-03-27
---

## 项目背景

想要持续关注几个微信公众号的文章，但微信订阅号信息流混乱，很难找到历史文章，也不方便搜索特定主题。这个项目帮你：

- ✅ 自助搭建私有微信公众号 RSS 订阅服务
- ✅ 定期自动拉取最新文章保存到本地
- ✅ 支持关键词搜索 + 发布时间范围筛选
- ✅ 使用 AI 判断文章是否与特定主题相关
- ✅ 打包成 Claude Code Skill 供其他 Agent 使用
- ✅ 完整 Docker Compose 一键部署

## 功能特性

### 核心功能
- **多公众号订阅**：通过 WeWe RSS 获取公众号 RSS 源，定时自动拉取
- **全文搜索**：本地缓存所有文章，支持关键词快速搜索
- **时间范围筛选**：可指定起止日期，只搜索某段时间内的文章
- **AI 主题分析**：输入文章链接和主题问题，AI 会判断文章是否讨论该主题并给出理由
- **Web 界面**：响应式网页界面，手机电脑都能用
- **REST API**：完整 API 可供二次开发
- **Claude Code Skill**：可在 Claude Code 中直接调用功能

### 技术架构
- **WeWe RSS**：负责抓取微信公众号文章生成 RSS
- **Node.js + TypeScript**：后端服务和 CLI 工具
- **Express**：Web 服务器和 API
- **Docker Compose**：一键编排所有服务
- **OpenAI API**：可选，用于 AI 内容分析
- **JSON 文件存储**：无需数据库，简单可靠

## 使用说明

### 一键部署（自己搭建）

```bash
# 1. 克隆项目
git clone https://github.com/your-username/wechat-rss-subscriber.git
cd wechat-rss-subscriber

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 添加 OPENAI_API_KEY（可选，AI 功能需要）

# 3. 修改 docker-compose.yml 填入你的微信 Cookie
# WECHAT_OPENID_COOKIE 需要从微信网页版获取

# 4. 启动服务
docker-compose up -d

# 5. 访问 http://your-server:3000 即可使用
```

### 添加订阅

1. 在 WeWe RSS 中添加你想要订阅的公众号
2. 获取 RSS 链接
3. 使用 CLI 添加订阅：`node dist/index.js add <rss-url> "公众号名称"`

### 使用搜索

- **网页搜索**：直接在首页输入关键词，可选填写起止日期
- **CLI 搜索**：`node dist/index.js search "关键词" --from 2026-01-01 --to 2026-03-31`
- **AI 分析**：在搜索结果点击「AI 分析」，输入你的问题，例如：「这篇文章是否讨论社保基数调整？」

### Claude Code Skill 安装

在 Claude Code 中安装：
```
npx skills add github-username/wechat-rss-subscriber@skill
```

安装后即可在 Claude Code 中使用：
- `addSubscription` - 添加订阅
- `fetchArticles` - 拉取最新文章
- `searchArticles` - 搜索文章（支持时间范围）
- `analyzeTopicRelevance` - AI 分析主题相关性
- `listSubscriptions` - 列出所有订阅

## 在线试用

我已经搭建了公共服务，可以直接试用：

👉 **[立即使用](https://rss.hione.one/)**

## 技能下载

如果你想在自己的 Claude Code 中使用这个 Skill，可以在这里下载：

👉 **[Skill JSON](https://raw.githubusercontent.com/your-username/wechat-rss-subscriber/main/skill.json)**

## 项目亮点

- **完全私有**：所有数据保存在自己服务器，不依赖第三方
- **零成本**：使用开源工具，只需要一个 VPS 即可运行
- **可扩展**：REST API 方便二次开发，可以集成到其他工作流
- **AI 增强**：利用大模型帮你快速筛选感兴趣的文章，节省阅读时间

## 后续优化方向

- 添加全文搜索引擎（Elasticsearch/Lunr.js）
- 支持邮件推送新文章通知
- 添加标签分类功能
- 支持导出所有文章为 Markdown 归档

