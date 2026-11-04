import os
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from huggingface_hub import HfApi, create_repo

def deploy():
    print("=" * 72)
    print("   TRIỂN KHAI ỨNG DỤNG ĐỌC TRUYỆN LÊN HUGGING FACE SPACES (24/7)")
    print("=" * 72)
    
    # 1. Ask for Hugging Face Token
    token = os.getenv("HF_TOKEN", "").strip()
    if not token:
        print("\n[?] Bạn cần một Hugging Face Access Token có quyền 'Write'.")
        print("    -> Vào link này để lấy hoặc tạo token: https://huggingface.co/settings/tokens")
        token = input("\nNhập Access Token (bắt đầu bằng hf_...): ").strip()
    
    if not token:
        print("\n[!] Không có token, đã hủy thao tác.")
        return

    api = HfApi(token=token)
    try:
        user_info = api.whoami()
        username = user_info.get("name")
        print(f"\n[+] Đăng nhập thành công với tài khoản: {username}")
    except Exception as e:
        print(f"\n[!] Token không hợp lệ hoặc lỗi xác thực: {e}")
        return

    # 2. Space Name
    default_space = "novel-reader"
    space_name = input(f"\nNhập tên Space bạn muốn tạo [mặc định: {default_space}]: ").strip() or default_space
    # Clean space name to alphanumeric and hyphen
    clean_space = "".join(c if c.isalnum() or c == "-" else "-" for c in space_name.lower()).strip("-")
    repo_id = f"{username}/{clean_space}"

    # 3. Private or Public
    print("\nChọn chế độ hiển thị cho Space:")
    print("  1. Public  (Khuyên dùng: Đã có mã PIN cá nhân bảo vệ, mở trên điện thoại cực mượt)")
    print("  2. Private (Riêng tư: Yêu cầu đăng nhập tài khoản Hugging Face trên trình duyệt điện thoại)")
    choice = input("Lựa chọn (1 hoặc 2) [mặc định: 1]: ").strip()
    is_private = (choice == "2")

    print(f"\n[+] Đang khởi tạo Space: {repo_id} (Docker SDK)...")
    try:
        create_repo(
            repo_id=repo_id,
            token=token,
            repo_type="space",
            space_sdk="docker",
            private=is_private,
            exist_ok=True
        )
        print("[+] Đã kết nối Space thành công!")
    except Exception as e:
        print(f"[!] Lỗi khởi tạo Space: {e}")
        return

    # 4. Upload folder
    base_dir = Path(__file__).resolve().parent
    print(f"\n[+] Đang đồng bộ toàn bộ mã nguồn & kho truyện lên Hugging Face...")
    try:
        api.upload_folder(
            folder_path=str(base_dir),
            repo_id=repo_id,
            repo_type="space",
            token=token,
            ignore_patterns=[
                ".venv/**",
                "venv/**",
                "**/__pycache__/**",
                "*.pyc",
                ".git/**",
                ".vscode/**",
                "*.log"
            ]
        )
        print("\n" + "=" * 72)
        print("   🎉 CHÚC MỪNG! ĐÃ TẢI LÊN HUGGING FACE SPACES THÀNH CÔNG!")
        print("=" * 72)
        print(f"\n📱 LINK ĐỌC TRUYỆN TRÊN ĐIỆN THOẠI (Chạy 24/7):")
        print(f"   -> Link Web Trực Tiếp: https://{username.lower()}-{clean_space}.hf.space")
        print(f"   -> Trang Quản Lý Space: https://huggingface.co/spaces/{repo_id}")
        print("\n💡 HƯỚNG DẪN BẢO MẬT & ĐỌC TRÊN ĐIỆN THOẠI:")
        print("   1. Đợi 1-2 phút để Hugging Face build Docker hoàn tất (Status hiện 'Running').")
        print("   2. Mở link trên điện thoại -> Nhập mã PIN cá nhân -> Tích 'Ghi nhớ trên máy này'.")
        print("   3. Chọn 'Thêm vào màn hình chính' (Add to Home Screen) để thành App riêng biệt!")
        print("=" * 72)
    except Exception as e:
        print(f"\n[!] Lỗi khi tải lên Space: {e}")

if __name__ == "__main__":
    deploy()
