# gdd-norm-feedback（给人类）

维护者手动触发：**从已完成 L2 产出萃取规范演进建议**，写入 `规范反哺报告.md`。

## 本文件夹结构

```text
gdd-norm-feedback/
├── SKILL.md
├── reference.md
├── examples.md
└── README.md
```

## ⚠️ 不能只复制 `.cursor/`

除本 Skill 外，还需要子项目根下的：

- `prompts/规范反哺/`
- `pipeline/p7-norm-feedback-规范反哺/`
- 已跑完的 `产出/{功能名}/`（02、03、logs）

## 与 gdd-decompose 的关系

| | gdd-decompose | gdd-norm-feedback |
|--|---------------|-------------------|
| 改 prompts/skills | ❌ | ❌（只出报告） |
| 自动衔接 | — | **禁止**接在拆解后 |
