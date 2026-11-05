import asyncio
import httpx
import sqlite3
import sys
import os
import re
import json
import subprocess
import time
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

LOCAL_AI_URL = "http://127.0.0.1:11434/v1/chat/completions"
DB_PATH = "data/novels.db"
PROGRESS_FILE = "data/translation_progress.json"

SAC_HIEP_NOVEL_IDS = [6, 7, 8, 9, 10, 11, 12, 13, 14]

SYSTEM_PROMPT = (
    "Bạn là dịch giả tiểu thuyết Trung - Việt hàng đầu. "
    "Hãy dịch đoạn văn tiểu thuyết sau sang tiếng Việt sắc sảo, tự nhiên, mượt mà, "
    "đúng chuẩn văn phong tiểu thuyết sắc hiệp / tiên hiệp. "
    "Giữ nguyên tên riêng nhân vật và địa danh theo phiên âm Hán-Việt (ví dụ: Long Nhất, Tây Môn Vô Hận, Tuyết Nhi, v.v.). "
    "Dịch sát nghĩa, đầy đủ chi tiết cảnh sắc, không cắt bỏ, không thêm lời bình hay giải thích."
)

def update_progress_file(novel_id: int, novel_title: str, ch_index: int, total_chapters: int, completed_count: int):
    data = {
        "current_novel_id": novel_id,
        "current_novel_title": novel_title,
        "last_translated_chapter": ch_index,
        "total_chapters": total_chapters,
        "completed_chapters": completed_count,
        "remaining_chapters": max(0, total_chapters - completed_count),
        "percentage": round(completed_count / total_chapters * 100, 2) if total_chapters else 0,
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def mark_novel_completed(novel_id: int, novel_title: str, total_chapters: int):
    report = {
        "status": "COMPLETED",
        "novel_id": novel_id,
        "novel_title": novel_title,
        "total_chapters": total_chapters,
        "completed_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        report_path = f"data/novel_{novel_id}_completed_report.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    msg = f"🎉 HOAN TAT TRON BO: {novel_title} ({total_chapters} chuong)"
    git_commit_and_push(msg)
    print("\n" + "="*80)
    print(f"   [🎉 CHÚC MỪNG] ĐÃ HOÀN TẤT TRỌN BỘ 100%: {novel_title} ({total_chapters} chương)!")
    print("="*80 + "\n")

def clean_piaotia_html(html_bytes: bytes) -> tuple[str, str]:
    soup = BeautifulSoup(html_bytes.decode('gbk', errors='ignore'), 'html.parser')
    h1 = soup.select_one('h1')
    title = h1.get_text().strip() if h1 else ""
    for tag in soup(['script', 'style', 'table', 'center', 'ul', 'ol', 'form', 'nav', 'ins']):
        tag.decompose()
    for br in soup.find_all(['br', 'p']):
        br.replace_with('\n')
    text = soup.get_text()
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    filtered = []
    for line in lines:
        if len(line) < 150 and any(kw in line for kw in ["飘天文学", "返回目录", "上一章", "下一章", "加入书签", "推荐本书", "选择背景", "fontbig", "重要声明", "最新全本"]):
            continue
        if line == title:
            continue
        filtered.append(line)
    
    clean_text = "\n\n".join(filtered)
    return title, clean_text

def smart_chunk_text(text: str, max_chars: int = 500) -> list[str]:
    paras = [p.strip() for p in re.split(r'\n+', text) if p.strip()]
    chunks = []
    curr = []
    curr_len = 0

    for p in paras:
        if len(p) > max_chars:
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

async def translate_chunk_with_local_ai(client: httpx.AsyncClient, chunk: str, max_retries: int = 2) -> str:
    payload = {
        "model": "qwen",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Dịch đoạn sau sang tiếng Việt:\n\n{chunk}"}
        ],
        "temperature": 0.3,
        "max_tokens": 800,
        "stream": False
    }
    for attempt in range(max_retries + 1):
        try:
            resp = await client.post(LOCAL_AI_URL, json=payload, timeout=180.0)
            if resp.status_code != 200:
                raise ValueError(f"Local AI Error {resp.status_code}: {resp.text}")
            res_json = resp.json()
            msg = res_json["choices"][0]["message"]
            text = (msg.get("content") or "").strip()
            return text
        except Exception as e:
            if attempt < max_retries:
                await asyncio.sleep(2)
                continue
            raise e

def git_commit_and_push(msg: str):
    try:
        subprocess.run(["git", "add", "data/novels.db", "data/translation_progress.json"], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", msg], check=True, capture_output=True)
        push_res = subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True, text=True)
        print(f"     [🚀 GitHub] Đã đẩy dữ liệu mới lên GitHub thành công!")
        return True
    except subprocess.CalledProcessError as e:
        # If nothing to commit, return quietly
        if "nothing to commit" in str(e) or e.returncode == 1:
            return True
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
            {"role": "system", "content": f"Dịch tiêu đề chương {ch_index} sang tiếng Việt ngắn gọn, giữ âm Hán-Việt cho tên riêng (ví dụ: Chương {ch_index}: Đại Địa Chi Hùng). Chỉ trả về tiêu đề dịch, không giải thích:"},
            {"role": "user", "content": title}
        ],
        "temperature": 0.2,
        "max_tokens": 60
    }
    title_resp = await client.post(LOCAL_AI_URL, json=title_payload, timeout=30.0)
    translated_title = title_resp.json()["choices"][0]["message"]["content"].strip()
    translated_title = translated_title.replace('"', '').replace("'", "").strip()
    print(f"     [Tiêu đề dịch]: {translated_title}")

    # 3. Translate Chunks with smart chunking (500 chars max)
    chunks = smart_chunk_text(raw_content, max_chars=500)
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

    # Get novel stats
    c.execute("SELECT title, total_chapters FROM novels WHERE id = ?", (novel_id,))
    n_row = c.fetchone()
    novel_title = n_row[0] if n_row else ""
    total_caps = n_row[1] if n_row else 0

    c.execute("SELECT count(*) FROM chapters WHERE novel_id = ? AND translation_status = 'completed'", (novel_id,))
    comp_count = c.fetchone()[0]
    try:
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
    except Exception:
        pass
    conn.close()

    print(f"     [✓] Hoàn thành Chương {ch_index} ({len(full_translation)} ký tự tiếng Việt) | Tiến độ: {comp_count}/{total_caps}")
    
    # Update progress file
    update_progress_file(novel_id, novel_title, ch_index, total_caps, comp_count)

    # Auto sync to GitHub immediately after each chapter
    git_commit_and_push(f"auto: translate novel {novel_id} chapter {ch_index} ({comp_count}/{total_caps})")
    return True

async def run_full_pipeline(batch_size: int = 5):
    print("=======================================================================")
    print("   TIẾN TRÌNH DỊCH TOÀN BỘ TRUYỆN SẮC HIỆP BẰNG AI LOCAL (FULL PIPELINE)")
    print("=======================================================================")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    while True:
        # Find next novel that has pending chapters
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        current_novel = None
        for nid in SAC_HIEP_NOVEL_IDS:
            c.execute("SELECT id, title, total_chapters FROM novels WHERE id = ?", (nid,))
            nrow = c.fetchone()
            if not nrow:
                continue
            
            c.execute("SELECT count(*) FROM chapters WHERE novel_id = ? AND translation_status != 'completed'", (nid,))
            pending_count = c.fetchone()[0]
            if pending_count > 0:
                current_novel = (nrow[0], nrow[1], nrow[2], pending_count)
                break

        if not current_novel:
            print("\n[🎉🎉🎉] TẤT CẢ CÁC BỘ TRUYỆN SẮC HIỆP ĐÃ ĐƯỢC DỊCH HOÀN TẤT 100%!")
            conn.close()
            break

        novel_id, novel_title, total_chapters, pending_count = current_novel

        # Fetch next batch
        c.execute("""
            SELECT id, novel_id, chapter_index, title, source_url, raw_content 
            FROM chapters 
            WHERE novel_id = ? AND translation_status != 'completed'
            ORDER BY chapter_index ASC
            LIMIT ?
        """, (novel_id, batch_size))
        pending_chapters = c.fetchall()
        conn.close()

        print(f"\n[📚 Đang dịch]: {novel_title} (ID: {novel_id}) | Còn {pending_count} chương...")
        async with httpx.AsyncClient(headers=headers) as client:
            for row in pending_chapters:
                ch_id, n_id, ch_idx, title, s_url, raw = row
                try:
                    await translate_chapter(client, ch_id, n_id, ch_idx, title, s_url, raw)
                except Exception as e:
                    print(f"     [X] Lỗi khi dịch chương {ch_idx}: {type(e).__name__} - {e}")
                    await asyncio.sleep(3)

        # Check if this novel is now completely finished
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT count(*) FROM chapters WHERE novel_id = ? AND translation_status != 'completed'", (novel_id,))
        remaining = c.fetchone()[0]
        conn.close()

        if remaining == 0:
            mark_novel_completed(novel_id, novel_title, total_chapters)

if __name__ == '__main__':
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    asyncio.run(run_full_pipeline(batch_size=limit))
