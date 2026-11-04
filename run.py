import socket
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import uvicorn
from backend.config import HOST, PORT

def get_lan_ip() -> str:
    """Detect the local LAN IP address of this computer"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable, just used to detect the default outgoing interface
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def print_banner(lan_ip: str, port: int):
    banner = f"""
================================================================================
       HỆ THỐNG CÀO, DỊCH TRUYỆN TRUNG QUỐC BẰNG AI & ĐỌC ĐA NỀN TẢNG (PWA)
================================================================================

  [+] Máy chủ Backend FastAPI & Frontend PWA đã sẵn sàng!

  💻 TRUY CẬP TRÊN MÁY TÍNH (PC):
     -> http://localhost:{port}
     -> http://127.0.0.1:{port}

  📱 TRUY CẬP TRÊN ĐIỆN THOẠI (iOS / Android - Chung Wi-Fi):
     -> http://{lan_ip}:{port}

  💡 HƯỚNG DẪN CÀI ĐẶT PWA LÊN ĐIỆN THOẠI:
     - iOS (Safari): Mở link trên -> Bấm nút 'Chia sẻ' (Share) -> Chọn 'Thêm vào MH chính' (Add to Home Screen).
     - Android (Chrome): Mở link trên -> Bấm menu 3 chấm -> Chọn 'Cài đặt ứng dụng' (Install App).

  ⚙️  AI Translation Engine: OpenAI-Compatible (Ollama, LM Studio, vLLM, DeepSeek...)
================================================================================
"""
    print(banner)

def main():
    lan_ip = get_lan_ip()
    print_banner(lan_ip, PORT)
    uvicorn.run(
        "backend.main:app",
        host=HOST,
        port=PORT,
        reload=False
    )

if __name__ == "__main__":
    main()
