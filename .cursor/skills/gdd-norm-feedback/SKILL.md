---
name: gdd-norm-feedback
description: >-
  Manual maintainer-only workflow to extract norm feedback from a completed
  L2 feature (02/03/logs) into 规范反哺报告.md. Does NOT modify prompts/ or
  skills/. Use only when the user explicitly asks for 规范反哺, norm feedback,
  or gdd-norm-feedback after a decomposition run — never auto-run after
  gdd-decompose.
---

# GDD 规范反哺（手动 · 维护者）

从已完成的 `产出/{功能名}/` L2 萃取**规范增量建议**，写入 **`规范反哺报告.md`**。

**子项目根目录**：`GDD SKILL/`

## 与 gdd-decompose 的关系

| | gdd-decompose | gdd-norm-feedback（本 Skill） |
|--|---------------|-------------------------------|
| 目的 | docx/01 → 02/03/04 交付 | L2 → 规范演进**建议** |
| 改 `产出/` | ✅ | ✅（仅报告） |
| 改 `prompts/`、`skills/` | ❌ | ❌ |
| 触发 | 用户 @ docx / 跑拆解 | **用户显式要求**规范反哺 |
| 自动衔接 | — | **禁止**拆解完成后自动执行 |

## 启动条件

**仅当**用户明确说出以下之一时才执行：

- 「规范反哺」「生成规范反哺报告」
- 「按 gdd-norm-feedback」
- 「总结这次拆解的规范缺口，但不要改 skill/prompt」

若用户只说「跑拆解 / gdd-decompose」，**不得**进入本 Skill。

## 执行流程

1. **读规范**：`GDD SKILL/skills/pipeline/p7-norm-feedback-规范反哺/SKILL.md`
2. **读 Prompt**：`GDD SKILL/prompts/规范反哺/生成规范反哺报告.md` →「提示词正文」
3. **@ 输入**：该功能的 02、03、logs、看板；`P2-P3-待完善清单.md`、`维度Skill路线图.md`
4. **写入**：`产出/{功能名}/规范反哺报告.md`（可用 `templates/规范反哺报告.md` 结构）
5. **汇报**：报告路径 + §3～§5 摘要 + 提醒「改库须另开会话、走 S1～S7」

## 铁律

1. **禁止**在本会话修改 `GDD SKILL/prompts/`、`GDD SKILL/skills/`
2. **禁止**把 L2 业务正文、数值写入「可抽象」建议
3. 未在 2+ 功能出现的模式 → 报告标「仅 L2」
4. 不替代策划/程序双签

## 快速示例

```text
@GDD SKILL/产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md
@GDD SKILL/产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md
@GDD SKILL/产出/{功能名}/logs/

请按 gdd-norm-feedback 生成规范反哺报告；不要改 prompts 和 skills。
```

## 延伸阅读

| 文件 | 用途 |
|------|------|
| `GDD SKILL/prompts/规范反哺/README.md` | 入口说明 |
| `GDD SKILL/skills/GDD-SKILL-更新规范.md` | 报告确认后改库流程 |
| `GDD SKILL/P2-P3-待完善清单.md` | 对照基线 |
