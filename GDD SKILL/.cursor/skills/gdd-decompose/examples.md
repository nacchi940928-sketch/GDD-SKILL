# gdd-decompose · 使用示例

## 整包拆解（docx → 04）

```text
/gdd-decompose
@源文档/{策划案}.docx
工作包：{功能名}
feature_root=产出/{功能名}
workflow=skills/workflows/{项目}.workflow.json
请从 docx 全流程跑到 04（含 P2.5），全流程不要停。
不要读 程序反馈/ 作为输入。
```

## 01 已定稿 → 从 P2 起

```text
/gdd-decompose
@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md
工作包：{功能名}
feature_root=产出/{功能名}
按 gdd-decompose 从需求拆解跑到 04，一步一确认。
```

## 只跑单步

```text
/gdd-decompose
@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md
工作包：{功能名}，只做需求拆解·规则
```

## 拆到 compile

```text
/gdd-decompose
@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md
工作包：{功能名}，拆到 compile
workflow=skills/workflows/{项目}.workflow.json
```

## 连续执行关键词

用户说以下任一时，不在每步暂停：

- 「全流程 / 不要停 / 继续」
