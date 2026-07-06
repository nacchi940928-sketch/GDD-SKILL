# GDD SKILL 子项目

策划工作流主内容目录。仓库根 [README.md](../README.md) 为项目组评审入口。

## 快速导航

| 文档 | 用途 |
|------|------|
| **[使用指导.md](使用指导.md)** | **路径规范、@ 引用、新建功能步骤** |
| **[prompts/规格交付库.md](prompts/规格交付库.md)** | **Part 2 规格交付 Prompt 库（工作重点）** |
| [产出/README.md](产出/README.md) | **管线交付物**（01~04） |
| [案例/README.md](案例/README.md) | **对照样例**（非日常产出） |

## 目录一览

```text
prompts/          提示词 P0~P6
skills/           规范与框架（Agent 读）
源文档/             仅原始策划 docx
config/             全项目表关联 JSON 模板
templates/        空模板
产出/{功能名}/     ★ 管线交付物（02/03 单文档 + 01/04 + logs）
案例/             对照样例（如竞技场高级赛）
outputs/          compile 三包（勿手改）
workflows/        feature_root → 产出/
tools/            compile.py 等
```

## 三层基底

| 层级 | 位置 | 内容 |
|------|------|------|
| L0 | `skills/tech/*`、`skills/ux/*` | 分辨率、交互反馈 |
| L1 | `skills/design/*` | 框架 Skill |
| L2 | **`产出/{功能}/`** + `workflows/*.json` | 项目交付实例 |

## 常用命令

```bash
# 真实产出
python tools/compile.py 产出/超级鸡马 --workflow workflows/chickenhorse.workflow.json

# 对照样例
python tools/compile.py 案例/竞技场高级赛 --workflow workflows/arena.workflow.json
```

## 当前产出

[产出/超级鸡马/](产出/超级鸡马/) — 《超级鸡马》docx 规格化交付。

## 对照样例

[案例/竞技场高级赛/](案例/竞技场高级赛/) — 继承 `tournament_bracket` 的 L2 样例。
