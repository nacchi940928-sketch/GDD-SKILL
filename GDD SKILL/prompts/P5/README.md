# P5 提示词索引

规范：`skills/gdd/p5-compile-verify/SKILL.md`

## 推荐顺序

```
P4-2 通过 → P5-1 分轨检查 → 修正 → P5-2 编译 → P5-3 策划验收 → P6
```

## 编译说明

P5-2 调用 `tools/compile.py`，合并：

| 输入 | 合并到 |
|------|--------|
| 03 功能点 + 02 关键维度 | 程序包.md |
| 02 验收标准 + 03 验收场景 + L1 qa.md | 测试包.md |
| 01 摘要 + skill_configs | 策划包.md |

```bash
python tools/compile.py 案例/{功能名} --workflow workflows/{项目}.workflow.json
```

**禁止手改** `outputs/`；改源文档后重新编译。

## 文件列表

| 提示词 | 产出 |
|--------|------|
| P5-1-职能分轨检查.md | 错轨清单 |
| P5-2-执行编译验收.md | compile 产出 + 检查报告 |
| P5-3-策划验收清单.md | 逐项验收结果 |
