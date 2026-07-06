# GDD SKILL

> **目标**：产出程序可执行的 **需求拆解（02）** 与 **功能点梳理（03）**，经补充清单迭代完善后入库交付程序。  
> 策划提供原始案 → AI/程序辅助拆解 → **补充清单 ↔ 回填验收** → 入库。

**当前分支**：`promptmerge`（PromptMerge 架构落地版）  
**仓库**：https://github.com/nacchi940928-sketch/GDD-SKILL.git

---

## 1. 项目定位

| 是什么 | 不是什么 |
|--------|----------|
| **程序可执行**的需求拆解（02）与功能点梳理（03）的产出流水线 | 游戏客户端 / 服务端**代码**工程 |
| 可复用的 Prompt + Skill 知识库，支撑拆解、补全与编译交付 | 玩法创意设计或从空白生成策划案 |
| design 仓库的**规格文档真相来源**，入库后交程序开发 | 替代策划撰写原始策划案（01） |

**本工程的唯一交付目标**：让程序（及下游 AI 开发管线）拿到**完整、自包含、可实现**的 02 + 03，而不是半成品摘要、创意草案或可运行产品。

**核心协作模式**：

```text
策划提供原始策划案（01）
        ↓
程序/AI 按 Prompt 拆解 → 02 需求拆解 + 03 功能点梳理
        ↓
生成 04 待策划补充清单 → 策划回填 → P4-2 回填验收
        ↓
未通过？→ 更新 02/03/04 → 再次「清单 → 回填 → 验收」（循环）
        ↓
P5 编译验收通过 → 05 入库交付 → 程序接手（P6 开发管线）
```

- **策划主责**：提供原始案、确认业务规则与数值文案、逐轮回填 04 缺失项  
- **程序/AI 主责**：拆解、生成补充清单、验收回填完整性、编译合并、入库  
- **交付物**：完整的 `02-需求拆解` + `03-功能点梳理`（及已填完的 `04`），可直接作为程序开发与 AI 管线的输入

**架构目标**：不同功能共享 L0/L1 基底，L2 只写项目差异，降低重复拆解劳动，提升程序与 AI 对需求理解的一致性。

---

## 2. 目录结构

```text
GDD SKILL/                          ← 项目主目录（本 README 同级为仓库根）
└── GDD SKILL/
    ├── README.md                   ← 详细说明（本文件副本见仓库根 README.md）
    ├── 策划工作流.md               ← 五阶段工作流详解 + 检查清单
    ├── 内容要点.md                 ← 与 design/server/client 仓库协作说明
    │
    ├── prompts/                    ← ★ 提示词（复制粘贴到 Agent 即用）
    │   ├── P1/  原始策划案（2）
    │   ├── P2/  需求拆解（8 维度）
    │   ├── P3/  功能点梳理（6）
    │   ├── P4/  待策划补充（2）
    │   ├── P5/  编译验收（3）
    │   └── P6/  开发管线（3）
    │
    ├── skills/                     ← ★ 规范与可复用知识（Skill）
    │   ├── gdd/                    ← 各阶段规范（p1~p6-decompose 等）
    │   ├── design/                 ← L1 系统基底（如 tournament_bracket）
    │   ├── ux/                     ← L0 横切（interaction_feedback）
    │   ├── tech/                   ← L0 横切（resolution_standard）
    │   └── _template/              ← 新建 Skill 模板
    │
    ├── templates/                  ← L2 实例化文档模板（01~04 阶段）
    ├── workflows/                  ← 项目配置（selected_skills + skill_configs）
    ├── tools/                      ← 工具脚本
    │   ├── compile.py              ← 02+03 → 程序包/测试包/策划包
    │   ├── docx_extract.py         ← 策划案 docx 提取
    │   └── organize.py             ← 目录整理
    │
    ├── 案例/                       ← 完整样例（竞技场高级赛）
    ├── outputs/                    ← 编译产出（由 compile.py 生成，勿手改）
    └── docs/
        └── PromptMerge规划.md      ← 架构设计与落地记录
```

---

## 3. 三层基底架构

```text
L0 横切基底（全项目共用）
  resolution_standard / interaction_feedback
        ↓
L1 系统基底（跨功能复用）
  tournament_bracket / …          ← **框架 Skill**：抽象模式 + config 槽位
  案例/{功能}/02~03                 ← **项目实例**：竞技场、周练组、竞猜等 delta
        ↓
L2 项目实例（本项目差异）
  案例/{功能}/01~04 + workflows/*.json skill_configs
```

**原则**：L1 写通用规则，workflow 填项目参数，**03-功能点梳理** 是程序 AI 管线的唯一主读文档。

---

## 4. 文档五阶段 + Prompt 六段

### 文档阶段（策划工作流）

| 阶段 | 目录 | 执行者 | 说明 |
|------|------|--------|------|
| 01 | 原始策划案 | **策划提供** | 完整设计叙述（本工程输入，非 AI 凭空生成） |
| 02 | 需求拆解 | 程序/AI | 8 维度：规则、边界、红点、数据源、UI、状态机、校验、验收 |
| 03 | 功能点梳理 | 程序/AI | **程序主文档**，自包含可开发 |
| 04 | 待策划补充 | 程序/AI + **策划** | 生成补充清单 → 策划回填 → 验收（**可循环**） |
| 05 | 入库交付 | 程序 | 02/03/04 完整后 git 提交，交付程序开发 |

### Prompt 阶段（Agent 执行）

| 段 | 提示词数 | 索引 |
|----|----------|------|
| P1 原始案 | 2 | [prompts/P1/](GDD%20SKILL/prompts/P1/) |
| P2 需求拆解 | 8 | [prompts/P2/](GDD%20SKILL/prompts/P2/) |
| P3 功能点 | 6 | [prompts/P3/](GDD%20SKILL/prompts/P3/) |
| P4 待补充 | 2 | [prompts/P4/](GDD%20SKILL/prompts/P4/) |
| P5 编译验收 | 3 | [prompts/P5/](GDD%20SKILL/prompts/P5/) |
| P6 开发管线 | 3 | [prompts/P6/](GDD%20SKILL/prompts/P6/) |

**用法**：打开对应 `.md` → 复制「提示词正文」→ 替换 `{功能名}` → `@` 引用文件 → 发送 Agent。  
规范细节见 `skills/gdd/*/SKILL.md`，**不要与提示词混淆**。

### 推荐执行顺序

```text
P1 → P2 → P3
  ↓
P4-1 补充清单 → 策划回填 → P4-2 验收 ──┐
  ↑                                    │ 未通过则循环
  └────────────────────────────────────┘
  ↓ 通过
P5 编译验收 → 05 入库交付 → P6 开发管线
```

完整索引：[prompts/README.md](GDD%20SKILL/prompts/README.md)

---

## 5. 快速开始

### 环境

- Python 3.8+
- 无需额外依赖（`compile.py` 纯标准库）

### 编译示例（竞技场高级赛）

```bash
cd "GDD SKILL"
python tools/compile.py 案例/竞技场高级赛 --workflow workflows/arena.workflow.json
```

**产出**（`outputs/竞技场高级赛/`）：

| 文件 | 读者 | 内容 |
|------|------|------|
| 程序包.md | 后端/前端/AI | 03 功能点 + 02 关键维度 |
| 测试包.md | 测试 | 验收标准 + 验收场景 + L1 QA |
| 策划包.md | 策划 | 01 + 规则摘要 + skill_configs |
| compiled.json | 工具链 | 编译 manifest |

### 新建功能（概要）

1. 策划按 P1 产出 `01-原始策划案`
2. 程序/AI 按 P2、P3 提示词逐段执行
3. P4 生成待补充清单 → 策划回填
4. P5 分轨检查 + 编译 + 验收
5. P6 生成 server/client design 四件套，进入 AI 自动开发管线

复制 `workflows/arena.workflow.json`，修改 `selected_skills` 与 `skill_configs`。

---

## 6. 已内置 Skill 清单

| ID | 层级 | 说明 |
|----|------|------|
| `resolution_standard` | L0 | 1080×2340 fit 留黑边、安全区 |
| `interaction_feedback` | L0 | 按钮三态、Toast、防连点 |
| `tournament_bracket` | L1 **框架** | 单败 Bracket 通用模式（报名/签位/阶段/节点）；**不含**竞技场/竞猜等业务 |
| `gdd/p1~p6-*` | 流程 | 各阶段规范 Skill（非业务系统） |

> 具体功能（如竞技场高级赛）的业务规则在 `案例/{功能名}/` 实例化，通过 `workflows/*.json` 的 `skill_configs` 填框架参数。

---

## 7. 参考案例

**竞技场高级赛**（`案例/竞技场高级赛/`）

- 完整走通 01 → 04 五阶段
- 关联 workflow：`workflows/arena.workflow.json`
- 已编译产出：`outputs/竞技场高级赛/`
- 继承现网「纷乱的群殴」决斗模块，本次增量为分组/报名/竞猜/商店

评审建议路径：

1. 读 `案例/.../03-功能点梳理/.../0-阅读说明.md` — 程序主文档入口  
2. 读 `outputs/竞技场高级赛/程序包.md` — 编译合并视角  
3. 对照 `skills/design/tournament_bracket/` — L1 基底 vs L2 实例差异  

---

## 8. 与研发仓库的关系

（详见 [内容要点.md](GDD%20SKILL/内容要点.md)）

```text
design 仓库（本工程产出）→ server/design + client/design（P6 四件套）→ AI 管线自动开发 → 测试验收
```

| 仓库 | 本工程交付物 |
|------|--------------|
| design | 01~04 阶段文档 + outputs 编译包 |
| server/client | P6 需求/设计/开发/管线编排 |
| design-skills | `skills/` 知识包 |

---

## 9. 评审关注点

| 维度 | 建议评审问题 |
|------|--------------|
| 工作流完整性 | P1~P6 是否覆盖策划→程序→测试全链路？ |
| 可复用性 | L1 tournament_bracket 能否支撑下一个锦标赛类功能？ |
| 程序可读性 | 03 是否自包含、无「见原文档」？ |
| AI 可执行性 | 02 规则是否有伪代码 + P-xx？状态机是否无歧义？ |
| 协作边界 | 04 待补充 vs 03 写全是否清晰？ |
| 工具链 | compile.py 产出是否满足后端/前端/测试分轨阅读？ |

---

## 10. 文档索引

| 文档 | 用途 |
|------|------|
| [策划工作流.md](GDD%20SKILL/策划工作流.md) | 阶段定义与检查清单 |
| [docs/PromptMerge规划.md](GDD%20SKILL/docs/PromptMerge规划.md) | 架构设计与 Vibe Studio 融合说明 |
| [prompts/README.md](GDD%20SKILL/prompts/README.md) | 22 个提示词索引 |
| [templates/转换规范.md](GDD%20SKILL/templates/转换规范.md) | 01→03 转换铁律 |

---

## 11. 版本与分支

| 分支 | 说明 |
|------|------|
| `main` | 初始提交：模板 + 竞技场案例 |
| `promptmerge` | PromptMerge 架构：skills / prompts / compile / workflows |

**变更原则**：改 `skills/`、`案例/`、`workflows/` → 重新 `compile.py` → **禁止手改 `outputs/`**。

---

## 12. 待办（评审后）

- [ ] 抽象更多 L1 Skill（shop、currency、背包等边缘系统）
- [ ] docx_extract 改为 XML 顺序提取（见转换规范）
- [ ] 与 server/client pipe 仓库的 artifact 路径对齐
- [ ] P0 立项提示词（GameDNA / Skill 选型，可选）

---

*文档生成供项目组评审 · 如有问题请在 PR / Issue 中标注具体阶段（P1~P6）与功能名。*
