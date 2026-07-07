#!/usr/bin/env python3
"""
将 legacy 02/03 多文件夹合并为单文档（一次性迁移用）。

日常交付请直接编辑 `{feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md` 与 `03-功能点梳理.md`。

用法:
  python tools/merge_delivery.py 产出/超级鸡马   # 仅当 legacy 目录仍存在时
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STAGE_02 = "02-需求拆解"
STAGE_03 = "03-功能点梳理"
SPEC_DIR = "02-03需求拆解与功能点梳理"

DIMENSION_ORDER_02 = [
    ("规则", "3. 业务规则"),
    ("状态机", "2. 流程与状态"),
    ("UI交互", "4. UI 与交互"),
    ("边界条件", "5. 边界与异常"),
    ("数据源", "6. 数据与配置"),
    ("校验规则", "6.2 校验规则"),
    ("红点", "6.3 红点"),
    ("验收标准", "7. 验收要点"),
]


def _find_inner(base: Path) -> Path | None:
    if not base.is_dir():
        return None
    for child in base.iterdir():
        if child.is_dir():
            return child
    return base


def _read_md(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    return text.lstrip("\ufeff")


def _strip_top_h1(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).strip()
    return text.strip()


def _downgrade_headers(text: str, levels: int = 1) -> str:
    """## -> ### when nesting under a parent section."""
    if levels <= 0:
        return text
    prefix = "#" * levels
    out = []
    for line in text.splitlines():
        if line.startswith("#"):
            m = re.match(r"^(#+)(\s.*)$", line)
            if m:
                out.append(prefix + m.group(1) + m.group(2))
                continue
        out.append(line)
    return "\n".join(out).strip()


def _collect(dir_path: Path, sub: str) -> list[Path]:
    d = dir_path / sub
    if not d.is_dir():
        return []
    return sorted(d.rglob("*.md"))


def _feature_point_files(dir_03: Path) -> list[Path]:
    fp = dir_03 / "功能点"
    if not fp.is_dir():
        return []
    return sorted(fp.glob("*.md"), key=lambda p: _sort_key(p.stem))


def _sort_key(stem: str) -> tuple:
    m = re.match(r"^(\d+)-(\d+)", stem)
    if m:
        return (int(m.group(1)), int(m.group(2)), stem)
    return (999, 999, stem)


def _chapter_title(stem: str) -> str:
    """1-1-选角与匹配 -> 1. 选角与匹配"""
    m = re.match(r"^(\d+)-\d+-(.+)$", stem)
    if m:
        return f"{m.group(1)}. {m.group(2)}"
    return stem.replace("-", " ")


def merge_03(feature_root: Path, feature_name: str, workflow_note: str = "") -> Path:
    dir_03 = _find_inner(feature_root / STAGE_03)
    if not dir_03:
        raise FileNotFoundError(f"未找到 {STAGE_03}: {feature_root}")

    intro = workflow_note or "字段：P-xx → 见附录 A；禁止自创未确认字段名。"
    lines = [
        f"# {feature_name} — 功能点梳理",
        "",
        f"> **程序主文档**：本文自包含，无需对照 docx 即可开发与验收。{intro}",
        f"> 生成时间：{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
    ]

    # §0 阅读说明
    readme = dir_03 / "0-阅读说明.md"
    if readme.exists():
        body = _downgrade_headers(_strip_top_h1(_read_md(readme)), 1)
        body = body.replace("03 本目录", "本文档")
        body = re.sub(r"\[([^\]]+)\]\([^)]*功能点/[^)]+\)", r"\1", body)
        body = re.sub(r"\|\s*\d+-\d+\s*\|\s*[^|]+\.md\s*\|", lambda m: m.group(0).replace(".md", ""), body)
        lines.append("## 0. 阅读说明")
        lines.append("")
        lines.append(body)
        lines.append("")

    # 功能点章节
    for fp in _feature_point_files(dir_03):
        title = _chapter_title(fp.stem)
        body = _downgrade_headers(_strip_top_h1(_read_md(fp)), 1)
        lines.append(f"## {title}")
        lines.append("")
        lines.append(body)
        lines.append("")
        lines.append("---")
        lines.append("")

    # 附录
    for appendix, fname in [
        ("附录 A 字段映射", "字段映射.md"),
        ("附录 B 验收场景", "验收场景.md"),
        ("附录 C 待确认事项", "待确认事项.md"),
    ]:
        p = dir_03 / fname
        if p.exists():
            lines.append(f"## {appendix}")
            lines.append("")
            lines.append(_downgrade_headers(_strip_top_h1(_read_md(p)), 1))
            lines.append("")

    out_dir = feature_root / SPEC_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "03-功能点梳理.md"
    out.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return out


def merge_02(feature_root: Path, feature_name: str) -> Path:
    dir_02 = _find_inner(feature_root / STAGE_02)
    dir_01 = _find_inner(feature_root / "01-原始策划案")
    if not dir_02:
        raise FileNotFoundError(f"未找到 {STAGE_02}: {feature_root}")

    lines = [
        f"# {feature_name} — 需求拆解",
        "",
        "> **汇报文档**：面向策划、运营、产品、管理层评审与汇报。",
        "> 编号体系：R-/P-/V-/T-/RD-；程序实现细节见同目录 **03-功能点梳理.md**。",
        f"> 生成时间：{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## 0. 文档说明",
        "",
        "| 项 | 说明 |",
        "|----|------|",
        f"| 功能名 | {feature_name} |",
        "| 02 本文 | 业务规则、流程、UI、边界、数据概要 |",
        "| 03 功能点梳理 | 程序/服务端/AI 开发主读 |",
        "| 04 待策划补充 | 策划回填数值与边界 |",
        "| 看板 | 补充与修改看板.md |",
        "",
    ]

    # 1. 功能概述（来自 01 前几节摘要）
    if dir_01:
        gdd = dir_01 / "原始策划案.md"
        if gdd.exists():
            text = _read_md(gdd)
            # 提取 ## 1. 概述 到 ## 2. 之前
            m = re.search(r"(## 1\.[^\n]*\n.*?)(?=\n## 2\.)", text, re.DOTALL)
            if m:
                lines.append("## 1. 功能概述")
                lines.append("")
                lines.append(m.group(1).strip())
                lines.append("")

    seen_sections: set[str] = set()

    # 状态机优先作为流程章
    sm_files = _collect(dir_02, "状态机")
    if sm_files:
        lines.append("## 2. 流程与状态")
        lines.append("")
        for f in sm_files:
            lines.append(_strip_top_h1(_read_md(f)))
            lines.append("")
        seen_sections.add("状态机")

    for dim, heading in DIMENSION_ORDER_02:
        if dim in seen_sections:
            continue
        files = _collect(dir_02, dim)
        if not files:
            continue
        if heading not in [l.strip("## ") for l in lines if l.startswith("## ")]:
            lines.append(f"## {heading}")
            lines.append("")
        for f in files:
            rel = f.relative_to(dir_02).as_posix()
            lines.append(f"<!-- {rel} -->")
            lines.append("")
            lines.append(_strip_top_h1(_read_md(f)))
            lines.append("")

    # 专项审计
    audit_files = sorted((dir_02 / "规则").glob("*审计*.md")) if (dir_02 / "规则").is_dir() else []
    audit_files += sorted((dir_02 / "数据源").glob("*审计*.md")) if (dir_02 / "数据源").is_dir() else []
    if audit_files:
        lines.append("## 8. 专项审计与数据契约")
        lines.append("")
        for f in audit_files:
            lines.append(_strip_top_h1(_read_md(f)))
            lines.append("")

    kanban = feature_root / "补充与修改看板.md"
    if kanban.exists():
        lines.append("## 9. 待办看板摘要")
        lines.append("")
        text = _read_md(kanban)
        # 只取总览 + 前两专项
        m = re.search(r"(## 一、总览.*?)(?=\n## 四、|\Z)", text, re.DOTALL)
        if m:
            lines.append(m.group(1).strip())
        else:
            lines.append("_见 补充与修改看板.md_")
        lines.append("")

    out_dir = feature_root / SPEC_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "02-需求拆解.md"
    out.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description="合并 02/03 为单文档")
    parser.add_argument("feature_root", help="功能根目录，如 产出/超级鸡马")
    parser.add_argument("--feature-name", help="文档标题中的功能名，默认取目录名")
    parser.add_argument("--workflow-note", default="", help="03 文首继承说明")
    args = parser.parse_args()

    root = Path(args.feature_root)
    if not root.is_absolute():
        root = ROOT / root
    name = args.feature_name or root.name

    p02 = merge_02(root, name)
    p03 = merge_03(root, name, args.workflow_note)
    print(f"Wrote {p02}")
    print(f"Wrote {p03}")


if __name__ == "__main__":
    main()
