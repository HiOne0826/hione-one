---
title: 抖音数据 AI 分析
description: MediaCrawler + FastAPI + OpenClaw AI 分析，输入抖音链接，输出 8 个维度的 AI 分析
status: 进行中
techStack:
  - FastAPI
  - 火山引擎
  - OpenClaw
  - MediaCrawler
image: /images/projects/douyin-ai.png
demoUrl: https://demo.hione.one
repoUrl: https://github.com/ericgao/douyin-ai
publishDate: 2026-03-01
updatedDate: 2026-03-05
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
