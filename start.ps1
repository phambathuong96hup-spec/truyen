# AI Web Novel Reader & Translator Launcher for PowerShell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Set-Location -Path $PSScriptRoot

Write-Host "=======================================================================" -ForegroundColor Cyan
Write-Host "    Khởi chạy Hệ Thống Cào & Dịch Truyện Trung Quốc bằng AI (PWA)      " -ForegroundColor Yellow
Write-Host "=======================================================================" -ForegroundColor Cyan
Write-Host ""

if (Test-Path ".\.venv\Scripts\python.exe") {
    Write-Host "[*] Đang sử dụng môi trường ảo Python .venv..." -ForegroundColor Green
    & ".\.venv\Scripts\python.exe" run.py
} else {
    Write-Host "[*] Đang sử dụng Python hệ thống..." -ForegroundColor Green
    python run.py
}

Write-Host ""
Write-Host "[!] Server đã dừng. Nhấn phím bất kỳ để thoát..." -ForegroundColor Red
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
