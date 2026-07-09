# 维度 Skill 路线图

> 跟踪 **需求拆解 拆解** 与 **功能点梳理 功能梳理** 各子域 Skill 的建设进度。  
> 更新流程见 [GDD-SKILL-更新规范.md](../GDD-SKILL-更新规范.md)。

**状态**：⬜ 待提炼 · 📝 代做 · 🟡 设计中 · ✅ 已启用

---

## 需求拆解 拆解维度

| skill_id | 维度 | Prompt | 状态 | 参考实例（L2） | 备注 |
|----------|------|--------|------|----------------|------|
| config_table | 配置表 | 需求拆解·数据源 | ✅ | （L2 待新建） | [tech.md](../tech/config_table/tech.md) |
| configurable_rules | 可配置规则 | 需求拆解·规则、待策划补充 | ✅ | （L2 待新建） | [tech.md](../tech/configurable_rules/tech.md) |
| implementation_data | 实现数据契约 | 需求拆解 收尾、P3、编译验收 | ✅ | （L2 待新建） | [tech.md](../tech/implementation_data/tech.md) |
| config_table_impact | 配置表变更影响 | 待建 | 📝 | `config/表关联关系.template.json` | [代做](config_table_impact.md) |
| decompose_rules | 规则 R-xx | 需求拆解·规则 | ⬜ | 待提供 | |
| decompose_state_machine | 状态机 | 需求拆解·状态机 | ⬜ | 待提供 | |
| decompose_protocol | 协议 | 需求拆解·数据源 | ⬜ | 待提供 | |
| decompose_boundary | 边界条件 | 需求拆解·边界条件 | ⬜ | 待提供 | |
| decompose_validation | 校验 V-xx | 需求拆解·校验规则 | ⬜ | 待提供 | |
| decompose_red_dot | 红点 | 需求拆解·红点 | ⬜ | 待提供 | |
| decompose_ui_flow | UI 跳转 | 需求拆解·UI交互 | ⬜ | 待提供 | |
| decompose_acceptance | 验收标准 | 需求拆解·验收标准 | ⬜ | 待提供 | |

---

## 功能点梳理 功能梳理

| skill_id | 关注点 | Prompt | 状态 | 参考实例（L2） | 备注 |
|----------|--------|--------|------|----------------|------|
| feature_spec_core | 03 总规范 | P3-* | 🟡 | （L2 待新建） | [p3-feature-spec-功能点梳理](../pipeline/p3-feature-spec-功能点梳理/SKILL.md) |
| feature_point_block | 功能点五段块 | 功能点梳理·功能点拆分 | ⬜ | 待提供 | |
| feature_module_split | 拆分粒度 | 功能点梳理·功能点拆分 | ⬜ | 待提供 | |
| feature_acceptance | 验收场景 | 功能点梳理·验收场景 | ⬜ | 待提供 | |
| feature_task_map | Feature 映射 | 功能点梳理·Feature对齐 | ⬜ | 待提供 | |
| feature_field_map | 字段映射 | 功能点梳理·字段映射 | ⬜ | 待提供 | |

---

## 变更记录

| 日期 | skill_id | 变更 |
|------|----------|------|
| 2026-07-06 | config_table | 从超级鸡马道具表问题抽象，晋升 L0 |
| 2026-07-06 | configurable_rules | 从超级鸡马计分审计抽象，晋升 L0 |
| 2026-07-06 | implementation_data | 从物理/摩擦遗漏问题抽象，晋升 L0 |
