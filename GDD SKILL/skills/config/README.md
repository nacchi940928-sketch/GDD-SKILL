# 配置表关联关系（全项目）

> **编写格式**：L0 Skill [config_table](../skills/tech/config_table/tech.md)  
> **改表影响检索**：代做 [config_table_impact](../skills/_backlog/config_table_impact.md)

| 文件 | 用途 |
|------|------|
| [表关联关系.template.json](表关联关系.template.json) | JSON 结构模板 |
| `表关联关系.json` | 正式数据（确认实现后创建） |

**维护原则**

- 每条 `relation` 须有 `type`、`target`、维护 `owner`
- 改现网表前：用变更表名在此 JSON 中查关联
- 单功能配置表规格仍在 `产出/{功能名}/02-…/数据源/配置表/`
