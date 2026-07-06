```yaml
id: interaction_feedback
name: 交互反馈规范
category: ux
description: 按钮、Toast、弹窗、奖励、错误反馈的横切行为规范。
dependencies:
  - resolution_standard

config_schema:
  - key: feedback_strength
    label: 反馈强度
    default: 标准
  - key: button_pressed_scale
    label: 按钮按下缩放
    default: 95%
  - key: toast_duration_ms
    label: Toast 默认时长(ms)
    default: "2000"
  - key: click_lock_ms
    label: 防连点锁定时长(ms)
    default: "300"
```
