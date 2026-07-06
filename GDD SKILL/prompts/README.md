# 提示词索引

> **路径规范**：所有产出写在 `案例/{功能名}/` 下，占位符 `{feature_root}` = `案例/{功能名}`。  
> 详见 [使用指导.md](../使用指导.md)。

## 提示词 vs Skill

| 类型 | 位置 | 用法 |
|------|------|------|
| **提示词** | `prompts/` | 复制「提示词正文」到 Agent 对话，直接执行 |
| **流程规范 Skill** | `skills/gdd/*/SKILL.md` | 格式铁律、检查清单（Agent 可读，人不逐条粘贴） |
| **框架 Skill** | `skills/design/*` 等 | L1 抽象模式；实例化见 `案例/` + `workflows/` |

详见 [skills/README.md](../skills/README.md)。

## 阶段索引

| 阶段 | 目录 | 规范 Skill | 说明 |
|------|------|------------|------|
| P0 立项探索（可选） | [P0/](P0/) | [p0-discovery](../skills/gdd/p0-discovery/SKILL.md) | 策划创作辅助：发现、定调、选型、大纲 |
| P1 原始策划案 | [P1/](P1/) | [p1-original-gdd](../skills/gdd/p1-original-gdd/SKILL.md) | 策划主文档定稿 |
| P2 需求拆解 | [P2/](P2/) | [p2-decompose](../skills/gdd/p2-decompose/SKILL.md) | 8 维度；可继承 L1 框架 |
| P3 功能点梳理 | [P3/](P3/) | [p3-feature-spec](../skills/gdd/p3-feature-spec/SKILL.md) | 程序主文档 |
| P4 待策划补充 | [P4/](P4/) | [p4-planner-fill](../skills/gdd/p4-planner-fill/SKILL.md) | 只填 L2 delta |
| P5 编译验收 | [P5/](P5/) | [p5-compile-verify](../skills/gdd/p5-compile-verify/SKILL.md) | 分轨 + compile + 验收 |
| P6 开发管线 | [P6/](P6/) | [p6-pipeline](../skills/gdd/p6-pipeline/SKILL.md) | server/client 四件套 |

## 全流程推荐顺序

```text
（可选）P0-1 → P0-2 → P0-3 → P0-4 → 策划确认 01 草稿
  ↓
P1-1 → P1-2 → 策划确认
  ↓
P2-DS → P2-R → P2-EX → P2-SM → P2-UI → P2-RD → P2-V → P2-T
  ↓
P3-1 → P3-2（可分批）→ P3-3 → P3-4 → P3-5 → P3-6
  ↓
P4-1 → 策划回填 04 → P4-2 验收 ──┐
  ↑                              │ 未通过则循环
  └──────────────────────────────┘
  ↓ 通过
P5-1 → P5-2 → P5-3 → 05 入库 → P6
```

## 用法

1. 打开对应 `.md` 文件
2. 复制 **「提示词正文」** 代码块内全文
3. 替换 `{功能名}`、`{feature_root}`（= `案例/{功能名}`）、`{skill_id}` 等占位符
4. `@` 引用 [使用指导.md](../使用指导.md) 第 4 节所列路径
5. 发送给 Agent

## L1 框架继承（P2/P3）

若 workflow 选了 `tournament_bracket` 等 L1 Skill：

- P2 各维度在 L1 骨架上**只写项目 delta**，标注 `继承 R-TB-xxx`
- P3 功能点**自包含**业务细节；L1 `feature.md` 仅作框架任务对照
- 项目参数从 `workflows/*.json` 的 `skill_configs` 读取，不硬编码进 Skill

## 编译

```bash
python tools/compile.py 案例/竞技场高级赛 --workflow workflows/arena.workflow.json
```

产出 `outputs/{功能名}/程序包.md | 测试包.md | 策划包.md`
