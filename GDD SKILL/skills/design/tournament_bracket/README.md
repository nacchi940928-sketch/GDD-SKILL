# tournament_bracket — 框架 Skill 说明

## 定位

本目录是 **单败淘汰赛对阵树的通用框架 Skill**，不是某个具体功能（如「竞技场高级赛」）的策划案。

| 本 Skill（L1 框架） | 项目实例（L2） |
|---------------------|----------------|
| 抽象模式、可配置槽位、规则编号 R-TB-xxx | `案例/{功能名}/` 下的 01~04 |
| 不绑定 P-xx、具体 UI 文案、签位表数值 | workflow `skill_configs` 填本项目参数 |
| 不定义竞猜/商店/货币等业务 | L2 delta 或独立 extension Skill |

## 框架覆盖的能力域

```text
报名 → 身份分流 → Bracket 组成 → 签位 → 阶段驱动 → 节点状态 → 晋级
         ↓
    [扩展槽] 竞猜 / 商店 / 自定义货币 …（仅声明挂点，规则在 L2）
```

## 实例化示例

竞技场高级赛：`workflows/arena.workflow.json` + `案例/竞技场高级赛/`  
（周练组、UTC0、16 强固定签位、竞猜币等均为 **L2 delta**）

## 文件职责

| 文件 | 内容 |
|------|------|
| meta.md | 框架 id、依赖、**抽象** config_schema |
| design.md | R-TB 通用规则（无项目名词） |
| ux.md | 界面架构模式、节点三态（无具体 Tab 名） |
| tech.md | 模块边界、BracketNode 骨架、接口族 |
| qa.md | T-TB/B-TB/E-TB 基线（无 P-xx） |
| feature.md | 框架层任务清单（无 L2 文件路径） |
