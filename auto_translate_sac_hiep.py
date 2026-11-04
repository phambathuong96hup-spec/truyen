import asyncio
import httpx
import sqlite3
import sys
import os
import re
import subprocess
import time
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

LOCAL_AI_URL = "http://127.0.0.1:11434/v1/chat/completions"
DB_PATH = "data/novels.db"

SYSTEM_PROMPT = (
    "Bạn là dịch giả tiểu thuyết Trung - Việt hàng đầu. "
    "Hãy dịch đoạn văn tiểu thuyết sau sang tiếng Việt sắc sảo, tự nhiên, mượt mà, "
    "đúng chuẩn văn phong tiểu thuyết sắc hiệp / tiên hiệp. "
    "Giữ nguyên tên riêng nhân vật và địa danh theo phiên âm Hán-Việt (ví dụ: Long Nhất, Tây Môn Vô Hận, Tuyết Nhi, v.v.). "
    "Dịch sát nghĩa, đầy đủ chi tiết cảnh sắc, không cắt bỏ, không thêm lời bình hay giải thích."
)

def clean_piaotia_html(html_bytes: bytes) -> tuple[str, str]:
    soup = BeautifulSoup(html_bytes.decode('gbk', errors='ignore'), 'html.parser')
    h1 = soup.select_one('h1')
    title = h1.get_text().strip() if h1 else ""
    # remove unwanted elements
    for tag in soup(['script', 'style', 'table', 'center', 'ul', 'ol', 'form', 'nav', 'ins']):
        tag.decompose()
    text = soup.get_text()
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    filtered = []
    for line in lines:
        if any(kw in line for kw in ["飘天文学", "返回目录", "上一章", "下一章", "加入书签", "推荐本书", "选择背景", "fontbig"]):
            continue
        filtered.append(line)
    
    clean_text = "\n\n".join(filtered)
    return title, clean_text

def smart_chunk_text(text: str, max_chars: int = 750) -> list[str]:
    """Split text into bite-sized chunks so the local AI translates in ~15-20s without exceeding context"""
    paras = [p.strip() for p in re.split(r'\n+', text) if p.strip()]
    chunks = []
    curr = []
    curr_len = 0

    for p in paras:
        if len(p) > max_chars:
            # Sub-split long paragraph by Chinese punctuation
            sub_sentences = re.split(r'(?<=[。？！；\n])', p)
            for s in sub_sentences:
                s = s.strip()
                if not s:
                    continue
                if curr_len + len(s) > max_chars and curr:
                    chunks.append("\n\n".join(curr))
                    curr = [s]
                    curr_len = len(s)
                else:
                    curr.append(s)
                    curr_len += len(s)
        else:
            if curr_len + len(p) > max_chars and curr:
                chunks.append("\n\n".join(curr))
                curr = [p]
                curr_len = len(p)
            else:
                curr.append(p)
                curr_len += len(p)

    if curr:
        chunks.append("\n\n".join(curr))

    return chunks

async def translate_chunk_with_local_ai(client: httpx.AsyncClient, chunk: str) -> str:
    payload = {
        "model": "qwen",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Dịch đoạn sau sang tiếng Việt:\n\n{chunk}"}
        ],
        "temperature": 0.3,
        "max_tokens": 1000,
        "stream": False
    }
    resp = await client.post(LOCAL_AI_URL, json=payload, timeout=90.0)
    if resp.status_code != 200:
        raise ValueError(f"Local AI Error {resp.status_code}: {resp.text}")
    res_json = resp.json()
    msg = res_json["choices"][0]["message"]
    text = (msg.get("content") or "").strip()
    return text

def git_commit_and_push(msg: str):
    """Automatically commit updated database and push to GitHub repository"""
    try:
        subprocess.run(["git", "add", "data/novels.db"], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", msg], check=True, capture_output=True)
        push_res = subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True, text=True)
        print(f"     [🚀 GitHub] Đã đẩy dữ liệu mới lên GitHub thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"     [!] Git push note: {e}")
        return False

async def translate_chapter(client: httpx.AsyncClient, ch_id: int, novel_id: int, ch_index: int, title: str, source_url: str, raw_content: str) -> bool:
    print(f"\n---> [Chương {ch_index}] Đang dịch: {title}")

    # 1. Fetch raw content if needed
    if not raw_content or len(raw_content.strip()) < 100 or "正文内容待抓取" in raw_content:
        if "piaotia.com" in source_url:
            print(f"     [Cào] Đang tải từ {source_url}...")
            res = await client.get(source_url, timeout=15.0)
            parsed_title, text = clean_piaotia_html(res.content)
            if len(text) > 100:
                raw_content = text
                if parsed_title:
                    title = parsed_title
    
    if not raw_content or len(raw_content.strip()) < 50:
        print(f"     [!] Bỏ qua: Không lấy được nội dung chương {ch_index}")
        return False

    # 2. Translate Title
    title_payload = {
        "model": "qwen",
        "messages": [
            {"role": "system", "content": "Dịch tiêu đề chương truyện sang tiếng Việt, giữ âm Hán-Việt cho tên riêng (ví dụ: Chương 6: Siêu Cấp Không Gian Giới Chỉ). Chỉ trả về duy nhất tên tiêu đề dịch, không giải thích:"},
            {"role": "user", "content": title}
        ],
        "temperature": 0.2,
        "max_tokens": 80
    }
    title_resp = await client.post(LOCAL_AI_URL, json=title_payload, timeout=20.0)
    translated_title = title_resp.json()["choices"][0]["message"]["content"].strip()
    translated_title = translated_title.replace('"', '').replace("'", "").strip()
    print(f"     [Tiêu đề dịch]: {translated_title}")

    # 3. Translate Chunks with smart chunking
    chunks = smart_chunk_text(raw_content, max_chars=750)
    print(f"     [Dịch] Chia thành {len(chunks)} đoạn dịch tối ưu...")
    translated_pieces = []
    
    for idx, chunk in enumerate(chunks, 1):
        print(f"       Đoạn {idx}/{len(chunks)} ({len(chunk)} ký tự)...", end="", flush=True)
        tr = await translate_chunk_with_local_ai(client, chunk)
        translated_pieces.append(tr)
        print(" OK!")

    full_translation = "\n\n".join(translated_pieces)

    # 4. Save to DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        UPDATE chapters 
        SET title = ?, title_translated = ?, raw_content = ?, translated_content = ?, translation_status = 'completed', error_message = NULL
        WHERE id = ?
    """, (title, translated_title, raw_content, full_translation, ch_id))
    conn.commit()
    conn.close()

    print(f"     [✓] Hoàn thành Chương {ch_index} ({len(full_translation)} ký tự tiếng Việt)")
    return True

async def run_continuous_worker(novel_id: int = 6, batch_size: int = 5, loop: bool = False):
    print("=======================================================================")
    print(f"   DỊCH TỰ ĐỘNG BẰNG AI LOCAL (Novel ID: {novel_id}, Loop: {loop})")
    print("=======================================================================")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    while True:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            SELECT id, novel_id, chapter_index, title, source_url, raw_content 
            FROM chapters 
            WHERE novel_id = ? AND translation_status != 'completed'
            ORDER BY chapter_index ASC
            LIMIT ?
        """, (novel_id, batch_size))
        pending_chapters = c.fetchall()
        conn.close()

        if not pending_chapters:
            print(f"[!] Tiểu thuyết {novel_id} đã dịch xong toàn bộ hoặc không còn chương chờ!")
            if not loop:
                break
            print("[Zzz] Nghỉ 30 giây rồi kiểm tra lại...")
            await asyncio.sleep(30)
            continue

        print(f"\n[+] Bắt đầu dịch đợt {len(pending_chapters)} chương tiếp theo...")
        translated_in_batch = 0
        async with httpx.AsyncClient(headers=headers) as client:
            for row in pending_chapters:
                ch_id, n_id, ch_idx, title, s_url, raw = row
                try:
                    success = await translate_chapter(client, ch_id, n_id, ch_idx, title, s_url, raw)
                    if success:
                        translated_in_batch += 1
                except Exception as e:
                    print(f"     [X] Lỗi khi dịch chương {ch_idx}: {e}")

        # Auto Git Commit & Push every batch
        if translated_in_batch > 0:
            last_ch = pending_chapters[-1][2]
            commit_msg = f"auto: translate novel {novel_id} up to chapter {last_ch}"
            print(f"[+] Đang đồng bộ CSDL lên GitHub ({commit_msg})...")
            git_commit_and_push(commit_msg)

        if not loop:
            print("\n[+] Đợt dịch đã hoàn tất thành công!")
            break

if __name__ == '__main__':
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    novel_id = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    is_loop = "--loop" in sys.argv
    asyncio.run(run_continuous_worker(novel_id=novel_id, batch_size=limit, loop=is_loop))
