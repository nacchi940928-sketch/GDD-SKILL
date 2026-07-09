# 规范反哺 — Prompt 入口（维护者 · 手动触发）

> **不纳入 gdd-decompose 自动管线。** 仅在维护者**显式要求**时执行，避免 Prompt/Skill 反复被动更新。

## 何时跑

| 场景 | 建议 |
|------|------|
| 某功能 P2/P3 已完成，程序或策划指出规范缺口 | ✅ 跑 |
| 每跑完一次 docx 拆解 | ❌ **不要**自动跑 |
| 准备晋升 `_backlog` → `skills/tech/` | ✅ 先跑报告再人工改库 |

## 入口

| 方式 | 说明 |
|------|------|
| **Cursor** | 另开会话，@ L2 + 说明按 **`gdd-norm-feedback`** 执行 |
| **半自动** | 复制 [生成规范反哺报告.md](生成规范反哺报告.md)「提示词正文」 |

## 产出

```text
产出/{功能名}/规范反哺报告.md    ← 仅建议，不直接改 prompts/skills/
产出/{功能名}/logs/…            ← 可选：维护者改库后另写 log
```

规范 Skill：[skills/pipeline/p7-norm-feedback-规范反哺/SKILL.md](../../skills/pipeline/p7-norm-feedback-规范反哺/SKILL.md)
