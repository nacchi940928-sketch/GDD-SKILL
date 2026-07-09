# GDD SKILL 可移植包

> **只复制本 `skills/` 文件夹**到其他项目即可（另建 `产出/`、安装 Cursor 入口，见下）。

## 目录结构

```text
skills/                          ← ★ 复制整棵此目录
├── README.md                    ← 本文件
├── 结构说明.md                  全结构说明
├── 使用指导.md                  日常操作
├── gdd-decompose/               Cursor 斜杠命令 · 交付轨
│   ├── SKILL.md                 ⭐ Agent 主指令
│   ├── reference.md             管线步骤表
│   ├── examples.md              对话示例
│   ├── scripts/compile.py
│   └── README.md
├── gdd-norm-feedback/           Cursor 斜杠命令 · 演进轨
├── prompts/                     各阶段 Prompt 正文
├── pipeline/                    格式铁律（p0～p7）
├── templates/                   01～04 模板
├── tools/                       compile.py 等
├── workflows/                   项目 JSON 配置
├── frameworks/                  L1 玩法框架
├── tech/、ux/                   L0 横切
└── GDD-SKILL-更新规范.md
```

## 在新项目安装（3 步）

### 1. 复制 skills 包

```text
你的项目/
├── skills/          ← 粘贴本目录
└── 产出/            ← 新建空目录（管线写入此处）
```

### 2. 注册 Cursor 斜杠命令

将编排 Skill **复制**到工作区 `.cursor/skills/`（Cursor 只认此路径）：

```powershell
# 在项目根执行（skills 的父目录）
New-Item -ItemType Directory -Force -Path ".cursor\skills"
Copy-Item -Recurse -Force "skills\gdd-decompose" ".cursor\skills\"
Copy-Item -Recurse -Force "skills\gdd-norm-feedback" ".cursor\skills\"
```

或运行：`powershell -File skills/install-cursor.ps1`

### 3. 用 Cursor 打开项目根

工作区根 = **`skills/` 的父目录**（与 `产出/` 同级），不是 `skills/` 本身。

## 路径约定

| 名称 | 路径 | 说明 |
|------|------|------|
| **SKILLS_ROOT** | `skills/` | 本包根；`prompts/`、`pipeline/` 相对此目录 |
| **WORKSPACE_ROOT** | `skills/../` | `产出/`、`源文档/` 在此 |
| **feature_root** | `产出/{功能名}` | 相对 WORKSPACE_ROOT |

## 一键拆解

```text
/gdd-decompose
@源文档/{策划案}.docx
工作包：{功能名}
feature_root=产出/{功能名}
workflow=skills/workflows/{项目}.workflow.json
请从 docx 全流程跑到 04，全流程不要停。
```

## 编译

```bash
python skills/tools/compile.py 产出/{功能名} --workflow skills/workflows/{项目}.workflow.json
```

## 快速入口

| 文档 | 用途 |
|------|------|
| [使用指导.md](使用指导.md) | @ 引用、新建功能 |
| [prompts/规格交付库.md](prompts/规格交付库.md) | Prompt 清单 |
| [结构说明.md](结构说明.md) | 详细结构 |
| [gdd-decompose/SKILL.md](gdd-decompose/SKILL.md) | 交付轨编排 |
