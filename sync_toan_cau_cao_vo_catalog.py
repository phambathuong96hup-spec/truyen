# -*- coding: utf-8 -*-
"""
Đồng bộ toàn bộ mục lục 1,444 chương chuẩn nguyên tác của Toàn Cầu Cao Võ (ID: 61)
Nguồn cào: https://www.piaotia.com/html/9/9640/index.html
"""

import sqlite3
import httpx
from bs4 import BeautifulSoup
import datetime
import time

NOVEL_ID = 61
INDEX_URL = "https://www.piaotia.com/html/9/9640/index.html"
BASE_URL = "https://www.piaotia.com/html/9/9640/"

def sync_catalog():
    print(f"[*] Đang tải danh mục chương từ {INDEX_URL}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    resp = httpx.get(INDEX_URL, headers=headers, timeout=20.0)
    resp.encoding = 'gbk'
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='gbk')
    
    links = soup.find_all('a')
    chapter_list = []
    for a in links:
        href = a.get('href', '')
        text = a.get_text().strip()
        if href and href.endswith('.html') and href != 'index.html' and 'bookinfo' not in href:
            full_url = BASE_URL + href if not href.startswith('http') else href
            chapter_list.append((text, full_url))
            
    print(f"[✓] Đã tìm thấy {len(chapter_list)} chương nguyên tác!")
    
    conn = sqlite3.connect('data/novels.db', timeout=60.0)
    cursor = conn.cursor()
    
    # 1. Cập nhật thông tin truyện
    cursor.execute("""
        UPDATE novels 
        SET total_chapters = ?, 
            source_url = ?
        WHERE id = ?
    """, (len(chapter_list), INDEX_URL, NOVEL_ID))
    
    # 2. Lấy danh sách các chương hiện có trong DB
    cursor.execute("SELECT chapter_index, translation_status FROM chapters WHERE novel_id = ?", (NOVEL_ID,))
    existing = dict(cursor.fetchall())
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    inserted = 0
    updated = 0
    
    for idx, (ch_title, ch_url) in enumerate(chapter_list, 1):
        if idx in existing:
            # Nếu chương đã có và chưa hoàn thành, cập nhật title chuẩn và url chuẩn
            if existing[idx] != 'completed':
                cursor.execute("""
                    UPDATE chapters 
                    SET title = ?, source_url = ?, updated_at = ?
                    WHERE novel_id = ? AND chapter_index = ?
                """, (ch_title, ch_url, now_str, NOVEL_ID, idx))
                updated += 1
        else:
            # Thêm mới chương vào DB
            cursor.execute("""
                INSERT INTO chapters (
                    novel_id, chapter_index, title, title_translated, 
                    source_url, translation_status, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, 'pending', ?, ?)
            """, (
                NOVEL_ID, idx, ch_title, f"Chương {idx}: {ch_title}",
                ch_url, now_str, now_str
            ))
            inserted += 1
            
    conn.commit()
    cursor.execute("PRAGMA wal_checkpoint(FULL);")
    conn.close()
    
    print(f"[HOÀN TẤT] Đồng bộ catalog thành công! Đã thêm mới: {inserted} chương, Cập nhật: {updated} chương.")
    print(f"Tổng số chương hiện tại của Toàn Cầu Cao Võ trong DB: {len(chapter_list)}")

if __name__ == '__main__':
    sync_catalog()
