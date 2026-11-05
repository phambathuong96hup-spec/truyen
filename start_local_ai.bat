@echo off
title Local AI Translation Server (Qwen 4B Abliterated - Single Dedicated Slot)
chcp 65001 >nul

echo =======================================================================
echo     KHOI DONG SERVER AI LOCAL (Qwen 4B Abliterated - Dedicated Slot)
echo =======================================================================
echo.
echo [+] Dang khoi chay backend Llama/Vulkan (Reasoning=OFF, Slots=1, Context=2048)...
echo [+] Mo hinh: InterimLabs-Huihui-Qwen3.5-4B-abliterated
echo [+] Cong API OpenAI tuong thich: http://127.0.0.1:11434
echo.

cd /d "C:\Users\Pham Ba Thuong\.lmstudio\extensions\backends\llama.cpp-win-x86_64-vulkan-avx2-2.55.0"
llama-server.exe -m "C:\Users\Pham Ba Thuong\.lmstudio\models\interimlabs\InterimLabs-Huihui-Qwen3.5-4B-abliterated-GGUF-Q4_K_M\model.gguf" --port 11434 --host 127.0.0.1 -c 2048 -ngl 16 -t 6 -np 1 --reasoning off

pause
