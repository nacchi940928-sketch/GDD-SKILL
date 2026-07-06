# 交互反馈 — 技术规范（L0 横切）

## 规范目标

客户端统一反馈组件接口，避免各模块自建 Toast/按钮态。

## 实现约束

- 全局 ClickLock 服务，duration = `click_lock_ms`
- Button 组件内置 Normal/Pressed/Disabled 三态
- ToastManager：单例队列或合并策略

## 验收标准

- [ ] 所有可点击 UI 走统一 Button 组件或等价封装
- [ ] Disabled 态 pointer-events: none
