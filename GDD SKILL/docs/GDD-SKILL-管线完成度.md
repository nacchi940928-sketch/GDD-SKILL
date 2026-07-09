# GDD SKILL — 管线规范完成度总结

> **统计日期**：2026-07-08  
> **范围**：`GDD SKILL/` 子项目，按 Part 2 规格交付管线（立项探索～开发管线）及三层 Skill 架构评估。  
> **L2 状态（2026-07-09）**：`产出/`、`案例/` 已清空为空白工程；下表 L2 行仅作历史参考。  
> **真源规范**：[prompts/规格交付库.md](../prompts/规格交付库.md) · [使用指导.md](../使用指导.md)

---

## 1. 总览

| 层级 | 完成度 | 说明 |
|------|--------|------|
| **管线规范与 Prompt 库** | 🟢 **~90%** | 立项探索～开发管线 提示词 + pipeline Skill 齐全；六段式、编号、门禁已文档化 |
| **工具链** | 🟢 **~90%** | `compile.py` 单文档编译；缺路径校验、CI |
| **目录与交付约定** | 🟢 **~100%** | `02-03…/` + `开发文档/` 已统一；legacy 目录与 `outputs/` 已清理 |
| **L0 横切 Skill** | 🟡 **~50%** | 5 个已启用；多数 需求拆解 维度 Skill 仍待提炼 |
| **L1 玩法框架** | 🟡 **~20%** | 仅 `tournament_bracket` |
| **L2 实例** | ⬜ **无** | 产出/案例 已清空；待新建功能验证管线 |

**一句话**：**管线骨架与 Prompt 库已就绪**；**待第一个 L2 项目跑通验证**。

---

## 2. 当前目录约定（已落地）

```text
产出/{功能名}/
├── 01-原始策划案/{功能名}/
├── 02-03需求拆解与功能点梳理/    ← {spec_root}：02 + 03 单文档
│   ├── 02-需求拆解.md
│   └── 03-功能点梳理.md
├── 04-待策划补充/{功能名}/
├── 开发文档/                     ← compile 三包（勿手改）
├── logs/
├── 补充与修改看板.md
└── README.md

skills/
├── pipeline/      ← 文档管线 立项探索～开发管线（原 gdd/）
├── frameworks/    ← L1 玩法框架（原 design/）
├── tech/ · ux/    ← L0 横切
├── _template/ · _backlog/

prompts/立项探索～开发管线/     ← 可复制的执行提示词
templates/         ← 空骨架（见 templates/README.md）
```

占位符：`{feature_root}` = `产出/{功能名}` · `{spec_root}` = `{feature_root}/02-03需求拆解与功能点梳理`

---

## 3. 管线分阶段完成度

### 图例

| 符号 | 含义 |
|------|------|
| ✅ | 规范 + 工具 + 至少一个 L2 实例已验证 |
| 🟡 | 规范已有，L2 部分完成或待回填 |
| ⬜ | 仅有规划/骨架，未落地或未跑通 |
| — | 可选阶段，本项目未走 |

### 3.1 阶段矩阵（规范层）

| 阶段 | Prompt | pipeline Skill | 规范完成 |
|------|--------|----------------|----------|
| 立项探索 | 4 ✅ | p0 ✅ | ✅ 可选 |
| 原始策划案 | 2 ✅ | p1 ✅ | ✅ |
| 需求拆解 | 9 ✅ | p2 ✅ | ✅ |
| 功能点梳理 | 6 ✅ | p3 ✅ | ✅ |
| 待策划补充 | 2 ✅ | p4 ✅ | ✅ |
| 编译验收 | 4 ✅ | p5 ✅ | ✅ |
| 开发管线 | 3 ✅ | p6 🟡 | 🟡 |

**L2 验证**：当前无实例；新建 `产出/{功能名}/` 后在本节补充项目列。

---

## 4. Skills 完成度

### 4.1 `skills/pipeline/`（文档管线 · 每功能必用）

| Skill | 状态 | 说明 |
|-------|------|------|
| p0-discovery-立项探索 ~ p6-pipeline-开发管线 | ✅ 7 个 SKILL.md | 与 prompts 一一对应 |
| pipeline/README.md | ✅ | 与 frameworks 区分说明 |

### 4.2 `skills/frameworks/`（L1 · workflow 按需）

| skill_id | 状态 | 实例 |
|----------|------|------|
| tournament_bracket | ✅ 完整 meta/design/ux/tech/qa/feature | workflow 按需实例化 |
| （其他玩法） | ⬜ | 待从 L2 抽象 |

### 4.3 `skills/tech/` · `skills/ux/`（L0 横切）

| skill_id | 状态 | 用途 |
|----------|------|------|
| config_table | ✅ | 需求拆解·数据源、功能点梳理·字段映射 配置表格式 |
| configurable_rules | ✅ | Const/表 + Q-D/Q-R 分轨 |
| implementation_data | ✅ | 03 附录 D 契约/专项审计 |
| resolution_standard | ✅ | workflow 可选 |
| interaction_feedback | ✅ | workflow 可选 |
| config_table_impact | 📝 代做 | `_backlog/`，无正式 Skill |

### 4.4 维度 Skill 路线图（需求拆解/功能点梳理 子域）

见 [skills/_backlog/维度Skill路线图.md](../skills/_backlog/维度Skill路线图.md)。

| 类别 | 已启用 | 待提炼 |
|------|--------|--------|
| 需求拆解 维度 | 3（config_table、configurable_rules、implementation_data） | 规则/状态机/协议/边界/校验/红点/UI/验收 等 9+ |
| 功能点梳理 子域 | p3-feature-spec-功能点梳理（🟡 总规范） | 功能点五块、验收场景、Feature 映射等独立 Skill |

> 路线图内部分 L2 引用路径仍为旧版（`02-…/多文件夹`、`skills/gdd/`），**文档待同步**，不影响真源路径。

---

## 5. Prompts · Templates · 文档

### 5.1 Prompts（`prompts/`）

| 项 | 状态 |
|----|------|
| 立项探索～开发管线 正文文件 | ✅ 共 25+ 个提示词 |
| 规格交付库.md | ✅ 编号、门禁、索引 |
| Part2-公共头.md | ✅ 含 spec_root / 开发文档 |
| 六段式结构 | ✅ 原始策划案～开发管线 已统一 |
| P7 Bug 回流 | ⬜ 仅在 PromptMerge 规划提及，无 prompts/ |

### 5.2 Templates（`templates/`）

| 项 | 状态 |
|----|------|
| templates/README.md | ✅ |
| 02 八维度扁平模板 | ✅ `规则.md` … `UI交互.md` |
| 02-需求拆解-写作规范.md | ✅ |
| logs/模板.log.md | ✅ |

### 5.3 治理文档

| 文档 | 状态 |
|------|------|
| 使用指导.md | ✅ 已对齐新目录 |
| 策划协作附录 | ✅ 已并入 `docs/附录-策划协作.md`（原策划工作流已删除） |
| skills/README.md | ✅ pipeline / frameworks 命名 |
| GDD-SKILL-更新规范.md | ✅ |
| docs/PromptMerge规划.md | 🟡 架构参考；部分路径/阶段描述过时 |

---

## 6. 工具链

| 工具 | 状态 | 说明 |
|------|------|------|
| compile.py | ✅ | 读 `{spec_root}/02+03` → `{feature_root}/开发文档/`（仅单文档） |
| skill_loader.py + meta_parser | ✅ | workflow 编译、Skill 索引 |
| docx_extract.py | ✅ | docx 表提取 |
| 路径校验脚本 | ⬜ | 未建（如检查 Prompt 与 spec_root 一致性） |
| CI / pre-commit | ⬜ | 无 |

---

## 7. L2 实例详情

**当前无 L2 实例**（`产出/`、`案例/` 已清空，2026-07-09）。新建功能后在本节补充进度。

---

## 8. 已完成内容清单（管线骨架）

1. **完整 Part 2 Prompt 库**（立项探索～开发管线）与 **pipeline Skill**
2. **单文档交付模型**：`{spec_root}/02+03`，compile → `{feature_root}/开发文档/`
3. **编号体系**与 02/03 职能分轨
4. **L0 维度 Skill**：config_table、configurable_rules、implementation_data 等
5. **L1 框架**：tournament_bracket（与具体案例目录解耦）
6. **执行日志规范** + 04 回填工作流约定

---

## 9. 未完成 / 待办清单

| 项 | 优先级 | 说明 |
|----|--------|------|
| 第一个 L2 项目跑通验证 | 高 | 新建 `产出/{功能名}/` 走 P1～P5 |
| docx_extract XML 顺序提取 | 中 | 工具与规范对齐 |
| compile 后路径自检 / CI | 中 | 无 L2 时暂无回归样例 |
| L1 新框架（按需） | 低 | 见 frameworks/_backlog |

---

## 10. 推荐推进顺序

```text
1. 使用指导 §5 新建 产出/{功能名}/
2. 复制 workflows/_template.workflow.json
3. P1～P3 跑通 → P4 回填 → compile → logs
4. 维护者：按 GDD-SKILL-更新规范 反哺 Skill
```

---

## 11. 相关索引

| 文档 | 路径 |
|------|------|
| 规格交付主库 | [prompts/规格交付库.md](../prompts/规格交付库.md) |
| 使用与路径 | [使用指导.md](../使用指导.md) |
| Skill 总览 | [skills/README.md](../skills/README.md) |
| Skill 演进规范 | [skills/GDD-SKILL-更新规范.md](../skills/GDD-SKILL-更新规范.md) |

---

**文档维护**：L2 里程碑变更时更新 §7。
