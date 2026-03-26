---
title: 抖音/小红书 AI 对标分析
description: 专为街拍/时尚博主打造的对标分析神器，输入抖音/小红书链接即可获取帖子内容并进行 AI 分析，一键拆解爆款内容的底层逻辑
status: 已完成
techStack:
  - Next.js
  - FastAPI
  - 豆包大模型
  - TikHub API
image: /images/projects/douyin-ai.png
demoUrl: https://hione.one/douyin-ai/
publishDate: 2026-03-01
updatedDate: 2026-03-26
---

## 项目背景

飞书 CSM 工作中发现，很多客户需要抖音数据分析，但现有工具要么太贵，要么太难用...

## 技术实现

### 架构
- MediaCrawler 爬取数据
- FastAPI 提供 API
- OpenClaw 做 AI 分析

### 踩坑记录
1. 抖音反爬：需要动态 IP
2. AI 分析超时：加了缓存机制
