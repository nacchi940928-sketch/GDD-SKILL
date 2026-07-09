---
name: gdd-decompose
description: >-
  Runs the GDD SKILL Part 2 pipeline to decompose game design documents into
  02-需求拆解 and 03-功能点梳理. Converts docx or 原始策划案.md through
  需求拆解, 功能点梳理, 待策划补充, compile, and optional 开发管线.
  Use when the user mentions 策划案拆解, GDD 管线, 需求拆解, 功能点梳理,
  原始策划案, docx 转规格, compile 策划包, 决策稿对账, 业务逻辑表,
  已经确认, 程序反馈对账, or asks to process a design doc in GDD SKILL.
---

# GDD 策划案拆解管线

将策划案（docx / 01 原始策划案）规格化为 **02 + 03**，供程序与 AI 开发读取。

**SKILLS_ROOT（包根）**：本文件所在目录的父级，即含 `prompts/`、`pipeline/`、`gdd-decompose/` 的 **`skills/`** 文件夹。  
**WORKSPACE_ROOT（工作区根）**：`skills/` 的父目录；`产出/`、`源文档/` 在其下。  
包内路径（`prompts/`、`pipeline/`、`templates/`、`tools/`、`workflows/`）均相对 **SKILLS_ROOT**。

## 前置依赖（必读）

本 Skill 与下列目录**同在 `skills/` 包内**（复制整包 `skills/` 即齐全）：

| 目录（相对 SKILLS_ROOT） | 用途 |
|--------------------------|------|
| `prompts/` | 各阶段 Prompt「提示词正文」 |
| `pipeline/` | 格式铁律（每步必读 p*-*/SKILL.md） |
| `templates/` | 01～04、logs 模板 |
| `tools/` | `compile.py`（P5） |
| `workflows/` | `{项目}.workflow.json` |

缺任一目录 → 汇报缺失项并停止，不要即兴编造规范。

## 执行模型

```text
Cursor Skill（本文件）     → 编排：选阶段、填占位符、过门禁
pipeline/         → 规范：格式铁律（每步必读对应 p*-*/SKILL.md）
prompts/                 → 指令：复制各 .md 的「提示词正文」逐步执行
```

**禁止**：修改 `prompts/`、`pipeline/`（除维护者任务）；手改 `{feature_root}/开发文档/`。

## 不包含：规范反哺（P7）

本 Skill **仅负责交付轨**（P1～P6 的拆解与 compile）。**不会**在 P3/P5 完成后自动：

- 生成 `规范反哺报告.md`
- 修改 `prompts/` 或 `skills/`

若维护者要从 L2 萃取规范增量，须**另开会话**并显式使用 **`gdd-norm-feedback`**（见 `prompts/规范反哺/README.md`）。

## 启动：向用户确认或推断

| 输入 | 用户需提供 | Agent 推断 |
|------|-----------|-----------|
| 工作包名称 | `{功能名}`（与 `产出/{功能名}` 一致） | 从路径或文档标题 |
| 产出目录 | `{feature_root}` = `产出/{功能名}` | 默认 |
| workflow | `skills/workflows/{项目}.workflow.json`（相对 WORKSPACE_ROOT） | 扫描 `workflows/` 或问用户 |
| 功能缩写 / skill_id | 可选 | 从 workflow 的 `selected_skills`、文档内容 |

**执行范围**（用户未说明时，从当前进度继续；有说明则 obey）：

| 用户说法 | 范围 |
|----------|------|
| 「整包 / 全流程 / 拆到 03」 | 当前入口 → 03 完成（含 04 清单可选） |
| 「拆到编译 / compile」 | → 编译验收·执行编译验收 |
| 「只拆 02 / 需求拆解」 | 需求拆解 9 步 |
| 「只拆 03 / 功能点梳理」 | 功能点梳理 6 步 |
| 「只做规则 / 只做 §4」 | 对应单个 Prompt |
| 「对账 / 程序反馈 / 业务逻辑表 / 已经确认」 | P4.5（diff + 回流 02/03/04/01 + logs） |

## 入口检测（按优先级）

```text
1. 用户 @ 了 docx / 口述稿 / 01 草稿     → 原始策划案（P1）
2. 存在 01/…/原始策划案.md 且无 02      → 需求拆解（P2）
3. 02 不完整 / 用户指定某维度            → 需求拆解 单步或续跑
4. 02 完成、02.5 缺                       → 工程真源对齐（P2.5）
5. 02.5 完成、03 缺或不全                  → 功能点梳理（P3）
6. 02+03 完成、04 未生成                 → 待策划补充（P4）
6.5 用户 @ 程序反馈 / 业务逻辑表 / *已经确认* → 外部决策稿对账（P4.5）
     （须已有 01~04 骨架；不替代 P1~P4 首次跑）
7. 用户要求 compile                      → 编译验收（P5）
8. 三包已有、用户要求开发文档            → 开发管线（P6）
```

**01 定稿唯一路径**：

```text
{feature_root}/01-原始策划案/{功能名}/原始策划案.md
```

**02/03 真源**：

```text
{feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md
{feature_root}/02-03需求拆解与功能点梳理/03-功能点梳理.md
```

## 单步执行流程（每步重复）

1. **读规范**：`pipeline/p{N}-*/SKILL.md`（本阶段）
2. **读 Prompt**：`prompts/{阶段}/{步骤}.md` → 使用「提示词正文」块（不含文末「输入内容示例」）
3. **替换占位符**：`{功能名}` `{feature_root}` `{功能缩写}` `{skill_id}` `{项目}`
4. **@ 必读输入**：按 Prompt 与 [reference.md](reference.md) 列表
5. **写入产出**：直接写文件，不要只输出大纲
6. **自检**：Prompt 内「完成后自检」勾选
7. **汇报**：本步产出路径 + 是否过门禁 + 下一步建议

**需求拆解固定顺序**（不可乱序）：

```text
数据源 → 系统内容分解 → 规则 → 边界条件 → 状态机 → UI交互 → 红点 → 校验规则 → 验收标准
```

**工程真源对齐（P2 之后必跑）**：

```text
按需求摘录字段 → 02.5-工程真源摘录.md（无 program_repo 时仍产出 §4 待补清单）
```

**功能点梳理固定顺序**：

```text
阅读说明 → 功能点拆分（可分批）→ 字段映射 → 验收场景 → 待确认事项 → Feature对齐
```

完整步骤表与门禁见 [reference.md](reference.md)；编号体系见 `prompts/规格交付库.md`。

## 可选：P4.5 外部决策稿对账

**触发**：用户显式 @ `程序反馈/`、`*业务逻辑表*`、`*已经确认*` 等**决策闭合表**（非策划案正文、非 docx 真源）。

**禁止**：在首次 P1～P4 流程中自动读取上述文件（铁律 #7 不变）。

**输入**：外部决策稿的「策划结论 / 已确认」列；现有 `{feature_root}/01~04`；`补充与修改看板.md`。

**步骤**：

1. 读 `prompts/决策稿对账/外部决策稿对账.md` → 使用「提示词正文」
2. 逐条 diff 决策稿 vs 01/02/03/04，分类：遗漏 / 写反 / 一致 / 双方仍开放
3. 更新 02 R-、03 伪代码与附录 C、04 Q-R/Q-D（仅闭合项）、01 流程歧义句
4. 新建 `logs/{YYYYMMDD}-{HHmmss}-决策稿回流.log.md`（类型：决策稿回流）
5. 更新 `补充与修改看板.md`；**不**修改 `prompts/`、`pipeline/`（维护者任务）
6. 仍开放的 sheet 导出、数值终稿、Spec 口头批准 → 只登记 04/看板，不编造

**产出门禁**：无新增 C 类（与决策稿冲突）；03 与 02 已定 R- 一致。

案例参考：[references/skill-update-程序反馈对账-超级鸡马案例.md](references/skill-update-程序反馈对账-超级鸡马案例.md)

## 铁律（Part 2 公共）

1. 不改策划业务意图；不遗漏 01 章节
2. 02 = 策划自然语言；伪代码 / P-xx / 审计 → 03
3. 03 禁止「见 02/xx」——规则正文须写全
4. 每条 R- 须含 **边界**（继承现网 / 本次新增 / 本次改动）
5. 产出只写 `{feature_root}/`；真实交付用 `产出/`，`案例/` 仅对照
6. **改动了交付文档后**：新建 `logs/{YYYYMMDD}-{HHmmss}.log.md`（模板 `templates/logs/模板.log.md`），禁止覆盖旧 log
7. **禁止读取 `程序反馈/`** 作为管线输入（与 L2 产出对账的审计稿，非 docx→04 真源）
8. **工程字段三态**：已绑定（02.5 有仓库来源）/ 待补·程序（— + Q-P）/ 待补·策划（Q-D）；无仓库来源时 **禁止** Agent 自造 proto 名、表名
9. **歧义消歧**：01 出现「轮流/同时/并行/依次/先到先得」→ 02 须择一写清，不得留两种解读
10. **终裁归属**：竞争、排序、计时类规则须写「由谁终裁」；无依据则【待确认】，禁止默认某一端
11. **02/03 一致**：03 伪代码与 02 已定 R- 冲突时，以 02 为准修订 03；P4.5 对账后必须同步 03

## 编译

仅当 02/03 就绪且用户要求或进入 P5 时：

```bash
# 在 WORKSPACE_ROOT 执行
python skills/tools/compile.py {feature_root} --workflow skills/workflows/{项目}.workflow.json
```

产出 `{feature_root}/开发文档/程序包.md | 测试包.md | 策划包.md`。**禁止手改三包**。

## 与用户交互

- **一步一确认**：默认每完成一个 Prompt 步骤后暂停，汇报并询问是否继续（用户说「继续 / 全流程 / 不要停」则连续执行）
- **阻塞项**：【待确认】、04 未填、完整性检查 gap → 列出清单，不编造数值
- **缺 workflow**：继续拆解但 `{skill_id}` 留空；compile 前须补齐

## 快速示例

见 [examples.md](examples.md)。

## 延伸阅读

| 文件 | 用途 |
|------|------|
| [reference.md](reference.md) | 逐步 Prompt 路径与门禁 |
| [references/skill-update-程序反馈对账-超级鸡马案例.md](references/skill-update-程序反馈对账-超级鸡马案例.md) | P4.5 回归案例 |
| [../结构说明.md](../结构说明.md) | 全结构、复制清单 |
| [../使用指导.md](../使用指导.md) | 路径、@ 引用、踩坑 |
| `prompts/规格交付库.md` | 编号、索引、Part 2 真源 |
