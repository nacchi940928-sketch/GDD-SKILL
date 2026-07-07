# P6 开发管线 — Prompt 库

> **Part 2 下游阶段**：基于 03 + 程序包，生成 server/client design 四件套，供 AI 自动开发。  
> 完整规范：[规格交付库.md](../规格交付库.md) · Skill：[p6-pipeline](../../skills/pipeline/p6-pipeline/SKILL.md)

---

## 前置门禁

- P5-3 策划验收通过
- `{feature_root}/开发文档/程序包.md` 已生成
- workflow 中 `selected_skills` 与 `skill_configs` 已定稿

---

## 执行顺序

```text
P6-3 继承现网 delta 清单（建议先做，可选）
  → P6-1 后端四件套
  → 后端 proto 交付
  → P6-2 前端四件套
```

---

## Prompt 清单

| ID | 文件 | 产出 |
|----|------|------|
| P6-3 | [P6-3-增量开发继承现网.md](P6-3-增量开发继承现网.md) | `{feature_root}/继承现网-delta清单.md` |
| P6-1 | [P6-1-后端管线编排.md](P6-1-后端管线编排.md) | `server/design/{功能名}/` 四件套 |
| P6-2 | [P6-2-前端管线编排.md](P6-2-前端管线编排.md) | `client/design/{功能名}/` 四件套 |

---

## 四件套结构（P6-1 / P6-2 共用）

```text
{server|client}/design/{功能名}/
  ├── 需求文档.md
  ├── 设计方案.md
  ├── 开发方案.md
  └── 管线编排.md
```

---

## 统一 @ 引用

**P6-1**：
```
@ {feature_root}/02-03需求拆解与功能点梳理/03-功能点梳理.md（各章 + 附录 A/D/E）
@ {feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md（§5/§6/§2）
@ {feature_root}/开发文档/程序包.md
@ workflows/{项目}.workflow.json
@ skills/frameworks/{skill_id}/tech.md、feature.md
```

**P6-2**：
```
@ {feature_root}/02-03需求拆解与功能点梳理/03-功能点梳理.md
@ {feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md（§4 UI、§2 状态机、§6.1 红点）
@ {feature_root}/开发文档/程序包.md
@ {feature_root}/04-…/01-字段命名.md（或 server proto）
@ skills/tech/resolution_standard/、skills/ux/interaction_feedback/
```

**P6-3**：
```
@ {feature_root}/02-03需求拆解与功能点梳理/03-功能点梳理.md
@ {feature_root}/01-…/原始策划案.md
@ server|client/design/{功能名}/（草稿，如有）
```

---

## 铁律

- 以 **03 + 程序包** 为开发输入
- 继承现网：复用只写对接点，改动只写 delta
- 每个管线任务须标注 P-xx 与对应 03 章节

---

## 完成标准

- [ ] 03 每个需开发的功能点在四件套/管线编排中有任务
- [ ] P6-3 与 03「涉及模块」表一致
- [ ] 前端协议字段与 server 04-01 / proto 一致
