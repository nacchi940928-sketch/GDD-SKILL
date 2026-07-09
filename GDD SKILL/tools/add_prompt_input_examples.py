#!/usr/bin/env python3
"""为 prompts 各阶段 Prompt 文件末尾追加「输入内容示例」节。

维护说明：空工程后请用 reset_prompt_examples.py 批量重置示例；
本文件的 EXAMPLES 须与 reset_prompt_examples.py 保持同步。
"""
from __future__ import annotations

# 实现已迁移至 reset_prompt_examples.py；运行：
#   python tools/reset_prompt_examples.py

if __name__ == "__main__":
    from reset_prompt_examples import main

    main()
