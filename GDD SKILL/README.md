# GDD SKILL 子项目

策划工作流主内容目录。仓库根 [README.md](../README.md) 为项目组评审入口。

## 快速导航

| 文档 | 用途 |
|------|------|
| [策划工作流.md](策划工作流.md) | 五阶段定义 + 检查清单 |
| [prompts/README.md](prompts/README.md) | 22 个可复制提示词索引 |
| [skills/README.md](skills/README.md) | Skill 知识库（L0/L1 框架 + 流程规范） |
| [docs/PromptMerge规划.md](docs/PromptMerge规划.md) | 架构设计与 Vibe Studio 融合 |
| [templates/转换规范.md](templates/转换规范.md) | 01→03 转换铁律 |

## 目录一览

```text
prompts/          提示词（复制粘贴到 Agent）
skills/           规范与框架知识（Agent 读，人不逐条粘贴）
  gdd/            P1~P6 阶段规范
  design/         L1 系统框架（如 tournament_bracket）
  tech/ ux/       L0 横切基底
templates/        01~04 阶段文档模板
workflows/        项目配置（selected_skills + skill_configs）
tools/            compile.py、docx_extract.py 等
案例/             L2 完整样例（竞技场高级赛）
outputs/          编译产出（勿手改）
```

## 三层基底

| 层级 | 位置 | 内容 |
|------|------|------|
| L0 | `skills/tech/*`、`skills/ux/*` | 分辨率、交互反馈 |
| L1 | `skills/design/*` | **框架 Skill**：抽象模式 + config 槽位 |
| L2 | `案例/{功能}/` + `workflows/*.json` | 项目实例：业务 delta + skill_configs |

## 常用命令

```bash
# 编译 02+03 → 程序包/测试包/策划包
python tools/compile.py 案例/竞技场高级赛 --workflow workflows/arena.workflow.json
```

产出：`outputs/竞技场高级赛/程序包.md | 测试包.md | 策划包.md`

## 参考案例

[案例/竞技场高级赛/](案例/竞技场高级赛/) — 继承 `tournament_bracket` 框架的首个 L2 实例。  
对照 [skills/design/tournament_bracket/](skills/design/tournament_bracket/) 理解框架与实例差异。
