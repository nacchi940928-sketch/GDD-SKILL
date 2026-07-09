# GDD SKILL 子项目

> **可移植包**：[skills/README.md](skills/README.md) — 复制 `skills/` 到其他项目即可。  
> 日常操作：[skills/使用指导.md](skills/使用指导.md) · Prompt 索引：[skills/prompts/规格交付库.md](skills/prompts/规格交付库.md)

```text
GDD SKILL/                 ← 本仓库子项目（工作区根）
├── skills/                ★ 唯一需要复制到其他项目的文件夹
├── 产出/                  L2 交付（按功能名）
├── 源文档/                策划 docx（可选）
├── 案例/、程序反馈/、docs/
└── README.md
```

## Cursor 斜杠命令

在本仓库已安装时，入口位于 `.cursor/skills/`（由 `skills/install-cursor.ps1` 生成）。

| 命令 | 源文件 |
|------|--------|
| `/gdd-decompose` | [skills/gdd-decompose/](skills/gdd-decompose/SKILL.md) |
| `/gdd-norm-feedback` | [skills/gdd-norm-feedback/](skills/gdd-norm-feedback/SKILL.md) |

```powershell
powershell -ExecutionPolicy Bypass -File skills/install-cursor.ps1
```
