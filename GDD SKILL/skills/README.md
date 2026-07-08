# Skill 知识库

`skills/` 存放**可复用规范与框架知识**，供 Agent 读取、编译脚本引用。  
**不是**可直接复制粘贴的提示词（提示词在 `prompts/`）。  
**不是**具体功能的策划案（交付物在 `产出/`；对照样例在 `案例/`）。

---

## 目录命名一览（先看这个）

```text
skills/
├── pipeline/          ★ 文档管线 P0~P6 格式规范（原 gdd/）— 每个功能必用
├── frameworks/        ★ L1 玩法框架模板（原 design/）— workflow 按需选
├── tech/              L0 技术横切（配置表、分辨率、契约…）
├── ux/                L0 体验横切（交互反馈…）
├── _template/         新建 frameworks 时复制
├── _backlog/          待建 Skill 构想（未晋升前禁止当正式 Skill）
├── README.md          ← 本文件
└── GDD-SKILL-更新规范.md
```

| 文件夹 | 一句话 | 配对 Prompt | 超级鸡马 | 竞技场 |
|--------|--------|-------------|----------|--------|
| **`pipeline/`** | 怎么写 01~03、怎么 compile | `prompts/P0~P6/` | ✅ 必用 | ✅ 必用 |
| **`frameworks/`** | 这类玩法通用的业务骨架 | P2/P3 里 `@ frameworks/…` | ❌ 未选 | ✅ tournament_bracket |
| **`tech/`、`ux/`** | 全项目横切标准 | P2-DS、P3-3、P6 | 部分勾选 | 部分勾选 |

> **易混点**：`pipeline` = 文档工序；`frameworks` = 玩法类型。二者都不是「某个功能的策划正文」。

详细说明：[pipeline/README.md](pipeline/README.md) · [frameworks/README.md](frameworks/README.md)

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
- 未经确认修改 L1 框架 Skill（`skills/frameworks/*`）

**Prompt 与 Skill 分工**

- **Prompt** = 告诉 AI「按什么格式、写到哪里、@ 什么输入」
- **Skill** = 告诉 AI「这类系统的抽象模式是什么」（不含项目名词）
- **01 原始策划案** = 业务内容的唯一来源（经 @ 引用）

---

## 三层 + 管线模型

```text
pipeline/（文档怎么写 — 与玩法无关）
    │
    ├── 引用 tech/*、ux/*（L0 横切）
    └── 引用 frameworks/*（L1，可选）
              │
              ▼ 实例化
    产出/{功能名}/ + workflows/*.json（L2）
```

| 读什么 | 何时读 |
|--------|--------|
| `skills/frameworks/{skill_id}/` | workflow 选中、且拆解**同类玩法** |
| `产出/{功能名}/02~03` | 看**该功能**如何实例化 |
| `workflows/{项目}.workflow.json` | 看**该项目** skill_configs |

> L2 实例路径因项目而异，**不应**写死在 Skill 正文中。

---

## 已内置 Skill

| ID | 层级 | 目录 | 说明 |
|----|------|------|------|
| `resolution_standard` | L0 | [tech/resolution_standard](tech/resolution_standard/) | 1080×2340 fit、安全区 |
| `config_table` | L0 | [tech/config_table](tech/config_table/) | 配置表单表结构、策划→Agent→程序三阶段 |
| `configurable_rules` | L0 | [tech/configurable_rules](tech/configurable_rules/) | 可配置规则：R-xx + Const/表、Q-D/Q-R 分轨 |
| `implementation_data` | L0 | [tech/implementation_data](tech/implementation_data/) | 实现数据契约：变量追溯、契约审计、就绪矩阵 |
| `interaction_feedback` | L0 | [ux/interaction_feedback](ux/interaction_feedback/) | 按钮三态、Toast、防连点 |
| `tournament_bracket` | L1 | [frameworks/tournament_bracket](frameworks/tournament_bracket/) | 单败 Bracket 通用模式 |
| `pipeline/p0~p6-*` | 管线 | [pipeline/](pipeline/) | 各阶段文档格式规范 |

---

## 新建 L1 框架

1. 复制 `_template/` 到 `frameworks/{skill_id}/`
2. 填写 `meta.md`（含 `config_schema`）与 `design/ux/tech/qa/feature.md`
3. 在 `frameworks/{skill_id}/README.md` 写清「框架覆盖什么 / 不覆盖什么」
4. **须维护者确认**后，才加入 `workflows/*.json` 的 `selected_skills`

**原则**：L1 只写模式与槽位；具体数值、文案、业务名词一律放在 L2 `产出/`。

---

## Skill 代做与演进

- 待建构想：[_backlog/](_backlog/README.md)
- 从真项目反哺：[GDD-SKILL-更新规范.md](GDD-SKILL-更新规范.md)
- 进度表：[_backlog/维度Skill路线图.md](_backlog/维度Skill路线图.md)
