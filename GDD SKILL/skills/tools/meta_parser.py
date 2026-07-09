"""Parse meta.md YAML blocks from skills/."""

import re
from pathlib import Path


def _parse_scalar(value):
    value = value.strip()
    if not value:
        return ""
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("'\"") for item in inner.split(",")]
    return value.strip("'\"")


def parse_meta_yaml(yaml_text):
    meta = {"dependencies": [], "config_schema": []}
    config_schema = []
    current_field = None
    mode = None

    for raw in yaml_text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("dependencies:"):
            mode = "dependencies"
            rest = stripped.split(":", 1)[1].strip()
            if rest:
                meta["dependencies"] = _parse_scalar(rest)
                mode = None
            continue

        if stripped.startswith("config_schema:"):
            mode = "config_schema"
            rest = stripped.split(":", 1)[1].strip()
            if rest == "[]":
                meta["config_schema"] = []
                mode = None
            continue

        if mode == "dependencies" and stripped.startswith("- "):
            meta["dependencies"].append(stripped[2:].strip())
            continue

        if mode == "config_schema" and stripped.startswith("- key:"):
            if current_field:
                config_schema.append(current_field)
            current_field = {"key": stripped.split(":", 1)[1].strip()}
            continue

        if mode == "config_schema" and current_field:
            if stripped.startswith("label:"):
                current_field["label"] = stripped.split(":", 1)[1].strip()
                continue
            if stripped.startswith("default:"):
                current_field["default"] = stripped.split(":", 1)[1].strip()
                continue

        if ":" in stripped and not line.startswith((" ", "\t")):
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in ("id", "name", "category", "description"):
                meta[key] = _parse_scalar(value)
            mode = None

    if current_field:
        config_schema.append(current_field)
    meta["config_schema"] = config_schema
    return meta


def parse_meta_md(path):
    text = Path(path).read_text(encoding="utf-8")
    match = re.search(r"```yaml\s*\n(.*?)```", text, re.DOTALL)
    if not match:
        raise ValueError(f"{path} 必须包含 ```yaml 代码块")
    return parse_meta_yaml(match.group(1))
