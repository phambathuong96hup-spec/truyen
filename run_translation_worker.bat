@echo off
title Worker Tu Dong Dich Truyen Sac Hiep (AI Local Qwen 4B Abliterated)
chcp 65001 >nul

echo =======================================================================
echo    TIẾN TRÌNH TỰ ĐỘNG DỊCH TRUYỆN SẮC HIỆP (AI LOCAL + GITHUB AUTO-PUSH)
echo =======================================================================
echo.
echo [+] Kiểm tra máy chủ AI Local (http://127.0.0.1:11434)...
curl -s http://127.0.0.1:11434/health >nul
if errorlevel 1 (
    echo [!] Server AI Local chua chay! Dang khoi dong server AI...
    start "Local AI Server" start_local_ai.bat
    timeout /t 5 >nul
)

echo [+] Server AI Local da san sang!
echo [+] Bat dau chay tien trinh dich tu dong lien tuc:
echo     - Tu dong cao chuong goc tieng Trung tu nguon chuan.
echo     - Tu dong tach doan, goi AI Local dich sang tieng Viet sac hiep muot ma.
echo     - Tu dong luu vao CSDL data/novels.db.
echo     - Tu dong push len GitHub sau moi dot de dien thoai cap nhat ngay.
echo.
echo Nhan Ctrl + C de dung tien trinh bat ky luc nao.
echo =======================================================================
echo.

.\.venv\Scripts\python.exe auto_translate_sac_hiep.py 5 6 --loop

pause
