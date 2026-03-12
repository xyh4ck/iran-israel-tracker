# 伊朗以色列冲突实时追踪 | Iran-Israel Conflict Tracker

[![Live](https://img.shields.io/badge/status-live-red)](https://xyh4ck.github.io/iran-israel-tracker/)
[![Auto-refresh](https://img.shields.io/badge/update-5%20min-blue)](https://xyh4ck.github.io/iran-israel-tracker/)
[![Dynamic](https://img.shields.io/badge/data-json-green)](https://xyh4ck.github.io/iran-israel-tracker/)

实时追踪2026年伊朗以色列冲突的最新动态，数据驱动架构，支持自动更新。

## ✨ 特性

- ⏱️ **自动刷新**: 每5分钟自动获取最新数据
- 📊 **动态数据**: 从 JSON 文件加载，支持自动化更新
- 🤖 **自动化就绪**: GitHub Actions 可自动抓取新闻
- 📅 **智能日期**: 自动显示最新日期的事件
- 🎨 **精美界面**: 深色主题，响应式设计
- 🔍 **即时筛选**: 点击日期按钮即时筛选事件

## 📊 当前数据（截至2026年3月12日）

- ⚔️ **冲突状态**: 进行中（第13天）
- 🚀 **导弹发射**: 500+
- 🛸 **无人机攻击**: 2000+
- 😔 **平民死亡**: 1800+
- 📍 **波及国家**: 9个中东国家

## 🚀 快速开始

### 在线访问

访问 [GitHub Pages](https://xyh4ck.github.io/iran-israel-tracker/) 查看实时追踪页面。

### 本地部署

1. 克隆仓库
```bash
git clone https://github.com/xyh4ck/iran-israel-tracker.git
cd iran-israel-tracker
```

2. 用浏览器打开 `index.html`

### 添加新事件

编辑 `data/events.json`，添加新事件：

```json
{
  "id": "2026-03-13-event-id",
  "date": "2026-03-13",
  "time": "3月13日",
  "title": "事件标题",
  "details": "详细描述...",
  "tags": ["标签1", "标签2"],
  "critical": false,
  "sources": [
    {
      "name": "来源名称",
      "url": "https://..."
    }
  ]
}
```

然后提交：
```bash
git add data/events.json
git commit -m "Add new event"
git push
```

### 使用 GitHub Pages 自动部署

1. Fork 本仓库
2. 进入 Settings > Pages
3. 选择 main 分支作为 Source
4. 点击 Save
5. 几分钟后访问 `https://yourusername.github.io/iran-israel-tracker/`

**注意**: GitHub Pages 部署需要 2-5 分钟，请耐心等待。

## 📚 数据来源

本页面数据来自以下公开来源：

- 📖 维基百科
- 📰 BBC中文
- 🇨🇳 新华网
- 🏛️ 中国外交部
- 🔍 ISW战争研究所
- 📺 CNN
- 📰 美联社

所有数据仅供参考，请以官方消息为准。

## 🛠️ 技术栈

- **前端**: 纯 HTML5 + CSS3 + JavaScript (无框架依赖)
- **数据**: JSON 格式存储 (`data/events.json`)
- **自动化**: Python 脚本 (`scripts/fetch_events.py`)
- **CI/CD**: GitHub Actions (`.github/workflows/auto-update.yml`)
- **响应式设计**: 支持桌面和移动设备

## 📁 项目结构

```
iran-israel-tracker/
├── index.html                    # 主页面(动态版本)
├── index-static-backup.html      # 静态版本备份
├── data/
│   ├── events.json              # 事件数据(主要编辑对象)
│   └── events.schema.json       # 数据结构定义
├── scripts/
│   └── fetch_events.py          # 自动抓取新闻脚本
├── .github/workflows/
│   └── auto-update.yml          # GitHub Actions 配置
└── README.md
```

## 🤖 自动化更新

### GitHub Actions 定时任务

项目配置了 GitHub Actions 工作流，每6小时自动运行：

- **运行时间**: UTC 00:00, 06:00, 12:00, 18:00
- **北京时间**: 08:00, 14:00, 20:00, 02:00

### 新闻来源

自动抓取脚本支持以下新闻源：
- 📰 Al Jazeera
- 📰 BBC News
- 📰 Reuters
- 📰 Associated Press
- 📰 The Guardian

## 📚 数据来源

本页面数据来自以下公开来源：

- 📖 维基百科
- 📰 BBC中文
- 🇨🇳 新华网
- 🏛️ 中国外交部
- 🔍 ISW战争研究所
- 📺 CNN
- 📰 美联社

所有数据仅供参考，请以官方消息为准。

## 📝 更新日志

### 2026-03-12 (v2.0)
- 🎉 **重大升级**: 切换到动态数据架构
- 📊 **数据分离**: 事件数据独立存储为 JSON
- 🤖 **自动化就绪**: 添加 GitHub Actions 工作流
- ⚡ **性能优化**: 客户端即时筛选，无需服务器
- 🔄 **自动刷新**: 缩短到5分钟刷新间隔
- 📅 **智能日期**: 自动选择最新日期显示

### 2026-03-11 (v1.0)
- ✨ 初始版本发布
- 📅 完整时间线（2025年6月 - 2026年3月）
- ⚡ 自动刷新功能（30分钟）
- 📊 实时统计数据

## ⚠️ 免责声明

本页面仅用于信息追踪目的，数据来自公开来源，可能存在延迟或错误。不对数据的准确性或完整性做任何保证。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**愿和平早日降临** 🕊️
