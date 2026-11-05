@echo off
title Worker Dich Full Toan Bo Truyen Sac Hiep (AI Local Qwen 4B Abliterated)
chcp 65001 >nul

echo =======================================================================
echo    TIẾN TRÌNH DỊCH FULL TOÀN BỘ TRUYỆN SẮC HIỆP (AI LOCAL + GITHUB)
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
echo [+] Bắt đầu tiến trình dịch full toàn bộ các bộ truyện Sắc Hiệp:
echo     - Dịch cuốn chiếu từng truyện từ chương 1 đến chương cuối cùng.
echo     - Tự động cào nguyên tác tiếng Trung chuẩn xác.
echo     - Tự động đẩy từng chương lên GitHub ngay lập tức.
echo     - Khi dịch xong trọn bộ 1 truyện sẽ lập báo cáo hoàn tất và chuyển truyện tiếp theo.
echo.
echo Nhấn Ctrl + C để tạm dừng bất kỳ lúc nào.
echo =======================================================================
echo.

.\.venv\Scripts\python.exe auto_translate_sac_hiep.py 5

pause
