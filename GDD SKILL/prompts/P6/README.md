# P6 提示词索引

规范：`skills/gdd/p6-pipeline/SKILL.md`

## 前置

- P3 完成，P4-2 / P5 验收通过
- 已执行 `python tools/compile.py` 生成 `outputs/{功能名}/程序包.md`
- workflow 中 `selected_skills` 与 `skill_configs` 已定稿

## 用法

1. 复制提示词正文到 Agent
2. `@` 引用 03、02、`outputs/程序包.md`、workflow、server 协议（前端用）

## 推荐顺序

```
P6-1 后端管线编排
  → 后端开发/交付协议
  → P6-2 前端管线编排
  → P6-3 增量开发核对（可选，或合并进 P6-1/2）
```

## 文件列表

| 提示词 | 产出路径 |
|--------|----------|
| P6-1-后端管线编排.md | server/design/{功能名}/ 四件套 |
| P6-2-前端管线编排.md | client/design/{功能名}/ 四件套 |
| P6-3-增量开发继承现网.md | 复用标注 + delta 清单 |

L1 框架规则已在 03 中实例化；P6 以 **03 + 程序包** 为开发输入，不回读 L1 抽象层。
