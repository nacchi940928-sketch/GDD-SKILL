# P0-3 功能层级与 Skill 选型

规范：`skills/gdd/p0-discovery/SKILL.md`

## 提示词正文（复制以下内容）

```
请阅读我 @ 的：
- 00-立项探索/{功能名}/project.json
- 00-立项探索/{功能名}/game_dna.json（或 game_dna.md）
- skills/README.md
- skills/design/*/meta.md（按需 @ 相关框架）

功能名：{功能名}

【任务】
1. 判定本功能所属层级
2. 从已有 skills/ 推荐可复用的 L0/L1 框架
3. 列出需新建的 Skill 或 extension 槽位
4. 输出 workflow 配置草案（供策划确认，非最终文件）

【输出文件】
00-立项探索/{功能名}/skill选型.md

【skill选型.md 必须包含的章节】

## 1. 功能层级
| 层级 | 是否涉及 | 说明 |
（基础功能层 / 边缘系统层 / 核心玩法层 / 活动玩法层）

## 2. L1 框架推荐
| skill_id | 匹配度 | 覆盖什么 | 本项目 delta | 需读的框架文件 |
- 匹配度：完全匹配 / 部分匹配 / 不适用
- **只推荐 skills/ 中已存在的 id**，禁止虚构
- 若无匹配：写「待建 Skill」及建议抽象域（不写假 id）

## 3. L0 横切（默认）
列出 resolution_standard、interaction_feedback 等是否适用及备注。

## 4. Extension 槽位
若 L1 有 extension_slots（如 tournament_bracket 的 betting,shop）：
- 本项目启用哪些
- 每个槽位的业务含义（一句话，细节留 P0-4）

## 5. skill_configs 草案
按 meta.config_schema 列出每项：
| config 键 | 建议值 | 依据 | 待确认 |
- 未知值写「待策划确认」，禁止编造具体 cron/数值

## 6. workflow 草案（JSON 代码块）
```json
{
  "project": { ... },
  "selected_skills": [],
  "skill_configs": {},
  "feature_root": "案例/{功能名}"
}
```
注明：确认后可复制为 workflows/{项目}.workflow.json

## 7. 风险与待建 Skill 清单
- 框架盖不住的能力
- 建议后续抽象的 L1 Skill 名称（描述级，非强制 id）

【铁律】
- 先读 meta.config_schema 再填 config
- delta 写体验/业务差异，不写 R/P 编号
- 与 game_dna.excluded_systems 冲突的系统不得推荐

【禁止】
- 不要写 02/03 规格
- 不要编造不存在的 skill_id

【完成后】
更新 README.md 进度（P0-3 ✅）

请直接写入 skill选型.md 并更新 README。
```
