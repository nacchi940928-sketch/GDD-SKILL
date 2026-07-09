# gdd-decompose（给人类）

Cursor 斜杠命令 **`/gdd-decompose`**：将策划 docx / 01 规格化为 02～04。

## 文件夹结构（Cursor 规范）

```text
gdd-decompose/
├── SKILL.md          ⭐ Agent 主指令
├── reference.md      管线步骤表
├── examples.md       对话示例
├── scripts/          compile 转发脚本
└── README.md         ← 本文件
```

## 复制到其他项目

1. 复制整棵 **`skills/`** 包到目标项目  
2. 运行 `skills/install-cursor.ps1` 将本目录注册到 `.cursor/skills/`  
3. Cursor 打开 **工作区根**（`skills/` 的父目录，含 `产出/`）

`prompts/`、`pipeline/` 等与 `gdd-decompose/` **同级**，均在 `skills/` 内。

详见 [../README.md](../README.md)。
