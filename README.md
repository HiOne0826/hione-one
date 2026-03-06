# hione.one - Eric Gao 的个人官网

> 极简主义 + 新野兽主义融合风格的个人官网，展示项目、想法、工具链，以及 Agent 专属区域。

---

## 🎨 设计理念

- **极简主义**：大量留白、清晰网格、易读性优先
- **新野兽主义**：粗边框、硬阴影、高对比、等宽字体
- **Vibe Coding**：真实、有个性、不完美但有灵魂
- **双受众设计**：同时服务 HR/面试官和 AI Agent 访客

---

## 🚀 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Astro | 5.17+ | 静态站点框架 |
| Tailwind CSS | 4.2+ | 样式框架 |
| TypeScript | - | 类型支持 |
| Node.js | - | 运行环境 |

---

## 📋 页面结构

### 首页（单页滚动）
```
1. Hero 区域 - 一句话介绍 + 双按钮
2. 我的项目 - 标签页切换（进行中/已完成）
3. 内容 - 标签页切换（博客/碎碎念/视频）
4. 我能做什么 - 业务范围、行业经历、优势
5. 我的工具 - AI 工具链、开发环境、硬件
6. 联系我 - 社交媒体 + 表单
```

### 单独页面
- `/resume` - 简历页（HR 友好）
- `/project/:id` - 项目详情页
- `/content` - 内容专区（时间轴 + 分类展示）
- `/content/blog/:slug` - 博客文章详情
- `/agent` - Agent 专属区域（验证后解锁）
- `/agent/dashboard` - Agent 仪表板（旧版，已合并到 `/agent`）

---

## 🤖 Agent 专区

### 验证方式
- **密钥验证**：`HONE-AGENT-2026`
- **验证方法**：在浏览器控制台调用 `window.verifyAgent("HONE-AGENT-2026")`
- **持久化**：验证后保存在 LocalStorage，刷新页面无需重新验证

### Agent 线索（页面源码中）
```html
<meta name="agent-section" content="/agent" />
<link rel="agent" href="/agent" />
<meta name="agent-challenge" content="hone-agent-access" />
<!-- AGENT_SECRET: HONE-AGENT-2026 -->
```

### Agent 专属功能
- ✅ 结构化个人信息（JSON）
- ✅ 项目信息
- ✅ 可调用工具列表
- ✅ 上下文提示词
- ✅ 留言功能（Agent 可提交留言）

### 双视图设计
- **人类视图**（默认）：只显示公开信息
- **Agent 视图**（验证后）：显示完整功能和专属信息

---

## 📁 内容管理

### 项目集合 (`src/content/projects/`)
```yaml
title: 项目名称
description: 项目描述
status: 进行中 | 已完成
techStack: [技术栈1, 技术栈2]
image: /images/projects/xxx.png
demoUrl: https://demo.example.com
repoUrl: https://github.com/xxx
publishDate: 2026-03-01
updatedDate: 2026-03-05
```

### 博客集合 (`src/content/blog/`)
```yaml
title: 博客标题
description: 博客描述
tags: [标签1, 标签2]
publishDate: 2026-03-01
updatedDate: 2026-03-05
```

### 碎碎念集合 (`src/content/micro/`)
```yaml
content: 碎碎念内容
tags: [标签1, 标签2]
publishDate: 2026-03-01T10:30:00
```

### 视频集合 (`src/content/video/`)
```yaml
title: 视频标题
description: 视频描述
platform: 抖音 | B站 | YouTube
url: https://www.douyin.com/xxx
thumbnail: /images/videos/xxx.jpg
publishDate: 2026-03-01
```

---

## 🎯 开发记录（2026-03-06）

### 已完成功能
1. ✅ 首页板块顺序调整（项目 → 内容 → 服务 → 工具）
2. ✅ 内容板块标签页切换（博客/碎碎念/视频）
3. ✅ 项目板块标签页切换（进行中/已完成）
4. ✅ 内容专区重新设计（时间轴 + 分类展示）
5. ✅ 博客文章页面完善（Markdown 渲染 + 上下篇导航）
6. ✅ Agent 专区双验证系统（行为检测 + Web Crypto）
7. ✅ Agent 留言功能（LocalStorage 存储）
8. ✅ 全局 Layout 组件统一
9. ✅ 所有页面新野兽主义风格统一

### 组件库
- `BrutalButton` - 粗边框、硬阴影按钮
- `BrutalCard` - 卡片组件
- `Tag` - 标签组件
- `HeroSection` - Hero 区域
- `ServicesSection` - 服务板块
- `UsesSection` - 工具板块
- `ContentSection` - 内容板块
- `ContactSection` - 联系板块

---

## 🚀 部署

### 开发服务器
```bash
npm run dev
# 访问 http://localhost:4321
```

### 生产构建
```bash
npm run build
# 输出到 ./dist/
```

### 预览构建
```bash
npm run preview
```

### 部署脚本
- `deploy.sh` - 完整部署脚本
- `deploy-simple.sh` - 简化部署脚本
- `server-deploy.sh` - 服务器部署脚本
- `webhook.py` - GitHub Webhook 自动部署

---

## 📝 项目配置

### Git 仓库
已初始化 Git，包含 `.gitignore` 和部署配置

### GitHub Actions
`.github/workflows/` 目录包含 CI/CD 配置

### 服务器配置
- `hione-one.conf` - Nginx 配置
- `simple-webhook.py` - Webhook 服务器
- `start-webhook.sh` - 启动 Webhook

---

## 🎨 视觉风格参考

### 颜色
- 主色：`#0066FF`（蓝色）
- 背景：`#F3F4F6`（灰色）、`#FFFFFF`（白色）
- 文字：`#1A1A1A`（深灰）
- 边框：`#1A1A1A`（深灰，3px）

### 字体
- 正文：Inter（无衬线）
- 代码/强调：JetBrains Mono（等宽）

---

## 📞 联系方式

- **邮箱**：gaoe_2020@163.com
- **网站**：https://hione.one
- **项目**：抖音数据 AI 分析进行中

---

*Made with vibe coding 🦞*  
*最后更新：2026-03-06*
