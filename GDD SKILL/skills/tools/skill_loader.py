"""Load V6 knowledge packages from skills/."""

from pathlib import Path

from meta_parser import parse_meta_md

KNOWLEDGE_ROLES = ("design", "ux", "tech", "qa", "feature")


def load_skills(skills_dir="skills"):
    root = Path(skills_dir)
    skills = {}
    if not root.exists():
        return skills

    for meta_path in sorted(root.rglob("meta.md")):
        pkg_dir = meta_path.parent
        if pkg_dir.name.startswith("_"):
            continue
        meta = parse_meta_md(meta_path)
        meta["package_dir"] = str(pkg_dir)

        knowledge_files = {}
        for role in KNOWLEDGE_ROLES:
            role_path = pkg_dir / f"{role}.md"
            if role_path.exists():
                knowledge_files[role] = str(role_path)
        meta["knowledge_files"] = knowledge_files
        skills[meta["id"]] = meta

    return skills


def resolve_dependencies(selected, skills):
    result = []
    visiting = set()

    def visit(sid):
        if sid in result:
            return
        if sid in visiting:
            raise ValueError(f"循环依赖: {sid}")
        if sid not in skills:
            raise KeyError(f"未找到 Skill: {sid}")

        visiting.add(sid)
        for dep in skills[sid].get("dependencies", []):
            visit(dep)
        visiting.remove(sid)
        if sid not in result:
            result.append(sid)

    for sid in selected:
        visit(sid)
    return result
