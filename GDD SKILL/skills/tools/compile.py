#!/usr/bin/env python3
"""
GDD 编译器：02-需求拆解.md + 03-功能点梳理.md → 程序包 / 测试包 / 策划包

输入：`{feature_root}/02-03需求拆解与功能点梳理/02-需求拆解.md` + `03-功能点梳理.md`
输出：`{feature_root}/开发文档/`

用法:
  python skills/tools/compile.py 产出/超级鸡马
  python skills/tools/compile.py 产出/超级鸡马 --workflow skills/workflows/chickenhorse.workflow.json
  python skills/tools/compile.py --workflow skills/workflows/arena.workflow.json --skills-only
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from skill_loader import load_skills, resolve_dependencies

TOOLS_DIR = Path(__file__).resolve().parent
SKILLS_ROOT = TOOLS_DIR.parent
WORKSPACE_ROOT = SKILLS_ROOT.parent

STAGE_DIRS = {
    "01": "01-原始策划案",
    "04": "04-待策划补充",
}

FILE_02 = "02-需求拆解.md"
FILE_03 = "03-功能点梳理.md"
SPEC_DIR = "02-03需求拆解与功能点梳理"
COMPILE_DIR = "开发文档"
SKILLS_PREVIEW_DIR = TOOLS_DIR / ".skills_preview"


def _resolve_delivery_paths(feature_root: Path) -> tuple[Path, Path]:
    spec = feature_root / SPEC_DIR
    return spec / FILE_02, spec / FILE_03


def _find_stage_dir(feature_root: Path, stage_key: str) -> Path | None:
    stage_name = STAGE_DIRS[stage_key]
    direct = feature_root / stage_name
    if direct.is_dir():
        for child in direct.iterdir():
            if child.is_dir():
                return child
        return direct
    return None


def _collect_md_files(base: Path) -> list[Path]:
    if not base or not base.exists():
        return []
    return sorted(base.rglob("*.md"))


def _read_files(files: list[Path], base: Path) -> str:
    if not files:
        return "_（无内容）_\n"
    parts = []
    for f in files:
        rel = f.relative_to(base).as_posix()
        body = f.read_text(encoding="utf-8").strip()
        parts.append(f"<!-- source: {rel} -->\n\n{body}")
    return "\n\n---\n\n".join(parts) + "\n"


def _read_single(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8").strip() + "\n"
    return ""


def _extract_appendix(text: str, pattern: str) -> str:
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return m.group(0).strip() if m else ""


def _build_doc(title: str, sections: list[tuple[str, str]]) -> str:
    lines = [f"# {title}", "", f"> 编译时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}", ""]
    for heading, body in sections:
        if not body.strip():
            continue
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
        elif not cfg:
            lines.append("- _未填写 skill_configs（请在 `skills/workflows/*.json` 配置本项目参数）_")
        else:
            schema_by_key = {f["key"]: f for f in schema}
            for key, val in cfg.items():
                field = schema_by_key.get(key)
                label = field.get("label", key) if field else key
                if val is None or (isinstance(val, str) and not val.strip()):
                    val = "【待填】"
                lines.append(f"- **{label}** (`{key}`): {val}")
        lines.append("")
    return "\n".join(lines)


def _skill_tier(pkg_dir: Path) -> str:
    skills_root = (SKILLS_ROOT).resolve()
    try:
        top = pkg_dir.resolve().relative_to(skills_root).parts[0]
    except (ValueError, IndexError):
        return "L?"
    if top == "frameworks":
        return "L1"
    if top in ("tech", "ux", "pipeline"):
        return "L0"
    return top


def _render_skill_index(workflow: dict, skills: dict) -> str:
    selected = workflow.get("selected_skills", [])
    if not selected:
        return ""

    try:
        ordered = resolve_dependencies(selected, skills)
    except (KeyError, ValueError) as e:
        return f"_Skill 解析失败: {e}_\n"

    lines = [
        "> 框架/横切 Skill **不嵌入全文**；详细规范请阅读仓库 `skills/` 下对应文件。",
        "> **本项目实例参数** → 见上方「节点配置 (skill_configs)」。",
        "",
        "| skill_id | 名称 | 层级 | 路径 | 文件 |",
        "|----------|------|------|------|------|",
    ]
    qa_refs: list[str] = []
    for sid in ordered:
        skill = skills[sid]
        pkg = Path(skill["package_dir"]).resolve()
        try:
            rel_pkg = pkg.relative_to(SKILLS_ROOT.resolve()).as_posix()
        except ValueError:
            rel_pkg = skill["package_dir"]
        tier = _skill_tier(pkg)
        kf = skill.get("knowledge_files", {})
        files = ", ".join(f"`{k}.md`" for k in sorted(kf)) if kf else "—"
        lines.append(
            f"| `{sid}` | {skill.get('name', sid)} | {tier} | `{rel_pkg}/` | {files} |"
        )
        if "qa" in kf:
            try:
                qa_rel = Path(kf["qa"]).resolve().relative_to(WORKSPACE_ROOT.resolve()).as_posix()
            except ValueError:
                qa_rel = kf["qa"]
            qa_refs.append(f"- `{sid}` → `{qa_rel}`")

    if qa_refs:
        lines.extend([
            "",
            "**测试基线 QA**（不嵌入全文）：",
            *qa_refs,
        ])
    lines.append("")
    return "\n".join(lines)


def compile_feature(
    feature_root: Path,
    output_dir: Path | None = None,
    workflow_path: Path | None = None,
    skills_dir: Path | None = None,
) -> dict:
    feature_root = feature_root.resolve()
    feature_name = feature_root.name

    path_02, path_03 = _resolve_delivery_paths(feature_root)
    dir_01 = _find_stage_dir(feature_root, "01")
    dir_04 = _find_stage_dir(feature_root, "04")

    if not path_02.exists() and not path_03.exists():
        raise FileNotFoundError(
            f"未找到交付文档: 需要 {feature_root / SPEC_DIR / FILE_02} 与 {FILE_03}"
        )

    skills_root = skills_dir or SKILLS_ROOT
    skills = load_skills(skills_root)
    workflow = {}
    if workflow_path and workflow_path.exists():
        workflow = json.loads(workflow_path.read_text(encoding="utf-8"))

    out = output_dir or (feature_root / COMPILE_DIR)
    out.mkdir(parents=True, exist_ok=True)

    text_03 = _read_single(path_03)
    text_02 = _read_single(path_02)

    prog_sections: list[tuple[str, str]] = []
    if text_03:
        prog_sections.append(("功能点梳理（程序主读）", text_03))

    if dir_04:
        filled = []
        for f in sorted(dir_04.glob("*.md")):
            if f.name == "README.md":
                continue
            text = f.read_text(encoding="utf-8")
            if "策划回复" in text or "【待" not in text:
                filled.append(f)
        if filled:
            prog_sections.append(("待策划补充（已填项）", _read_files(filled, dir_04)))

    program_doc = _build_doc(f"{feature_name} — 程序包", prog_sections)
    (out / "程序包.md").write_text(program_doc, encoding="utf-8")

    test_sections: list[tuple[str, str]] = []
    if text_03:
        appendix_b = _extract_appendix(text_03, r"## 附录 B 验收场景.*")
        if appendix_b:
            test_sections.append(("验收场景", appendix_b))

    if text_02:
        acc = _extract_appendix(text_02, r"## 7\. 验收要点.*")
        boundary = _extract_appendix(text_02, r"## 5\. 边界与异常.*")
        if acc:
            test_sections.append(("验收要点", acc))
        if boundary:
            test_sections.append(("边界与异常", boundary))

    skill_index = _render_skill_index(workflow, skills) if workflow else ""
    if skill_index.strip():
        test_sections.append(("Skill 索引", skill_index))

    test_doc = _build_doc(f"{feature_name} — 测试包", test_sections)
    (out / "测试包.md").write_text(test_doc, encoding="utf-8")

    plan_sections: list[tuple[str, str]] = []
    if workflow:
        plan_sections.append(("节点配置 (skill_configs)", _render_skill_configs(workflow, skills)))
    if dir_01:
        plan_sections.append(("原始策划案", _read_files(_collect_md_files(dir_01), dir_01)))
    if text_02:
        plan_sections.append(("需求拆解（汇报主读）", text_02))
    skill_index = _render_skill_index(workflow, skills) if workflow else ""
    if skill_index.strip():
        plan_sections.append(("Skill 索引", skill_index))

    plan_doc = _build_doc(f"{feature_name} — 策划包", plan_sections)
    (out / "策划包.md").write_text(plan_doc, encoding="utf-8")

    manifest = {
        "feature": feature_name,
        "feature_root": str(feature_root),
        "compiled_at": datetime.now(timezone.utc).isoformat(),
        "workflow": str(workflow_path) if workflow_path else None,
        "selected_skills": workflow.get("selected_skills", []),
        "delivery_format": "single_md",
        "compiled_dir": str(out),
        "outputs": ["程序包.md", "测试包.md", "策划包.md"],
        "sources": {
            "spec_dir": str(feature_root / SPEC_DIR),
            "01": str(dir_01) if dir_01 else None,
            FILE_02: str(path_02) if path_02.exists() else None,
            FILE_03: str(path_03) if path_03.exists() else None,
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
    skill_index = _render_skill_index(workflow, skills)
    if skill_index.strip():
        sections.append(("Skill 索引", skill_index))

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
    parser = argparse.ArgumentParser(description="GDD 编译器：单文档 02+03 → 三包")
    parser.add_argument("feature", nargs="?", help="功能根目录，如 产出/超级鸡马")
    parser.add_argument("--workflow", "-w", help="workflow JSON 路径")
    parser.add_argument("--output", "-o", help="输出目录")
    parser.add_argument("--skills-dir", default=str(SKILLS_ROOT))
    parser.add_argument("--skills-only", action="store_true", help="仅编译 workflow + skills")
    args = parser.parse_args()

    workflow_path = Path(args.workflow) if args.workflow else None
    if workflow_path and not workflow_path.is_absolute():
        workflow_path = WORKSPACE_ROOT / workflow_path

    output_dir = Path(args.output) if args.output else None

    if args.skills_only:
        if not workflow_path:
            print("错误: --skills-only 需要 --workflow", file=sys.stderr)
            sys.exit(1)
        out = output_dir or SKILLS_PREVIEW_DIR
        manifest = compile_skills_only(workflow_path, Path(args.skills_dir), out)
    else:
        if not args.feature:
            print("错误: 请指定功能目录或使用 --skills-only", file=sys.stderr)
            sys.exit(1)
        feature_root = Path(args.feature)
        if not feature_root.is_absolute():
            feature_root = WORKSPACE_ROOT / feature_root
        manifest = compile_feature(
            feature_root,
            output_dir=output_dir,
            workflow_path=workflow_path,
            skills_dir=Path(args.skills_dir),
        )

    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
