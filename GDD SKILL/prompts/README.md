# 提示词总索引

> **路径规范**：`{feature_root}` = `产出/{功能名}`。详见 [使用指导.md](../使用指导.md)。

---

## 两部分 Prompt 体系

| 部分 | 目录 | 定位 | 索引 |
|------|------|------|------|
| **Part 1 策划辅助** | [P0/](P0/) | 帮策划**写**案（可选） | [P0/README.md](P0/README.md) |
| **Part 2 规格交付** | [P1/](P1/) ~ [P6/](P6/) | 将 01 **拆解**为程序/AI 可执行 GDD（**工作重点**） | **[规格交付库.md](规格交付库.md)** |

```text
Part 1（可选）              Part 2（核心）
P0 → 01 草稿        →    P1 定稿 → P2 八维度 → P3 功能点 → P4~P6 交付
                              ↑
                    策划 docx 可直接从 P1 进入
```

**Part 2 交付目标**：无论哪位策划的 01，经统一 Prompt 库产出规范一致的 `02 + 03`。

> **边界**：Prompt 只描述**文档规范**（格式、路径、编号）；具体业务在 `案例/`。`skills/` 变更须维护者确认，AI 跑管线时不得修改。

---

## Part 2 快速入口

| 你要做什么 | 打开 |
|------------|------|
| 了解完整规范、编号、门禁 | **[规格交付库.md](规格交付库.md)** |
| 复制公共头块 | [_shared/Part2-公共头.md](_shared/Part2-公共头.md) |
| P1 入口 | [P1/README.md](P1/README.md) |
| P2 八维度拆解 | [P2/README.md](P2/README.md) |
| P3 功能点梳理 | [P3/README.md](P3/README.md) |
| P4 待补充 | [P4/README.md](P4/README.md) |
| P5 编译验收 | [P5/README.md](P5/README.md) |
| P6 开发管线 | [P6/README.md](P6/README.md) |

> **P1~P6 共 23 个提示词正文**均已统一 Part 2 六段式结构。

---

## Part 2 阶段索引

| 阶段 | 提示词数 | 规范 Skill | 说明 |
|------|----------|------------|------|
| P1 入口 | 2 | [p1-original-gdd](../skills/gdd/p1-original-gdd/SKILL.md) | docx → 01 定稿 |
| **P2 需求拆解** | **8** | [p2-decompose](../skills/gdd/p2-decompose/SKILL.md) | **核心：八维度编号化** |
| **P3 功能点** | **6** | [p3-feature-spec](../skills/gdd/p3-feature-spec/SKILL.md) | **核心：程序主文档** |
| P4 待补充 | 2 | [p4-planner-fill](../skills/gdd/p4-planner-fill/SKILL.md) | 策划回填 delta |
| P5 编译验收 | 4 | [p5-compile-verify](../skills/gdd/p5-compile-verify/SKILL.md) | compile + 验收 + **执行日志** |
| P6 开发管线 | 3 | [p6-pipeline](../skills/gdd/p6-pipeline/SKILL.md) | server/client 四件套 |

## Part 2 推荐顺序

```text
P1-1 → P1-2 → 策划确认 01
  ↓
P2-DS → P2-R → P2-EX → P2-SM → P2-UI → P2-RD → P2-V → P2-T
  ↓
P3-1 → P3-2（可分批）→ P3-3 → P3-4 → P3-5 → P3-6
  ↓
P4-1 → 策划回填 04 → P4-2 验收 ──┐
  ↑                              │ 未通过
  └──────────────────────────────┘
  ↓
P5-1 → P5-2 → P5-3 → P5-4 → P6
```

## 用法

1. 打开 [规格交付库.md](规格交付库.md) 确认本步门禁与 @ 引用
2. 打开对应 `P1~P6/*.md`，复制「提示词正文」
3. 替换 `{功能名}`、`{feature_root}`、`{功能缩写}`、`{skill_id}`、`{项目}`
4. `@` 引用必读输入文件
5. 检查产出落在 `{feature_root}/` 正确子目录

## 编译

```bash
python tools/compile.py 产出/{功能名} --workflow workflows/{项目}.workflow.json
```

产出 `outputs/{功能名}/程序包.md | 测试包.md | 策划包.md`
