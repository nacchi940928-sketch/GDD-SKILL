# pipeline — 文档管线阶段规范

> **与 `prompts/` 各阶段目录一一对应**：Prompt 是可复制的执行指令；本目录是各阶段的**格式铁律与门禁**。

**子目录名已含中文**（如 `p2-decompose-需求拆解/`），与 `prompts/` 各阶段一一对应。

---

## 阶段对照表

| 阶段 | **中文名** | Skill 目录 | 对应 Prompt | 产出目录 |
|------|-----------|------------|-------------|----------|
| Part 1 | **立项探索** | `p0-discovery-立项探索/` | `prompts/立项探索/` | `00-立项探索/`（可选） |
| P1 | **原始策划案** | `p1-original-gdd-原始策划案/` | `prompts/原始策划案/` | `01-原始策划案/` |
| P2 | **需求拆解** | `p2-decompose-需求拆解/` | `prompts/需求拆解/` | `02-需求拆解.md` |
| P3 | **功能点梳理** | `p3-feature-spec-功能点梳理/` | `prompts/功能点梳理/` | `03-功能点梳理.md` |
| P4 | **待策划补充** | `p4-planner-fill-待策划补充/` | `prompts/待策划补充/` | `04-待策划补充/` |
| P5 | **编译验收** | `p5-compile-verify-编译验收/` | `prompts/编译验收/` | `开发文档/` 三包 |
| P6 | **开发管线** | `p6-pipeline-开发管线/` | `prompts/开发管线/` | server/client 四件套 |
| P7 | **规范反哺**（**手动 · 维护者**） | `p7-norm-feedback-规范反哺/` | `prompts/规范反哺/` | `规范反哺报告.md`（**不**进 gdd-decompose） |

`{spec_root}` = `产出/{功能名}/02-03需求拆解与功能点梳理`

---

## 何时读

| 你在跑… | 读 |
|---------|-----|
| 立项探索 | [p0-discovery-立项探索/SKILL.md](p0-discovery-立项探索/SKILL.md) |
| 原始策划案（01 定稿） | [p1-original-gdd-原始策划案/SKILL.md](p1-original-gdd-原始策划案/SKILL.md) |
| 需求拆解（02） | [p2-decompose-需求拆解/SKILL.md](p2-decompose-需求拆解/SKILL.md) |
| 功能点梳理（03） | [p3-feature-spec-功能点梳理/SKILL.md](p3-feature-spec-功能点梳理/SKILL.md) |
| 待策划补充（04） | [p4-planner-fill-待策划补充/SKILL.md](p4-planner-fill-待策划补充/SKILL.md) |
| 编译验收 | [p5-compile-verify-编译验收/SKILL.md](p5-compile-verify-编译验收/SKILL.md) |
| 开发管线 | [p6-pipeline-开发管线/SKILL.md](p6-pipeline-开发管线/SKILL.md) |
| **规范反哺**（手动，非自动） | [p7-norm-feedback-规范反哺/SKILL.md](p7-norm-feedback-规范反哺/SKILL.md) |

**每个功能都要用**（立项探索、规范反哺除外），与玩法类型无关。

---

## 与 `frameworks/` 的区别

| | **pipeline/**（本目录） | **frameworks/** |
|--|-------------------------|-----------------|
| 管什么 | **怎么写 GDD 文档** | **某类玩法/系统的业务骨架** |
| 是否必选 | 跑 Part 2 **必选** | workflow **按需**勾选 |
| 例子 | 02 九步、03 附录 A~E | Bracket 锦标赛 R-TB-xxx |

上级索引：[skills/README.md](../README.md)
