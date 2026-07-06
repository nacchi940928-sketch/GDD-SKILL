# 7.2 Bracket 视觉排布（16 人单败）

## 涉及模块

| 模块 | 本功能点在此的表现 |
|------|-------------------|
| 对阵树界面（中央区域） | BracketView 渲染 15 节点 |
| BracketService | P-10 节点 round/matchIndex 映射视觉位置 |
| 竞猜 / 战报 | 节点下挂按钮（7.3） |

> **继承 tournament_bracket** 16 人单败倒金字塔布局

## 功能点

- **树形**：倒金字塔——上方/两侧为早期轮次，**最底中为冠军位**（带王冠）。
- **节点数**：与 **4.2 签位表** 一致 — 8 场 → 4 → 2 → 1。

| 层级 | 节点数 | 表现 |
|------|--------|------|
| 16 进 8 | 左右各 4 场，共 8 场 | 每节点：头像 + 名称；失败者灰/X |
| 8 进 4 | 左右各 2 场 | 未定显示 **?** |
| 4 进 2 | 左右各 1 场 | 同上 |
| 决赛 | 底部中央 1 格 | 冠军王冠；其下可挂「竞猜」文字按钮（精确场次入口） |

- **连线**：白/浅色线连接父子节点；已完成路径可高亮。
- **M1–M8 映射**：round=1, matchIndex=1..8 按 4.2 从左到右、从上到下排布于 16 进 8 层。
- **胜者上推**：视觉位置由 parentMatchId 关联；QF/SF/F 节点在胜者产生前显示 `?` 占位。

## 数据来源

| 读写 | 业务数据 | 程序字段 | 用途 |
|------|----------|----------|------|
| 读 | 对阵树快照 | P-10 | 全部节点 slot/status/score |
| 读 | 选手信息 | 【待程序补充】 | 头像、名称 |
| 读 | 当前轮次 | 【待程序补充】 | ? 占位 vs 竞猜按钮 |
| 读 | 已押注标记 | P-27 | 头像标签 |

## 怎么实现

### 通用

- 客户端**不做**签位计算，仅按 P-10 的 round + matchIndex 查表映射到预设坐标。
- 失败选手：灰化或 X 标识（沿用现网失败表现）。
- 未到轮次或 slot 为空：双方显示 `?`。

### 服务端

- P-10 下发完整 15 节点；BracketUpdatePush 携带变更节点（matchId、status、winnerId、score）。
- matchIndex 与 4.2 场次编号一一对应，保证多端渲染一致。

### 客户端

```
func layoutNode(node):
    pos = BRACKET_LAYOUT[node.round][node.matchIndex]
    if node.slotLeft == 0:  showPlaceholder("?", left)
    else:                   showPlayer(node.slotLeft, left)
    // slotRight 同理
    if node.status == COMPLETED:
        highlightPath(node.matchId → root)
    attachButtons(node)  // 7.3
```

- 决赛节点底部中央；冠军产生后显示王冠 icon。
- 支持横向滑动/缩放（若现网已有则保留）。

## 程序分工

| 事项 | 客户端 | 服务端 | 备注 |
| 布局坐标表 | ✓ 本地常量 | — | round×matchIndex |
| 节点数据 | ✓ 渲染 | ✓ P-10 | 15 节点 |
| 连线/高亮 | ✓ | — | 完成路径 |
| 签位一致性 | — | ✓ | 4.2 映射 |
| 节点按钮 | ✓ | ✓ status | 7.3 |
