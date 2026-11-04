---
title: Novel AI Reader
emoji: 📖
colorFrom: indigo
colorTo: sky
sdk: docker
app_port: 7860
pinned: false
---

# HỆ THỐNG CÀO, DỊCH TRUYỆN TRUNG QUỐC BẰNG AI & ĐỌC ĐA NỀN TẢNG (PC & MOBILE PWA)

Ứng dụng web tự động lấy truyện chữ Trung Quốc (Web Novel), dịch sang tiếng Việt mượt mà bằng AI ngay trên máy chủ nội bộ (Local Machine) hoặc Cloud API, và cung cấp giao diện đọc truyện đồng bộ giữa PC và Điện thoại thông minh.

---

## 🌟 TÍNH NĂNG NỔI BẬT

### 1. Module Cào Truyện Đa Nguồn (Smart Scraper)
- **Cào tự động bằng URL:** Nhập link mục lục từ các web truyện lớn như `69shuba`, `biquge`, `uukanshu`, `piaotia`...
- **Bộ Custom CSS Selector Rules:** Lưu trong SQLite theo từng domain, tùy biến selector tiêu đề, mục lục, nội dung chương, bộ lọc quảng cáo.
- **Auto-Detect Content:** Thuật toán tự động phân tích mật độ văn bản tiếng Trung để bóc tách nội dung chương ngay cả khi trang web chưa có cấu hình sẵn.
- **Tự động xử lý Encoding:** Hỗ trợ đầy đủ `GB18030`, `GBK`, `GB2312`, `Big5`, `UTF-8`.
- **Nhập Raw Text / Upload File TXT:** Dán text tiếng Trung hoặc tải file `.txt`, hệ thống tự động tách chương theo Regex (`第...章`).

### 2. Pipeline Dịch Thuật AI Chuyên Sâu (AI Novel Translator)
- **Chuẩn OpenAI-Compatible API:** Kết nối mượt mà với Ollama (`http://localhost:11434/v1`), LM Studio, vLLM, DeepSeek, Gemini, OpenAI...
- **System Prompt Tiểu Thuyết:** Tối ưu hóa cho văn phong Tiên hiệp, Huyền huyễn, Kiếm hiệp, Đô thị, giữ trọn sắc thái xưng hô (`ta - ngươi`, `huynh - đệ`, `sư phụ - đồ nhi`, `tiền bối - vãn bối`...).
- **Hệ thống Glossary / Từ Điển Tên Riêng:**
  - Mỗi bộ truyện có bảng Từ Điển riêng (Nhân vật, Cảnh giới, Môn phái, Địa danh, Công pháp, Pháp bảo).
  - Tự động lọc các từ xuất hiện trong chương và đính kèm vào Prompt để AI dịch đồng nhất 100% suốt hàng nghìn chương.
  - Nút **"Trích xuất tên riêng bằng AI"** tự động phát hiện nhân vật / thuật ngữ mới trong chương để thêm vào Glossary với 1 click.
- **Hàng Đợi Dịch Ngầm & Dịch Trước (Background Pre-fetching Queue):**
  - Đang đọc Chương `N`, hệ thống tự động đưa Chương `N+1` và `N+2` vào hàng đợi dịch ngầm ở máy chủ. Đọc xong bấm "Chương sau" là có sẵn bản dịch ngay.
  - Hỗ trợ dịch trực tiếp theo luồng (Streaming SSE) nếu mở chương chưa kịp dịch trước.

### 3. Giao Diện Đọc Đa Nền Tảng (PC & Mobile PWA)
- **PWA (Progressive Web App):** Hỗ trợ "Thêm vào màn hình chính" (Add to Home Screen) trên iPhone/iPad và Android như ứng dụng bản địa, toàn màn hình, không thanh địa chỉ trình duyệt.
- **Đồng Bộ Tiến Độ Đọc (Cross-Device Sync):** Lưu chương đang đọc và vị trí cuộn trang (`scroll_position`) vào server. Đọc dở trên PC, cầm điện thoại lên là đọc tiếp đúng đoạn đó.
- **4 Chế Độ Màu Nền:** Tối (OLED Dark #090d16), Vàng dịu mắt (Sepia #f7efe1), Xanh rêu (Forest #eaf1e7), Sáng (Light #ffffff).
- **Typography Tùy Chỉnh:** Font Literata, Merriweather, Be Vietnam Pro, Roboto, Palatino. Tùy chỉnh cỡ chữ, giãn dòng, độ rộng khung đọc.
- **Chế Độ Song Ngữ:** Bật/tắt hiển thị câu gốc tiếng Trung ngay dưới câu dịch để đối chiếu.
- **Phím Tắt & Cảm Ứng:** PC dùng `Mũi tên Trái / Phải`. Điện thoại chạm viền trái/phải để chuyển chương, chạm giữa màn hình để ẩn/hiện thanh công cụ.

---

## 🚀 HƯỚNG DẪN KHỞI CHẠY NHANH

### Cách 1: Chạy bằng file `start.bat` (Khuyên dùng trên Windows)
Chỉ cần nhấp đúp vào file `start.bat`.

### Cách 2: Chạy bằng dòng lệnh Terminal
```bash
# Kích hoạt môi trường ảo
.venv\Scripts\activate

# Khởi chạy server
python run.py
```

Khi khởi động, console sẽ in ra địa chỉ truy cập:
- **Trên máy tính (PC):** `http://localhost:8000`
- **Trên điện thoại (Chung Wi-Fi):** `http://<IP_LAN_CUA_MAY>:8000` (ví dụ: `http://192.168.1.15:8000`)

---

## 📱 CÀI ĐẶT LÊN ĐIỆN THOẠI (PWA)

1. Đảm bảo điện thoại và máy tính kết nối **chung mạng Wi-Fi**.
2. Mở trình duyệt trên điện thoại và truy cập địa chỉ IP máy tính (ví dụ: `http://192.168.1.x:8000`).
3. **Trên iOS (Safari):**
   - Bấm nút **Chia sẻ** (biểu tượng mũi tên đi lên ở thanh dưới cùng).
   - Chọn **Thêm vào MH chính** (Add to Home Screen).
4. **Trên Android (Chrome):**
   - Bấm nút menu **3 chấm** ở góc trên bên phải.
   - Chọn **Cài đặt ứng dụng** (Install App) hoặc **Thêm vào Màn hình chính**.

---

## ⚙️ KẾT NỐI VỚI AI DỊCH THUẬT

Vào mục **Cài đặt AI** (biểu tượng bánh răng ở góc trên màn hình web):
1. **Dùng Ollama trên máy tính:**
   - Cài đặt Ollama và tải model: `ollama run qwen2.5:7b`
   - Base URL: `http://localhost:11434/v1`
   - Bấm nút **"Fetch Models từ Server"** để chọn model `qwen2.5:7b`.
2. **Dùng LM Studio:**
   - Bật Local Server trong LM Studio (cổng mặc định `1234`).
   - Base URL: `http://localhost:1234/v1`
3. **Dùng Cloud API (DeepSeek, OpenAI, v.v.):**
   - Base URL: `https://api.deepseek.com/v1`
   - Nhập API Key của bạn.
   - Model: `deepseek-chat`
4. Bấm **"Test Connection"** để kiểm tra phản hồi.
