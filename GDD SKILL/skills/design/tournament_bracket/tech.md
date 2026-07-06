# 单败淘汰赛对阵树 — 技术规范（框架 Skill）

## 规范目标

模块边界、数据结构骨架、接口**族**。不含具体 proto 名、P-xx、项目服务类名。

## 服务 / 模块（框架）

| 模块 | 职责 |
|------|------|
| TournamentScheduler | 阶段切换 |
| RegistrationService | 报名 |
| BracketService | 签位、晋级写入 |
| MatchService | 对战（可继承现网或 L2 新建） |
| ExtensionAdapter | 扩展槽适配（betting/shop…，可选） |
| PushGateway | 阶段/节点推送 |

## BracketNode（骨架）

```json
{
  "matchId": 0,
  "round": 0,
  "matchIndex": 0,
  "slotLeft": 0,
  "slotRight": 0,
  "winnerId": 0,
  "status": "PENDING",
  "isRobotLeft": false,
  "isRobotRight": false,
  "parentMatchId": 0
}
```

**status**：`PENDING` | `IN_PROGRESS` | `COMPLETED`

**round**：从 1 递增；语义（十六强/八强…）由 `bracket_size` 推导，L2 可命名别名。

## 接口族（框架）

| 接口族 | 方向 | 用途 |
|--------|------|------|
| GetBracketSnapshot | C→S | 拉取对阵树 |
| GetPhaseInfo | C→S | 阶段 + 倒计时 |
| PhaseChangePush | S→C | 阶段变更 |
| BracketUpdatePush | S→C | 节点更新 |
| Extension* | C↔S | 扩展槽，L2 定义 |

## 实现约束

- 签位与报名同事务
- 阶段切换前：L2 定义上一轮结算完成条件
- Push：L2 选全量/增量

## 校验规则（框架）

| 编号 | 校验 |
|------|------|
| V-TB-001 | 扩展槽写操作：phase 允许 + 业务规则（L2） |
| V-TB-002 | 身份门控：参赛者才能进战斗接口 |
| V-TB-003 | 叶节点数 == bracket_size（含机器人） |

## 验收标准

- [ ] L2 协议与骨架字段一一映射
- [ ] 服务端权威，客户端不 sole source of truth
