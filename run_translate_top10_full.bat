@echo off
title Worker Dich Full Top 10 Sieu Pham (AI Local Qwen + GitHub Sync)
chcp 65001 >nul

echo =======================================================================
echo    HỆ THỐNG DỊCH FULL TOÀN BỘ TOP 10 SIÊU PHẨM (AI ENGINE + GITHUB)
echo =======================================================================
echo.
echo Danh sách 10 siêu phẩm hàng đầu:
echo   1. Đấu Phá Thương Khung (ID: 42)
echo   2. Phàm Nhân Tu Tiên (ID: 65)
echo   3. Đấu La Đại Lục (ID: 66)
echo   4. Tru Tiên (ID: 64)
echo   5. Quỷ Bí Chi Chủ (ID: 54)
echo   6. Đế Bá (ID: 77)
echo   7. Vũ Động Càn Khôn (ID: 67)
echo   8. Bàn Long (ID: 71)
echo   9. Võ Luyện Đỉnh Phong (ID: 81)
echo   10. Ta Thật Không Muốn Trùng Sinh A (ID: 89)
echo.
echo [+] Đang kiểm tra máy chủ AI Local (http://127.0.0.1:11434)...
curl -s http://127.0.0.1:11434/health >nul
if errorlevel 1 (
    echo [!] Server AI Local chưa chạy! Đang khởi động máy chủ AI Local...
    start "Local AI Server" start_local_ai.bat
    timeout /t 5 >nul
)

echo [+] Server AI Local đã sẵn sàng!
echo [+] Bắt đầu tiến trình dịch full toàn bộ Top 10 siêu phẩm:
echo     - Dịch cuốn chiếu liên tục từ chương đầu đến chương cuối.
echo     - Tự động cào chương gốc, chia đoạn tối ưu.
echo     - Tự động Git Commit và Git Push lên GitHub sau mỗi chương.
echo.
echo Nhấn Ctrl + C để tạm dừng bất cứ lúc nào.
echo =======================================================================
echo.

.\.venv\Scripts\python.exe auto_translate_top10.py 5

pause
