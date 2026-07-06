# 配置表关联关系（参考）

> **供未来 Skill `config_table_impact` 使用**（当前为代做，见 [skills/_backlog/config_table_impact.md](../../skills/_backlog/config_table_impact.md)）。  
> 策划与程序在此维护**全项目或跨功能**的表关联；单功能细表仍可在 `产出/{功能名}/02-…/数据源/` 登记。

| 文件 | 用途 |
|------|------|
| [表关联关系.template.json](表关联关系.template.json) | JSON 结构模板 |
| `表关联关系.json` | 正式数据（确认实现后创建，勿提交空壳） |

**维护原则**

- 每条 `relation` 须有 `type`、`target`、维护 `owner`
- 改现网表前：用变更表名在此 JSON 中查关联，再通知相关职能
- 与 GDD 的 P-xx 可用 `gdd_pxx` 边_optional 链接
