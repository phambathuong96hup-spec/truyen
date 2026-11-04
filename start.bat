@echo off
chcp 65001 > nul
cd /d "%~dp0"
title AI Web Novel Reader - Translator

echo =======================================================================
echo     Khoi chay He Thong Cao, Dich Truyen Trung Quoc bang AI (PWA)
echo =======================================================================
echo.

if exist ".venv\Scripts\python.exe" (
    echo [*] Dang su dung moi truong Python ao .venv ...
    ".venv\Scripts\python.exe" run.py
) else (
    echo [*] Dang su dung Python he thong ...
    python run.py
)

echo.
echo =======================================================================
echo [!] Server da dung hoac gap su co. Nhan phim bat ky de thoat...
pause
