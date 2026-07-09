# GDD Skill 更新规范

> **读者**：Skill 维护者、程序、策划负责人。  
> **目的**：用**已投入使用的真策划案**与**程序拆解成果**，逐步完善 Part 2 各维度 Skill 与 功能点梳理 功能梳理 Skill；避免 Skill 脱离实战或把 L2 业务写进框架。

---

## 1. 背景与目标

当前仓库有两类「知识」：

| 类型 | 位置 | 状态 |
|------|------|------|
| **阶段 Skill** | `skills/pipeline/pipeline 各阶段-*/SKILL.md` | 有骨架，随项目打磨 |
| **维度 Skill** | `skills/tech/*`、`skills/ux/*`、`skills/frameworks/*` | 按领域增量建设 |

**config_table** 是第一个成熟的**维度 Skill** 范例：从超级鸡马道具表结构问题抽象出「程序态单表 + 三阶段协作」，而非改某一功能的数值。

后续你将提供：

- **程序已拆解、线上在用的策划案**（真源对照）
- 按维度逐个完善 **需求拆解 拆解 Skill**（规则、状态机、协议、配置表…）
- 按模块逐个完善 **功能点梳理 功能梳理 Skill**（功能点块、分工表、验收场景…）

本规范定义：**如何从真项目提炼 → 登记 → 评审 → 写入 Skill → 同步 Prompt**。

---

## 2. Skill 两层模型

```text
                    ┌─────────────────────────────┐
                    │  阶段 Skill（gdd/p1~p6）     │
                    │  管「这一阶段产出什么结构」   │
                    └──────────────┬──────────────┘
                                   │ 引用
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
  tech/config_table          tech/…（待建）           design/tournament_bracket
  （需求拆解·数据源 配置表）            （需求拆解 其他维度）            （L1 业务模式）
         │                         │
         └─────────────┬───────────┘
                       ▼
              prompts/需求拆解、功能点梳理…（执行步骤 + @ Skill）
                       ▼
              产出/{功能名}/02、03（L2 实例，不回写 Skill）
```

| 层级 | 目录示例 | 写什么 | 不写什么 |
|------|----------|--------|----------|
| **阶段 Skill** | `gdd/p2-decompose-需求拆解` | 八维度索引、编号铁律、职能分轨 | 具体表名、P-xx 数值、功能名 |
| **维度 Skill** | `tech/config_table` | 该维度的格式、流程、反模式、自检 | 47 行道具数据、CHH 缩写规则 |
| **L1 框架 Skill** | `design/tournament_bracket` | 抽象模式、R-TB 编号、config 槽位 | 竞技场 UI 文案 |
| **L2 产出** | `产出/超级鸡马/` | 全部业务实例 | — |

**维度 Skill 与阶段 Skill 的关系**：阶段 Skill 保持薄；**可复用的拆解套路**下沉为维度 Skill，由对应 Prompt `@` 引用。

---

## 3. 演进闭环（真项目 → Skill）

```text
① 真源输入          ② 跑管线 / 程序拆解        ③ 发现缺口或反模式
   源文档/docx            产出/ 或 程序交付 GDD          评审会 / diff / QA
        │                        │                        │
        └────────────────────────┴────────────────────────┘
                                 ▼
                    ④ 抽象为维度 Skill 草案（_backlog 或 PR）
                                 ▼
                    ⑤ 维护者确认 → 写入 skills/ + 改 prompts/
                                 ▼
                    ⑥ 下一功能复用；L2 只写 delta
```

### 3.1 合格输入（真源）

| 输入类型 | 典型路径 | 用途 |
|----------|----------|------|
| 策划定稿 | `源文档/*.docx`、`产出/…/01-原始策划案/` | 业务意图 |
| 程序拆解 GDD | `产出/…/02`、`产出/…/03` 或程序仓库导出 | **格式与分工的真标准** |
| 已上线配置 / 协议 | 程序提供表结构、proto、枚举 | 配置表、协议类 Skill |
| 回填结果 | `04-待策划补充/` 定稿后回流 | 验证「待填 → 定值」流程 |

### 3.2 触发更新的信号

- Agent 产出结构**程序无法直接加载**（如配置表双段式）
- 同一维度在 **2+ 功能** 重复犯相同错误
- 程序在 03 反复补同一类块（如分工表缺列）
- 策划 docx 形态与 GDD 形态**系统性不一致**（需 Skill 规定合并规则）

### 3.3 抽象铁律（写入 Skill 前必问）

1. **能否去掉功能名？** 不能 → 留在 L2 `产出/`
2. **能否去掉具体数值？** 不能 → 留在 L2 或标 `待填` 流程说明
3. **是否 2+ 项目复用？** 否 → 先记在 L2 README，不急着进 Skill
4. **是格式问题还是业务规则？** 业务规则 → `02` §3 + `03` 怎么实现；格式/协作 → Skill
5. **程序是否已认可该结构？** 未认可 → 先 `_backlog` 代做，不晋升

---

## 4. 更新流程（维护者）

| 步 | 动作 | 产出 |
|----|------|------|
| **S1 登记** | 在 `_backlog/` 新增 `{skill_id}.md` 或更新 [维度 Skill 路线图](_backlog/维度Skill路线图.md) | 问题描述、拟 skill_id、关联 Prompt |
| **S2 对照** | 指定 1 个**已投产** L2 实例为参考（只读链接，不复制正文） | 「参考实例」表 |
| **S3 草案** | 写 Skill 骨架：`meta.md` + `tech.md` 或 `SKILL.md` | 格式铁律、流程、反模式、自检清单 |
| **S4 评审** | 策划（业务完备）+ 程序（可加载/可开发）双签 | 评审记录可写在 backlog 文件底部 |
| **S5 晋升** | 迁入 `skills/tech|ux|design|gdd/`；更新 `skills/README.md` | 正式 Skill |
| **S6 挂接** | 改 `prompts/Px/`：@ Skill、本步铁律、自检项；阶段 Skill 加一节指针 | Prompt 与 Skill 一致 |
| **S7 验证** | 用**新功能**或**回归跑一轮** 需求拆解/功能点梳理，对照自检清单 | `产出/…/logs/` **新建**变更记录（每次改文档必写，见 [使用指导](../使用指导.md)） |

**禁止**：维护者未确认时，Agent 跑管线**不得**改 `skills/`（见 `skills/README.md` 治理原则）。

---

## 5. 范例：config_table（第一个维度 Skill）

| 项 | 内容 |
|----|------|
| **问题** | docx 双 sheet（列说明 + 道具清单）被原样拆成两段，程序不可用 |
| **真源** | `产出/超级鸡马/01-原始策划案/超级鸡马/源表提取/`、`产出/超级鸡马/02-…/AB2_ChickenHorseItem.md` |
| **抽象** | 一行一主键；enum/bool 类型化；三阶段（策划→Agent→程序）；缺值 `待填` |
| **Skill** | [tech/config_table/tech.md](tech/config_table/tech.md) |
| **Prompt** | [prompts/需求拆解/数据源.md](../prompts/需求拆解/数据源.md) 已 @ 并增自检 |
| **阶段 Skill** | [gdd/p2-decompose-需求拆解/SKILL.md](gdd/p2-decompose-需求拆解/SKILL.md) 增配置表指针 |
| **后续** | [config_table_impact](_backlog/config_table_impact.md)（改表影响检索，待建） |

**可复制模式**：「实战翻车 → 抽象铁律 → L0 维度 Skill → 挂 需求拆解 Prompt → L2 仅作参考实例链接」。

---

## 5b. 范例：configurable_rules（第二个维度 Skill）

| 项 | 内容 |
|----|------|
| **问题** | 计分类规则有 R-xx，但 Const/表分值缺失、边界用散文、「待确认明细」笼统 |
| **真源** | `产出/超级鸡马/02-…/计分全量审计.md`、`04-…/09-规则边界确认.md` |
| **抽象** | R-xx 读 P-xx；Q-D 数值 / Q-R 边界分轨；按需 09；可选域审计 md |
| **Skill** | [tech/configurable_rules/tech.md](tech/configurable_rules/tech.md) |

**可复制模式**：与 config_table 相同，L2 只链实例，Skill 不写玩法名。

---

## 5c. 范例：implementation_data（第三个维度 Skill）

| 项 | 内容 |
|----|------|
| **问题** | R-xx 有「重力/摩擦」等词但无 P-xx/表列；表骨架 ✅ 被当作可开发；数值埋在 trigger_desc |
| **真源** | `产出/超级鸡马/02-…/数据契约审计.md`、`物理全量审计.md` |
| **抽象** | 变量追溯；G-xxa/G-xxb；数据契约审计；模块就绪矩阵；01 推断义务 |
| **Skill** | [tech/implementation_data/tech.md](tech/implementation_data/tech.md) |

**可复制模式**：与 configurable_rules 并列；计分域用 configurable_rules + implementation_data 双 Skill。

---

## 6. 待建设维度 Skill 路线图

> 由维护者维护 [\_backlog/维度Skill路线图.md](_backlog/维度Skill路线图.md)。  
> 你提供程序拆解策划案后，按优先级将 📝 改为 🟡/✅。

### 6.1 需求拆解 拆解类（需求拆解八维度）

| skill_id（拟） | 维度 | Prompt | 状态 | 说明 |
|----------------|------|--------|------|------|
| **config_table** | 数据源·配置表 | 需求拆解·数据源 | ✅ 已启用 | 程序态单表、三阶段协作 |
| **configurable_rules** | 可配置规则 | 需求拆解·规则、待策划补充 | ✅ 已启用 | Q-D/Q-R 分轨、按需 09 |
| **implementation_data** | 实现数据契约 | 需求拆解 收尾、P3、编译验收 | ✅ 已启用 | 数据契约审计、就绪矩阵 |
| config_table_impact | 配置表·变更影响 | （待建） | 📝 代做 | 表关联 JSON 检索 |
| decompose_rules | 规则 R-xx | 需求拆解·规则 | ⬜ 待提炼 | 触发/检测位置/读写表 |
| decompose_state_machine | 状态机 | 需求拆解·状态机 | ⬜ 待提炼 | V6 写法、迁移条件 |
| decompose_protocol | 协议·运行时 | 需求拆解·数据源 子域 | ⬜ 待提炼 | proto 字段、读写方 |
| decompose_boundary | 边界 EX/PRE/LIM | 需求拆解·边界条件 | ⬜ 待提炼 | 异常流、前置、限制 |
| decompose_validation | 校验 V-xx | 需求拆解·校验规则 | ⬜ 待提炼 | 与配置/协议联动 |
| decompose_red_dot | 红点 RD-xx | 需求拆解·红点 | ⬜ 待提炼 | |
| decompose_ui_flow | UI 跳转 | 需求拆解·UI交互 | ⬜ 待提炼 | 非线框，是跳转与状态 |
| decompose_acceptance | 验收 T/B/E | 需求拆解·验收标准 | ⬜ 待提炼 | 与 03 验收场景衔接 |

**命名约定**：横切放 `tech/decompose_*` 或 `tech/{domain}`；仅当形成稳定子域时拆目录，避免 Skill 碎片化。

### 6.2 功能点梳理 功能梳理类

| skill_id（拟） | 关注点 | Prompt | 状态 | 说明 |
|----------------|--------|--------|------|------|
| feature_spec_core | 03 总规范 | P3-* 公共 | 🟡 有骨架 | [p3-feature-spec-功能点梳理/SKILL.md](gdd/p3-feature-spec-功能点梳理/SKILL.md) |
| feature_point_block | 功能点五段块 | 功能点梳理·功能点拆分 | ⬜ 待提炼 | 模块/数据/实现/分工 |
| feature_module_split | 功能点拆分粒度 | 功能点梳理·功能点拆分 | ⬜ 待提炼 | N / N.M 与文件映射 |
| feature_acceptance | 验收场景 | 功能点梳理·验收场景 | ⬜ 待提炼 | 可执行、自带关键规则 |
| feature_task_map | Feature 任务映射 | 功能点梳理·Feature对齐 | ⬜ 待提炼 | L2 映射，不改 L1 feature.md |
| feature_field_map | 03 字段映射 | 功能点梳理·字段映射 | ⬜ 待提炼 | 与 02 P-xx 一致 |

### 6.3 优先级建议

1. **程序已痛**的维度优先（配置表 ✅、协议、状态机、功能点分工）
2. **多项目复用**高者优先（交互反馈 L0 已有）
3. **仅单项目特例**延后或只写 L2 备注

---

## 7. 与 Prompt、Backlog、产出的分工

| 工件 | 职责 | Skill 更新时是否改 |
|------|------|-------------------|
| **Skill** | 抽象格式、协作流程、反模式 | ✅ 主改对象 |
| **Prompt** | 步骤、路径占位符、`@` 必读、自检清单 | ✅ 挂接新 Skill |
| **_backlog** | 未确认构想、路线图状态 | ✅ 登记与晋升 |
| **templates/** | 空壳模板 | 随 Skill 改结构时同步 |
| **产出/** | 真项目 L2 | ❌ 禁止回写 Skill；可作参考实例链接 |
| **案例/** | 对照样例 | 仅维护者迁移，不作 Skill 来源 |

---

## 8. Skill 文件约定

### 8.1 维度 Skill（推荐 `tech/{id}/`）

```text
skills/tech/{skill_id}/
├── meta.md      # id、name、category、description
└── tech.md      # 铁律、流程、模板、自检、参考实例链接（L2 路径）
```

### 8.2 阶段 Skill（`gdd/p{n}-*/SKILL.md`）

- 保持**索引与铁律**；具体维度细节**链接**到维度 Skill，避免单文件膨胀。
- 新增维度时：阶段 Skill 增加 1 节指针 + 路线图登记。

### 8.3 代做记录（`_backlog/{skill_id}.md`）

必含：问题、WHEN、输入输出、拟目录、评审项、晋升检查表（与 [\_backlog/README.md](_backlog/README.md) 一致）。

---

## 9. 维护者检查清单（每次晋升）

- [ ] Skill 正文无具体功能名、无数值、无 L2 规则全文
- [ ] 至少有 1 个**已投产或程序认可**的 L2 参考实例（链接）
- [ ] 对应 Prompt 已 `@` 且自检项可执行
- [ ] `skills/README.md` 已收录
- [ ] 路线图状态已更新
- [ ] Agent 跑管线文档中仍写明「禁止擅自改 skills/」

---

## 10. 你提供材料时的推荐格式

便于批量提炼 Skill，建议每次提供：

```markdown
## 维度
配置表 / 状态机 / 功能点分工 / …

## 参考功能
产出/{功能名} 或 程序仓库路径

## 程序认可的标准文件
- 路径 1（主对照）
- 路径 2（可选）

## 当前 Agent 问题
- 问题 1
- 问题 2

## 期望 Skill 产出
skill_id、挂接 Prompt、是否 L0/L1
```

维护者按 **§4 更新流程** 走 S1→S7。

---

## 相关文档

- [skills/README.md](README.md) — 治理原则与已内置 Skill 列表
- [\_backlog/README.md](_backlog/README.md) — 代做晋升规则
- [\_backlog/维度Skill路线图.md](_backlog/维度Skill路线图.md) — 拆解/梳理 Skill 进度表
- [tech/config_table/tech.md](tech/config_table/tech.md) — 首个完整维度 Skill 范例
