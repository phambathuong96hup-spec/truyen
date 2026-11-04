import sys
import time
import json
import os
import re
import random
import httpx
from bs4 import BeautifulSoup

sys.path.append('.')
sys.stdout.reconfigure(encoding='utf-8')

from backend.scraper import detect_and_decode
from backend.hanviet import to_sino_vietnamese

def build_cache():
    print("Fetching xiaoshuodaquan from 8tsw.com (Biquge mirror)...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    resp = httpx.get("https://www.8tsw.com/xiaoshuodaquan/", headers=headers, timeout=20.0)
    html = detect_and_decode(resp.content)
    soup = BeautifulSoup(html, "lxml")
    h2s = soup.find_all("h2")
    print(f"Found {len(h2s)} category blocks.")

    category_mapping = {
        "奇幻、玄幻小说大全列表": "huyen_huyen",
        "武侠、仙侠、修真小说大全列表": "huyen_huyen",
        "言情、都市小说大全列表": "do_thi",
        "历史、军事、穿越小说大全列表": "lich_su",
        "游戏、竞技、网游小说大全列表": "vong_du",
        "异灵、科幻小说大全列表": "linh_di"
    }

    cat_names = {
        "huyen_huyen": "Huyền Huyễn / Tiên Hiệp",
        "he_thong": "Hệ Thống",
        "trong_sinh": "Trọng Sinh / Xuyên Không",
        "do_thi": "Đô Thị / Thần Hào",
        "linh_di": "Linh Dị / Huyền Nghi",
        "sac_hau_cung": "Sắc / Hậu Cung",
        "lich_su": "Lịch Sử / Quân Sự",
        "vong_du": "Võng Du / Game"
    }

    all_novels = []
    seen_urls = set()

    for h2 in h2s:
        cat_text = h2.get_text()
        base_cat = category_mapping.get(cat_text, "huyen_huyen")
        ul = h2.find_next_sibling("ul")
        if not ul:
            continue
        for a in ul.find_all("a"):
            title = a.get_text().strip()
            href = a.get("href", "").strip()
            if not href or href in seen_urls:
                continue
            seen_urls.add(href)

            # Sub-genre detection
            cat = base_cat
            tags = []
            if any(w in title for w in ["系统", "签到", "面板", "外挂", "金手指"]):
                cat = "he_thong"
                tags.extend(["Hệ Thống", "Kim Thủ Chỉ"])
            elif any(w in title for w in ["重生", "穿越", "回到", "重回", "逆袭"]):
                cat = "trong_sinh"
                tags.extend(["Trọng Sinh", "Xuyên Không"])
            elif any(w in title for w in ["女帝", "后宫", "师尊", "仙子", "红颜", "绝色", "退婚", "冲师"]):
                cat = "sac_hau_cung"
                tags.extend(["Hậu Cung", "Đa Nữ Chủ"])
            elif any(w in title for w in ["诡异", "盗墓", "恐怖", "灵异", "悬疑", "镇魂", "妖魔"]):
                cat = "linh_di"
                tags.extend(["Linh Dị", "Huyền Nghi"])
            elif any(w in title for w in ["三国", "大明", "大秦", "唐朝", "皇帝", "权谋", "暴君", "皇子"]):
                cat = "lich_su"
                tags.extend(["Lịch Sử", "Quân Sự"])
            elif any(w in title for w in ["网游", "游戏", "电竞", "领主", "全职", "玩家", "魔兽"]):
                cat = "vong_du"
                tags.extend(["Võng Du", "Trò Chơi"])
            elif any(w in title for w in ["神豪", "都市", "首富", "校花", "赘婿", "医圣"]):
                cat = "do_thi"
                tags.extend(["Đô Thị", "Sảng Văn"])
            else:
                tags.extend(["Tiên Hiệp", "Huyền Huyễn"])

            m = re.search(r'/(\d+)_(\d+)/', href)
            nid = f"{m.group(1)}_{m.group(2)}" if m else str(abs(hash(href)) % 1000000)
            cover = f"https://www.8tsw.com/files/article/image/{m.group(1)}/{m.group(2)}/{m.group(2)}s.jpg" if m else "https://www.8tsw.com/images/defaultcover.jpg"

            views_cnt = random.randint(650000, 6800000)
            views_str = f"{views_cnt / 1000000:.1f}M"
            rating = round(random.uniform(9.4, 9.9), 1)
            total_chaps = random.randint(450, 3200)

            title_vi = to_sino_vietnamese(title)

            all_novels.append({
                "id": f"live_{nid}",
                "title": title,
                "title_vi": title_vi,
                "author": "Đang lấy",
                "author_vi": "Tác giả mạng",
                "category": cat,
                "category_name": cat_names.get(cat, "Tiên Hiệp"),
                "cover_url": cover,
                "source_domain": "8tsw.com",
                "source_url": href if href.startswith("http") else f"https://www.8tsw.com{href}",
                "views": views_str,
                "views_count": views_cnt,
                "rating": rating,
                "total_chapters": total_chaps,
                "tags": tags[:3] + ["Sảng Văn", "Thịnh Hành"],
                "description_vi": f"Tiểu thuyết \"{title_vi}\" ({title}) thể loại {cat_names.get(cat, 'Huyền Huyễn')}. Cốt truyện gay cấn, nhân vật chính bá đạo đang được hàng triệu độc giả theo dõi trên mạng văn học Trung Quốc."
            })

    print(f"Successfully processed {len(all_novels)} novels!")
    os.makedirs("data", exist_ok=True)
    cache_path = os.path.join("data", "web_novels_cache.json")
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(all_novels, f, ensure_ascii=False)
    print(f"Saved to {cache_path}!")

    from collections import Counter
    print("Category breakdown:")
    for cat, count in Counter(n['category'] for n in all_novels).items():
        print(f"  - {cat} ({cat_names.get(cat, cat)}): {count} truyện")

if __name__ == "__main__":
    build_cache()
