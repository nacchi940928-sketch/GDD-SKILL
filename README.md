# GDD SKILL

> 游戏策划案标准化工作流：**提示词驱动拆解 + 可复用 Skill 基底 + 编译交付多职能文档**  
> 面向 AI 辅助开发管线，支撑策划 → 程序 → 测试协作。

**当前分支**：`promptmerge`（PromptMerge 架构落地版）  
**仓库**：https://github.com/nacchi940928-sketch/GDD-SKILL.git

---

## 1. 项目定位

| 是什么 | 不是什么 |
|--------|----------|
| 策划案从原始文档到程序可执行规格的**工作流与工具集** | 游戏客户端 / 服务端代码工程 |
| 可复用的 **Prompt + Skill 知识库** | 一键从想法到可玩 Demo |
| 对接 design / server / client 仓库的**文档真相来源** | 直接替代策划人工写案 |

**核心目标**：不同功能共享同一套 L0/L1 基底，按项目配置差异（L2 实例），降低策划重复劳动，提升程序与 AI 对需求的理解一致性。

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
  tournament_bracket / shop_system / …
  meta.md + design/ux/tech/qa/feature + config_schema
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
| 01 | 原始策划案 | 策划 | 完整设计叙述 |
| 02 | 需求拆解 | 程序/AI | 8 维度：规则、边界、红点、数据源、UI、状态机、校验、验收 |
| 03 | 功能点梳理 | 程序/AI | **程序主文档**，自包含可开发 |
| 04 | 待策划补充 | 策划回填 | 数值、文案、美术、打点等 |
| 05 | 入库交付 | 程序 | git 提交 |

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
P1 → P2(DS→R→EX→SM→UI→RD→V→T) → P3 → P4 → P5 → P6
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
| `tournament_bracket` | L1 | 单败对阵树：报名、签位、阶段、节点状态机 |
| `gdd/p1~p6-*` | 流程 | 各阶段规范 Skill（非业务系统） |

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
