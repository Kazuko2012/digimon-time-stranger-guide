# 数码宝贝物语 时空异客 · 全进化关系图鉴

《Digimon Story: Time Stranger》475 只数码兽的离线图鉴与谱系图，单个 `index.html` 即可运行，无构建、无依赖、可离线打开。

**在线预览 / Live demo**：https://kazuko2012.github.io/digimon-time-stranger-guide/

An offline field guide and evolution-graph explorer for all 475 Digimon in *Digimon Story: Time Stranger*. Everything runs from a single `index.html` — no build step, no runtime dependencies.

## 多语言 / Languages

右上角可切换 **中文 / English / 日本語**，并记忆上次选择、支持深链 `?lang=en` / `?lang=ja`。
名称、简介与全部界面术语（阶段、属性、类型、性格、条件、技能数值、耐性）均本地化；英文与日文名称、简介取自 [digimon.net](https://digimon.net/) 官方图鉴。


## 预览 / Screenshots

**图鉴卡片视图**：475 只全列表，顶部三组筛选（阶段 / 属性 / 条件）与「标准 / 大图 / 无图」密度切换。

![图鉴卡片视图](docs/screenshot-deck.webp)

**谱系图视图**：以亚古兽为中心，左侧窄栏 475 只可切换，节点左 `↑N` 上溯、右 `+N` 下展，连线为进化关系（无箭头）。  

![谱系图视图](docs/screenshot-lineage.webp)

**详情抽屉**：基础数值、Lv99 数值、耐性与技能、图鉴说明；「可进化为」列表里鼠标悬停任一条目，即显示进化成该形态所需的条件。

![详情抽屉与悬停进化条件](docs/screenshot-drawer.webp)

---

## 功能 / Features

**图鉴卡片 / Card view**

- 475 只数码兽，编号、中文名、日文名、阶段、属性、进化条件
- 图片密度三档：标准 / 大图 / 无图；图片加载方式两种：单图按需 / 精灵图切片
- 阶段、属性、条件三组筛选，可叠加；一键清除全部筛选
- 点击卡片打开详情抽屉：基础数值、Lv99 数值、属性抗性、技能、进化条件、图鉴说明

**谱系图 / Lineage view**

- 以任意一只为中心，逐层展开后代与祖先，可无限上溯
- 节点左侧金色 `↑N` = 还没显示的直系进化源数量，点击往上拉出一层
- 节点右侧蓝色 `+N` = 还没显示的直系下一代数量，点击往下展开一层
- 滚轮缩放（锚定光标位置）、拖拽平移、双击空白适应窗口、`适应窗口` 按钮
- 悬停高亮「该节点 → 中心」的整条链，弱化无关分支
- 折叠逐步展开，展开/收起保持当前视角不跳
- 进化路线查询：任选两只，算出最短进化链与同长度备选路线

**通用 / Common**

- 详情侧栏可左右拖动调宽（双击回到半屏），顶部一键「半屏 / 全屏」，宽度与状态会被记住
- 深浅双主题，选择会被记住
- 搜索支持中文名 / 日文名 / 编号（编号自动三位补零）
- 记忆上次状态：视图、中心、搜索词、筛选组合
- 深链：地址栏自动带 `?view=lineage&d=092&q=暴龙`，可直接分享某个谱系
- 键盘：`/` 聚焦搜索，`← →` 切换相邻编号，`L` 谱系图，`C` 图鉴卡片，`F` 适应窗口，`Esc` 关闭浮层
- 无障碍：焦点环、`aria-label`、`prefers-reduced-motion` 时关闭动效

## 目录结构 / Layout

```
.
├── index.html                # 主页面（唯一运行文件）
├── assets
│   ├── icons/                # 475 张图标，001.webp … 475.webp，112×112
│   └── sprites/              # 精灵图：sprite-56 / 112 / 160.webp
├── data
│   ├── digimon-475.csv       # 词条数据（编号 / 名称 / 阶段 / 属性 / 条件 / 说明）
│   └── digimon-lv99.csv      # 各性格 Lv99 数值
├── scripts
│   └── build_single.py       # 打成一个自包含的离线单文件版
├── docs                     # README 用真实截图
│   ├── screenshot-deck.webp
│   ├── screenshot-lineage.webp
│   └── screenshot-drawer.webp
└── .github/workflows/pages.yml   # 推 main 自动发布到 GitHub Pages
```

## 本地运行 / Run locally

```bash
# 直接双击 index.html 也行；用本地服务更稳妥（避免个别浏览器对本地图片的限制）
python3 -m http.server 8000
# 打开 http://localhost:8000
```

## 打包单文件版 / Build a standalone file

```bash
python3 scripts/build_single.py
# 产出 dist/digimon-time-stranger-guide-single.html（图标 base64 内嵌，约 2.2 MB）
```

单文件版可以拷到 U 盘或直接发给别人，断网、无服务器也能打开。

## 部署 / Deploy

推到 `main` 分支后，GitHub Actions 会把这个仓库发布到 GitHub Pages：

`https://kazuko2012.github.io/digimon-time-stranger-guide/`

仓库设置里把 **Settings → Pages → Source** 选为 **GitHub Actions** 即可。

## 更新说明 / Changelog

### v1.5.0 — 2026-11-21 · 交互与无障碍优化

- **跨语言搜索**：无论当前显示语言，搜索框 / 左栏 / 谱系中心 / 路线下拉都同时匹配中、日、英三种名字（中文模式搜 `Agumon`、英文模式搜「亚古兽」均可）
- **键盘可达**：卡片、左栏条目、谱系节点支持 Tab 聚焦 + Enter/Space 打开；新增 `?` 快捷键帮助浮层
- **Esc 分层关闭**：只关最上层浮层（帮助 > 路线弹窗 > 筛选 > 抽屉），不再一次全关
- **分享链接**：抽屉头部与多选路线面板新增「复制链接」按钮，生成带 `view/d/dr/multi/lang` 的深链；新增 `?dr=编号` 深链直接打开详情
- **搜索体验**：搜索框 / 左栏新增 ✕ 清除按钮；卡片命中词高亮；编号「包含匹配」规则加入提示
- **谱系中心历史**：工具栏 ‹ › 按钮 + `Alt+←/→` 回退 / 前进上一个中心
- **触摸设备**：详情「可进化为」条目改为点按显示 / 再点收起进化条件（桌面悬停不变）
- **性能**：多语言 DOM 观察器只遍历本次变更的子树，不再每次全页扫描

### v1.4.0 — 2026-11-21 · 中 / 英 / 日 三语

- 工具条新增 `中文 | EN | 日本語` 语言切换，记住上次选择；深链支持 `?lang=en` / `?lang=ja`，并兼容参考站的 `?language=en` 写法
- 名称与图鉴简介接入 digimon.net 官方英文 / 日文资料：445 条官方条目 + 30 条游戏特有形态（JM/FM/HM/DM/SM/RM/BM/LM/MM/WM、奥米加兽 Alter 系列、X 抗体等）手工补名，475 只全覆盖
- 全部界面术语本地化：阶段、属性、类型、性格、进化条件、技能数值与效果、耐性表、图例、统计、抽屉、谱系说明、页脚
- 修复切回中文时部分 UI 不还原：改为按节点记录原文，文本、`placeholder`、`title`、`aria-label` 统一回填
- 谱系页筛选反馈：列表计数显示 `128/475`，筛选时滚动条变青绿色，条件变化自动回到顶部
- 修复谱系页顶部搜索框不作用于左侧列表：现在 `?q=9` / 输入关键词会同步筛选左栏，滚动条长度随结果变化

### v1.3.0 — 2026-11-21 · 谱系与详情体验

- 详情侧栏支持左右拖动调宽，双击回到半屏；顶部一键「半屏 / 全屏」，宽度与状态记忆
- 「可进化为」列表悬停即显示进化成该形态所需条件
- 谱系节点 `i` 按钮移到右上角外，与右侧 `+N` 热区拉开，避免误触
- 筛选浮层点选后不再自动关闭，可连续多选
- 谱系页左侧 475 列表自己接管滚轮：搜索框、空白区、条目上滚都能滚动
- 修复谱系页全局滚轮拦截导致详情抽屉无法滚动的问题

### v1.2.0 — 2026-11-20 · 项目化与自动部署

- 重组为标准项目结构，接入 GitHub Pages 自动部署（`main` 推送即发布）
- README 补充图鉴 / 谱系 / 详情抽屉三张真实截图
- 「进化路线」按钮移到「图鉴卡片 / 谱系图」切换左侧

### v1.1.0 — 2026-11-20 · 主题与筛选

- 默认主题跟随系统外观（URL 参数 > 本地记忆 > `prefers-color-scheme` > 深色），可手动切换深浅
- 阶段 / 属性 / 条件三组筛选改完整体验，同项再点一次即取消，支持叠加与一键清除
- 修正 452–467 号图标，中文名统一采用 Arceus-Jia 攻略站译名

### v1.0.0 — 2026-11-20 · 初版

- 475 只数码兽图鉴、进化 / 退化关系、谱系图与进化路线查询，单文件 `index.html` 运行

## 数据来源 / Data

- 数值与图鉴说明整理自日版攻略站 AppMedia 的《时空异客》图鉴页（含 DLC 数码兽）
- 进化条件文本做了中文意译，与游戏内原文可能有措辞差异，以游戏内为准
- 图标来自游戏内素材，仅作同人图鉴用途

## 声明 / Disclaimer

本项目是非商业性质的同人整理作品。《数码宝贝》系列角色、名称、图像版权归 Bandai Namco Entertainment 及各自权利方所有。代码部分以 MIT 许可开源，素材版权不随代码许可转让。若权利方有异议，会立即下线相关内容。

This is a non-commercial fan project. All Digimon characters, names and artwork belong to Bandai Namco Entertainment and their respective owners. The source code is released under MIT; the license does **not** extend to third-party game assets.

## 许可 / License

代码：MIT（见 `LICENSE`）。素材：版权归原权利方，仅限学习交流。
