# Part 2 公共头（复制到各 Prompt 正文开头）

> 本文件不是独立 Prompt。复制下方块，粘贴到 Part 2 各提示词「提示词正文」**最前面**，再追加本步特有内容。  
> 完整规范见 [规格交付库.md](../规格交付库.md) · 02 写作：[templates/02-需求拆解-写作规范.md](../../templates/02-需求拆解-写作规范.md)

---

## 可复制的公共头

```
【规格交付 · Part 2】
将 01 原始策划案转化为 GDD 交付物：02（策划语言）+ 03（程序规格）。
不得改变策划业务意图；不得遗漏 01 内容；禁止「见原始文档」「见上文」。

功能名：{功能名}
feature_root：产出/{功能名}
spec_root：{feature_root}/02-03需求拆解与功能点梳理   ← 即 02/03 拆解目录
功能缩写：{功能缩写}
L1 skill_id：{skill_id，无则留空}

【交付形态 · 单文档】
- 02：{spec_root}/02-需求拆解.md          ← 策划/汇报，自然语言
- 03：{spec_root}/03-功能点梳理.md        ← 程序/AI，伪代码 + P-xx + 附录 A~E
- 04：{feature_root}/04-待策划补充/{功能名}/
- 开发文档：{feature_root}/开发文档/       ← compile 三包（勿手改）
- logs：每次改交付文档须新建 {feature_root}/logs/{YYYYMMDD}-{HHmmss}.log.md

【Part 2 公共铁律】
1. **02 vs 03**：02 写「做什么」（规则说明、玩家流程）；03 写「怎么做」（伪代码、字段、协议、审计）
2. **P-xx 只登记在 03 附录 A**（P3-3）；02 禁止 P-xx 大表与伪代码
3. 每条 02 规则/边界/验收须标注「来源：01 §x.x」；R- 编号供 02↔03 对照
4. L1 已有规则写「继承 {skill_id} R-xxx」，只写 delta
5. 03 必须自包含；禁止「见 02 §x」「见原始文档」
6. **禁止**修改 `skills/`；业务只写入 `{feature_root}/`
7. 会话结束或文档更新后：**P5-4 新建 log**（禁止覆盖旧 log）

---

## 各阶段 @ 必读输入（按步追加在公共头之后）

### P1-1 / P1-2

```
【@ 必读输入】
- 源文档/{策划案}.docx（P1-1）或 {feature_root}/01-原始策划案/{功能名}/原始策划案.md（P1-2）
- templates/01-原始策划案/{功能名}/原始策划案.md
```

### P2 全维度（写入 02-需求拆解.md）

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md（已有则追加对应章节）
- templates/02-需求拆解-写作规范.md
- workflows/{项目}.workflow.json
- skills/frameworks/{skill_id}/（如有 L1）
```

### P3 全步骤（写入 03-功能点梳理.md）

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md
- {feature_root}/02-03需求拆解与功能点梳理/03-功能点梳理.md（已有则追加）
- 源文档/竞技场高级赛（纷乱的群殴锦标赛）—— 功能点梳理.docx（格式真源，P3-2）
- skills/frameworks/{skill_id}/（如有 L1）
- skills/tech/config_table、implementation_data（P3-3 附录）
```

### P4 / P5 / P6

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md
- {feature_root}/02-03需求拆解与功能点梳理/03-功能点梳理.md
- workflows/{项目}.workflow.json
- {feature_root}/开发文档/程序包.md（P5-2 之后 / P6）
- {feature_root}/04-待策划补充/{功能名}/（P4-2 / P5-3）
- {feature_root}/职能分轨检查报告.md（P5-1 之后，如有）
- templates/logs/模板.log.md（P5-4）
```
