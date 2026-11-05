@echo off
title Worker Dich Tu Dong Top 100 Sieu Pham (AI Local Qwen)
chcp 65001 >nul

echo =======================================================================
echo    HỆ THỐNG DỊCH TỰ ĐỘNG BẢNG XẾP HẠNG TOP 100 SIÊU PHẨM (AI + GITHUB)
echo =======================================================================
echo.
echo [+] Kiểm tra máy chủ AI Local (http://127.0.0.1:11434)...
curl -s http://127.0.0.1:11434/health >nul
if errorlevel 1 (
    echo [!] Server AI Local chưa chạy! Đang khởi động máy chủ AI Local...
    start "Local AI Server" start_local_ai.bat
    timeout /t 5 >nul
)

echo [+] Server AI Local đã sẵn sàng!
echo.
echo Menu lựa chọn chế độ dịch:
echo   1. Dịch tuần tự toàn bộ kho truyện trong thư viện (Top 100)
echo   2. Dịch bộ truyện cụ thể theo ID
echo   3. Tiếp tục dịch tiến trình truyện Sắc Hiệp (Phong Lưu Đại Pháp Sư...)
echo.
set /p choice="Nhập lựa chọn của bạn [1, 2, 3 - Mặc định: 1]: "

if "%choice%"=="2" (
    set /p nid="Nhập ID truyện bạn muốn dịch: "
    echo [+] Bắt đầu dịch tự động truyện ID %nid%...
    .\.venv\Scripts\python.exe auto_translate_top100.py %nid% 5
) else if "%choice%"=="3" (
    echo [+] Tiếp tục dịch các bộ Sắc Hiệp...
    .\.venv\Scripts\python.exe auto_translate_sac_hiep.py 5
) else (
    echo [+] Bắt đầu dịch tuần tự toàn bộ danh sách Top 100...
    .\.venv\Scripts\python.exe auto_translate_top100.py "" 5
)

pause
