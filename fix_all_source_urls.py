# -*- coding: utf-8 -*-
import sqlite3
import httpx
from bs4 import BeautifulSoup

INDEX_URL = "https://www.piaotia.com/html/9/9640/index.html"
BASE_URL = "https://www.piaotia.com/html/9/9640/"

resp = httpx.get(INDEX_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20.0)
soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='gbk')

links = soup.find_all('a')
chapter_links = []
for a in links:
    href = a.get('href', '')
    text = a.get_text().strip()
    if href and href.endswith('.html') and href != 'index.html' and 'bookinfo' not in href:
        full_url = BASE_URL + href if not href.startswith('http') else href
        chapter_links.append((text, full_url))

print(f"Tổng số chương lấy được từ index: {len(chapter_links)}")

conn = sqlite3.connect('data/novels.db')
c = conn.cursor()

# Cập nhật source_url và title cho toàn bộ 1443 chương
for idx, (title, url) in enumerate(chapter_links, 1):
    c.execute("""
        UPDATE chapters 
        SET source_url = ?, title = ?
        WHERE novel_id = 61 AND chapter_index = ?
    """, (url, title, idx))

conn.commit()
c.execute("PRAGMA wal_checkpoint(FULL);")

# Kiểm tra lại chapters 6-10
c.execute("SELECT chapter_index, title, source_url FROM chapters WHERE novel_id = 61 AND chapter_index BETWEEN 6 AND 15 ORDER BY chapter_index")
rows = c.fetchall()
print("\n--- KIỂM TRA CHAPTERS 6 - 15 ---")
for r in rows:
    print(r)

conn.close()
