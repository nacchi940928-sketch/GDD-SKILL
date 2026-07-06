# P2-R 规则

规范：`skills/gdd/p2-decompose/SKILL.md` · **配置表**：`skills/tech/config_table/tech.md` · **可配置规则**：`skills/tech/configurable_rules/tech.md` · **实现数据契约**：`skills/tech/implementation_data/tech.md` · 库索引：[规格交付库.md](../规格交付库.md)

## 提示词正文（复制以下内容）

```
【规格交付 · Part 2】
将策划已定稿的 01 原始策划案转化为程序与 AI 可执行的 GDD 规格（02/03）。
不得改变策划业务意图；不得遗漏 01 内容；禁止「见原始文档」「见上文」。

功能名：{功能名}
feature_root：产出/{功能名}
功能缩写：{功能缩写}
L1 skill_id：{skill_id，无则留空}

【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-需求拆解/{功能名}/数据源/字段映射索引.md
- workflows/{项目}.workflow.json
- skills/design/{skill_id}/design.md（如有 L1）
- skills/tech/configurable_rules/tech.md（R-xx 依赖 Const/配置表时）
- skills/tech/implementation_data/tech.md（R-xx 变量追溯、契约层自检）

【本步任务】
为「{功能名}」生成 02-需求拆解 的「规则」维度。

【输出路径】
{feature_root}/02-需求拆解/{功能名}/规则/
（按子系统拆文件，如 报名与身份规则.md、签位规则.md）

【本步格式要求】
- 编号：R-{功能缩写}-{序号}（如 R-{缩写}-001）
- L1 已有编号继承：写「继承 {skill_id} R-TB-001」，不重新编号
- 每条规则必须写全：
  · 编号 + 标题
  · 触发条件、行为（执行什么）
  · 检测位置（服务端/客户端/双端）、检测方式（定时/请求/事件）
  · 数据依赖（P-xx 读写，引用已登记编号）
  · 伪代码（可执行级别）
  · 来源：01 §x.x
- 可配置规则（configurable_rules）：伪代码读 P-xx/表，禁止魔法数；数值缺口登记 Q-Dxx，边界歧义写默认实现并登记 Q-Rxx
- 实现数据契约（implementation_data）：
  · 伪代码中**每个读写的量**须对应已登记 P-xx、配置表.列或枚举；禁止「摩擦衰减」「应用重力」等无落点散文
  · 01 明确的比例/速度/周期须引用表列或 Const，不得只写在 trigger_desc
  · 复杂域按需产出 `02/规则/{域}全量审计.md`（含 R-xx 变量追溯表）
  · P2 全部维度完成后，配合 P2-DS 产出/更新 `02/…/数据源/数据契约审计.md`

【Part 2 公共铁律】
1. 产出路径固定在 {feature_root}/ 下
2. 字段只用已登记 P-xx
3. L1 已覆盖规则只写 delta，其余写「继承 {skill_id}，无 delta」
4. 继承现网模块只写对接点，标注「继承现网 {模块名}」

【本步铁律】
- 禁止 UI 布局、跳转、像素（归 P2-UI）
- 禁止「见原始文档」
- 禁止重复展开 L1 通用规则全文

【完成后自检】
- [ ] 每条 R- 是否都有触发、行为、伪代码、P-xx / 表列？
- [ ] 01 规则章节是否全覆盖？
- [ ] 依赖 Const/表的规则是否无未登记魔法数？数值/边界是否分 Q-D / Q-R？
- [ ] **implementation_data**：导出每条 R-xx 的读/写变量清单，是否**全部**有 P-xx / 表.列 / 枚举落点？
- [ ] 伪代码中是否仍有无 Const/表列支撑的概念词（重力、摩擦、倍率、冷却…）？
- [ ] 需策划填的 Const/表列是否已链到 Q-Dxx（非笼统「待确认」）？
- [ ] 若本域为复杂域：是否已建 `{域}全量审计.md` 并含变量追溯节？

请直接创建/写入 markdown 文件，不要只输出大纲。
```
