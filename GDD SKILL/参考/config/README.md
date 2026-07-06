# 配置表关联关系（参考）

> **编写格式**：L0 Skill [config_table](../../skills/tech/config_table/tech.md)（策划→Agent→程序三阶段）  
> **改表影响检索**：代做 Skill [config_table_impact](../../skills/_backlog/config_table_impact.md)（待实现）

| 文件 | 用途 |
|------|------|
| [表关联关系.template.json](表关联关系.template.json) | JSON 结构模板 |
| `表关联关系.json` | 正式数据（确认实现后创建，勿提交空壳） |

**维护原则**

- 每条 `relation` 须有 `type`、`target`、维护 `owner`
- 改现网表前：用变更表名在此 JSON 中查关联，再通知相关职能
- 与 GDD 的 P-xx 可用 `gdd_pxx` 边_optional 链接
