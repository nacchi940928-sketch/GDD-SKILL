#!/usr/bin/env python3
"""为 prompts 各阶段 Prompt 文件末尾追加「输入内容示例」节。"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"

MARKER = "## 输入内容示例"

# 通用占位符表（Part 2）
PLACEHOLDER_TABLE = """### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | 竞技场高级赛 |
| `{feature_root}` | `产出/竞技场高级赛` |
| `{功能缩写}` | CHH（Agent/程序填） |
| `{skill_id}` | `tournament_bracket`（无 L1 则留空） |
| `{项目}` | `arena`（Agent/程序填） |"""

PLACEHOLDER_TABLE_P1 = """### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | 竞技场高级赛 |"""

FOOTER = """

---

## 输入内容示例

> 说明如何填写占位符与 @ 引用。**勿与上方「提示词正文」一并复制**；示例以 `案例/竞技场高级赛` 为参照。

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

EXAMPLES: dict[str, dict[str, str]] = {
    "立项探索/项目发现.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1
        + "\n\n**模式 A**：无需 @ 文件，在对话中回答 AI 提问即可。\n\n**模式 B**：@ 参考材料。",
        "at_refs": """# 模式 B 示例
@源文档/竞技场高级赛策划口述整理.md

# 模式 A 示例（首轮对话，无 @）
工作包名称（策划案主题）：竞技场高级赛
我想做现网「纷乱的群殴」活动的优化，自动分组+淘汰赛+竞猜商店。""",
        "notes": """模式 A：策划用口语回答「玩家体验一句话」「参考什么」「是否继承现网」等。
模式 B：材料里没写的字段留空并记入 open_questions，不要编造规则数值。""",
    },
    "立项探索/GameDNA定调.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1,
        "at_refs": """@产出/竞技场高级赛/00-立项探索/竞技场高级赛/project.json
@产出/竞技场高级赛/00-立项探索/竞技场高级赛/README.md""",
        "notes": """project.json 已确认：scope=delta，继承现网 MatchService。
请突出「周练定组 + 16 人淘汰赛 + 竞猜持续参与」三条体验支柱。""",
    },
    "立项探索/功能层级与Skill选型.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1,
        "at_refs": """@产出/竞技场高级赛/00-立项探索/竞技场高级赛/project.json
@产出/竞技场高级赛/00-立项探索/竞技场高级赛/game_dna.json
@skills/frameworks/tournament_bracket/design.md
@workflows/arena.workflow.json""",
        "notes": """对照 workflow 的 selected_skills，说明 L1 用 tournament_bracket，L2 delta 为竞猜/商店/入口分流。""",
    },
    "立项探索/玩法大纲与01初稿.md": {
        "placeholder_table": PLACEHOLDER_TABLE_P1,
        "at_refs": """@产出/竞技场高级赛/00-立项探索/竞技场高级赛/project.json
@产出/竞技场高级赛/00-立项探索/竞技场高级赛/game_dna.md
@templates/01-原始策划案/竞技场高级赛/原始策划案.md""",
        "notes": """输出 01 草稿到产出目录；继承现网章节标注清楚，数值未定标【待确认】。""",
    },
    "原始策划案/Docx转原始案.md": {
        "placeholder_table": """### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | 竞技场高级赛 |
| `{feature_root}` | `产出/竞技场高级赛` |""",
        "at_refs": """@源文档/竞技场高级赛（纷乱的群殴锦标赛）—— 策划案.docx""",
        "notes": """策划已有 docx，跳过立项探索直接从本步进入 Part 2。
表格须转 markdown；六章节齐全；边界标「继承现网 / 本次新增 / 本次改动」。""",
    },
    "原始策划案/完整性检查.md": {
        "placeholder_table": """### 占位符

| 占位符 | 本例取值 |
|--------|----------|
| `{功能名}` | 竞技场高级赛 |
| `{feature_root}` | `产出/竞技场高级赛` |""",
        "at_refs": """@产出/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@templates/01-原始策划案/竞技场高级赛/原始策划案.md""",
        "notes": """只出 gap 报告，不要自动补写 01 正文。策划确认后再进入需求拆解。""",
    },
    "需求拆解/数据源.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@templates/02-需求拆解-写作规范.md
@skills/tech/config_table/tech.md""",
        "notes": """02 尚无 §6 时从零写入；只写业务数据概要，不要 P-xx 大表。""",
    },
    "需求拆解/系统内容分解.md": {
        "at_refs": """@产出/超级鸡马/01-原始策划案/超级鸡马/原始策划案.md
@产出/超级鸡马/02-03需求拆解与功能点梳理/02-需求拆解.md
@templates/02-需求拆解-写作规范.md
@workflows/chickenhorse.workflow.json""",
        "notes": """§6 已写完。归纳布置/跑酷/匹配各系统 CNT-；关联后续 R-。""",
    },
    "需求拆解/规则.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@templates/02-需求拆解-写作规范.md
@workflows/arena.workflow.json
@skills/frameworks/tournament_bracket/design.md""",
        "notes": """每条 R-CHH-xxx 必须含「边界」字段；继承 MatchService 写「继承 tournament_bracket R-TB-001」。""",
    },
    "需求拆解/边界条件.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@templates/02-需求拆解-写作规范.md""",
        "notes": """§3 规则已写完后再跑本步；EX/PRE/LIM 编号与 02 写作规范一致。""",
    },
    "需求拆解/状态机.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@templates/02-需求拆解-写作规范.md""",
        "notes": """写玩家视角期次流转：公示→战斗轮→结算；SM-CHH-xxx 状态名用策划语言。""",
    },
    "需求拆解/UI交互.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@templates/02-需求拆解-写作规范.md
@skills/ux/interaction_feedback/qa.md""",
        "notes": """按界面写：入口分流、对阵树、竞猜、商店；选手/观众身份差异写清。""",
    },
    "需求拆解/红点.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@templates/02-需求拆解-写作规范.md""",
        "notes": """§4 UI 已有后再写 §6.1；RD-CHH-xxx 写「何时出现/消失」，不写检测代码。""",
    },
    "需求拆解/校验规则.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@templates/02-需求拆解-写作规范.md""",
        "notes": """V-CHH-xxx 写程序向校验；与 §5 边界、附录 A 字段对齐。""",
    },
    "需求拆解/验收标准.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@skills/frameworks/tournament_bracket/qa.md""",
        "notes": """T-CHH-xxx 给策划/测试可读；覆盖自动报名、身份锁定、竞猜结算等主路径。""",
    },
    "功能点梳理/阅读说明.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@源文档/竞技场高级赛（纷乱的群殴锦标赛）—— 功能点梳理.docx
@skills/frameworks/tournament_bracket/""",
        "notes": """仅写 03 的 §0；导航表章节数与后续 ## N. 一致。""",
    },
    "功能点梳理/功能点拆分.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@源文档/竞技场高级赛（纷乱的群殴锦标赛）—— 功能点梳理.docx
@skills/frameworks/tournament_bracket/""",
        "notes": """本次拆分范围：§2 自动报名与分组（可分批跑多轮）。
每章五块结构齐全；规则正文写全，禁止「见 02 §x」。""",
    },
    "功能点梳理/字段映射.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@skills/tech/config_table/tech.md
@skills/tech/implementation_data/tech.md""",
        "notes": """写入 03 附录 A/D/E；P-CHH-xxx 全局唯一；与 config_table 规范对齐。""",
    },
    "功能点梳理/验收场景.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@skills/frameworks/tournament_bracket/qa.md""",
        "notes": """附录 B：细粒度场景含前置条件、步骤、期望；引用 T-/R- 编号。""",
    },
    "功能点梳理/待确认事项.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@产出/竞技场高级赛/补充与修改看板.md""",
        "notes": """汇总 Q-Dxx / 【待确认】到看板与 03 附录 C；不要重复已确认项。""",
    },
    "功能点梳理/Feature对齐.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md""",
        "notes": """§0.2 导航每一行映射到 server/client Feature 名；无仓库时先写建议模块名。""",
    },
    "待策划补充/生成待补充清单.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@产出/竞技场高级赛/补充与修改看板.md
@skills/frameworks/tournament_bracket/""",
        "notes": """按 templates/04 生成 06-美术与表现资源 等待填表；数值/文案空缺进 04。""",
    },
    "待策划补充/策划回填验收.md": {
        "at_refs": """@产出/竞技场高级赛/04-待策划补充/竞技场高级赛/
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@产出/竞技场高级赛/补充与修改看板.md""",
        "notes": """策划已在 04 回复区填完竞猜币汇率与商店道具表；请检查与 03 附录 A 是否矛盾。""",
    },
    "编译验收/职能分轨检查.md": {
        "at_refs": """@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md""",
        "notes": """只出报告：检查 02 是否混入 P-xx/伪代码、03 是否缺规则正文。""",
    },
    "编译验收/执行编译验收.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@workflows/arena.workflow.json
@产出/竞技场高级赛/职能分轨检查报告.md""",
        "notes": """Agent 执行：python tools/compile.py 产出/竞技场高级赛 --workflow workflows/arena.workflow.json
勿手改 开发文档/ 下三包。""",
    },
    "编译验收/策划验收清单.md": {
        "at_refs": """@产出/竞技场高级赛/开发文档/程序包.md
@产出/竞技场高级赛/开发文档/策划包.md
@产出/竞技场高级赛/开发文档/编译验收报告.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@workflows/arena.workflow.json""",
        "notes": """策划核对：01 意图是否在策划包中完整呈现；待确认项是否已闭环。""",
    },
    "编译验收/管线执行日志.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@产出/竞技场高级赛/logs/
@templates/logs/模板.log.md
@workflows/arena.workflow.json""",
        "notes": """汇总本轮改动的文件列表、compile 命令、门禁结果；新建 logs/YYYYMMDD-HHMMSS.log.md。""",
    },
    "开发管线/后端管线编排.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/开发文档/程序包.md
@workflows/arena.workflow.json
@skills/frameworks/tournament_bracket/tech.md""",
        "notes": """按 03 各章 + 附录 A/D 生成 server/design/竞技场高级赛/ 四件套草稿。""",
    },
    "开发管线/前端管线编排.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@产出/竞技场高级赛/02-03需求拆解与功能点梳理/02-需求拆解.md
@产出/竞技场高级赛/开发文档/程序包.md
@产出/竞技场高级赛/04-待策划补充/竞技场高级赛/01-字段命名.md
@skills/tech/resolution_standard/
@workflows/arena.workflow.json""",
        "notes": """主读 03 + 02 §4 UI；生成 client/design/竞技场高级赛/ 四件套。""",
    },
    "开发管线/增量开发继承现网.md": {
        "at_refs": """@产出/竞技场高级赛/02-03需求拆解与功能点梳理/03-功能点梳理.md
@案例/竞技场高级赛/01-原始策划案/竞技场高级赛/原始策划案.md""",
        "notes": """核对「继承现网 MatchService」模块，输出 delta 清单，避免重复实现决斗判定。""",
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
    skipped = 0
    for rel in EXAMPLES:
        path = PROMPTS / rel.replace("/", "\\") if False else PROMPTS / Path(rel)
        if not path.exists():
            print(f"MISSING: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            print(f"SKIP (exists): {rel}")
            skipped += 1
            continue
        path.write_text(text.rstrip() + build_footer(rel), encoding="utf-8")
        print(f"OK: {rel}")
        updated += 1
    print(f"\nDone: {updated} updated, {skipped} skipped")


if __name__ == "__main__":
    main()
