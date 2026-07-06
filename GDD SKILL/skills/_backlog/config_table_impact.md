# 代做记录：config_table_impact（配置表变更影响检索）

| 项 | 值 |
|----|-----|
| **skill_id**（拟） | `config_table_impact` |
| **层级**（拟） | L0 · `skills/tech/config_table_impact/` |
| **状态** | 📝 代做（未实现） |
| **提出** | 2026-07-06 |
| **须确认** | 维护者批准后才开始实现 |

---

## 1. 要解决什么问题

**对线上配置表进行调整**（改字段、改行、改引用、上下线表）时，单表改动常**级联影响**其他配置表、服务端加载逻辑、客户端读表与 GDD 中的 P-xx / 02 数据源。

本 Skill 目标：给定**被修改的表（或字段）**，自动**检索并列出所有关联配置表**及建议复查范围，避免漏改。

---

## 2. 使用场景（WHEN）

| 场景 | 触发方 |
|------|--------|
| 现网/预发配置表变更前 | 策划、程序 |
| 配置表结构评审 | 策划 |
| GDD 02/数据源与现网表对齐 | Agent + 程序 |
| 热更配置后的回归范围评估 | QA、程序 |

**不用于**：Part 2 从 docx 首次拆解（那是 P2-DS + [config_table](../tech/config_table/tech.md)）；本 Skill 面向**已有表关系网后的变更管理**。

**前置**：GDD 配置表须先按 [config_table](../tech/config_table/tech.md) 写成程序态单表；程序定稿后维护本目录 `config/表关联关系.json`。

---

## 3. 核心输入（策划 + 程序提供）

### 3.1 表关联关系库（必须）

由**策划与程序共同维护**，Skill **只读检索**，不自动推断业务关系。

建议路径（实现时二选一，维护者确认）：

```text
config/表关联关系.json          ← 全项目一张
或
产出/{功能名}/02-…/数据源/表关联关系.json  ← 按功能增量
```

### 3.2 关系条目格式（草案）

```json
{
  "version": "1.0",
  "tables": [
    {
      "table_id": "AB2_ChickenHorseItem",
      "name": "超级鸡马道具表",
      "owner": "策划",
      "relations": [
        {
          "type": "ref",
          "target": "AB2_ChickenHorseScore",
          "via": "behavior_id",
          "desc": "成就行为引用积分表"
        },
        {
          "type": "load_group",
          "target": "Const_ChickenHorse",
          "desc": "服务端同包加载"
        }
      ]
    }
  ]
}
```

| relation.type | 含义 |
|---------------|------|
| `ref` | 字段级外键/引用 |
| `load_group` | 同包加载、同版本发布 |
| `derive` | 派生/编译产出（如客户端表由服务端表生成） |
| `gdd_pxx` | 对应 GDD 字段映射 P-xx（可选，链到 02/数据源） |

### 3.3 变更事件（单次检索输入）

| 字段 | 说明 |
|------|------|
| `changed_table` | 被改表名 |
| `changed_fields` | 可选，字段列表 |
| `change_type` | `add` / `modify` / `delete` / `rename` |
| `env` | `prod` / `staging` / `dev` |

---

## 4. Skill 行为（WHAT · 拟实现）

```text
输入：changed_table + 表关联关系.json
  ↓
1. 在关系图中 BFS/DFS 展开 direct + indirect 关联表
2. 标注每条边的 type 与维护 owner（策划/程序）
3. 若存在 gdd_pxx 边，列出 产出/ 下对应 P-xx 与 02/03 文件路径
4. 输出《配置表变更影响报告》
  ↓
输出：影响表清单 + 建议复查 GDD 路径 + 建议通知职能
```

### 4.1 输出报告模板（拟）

```markdown
# 配置表变更影响报告

> 变更表：{changed_table}
> 检索依据：{关系库路径} v{version}

## 直接关联（1 跳）
| 表 | 关系类型 | 说明 | 责任 |

## 间接关联（2+ 跳）
| 表 | 路径 | 说明 |

## GDD 建议复查
| P-xx / 文件 | 原因 |

## 建议动作
- [ ] 策划确认关联行/默认值
- [ ] 程序确认加载顺序与热更包
- [ ] 更新 02/数据源 若结构变更
```

---

## 5. 拟目录结构（实现后）

```text
skills/tech/config_table_impact/
├── README.md
├── meta.md              # config_schema: 关系库路径、最大展开深度
├── tech.md              # 检索算法、边类型语义
└── qa.md                # 变更后验收要点

tools/
└── config_table_impact.py   # 可选：读 JSON 输出报告

prompts/                   # 可选 Part 2 外挂
└── CFG-1-配置表影响检索.md
```

**不写入** `workflows/*.json` 的 `selected_skills`，除非维护者确认（本 Skill 为**运维/变更**向，非 GDD 拆解必选）。

---

## 6. 与现有 GDD 管线的关系

| 现有 | 本 Skill |
|------|----------|
| P2-DS 登记 P-xx、02/数据源 | 现网改表后**反向**查哪些 P-xx / 表要同步 |
| 04-02 配置数值（策划填） | 变更影响报告可指向 04 待填项 |
| compile.py | 无直接依赖；结构大变后仍须重跑 compile |

---

## 7. 待维护者确认项

| # | 问题 | 选项 |
|---|------|------|
| C-01 | 关系库放 `config/` 还是各 `产出/`？ | 全局 / 按功能 / 混合 |
| C-02 | 是否做 CLI 工具还是仅 Agent + Prompt？ | tools / Prompt only |
| C-03 | 是否与现网配置仓库（Git/Excel）对接？ | 手动 JSON / 自动同步 |
| C-04 | 最大关联展开深度 | 默认 3 跳？ |

---

## 8. 实现检查清单（晋升前）

- [ ] 维护者确认 C-01~C-04
- [ ] 至少一份真实 `表关联关系.json` 样例（可先超级鸡马 3 张表）
- [ ] `skills/tech/config_table_impact/` 骨架 + meta.md
- [ ] Prompt 或 `tools/config_table_impact.py` 可跑通一次
- [ ] 从 `_backlog/` 移除或标 ✅ 已晋升
- [ ] 更新 [skills/README.md](../README.md) 已内置表

---

## 9. 关联示例（超级鸡马 · 待程序/策划补全）

| 表 | 拟关联 |
|----|--------|
| AB2_ChickenHorseItem | ↔ Const、AB2_ChickenHorseScore（too_easy 权重）、地图表 |
| AB2_ChickenHorseScore | ↔ 单轮结算逻辑、P-44 |
| AB2_ChickenHorseLv | ↔ 对局结算、P-45~P-46 |

> 正式边数据**不在本代做记录内填实**；实现时在关系库 JSON 中维护。
