# P2 提示词索引

`prompts/P2/` = **可直接复制粘贴到 Agent 的提示词**  
`skills/gdd/p2-decompose/SKILL.md` = **八维度拆解规范**

## 用法

1. 打开对应维度的 `.md` 文件
2. 复制「提示词正文」代码块内的全文
3. 替换 `{功能名}`、`{功能缩写}`、`{skill_id}` 等占位符
4. `@` 引用：01 原始案、L1 框架 Skill（如 `skills/design/tournament_bracket/design.md`）、workflow
5. 发送给 Agent

## 推荐执行顺序

```
P2-DS（数据源，先登记 P-xx）
  → P2-R → P2-EX → P2-SM → P2-UI → P2-RD → P2-V → P2-T
```

## L1 框架继承

若 `workflows/*.json` 的 `selected_skills` 包含 L1 框架（如 `tournament_bracket`）：

| 做法 | 说明 |
|------|------|
| 先读 L1 | `@skills/design/tournament_bracket/design.md` 等 |
| 标注继承 | 02 正文中写 `继承 R-TB-xxx`，仅补充项目 delta |
| 参数来源 | 数值从 `skill_configs` 取，不写进 Skill 文件 |
| 04 减负 | L1 已覆盖的通用规则不进 04 待补充 |

示例：`案例/竞技场高级赛/02-需求拆解/` 继承 `tournament_bracket`，竞猜/商店/签位表为 L2 delta。

## 文件列表

| 提示词 | 输出目录 |
|--------|----------|
| P2-DS-数据源.md | 02-需求拆解/{功能名}/数据源/ |
| P2-R-规则.md | 02-需求拆解/{功能名}/规则/ |
| P2-EX-边界条件.md | 02-需求拆解/{功能名}/边界条件/ |
| P2-SM-状态机.md | 02-需求拆解/{功能名}/状态机/ |
| P2-UI-UI交互.md | 02-需求拆解/{功能名}/UI交互/ |
| P2-RD-红点.md | 02-需求拆解/{功能名}/红点/ |
| P2-V-校验规则.md | 02-需求拆解/{功能名}/校验规则/ |
| P2-T-验收标准.md | 02-需求拆解/{功能名}/验收标准/ |

规范细节见 `skills/gdd/p2-decompose/SKILL.md`。
