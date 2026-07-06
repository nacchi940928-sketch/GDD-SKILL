# P2 需求拆解 — Prompt 库

> **Part 2 核心阶段之一**：将 01 原始策划案拆解为 8 维度、编号化、可评审的 02 规格。  
> 完整规范：[规格交付库.md](../规格交付库.md) · Skill：[p2-decompose](../../skills/gdd/p2-decompose/SKILL.md)

---

## 执行顺序（固定）

```text
P2-DS（必须先做，登记 P-xx）
  → P2-R → P2-EX → P2-SM → P2-UI → P2-RD → P2-V → P2-T
```

| 顺序 | 原因 |
|------|------|
| DS 第一 | 全部 P-xx 字段须先登记 |
| R 第二 | 业务规则是其他维度基础 |
| EX 第三 | 边界依赖规则 |
| SM 第四 | 状态机依赖规则+字段 |
| UI 第五 | 界面依赖阶段/身份规则 |
| RD/V | 依赖 UI 入口与写操作规则 |
| T 最后 | 验收覆盖全部 R-/边界/状态 |

---

## 占位符

| 占位符 | 填写说明 |
|--------|----------|
| `{功能名}` | 与 `产出/{功能名}` 目录名一致 |
| `{feature_root}` | `产出/{功能名}` |
| `{功能缩写}` | 大写英文缩写 |
| `{skill_id}` | workflow 中 L1 框架 id |
| `{项目}` | workflow 文件名（不含 `.json`） |

---

## 八维度 Prompt 清单

| ID | 文件 | 产出路径 | 编号 |
|----|------|----------|------|
| P2-DS | [P2-DS-数据源.md](P2-DS-数据源.md) | `{feature_root}/02-…/数据源/` | P-xx |
| P2-R | [P2-R-规则.md](P2-R-规则.md) | `{feature_root}/02-…/规则/` | R- |
| P2-EX | [P2-EX-边界条件.md](P2-EX-边界条件.md) | `{feature_root}/02-…/边界条件/` | EX/PRE/LIM |
| P2-SM | [P2-SM-状态机.md](P2-SM-状态机.md) | `{feature_root}/02-…/状态机/` | — |
| P2-UI | [P2-UI-UI交互.md](P2-UI-UI交互.md) | `{feature_root}/02-…/UI交互/` | — |
| P2-RD | [P2-RD-红点.md](P2-RD-红点.md) | `{feature_root}/02-…/红点/` | RD- |
| P2-V | [P2-V-校验规则.md](P2-V-校验规则.md) | `{feature_root}/02-…/校验规则/` | V- |
| P2-T | [P2-T-验收标准.md](P2-T-验收标准.md) | `{feature_root}/02-…/验收标准/` | T/B/E |

---

## 统一 @ 引用（P2-DS 完成后）

```
@ {feature_root}/01-原始策划案/{功能名}/原始策划案.md
@ {feature_root}/02-需求拆解/{功能名}/数据源/字段映射索引.md
@ workflows/{项目}.workflow.json
@ skills/design/{skill_id}/design.md（如有 L1）
```

---

## L1 框架继承

若 workflow 选了 `tournament_bracket` 等 L1 Skill：

- 在正文中标注 `继承 R-TB-xxx`，**只写项目 delta**
- 数值从 `skill_configs` 取，不硬编码进 Skill
- L1 已覆盖的通用规则**不重复展开**

L2 delta 写在 `{feature_root}/02-需求拆解/`，**禁止**回写 `skills/`。

---

## 进入 P3 的门禁

- [ ] 八维度文件夹均有实质内容
- [ ] `字段映射索引.md` 覆盖 01 全部数据项
- [ ] 核心 R- 均有伪代码 + P-xx 依赖
- [ ] 每条标注 `来源：01 §x.x`
