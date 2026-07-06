# P5 编译验收 — Prompt 库

> **Part 2 交付阶段**：分轨检查 → 编译 → 策划验收，产出 `outputs/` 三包。  
> 完整规范：[规格交付库.md](../规格交付库.md) · Skill：[p5-compile-verify](../../skills/gdd/p5-compile-verify/SKILL.md)

---

## 执行顺序

```text
P4-2 通过 → P5-1 分轨检查 → 修正 02/03
  → P5-2 compile → P5-3 策划验收 → P6
```

---

## Prompt 清单

| ID | 文件 | 产出 |
|----|------|------|
| P5-1 | [P5-1-职能分轨检查.md](P5-1-职能分轨检查.md) | `{feature_root}/职能分轨检查报告.md` |
| P5-2 | [P5-2-执行编译验收.md](P5-2-执行编译验收.md) | `outputs/{功能名}/编译验收报告.md` + 三包 |
| P5-3 | [P5-3-策划验收清单.md](P5-3-策划验收清单.md) | `outputs/{功能名}/策划验收清单.md` |

---

## 编译命令（P5-2）

```bash
cd "GDD SKILL"
python tools/compile.py 案例/{功能名} --workflow workflows/{项目}.workflow.json
```

| 输入 | 合并到 |
|------|--------|
| 03 功能点 + 02 关键维度 | 程序包.md |
| 02 验收标准 + 03 验收场景 + L1 qa | 测试包.md |
| 01 摘要 + skill_configs | 策划包.md |

**禁止手改** `outputs/`；改 02/03/04 后重新 compile。

---

## 统一 @ 引用

**P5-1**：01 + 02 全目录 + 03 全目录  
**P5-2**：02 + 03 + workflow + P5-1 报告  
**P5-3**：outputs 三包 + 03 + 04 回填报告 + P5-1/P5-2 报告

---

## 进入 P6 的门禁

- [ ] P5-3 策划验收：可否进入 P6 = **是**
- [ ] `outputs/{功能名}/程序包.md` 已生成
- [ ] 无 blocking 编译/错轨问题
