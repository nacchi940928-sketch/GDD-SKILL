# GDD SKILL

策划案（01）→ **02 需求拆解** + **03 功能点梳理** → 编译交付程序/AI 管线。

所有 Prompt、模板、产出在 [`GDD SKILL/`](GDD%20SKILL/) 子目录。

---

## 只看这两个

| 我要… | 打开 |
|--------|------|
| **怎么跑**（路径、`@`、新建、对话示例） | **[GDD SKILL/使用指导.md](GDD%20SKILL/使用指导.md)** |
| **复制哪个 Prompt**（顺序、门禁、编号） | **[GDD SKILL/prompts/规格交付库.md](GDD%20SKILL/prompts/规格交付库.md)** |

Cursor 一键编排：[`.cursor/skills/gdd-decompose/`](.cursor/skills/gdd-decompose/SKILL.md)

```bash
cd "GDD SKILL"
python tools/compile.py 产出/超级鸡马 --workflow workflows/chickenhorse.workflow.json
```

更多索引（模板、Skill、案例、维护者文档）→ [GDD SKILL/docs/文档索引.md](GDD%20SKILL/docs/文档索引.md)
