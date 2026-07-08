# GDD SKILL — 管线规范完成度总结

> **统计日期**：2026-07-08  
> **范围**：`GDD SKILL/` 子项目，按 Part 2 规格交付管线（P0~P6）及三层 Skill 架构评估。  
> **真源规范**：[prompts/规格交付库.md](../prompts/规格交付库.md) · [使用指导.md](../使用指导.md)

---

## 1. 总览

| 层级 | 完成度 | 说明 |
|------|--------|------|
| **管线规范与 Prompt 库** | 🟢 **~90%** | P0~P6 提示词 + pipeline Skill 齐全；六段式、编号、门禁已文档化 |
| **工具链** | 🟢 **~90%** | `compile.py` 单文档编译；缺路径校验、CI |
| **目录与交付约定** | 🟢 **~100%** | `02-03…/` + `开发文档/` 已统一；legacy 目录与 `outputs/` 已清理 |
| **L0 横切 Skill** | 🟡 **~50%** | 5 个已启用；多数 P2 维度 Skill 仍待提炼 |
| **L1 玩法框架** | 🟡 **~20%** | 仅 `tournament_bracket`；无超级鸡马类框架 |
| **L2 真项目（超级鸡马）** | 🟡 **~70%** | 02/03 主文档完成；04 大量待填；P6 未启动 |
| **L2 对照样例（竞技场）** | 🟢 **~90%** | 全链路曾跑通；仅保留 02-03 单文档 |

**一句话**：**「怎么写、怎么编译」的规范与工具已基本就绪**；**「策划填完、程序开干」在超级鸡马上仍卡在 P4 待办与 P6 未执行**。

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
├── pipeline/      ← 文档管线 P0~P6（原 gdd/）
├── frameworks/    ← L1 玩法框架（原 design/）
├── tech/ · ux/    ← L0 横切
├── _template/ · _backlog/

prompts/P0~P6/     ← 可复制的执行提示词
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

### 3.1 阶段矩阵

| 阶段 | Prompt | pipeline Skill | 规范完成 | 超级鸡马 | 竞技场样例 | 备注 |
|------|--------|----------------|----------|----------|------------|------|
| **P0** 立项 | P0-1~4 ✅ | p0-discovery ✅ | ✅ | — 跳过 | — | 可选；有 docx 直进 P1 |
| **P1** 01 定稿 | P1-1~2 ✅ | p1-original-gdd ✅ | ✅ | ✅ 01 + gap | ✅ | |
| **P2** 02 拆解 | P2×8 ✅ | p2-decompose ✅ | ✅ | ✅ 单文档 | ✅ 单文档 | 八维度扁平模板已整理 |
| **P3** 03 功能点 | P3-1~6 ✅ | p3-feature-spec ✅ | ✅ | ✅ §0~11 + 附录 A~E | ✅ | 附录 D 专项审计已写 |
| **P4** 04 回填 | P4-1~2 ✅ | p4-planner-fill ✅ | ✅ | 🟡 04 多项 ⬜ | 🟡 部分填 | **当前主要阻塞** |
| **P5** 编译验收 | P5-1~4 ✅ | p5-compile-verify ✅ | ✅ | 🟡 compile ✅；验收清单 ⬜ | ✅ 三包 + 验收清单 | 超级鸡马缺 P5-3 产出 |
| **P6** 开发管线 | P6-1~3 ✅ | p6-pipeline 🟡 | 🟡 | ⬜ | ⬜ | 四件套在仓库外，未执行 |

### 3.2 Part 2 质量门禁（规格交付库 §9）— 超级鸡马

| 检查项 | 状态 |
|--------|------|
| 01 → 02/03 全覆盖 | 🟡 主体覆盖；看板仍有 UI/匹配等待确认 |
| P-xx 附录 A 登记一致 | 🟡 大部分已登记；Q-D/Q-P 待定字段未闭合 |
| 03 五块结构 + 伪代码 | ✅ |
| 03 自包含、无「见 02」 | ✅（已做编号交叉引用规范） |
| 02 自然语言、无伪代码块 | ✅ |
| P4-2 策划验收通过 | ⬜ 04 大量未填 |
| compile 三包 | ✅ `开发文档/` |
| P5-4 logs | ✅ 多条 |
| 程序包可交 AI 开发管线 | 🟡 文档可交；数值/边界待 04 闭合 |

---

## 4. Skills 完成度

### 4.1 `skills/pipeline/`（文档管线 · 每功能必用）

| Skill | 状态 | 说明 |
|-------|------|------|
| p0-discovery ~ p6-pipeline | ✅ 7 个 SKILL.md | 与 prompts 一一对应 |
| pipeline/README.md | ✅ | 与 frameworks 区分说明 |

### 4.2 `skills/frameworks/`（L1 · workflow 按需）

| skill_id | 状态 | 实例 |
|----------|------|------|
| tournament_bracket | ✅ 完整 meta/design/ux/tech/qa/feature | 竞技场高级赛 |
| （其他玩法） | ⬜ | 超级鸡马无 L1，规则全在 L2 |

### 4.3 `skills/tech/` · `skills/ux/`（L0 横切）

| skill_id | 状态 | 用途 |
|----------|------|------|
| config_table | ✅ | P2-DS、P3-3 配置表格式 |
| configurable_rules | ✅ | Const/表 + Q-D/Q-R 分轨 |
| implementation_data | ✅ | 03 附录 D 契约/专项审计 |
| resolution_standard | ✅ | workflow 可选 |
| interaction_feedback | ✅ | workflow 可选 |
| config_table_impact | 📝 代做 | `_backlog/`，无正式 Skill |

### 4.4 维度 Skill 路线图（P2/P3 子域）

见 [skills/_backlog/维度Skill路线图.md](../skills/_backlog/维度Skill路线图.md)。

| 类别 | 已启用 | 待提炼 |
|------|--------|--------|
| P2 维度 | 3（config_table、configurable_rules、implementation_data） | 规则/状态机/协议/边界/校验/红点/UI/验收 等 9+ |
| P3 子域 | p3-feature-spec（🟡 总规范） | 功能点五块、验收场景、Feature 映射等独立 Skill |

> 路线图内部分 L2 引用路径仍为旧版（`02-…/多文件夹`、`skills/gdd/`），**文档待同步**，不影响真源路径。

---

## 5. Prompts · Templates · 文档

### 5.1 Prompts（`prompts/`）

| 项 | 状态 |
|----|------|
| P0~P6 正文文件 | ✅ 共 25+ 个提示词 |
| 规格交付库.md | ✅ 编号、门禁、索引 |
| Part2-公共头.md | ✅ 含 spec_root / 开发文档 |
| 六段式结构 | ✅ P1~P6 已统一 |
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
| 策划工作流.md | ✅ 阶段 2/3/5 已对齐单文档 |
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

### 7.1 超级鸡马（`产出/超级鸡马/` · 主真项目）

| 交付物 | 状态 | 说明 |
|--------|------|------|
| 01 原始策划案 | ✅ | 含源表提取 |
| 02 需求拆解 | ✅ | 策划语言；八维度 |
| 03 功能点梳理 | ✅ | §0~11 + 附录 A~E；D 专项审计 |
| 04 待策划补充 | 🟡 | 模板齐全；**看板 🔴8 / 🟡6 / 🟢2 待办** |
| 开发文档 三包 | ✅ | compile 可重复生成 |
| 策划验收清单 | ⬜ | 竞技场有；超级鸡马未写 |
| 职能分轨检查报告 | 🟡 | 有过迭代；非最新门禁快照 |
| workflow skill_configs | ⬜ | 空；Q-L01 待程序填 |
| P6 server/client design | ⬜ | 未产出 |

**优先待办（来自看板）**：Q-D09 跑酷物理 → Q-D08/D07/D04 计分 → Q-R01 规则边界 → Q-P01 匹配协议 → Q-L01 skill_configs。

### 7.2 竞技场高级赛（`案例/竞技场高级赛/` · 对照样例）

| 交付物 | 状态 | 说明 |
|--------|------|------|
| L1 tournament_bracket 实例化 | ✅ | workflow + 02 继承 R-TB |
| 02-03 单文档 | ✅ | 与现规范一致 |
| 开发文档 + 策划验收清单 | ✅ | P5 曾跑通 |
| P6 | ⬜ | 未在仓库内落地 |

---

## 8. 已完成内容清单（可对外说「有了什么」）

1. **完整 Part 2 Prompt 库**（P1~P6 + 可选 P0）与 **pipeline Skill** 七件套  
2. **单文档交付模型**：02/03 合并为 `{spec_root}`，compile 产出 `{feature_root}/开发文档/`  
3. **编号体系**：R / EX / PRE / LIM / RD / V / T / B / E / P-xx，02 vs 03 职能分轨  
4. **三个成熟 L0 维度 Skill**：config_table、configurable_rules、implementation_data  
5. **一个 L1 框架**：tournament_bracket + 竞技场完整样例  
6. **超级鸡马真项目**：01~03 主文档 + 附录 D 物理/计分/契约审计 + compile 三包  
7. **执行日志规范**（P5-4）+ 看板驱动的 04 回填工作流  
8. **目录命名清晰化**：pipeline / frameworks / 02-03… / 开发文档 / templates 扁平化  

---

## 9. 未完成 / 待办清单

### 9.1 规范与文档（维护层）

| 项 | 优先级 | 说明 |
|----|--------|------|
| 同步 `维度Skill路线图.md` 路径 | 中 | 旧 gdd/design、旧 02 路径 |
| 新增 `prompts/P7` Bug 回流 | 低 | 规划已有，未建 Prompt |
| Prompt 瘦身（公共头 + 本步差异） | 低 | 减少 P2 重复粘贴 |

### 9.2 Skill 建设（能力层）

| 项 | 优先级 | 说明 |
|----|--------|------|
| config_table_impact | 中 | 表关联变更影响检索 |
| P2 各维度独立 Skill（规则/状态机/…） | 低~中 | 路线图 ⬜ 项 |
| P3 子域 Skill（五块/验收/Feature 映射） | 低 | 现靠 p3-feature-spec 总规范 |
| 新 L1 frameworks（如 party_platform） | 按需 | 超级鸡马类暂无抽象 |

### 9.3 工具与自动化

| 项 | 优先级 |
|----|--------|
| compile 后路径/链接自检 | 中 |
| CI：超级鸡马 compile 回归 | 中 |
| docx → 01 半自动流水线文档化 | 低 |

### 9.4 超级鸡马项目（交付层 · 阻塞开发）

| 项 | 阶段 | 状态 |
|----|------|------|
| 04 配置数值 / 规则边界策划回填 | P4 | ⬜ 多项 Q-D / Q-R |
| 04-01 字段命名程序确认 + Q-L01 workflow | P4 | ⬜ |
| 04 回流 → 02/03 更新 | P4→P2/P3 | 🟡 机制有，未批量执行 |
| P5-3 策划验收清单 | P5 | ⬜ |
| P6 后端/前端四件套 | P6 | ⬜ |
| 策划验收「可否进 P6 = 是」 | 门禁 | ⬜ |

### 9.5 案例库

| 项 | 说明 |
|----|------|
| 超级鸡马作为第二份「全链路闭合」样例 | 待 P4+P5-3 完成后可与竞技场并列 |

---

## 10. 推荐推进顺序

```text
1. 策划闭合 04（看板 §八 顺序）→ P4-2 验收
2. Agent 回流 02/03 → compile → 新建 logs
3. 补 P5-3 策划验收清单（超级鸡马/开发文档/）
4. 程序填 workflow skill_configs（Q-L01）
5. 跑 P6-1 / P6-2（仓库外 server/client design）
6. 维护者：按 GDD-SKILL-更新规范 从闭合项目反哺 L0 维度 Skill
```

---

## 11. 相关索引

| 文档 | 路径 |
|------|------|
| 规格交付主库 | [prompts/规格交付库.md](../prompts/规格交付库.md) |
| 使用与路径 | [使用指导.md](../使用指导.md) |
| Skill 总览 | [skills/README.md](../skills/README.md) |
| 模板说明 | [templates/README.md](../templates/README.md) |
| 超级鸡马看板 | [产出/超级鸡马/补充与修改看板.md](../产出/超级鸡马/补充与修改看板.md) |
| Skill 演进规范 | [skills/GDD-SKILL-更新规范.md](../skills/GDD-SKILL-更新规范.md) |
| 维度 Skill 进度 | [skills/_backlog/维度Skill路线图.md](../skills/_backlog/维度Skill路线图.md) |

---

**文档维护**：管线规范或 L2 里程碑变更时，由维护者更新本节「统计日期」与 §3、§7 状态列。
