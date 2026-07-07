# P5 编译验收 — Prompt 库

> **Part 2 交付阶段**：分轨检查 → 编译 → 策划验收，产出 `{feature_root}/开发文档/` 三包。  
> 完整规范：[规格交付库.md](../规格交付库.md) · Skill：[p5-compile-verify](../../skills/pipeline/p5-compile-verify/SKILL.md)

---

## 执行顺序

```text
P4-2 通过 → P5-1 分轨检查 → 修正 02/03
  → P5-2 compile → P5-3 策划验收 → P5-4 执行日志 → P6
```

---

## Prompt 清单

| ID | 文件 | 产出 |
|----|------|------|
| P5-1 | [P5-1-职能分轨检查.md](P5-1-职能分轨检查.md) | `{feature_root}/职能分轨检查报告.md` |
| P5-2 | [P5-2-执行编译验收.md](P5-2-执行编译验收.md) | `{feature_root}/开发文档/编译验收报告.md` + 三包 |
| P5-3 | [P5-3-策划验收清单.md](P5-3-策划验收清单.md) | `{feature_root}/开发文档/策划验收清单.md` |
| P5-4 | [P5-4-管线执行日志.md](P5-4-管线执行日志.md) | `{feature_root}/logs/{YYYYMMDD}-{HHmmss}.log.md` |

---

## 执行日志（P5-4 · 每次文档更新必写）

| 规则 | 说明 |
|------|------|
| 路径 | `{feature_root}/logs/` |
| 命名 | `{YYYYMMDD}-{HHmmss}.log.md`（结束时刻本地时间） |
| 频次 | **每次**改动交付文档后新建一条，**禁止覆盖**、禁止追加旧 log |
| 模板 | [templates/logs/模板.log.md](../../templates/logs/模板.log.md) |
| 必填 | 模板 **§0 本次变更**（文件清单 + 是否 compile） |

触发：全量/部分管线、02/03 局部改、04 回流、compile 重跑、目录与规范维护。只读未改文件时可不写。

部分执行（仅 P1~P2 等）或仅改单文档一节时也须写 log；未触达阶段标 `—`。

---

## 编译命令（P5-2）

```bash
cd "GDD SKILL"
python tools/compile.py 产出/{功能名} --workflow workflows/{项目}.workflow.json
```

| 输入 | 合并到 |
|------|--------|
| 03 功能点 | 程序包.md |
| 03 附录 B + 02 §5/§7 + Skill 索引 | 测试包.md |
| skill_configs + 01 + 02 + Skill 索引 | 策划包.md |

**禁止手改** `{feature_root}/开发文档/`；改 02/03/04 后重新 compile。

---

## 统一 @ 引用

**P5-1**：01 + 02 全目录 + 03 全目录  
**P5-2**：02 + 03 + workflow + P5-1 报告  
**P5-3**：编译三包 + 03 + 04 回填报告 + P5-1/P5-2 报告

---

## 进入 P6 的门禁

- [ ] P5-3 策划验收：可否进入 P6 = **是**
- [ ] `{feature_root}/开发文档/程序包.md` 已生成
- [ ] 无 blocking 编译/错轨问题
- [ ] **P5-4** 已写入 `logs/{YYYYMMDD}-{HHmmss}.log.md`
