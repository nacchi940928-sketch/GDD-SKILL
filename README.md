# GDD SKILL

策划案（01）→ **02 需求拆解** + **03 功能点梳理** → 编译交付。

**可移植包**：[GDD SKILL/skills/README.md](GDD%20SKILL/skills/README.md) — 只复制 `skills/` 文件夹到其他项目。

| 我要… | 打开 |
|--------|------|
| 怎么跑 / 复制到新项目 | [GDD SKILL/skills/README.md](GDD%20SKILL/skills/README.md) |
| 日常 @ 引用 | [GDD SKILL/skills/使用指导.md](GDD%20SKILL/skills/使用指导.md) |
| Prompt 清单 | [GDD SKILL/skills/prompts/规格交付库.md](GDD%20SKILL/skills/prompts/规格交付库.md) |

```bash
cd "GDD SKILL"
powershell -ExecutionPolicy Bypass -File skills/install-cursor.ps1
python skills/tools/compile.py 产出/{功能名} --workflow skills/workflows/{项目}.workflow.json
```
