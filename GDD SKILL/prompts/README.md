# 提示词索引

`prompts/` = **可直接复制粘贴到 Agent 的提示词**  
`skills/gdd/` = **规范与知识（Skill）**，Agent 可读，人不逐条粘贴

## 阶段索引

| 阶段 | 目录 | 规范 Skill | 说明 |
|------|------|------------|------|
| P1 原始策划案 | [P1/](P1/) | [p1-original-gdd](../skills/gdd/p1-original-gdd/SKILL.md) | 策划主文档 |
| P2 需求拆解 | [P2/](P2/) | [p2-decompose](../skills/gdd/p2-decompose/SKILL.md) | 8 个维度 |
| P3 功能点梳理 | [P3/](P3/) | [p3-feature-spec](../skills/gdd/p3-feature-spec/SKILL.md) | 程序主文档 |
| P4 待策划补充 | [P4/](P4/) | [p4-planner-fill](../skills/gdd/p4-planner-fill/SKILL.md) | 策划回填 |
| P5 编译验收 | [P5/](P5/) | [p5-compile-verify](../skills/gdd/p5-compile-verify/SKILL.md) | 分轨+编译+验收 |
| P6 开发管线 | [P6/](P6/) | [p6-pipeline](../skills/gdd/p6-pipeline/SKILL.md) | 后端/前端四件套 |

## 全流程推荐顺序

```text
P1-1 → P1-2 → 策划确认
  ↓
P2-DS → P2-R → P2-EX → P2-SM → P2-UI → P2-RD → P2-V → P2-T
  ↓
P3-1 → P3-2（可分批）→ P3-3 → P3-4 → P3-5 → P3-6
  ↓
P4-1 → 策划回填 04 → P4-2 验收 ──┐
  ↑                              │ 未通过则循环
  └──────────────────────────────┘
  ↓ 通过
P5-1 → P5-2 → P5-3 → 05 入库 → P6
```

## 用法

1. 打开对应 `.md` 文件
2. 复制 **「提示词正文」** 代码块内全文
3. 替换 `{功能名}` 等占位符
4. `@` 引用实际文件
5. 发送给 Agent

## 编译

```bash
python tools/compile.py 案例/竞技场高级赛 --workflow workflows/arena.workflow.json
```

产出 `outputs/{功能名}/程序包.md | 测试包.md | 策划包.md`
