# 单败淘汰赛对阵树 — 设计规范（框架 Skill）

## 规范目标

提供**可复用的锦标赛 Bracket 策划框架**：任意「来源分组 → 报名 → 签位 → 多轮单败 → 结算」类玩法，均可继承本 Skill，在 L2 只写业务 delta。

**本文件不包含**：具体项目名称、来源组/分区名词、固定签位表数值、extension 槽内业务规则、P-xx 字段。

## 适用范围

- 单败 Bracket，`bracket_size` 可配置（8/16/32…）
- 可选**双身份**（参赛者 / 观赛者）或 L2 定义为单一身份
- 服务端权威**阶段机** + 客户端门控
- `extension_slots` 声明扩展能力挂点，**不定义**扩展业务规则

## 玩家流程（框架）

```text
[活动入口] → [公示/活动展示]
  ├── 参赛者 → [战斗主界面]
  └── 观赛者 → [对阵树主界面] →（可选扩展槽）
```

## 核心规则

### R-TB-001 报名模式

| registration_mode | 行为 |
|-------------------|------|
| `auto` | 按 `registration_schedule` 触发；无主动报名 UI/接口 |
| `manual` | 玩家主动报名；截止时间与资格由 L2 定义 |

**自动报名框架行为**：
- 触发：`registration_schedule`
- 读：来源组归属 + 组内排名（字段名 L2 定义）
- 写：身份、Bracket 快照
- 签位与报名**同一事务**；失败回滚

### R-TB-002 身份判定（双身份模式）

```
if rank in [1 .. contestant_rank_top_n]:
    role = CONTESTANT
else:
    role = SPECTATOR
```

- 身份在 `identity_lock_duration` 内不变（GM 修改需 L2 定义审计）
- 下一周期重新报名时覆盖

> 若项目无观赛者，L2 标注「R-TB-002 N/A，全员 CONTESTANT」。

### R-TB-003 Bracket 组成

- 每 `source_groups_per_bracket` 个**来源组**合并为一个独立 Bracket
- 各 Bracket 独立淘汰赛、独立冠军
- 规模：叶节点 `bracket_size` 名参赛者 + L2 定义的观赛者池（若有）

**来源组**：L2 定义（按排名/公会/服务器等分组），框架不绑定具体算法。

### R-TB-004 签位生成

- 签位表由**配置/常量表**驱动，**不可运行时随机**
- 报名成功 → 写叶节点 → `robot_fill=true` 时不足补机器人
- 签位失败 → 回滚报名

签位算法（同组规避、种子保护等）：**L2 在 02 §3 规则说明 展开**。

### R-TB-005 对战与晋级

- 单败：胜者写入父节点
- 轮次数量由 `bracket_size` 决定（log2 规模）
- **战斗判定**：框架不定义；L2 标注「继承现网 {模块}」或「新建 MatchService」

### R-TB-006 阶段日程

由 `period_structure` 实例化，框架阶段枚举：

| 阶段 | 框架含义 |
|------|----------|
| ANNOUNCE | 公示；不可战斗 |
| BATTLE_* | 各战斗轮（数量 = f(bracket_size)） |
| SETTLE | 结算、发奖、扩展槽收尾（L2 定义） |

阶段切换：服务端权威；切换 tick 由 L2 定义（如 UTC0）。

## 扩展槽（框架挂点）

`extension_slots` 非空时，L2 在独立章节/SKill 定义规则，例如：

| 槽位 id | 框架约定 | 规则定义方 |
|---------|----------|------------|
| `betting` | 观赛者可选参与；与 BATTLE 轮次对齐 | L2 / 独立 Skill |
| `shop` | 结算后或期内兑换 | L2 |
| `custom_currency` | 期内代币与结算转化 | L2 |

框架**不包含**扩展槽的业务数值与 UI 文案。

## 数据模型（概念层）

| 概念 | 说明 |
|------|------|
| BracketSnapshot | 完整对阵树 |
| BracketNode | 单场比赛节点 |
| PlayerRole | CONTESTANT / SPECTATOR（可扩展） |
| Phase | ANNOUNCE / BATTLE_n / SETTLE |

字段编号、proto 名：**L2 在 02/数据源 登记**。

## 边界与异常（框架）

| 编号 | 场景 | 框架处理 |
|------|------|----------|
| EX-TB-001 | 定时任务失败 | L2 定义重试 |
| EX-TB-002 | 签位失败 | 回滚报名 |
| EX-TB-003 | 战斗超时未结算 | L2 定义判负/延期 |
| PRE-TB-001 | 无来源组资格 | 不参与本期 |
| LIM-TB-001 | 身份锁定期 | 不因局内事件改身份 |

## 验收标准（框架）

- [ ] registration_mode 行为与配置一致
- [ ] 身份判定符合 contestant_rank_top_n（若启用双身份）
- [ ] 签位非随机、robot_fill 行为正确
- [ ] 阶段切换服务端权威，客户端门控一致
- [ ] 节点三态无歧义（见 ux.md）
- [ ] L2 workflow skill_configs 与 02 规则数值一致
