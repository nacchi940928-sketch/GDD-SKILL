# 单败淘汰赛对阵树 — 功能拆解（框架 Skill）

## 交付目标

Bracket **最小闭环**：报名 → 签位 → 阶段驱动 → 节点渲染 → 晋级。  
L2 `03-功能点梳理` 为程序主读；本表为**框架层排期索引**，不引用具体案例路径。

## 任务清单

| 优先级 | 框架任务 | 依赖 | 框架验收 |
|--------|----------|------|----------|
| 立项探索 | 阶段 Scheduler | — | T-TB-001 |
| 立项探索 | 报名 + 身份判定 | Scheduler | T-TB-001, T-TB-002 |
| 立项探索 | 签位 + 机器人补位 | 报名 | T-TB-003 |
| 立项探索 | Bracket 快照与协议族 | 签位 | GetBracketSnapshot |
| 原始策划案 | 对阵树 UI + 节点三态 | 快照 | ux 节点机 |
| 原始策划案 | 身份门控（战斗 vs 树） | 身份 | B-TB-001 |
| 原始策划案 | Phase Push + 客户端门控 | Scheduler | 阶段一致 |
| 需求拆解 | 扩展槽适配 | extension_slots | L2 用例 |

## 依赖关系

```text
Scheduler → Registration → BracketService → MatchService
                ↓
           UI + Push
                ↓
      ExtensionAdapter（可选）
```

## 完成定义

- 框架任务在 L2 03 中实例化为具体功能点文件
- 继承现网模块：L2 标注「复用」，不重复展开框架任务
