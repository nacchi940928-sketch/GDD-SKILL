# Part 2 公共头（复制到各 Prompt 正文开头）

> 本文件不是独立 Prompt。复制下方块，粘贴到 Part 2 各提示词「提示词正文」**最前面**，再追加本步特有内容。  
> 完整规范见 [规格交付库.md](../规格交付库.md)。

---

## 可复制的公共头

```
【规格交付 · Part 2】
将策划已定稿的 01 原始策划案转化为程序与 AI 可执行的 GDD 规格（02/03）。
不得改变策划业务意图；不得遗漏 01 内容；禁止「见原始文档」「见上文」。

功能名：{功能名}
feature_root：案例/{功能名}
功能缩写：{功能缩写}
L1 skill_id：{skill_id，无则留空}

【Part 2 公共铁律】
1. 产出路径固定在 {feature_root}/ 下对应阶段目录
2. 字段须先在 P2-DS 登记 P-xx，后续禁止自创字段名
3. 每条规则/边界/校验/验收须标注「来源：01 §x.x」
4. L1 框架已有规则写「继承 {skill_id} R-xxx」，只写本项目 delta
5. 写全：检测位置、检测方式、数据依赖（P-xx）、伪代码
6. 03 功能点必须自包含；02 允许跨文件引用编号
7. **禁止**修改 `skills/`（Skill 变更须维护者确认）；业务内容只写入 `{feature_root}/`

---

## 各阶段 @ 必读输入（按步追加在公共头之后）

### P1-1 / P1-2

```
【@ 必读输入】
- 参考/{策划案}.docx（P1-1）或 {feature_root}/01-原始策划案/{功能名}/原始策划案.md（P1-2）
- templates/01-原始策划案/{功能名}/原始策划案.md
```

### P2-DS（首个维度，须最先执行）

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- workflows/{项目}.workflow.json
- skills/design/{skill_id}/meta.md、tech.md（如有 L1）
```

### P2-R / P2-EX / P2-V / P2-T / P2-RD

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-需求拆解/{功能名}/数据源/字段映射索引.md
- workflows/{项目}.workflow.json
- skills/design/{skill_id}/design.md（如有 L1）
- （按维度追加已完成的 02 子目录）
```

### P2-SM / P2-UI

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-需求拆解/{功能名}/规则/、数据源/
- skills/design/{skill_id}/、skills/ux/、skills/tech/（按本步需要）
```

### P3 全步骤

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-需求拆解/{功能名}/（全目录）
- skills/design/{skill_id}/（如有 L1）
```

### P4 / P5 / P6

```
【@ 必读输入】
- {feature_root}/01-原始策划案/{功能名}/原始策划案.md
- {feature_root}/02-需求拆解/{功能名}/（全目录）
- {feature_root}/03-功能点梳理/{功能名}/（全目录）
- workflows/{项目}.workflow.json
- outputs/{功能名}/程序包.md（P5-2 之后 / P6）
- {feature_root}/04-待策划补充/{功能名}/（P4-2 / P5-3）
- {feature_root}/职能分轨检查报告.md（P5-1 之后）
```
