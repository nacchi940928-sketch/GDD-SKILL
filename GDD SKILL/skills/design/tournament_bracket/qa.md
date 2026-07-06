# 单败淘汰赛对阵树 — 测试规范（框架 Skill）

## 规范目标

框架层测试基线。L2 在 `02/验收标准`、`03/验收场景` 展开项目用例并映射本编号。

## 测试范围

- 报名与身份
- 签位与机器人补位
- 阶段切换
- 节点状态与晋级
- 身份门控
- 扩展槽（若 extension_slots 非空）

## 测试用例

### T-TB-001 自动报名

**前置**：registration_mode=auto，到达 registration_schedule  
**验证**：身份写入正确；Bracket 快照生成  

### T-TB-002 身份锁定

**前置**：identity_lock_duration 生效期内已报名  
**步骤**：触发排名变化类事件  
**验证**：身份字段不变  

### T-TB-003 签位固定

**前置**：bracket_size 配置值，部分空缺  
**步骤**：robot_fill=true  
**验证**：叶节点数正确；与配置签位表一致  

### B-TB-001 观赛者进战斗

**前置**：role=SPECTATOR（若项目启用双身份）  
**验证**：门控拦截 + 提示  

### E-TB-001 签位失败回滚

**前置**：模拟签位异常  
**验证**：报名回滚；无脏快照  

## 自动化检查点

- Phase 枚举与 Scheduler 日志一致
- BracketNode.status 合法枚举
- COMPLETED 时 winnerId 有效

## 验收标准

- [ ] L2 用例映射 T-TB/B-TB/E-TB 或标注 N/A
