# workflows — 项目配置

每个功能复制 [`_template.workflow.json`](_template.workflow.json) 为 `skills/workflows/{项目}.workflow.json`：

1. 将 `{功能名}` 替换为工作包名称（与 `产出/{功能名}` 目录一致）
2. 按需勾选 `selected_skills`（L0/L1，见 `skills/README.md`）
3. 在 `skill_configs` 填写 L1 框架参数
4. `feature_root` 必须为 `产出/{功能名}`（真实交付）

```bash
python skills/tools/compile.py 产出/{功能名} --workflow skills/workflows/{项目}.workflow.json
```
