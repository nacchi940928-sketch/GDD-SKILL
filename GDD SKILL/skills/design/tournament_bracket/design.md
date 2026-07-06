# 锦标赛对阵树 — 设计规范（L1 基底）

## 规范目标

定义**单败淘汰赛对阵树**的通用策划规则，适用于「周练定组 → 自动/手动报名 → 签位 → 多轮战斗 → 结算」类活动。

L2 项目实例（如竞技场高级赛）**只写与本文不同的 delta**，相同规则标注「继承 tournament_bracket」。

## 适用范围

- 16/8/32 人单败 Bracket（由 `bracket_size` 配置）
- 选手 vs 观众双身份分流
- 服务端权威阶段驱动 + 客户端门控
- 可选竞猜子系统（`enable_betting=true` 时启用，规则见项目 delta）

## 玩家流程

```text
[活动入口] → [活动展示/公示]
  ├── 选手 → [决斗/战斗界面]
  └── 观众 → [对阵树界面] →（可选）竞猜
```

## 核心规则

### R-TB-001 报名模式

| registration_mode | 行为 |
|-------------------|------|
| `auto` | 定时任务触发，无主动报名 UI/接口 |
| `manual` | 玩家主动报名，有截止时间与资格校验 |

**自动报名（默认）**：
- 触发：`registration_cron`（如周一 UTC0）
- 读：玩家分组归属 + 组内排名
- 写：身份（选手/观众）、对阵树快照
- 失败：整事务回滚，签位与报名原子提交

### R-TB-002 身份判定

```
if rank in [1 .. contestant_top_n]:
    role = CONTESTANT
else:
    role = SPECTATOR
```

- 身份在 `identity_lock_days` 内不变（除非 GM 审计修改）
- 下一周期重新报名时覆盖

### R-TB-003 赛区/Bracket 组成

- 每 `groups_per_bracket` 个来源组合并为一个独立 Bracket
- 各 Bracket 独立淘汰赛、独立冠军、独立竞猜池（若启用）
- 规模：`bracket_size` 叶节点选手 + 对应观众池

### R-TB-004 签位生成

- Bracket 签位表**固定**（不可随机），由配置或常量表定义
- 报名成功后生成签位 → 写叶节点 → `robot_fill=true` 时不足补机器人
- 签位失败回滚报名事务

### R-TB-005 对战与晋级

- 单败：胜者写入父节点 slotLeft/slotRight
- 轮次顺序：R16 → QF → SF → FINAL（随 `bracket_size` 缩放）
- **继承现网战斗模块**的项目：只写对接点，不重写战斗判定逻辑

### R-TB-006 阶段日程

由 `phase_schedule` 实例化，典型结构：

| 阶段 | 选手 | 观众 |
|------|------|------|
| ANNOUNCE（公示） | 预览对阵，不可战斗 | 预览，不可竞猜 |
| BATTLE_n（各轮） | 可战斗 | 可竞猜（若启用） |
| SETTLE（结算） | 发奖、积分转化 | 同左 |

每日 UTC0（或可配置 tick）切换阶段；服务端权威，客户端读倒计时 + 本地门控。

## 数据模型（策划视角）

| 概念 | 说明 |
|------|------|
| BracketSnapshot | 完整对阵树，含所有节点 |
| BracketNode | matchId, round, slotLeft/Right, winnerId, status |
| PlayerRole | CONTESTANT / SPECTATOR |
| Phase | ANNOUNCE / BATTLE_* / SETTLE |

字段编号 P-xx 在 L2 `02/数据源/字段映射索引.md` 登记，L1 不绑定具体 P 编号。

## 边界与异常

| 编号 | 场景 | 处理 |
|------|------|------|
| EX-TB-001 | 定时任务失败 | 需 L2 定义重试策略 |
| EX-TB-002 | 签位生成失败 | 回滚报名，告警 |
| EX-TB-003 | 战斗超时未结算 | 需 L2 定义超时判负/延期 |
| PRE-TB-001 | 玩家未在来源组 | 不参与本期 |
| LIM-TB-001 | 身份锁定期内 | 不因游戏内事件改变身份 |

## 验收标准

- [ ] 自动/手动报名与 `registration_mode` 一致
- [ ] 身份判定符合 `contestant_top_n`，锁定期内不变
- [ ] 签位固定、机器人补位符合 `robot_fill`
- [ ] 阶段切换服务端权威，客户端门控与阶段一致
- [ ] 节点状态 PENDING → IN_PROGRESS → COMPLETED 无歧义
- [ ] L2 delta 与 workflow `skill_configs` 数值一致
