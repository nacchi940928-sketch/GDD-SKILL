#!/usr/bin/env python3
"""Rename pipeline subdirs to {english}-{chinese} and update references."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "skills" / "pipeline"

RENAMES = [
    ("p0-discovery", "p0-discovery-立项探索"),
    ("p1-original-gdd", "p1-original-gdd-原始策划案"),
    ("p2-decompose", "p2-decompose-需求拆解"),
    ("p3-feature-spec", "p3-feature-spec-功能点梳理"),
    ("p4-planner-fill", "p4-planner-fill-待策划补充"),
    ("p5-compile-verify", "p5-compile-verify-编译验收"),
    ("p6-pipeline", "p6-pipeline-开发管线"),
]

# longest first to avoid partial replacement
REPLACE_ORDER = sorted(RENAMES, key=lambda x: len(x[0]), reverse=True)

SKIP_DIRS = {".git", "__pycache__", "node_modules"}
SKIP_LOGS = True  # 历史 log 不改


def rename_dirs() -> None:
    for old, new in RENAMES:
        src = PIPELINE / old
        dst = PIPELINE / new
        if not src.exists():
            if dst.exists():
                print(f"SKIP rename (exists): {new}")
                continue
            print(f"MISSING: {old}")
            continue
        if dst.exists():
            print(f"SKIP rename (target exists): {new}")
            continue
        src.rename(dst)
        print(f"RENAMED: {old} -> {new}")


def should_skip(path: Path) -> bool:
    parts = path.parts
    if any(p in SKIP_DIRS for p in parts):
        return True
    if SKIP_LOGS and "logs" in parts and path.suffix == ".md":
        return True
    return False


def update_file(path: Path) -> bool:
    if path.name == "rename_pipeline_dirs.py":
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False
    new_text = text
    for old, new in REPLACE_ORDER:
        new_text = new_text.replace(old, new)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def walk_and_update(base: Path) -> int:
    n = 0
    for p in base.rglob("*"):
        if not p.is_file():
            continue
        if should_skip(p):
            continue
        if p.suffix not in {".md", ".json", ".py", ".txt"}:
            continue
        if update_file(p):
            print(f"UPDATED: {p.relative_to(base.parent)}")
            n += 1
    return n


def main() -> None:
    rename_dirs()
    # workspace root = parent of GDD SKILL subproject
    ws = ROOT.parent
    count = walk_and_update(ws)
    print(f"\nDone: {count} files updated")


if __name__ == "__main__":
    main()
