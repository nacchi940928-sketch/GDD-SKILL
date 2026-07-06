# 维度 Skill 路线图

> 跟踪 **P2 拆解** 与 **P3 功能梳理** 各子域 Skill 的建设进度。  
> 更新流程见 [GDD-SKILL-更新规范.md](../GDD-SKILL-更新规范.md)。

**状态**：⬜ 待提炼 · 📝 代做 · 🟡 设计中 · ✅ 已启用

---

## P2 拆解维度

| skill_id | 维度 | Prompt | 状态 | 参考实例（L2） | 备注 |
|----------|------|--------|------|----------------|------|
| config_table | 配置表 | P2-DS | ✅ | `产出/超级鸡马/02-…/AB2_ChickenHorseItem.md` | [tech.md](../tech/config_table/tech.md) |
| configurable_rules | 可配置规则 | P2-R、P4 | ✅ | `产出/超级鸡马/02-…/计分全量审计.md` | [tech.md](../tech/configurable_rules/tech.md) |
| config_table_impact | 配置表变更影响 | 待建 | 📝 | `config/表关联关系.template.json` | [代做](config_table_impact.md) |
| decompose_rules | 规则 R-xx | P2-R | ⬜ | 待提供 | |
| decompose_state_machine | 状态机 | P2-SM | ⬜ | 待提供 | 竞技场对阵树可作候选 |
| decompose_protocol | 协议 | P2-DS | ⬜ | `产出/超级鸡马/02-…/协议/` | 与 DS 分文件 |
| decompose_boundary | 边界条件 | P2-EX | ⬜ | 待提供 | |
| decompose_validation | 校验 V-xx | P2-V | ⬜ | 待提供 | |
| decompose_red_dot | 红点 | P2-RD | ⬜ | 待提供 | |
| decompose_ui_flow | UI 跳转 | P2-UI | ⬜ | 待提供 | |
| decompose_acceptance | 验收标准 | P2-T | ⬜ | 待提供 | |

---

## P3 功能梳理

| skill_id | 关注点 | Prompt | 状态 | 参考实例（L2） | 备注 |
|----------|--------|--------|------|----------------|------|
| feature_spec_core | 03 总规范 | P3-* | 🟡 | `产出/超级鸡马/03-…/0-阅读说明.md` | [p3-feature-spec](../gdd/p3-feature-spec/SKILL.md) |
| feature_point_block | 功能点五段块 | P3-2 | ⬜ | `产出/超级鸡马/03-…/功能点/` | |
| feature_module_split | 拆分粒度 | P3-2 | ⬜ | 待提供 | |
| feature_acceptance | 验收场景 | P3-4 | ⬜ | `产出/超级鸡马/03-…/验收场景.md` | |
| feature_task_map | Feature 映射 | P3-6 | ⬜ | `产出/超级鸡马/03-…/Feature任务映射.md` | |
| feature_field_map | 字段映射 | P3-3 | ⬜ | `产出/超级鸡马/03-…/字段映射.md` | |

---

## 变更记录

| 日期 | skill_id | 变更 |
|------|----------|------|
| 2026-07-06 | config_table | 从超级鸡马道具表问题抽象，晋升 L0 |
| 2026-07-06 | configurable_rules | 从超级鸡马计分审计抽象，晋升 L0 |
