# -*- coding: utf-8 -*-
import sqlite3
import httpx
from bs4 import BeautifulSoup
import re

def clean_piaotia(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = httpx.get(url, headers=headers, timeout=20.0)
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='gbk')
    h1 = soup.find('h1')
    title = h1.get_text().strip() if h1 else ""
    title = re.sub(r'^全球高武\s*', '', title)
    for tag in soup(['script', 'style', 'table', 'center', 'ul', 'ol', 'form', 'nav', 'ins', 'span']):
        tag.decompose()
    text = soup.get_text()
    text = text.replace('\xa0\xa0\xa0\xa0', '\n\n').replace('\u3000\u3000', '\n\n')
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    filtered = []
    ad_kws = ['飘天文学', '返回目录', '上一章', '下一章', '加入书签', '推荐本书', '收藏本书', '选择背景', 'fontbig', '书籍介绍', '我的书架', '加入书架', '繁體中文', '重要声明', '阅读更多小说最新章节']
    for l in lines:
        if len(l) < 150 and any(kw in l for kw in ad_kws):
            continue
        if any(ad in l for ad in ['重要声明：小说“全球高武”', '小说阅读网永久地址', 'Copyright ©']):
            continue
        if l == title or l == f'全球高武 {title}':
            continue
        filtered.append(l)
    return title, '\n\n'.join(filtered)

conn = sqlite3.connect('data/novels.db')
cur = conn.cursor()
cur.execute('SELECT chapter_index, source_url FROM chapters WHERE novel_id=61 AND chapter_index BETWEEN 11 AND 15 ORDER BY chapter_index')
for ch_idx, url in cur.fetchall():
    t, c = clean_piaotia(url)
    with open(f'ch{ch_idx}_raw.txt', 'w', encoding='utf-8') as f:
        f.write(t + '\n\n' + c)
    print(f'Ch {ch_idx}: {t} saved, chars: {len(c)}')
