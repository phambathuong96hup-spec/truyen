import re
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 1. Load single character Han-Viet dictionary from VietPhrase.txt
hanviet_char_map = {}
if os.path.exists('data/VietPhrase.txt'):
    with open('data/VietPhrase.txt', 'r', encoding='utf-16-le', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line or '=' not in line:
                continue
            parts = line.split('=', 1)
            k, v = parts[0].strip(), parts[1].strip()
            if len(k) == 1 and k not in hanviet_char_map:
                # pick first translation
                trans = v.split('/')[0].strip()
                hanviet_char_map[k] = trans

print(f"Loaded {len(hanviet_char_map)} Han-Viet character mappings.")

import re
import json
import os
import sys
import zhconv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 1. Load single character Han-Viet dictionary from VietPhrase.txt
hanviet_char_map = {}
if os.path.exists('data/VietPhrase.txt'):
    with open('data/VietPhrase.txt', 'r', encoding='utf-16-le', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line or '=' not in line:
                continue
            parts = line.split('=', 1)
            k, v = parts[0].strip(), parts[1].strip()
            if len(k) == 1 and k not in hanviet_char_map:
                trans = v.split('/')[0].strip()
                hanviet_char_map[k] = trans

# 2. Load Unihan kVietnamese
unihan_map = {}
if os.path.exists('data/hanviet_unihan.json'):
    try:
        with open('data/hanviet_unihan.json', 'r', encoding='utf-8') as f:
            unihan_map = json.load(f)
    except Exception:
        pass

# Fallbacks for common particles / missed chars
FALLBACKS = {
    '了': 'liễu',
    '的': 'của',
    '银': 'ngân',
    '发': 'phát',
    '戮': 'lục',
    '着': 'trứ',
    '把': 'đem',
    '被': 'bị',
    '给': 'cho',
    '让': 'để',
    '从': 'từ',
    '到': 'đến',
    '在': 'tại',
    '中': 'trung',
    '上': 'thượng',
    '下': 'hạ',
    '前': 'tiền',
    '后': 'hậu',
    '里': 'lý',
    '外': 'ngoại',
}

# 3. Key phrases and character names specific to Novel 6 & Xianxia/Sac Hiep
COMMON_FIXES = {
    "Cold Youyou": "Lãnh U U",
    "Cold幽幽": "Lãnh U U",
    "Coldyouyou": "Lãnh U U",
    "Coldyoudi": "Lãnh U U",
    "Lãnh Youyou": "Lãnh U U",
    "冷幽幽": "Lãnh U U",
    "幽幽": "U U",
    "露茜娅": "Lộ Thiến Á",
    "露西亚": "Lộ Thiến Á",
    "如意冰蚕丝": "Như Ý Băng Tằm Ty",
    "如意冰蚕": "Như Ý Băng Tằm",
    "苍澜大陆": "đại lục Thương Lam",
    "苍澜": "Thương Lam",
    "蒼澜": "Thương Lam",
    "腾龙城": "thành Đằng Long",
    "腾龙": "Đằng Long",
    "西门无恨": "Tây Môn Vô Hận",
    "雪儿": "Tuyết Nhi",
    "狂雷兽": "Cuồng Lôi Thú",
    "银背地龙": "Ngân Bối Địa Long",
    "黑暗魔玉": "Hắc Ám Ma Ngọc",
    "大地之熊": "Đại Địa Chi Hùng",
    "乾坤大挪移": "Càn Khôn Đại Na Di",
    "狂龙帝国": "Cuồng Long Đế Quốc",
    "幽冥圣女": "U Minh Thánh Nữ",
    "光明圣女": "Quang Minh Thánh Nữ",
    "光明神": "Quang Minh Thần",
    "异世之风流大法师": "Phong Lưu Đại Pháp Sư",
    "Long một": "Long Nhất",
    "Dragon One": "Long Nhất",
    "Princess": "Công chúa",
    "princess": "công chúa",
    "moment": "khoảnh khắc",
    "almost faint": "gần như ngất đi",
    "自制力": "khả năng tự chủ",
    "小家伙": "tiểu gia hỏa",
    "赶紧": "nhanh chóng",
    "老实": "thành thật",
    "丢兵弃甲": "tơi bời hoa lá",
    "那一霎": "trong một sát na",
    "那一刹那": "trong một sát na kia",
    "春光": "xuân quang",
    "迷情": "mê tình",
    "娇躯": "kiều khu",
    "呻吟": "rên rỉ",
    "喘息": "thở dốc",
    "酥麻": "tê dại",
    "温存": "ôn tồn hoan lạc",
    "缠绵": "triền miên",
    "瘫软": "mềm nhũn",
    # Máy dịch lỗi & tiếng Anh rác
    "chiếc áo ngực": "hộ tâm giáp",
    "cái áo ngực": "tấm hộ tâm giáp",
    "áo ngực": "hộ tâm giáp",
    "liền liền chút:điểm đầu": "gật đầu lia lịa",
    "liền liền chút điểm đầu": "gật đầu lia lịa",
    "chút:điểm đầu": "gật đầu",
    "chút điểm đầu": "gật đầu",
    "điểm đầu": "gật đầu",
    "chơi vơi mãi không thôi": "yêu thích không nỡ buông tay",
    "chơi vơi mãi": "say đắm ngắm nhìn",
    "viên cầu tinh anh": "thủy tinh cầu trong suốt",
    "tinh cầu tinh anh": "thủy tinh cầu",
    "bảo vệ quản": "bảo quản",
    "bảo vệ quản nó trước": "giữ hộ nó trước",
    "Đổ Vào Kho Gold": "Lạc Vào Động Vàng",
    "Kho Gold": "Động Vàng Hoàng Kim",
    "kho Gold": "động vàng hoàng kim",
    "Gold": "Hoàng kim",
    "gold": "hoàng kim",
    "secret": "mật đạo",
    "Secret": "Mật đạo",
    "magic đen": "hắc ma pháp",
    "Magic đen": "Hắc ma pháp",
    "magic": "ma pháp",
    "Magic": "Ma pháp",
    "seal magic": "phong ấn ma pháp",
    "seal": "phong ấn",
    "Seal": "Phong ấn",
    "arco tinh linh": "tinh linh cung",
    "arco": "cung tiễn",
    "Arco": "Cung tiễn",
    "what họ cần": "thứ họ cần",
    "Sleep": "say ngủ",
    "sleep": "say ngủ",
    "weak": "yếu ớt",
    "Weak": "Yếu ớt",
    "Harley": "Hạ Lê",
    "harley": "Hạ Lê",
    "Lucia": "Lộ Thiến Á",
    "lucia": "Lộ Thiến Á",
    "Lucius": "Lộ Thiến Á",
    "Blue Sky": "Lam Thiên",
    "blue sky": "lam thiên",
    "Wow": "Ôi",
    "wow": "ôi",
    "Wa!": "A!",
    "Wa,": "A,",
    "wa,": "a,",
    "wa!": "a!",
    "low một tiếng": "khẽ thốt lên một tiếng",
    "thấp giọng hô": "khẽ thốt lên",
    "tâm hồn thiếu nữ không khỏi một hồi kinh hoàng": "phương tâm không khỏi đập rộn ràng",
    "đau lòng cái chết": "đau lòng muốn chết",
    "giống cái": "nữ nhân",

}

def get_char_hanviet(ch: str) -> str:
    if ch in FALLBACKS:
        return FALLBACKS[ch]
    if ch in hanviet_char_map:
        return hanviet_char_map[ch]
    trad = zhconv.convert(ch, 'zh-hant')
    if trad in hanviet_char_map:
        return hanviet_char_map[trad]
    if ch in unihan_map and unihan_map[ch]:
        return unihan_map[ch][0]
    if trad in unihan_map and unihan_map[trad]:
        return unihan_map[trad][0]
    return ch

def clean_translated_text(text: str) -> str:
    if not text:
        return ""
    
    # Step 1: Apply phrase fixes
    for k, v in COMMON_FIXES.items():
        text = text.replace(k, v)
        
    # Step 2: Replace remaining Chinese character sequences with Han-Viet
    def replace_chinese(match):
        zh_str = match.group(0)
        if zh_str in COMMON_FIXES:
            return COMMON_FIXES[zh_str]
        res = [get_char_hanviet(c) for c in zh_str]
        return " " + " ".join(res) + " "

    # Match any Chinese characters
    text = re.sub(r'[\u4e00-\u9fff]+', replace_chinese, text)
    
    # Step 3: Clean up redundant spaces and formatting
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r' \n', '\n', text)
    text = re.sub(r'\n ', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()

if __name__ == '__main__':
    # Test on Chapter 2 snippet
    sample = "Trên đất蒼澜, đế quốc Long Long, thành腾龙, đêm xuống... Long Nhất ngạc nhiên nhìn那块 ánh sáng... Cold幽幽 khẽ thở dài..."
    print("Before:", sample)
    print("After :", clean_translated_text(sample))
