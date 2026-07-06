#!/usr/bin/env python3
"""
GDD 编译器：02-需求拆解 + 03-功能点梳理 → 程序包 / 测试包 / 策划包

用法:
  python compile.py 案例/竞技场高级赛
  python compile.py 案例/竞技场高级赛 --workflow workflows/arena.workflow.json
  python compile.py --workflow workflows/arena.workflow.json --skills-only
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from meta_parser import parse_meta_md
from skill_loader import load_skills, resolve_dependencies

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = TOOLS_DIR.parent

STAGE_DIRS = {
    "01": "01-原始策划案",
    "02": "02-需求拆解",
    "03": "03-功能点梳理",
    "04": "04-待策划补充",
}

DIMENSION_ORDER = [
    "规则",
    "边界条件",
    "红点",
    "数据源",
    "UI交互",
    "状态机",
    "校验规则",
    "验收标准",
]

PROGRAM_02_DIMS = {"数据源", "状态机", "校验规则", "规则"}
TEST_02_DIMS = {"验收标准", "边界条件"}
PLANNING_02_DIMS = {"规则", "UI交互"}


def _find_stage_dir(feature_root: Path, stage_key: str) -> Path | None:
    stage_name = STAGE_DIRS[stage_key]
    direct = feature_root / stage_name
    if direct.is_dir():
        for child in direct.iterdir():
            if child.is_dir():
                return child
        return direct
    return None


def _collect_md_files(base: Path, subdirs: list[str] | None = None) -> list[Path]:
    if not base or not base.exists():
        return []
    files: list[Path] = []
    if subdirs:
        for sub in subdirs:
            d = base / sub
            if d.is_dir():
                files.extend(sorted(d.rglob("*.md")))
    else:
        files.extend(sorted(base.rglob("*.md")))
    return files


def _read_files(files: list[Path], base: Path) -> str:
    if not files:
        return "_（无内容）_\n"
    parts = []
    for f in files:
        rel = f.relative_to(base).as_posix()
        body = f.read_text(encoding="utf-8").strip()
        parts.append(f"<!-- source: {rel} -->\n\n{body}")
    return "\n\n---\n\n".join(parts) + "\n"


def _build_doc(title: str, sections: list[tuple[str, str]]) -> str:
    lines = [f"# {title}", "", f"> 编译时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}", ""]
    for heading, body in sections:
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(body.strip())
        lines.append("")
    return "\n".join(lines)


def _render_skill_configs(workflow: dict, skills: dict) -> str:
    selected = workflow.get("selected_skills", [])
    configs = workflow.get("skill_configs", {})
    if not selected:
        return "_未配置 selected_skills_\n"

    lines = []
    try:
        ordered = resolve_dependencies(selected, skills)
    except (KeyError, ValueError) as e:
        return f"_Skill 解析失败: {e}_\n"

    for sid in ordered:
        skill = skills[sid]
        lines.append(f"### {skill.get('name', sid)} (`{sid}`)")
        lines.append("")
        cfg = configs.get(sid, {})
        schema = skill.get("config_schema", [])
        if not schema:
            lines.append("- 无 config_schema")
        else:
            for field in schema:
                key = field["key"]
                label = field.get("label", key)
                val = cfg.get(key, field.get("default", ""))
                lines.append(f"- **{label}** (`{key}`): {val}")
        lines.append("")
    return "\n".join(lines)


def _render_l1_skills(workflow: dict, skills: dict) -> list[tuple[str, str]]:
    selected = workflow.get("selected_skills", [])
    if not selected:
        return []
    try:
        ordered = resolve_dependencies(selected, skills)
    except (KeyError, ValueError):
        return []

    sections = []
    for sid in ordered:
        skill = skills[sid]
        pkg = Path(skill["package_dir"])
        for role in ("design", "ux", "tech", "qa"):
            path = pkg / f"{role}.md"
            if path.exists():
                sections.append((f"L1 {sid} / {role}", path.read_text(encoding="utf-8")))
    return sections


def compile_feature(
    feature_root: Path,
    output_dir: Path | None = None,
    workflow_path: Path | None = None,
    skills_dir: Path | None = None,
) -> dict:
    feature_root = feature_root.resolve()
    feature_name = feature_root.name

    dir_01 = _find_stage_dir(feature_root, "01")
    dir_02 = _find_stage_dir(feature_root, "02")
    dir_03 = _find_stage_dir(feature_root, "03")
    dir_04 = _find_stage_dir(feature_root, "04")

    if not dir_02 and not dir_03:
        raise FileNotFoundError(f"未找到 02/03 目录: {feature_root}")

    skills_root = skills_dir or ROOT / "skills"
    skills = load_skills(skills_root)
    workflow = {}
    if workflow_path and workflow_path.exists():
        workflow = json.loads(workflow_path.read_text(encoding="utf-8"))

    out = output_dir or ROOT / "outputs" / feature_name
    out.mkdir(parents=True, exist_ok=True)

    # --- 程序包 ---
    prog_sections: list[tuple[str, str]] = []
    if dir_03:
        prog_sections.append(("0. 阅读说明与索引", _read_files(
            [p for p in _collect_md_files(dir_03) if p.name.startswith("0-") or p.name in (
                "字段映射.md", "待确认事项.md")],
            dir_03,
        )))
        fp_dir = dir_03 / "功能点"
        if fp_dir.is_dir():
            prog_sections.append(("1. 功能点（程序主读）", _read_files(sorted(fp_dir.glob("*.md")), dir_03)))
        else:
            rest = [p for p in _collect_md_files(dir_03) if "功能点" not in str(p)]
            prog_sections.append(("1. 功能点梳理", _read_files(rest, dir_03)))

    if dir_02:
        for dim in DIMENSION_ORDER:
            if dim in PROGRAM_02_DIMS:
                files = _collect_md_files(dir_02, [dim])
                if files:
                    prog_sections.append((f"2. {dim}", _read_files(files, dir_02)))

    if dir_04:
        filled = []
        for f in sorted(dir_04.glob("*.md")):
            if f.name == "README.md":
                continue
            text = f.read_text(encoding="utf-8")
            if "策划回复" in text or "【待" not in text:
                filled.append(f)
        if filled:
            prog_sections.append(("3. 待策划补充（已填项）", _read_files(filled, dir_04)))

    program_doc = _build_doc(f"{feature_name} — 程序包", prog_sections)
    (out / "程序包.md").write_text(program_doc, encoding="utf-8")

    # --- 测试包 ---
    test_sections: list[tuple[str, str]] = []
    if dir_03:
        for name in ("验收场景.md",):
            p = dir_03 / name
            if p.exists():
                test_sections.append(("验收场景", p.read_text(encoding="utf-8")))
    if dir_02:
        for dim in DIMENSION_ORDER:
            if dim in TEST_02_DIMS:
                files = _collect_md_files(dir_02, [dim])
                if files:
                    test_sections.append((dim, _read_files(files, dir_02)))

    for sid in workflow.get("selected_skills", []):
        qa_path = Path(skills.get(sid, {}).get("package_dir", "")) / "qa.md"
        if qa_path.exists():
            test_sections.append((f"L1 QA / {sid}", qa_path.read_text(encoding="utf-8")))

    test_doc = _build_doc(f"{feature_name} — 测试包", test_sections)
    (out / "测试包.md").write_text(test_doc, encoding="utf-8")

    # --- 策划包 ---
    plan_sections: list[tuple[str, str]] = []
    if workflow:
        plan_sections.append(("节点配置 (skill_configs)", _render_skill_configs(workflow, skills)))
    if dir_01:
        plan_sections.append(("原始策划案", _read_files(_collect_md_files(dir_01), dir_01)))
    if dir_02:
        for dim in DIMENSION_ORDER:
            if dim in PLANNING_02_DIMS:
                files = _collect_md_files(dir_02, [dim])
                if files:
                    plan_sections.append((dim, _read_files(files, dir_02)))
    plan_sections.extend(_render_l1_skills(workflow, skills))

    plan_doc = _build_doc(f"{feature_name} — 策划包", plan_sections)
    (out / "策划包.md").write_text(plan_doc, encoding="utf-8")

    manifest = {
        "feature": feature_name,
        "feature_root": str(feature_root),
        "compiled_at": datetime.now(timezone.utc).isoformat(),
        "workflow": str(workflow_path) if workflow_path else None,
        "selected_skills": workflow.get("selected_skills", []),
        "outputs": ["程序包.md", "测试包.md", "策划包.md"],
        "sources": {
            "01": str(dir_01) if dir_01 else None,
            "02": str(dir_02) if dir_02 else None,
            "03": str(dir_03) if dir_03 else None,
            "04": str(dir_04) if dir_04 else None,
        },
    }
    (out / "compiled.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    return manifest


def compile_skills_only(workflow_path: Path, skills_dir: Path, output_dir: Path) -> dict:
    workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
    skills = load_skills(skills_dir)
    out = output_dir
    out.mkdir(parents=True, exist_ok=True)

    sections = [
        ("Skill 配置", _render_skill_configs(workflow, skills)),
    ]
    sections.extend(_render_l1_skills(workflow, skills))

    doc = _build_doc("Skill 编译预览", sections)
    (out / "策划包.md").write_text(doc, encoding="utf-8")

    manifest = {
        "mode": "skills-only",
        "workflow": str(workflow_path),
        "selected_skills": workflow.get("selected_skills", []),
        "outputs": ["策划包.md"],
    }
    (out / "compiled.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return manifest


def main():
    parser = argparse.ArgumentParser(description="GDD 编译器：02+03 → 程序包/测试包/策划包")
    parser.add_argument("feature", nargs="?", help="功能案例根目录，如 案例/竞技场高级赛")
    parser.add_argument("--workflow", "-w", help="workflow JSON 路径")
    parser.add_argument("--output", "-o", help="输出目录")
    parser.add_argument("--skills-dir", default=str(ROOT / "skills"))
    parser.add_argument("--skills-only", action="store_true", help="仅编译 workflow + skills")
    args = parser.parse_args()

    workflow_path = Path(args.workflow) if args.workflow else None
    if workflow_path and not workflow_path.is_absolute():
        workflow_path = ROOT / workflow_path

    output_dir = Path(args.output) if args.output else None

    if args.skills_only:
        if not workflow_path:
            print("错误: --skills-only 需要 --workflow", file=sys.stderr)
            sys.exit(1)
        out = output_dir or ROOT / "outputs" / "skills_preview"
        manifest = compile_skills_only(workflow_path, Path(args.skills_dir), out)
    else:
        if not args.feature:
            print("错误: 请指定功能目录或使用 --skills-only", file=sys.stderr)
            sys.exit(1)
        feature_root = Path(args.feature)
        if not feature_root.is_absolute():
            feature_root = ROOT / feature_root
        manifest = compile_feature(
            feature_root,
            output_dir=output_dir,
            workflow_path=workflow_path,
            skills_dir=Path(args.skills_dir),
        )

    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
