```yaml
id: tournament_bracket
name: 锦标赛对阵树系统
category: design
description: 单败淘汰赛对阵树基底：报名/身份、签位、节点状态机、阶段流转、机器人补位。项目实例只写 delta。
dependencies:
  - interaction_feedback
  - resolution_standard

config_schema:
  - key: bracket_size
    label: Bracket 规模（叶节点选手数）
    default: "16"
  - key: registration_mode
    label: 报名方式
    default: "auto"
  - key: registration_cron
    label: 自动报名触发（cron/描述）
    default: "周一 UTC0"
  - key: contestant_top_n
    label: 每组前 N 名为选手
    default: "4"
  - key: groups_per_bracket
    label: 合并为一对阵树的周练组数
    default: "4"
  - key: robot_fill
    label: 不足时机器人补位
    default: "true"
  - key: identity_lock_days
    label: 身份锁定期（天）
    default: "7"
  - key: enable_betting
    label: 是否启用竞猜子系统
    default: "false"
  - key: phase_schedule
    label: 阶段日程（announce + N 轮战斗 + settle）
    default: "公示1天 + 战斗4轮 + 结算2天"
```
