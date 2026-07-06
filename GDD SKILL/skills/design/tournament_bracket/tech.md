# 锦标赛对阵树 — 技术规范（L1 基底）

## 规范目标

定义对阵树系统的模块划分、数据结构骨架与接口约定。L2 在 `02/数据源/` 填写具体 P-xx 与协议字段名。

## 适用范围

服务端权威；客户端读快照 + Push 增量更新。

## 服务 / 模块

| 模块 | 职责 |
|------|------|
| TournamentScheduler | 阶段切换定时任务 |
| RegistrationService | 自动/手动报名 |
| BracketService | 签位生成、晋级写入 |
| MatchService | 对战调度（可继承现网） |
| BettingService | 竞猜（optional） |
| PushGateway | PhaseChange / BracketUpdate |

## 数据结构 — BracketNode（骨架）

```json
{
  "matchId": 0,
  "round": 1,
  "matchIndex": 0,
  "slotLeft": 0,
  "slotRight": 0,
  "winnerId": 0,
  "status": "PENDING",
  "isRobotLeft": false,
  "isRobotRight": false,
  "scoreLeft": 0,
  "scoreRight": 0,
  "parentMatchId": 0
}
```

**status 枚举**：`PENDING` | `IN_PROGRESS` | `COMPLETED`

**round 映射**（bracket_size=16）：1=R16, 2=QF, 3=SF, 4=FINAL

## 接口约定（骨架）

| 接口 | 方向 | 说明 |
|------|------|------|
| GetBracketSnapshot | C→S | 拉取对阵树 |
| GetPhaseInfo | C→S | 当前阶段 + 倒计时 |
| PhaseChangePush | S→C | 阶段变更 |
| BracketUpdatePush | S→C | 节点状态/胜者更新 |

L2 在 `02/数据源/协议/` 展开完整 proto/message。

## 实现约束

- 签位生成与报名同一事务
- 阶段切换前校验上一轮全部 COMPLETED（或 L2 定义例外）
- Push 策略：L2 选择全量 vs 增量

## 校验规则（骨架）

| 编号 | 校验 |
|------|------|
| V-TB-001 | 押注请求：phase 允许 + 未重复押注 + 目标场次 IN_PROGRESS |
| V-TB-002 | 身份门控：CONTESTANT 才能进入战斗接口 |
| V-TB-003 | 签位：叶节点数 == bracket_size（含机器人） |

## 验收标准

- [ ] 模块边界清晰，L2 协议与 P-xx 对齐
- [ ] 状态枚举与 02/状态机 一致
- [ ] 服务端权威，客户端无 sole source of truth
