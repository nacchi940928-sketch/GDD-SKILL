#!/usr/bin/env python3
"""将 prompts 文末「输入内容示例」重置为通用占位符（空工程）。"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
MARKER = "## 输入内容示例"

PLACEHOLDER_TABLE = """### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | {你的工作包名称} |
| `{feature_root}` | `产出/{功能名}` |
| `{功能缩写}` | XXX（Agent/程序填） |
| `{skill_id}` | 有 L1 时填 id，无则留空 |
| `{项目}` | workflow 文件名不含 .json（Agent/程序填） |"""

PLACEHOLDER_TABLE_P1 = """### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | {你的工作包名称} |"""

PLACEHOLDER_TABLE_P1_DOCX = """### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | {你的工作包名称} |
| `{feature_root}` | `产出/{功能名}` |"""

FOOTER = """

---

## 输入内容示例

> 说明如何填写占位符与 @ 引用。**勿与上方「提示词正文」一并复制**。路径均相对于 `GDD SKILL/` 根。

{placeholder_table}

### Cursor 中 @ 引用

```
{at_refs}
```

### 策划补充说明（可选）

```
{notes}
```
"""

FORMAT_DOCX = ""  # 仓库初始状态不含样例 docx；03 格式见 p3-feature-spec SKILL.md

EXAMPLES: dict[str, dict[str, str]] = {
    "立项探索/项目发现.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1
        + "\n\n**模式 A**：无需 @ 文件，在对话中回答 AI 提问即可。\n\n**模式 B**：@ 参考材料。",
        "at_refs": "# 模式 B\n@源文档/{你的策划案}.docx\n\n# 模式 A（无 @）\n工作包名称：{你的工作包名称}",
        "notes": "模式 A：口语回答体验目标、参考竞品、是否继承现网。模式 B：材料未写字段记入 open_questions。",
    },
    "立项探索/GameDNA定调.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1,
        "at_refs": "@产出/{功能名}/00-立项探索/{功能名}/project.json",
        "notes": "project.json 已确认后再跑本步。",
    },
    "立项探索/功能层级与Skill选型.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1,
        "at_refs": "@产出/{功能名}/00-立项探索/{功能名}/project.json\n@产出/{功能名}/00-立项探索/{功能名}/game_dna.json\n@skills/README.md\n@skills/frameworks/*/meta.md",
        "notes": "只推荐 skills/ 中已存在的 skill_id；无匹配写「待建 Skill」。",
    },
    "立项探索/玩法大纲与01初稿.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1,
        "at_refs": "@产出/{功能名}/00-立项探索/{功能名}/project.json\n@templates/01-原始策划案/{功能名}/原始策划案.md",
        "notes": "输出 01 草稿；数值未定标【待确认】。",
    },
    "原始策划案/Docx转原始案.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1_DOCX,
        "at_refs": "@源文档/{你的策划案}.docx",
        "notes": "表格转 markdown；六章节齐全；边界标继承现网/新增/改动。",
    },
    "原始策划案/完整性检查.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1_DOCX,
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@templates/01-原始策划案/{功能名}/原始策划案.md",
        "notes": "只出 gap 报告，不自动补写 01。",
    },
    "需求拆解/数据源.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@templates/02-需求拆解-写作规范.md\n@skills/tech/config_table/tech.md\n@workflows/{项目}.workflow.json",
        "notes": "02 尚无 §6 时从零写入；只写数据概要，不要 P-xx 大表。",
    },
    "需求拆解/系统内容分解.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@templates/02-需求拆解-写作规范.md",
        "notes": "§6 已写完后再跑；归纳各系统 SYS-/CNT-。",
    },
    "需求拆解/规则.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@templates/02-需求拆解-写作规范.md\n@workflows/{项目}.workflow.json",
        "notes": "有 L1 时 @ skills/frameworks/{skill_id}/design.md；每条 R- 含「边界」字段。",
    },
    "需求拆解/边界条件.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@templates/02-需求拆解-写作规范.md",
        "notes": "§3 规则完成后再跑；EX/PRE/LIM 编号一致。",
    },
    "需求拆解/状态机.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@templates/02-需求拆解-写作规范.md",
        "notes": "写玩家视角期次/流程状态；策划语言，无伪代码。",
    },
    "需求拆解/UI交互.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@templates/02-需求拆解-写作规范.md\n@skills/ux/interaction_feedback/qa.md",
        "notes": "按界面写布局→交互→状态→空态。",
    },
    "需求拆解/红点.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@templates/02-需求拆解-写作规范.md",
        "notes": "§4 UI 已有后再写 §6.1。",
    },
    "需求拆解/校验规则.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@templates/02-需求拆解-写作规范.md",
        "notes": "V-xxx 默认引导至 03 附录 E.2。",
    },
    "需求拆解/验收标准.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md",
        "notes": "T-/B-/E- 给策划/测试可读。",
    },
    "功能点梳理/阅读说明.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@skills/pipeline/p3-feature-spec-功能点梳理/SKILL.md",
        "notes": "仅写 03 §0；格式见 p3 Skill。",
    },
    "功能点梳理/功能点拆分.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@skills/pipeline/p3-feature-spec-功能点梳理/SKILL.md",
        "notes": "可分批拆章节；五块结构齐全。",
    },
    "功能点梳理/字段映射.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@skills/tech/config_table/tech.md\n@skills/tech/implementation_data/tech.md",
        "notes": "写入 03 附录 A/D/E；P-xx 全局唯一。",
    },
    "功能点梳理/验收场景.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md",
        "notes": "附录 B：含前置、步骤、期望。",
    },
    "功能点梳理/待确认事项.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@产出/{功能名}/补充与修改看板.md",
        "notes": "汇总 Q-xx / 【待确认】到附录 C 与看板。",
    },
    "功能点梳理/Feature对齐.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md",
        "notes": "§0.2 映射 server/client Feature；无仓库时写建议模块名。",
    },
    "待策划补充/生成待补充清单.md": {
        "at_refs": "@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@产出/{功能名}/补充与修改看板.md",
        "notes": "按 templates/04 生成待填表。",
    },
    "待策划补充/策划回填验收.md": {
        "at_refs": "@产出/{功能名}/04-待策划补充/{功能名}/\n@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md",
        "notes": "检查 04 策划必填项与 03 是否矛盾。",
    },
    "编译验收/职能分轨检查.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md",
        "notes": "只出报告，不改正文。",
    },
    "编译验收/执行编译验收.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/02-需求拆解.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@workflows/{项目}.workflow.json",
        "notes": "python tools/compile.py 产出/{功能名} --workflow workflows/{项目}.workflow.json",
    },
    "编译验收/策划验收清单.md": {
        "at_refs": "@产出/{功能名}/开发文档/程序包.md\n@产出/{功能名}/开发文档/策划包.md\n@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md",
        "notes": "策划核对业务意图是否完整呈现。",
    },
    "编译验收/管线执行日志.md": {
        "at_refs": "@产出/{功能名}/logs/\n@templates/logs/模板.log.md",
        "notes": "每次文档变更新建 log，禁止覆盖。",
    },
    "开发管线/后端管线编排.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@产出/{功能名}/开发文档/程序包.md\n@workflows/{项目}.workflow.json",
        "notes": "生成 server/design/{功能名}/ 四件套草稿。",
    },
    "开发管线/前端管线编排.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@产出/{功能名}/开发文档/程序包.md\n@skills/tech/resolution_standard/\n@workflows/{项目}.workflow.json",
        "notes": "生成 client/design/{功能名}/ 四件套。",
    },
    "开发管线/增量开发继承现网.md": {
        "at_refs": "@产出/{功能名}/02-03需求拆解与功能点梳理/03-功能点梳理.md\n@产出/{功能名}/01-原始策划案/{功能名}/原始策划案.md",
        "notes": "核对继承现网模块，输出 delta 清单。",
    },
}


def build_footer(rel: str) -> str:
    ex = EXAMPLES[rel]
    ph = ex.get("placeholder_table", PLACEHOLDER_TABLE)
    return FOOTER.format(
        placeholder_table=ph,
        at_refs=ex["at_refs"].strip(),
        notes=ex["notes"].strip(),
    )


def main() -> None:
    updated = 0
    for rel in EXAMPLES:
        path = PROMPTS / Path(rel)
        if not path.exists():
            print(f"MISSING: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            text = text[: text.index(MARKER)].rstrip()
        path.write_text(text + build_footer(rel), encoding="utf-8")
        print(f"OK: {rel}")
        updated += 1
    print(f"\nDone: {updated} files")


if __name__ == "__main__":
    main()
