# 📅 日程日历 PWA

一个 iPhone 友好的 Web 应用，按小时安排每天的工作内容。

## 功能

- ✅ **日/周视图** - 切换查看单日或整周日程
- ✅ **24 小时时间格** - 从 0:00 到 23:00，每小时一个格子
- ✅ **时间冲突检测** - 添加任务时自动检测并提示冲突
- ✅ **任务分类** - 工作/会议/个人/其他，颜色区分
- ✅ **本地存储** - 数据保存在手机本地，无需服务器
- ✅ **离线可用** - PWA 支持，无网络也能用
- ✅ **添加到主屏幕** - 像原生 App 一样使用

## 快速部署

### 方法 1：GitHub Pages（推荐）

1. 在 GitHub 创建新仓库（如 `calendar-app`）
2. 上传 `index.html`、`manifest.json`、`sw.js` 和图标文件
3. 进入仓库 Settings → Pages
4. Source 选择 `main` 分支，保存
5. 几分钟后访问 `https://你的用户名.github.io/calendar-app`

### 方法 2：本地测试

```bash
# Python 3
cd calendar-app
python3 -m http.server 8000

# 然后在浏览器访问 http://localhost:8000
```

### 方法 3：任意静态托管

- Vercel / Netlify / Cloudflare Pages
- 任何支持静态文件的 Web 服务器

## iPhone 安装到主屏幕

1. 用 **Safari** 打开应用网址
2. 点击底部 **分享按钮**（方框带箭头）
3. 选择 **"添加到主屏幕"**
4. 点击右上角 **"添加"**

现在你的主屏幕上会有一个日历 App 图标！

## 生成图标（可选）

如果不想用默认图标，可以自定义：

```bash
# 需要安装 Pillow
pip3 install Pillow

# 运行生成脚本
python3 generate-icons.py
```

## 使用说明

### 添加任务
- 点击任意时间格子，或点击右下角 **+** 按钮
- 填写任务信息，保存即可

### 编辑/删除任务
- 点击已有任务卡片
- 修改信息或删除

### 切换视图
- 点击顶部的 **日** / **周** 按钮

### 导航日期
- 点击 **前一天** / **后一天** 按钮

## 数据存储

- 使用 IndexedDB 存储在本地
- 数据不会上传到任何服务器
- 清除浏览器数据会删除所有日程

## 技术栈

- 纯 HTML/CSS/JavaScript（无框架）
- IndexedDB 本地存储
- PWA + Service Worker 离线支持
- 移动端优化设计

## 文件结构

```
calendar-app/
├── index.html          # 主应用（所有代码在此）
├── manifest.json       # PWA 清单
├── sw.js              # Service Worker
├── icon-192.png       # 图标（需生成）
├── icon-512.png       # 图标（需生成）
├── icon.svg           # SVG 图标源文件
├── generate-icons.py  # 图标生成脚本
└── README.md          # 本文件
```

---

**提示**：首次加载后，应用会缓存到本地，之后可以离线使用。
