with open('backend/discover.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''    {
        "id": "sys_8",
        "title": "全球高武",
        "title_vi": "Toàn Cầu Cao Võ",
        "author": "老鹰吃小鸡",
        "author_vi": "Lão Ưng Cật Tiểu Kê",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.8tsw.com/files/article/image/8/8912/8912s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/8_8912/",
        "views": "10.1M",
        "views_count": 10100000,
        "rating": 9.8,
        "total_chapters": 1432,
        "tags": ["Hệ Thống Tiền", "Phương Bình", "Địa Quật", "Chiến Tranh"],
        "description_vi": "Phương Bình trọng sinh vào thế giới võ giả chí thượng, nơi nhân loại đang phải chiến đấu ngầm với Địa Quật quái vật dưới lòng đất. Với hệ thống kiếm tiền tăng khí huyết, Phương Bình điên cuồng làm giàu để bảo vệ nhân tộc!"
    }'''

replacement = '''    {
        "id": "sys_8",
        "title": "全球高武",
        "title_vi": "Toàn Cầu Cao Võ",
        "author": "老鹰吃小鸡",
        "author_vi": "Lão Ưng Cật Tiểu Kê",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.8tsw.com/files/article/image/8/8912/8912s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/9/9640/index.html",
        "views": "10.1M",
        "views_count": 10100000,
        "rating": 9.8,
        "total_chapters": 1443,
        "tags": ["Hệ Thống Tiền", "Phương Bình", "Địa Quật", "Chiến Tranh"],
        "description_vi": "Phương Bình trọng sinh vào thế giới võ giả chí thượng, nơi nhân loại đang phải chiến đấu ngầm với Địa Quật quái vật dưới lòng đất. Với hệ thống kiếm tiền tăng khí huyết, Phương Bình điên cuồng làm giàu để bảo vệ nhân tộc!"
    }'''

assert target in text, "Target not found in discover.py"
text = text.replace(target, replacement)

with open('backend/discover.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Targeted update of sys_8 in discover.py succeeded!")
