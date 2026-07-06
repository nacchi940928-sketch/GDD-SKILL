```yaml
id: resolution_standard
name: 分辨率与适配规范
category: tech
description: 全项目唯一画布与屏幕适配策略（9:20 fit 留黑边、安全区、布局锚点）。
dependencies: []

config_schema:
  - key: orientation
    label: 屏幕方向
    default: 竖屏
  - key: reference_resolution
    label: 设计基准分辨率
    default: 1080x2340
  - key: scale_mode
    label: 缩放模式
    default: 等比包含留黑边（fit）
  - key: long_screen_policy
    label: 长屏策略
    default: 宽度顶满，上下留纯黑边
  - key: wide_screen_policy
    label: 宽扁屏策略
    default: 高度顶满，左右留纯黑边
  - key: letterbox_color
    label: 留黑边颜色
    default: 纯黑（#000000）
  - key: layout_anchor_policy
    label: 画布内布局
    default: 顶栏贴顶、底栏贴底、中间填满（stretch_center）
  - key: safe_area_fallback
    label: 安全区回退
    default: 顶44pt 底34pt（设计坐标等效）
  - key: target_fps
    label: 目标帧率
    default: 60fps
```
