# tournament_bracket — 框架 Skill 说明

## 定位

本目录是 **单败淘汰赛对阵树的通用框架 Skill**，不是某个具体功能的策划案。

| 本 Skill（L1 框架） | 项目实例（L2） |
|---------------------|----------------|
| 抽象模式、可配置槽位、规则编号 R-TB-xxx | `案例/{功能名}/` 下的 01~04 |
| 不绑定 P-xx、具体 UI 文案、签位表数值 | workflow `skill_configs` 填本项目参数 |
| 不定义 extension 槽内的具体业务 | L2 delta 写在 `案例/` |

上级索引：[skills/README.md](../../README.md)

## 框架覆盖的能力域

```text
报名 → 身份分流 → Bracket 组成 → 签位 → 阶段驱动 → 节点状态 → 晋级
         ↓
    [扩展槽 extension_slots] 自定义业务模块 …（仅挂点，规则在 L2）
```

## config_schema（抽象参数）

| 键 | 含义 | 默认 |
|----|------|------|
| `bracket_size` | 叶节点选手数（8/16/32…） | 16 |
| `registration_mode` | auto / manual | auto |
| `registration_schedule` | 自动报名触发描述 | 周期首日定时任务 |
| `contestant_rank_top_n` | 每个来源组前 N 名参赛 | 4 |
| `source_groups_per_bracket` | 合并为一对阵树的来源组数 | 4 |
| `robot_fill` | 选手不足是否机器人补位 | true |
| `identity_lock_duration` | 身份锁定时长 | 本期全程 |
| `period_structure` | 公示 + 战斗轮 + 结算 | 文字描述 |
| `extension_slots` | 扩展槽（逗号分隔） | 空 |

完整定义见 [meta.md](meta.md)。

## L2 实例化（不在本 Skill 内）

框架通过 workflow + `案例/{功能名}/` 实例化：

| 配置 | 位置 |
|------|------|
| `selected_skills` / `skill_configs` | `workflows/{项目}.workflow.json` |
| 业务 delta、P-xx、R-{缩写}-* | `案例/{功能名}/02~03` |

**禁止**将 L2 案例正文回写进本目录。

## 文件职责

| 文件 | 内容 |
|------|------|
| meta.md | 框架 id、依赖、config_schema |
| design.md | R-TB 通用规则（无项目名词） |
| ux.md | 界面架构模式、节点三态（无具体 Tab 名） |
| tech.md | 模块边界、BracketNode 骨架、接口族 |
| qa.md | T-TB/B-TB/E-TB 基线（无 P-xx） |
| feature.md | 框架层任务清单（无 L2 文件路径） |

## P2 继承约定

在 02 各维度正文中标注 `继承 R-TB-xxx`，仅写本项目与框架的差异。  
03 功能点须**自包含**业务细节，程序不依赖读本目录。
