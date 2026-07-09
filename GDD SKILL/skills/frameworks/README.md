# frameworks — L1 玩法 / 系统框架

> **可复用的业务模式模板**（如单败 Bracket 锦标赛）。  
> **不是**文档格式规范（那是 `pipeline/`）；**不是**具体项目策划案（那是 `产出/`）。

---

## 何时读

1. `workflows/{项目}.workflow.json` 的 `selected_skills` **包含**某 `skill_id`
2. 需求拆解/功能点梳理 Prompt 要求 `@ skills/frameworks/{skill_id}/design.md` 等
3. 在 02 中写「继承 R-TB-xxx，本项目 delta …」

**未选中的 framework 不必读**（如超级鸡马未选任何 L1 framework）。

---

## 当前框架

| skill_id | 目录 | 适用玩法 |
|----------|------|----------|
| `tournament_bracket` | [tournament_bracket/](tournament_bracket/) | 来源分组 → 报名 → 签位 → 单败 Bracket → 结算 |

---

## 文件约定（每个 `{skill_id}/`）

| 文件 | 内容 |
|------|------|
| `README.md` | 框架边界、config 槽位、L2 实例化方式 |
| `meta.md` | id、dependencies、**config_schema** |
| `design.md` | 抽象业务规则（R-{框架缩写}-xxx） |
| `ux.md` / `tech.md` / `qa.md` / `feature.md` | 界面模式、模块边界、基线用例、任务索引 |

---

## 新建框架

1. 复制 `_template/` → `frameworks/{skill_id}/`
2. 维护者确认后写入 workflow `selected_skills`
3. L2 只在 `产出/` 写 delta，**禁止**把案例正文回写本目录

上级索引：[skills/README.md](../README.md)
