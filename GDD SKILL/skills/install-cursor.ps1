# 安装 Cursor 斜杠命令
# 在「skills 的父目录」（工作区根）执行：
#   powershell -ExecutionPolicy Bypass -File skills/install-cursor.ps1

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspace = Split-Path -Parent $here
$cursorSkills = Join-Path $workspace ".cursor\skills"

New-Item -ItemType Directory -Force -Path $cursorSkills | Out-Null

foreach ($name in @("gdd-decompose", "gdd-norm-feedback")) {
    $src = Join-Path $here $name
    $dst = Join-Path $cursorSkills $name
    if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
    Copy-Item -Recurse -Force $src $dst
    Write-Host "OK: $name -> $dst"
}

Write-Host ""
Write-Host "完成。请用 Cursor 打开工作区根: $workspace"
Write-Host "斜杠命令: /gdd-decompose  /gdd-norm-feedback"
