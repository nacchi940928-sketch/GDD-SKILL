# Skill 代做记录（Backlog）

> 此处登记**尚未实现、须维护者确认后**才晋升为正式 Skill 的构想。  
> **禁止** Agent 在跑 Part 2 管线时把 `_backlog/` 当作已启用 Skill 写入 `产出/`。

---

## 状态说明

| 状态 | 含义 |
|------|------|
| 📝 代做 | 仅有构想与接口约定，无 SKILL.md 执行体 |
| 🟡 设计中 | 已有目录草案，待评审 |
| ✅ 已晋升 | 迁入 `tech/` / `design/` / `gdd/`，并从本表移除 |

**晋升条件**：维护者确认 + 关联数据（如表关系图）有维护责任人 + 至少一个 Prompt 或工具入口。

---

## 代做清单

| ID | 状态 | 文件 | 摘要 |
|----|------|------|------|
| **config_table_impact** | 📝 代做 | [config_table_impact.md](config_table_impact.md) | 线上改表后，按关联关系检索所有受影响配置表 |

**全量路线图**（含已启用的 config_table）：[维度Skill路线图.md](维度Skill路线图.md)  
**更新流程**：[GDD-SKILL-更新规范.md](../GDD-SKILL-更新规范.md)

---

## 与正式 Skill 的关系

```text
_backlog/（代做记录）
    ↓ 维护者确认
skills/tech|design|gdd/（正式 Skill）
    ↓ 可选
prompts/（执行 Prompt）
    ↓ 可选
tools/（检索脚本）
```

---

## 谁可新增代做记录

- 策划 / 程序 / 维护者提出需求
- 由维护者在本目录新增 `.md`，**不得**直接写进 L1 框架或 Part 2 Prompt 正文
