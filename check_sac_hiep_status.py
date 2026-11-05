import sqlite3
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('data/novels.db')
c = conn.cursor()

c.execute("SELECT id, title, total_chapters, source_url FROM novels WHERE id >= 6")
novels = c.fetchall()

print(f"{'ID':<4} | {'Title':<40} | {'Total':<6} | {'Completed':<10} | {'Pending':<8} | {'Progress'}")
print("-" * 85)

for n in novels:
    nid, title, total, s_url = n
    c.execute("SELECT count(*) FROM chapters WHERE novel_id = ? AND translation_status = 'completed'", (nid,))
    comp = c.fetchone()[0]
    c.execute("SELECT count(*) FROM chapters WHERE novel_id = ? AND translation_status != 'completed'", (nid,))
    pend = c.fetchone()[0]
    total_db = comp + pend
    pct = (comp / total_db * 100) if total_db > 0 else 0
    print(f"{nid:<4} | {title:<40} | {total_db:<6} | {comp:<10} | {pend:<8} | {pct:.1f}%")

conn.close()
