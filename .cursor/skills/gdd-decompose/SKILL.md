---
name: gdd-decompose
description: >-
  Runs the GDD SKILL Part 2 pipeline to decompose game design documents into
  02-需求拆解 and 03-功能点梳理. Converts docx or 原始策划案.md through
  需求拆解, 功能点梳理, 待策划补充, compile, and optional 开发管线.
  Use when the user mentions 策划案拆解, GDD 管线, 需求拆解, 功能点梳理,
  原始策划案, docx 转规格, compile 策划包, or asks to process a design doc
  in GDD SKILL.
---

# GDD 策划案拆解管线

将策划案（docx / 01 原始策划案）规格化为 **02 + 03**，供程序与 AI 开发读取。

**子项目根目录**：`GDD SKILL/`（与 `prompts/`、`产出/`、`skills/` 同级）。所有路径均相对此根。

## 执行模型

```text
Cursor Skill（本文件）     → 编排：选阶段、填占位符、过门禁
GDD SKILL/skills/pipeline/ → 规范：格式铁律（每步必读对应 p*-*/SKILL.md）
GDD SKILL/prompts/         → 指令：复制各 .md 的「提示词正文」逐步执行
```

**禁止**：修改 `GDD SKILL/skills/`（除维护者任务）；手改 `{feature_root}/开发文档/`。

## 启动：向用户确认或推断

| 输入 | 用户需提供 | Agent 推断 |
|------|-----------|-----------|
| 工作包名称 | `{功能名}`（与 `产出/{功能名}` 一致） | 从路径或文档标题 |
| 产出目录 | `{feature_root}` = `产出/{功能名}` | 默认 |
| workflow | `workflows/{项目}.workflow.json` | 扫描 workflows/ 或问用户 |
| 功能缩写 / skill_id | 可选 | 从 workflow 的 `selected_skills`、文档内容 |

**执行范围**（用户未说明时，从当前进度继续；有说明则 obey）：

| 用户说法 | 范围 |
|----------|------|
| 「整包 / 全流程 / 拆到 03」 | 当前入口 → 03 完成（含 04 清单可选） |
| 「拆到编译 / compile」 | → 编译验收·执行编译验收 |
| 「只拆 02 / 需求拆解」 | 需求拆解 9 步 |
| 「只拆 03 / 功能点梳理」 | 功能点梳理 6 步 |
| 「只做规则 / 只做 §4」 | 对应单个 Prompt |

## 入口检测（按优先级）

```text
1. 用户 @ 了 docx / 口述稿 / 01 草稿     → 原始策划案（P1）
2. 存在 01/…/原始策划案.md 且无 02      → 需求拆解（P2）
3. 02 不完整 / 用户指定某维度            → 需求拆解 单步或续跑
4. 02 完成、03 缺或不全                  → 功能点梳理（P3）
5. 02+03 完成、04 未生成                 → 待策划补充（P4）
6. 用户要求 compile                      → 编译验收（P5）
7. 三包已有、用户要求开发文档            → 开发管线（P6）
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

1. **读规范**：`GDD SKILL/skills/pipeline/p{N}-*/SKILL.md`（本阶段）
2. **读 Prompt**：`GDD SKILL/prompts/{阶段}/{步骤}.md` → 使用「提示词正文」块（不含文末「输入内容示例」）
3. **替换占位符**：`{功能名}` `{feature_root}` `{功能缩写}` `{skill_id}` `{项目}`
4. **@ 必读输入**：按 Prompt 与 [pipeline-steps.md](pipeline-steps.md) 列表
5. **写入产出**：直接写文件，不要只输出大纲
6. **自检**：Prompt 内「完成后自检」勾选
7. **汇报**：本步产出路径 + 是否过门禁 + 下一步建议

**需求拆解固定顺序**（不可乱序）：

```text
数据源 → 系统内容分解 → 规则 → 边界条件 → 状态机 → UI交互 → 红点 → 校验规则 → 验收标准
```

**功能点梳理固定顺序**：

```text
阅读说明 → 功能点拆分（可分批）→ 字段映射 → 验收场景 → 待确认事项 → Feature对齐
```

完整步骤表与门禁见 [pipeline-steps.md](pipeline-steps.md)；编号体系见 `GDD SKILL/prompts/规格交付库.md`。

## 铁律（Part 2 公共）

1. 不改策划业务意图；不遗漏 01 章节
2. 02 = 策划自然语言；伪代码 / P-xx / 审计 → 03
3. 03 禁止「见 02/xx」——规则正文须写全
4. 每条 R- 须含 **边界**（继承现网 / 本次新增 / 本次改动）
5. 产出只写 `{feature_root}/`；真实交付用 `产出/`，`案例/` 仅对照
6. **改动了交付文档后**：新建 `logs/{YYYYMMDD}-{HHmmss}.log.md`（模板 `GDD SKILL/templates/logs/模板.log.md`），禁止覆盖旧 log

## 编译

仅当 02/03 就绪且用户要求或进入 P5 时：

```bash
cd "GDD SKILL"
python tools/compile.py {feature_root} --workflow workflows/{项目}.workflow.json
```

产出 `{feature_root}/开发文档/程序包.md | 测试包.md | 策划包.md`。**禁止手改三包**。

## 与用户交互

- **一步一确认**：默认每完成一个 Prompt 步骤后暂停，汇报并询问是否继续（用户说「继续 / 全流程 / 不要停」则连续执行）
- **阻塞项**：【待确认】、04 未填、完整性检查 gap → 列出清单，不编造数值
- **缺 workflow**：继续拆解但 `{skill_id}` 留空；compile 前须补齐

## 快速示例

**docx → 整包拆解**：

```text
@GDD SKILL/源文档/{你的策划案}.docx
工作包：{功能名}
请按 gdd-decompose 从 docx 跑到 03 完成，feature_root=产出/{功能名}
```

**01 已有 → 只跑需求拆解·规则**：

```text
@GDD SKILL/产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md
工作包：{功能名}，只做需求拆解·规则
```

## 延伸阅读

| 文件 | 用途 |
|------|------|
| [pipeline-steps.md](pipeline-steps.md) | 逐步 Prompt 路径与门禁 |
| `GDD SKILL/使用指导.md` | 路径、@ 引用、踩坑 |
| `GDD SKILL/prompts/规格交付库.md` | 编号、索引、Part 2 真源 |
