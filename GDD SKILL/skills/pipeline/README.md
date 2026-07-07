# pipeline — 文档管线阶段规范

> **与 `prompts/P0~P6/` 一一对应**：Prompt 是可复制的执行指令；本目录是各阶段的**格式铁律与门禁**。  
> **不含任何具体功能的业务内容**（业务在 `产出/{功能名}/`）。

---

## 何时读

| 你在跑… | 读 |
|---------|-----|
| P0 立项 | `p0-discovery/SKILL.md` |
| P1 定稿 01 | `p1-original-gdd/SKILL.md` |
| P2 写 02 | `p2-decompose/SKILL.md` |
| P3 写 03 | `p3-feature-spec/SKILL.md` |
| P4 填 04 | `p4-planner-fill/SKILL.md` |
| P5 compile | `p5-compile-verify/SKILL.md` |
| P6 开发管线 | `p6-pipeline/SKILL.md` |

**每个功能都要用**，与玩法类型无关。

---

## 目录清单

| 子目录 | 对应 Prompt | 产出 |
|--------|-------------|------|
| `p0-discovery/` | `prompts/P0/` | `00-立项探索/`（可选） |
| `p1-original-gdd/` | `prompts/P1/` | `01-原始策划案/` |
| `p2-decompose/` | `prompts/P2/` | `{spec_root}/02-需求拆解.md` |
| `p3-feature-spec/` | `prompts/P3/` | `{spec_root}/03-功能点梳理.md` |
| `p4-planner-fill/` | `prompts/P4/` | `04-待策划补充/` |
| `p5-compile-verify/` | `prompts/P5/` | `{feature_root}/开发文档/` |
| `p6-pipeline/` | `prompts/P6/` | server/client 四件套（仓库外） |

---

## 与 `frameworks/` 的区别

| | **pipeline/**（本目录） | **frameworks/** |
|--|-------------------------|-----------------|
| 管什么 | **怎么写 GDD 文档** | **某类玩法/系统的业务骨架** |
| 是否必选 | 跑 Part 2 **必选** | workflow **按需**勾选 |
| 例子 | 02 八维度、03 附录 A~E | Bracket 锦标赛 R-TB-xxx |

上级索引：[skills/README.md](../README.md)
