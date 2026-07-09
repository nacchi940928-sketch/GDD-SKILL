# 立项探索·GameDNA定调 GameDNA 定调

规范：`skills/pipeline/p0-discovery-立项探索/SKILL.md`

## 提示词正文（复制以下内容）

```
请阅读我 @ 的 产出/{功能名}/00-立项探索/{功能名}/project.json（及策划补充说明，如有）。

工作包名称（策划案主题）：{功能名}

【任务】
根据已确认的项目边界，提炼体验定调（GameDNA）。输出 JSON + 人类可读 markdown。

【输出文件】
产出/{功能名}/00-立项探索/{功能名}/game_dna.json
产出/{功能名}/00-立项探索/{功能名}/game_dna.md

【game_dna 必须包含】
1. fantasy — 玩家扮演什么、在什么世界/情境（1~3 句）
2. emotion — 目标情绪（数组，如「紧张」「社交炫耀」「公平竞技」）
3. core_experience — 核心体验一句话（玩家记得什么）
4. core_loop — 核心循环（文字或 ASCII，3~7 步，不含数值）
5. excluded_systems — 明确**不做**的系统/玩法（防止范围蔓延）
6. design_pillars — 设计支柱 2~4 条（做取舍时的原则）
7. references_notes — 参考游戏启发点（非规则照搬）

【game_dna.json 格式】
{
  "fantasy": "",
  "emotion": [],
  "core_experience": "",
  "core_loop": "",
  "excluded_systems": [],
  "design_pillars": [],
  "references_notes": "",
  "open_questions": [],
  "confirmed_by_planner": false
}

【game_dna.md 格式】
- 用策划语言展开上述字段，每节 2~5 句
- core_loop 可用 ASCII 流程图
- 文末「待策划确认」：列出 2~5 个体验层面的选择题（A/B 方向），供策划拍板

【写作要求】
- 聚焦**体验与边界**，不写具体规则数值
- 信息不足标「待研究」，禁止编造
- 与 project.json 的 monetization/constraints 一致，冲突则标注并提问

【禁止】
- 不要写 UI 线框、配置表、接口
- 不要输出 R-xxx / P-xx、伪代码
- 不要写成功能设计说明书

【完成后】
更新 00-立项探索/{功能名}/README.md 进度表（立项探索·GameDNA定调 ✅）

请直接写入 game_dna.json、game_dna.md，并更新 README。
```

---

---

---

## 输入内容示例

> 说明如何填写占位符与 @ 引用。**勿与上方「提示词正文」一并复制**。路径均相对于 `GDD SKILL/` 根。

### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | {你的工作包名称} |

### Cursor 中 @ 引用

```
@产出/{功能名}/00-立项探索/{功能名}/project.json
```

### 策划补充说明（可选）

```
project.json 已确认后再跑本步。
```
