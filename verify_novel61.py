import sqlite3

conn = sqlite3.connect('data/novels.db', timeout=60)
c = conn.cursor()

c.execute("SELECT count(*), sum(length(translated_content)) FROM chapters WHERE novel_id=61 AND translation_status='completed'")
total_done, total_chars = c.fetchone()
print(f"Novel 61 (Toan Cau Cao Vo) -> Completed chapters: {total_done}, Total translated characters: {total_chars:,}")

c.execute("SELECT chapter_index, title_translated, translation_status, length(translated_content) FROM chapters WHERE novel_id=61 AND translation_status='completed' ORDER BY chapter_index")
rows = c.fetchall()
for r in rows:
    print(f"  Chương {r[0]:02d}: {r[1]} [{r[2]}] ({r[3]:,} ký tự)")

conn.close()
