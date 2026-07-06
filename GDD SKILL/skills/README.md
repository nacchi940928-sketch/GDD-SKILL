# Skill 知识库

`skills/` 存放**可复用规范与框架知识**，供 Agent 读取、编译脚本引用。  
**不是**可直接复制粘贴的提示词（提示词在 `prompts/`）。  
**不是**具体功能的策划案（交付物在 `产出/`；对照样例在 `案例/`）。

---

## 治理原则（必读）

| 层级 | 位置 | 写什么 | 谁可改 |
|------|------|--------|--------|
| **Skill** | `skills/` | 抽象框架、格式铁律、编号体系、config 槽位 | **须维护者确认**，AI 不得擅自写入 L2 业务 |
| **Prompt** | `prompts/` | **文档规范**与执行步骤；只用 `{占位符}` | 维护者迭代 |
| **产出** | `产出/{功能名}/` | 管线交付物（01~04） | 按项目执行 |
| **案例** | `案例/` | 对照样例 | 维护者 |
| **workflow** | `workflows/*.json` | 本项目 skill_configs | 按项目配置 |

**禁止行为**

- 将某次 `产出/` 的正文、规则、P-xx 数值**回写**进 `skills/`
- 在 Prompt 正文中写死具体功能名/业务规则（应用 `{功能名}`、`{功能缩写}`）
- 未经确认修改 L1 框架 Skill（`skills/design/*`）

**Prompt 与 Skill 分工**

- **Prompt** = 告诉 AI「按什么格式、写到哪里、@ 什么输入」
- **Skill** = 告诉 AI「这类系统的抽象模式是什么」（不含项目名词）
- **01 原始策划案** = 业务内容的唯一来源（经 @ 引用）

---

## 三类 Skill

| 类型 | 路径 | 层级 | 说明 |
|------|------|------|------|
| **流程规范** | `gdd/p0~p6-*/SKILL.md` | — | 各阶段**文档格式**铁律（P0~P6） |
| **横切基底** | `tech/*`、`ux/*` | L0 | 分辨率、交互反馈等全项目共用 |
| **系统框架** | `design/*` | L1 | 抽象业务模式 + `config_schema` |

## 框架 vs 实例

```text
L1 框架 Skill（本目录 design/*）
  → 抽象规则编号（如 R-TB-xxx）、config 槽位、extension 挂点
        ↓ 实例化
L2 项目实例（产出/{功能名}/ + workflows/*.json）
  → 填 skill_configs、写业务 delta
```

| 读什么 | 何时读 |
|--------|--------|
| `skills/design/{skill_id}/` | 拆解对应**类型**的功能前，继承框架骨架 |
| `产出/{功能名}/02~03` | 看**该功能**如何实例化框架 |
| `workflows/{项目}.workflow.json` | 看**该项目** skill_configs |

> L2 实例路径因项目而异，**不应**写死在 Skill 正文中。

---

## 已内置 Skill

| ID | 层级 | 目录 | 说明 |
|----|------|------|------|
| `resolution_standard` | L0 | [tech/resolution_standard](tech/resolution_standard/) | 1080×2340 fit、安全区 |
| `interaction_feedback` | L0 | [ux/interaction_feedback](ux/interaction_feedback/) | 按钮三态、Toast、防连点 |
| `tournament_bracket` | L1 框架 | [design/tournament_bracket](design/tournament_bracket/) | 单败 Bracket 通用模式 |
| `gdd/p0-discovery` | 流程 | [gdd/p0-discovery](gdd/p0-discovery/) | P0 立项探索（可选） |
| `gdd/p1~p6-*` | 流程 | [gdd/p1-original-gdd](gdd/p1-original-gdd/) 等 | 各阶段文档格式规范 |

---

## 新建 L1 框架 Skill

1. 复制 `_template/` 到 `design/{skill_id}/`
2. 填写 `meta.md`（含 `config_schema`）与 `design/ux/tech/qa/feature.md`
3. 在 `design/{skill_id}/README.md` 写清「框架覆盖什么 / 不覆盖什么」
4. **须维护者确认**后，才加入 `workflows/*.json` 的 `selected_skills`

**原则**：L1 只写模式与槽位；具体数值、文案、业务名词一律放在 L2 `产出/`。
