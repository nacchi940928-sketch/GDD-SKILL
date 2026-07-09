#!/usr/bin/env python3
"""从 gdd-decompose 调用 skills/tools/compile.py。

用法（在工作区根 — skills/ 的父目录）:
  python skills/gdd-decompose/scripts/compile.py 产出/{功能名} --workflow skills/workflows/{项目}.workflow.json
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = SKILLS_ROOT.parent
TARGET = SKILLS_ROOT / "tools" / "compile.py"

if not TARGET.is_file():
    sys.stderr.write(
        f"找不到编译器: {TARGET}\n请确认 skills/ 包完整（含 tools/、workflows/）。\n"
    )
    sys.exit(1)

result = subprocess.run(
    [sys.executable, str(TARGET), *sys.argv[1:]],
    cwd=str(WORKSPACE_ROOT),
)
sys.exit(result.returncode)
