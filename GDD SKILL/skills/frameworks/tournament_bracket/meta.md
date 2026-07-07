```yaml
id: tournament_bracket
name: 单败淘汰赛对阵树（框架）
category: design
description: >
  通用框架：报名、身份分流、Bracket 组成、签位、阶段驱动、节点状态机、晋级。
  不含具体项目业务（extension 槽内规则由 L2 或 extension Skill 实例化。
dependencies:
  - interaction_feedback
  - resolution_standard

config_schema:
  - key: bracket_size
    label: 叶节点选手数（8/16/32…）
    default: "16"
  - key: registration_mode
    label: 报名方式（auto / manual）
    default: "auto"
  - key: registration_schedule
    label: 自动报名触发描述（cron 或周期事件）
    default: "周期首日定时任务"
  - key: contestant_rank_top_n
    label: 每个来源组前 N 名视为参赛者
    default: "4"
  - key: source_groups_per_bracket
    label: 合并为一对阵树的来源组数量
    default: "4"
  - key: robot_fill
    label: 选手不足时是否机器人补位
    default: "true"
  - key: identity_lock_duration
    label: 身份锁定时长（天或至本期结束）
    default: "本期全程"
  - key: period_structure
    label: 期次结构（公示 + N 轮战斗 + 结算，文字描述）
    default: "公示 + 多轮战斗 + 结算"
  - key: extension_slots
    label: 启用的扩展槽（逗号分隔，如 betting,shop）
    default: ""
```
