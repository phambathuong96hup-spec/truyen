@echo off
cd /d "%~dp0"
chcp 65001 >nul
title Trien Khai Web Doc Truyen Len Hugging Face Spaces

echo =======================================================================
echo          TRIEN KHAI UNG DUNG LEN HUGGING FACE SPACES [24/7]
echo =======================================================================
echo.

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" deploy_hf.py
    goto end
)

python deploy_hf.py

:end
echo.
pause
