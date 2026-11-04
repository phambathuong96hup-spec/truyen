import json
import os
import re
from typing import Optional
import zhconv

# Path to hanviet mapping
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HANVIET_PATH = os.path.join(BASE_DIR, "data", "hanviet.json")

_HV_MAP = None

def get_hv_map():
    global _HV_MAP
    if _HV_MAP is None:
        if os.path.exists(HANVIET_PATH):
            try:
                with open(HANVIET_PATH, "r", encoding="utf-8") as f:
                    _HV_MAP = json.load(f)
            except Exception:
                _HV_MAP = {}
        else:
            _HV_MAP = {}
    return _HV_MAP

# 300+ Most common web novel compounds & phrases
COMPOUND_PHRASES = [
    ("玄幻", "Huyền Huyễn"), ("仙侠", "Tiên Hiệp"), ("修真", "Tu Chân"), ("修仙", "Tu Tiên"),
    ("武侠", "Võ Hiệp"), ("都市", "Đô Thị"), ("言情", "Ngôn Tình"), ("历史", "Lịch Sử"),
    ("军事", "Quân Sự"), ("科幻", "Khoa Huyễn"), ("网游", "Võng Du"), ("灵异", "Linh Dị"),
    ("悬疑", "Huyền Nghi"), ("恐怖", "Khủng Bố"), ("后宫", "Hậu Cung"), ("纯爱", "Thuần Ái"),
    ("重生", "Trọng Sinh"), ("穿越", "Xuyên Không"), ("系统", "Hệ Thống"), ("签到", "Điểm Danh"),
    ("开局", "Khai Cục"), ("无敌", "Vô Địch"), ("反派", "Phản Phái"), ("大帝", "Đại Đế"),
    ("女帝", "Nữ Đế"), ("师尊", "Sư Tôn"), ("徒弟", "Đồ Đệ"), ("逆徒", "Nghịch Đồ"),
    ("圣子", "Thánh Tử"), ("圣女", "Thánh Nữ"), ("宗门", "Tông Môn"), ("老祖", "Lão Tổ"),
    ("神豪", "Thần Hào"), ("首富", "Thủ Phú"), ("百亿", "Trăm Tỷ"), ("千亿", "Nghìn Tỷ"),
    ("万亿", "Vạn Tỷ"), ("补贴", "Trợ Cấp"), ("获得", "Đạt Được"), ("机缘", "Cơ Duyên"),
    ("全族", "Toàn Tộc"), ("族人", "Tộc Nhân"), ("天命", "Thiên Mệnh"), ("投资", "Đầu Tư"),
    ("修为", "Tu Vi"), ("召唤", "Triệu Hoán"), ("护卫", "Hộ Vệ"), ("金身", "Kim Thân"),
    ("天帝", "Thiên Đế"), ("成神", "Thành Thần"), ("队伍", "Đội Ngũ"), ("踢出", "Đá Khỏi"),
    ("全球", "Toàn Cầu"), ("冰封", "Băng Phong"), ("末日", "Mạt Thế"), ("安全屋", "Nơi Trú Ẩn"),
    ("庇护所", "Pháo Đài Trú Ẩn"), ("斩神", "Trảm Thần"), ("诡异", "Quỷ Dị"), ("盗墓", "Đạo Mộ"),
    ("长生", "Trường Sinh"), ("苟道", "Cẩu Đạo"), ("深渊", "Vực Sâu"), ("主神", "Chủ Thần"),
    ("乐园", "Nhạc Viên"), ("进化", "Tiến Hóa"), ("吞噬", "Thôn Phệ"), ("星空", "Tinh Không"),
    ("完美", "Hoàn Mỹ"), ("遮天", "Già Thiên"), ("斗罗", "Đấu La"), ("斗破", "Đấu Phá"),
    ("苍穹", "Thương Khung"), ("凡人", "Phàm Nhân"), ("万古", "Vạn Cổ"), ("一世", "Nhất Thế"),
    ("武神", "Võ Thần"), ("剑神", "Kiếm Thần"), ("刀皇", "Đao Hoàng"), ("龙王", "Long Vương"),
    ("战神", "Chiến Thần"), ("赘婿", "Ở Rể"), ("奶爸", "Bố Bỉm"), ("学霸", "Học Bá"),
    ("文娱", "Văn Nghệ"), ("文豪", "Văn Hào"), ("巨星", "Siêu Sao"), ("退婚", "Thoái Hôn"),
    ("打脸", "Vả Mặt"), ("装逼", "Giả Vờ"), ("扮猪吃虎", "Giả Heo Ăn Thịt Hổ"),
    ("杀女证道", "Sát Nữ Chứng Đạo"), ("人设崩了", "Hình Tượng Sụp Đổ"),
    ("莫欺少年穷", "Đừng Khinh Thiếu Niên Nghèo"), ("莫欺中年穷", "Đừng Khinh Trung Niên Nghèo"),
    ("三十年河东", "Ba Mươi Năm Sông Đông"), ("我只想", "Ta Chỉ Muốn"), ("我真的", "Ta Thực Sự"),
    ("其实我是", "Thực Ra Ta Là"), ("这个世界", "Thế Giới Này"), ("诸天万界", "Chư Thiên Vạn Giới"),
    ("万族之劫", "Vạn Tộc Chi Kiếp"), ("轮回", "Luân Hồi"), ("宿命", "Túc Mệnh"),
    ("诡秘", "Quỷ Bí"), ("道诡", "Đạo Quỷ"), ("异仙", "Dị Tiên"), ("赤心", "Xích Tâm"),
    ("巡天", "Tuần Thiên"), ("剑来", "Kiếm Lai"), ("雪中", "Tuyết Trung"), ("悍刀行", "Hãn Đao Hành"),
    ("大奉", "Đại Phụng"), ("打更人", "Đả Canh Nhân"), ("择日飞升", "Trạch Nhật Phi Thăng"),
    ("不科学", "Bất Khoa Học"), ("御兽", "Ngự Thú"), ("宠兽", "Sủng Thú"), ("神级", "Thần Cấp"),
    ("神话", "Thần Thoại"), ("禁区", "Cấm Khu"), ("复苏", "Hồi Sinh"), ("降临", "Giáng Lâm"),
    ("入侵", "Xâm Lược"), ("领主", "Lãnh Chúa"), ("全民", "Toàn Dân"), ("城堡", "Lâu Đài"),
    ("兵种", "Binh Chủng"), ("网游之", "Võng Du Chi"), ("网游", "Võng Du"), ("全职", "Toàn Chức"),
    ("高手", "Cao Thủ"), ("巅峰", "Đỉnh Cao"), ("神座", "Thần Tọa"), ("王座", "Vương Tọa")
]

# Character-level corrections for web novel literary style
CHAR_CORRECTIONS = {
    '你': 'Nhĩ', '我': 'Ngã', '他': 'Tha', '她': 'Nàng', '它': 'Tha',
    '们': 'Môn', '这': 'Giá', '那': 'Na', '个': 'Cá', '把': 'Bả',
    '被': 'Bị', '在': 'Tại', '着': 'Trước', '了': 'Liễu', '过': 'Quá',
    '队': 'Đội', '踢': 'Thích', '快': 'Khoái', '都': 'Đô', '成': 'Thành',
    '神': 'Thần', '出': 'Xuất', '伍': 'Ngũ', '从': 'Tùng', '到': 'Đáo',
    '女': 'Nữ', '男': 'Nam', '设': 'Thiết', '崩': 'Băng', '人': 'Nhân',
    '穷': 'Cùng', '富': 'Phú', '岁': 'Tuổi', '金': 'Kim', '身': 'Thân',
    '帝': 'Đế', '皇': 'Hoàng', '宗': 'Tông', '门': 'Môn', '派': 'Phái',
    '天': 'Thiên', '地': 'Địa', '玄': 'Huyền', '幻': 'Huyễn', '仙': 'Tiên',
    '魔': 'Ma', '妖': 'Yêu', '鬼': 'Quỷ', '佛': 'Phật', '道': 'Đạo',
    '剑': 'Kiếm', '刀': 'Đao', '枪': 'Thương', '戟': 'Kích', '拳': 'Quyền',
    '掌': 'Chưởng', '指': 'Chỉ', '尊': 'Tôn', '王': 'Vương', '皇': 'Hoàng',
    '侯': 'Hầu', '将': 'Tướng', '相': 'Tướng', '杀': 'Sát', '灭': 'Diệt',
    '破': 'Phá', '立': 'Lập', '生': 'Sinh', '死': 'Tử', '劫': 'Kiếp',
    '运': 'Vận', '气': 'Khí', '力': 'Lực', '势': 'Thế', '威': 'Uy',
    '无': 'Vô', '极': 'Cực', '绝': 'Tuyệt', '万': 'Vạn', '千': 'Thiên',
    '百': 'Bách', '十': 'Thập', '一': 'Nhất', '二': 'Nhị', '三': 'Tam',
    '四': 'Tứ', '五': 'Ngũ', '六': 'Lục', '七': 'Thất', '八': 'Bát',
    '九': 'Cửu', '零': 'Linh', '谁': 'Thùy', '何': 'Hà', '怎': 'Chẩm',
    '么': 'Ma', '样': 'Dạng', '如': 'Như', '是': 'Thị', '非': 'Phi',
    '可': 'Khả', '以': 'Dĩ', '能': 'Năng', '要': 'Yếu', '想': 'Tưởng',
    '看': 'Khán', '听': 'Thính', '说': 'Thuyết', '话': 'Thoại', '走': 'Tẩu',
    '跑': 'Bào', '飞': 'Phi', '升': 'Thăng', '降': 'Hàng', '来': 'Lai',
    '去': 'Khứ', '回': 'Hồi', '归': 'Quy', '起': 'Khởi', '落': 'Lạc'
}

def to_sino_vietnamese(text: str) -> str:
    """Convert Chinese title or text into Sino-Vietnamese (Hán-Việt) reading"""
    if not text:
        return ""

    hv_map = get_hv_map()

    # Step 1: Replace multi-character compound phrases with placeholders
    working_text = text
    placeholders = {}
    p_idx = 0
    for zh_phrase, vi_phrase in COMPOUND_PHRASES:
        if zh_phrase in working_text:
            key = f"__PH{p_idx}__"
            placeholders[key] = vi_phrase
            working_text = working_text.replace(zh_phrase, f" {key} ")
            p_idx += 1

    # Step 2: Convert remainder to Traditional Chinese for better Unihan coverage
    try:
        hant = zhconv.convert(working_text, 'zh-hant')
    except Exception:
        hant = working_text

    # Step 3: Character by character conversion
    tokens = []
    i = 0
    while i < len(working_text):
        # Check placeholder
        matched_ph = None
        for k in placeholders:
            if working_text[i:].startswith(k):
                matched_ph = k
                break
        if matched_ph:
            tokens.append(placeholders[matched_ph])
            i += len(matched_ph)
            continue

        ch = working_text[i]
        ch_trad = hant[i] if i < len(hant) else ch

        if ch in CHAR_CORRECTIONS:
            tokens.append(CHAR_CORRECTIONS[ch])
        elif ch in hv_map:
            tokens.append(hv_map[ch][0].capitalize())
        elif ch_trad in hv_map:
            tokens.append(hv_map[ch_trad][0].capitalize())
        elif re.match(r'[a-zA-Z0-9]', ch):
            tokens.append(ch)
        elif ch in ['：', ':', '，', ',', '！', '!', '？', '?', '。', '.', '、', '—', '-', '·', ' ']:
            tokens.append(ch)
        elif ch in ['《', '》', '【', '】', '（', '）', '(', ')']:
            tokens.append(ch)
        else:
            # Leave unchanged if unknown symbol
            tokens.append(ch)
        i += 1

    # Step 4: Clean up spacing around punctuation
    result = " ".join(tokens)
    result = re.sub(r'\s+', ' ', result)
    result = re.sub(r'\s*([\,\:\.\!\?\—\·\，\：\！\？\。])\s*', r'\1 ', result)
    result = re.sub(r'\s*([\(\[\【\《])\s*', r' \1', result)
    result = re.sub(r'\s*([\)\]\】\》])\s*', r'\1 ', result)
    result = re.sub(r'\s+', ' ', result).strip()
    return result
