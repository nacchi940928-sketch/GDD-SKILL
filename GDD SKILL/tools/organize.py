import os, shutil, glob as _glob

ROOT = r"g:\GDD SKILL"
DRY = False  # set True to preview only

def mv(src, dst):
    """Move file or directory"""
    if not os.path.exists(src):
        print(f"  SKIP (not found): {src}")
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if DRY:
        print(f"  [DRY] {src} → {dst}")
    else:
        shutil.move(src, dst)
        print(f"  {os.path.basename(src)} → {os.path.relpath(dst, ROOT)}")

def rm(path):
    if not os.path.exists(path):
        return
    if DRY:
        print(f"  [DRY] rm {path}")
    else:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        print(f"  rm {os.path.relpath(path, ROOT)}")

# ═══════════════════════════════
# 1. Create target directories
# ═══════════════════════════════
for d in ['templates', '案例', 'tools', '参考']:
    os.makedirs(os.path.join(ROOT, d), exist_ok=True)

# ═══════════════════════════════
# 2. Move templates: .template → templates/
# ═══════════════════════════════
print("\n--- Templates ---")
src_tmpl = os.path.join(ROOT, '.template')
dst_tmpl = os.path.join(ROOT, 'templates')
if os.path.exists(src_tmpl):
    # Move contents of .template into templates/
    for item in os.listdir(src_tmpl):
        s = os.path.join(src_tmpl, item)
        d = os.path.join(dst_tmpl, item)
        if os.path.exists(d):
            if os.path.isdir(d):
                shutil.rmtree(d)
            else:
                os.remove(d)
        mv(s, d)
    rm(src_tmpl)
print("templates done")

# ═══════════════════════════════
# 3. Move case studies: 竞技场高级赛 + 军团争霸 → 案例/
# ═══════════════════════════════
print("\n--- Cases ---")
for case in ['竞技场高级赛', '军团争霸']:
    src = os.path.join(ROOT, case)
    dst = os.path.join(ROOT, '案例', case)
    if os.path.exists(src):
        mv(src, dst)

# Also check for v2 garbage
rm(os.path.join(ROOT, '军团争霸_v2'))

# Fix bad filenames in 竞技场高级赛
arena_fp = os.path.join(ROOT, '案例', '竞技场高级赛', '03-功能点梳理', '竞技场高级赛', '功能点')
bad_files = [
    '2-倍  0 返还结算正确.md',
    '4-个周练组映射为 ABCD；Ax 表示 A 组第 x 名。.md',
]
for bf in bad_files:
    p = os.path.join(arena_fp, bf) if os.path.exists(arena_fp) else ''
    if p and os.path.exists(p):
        rm(p)
print("cases done")

# ═══════════════════════════════
# 4. Move reference docs: 策划案参考 → 参考/
# ═══════════════════════════════
print("\n--- References ---")
ref_src = os.path.join(ROOT, '策划案参考')
ref_dst = os.path.join(ROOT, '参考')
if os.path.exists(ref_src):
    for item in os.listdir(ref_src):
        s = os.path.join(ref_src, item)
        d = os.path.join(ref_dst, item)
        # Only move .docx files (original references)
        if item.endswith('.docx'):
            if os.path.exists(d): os.remove(d)
            mv(s, d)
        else:
            # Delete extracted txt files and other junk
            rm(s)
    # Remove empty ref dir
    remaining = os.listdir(ref_src) if os.path.exists(ref_src) else []
    if not remaining:
        rm(ref_src)
print("references done")

# ═══════════════════════════════
# 5. Move Python scripts → tools/
# ═══════════════════════════════
print("\n--- Tools ---")
py_files = _glob.glob(os.path.join(ROOT, '*.py'))
for f in py_files:
    dst = os.path.join(ROOT, 'tools', os.path.basename(f))
    mv(f, dst)
print("tools done")

# ═══════════════════════════════
# 6. Clean up temp files
# ═══════════════════════════════
print("\n--- Cleanup ---")
for pattern in ['*.txt', '*.log']:
    for f in _glob.glob(os.path.join(ROOT, pattern)):
        rm(f)

# Also clean .txt files in subdirs (not in templates or 案例)
for root_dir, dirs, files in os.walk(ROOT):
    if 'templates' in root_dir or '案例' in root_dir or '.git' in root_dir:
        continue
    for f in files:
        if f.endswith('.txt'):
            rm(os.path.join(root_dir, f))

# Clean any leftover _cleanup, _ok, _done marker files
for pattern in ['_cleanup*', '_ok*', '_done*', 'rename_*', '*_result*', '*_log*']:
    for f in _glob.glob(os.path.join(ROOT, pattern)):
        rm(f)

print("\n=== DONE ===")

# ═══════════════════════════════
# 7. Print final structure
# ═══════════════════════════════
print("\nFinal structure:")
for item in sorted(os.listdir(ROOT)):
    path = os.path.join(ROOT, item)
    if item.startswith('.') and item != '.template':
        continue
    if os.path.isdir(path):
        count = sum(1 for _ in os.walk(path) for f in _[2])
        print(f"  {item}/ ({count} files)")
    else:
        print(f"  {item}")
