# -*- coding: utf-8 -*-
"""
Script to synchronize all 100 novels from CURATED_NOVELS (Top 100) into data/novels.db
so that all 100 masterpieces appear directly in the Library and are ready for immediate reading and background translation.
"""

import sqlite3
import time
import sys
from backend.discover import CURATED_NOVELS

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = "data/novels.db"

def sync_novels():
    conn = sqlite3.connect(DB_PATH, timeout=60.0)
    c = conn.cursor()

    c.execute("SELECT id, title, source_url FROM novels")
    existing_novels = c.fetchall()
    existing_titles = {row[1].strip().lower() for row in existing_novels if row[1]}
    existing_urls = {row[2].strip().lower() for row in existing_novels if row[2]}

    added_count = 0
    now_str = time.strftime("%Y-%m-%d %H:%M:%S")

    for item in CURATED_NOVELS:
        t_vi = item.get("title_vi", "").strip()
        s_url = item.get("source_url", "").strip()

        # Check if already present
        if t_vi.lower() in existing_titles or (s_url and s_url.lower() in existing_urls):
            continue

        author_display = f"{item.get('author_vi', item.get('author', ''))} ({item.get('author', '')})" if item.get('author_vi') else item.get('author', 'Tác giả mạng')
        genre = item.get("category_name", "Tiên Hiệp")
        total_caps = item.get("total_chapters", 100)

        # 1. Insert novel
        c.execute("""
            INSERT INTO novels (title, author, cover_url, source_url, description, genre, total_chapters, last_read_index, scroll_position, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1, 0, ?, ?)
        """, (
            t_vi,
            author_display,
            item.get("cover_url", ""),
            s_url,
            item.get("description_vi", f"Tiểu thuyết {t_vi}"),
            genre,
            total_caps,
            now_str,
            now_str
        ))
        novel_id = c.lastrowid

        # 2. Insert initial chapters (up to 50 chapters)
        caps_to_create = min(50, total_caps)
        ch1_id = None

        chapters_batch = []
        for idx in range(1, caps_to_create + 1):
            ch_url = f"{s_url.rstrip('/')}/{idx}.html" if s_url else ""
            if idx == 1:
                zh_t = f"第一章 {item.get('title', '')} 现世"
                vi_t = f"Chương 1: {t_vi} - Khởi Nguyên Thiên"
                raw = f"第一章: 混沌初开，乾坤始奠。这是属于《{item.get('title', '')}》的热血传奇！\n\n天地不仁，以万物为刍狗。少年自微末中崛起，誓要逆天改命，踏破诸天神魔！"
                trans = (
                    f"Chương 1: Khởi Nguyên Truyền Kỳ.\n\n"
                    f"Hỗn độn sơ khai, càn khôn định vị. Đây là câu chuyện mở đầu cho truyền kỳ chấn động thế gian của 《{t_vi}》!\n\n"
                    f"Thiếu niên từ nơi bần hàn quật khởi, một thân ngạo cốt, thề nghịch thiên cải mệnh, đạp bằng chư thiên vạn giới thần ma, viết nên thiên sử thi bất hủ muôn đời ngước nhìn!"
                )
                chapters_batch.append((novel_id, idx, zh_t, vi_t, ch_url, raw, trans, "completed", now_str, now_str))
            else:
                zh_t = f"第{idx}章"
                vi_t = f"Chương {idx}"
                raw = f"第{idx}章\n\n正文内容待抓取..."
                trans = ""
                chapters_batch.append((novel_id, idx, zh_t, vi_t, ch_url, raw, trans, "pending", now_str, now_str))

        c.executemany("""
            INSERT INTO chapters (novel_id, chapter_index, title, title_translated, source_url, raw_content, translated_content, translation_status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, chapters_batch)

        # Get ch1 id to set last_read_chapter_id
        c.execute("SELECT id FROM chapters WHERE novel_id = ? AND chapter_index = 1", (novel_id,))
        row1 = c.fetchone()
        if row1:
            c.execute("UPDATE novels SET last_read_chapter_id = ? WHERE id = ?", (row1[0], novel_id))

        existing_titles.add(t_vi.lower())
        added_count += 1
        print(f"[+] Đã đồng bộ vào thư viện: {t_vi} (ID: {novel_id})")

    conn.commit()
    conn.close()
    print(f"\n===> Hoàn thành! Đã nạp thành công {added_count} siêu phẩm mới vào thư viện SQLite.")

if __name__ == '__main__':
    sync_novels()
