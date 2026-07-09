# GDD SKILL 子项目

> 日常只看 **[使用指导.md](使用指导.md)** 和 **[prompts/规格交付库.md](prompts/规格交付库.md)**，不必在多个 README 间跳转。

---

## 目录

```text
prompts/          可执行 Prompt（立项探索～开发管线）
skills/           pipeline 规范 · L0/L1 框架
templates/        00~04 空模板
产出/{功能名}/     ★ 真实交付（01~04 + 开发文档 + logs）
案例/             对照样例（竞技场高级赛）
workflows/        feature_root 配置
tools/            compile.py 等
```

## 常用

| 入口 | 说明 |
|------|------|
| [使用指导.md](使用指导.md) | 路径、`@`、新建、踩坑 |
| [prompts/规格交付库.md](prompts/规格交付库.md) | Prompt 清单与门禁 |
| [`.cursor/skills/gdd-decompose/`](../.cursor/skills/gdd-decompose/SKILL.md) | Cursor 一键拆解 |
| [产出/超级鸡马/](产出/超级鸡马/) | 当前真产出 |
| [案例/竞技场高级赛/](案例/竞技场高级赛/) | 对照样例 |

```bash
python tools/compile.py 产出/超级鸡马 --workflow workflows/chickenhorse.workflow.json
```

全量文档地图（维护者用）→ [docs/文档索引.md](docs/文档索引.md)
