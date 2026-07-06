# Skill 知识库

`skills/` 存放**可复用规范与框架知识**，供 Agent 读取、编译脚本引用。  
**不是**可直接复制粘贴的提示词（提示词在 `prompts/`）。

## 三类 Skill

| 类型 | 路径 | 层级 | 说明 |
|------|------|------|------|
| **流程规范** | `gdd/p0~p6-*/SKILL.md` | — | 各阶段格式铁律、检查清单（P0~P6 对应） |
| **横切基底** | `tech/*`、`ux/*` | L0 | 分辨率、交互反馈等全项目共用 |
| **系统框架** | `design/*` | L1 | 抽象业务模式 + `config_schema`，**不含具体项目名词** |

## 框架 vs 实例

```text
L1 框架 Skill（本目录 design/*）
  → 抽象规则编号（如 R-TB-xxx）、config 槽位、extension 挂点
        ↓ 实例化
L2 项目实例（案例/{功能名}/ + workflows/*.json）
  → 填 skill_configs、写业务 delta（竞猜、签位表、周练组等）
```

| 读什么 | 何时读 |
|--------|--------|
| `skills/design/tournament_bracket/` | 拆解任意「单败 Bracket」类功能前，继承 R-TB 骨架 |
| `案例/竞技场高级赛/02~03` | 看竞技场如何把框架实例化 |
| `workflows/arena.workflow.json` | 看本项目 `skill_configs` 取值 |

## 已内置 Skill

| ID | 层级 | 目录 | 说明 |
|----|------|------|------|
| `resolution_standard` | L0 | [tech/resolution_standard](tech/resolution_standard/) | 1080×2340 fit、安全区 |
| `interaction_feedback` | L0 | [ux/interaction_feedback](ux/interaction_feedback/) | 按钮三态、Toast、防连点 |
| `tournament_bracket` | L1 框架 | [design/tournament_bracket](design/tournament_bracket/) | 单败 Bracket 通用模式 |
| `gdd/p0-discovery` | 流程 | [gdd/p0-discovery](gdd/p0-discovery/) | P0 立项探索（策划创作辅助，可选） |
| `gdd/p1-original-gdd` | 流程 | [gdd/p1-original-gdd](gdd/p1-original-gdd/) | P1 原始案规范 |
| `gdd/p2-decompose` | 流程 | [gdd/p2-decompose](gdd/p2-decompose/) | P2 八维度拆解规范 |
| `gdd/p3-feature-spec` | 流程 | [gdd/p3-feature-spec](gdd/p3-feature-spec/) | P3 功能点规范 |
| `gdd/p4-planner-fill` | 流程 | [gdd/p4-planner-fill](gdd/p4-planner-fill/) | P4 待补充与回填 |
| `gdd/p5-compile-verify` | 流程 | [gdd/p5-compile-verify](gdd/p5-compile-verify/) | P5 编译验收 |
| `gdd/p6-pipeline` | 流程 | [gdd/p6-pipeline](gdd/p6-pipeline/) | P6 开发管线 |

## 新建 L1 框架 Skill

1. 复制 `_template/` 到 `design/{skill_id}/`
2. 填写 `meta.md`（含 `config_schema`）与 `design/ux/tech/qa/feature.md`
3. 在 `design/{skill_id}/README.md` 写清「框架覆盖什么 / 不覆盖什么」
4. 在 `workflows/*.json` 的 `selected_skills` 与 `skill_configs` 中引用

**原则**：L1 只写模式与槽位；具体数值、文案、业务名词一律放在 L2 案例。
