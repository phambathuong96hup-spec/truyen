import os
import json
import re
import urllib.parse
from typing import List, Dict, Any, Optional
import httpx
from bs4 import BeautifulSoup
from backend.scraper import fetch_page_content, detect_and_decode

DISCOVER_CATEGORIES = [
    {"id": "all", "name": "Tất cả thể loại", "icon": "🌟"},
    {"id": "sac_hiep", "name": "Sắc Hiệp (18+)", "icon": "💋", "zh_keyword": "风流后宫"},
    {"id": "sac_hiep_nang", "name": "Sắc Hiệp Nặng Đô (21+)", "icon": "🔞", "zh_keyword": "高H重口"},
    {"id": "he_thong", "name": "Hệ Thống", "icon": "⚡", "zh_keyword": "系统"},
    {"id": "trong_sinh", "name": "Trọng Sinh / Xuyên Không", "icon": "🔄", "zh_keyword": "重生"},
    {"id": "do_thi", "name": "Đô Thị / Thần Hào", "icon": "🏙️", "zh_keyword": "都市"},
    {"id": "huyen_huyen", "name": "Huyền Huyễn / Tiên Hiệp", "icon": "⚔️", "zh_keyword": "玄幻"},
    {"id": "sac_hau_cung", "name": "Hậu Cung / Sảng Văn", "icon": "🔥", "zh_keyword": "后宫"},
    {"id": "linh_di", "name": "Linh Dị / Kinh Dị / Huyền Nghi", "icon": "👻", "zh_keyword": "悬疑"},
    {"id": "lich_su", "name": "Lịch Sử / Quân Sự", "icon": "🏰", "zh_keyword": "历史"},
    {"id": "vong_du", "name": "Võng Du / Game", "icon": "🎮", "zh_keyword": "网游"},
]

# Curated High-Heat Novel Catalog (Top 60+ Famous Chinese Web Novels)
CURATED_NOVELS = [
    # ==================== 1. HỆ THỐNG (SYSTEM) ====================
    {
        "id": "sys_1",
        "title": "全球冰封：我打造了末日安全屋",
        "title_vi": "Toàn Cầu Băng Phong: Ta Chế Tạo Nơi Trú Ẩn Tận Thế",
        "author": "焦和",
        "author_vi": "Tiêu Hòa",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://img.piaotia.com/14/14988/14988s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/14/14988/",
        "views": "4.8M",
        "views_count": 4820000,
        "rating": 9.8,
        "total_chapters": 1420,
        "tags": ["Hệ Thống", "Tận Thế", "Sảng Văn", "Vô Địch"],
        "description_vi": "Tận thế băng tuyết giáng lâm, 95% nhân loại diệt vong. Trương Dịch sống lại trước tận thế 1 tháng, mở ra không gian dị năng, điên cuồng vơ vét vật tư trăm tỷ và chế tạo pháo đài trú ẩn bất khả xâm phạm!"
    },
    {
        "id": "sys_2",
        "title": "亏成首富从游戏开始",
        "title_vi": "Lỗ Thành Người Giàu Nhất Bắt Đầu Từ Trò Chơi",
        "author": "绝不咸鱼",
        "author_vi": "Tuyệt Bất Hàm Ngư",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.biquge.tv/files/article/image/45/45321/45321s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/45_45321/",
        "views": "3.9M",
        "views_count": 3950000,
        "rating": 9.7,
        "total_chapters": 1780,
        "tags": ["Hệ Thống", "Hài Hước", "Kinh Doanh", "Đô Thị"],
        "description_vi": "Bùi Khiêm nhận được 'Hệ Thống Chuyển Đổi Tài Khai', công ty càng lỗ thì tiền cá nhân càng nhiều. Hắn cố tình làm game tệ, đầu tư dự án điên rồ, kết quả người chơi lại phát cuồng biến hắn thành tỷ phú số 1 thế giới!"
    },
    {
        "id": "sys_3",
        "title": "万族之劫",
        "title_vi": "Vạn Tộc Chi Kiếp",
        "author": "老鹰吃小鸡",
        "author_vi": "Lão Ưng Cật Tiểu Kê",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.biquge.tv/files/article/image/48/48912/48912s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/48_48912/",
        "views": "5.6M",
        "views_count": 5600000,
        "rating": 9.9,
        "total_chapters": 965,
        "tags": ["Hệ Thống", "Chiến Tranh", "Vạn Tộc", "Sát Phạt Quyết Đoán"],
        "description_vi": "Chư thiên vạn tộc tranh hùng, nhân tộc nguy nan. Tô Vũ mở ra kim thủ chỉ Đồ Lục Vạn Tộc, từng bước trảm thiên tài, chém thần ma, trấn áp chư thiên vạn giới!"
    },
    {
        "id": "sys_4",
        "title": "轮回乐园",
        "title_vi": "Luân Hồi Nhạc Viên",
        "author": "那一只蚊子",
        "author_vi": "Na Nhất Chỉ Văn Tử",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.biquge.tv/files/article/image/24/24987/24987s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/24_24987/",
        "views": "6.5M",
        "views_count": 6500000,
        "rating": 9.9,
        "total_chapters": 4200,
        "tags": ["Hệ Thống", "Vô Hạn Lưu", "Trảm Muội", "Sát Thủ"],
        "description_vi": "Tô Hiểu ký khế ước với Luân Hồi Nhạc Viên, du hành qua các thế giới anime, điện ảnh và dị giới để thực hiện các nhiệm vụ đẫm máu. Thanh đao Trảm Long Thiểm nơi tay, không nói nhảm, rút đao là trảm!"
    },
    {
        "id": "sys_5",
        "title": "我有一身被动技",
        "title_vi": "Ta Có Một Thân Kỹ Năng Bị Động",
        "author": "熬夜吃苹果",
        "author_vi": "Ngao Dạ Cật Táo Quả",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://img.piaotia.com/15/15890/15890s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/15/15890/",
        "views": "3.7M",
        "views_count": 3700000,
        "rating": 9.6,
        "total_chapters": 1950,
        "tags": ["Hệ Thống", "Kỹ Năng Bị Động", "Hài Hước", "Trang Bức"],
        "description_vi": "Từ Tiểu Thụ đạt được hệ thống bị động: Càng bị công kích thì thân thể càng cứng, càng bị mắng chửi thì kinh nghiệm càng tăng. Hắn chỉ cần đứng im trào phúng là kẻ địch tự sụp đổ!"
    },
    {
        "id": "sys_6",
        "title": "顶级气运，悄悄修炼千年",
        "title_vi": "Đỉnh Cấp Khí Vận, Lặng Lẽ Tu Luyện Ngàn Năm",
        "author": "任我笑",
        "author_vi": "Nhậm Ngã Tiếu",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.biquge.tv/files/article/image/49/49102/49102s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/49_49102/",
        "views": "4.9M",
        "views_count": 4900000,
        "rating": 9.8,
        "total_chapters": 1192,
        "tags": ["Hệ Thống", "Cẩu Đạo", "Vô Địch", "Nhẹ Nhàng"],
        "description_vi": "Chuyển sinh vào thế giới tu tiên, Hàn Tuyệt đổ xúc xắc nhận được khí vận đỉnh phong và tư chất tuyệt thế. Nhưng hắn quyết định không bước ra khỏi động phủ nửa bước, cẩu trụ tu luyện ngàn năm cho đến khi vô địch thiên hạ!"
    },
    {
        "id": "sys_7",
        "title": "第一序列",
        "title_vi": "Đệ Nhất Danh Sách",
        "author": "会说话的肘子",
        "author_vi": "Hội Thuyết Thoại Đích Trửu Tử",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.biquge.tv/files/article/image/40/40891/40891s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/40_40891/",
        "views": "5.2M",
        "views_count": 5200000,
        "rating": 9.9,
        "total_chapters": 1280,
        "tags": ["Hệ Thống", "Hậu Tận Thế", "Hài Hước", "Cảm Động"],
        "description_vi": "Thế giới sau thảm họa hạt nhân, trật tự sụp đổ. Nhâm Tiểu Túc cùng đệ đệ sinh tồn nơi vùng hoang dã ngoài hàng rào pháo đài, kích hoạt hệ thống hấp thụ năng lượng tích cực từ lòng biết ơn của người khác!"
    },

    # ==================== 2. TRỌNG SINH / XUYÊN KHÔNG ====================
    {
        "id": "ts_1",
        "title": "重生的我只想暴富",
        "title_vi": "Trọng Sinh Ta Chỉ Muốn Bạo Phú",
        "author": "十目仙",
        "author_vi": "Thập Mục Tiên",
        "category": "trong_sinh",
        "category_name": "Trọng Sinh",
        "cover_url": "https://img.piaotia.com/15/15124/15124s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/15/15124/",
        "views": "3.2M",
        "views_count": 3200000,
        "rating": 9.6,
        "total_chapters": 1150,
        "tags": ["Trọng Sinh", "Thương Trường", "Làm Giàu", "Đô Thị"],
        "description_vi": "Trọng sinh về năm 2008 trước kỳ thi đại học. Đời trước cúc cung tận tụy nghèo kiết xác, đời này hắn chỉ muốn lợi dụng tầm nhìn tương lai để kiếm tiền bạo phát và sống một đời phóng khoáng!"
    },
    {
        "id": "ts_2",
        "title": "重生之魔教教主",
        "title_vi": "Trọng Sinh Chi Ma Giáo Giáo Chủ",
        "author": "封七月",
        "author_vi": "Phong Thất Nguyệt",
        "category": "trong_sinh",
        "category_name": "Trọng Sinh",
        "cover_url": "https://www.biquge.tv/files/article/image/22/22105/22105s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/22_22105/",
        "views": "4.1M",
        "views_count": 4100000,
        "rating": 9.8,
        "total_chapters": 1390,
        "tags": ["Trọng Sinh", "Ma Đạo", "Sát Phạt Quyết Đoán", "Kiếm Hiệp"],
        "description_vi": "Sở Hưu xuyên không mang theo hệ thống boss phản diện, trọng sinh thành đại phản diện ma đạo. Ra tay tàn nhẫn, mưu mô thâm sâu, từng bước đoạt lại quyền lực thống nhất giang hồ ma giáo!"
    },
    {
        "id": "ts_3",
        "title": "重生之都市修仙",
        "title_vi": "Trọng Sinh Chi Đô Thị Tu Tiên",
        "author": "十里剑神",
        "author_vi": "Thập Lý Kiếm Thần",
        "category": "trong_sinh",
        "category_name": "Trọng Sinh",
        "cover_url": "https://www.biquge.tv/files/article/image/13/13210/13210s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/13_13210/",
        "views": "7.8M",
        "views_count": 7800000,
        "rating": 9.8,
        "total_chapters": 1410,
        "tags": ["Trọng Sinh", "Đô Thị Tu Tiên", "Trang Bức Đỉnh Phong", "Bắc Huyền Tiên Tôn"],
        "description_vi": "Độ Kiếp kỳ đại tu sĩ Trần Bắc Huyền vẫn lạc dưới thiên kiếp, trùng sinh về thời niên thiếu tại địa cầu. Đời trước gia đình tan nát, đời này hắn đạp vỡ mọi chướng ngại, một kiếm trảm thần ma!"
    },
    {
        "id": "ts_4",
        "title": "重生之贼行天下",
        "title_vi": "Trọng Sinh Chi Tặc Hành Thiên Hạ",
        "author": "发飙的蜗牛",
        "author_vi": "Phát Tiêu Đích Oa Ngưu",
        "category": "trong_sinh",
        "category_name": "Trọng Sinh",
        "cover_url": "https://www.biquge.tv/files/article/image/2/2103/2103s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/2_2103/",
        "views": "4.5M",
        "views_count": 4500000,
        "rating": 9.8,
        "total_chapters": 980,
        "tags": ["Trọng Sinh", "Võng Du", "Đạo Tặc", "Chiến Thần"],
        "description_vi": "Đạo tặc cấp thần Nhiếp Ngôn bị kẻ thù ám sát, trùng sinh trở lại mười năm trước vào đúng ngày trò chơi thực tế ảo Tín Ngưỡng vừa ra mắt. Mang theo ký ức đỉnh phong, hắn tạo lập đế chế ngầm vô địch!"
    },
    {
        "id": "ts_5",
        "title": "重回二零零五",
        "title_vi": "Trùng Hồi Năm 2005",
        "author": "西江听雨",
        "author_vi": "Tây Giang Thính Vũ",
        "category": "trong_sinh",
        "category_name": "Trọng Sinh",
        "cover_url": "https://img.piaotia.com/16/16012/16012s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/16/16012/",
        "views": "2.8M",
        "views_count": 2800000,
        "rating": 9.5,
        "total_chapters": 1020,
        "tags": ["Trọng Sinh", "Đô Thị", "Thương Trường", "Học Đường"],
        "description_vi": "Trọng sinh về tuổi 18, thời kỳ Internet Trung Quốc bắt đầu bùng nổ. Không tu tiên, không ma thuật, chỉ có đầu óc thương mại sắc bén và những bước đi chiến lược biến hắn thành tài phiệt thế hệ mới."
    },

    # ==================== 3. ĐÔ THỊ / THẦN HÀO ====================
    {
        "id": "dt_1",
        "title": "都市极品医神",
        "title_vi": "Đô Thị Cực Phẩm Y Thần",
        "author": "风会笑",
        "author_vi": "Phong Hội Tiếu",
        "category": "do_thi",
        "category_name": "Đô Thị",
        "cover_url": "https://www.biquge.tv/files/article/image/10/10839/10839s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/10_10839/",
        "views": "6.2M",
        "views_count": 6200000,
        "rating": 9.7,
        "total_chapters": 3500,
        "tags": ["Đô Thị", "Thần Y", "Trở Về", "Trang Bức Sảng Văn"],
        "description_vi": "Năm năm trước, Diệp Thần bị kẻ thù hãm hại rơi xuống vách núi. Năm năm sau, hắn mang theo y thuật thông thần và võ công tuyệt thế trở lại đô thị, nợ máu phải trả bằng máu!"
    },
    {
        "id": "dt_2",
        "title": "大医凌然",
        "title_vi": "Đại Y Lăng Nhiên",
        "author": "志鸟村",
        "author_vi": "Chí Điểu Thôn",
        "category": "do_thi",
        "category_name": "Đô Thị",
        "cover_url": "https://img.piaotia.com/12/12318/12318s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/12/12318/",
        "views": "3.5M",
        "views_count": 3500000,
        "rating": 9.8,
        "total_chapters": 1450,
        "tags": ["Đô Thị", "Bác Sĩ", "Học Bá", "Thực Tế"],
        "description_vi": "Lăng Nhiên với mục tiêu trở thành bác sĩ ngoại khoa vĩ đại nhất, đạt được hệ thống hỗ trợ y khoa đỉnh phong. Khâu vết mổ, ghép gan, cứu mạng người trong gang tấc."
    },
    {
        "id": "dt_3",
        "title": "我每星期换一个新职业",
        "title_vi": "Ta Mỗi Tuần Đổi Một Nghề Mới",
        "author": "无右",
        "author_vi": "Vô Hữu",
        "category": "do_thi",
        "category_name": "Đô Thị",
        "cover_url": "https://www.biquge.tv/files/article/image/44/44512/44512s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/44_44512/",
        "views": "4.3M",
        "views_count": 4300000,
        "rating": 9.6,
        "total_chapters": 2400,
        "tags": ["Đô Thị", "Thần Hào", "Hệ Thống Nghề Nghiệp", "Hài Hước"],
        "description_vi": "Lâm Dật trải nghiệm hệ thống nghề nghiệp: Tuần này làm tài xế Didi, tuần sau làm bảo vệ trường học, tuần tiếp theo làm bác sĩ... Hoàn thành nhiệm vụ nhận siêu xe Pagani, tập đoàn khách sạn 5 sao!"
    },
    {
        "id": "dt_4",
        "title": "从相亲破产到万亿富豪",
        "title_vi": "Từ Xem Mắt Phá Sản Đến Tỷ Phú Ngàn Tỷ",
        "author": "秋风起",
        "author_vi": "Thu Phong Khởi",
        "category": "do_thi",
        "category_name": "Đô Thị",
        "cover_url": "https://img.piaotia.com/15/15740/15740s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/15/15740/",
        "views": "3.1M",
        "views_count": 3100000,
        "rating": 9.5,
        "total_chapters": 1100,
        "tags": ["Đô Thị", "Thần Hào", "Nghịch Tập", "Sảng Văn"],
        "description_vi": "Bị bạn gái chia tay và coi thường khi đi xem mắt, Trần Phàm bất ngờ thức tỉnh tài khoản ngân hàng vô hạn. Bắt đầu từ mua đứt tòa nhà công ty cũ, vả mặt toàn bộ những kẻ khinh khi!"
    },

    # ==================== 4. LINH DỊ / KINH DỊ / HUYỀN NGHI ====================
    {
        "id": "ld_1",
        "title": "神秘复苏",
        "title_vi": "Thần Bí Phục Tô (Khủng Bố Sống Lại)",
        "author": "佛前献花",
        "author_vi": "Phật Tiền Hiến Hoa",
        "category": "linh_di",
        "category_name": "Linh Dị",
        "cover_url": "https://www.biquge.tv/files/article/image/34/34872/34872s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/34_34872/",
        "views": "5.9M",
        "views_count": 5900000,
        "rating": 9.9,
        "total_chapters": 1600,
        "tags": ["Linh Dị", "Kinh Dị", "Ngự Quỷ", "Sinh Tồn"],
        "description_vi": "Quỷ không thể giết chết, chỉ có thể phong ấn; muốn đối kháng quỷ chỉ có thể dùng quỷ. Dương Gian vô tình mở ra mắt quỷ, bước vào con đường người ngự quỷ giãy giụa trong tuyệt vọng để cứu rỗi nhân loại!"
    },
    {
        "id": "ld_2",
        "title": "我有一座恐怖屋",
        "title_vi": "Ta Có Một Tòa Nhà Ma",
        "author": "我会修空调",
        "author_vi": "Ngã Hội Tu Không Điều",
        "category": "linh_di",
        "category_name": "Linh Dị",
        "cover_url": "https://www.biquge.tv/files/article/image/32/32189/32189s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/32_32189/",
        "views": "4.7M",
        "views_count": 4700000,
        "rating": 9.9,
        "total_chapters": 1215,
        "tags": ["Linh Dị", "Nhà Ma", "Hài Hước", "Giải Đố"],
        "description_vi": "Trần Ca kế thừa nhà ma sắp phá sản của cha mẹ, vô tình tìm được điện thoại màu đen. Hoàn thành nhiệm vụ ở các hiện trường kỳ dị, thu phục lệ quỷ về làm nhân viên phục vụ khách tham quan!"
    },
    {
        "id": "ld_3",
        "title": "诡异入侵",
        "title_vi": "Quỷ Dị Xâm Nhập",
        "author": "犁天",
        "author_vi": "Lê Thiên",
        "category": "linh_di",
        "category_name": "Linh Dị",
        "cover_url": "https://img.piaotia.com/14/14890/14890s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/14/14890/",
        "views": "3.8M",
        "views_count": 3800000,
        "rating": 9.7,
        "total_chapters": 1540,
        "tags": ["Linh Dị", "Thế Giới Biến Đổi", "Trảm Quỷ", "Hành Động"],
        "description_vi": "Hiện thực thế giới bắt đầu xuất hiện những khe nứt dị thường, tà ma xâm thực. Giang Dược phát hiện trong mắt mình có thể nhìn thấu quỷ vật và hấp thu linh năng để thức tỉnh dị thuật Viêm Dương!"
    },
    {
        "id": "ld_4",
        "title": "极道天魔",
        "title_vi": "Cực Đạo Thiên Ma",
        "author": "滚开",
        "author_vi": "Cổn Khai",
        "category": "linh_di",
        "category_name": "Linh Dị",
        "cover_url": "https://www.biquge.tv/files/article/image/23/23145/23145s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/23_23145/",
        "views": "5.1M",
        "views_count": 5100000,
        "rating": 9.8,
        "total_chapters": 1360,
        "tags": ["Linh Dị", "Cơ Bắp Lưu", "Tà Ma", "Vô Địch"],
        "description_vi": "Thế giới đầy rẫy yêu ma quỷ quái, võ đạo suy tàn. Lộ Thắng mang theo bảng điều khiển sửa đổi võ công, đẩy cơ thể lên giới hạn cực đạo kinh hoàng: Ta không cần pháp thuật, cơ bắp của ta chính là thần tích!"
    },

    # ==================== 5A. SẮC HIỆP (18+ / DIỄM TÌNH / TIÊN HIỆP SẮC) ====================
    {
        "id": "sh_1",
        "title": "风流大法师",
        "title_vi": "Phong Lưu Đại Pháp Sư",
        "author": "天堂不寂寞",
        "author_vi": "Thiên Đường Bất Tịch Mịch",
        "category": "sac_hiep",
        "category_name": "Sắc Hiệp (18+)",
        "cover_url": "https://www.biquge.tv/files/article/image/0/654/654s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/0_654/",
        "views": "6.8M",
        "views_count": 6800000,
        "rating": 9.8,
        "total_chapters": 782,
        "tags": ["Sắc Hiệp 18+", "Dị Giới", "Đại Pháp Sư", "Hậu Cung Tuyệt Sắc"],
        "description_vi": "Tác phẩm huyền huyễn sắc hiệp kinh điển đời đầu làm say đắm biết bao độc giả! Long Nhất mang theo công pháp Lôi Thần Quyết xuyên việt đến dị giới ma pháp, bước vào con đường chinh phục vô số cực phẩm mỹ nhân từ tinh linh nữ vương, công chúa đế quốc đến nữ thần long tộc!"
    },
    {
        "id": "sh_2",
        "title": "猎艳江湖梦",
        "title_vi": "Liệp Diễm Giang Hồ Mộng",
        "author": "神哭鬼啸",
        "author_vi": "Thần Khóc Quỷ Khiếu",
        "category": "sac_hiep",
        "category_name": "Sắc Hiệp (18+)",
        "cover_url": "https://www.biquge.tv/files/article/image/2/2311/2311s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/2_2311/",
        "views": "7.5M",
        "views_count": 7500000,
        "rating": 9.9,
        "total_chapters": 620,
        "tags": ["Kiếm Hiệp Sắc", "Liệp Diễm", "Giang Hồ", "Hoan Lạc Mây Mưa"],
        "description_vi": "Đệ nhất kiếm hiệp sắc tình kinh điển! Thiếu niên Tô Triệt bước vào giang hồ ân oán tình thù, tu luyện Âm Dương Hoan Hỷ Thiền. Dưới đao kiếm phân tranh là những màn liệp diễm phong lưu, hàng phục các đại chưởng môn nữ phái, nữ hiệp băng thanh ngọc khiết và ma giáo yêu nữ."
    },
    {
        "id": "sh_3",
        "title": "琼明剑典",
        "title_vi": "Quỳnh Minh Kiếm Điển",
        "author": "剑断九洲",
        "author_vi": "Kiếm Đoạn Cửu Châu",
        "category": "sac_hiep",
        "category_name": "Sắc Hiệp (18+)",
        "cover_url": "https://www.8tsw.com/files/article/image/58/58210/58210s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/58_58210/",
        "views": "8.9M",
        "views_count": 8900000,
        "rating": 9.9,
        "total_chapters": 450,
        "tags": ["Tiên Hiệp Sắc", "Kiếm Đạo", "Bùi Ngữ Hàm", "Diễm Lệ"],
        "description_vi": "Tuyệt phẩm tiên hiệp sắc diễm lệ bậc nhất văn đàn mạng! Thiếu niên Ô Hành Tuyết tu kiếm vấn đạo giữa hồng trần tình kiếp. Từng trang truyện là sự giao thoa đỉnh cao giữa kiếm ý ngút trời và dục vọng tình si, đan xen cùng những phân đoạn ân ái rung động tâm can giữa sư đồ, tuyệt sắc kiếm tiên."
    },
    {
        "id": "sh_4",
        "title": "极乐净土: 仙道艳皇",
        "title_vi": "Cực Lạc Tịnh Thổ: Tiên Đạo Diễm Hoàng",
        "author": "御剑逍遥",
        "author_vi": "Ngự Kiếm Tiêu Dao",
        "category": "sac_hiep",
        "category_name": "Sắc Hiệp (18+)",
        "cover_url": "https://www.8tsw.com/files/article/image/73/73190/73190s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/73_73190/",
        "views": "5.6M",
        "views_count": 5600000,
        "rating": 9.7,
        "total_chapters": 890,
        "tags": ["Song Tu", "Lô Đỉnh", "Tiên Đạo", "Thu Hậu Cung"],
        "description_vi": "Diệp Thần thức tỉnh Cực Lạc Diễm Thể, nắm giữ pháp quyết song tu vô thượng. Con đường tu tiên của hắn là một hồi mỹ vị tiệc rượu: thu phục thánh nữ bạch đạo, thuần hóa ma tôn lãnh ngạo, biến các bậc nữ đế cao cao tại thượng trở thành bạn lữ triền miên trong hậu cung tịnh thổ!"
    },
    {
        "id": "sh_5",
        "title": "洪荒仙女录",
        "title_vi": "Hồng Hoang Tiên Nữ Lục",
        "author": "太上忘情",
        "author_vi": "Thái Thượng Vong Tình",
        "category": "sac_hiep",
        "category_name": "Sắc Hiệp (18+)",
        "cover_url": "https://www.biquge.tv/files/article/image/15/15870/15870s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/15_15870/",
        "views": "6.2M",
        "views_count": 6200000,
        "rating": 9.6,
        "total_chapters": 740,
        "tags": ["Hồng Hoang", "Nữ Oa", "Tam Tiêu", "Diễm Tình"],
        "description_vi": "Xuyên không trở về thời đại Hồng Hoang sơ khai, chấp chưởng Hỗn Độn Dâm Dương Kính. Hắn từng bước chinh phục các tuyệt sắc nữ tiên chấn động vạn cổ: Nữ Oa nương nương, Tây Vương Mẫu, Tam Tiêu tiên tử, Thường Nga tiên tử, cùng nhau tham ngộ Đại Đạo hoan lạc chí tôn."
    },
    {
        "id": "sh_6",
        "title": "游龙清影",
        "title_vi": "Du Long Thanh Ảnh",
        "author": "幻剑琴书",
        "author_vi": "Hoạn Kiếm Cầm Thư",
        "category": "sac_hiep",
        "category_name": "Sắc Hiệp (18+)",
        "cover_url": "https://www.biquge.tv/files/article/image/8/8940/8940s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/8_8940/",
        "views": "4.9M",
        "views_count": 4900000,
        "rating": 9.7,
        "total_chapters": 530,
        "tags": ["Cổ Điển Sắc", "Võ Hiệp", "Hương Diễm", "Tình Ái"],
        "description_vi": "Tác phẩm kiếm hiệp sắc tình cổ điển với ngòi bút miêu tả phong nguyệt trác tuyệt. Long Phiêu bước chân vào giang hồ hiểm ác nhưng tràn ngập hương hoa phấn son, lướt qua hàng loạt mỹ nhân kiều diễm trong những đêm xuân mộng ảo triền miên."
    },

    # ==================== 5B. SẮC HIỆP NẶNG ĐÔ (21+ CAO H / TRỌNG KHẨU) ====================
    {
        "id": "shn_1",
        "title": "朱颜血",
        "title_vi": "Chu Nhan Huyết (Trọn Bộ Hệ Liệt)",
        "author": "黑叶子 / 蓝晶",
        "author_vi": "Hắc Diệp Tử / Lam Tinh",
        "category": "sac_hiep_nang",
        "category_name": "Sắc Hiệp Nặng Đô (21+)",
        "cover_url": "https://www.8tsw.com/files/article/image/19/19440/19440s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/19_19440/",
        "views": "11.2M",
        "views_count": 11200000,
        "rating": 9.9,
        "total_chapters": 320,
        "tags": ["21+", "Đệ Nhất Trọng Khẩu", "Hắc Ám", "Ngược Đãi", "Chu Nhan"],
        "description_vi": "Bộ tiểu thuyết sắc tình hắc ám nặng đô khét tiếng nhất lịch sử mạng Trung Quốc! Tuyệt đối không dành cho người yếu tim. Từng phần là những màn đoạt thê tử, lăng nhục thần thánh, đọa lạc tàn bạo, biến các bậc thánh nữ, hoàng hậu, phu nhân đài các thành tính nô trong vũng lầy nhục dục và bi kịch tột cùng."
    },
    {
        "id": "shn_2",
        "title": "魔刀丽影",
        "title_vi": "Ma Đao Lệ Ảnh",
        "author": "雪月花",
        "author_vi": "Tuyết Nguyệt Hoa",
        "category": "sac_hiep_nang",
        "category_name": "Sắc Hiệp Nặng Đô (21+)",
        "cover_url": "https://www.8tsw.com/files/article/image/44/44120/44120s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/44_44120/",
        "views": "8.4M",
        "views_count": 8400000,
        "rating": 9.8,
        "total_chapters": 480,
        "tags": ["21+", "Hắc Ám Võ Hiệp", "Cao H", "Thuần Dâm", "Đoạt Thê"],
        "description_vi": "Tà phái ma đao xuất thế, dấy lên một trường dâm phong huyết vũ. Nữ hiệp giang hồ, tiểu thư khuê các lần lượt bị ma đao tà thuật khống chế tâm trí, biến đổi từ trinh bạch kiêu hãnh thành những dâm phụ dâm đãng vô liêm sỉ, phục tùng mọi thú vui bạo liệt."
    },
    {
        "id": "shn_3",
        "title": "绿帽第一仙",
        "title_vi": "Lục Mũ Đệ Nhất Tiên",
        "author": "绿仙翁",
        "author_vi": "Lục Tiên Ông",
        "category": "sac_hiep_nang",
        "category_name": "Sắc Hiệp Nặng Đô (21+)",
        "cover_url": "https://www.8tsw.com/files/article/image/61/61050/61050s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/61_61050/",
        "views": "7.8M",
        "views_count": 7800000,
        "rating": 9.7,
        "total_chapters": 560,
        "tags": ["21+", "NTR", "Lục Sắc", "Đoạt Vợ", "Đọa Lạc"],
        "description_vi": "Đỉnh cao thể loại lục sắc (NTR) tu tiên nặng đô! Nhân vật chính tận mắt chứng kiến đạo lữ tiên tử băng thanh ngọc khiết của mình từng bước bị các đại lão, ma tu và ác bá thao túng thể xác, từ kháng cự nhục nhã chuyển dần sang mê đắm khoái lạc nhục dục trước mắt trượng phu."
    },
    {
        "id": "shn_4",
        "title": "仙子堕落录: 圣女的调教",
        "title_vi": "Tiên Tử Đọa Lạc Lục: Thánh Nữ Điều Giáo",
        "author": "邪情天尊",
        "author_vi": "Tà Tình Thiên Tôn",
        "category": "sac_hiep_nang",
        "category_name": "Sắc Hiệp Nặng Đô (21+)",
        "cover_url": "https://www.biquge.tv/files/article/image/29/29810/29810s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/29_29810/",
        "views": "9.1M",
        "views_count": 9100000,
        "rating": 9.8,
        "total_chapters": 390,
        "tags": ["21+", "Cao H Thuần Nhục", "Thánh Nữ Đọa Lạc", "Lô Đỉnh", "Dâm Độc"],
        "description_vi": "Tông môn thánh nữ cao quý lãnh diễm, thề bất khuất trước ma đạo. Nào ngờ rơi vào tay tà ma dâm tăng, bị hạ 'Vạn Dâm Hóa Cốt Đan', trải qua trăm ngày điều giáo biến thành dâm nô chuyên phục vụ thân xác, thân thể chỉ cần chạm nhẹ là run rẩy xuân thủy đầm đìa."
    },
    {
        "id": "shn_5",
        "title": "母子艳录: 禁忌之花",
        "title_vi": "Mẫu Tử Diễm Lục: Cấm Kỵ Chi Hoa",
        "author": "暗夜游魂",
        "author_vi": "Ám Dạ Du Hồn",
        "category": "sac_hiep_nang",
        "category_name": "Sắc Hiệp Nặng Đô (21+)",
        "cover_url": "https://www.8tsw.com/files/article/image/36/36720/36720s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/36_36720/",
        "views": "8.5M",
        "views_count": 8500000,
        "rating": 9.8,
        "total_chapters": 410,
        "tags": ["21+", "Cấm Kỵ Loạn Luân", "Mẫu Tử", "Gia Tộc Sắc", "Cực Hạn Nhục Dục"],
        "description_vi": "Thể loại cấm kỵ gia đình loạn luân nặng đô. Mối quan hệ mẫu tử thiêng liêng dần bị dục vọng cuồng si nuốt chửng sau những biến cố gia tộc. Những đêm dài triền miên tội lỗi, giữa sự cắn rứt của luân thường đạo lý và khoái lạc thể xác điên cuồng tột bực."
    },
    {
        "id": "shn_6",
        "title": "天魔淫录: 万艳鼎炉",
        "title_vi": "Thiên Ma Dâm Lục: Vạn Diễm Đỉnh Lô",
        "author": "嗜血狂魔",
        "author_vi": "Thị Huyết Cuồng Ma",
        "category": "sac_hiep_nang",
        "category_name": "Sắc Hiệp Nặng Đô (21+)",
        "cover_url": "https://www.8tsw.com/files/article/image/51/51290/51290s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/51_51290/",
        "views": "7.2M",
        "views_count": 7200000,
        "rating": 9.7,
        "total_chapters": 680,
        "tags": ["21+", "Ma Tu Thải Bổ", "Lô Đỉnh Hàng Loạt", "Bạo Liệt Phòng The"],
        "description_vi": "Ma môn thiếu chủ tu luyện 'Cửu Chuyển Hóa Âm Bí Quyết', bắt giữ hàng trăm tiên tử, cung chủ, phu nhân của các danh môn chính phái giam cầm trong mật động tịnh thất. Từng đêm thải âm bổ dương bạo liệt, tiếng rên rỉ van xin vang vọng không dứt."
    },

    # ==================== 5C. HẬU CUNG / SẢNG VĂN ====================
    {
        "id": "sac_1",
        "title": "反派：女主求我别退婚",
        "title_vi": "Phản Diện: Nữ Chính Cầu Xin Ta Đừng Thoái Hôn",
        "author": "醉酒听风",
        "author_vi": "Túy Tửu Thính Phong",
        "category": "sac_hau_cung",
        "category_name": "Hậu Cung / Sảng Văn",
        "cover_url": "https://img.piaotia.com/16/16230/16230s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/16/16230/",
        "views": "3.8M",
        "views_count": 3800000,
        "rating": 9.5,
        "total_chapters": 890,
        "tags": ["Hậu Cung", "Phản Diện", "Đô Thị", "Mỹ Nữ Vây Quanh"],
        "description_vi": "Xuyên không thành thiếu gia phản diện giàu có, định thoái hôn với nữ chính kiêu ngạo để sống sót. Ai ngờ tiếng lòng bị các nữ thần nghe thấy, nữ tổng tài, giáo hoa, nữ sát thủ tranh nhau theo đuổi!"
    },
    {
        "id": "sac_2",
        "title": "逍遥小贵婿",
        "title_vi": "Tiêu Dao Tiểu Quý Tế",
        "author": "堵上西楼",
        "author_vi": "Đổ Thượng Tây Lâu",
        "category": "sac_hau_cung",
        "category_name": "Hậu Cung / Sảng Văn",
        "cover_url": "https://www.biquge.tv/files/article/image/52/52119/52119s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/52_52119/",
        "views": "3.4M",
        "views_count": 3400000,
        "rating": 9.6,
        "total_chapters": 1280,
        "tags": ["Hậu Cung", "Ở Rể", "Lịch Sử", "Hồng Nhan"],
        "description_vi": "Lý Thần An xuyên không thành con trai thứ ở rể danh môn. Hắn vốn chỉ muốn làm một quý tế an nhàn uống rượu ngắm hoa, nào ngờ tài thơ ca và quyền mưu lại khiến công chúa, tài nữ khắp thiên hạ say đắm."
    },
    {
        "id": "sac_3",
        "title": "极品家丁",
        "title_vi": "Cực Phẩm Gia Đinh",
        "author": "禹岩",
        "author_vi": "Vũ Nham",
        "category": "sac_hau_cung",
        "category_name": "Hậu Cung / Sảng Văn",
        "cover_url": "https://www.biquge.tv/files/article/image/0/12/12s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/0_12/",
        "views": "9.1M",
        "views_count": 9100000,
        "rating": 9.9,
        "total_chapters": 680,
        "tags": ["Hậu Cung", "Gia Đinh", "Kinh Điển", "Đỉnh Cao Hài Hước"],
        "description_vi": "Tác phẩm hậu cung kinh điển nhất lịch sử mạng văn Trung Quốc! Lâm Vãn Vinh vô tình rơi vào Đại Hoa triều, trở thành đệ nhất gia đinh Tiêu phủ, dùng trí tuệ hiện đại chinh phục tuyệt sắc giai nhân từ đại tiểu thư đến nữ hiệp, công chúa!"
    },
    {
        "id": "sac_4",
        "title": "绝色总裁的贴身高手",
        "title_vi": "Tuyệt Sắc Tổng Tài Đích Thiếp Thân Cao Thủ",
        "author": "未知",
        "author_vi": "Mao Tử",
        "category": "sac_hau_cung",
        "category_name": "Hậu Cung / Sảng Văn",
        "cover_url": "https://www.biquge.tv/files/article/image/18/18902/18902s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/18_18902/",
        "views": "4.2M",
        "views_count": 4200000,
        "rating": 9.5,
        "total_chapters": 2100,
        "tags": ["Hậu Cung", "Đô Thị", "Binh Vương", "Mỹ Nữ"],
        "description_vi": "Vua lính đánh thuê Đoạn Vân hồi hương, nhận nhiệm vụ bảo vệ nữ tổng tài băng sơn kiêm vị hôn thê. Nơi đô thị phồn hoa, hắn liên tục thu phục các bóng hồng từ minh tinh, nữ cảnh sát đến nữ sát thủ."
    },

    # ==================== 6. HUYỀN HUYỄN / TIÊN HIỆP ====================
    {
        "id": "hh_1",
        "title": "遮天",
        "title_vi": "Già Thiên",
        "author": "辰东",
        "author_vi": "Thần Đông",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.biquge.tv/files/article/image/0/68/68s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/0_68/",
        "views": "8.5M",
        "views_count": 8500000,
        "rating": 9.9,
        "total_chapters": 1820,
        "tags": ["Tiên Hiệp", "Cổ Thần", "Hoang Cổ Thánh Thể", "Kinh Điển"],
        "description_vi": "Cửu Long kéo quan, mở ra con đường sao băng cổ xưa. Diệp Phàm nghịch thiên quật khởi, một quyền chấn toái chư thiên vạn đạo, vấn đỉnh Đế tôn!"
    },
    {
        "id": "hh_2",
        "title": "宿命之环",
        "title_vi": "Túc Mệnh Chi Hoàn (Quỷ Bí Chi Chủ 2)",
        "author": "爱潜水的乌贼",
        "author_vi": "Ái Tiềm Thủy Đích Ô Tặc",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.biquge.tv/files/article/image/51/51234/51234s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/51_51234/",
        "views": "6.8M",
        "views_count": 6800000,
        "rating": 9.9,
        "total_chapters": 1150,
        "tags": ["Phương Tây Huyễn Tưởng", "Ma Thuật", "Huyền Bí", "Kinh Điển"],
        "description_vi": "Phần 2 tiếp nối đại tác phẩm Quỷ Bí Chi Chủ! Lumian Lee bước vào vòng lặp vận mệnh của làng Cordu, tìm kiếm chân tướng thần bí và thăng tiến ma dược."
    },
    {
        "id": "hh_3",
        "title": "凡人修仙之仙界篇",
        "title_vi": "Phàm Nhân Tu Tiên: Tiên Giới Thiên",
        "author": "忘语",
        "author_vi": "Vong Ngữ",
        "category": "huyen_huyen",
        "category_name": "Tiên Hiệp",
        "cover_url": "https://www.biquge.tv/files/article/image/25/25412/25412s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/25_25412/",
        "views": "9.5M",
        "views_count": 9500000,
        "rating": 9.9,
        "total_chapters": 1395,
        "tags": ["Tiên Hiệp", "Hàn Lập", "Hàn Bảo", "Kinh Điển Mọi Thời Đại"],
        "description_vi": "Hàn Lập phi thăng tiên giới, lạc mất ký ức ba trăm năm, tu vi rơi xuống. Mang theo Chưởng Thiên Bình và ý chí bất khuất, Hàn Thỏ Đế một lần nữa từng bước bước lên chí cao Tiên Đế!"
    },
    {
        "id": "hh_4",
        "title": "斗破苍穹",
        "title_vi": "Đấu Phá Thương Khung",
        "author": "天蚕土豆",
        "author_vi": "Thiên Tằm Thổ Đậu",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.biquge.tv/files/article/image/0/2/2s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/0_2/",
        "views": "12.0M",
        "views_count": 12000000,
        "rating": 9.9,
        "total_chapters": 1648,
        "tags": ["Đấu Khí", "Dị Hỏa", "Tiêu Viêm", "Ba Mươi Năm Hà Đông"],
        "description_vi": "Ba mươi năm Hà Đông, ba mươi năm Hà Tây, đừng khinh thiếu niên nghèo! Tiêu Viêm thu thập Dị Hỏa trong thiên hạ, sáng chế Phật Nộ Hỏa Liên, trấn áp Đấu Khí Đại Lục thành Viêm Đế!"
    },
    {
        "id": "hh_5",
        "title": "剑来",
        "title_vi": "Kiếm Lai",
        "author": "烽火戏诸侯",
        "author_vi": "Phong Hỏa Hí Chư Hầu",
        "category": "huyen_huyen",
        "category_name": "Tiên Hiệp",
        "cover_url": "https://www.biquge.tv/files/article/image/21/21490/21490s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/21_21490/",
        "views": "7.9M",
        "views_count": 7900000,
        "rating": 9.9,
        "total_chapters": 1200,
        "tags": ["Tiên Hiệp", "Kiếm Đạo", "Trần Bình An", "Văn Phong Đỉnh Cao"],
        "description_vi": "Thiếu niên Trần Bình An xuất thân từ trấn nhỏ Ly Châu, lưng đeo kiếm gỗ, từng bước đi qua các châu thiên hạ, cầu đạo trảm yêu, dùng một thanh kiếm vấn hỏi đạo tâm!"
    },
    {
        "id": "hh_6",
        "title": "吞噬星空",
        "title_vi": "Thôn Phệ Tinh Không",
        "author": "我吃西红柿",
        "author_vi": "Ngã Cật Tây Hồng Thị",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.biquge.tv/files/article/image/0/1/1s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/0_1/",
        "views": "8.8M",
        "views_count": 8800000,
        "rating": 9.9,
        "total_chapters": 1480,
        "tags": ["Vũ Trụ", "Tế Bào", "La Phong", "Kim Giác Cự Thú"],
        "description_vi": "Trái Đất sau đại thảm họa virus RR, quái thú hoành hành. La Phong từng bước vượt qua khảo hạch chiến thần, đoạt xá Kim Giác Cự Thú, vươn ra biển sao vũ trụ thôn phệ càn khôn!"
    },
    {
        "id": "hh_7",
        "title": "仙逆",
        "title_vi": "Tiên Nghịch",
        "author": "耳根",
        "author_vi": "Nhĩ Căn",
        "category": "huyen_huyen",
        "category_name": "Tiên Hiệp",
        "cover_url": "https://www.biquge.tv/files/article/image/0/23/23s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/0_23/",
        "views": "7.5M",
        "views_count": 7500000,
        "rating": 9.9,
        "total_chapters": 1970,
        "tags": ["Tiên Hiệp", "Vương Lâm", "Nghịch Tu", "Hóa Phàm"],
        "description_vi": "Thuận vi phàm, nghịch tắc tiên. Vương Lâm bình phàm quật khởi, nhờ Thiên Nghịch châu bước lên con đường tu đạo sát phạt đẫm máu, nghịch thiên phục sinh thê tử Lý Mộ Uyển!"
    },
    {
        "id": "hh_8",
        "title": "牧神记",
        "title_vi": "Mục Thần Ký",
        "author": "宅猪",
        "author_vi": "Trạch Trư",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.biquge.tv/files/article/image/23/23891/23891s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/23_23891/",
        "views": "6.1M",
        "views_count": 6100000,
        "rating": 9.9,
        "total_chapters": 1820,
        "tags": ["Huyền Huyễn", "Tần Mục", "Tàn Lão Thôn", "Hài Hước Trí Tuệ"],
        "description_vi": "Đại Khư tàn lão thôn chín vị lão nhân tàn tật nuôi dưỡng một hài nhi nhặt được bên bờ sông. Hài nhi Tần Mục lớn lên, dùng tư thái Bá Thể chấn động thần ma khắp chư thiên!"
    },

    # ==================== 7. LỊCH SỬ / QUÂN SỰ ====================
    {
        "id": "ls_1",
        "title": "大奉打更人",
        "title_vi": "Đại Phụng Đả Canh Nhân",
        "author": "卖报小郎君",
        "author_vi": "Mại Báo Tiểu Lang Quân",
        "category": "lich_su",
        "category_name": "Lịch Sử",
        "cover_url": "https://www.biquge.tv/files/article/image/46/46889/46889s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/46_46889/",
        "views": "7.2M",
        "views_count": 7200000,
        "rating": 9.9,
        "total_chapters": 980,
        "tags": ["Phá Án", "Tiên Hiệp Lịch Sử", "Hài Hước", "Hậu Cung"],
        "description_vi": "Hứa Thất An cảnh sát hình sự xuyên không thành tử tù, dùng tài phá án hiện đại để giải nguy, gia nhập Ty Đả Canh. Phá án kinh thiên, trảm gian thần, bảo vệ thiên hạ thái bình!"
    },
    {
        "id": "ls_2",
        "title": "明朝败家子",
        "title_vi": "Minh Triều Bại Gia Tử",
        "author": "上山打老虎额",
        "author_vi": "Thượng Sơn Đả Lão Hổ Ngạch",
        "category": "lich_su",
        "category_name": "Lịch Sử",
        "cover_url": "https://www.biquge.tv/files/article/image/33/33102/33102s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/33_33102/",
        "views": "4.6M",
        "views_count": 4600000,
        "rating": 9.8,
        "total_chapters": 2080,
        "tags": ["Lịch Sử", "Minh Triều", "Bại Gia", "Cười Nghiêng Ngả"],
        "description_vi": "Phương Kế Phiên xuyên không thành đệ nhất bại gia tử kinh thành thời Hoằng Trị. Càng ăn chơi phá của thì triều đình càng hưng thịnh, mở mang biên cương, biến Đại Minh thành bá chủ toàn cầu!"
    },
    {
        "id": "ls_3",
        "title": "汉乡",
        "title_vi": "Hán Hương",
        "author": "孑与2",
        "author_vi": "Kiết Dữ 2",
        "category": "lich_su",
        "category_name": "Lịch Sử",
        "cover_url": "https://img.piaotia.com/13/13210/13210s.jpg",
        "source_domain": "piaotia.com",
        "source_url": "https://www.piaotia.com/html/13/13210/",
        "views": "3.8M",
        "views_count": 3800000,
        "rating": 9.7,
        "total_chapters": 1120,
        "tags": ["Lịch Sử", "Thời Hán", "Lưu Triệt", "Văn Học Tinh Tế"],
        "description_vi": "Vân Lang rơi vào thời Tây Hán Hán Vũ Đế Lưu Triệt. Bằng kiến thức nông nghiệp và công nghệ hiện đại, hắn xây dựng Vân thị trang viên, bồi dưỡng tướng tài Hoắc Khứ Bệnh, phạt Hung Nô!"
    },
    {
        "id": "ls_4",
        "title": "唐砖",
        "title_vi": "Đường Chuyên",
        "author": "孑与2",
        "author_vi": "Kiết Dữ 2",
        "category": "lich_su",
        "category_name": "Lịch Sử",
        "cover_url": "https://www.biquge.tv/files/article/image/3/3412/3412s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/3_3412/",
        "views": "5.3M",
        "views_count": 5300000,
        "rating": 9.8,
        "total_chapters": 1400,
        "tags": ["Lịch Sử", "Đại Đường", "Lý Thế Dân", "Kinh Điển"],
        "description_vi": "Vân Diệp rơi về thời Trinh Quán của Đường Thái Tông Lý Thế Dân. Là một viên gạch lát nền cho sự thịnh vượng của Đại Đường, hắn mang lại muối trắng, khoai tây và vũ khí cải cách đế quốc!"
    },

    # ==================== 8. VÕNG DU / GAME ====================
    {
        "id": "vd_1",
        "title": "全职高手",
        "title_vi": "Toàn Chức Cao Thủ",
        "author": "蝴蝶蓝",
        "author_vi": "Hồ Điệp Lam",
        "category": "vong_du",
        "category_name": "Võng Du",
        "cover_url": "https://www.biquge.tv/files/article/image/1/1452/1452s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/1_1452/",
        "views": "5.1M",
        "views_count": 5100000,
        "rating": 9.9,
        "total_chapters": 1728,
        "tags": ["E-Sports", "Game Thủ", "Quân Mạc Tiếu", "Nhiệt Huyết"],
        "description_vi": "Đấu Thần Diệp Tu bị câu lạc bộ xua đuổi, rời đi với tài khoản cấp 1 Quân Mạc Tiếu và vũ khí tự chế Ô Thiên Cơ. Trở lại từ khu 10, tập hợp đồng đội bước lên đỉnh phong Vinh Quang một lần nữa!"
    },
    {
        "id": "vd_2",
        "title": "全职法师",
        "title_vi": "Toàn Chức Pháp Sư",
        "author": "乱",
        "author_vi": "Loạn",
        "category": "vong_du",
        "category_name": "Võng Du",
        "cover_url": "https://www.biquge.tv/files/article/image/12/12301/12301s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/12_12301/",
        "views": "8.1M",
        "views_count": 8100000,
        "rating": 9.8,
        "total_chapters": 3200,
        "tags": ["Ma Pháp", "Song Hệ", "Mạc Phàm", "Nhiệt Huyết"],
        "description_vi": "Thế giới biến thành thời đại ma pháp, khoa học biến thành ma pháp học. Mạc Phàm thức tỉnh song hệ Lôi và Hỏa, sau đó mỗi lần thăng cấp lại thức tỉnh thêm hai hệ, một mình cân cả yêu ma đại quân!"
    },
    {
        "id": "vd_3",
        "title": "网游之近战法师",
        "title_vi": "Võng Du Chi Cận Chiến Pháp Sư",
        "author": "蝴蝶蓝",
        "author_vi": "Hồ Điệp Lam",
        "category": "vong_du",
        "category_name": "Võng Du",
        "cover_url": "https://www.biquge.tv/files/article/image/1/1280/1280s.jpg",
        "source_domain": "biquge.tv",
        "source_url": "https://www.biquge.tv/1_1280/",
        "views": "3.9M",
        "views_count": 3900000,
        "rating": 9.7,
        "total_chapters": 1350,
        "tags": ["Võng Du", "Hài Hước", "Cố Phi", "Võ Thuật"],
        "description_vi": "Cố Phi là thầy giáo thể dục tinh thông võ thuật gia truyền, vào game lại chọn nhầm nghề Pháp sư yếu đuối. Nhưng với thân thủ võ thuật ngoài đời, hắn cầm pháp trượng xông vào cận chiến chém quái như chém chuối!"
    },
    {
        "id": "hh_9",
        "title": "诡秘之主",
        "title_vi": "Quỷ Bí Chi Chủ (Lord of the Mysteries)",
        "author": "爱潜水的乌贼",
        "author_vi": "Ái Tiềm Thủy Đích Ô Tặc",
        "category": "linh_di",
        "category_name": "Linh Dị / Huyền Nghi",
        "cover_url": "https://www.8tsw.com/files/article/image/31/31920/31920s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/31_31920/",
        "views": "12.5M",
        "views_count": 12500000,
        "rating": 9.9,
        "total_chapters": 1432,
        "tags": ["Steampunk", "Cthulhu", "Dị Giới", "Siêu Phẩm"],
        "description_vi": "Chu Minh Thụy xuyên không đến thế giới mang phong cách Victoria xen lẫn các yếu tố ma thuật và thần bí. Nhờ vào 'Sương Mù Xám', hắn lập nên Hội Tarot và bước lên con đường Ngu Giả huyền thoại!"
    },
    {
        "id": "hh_10",
        "title": "道诡异仙",
        "title_vi": "Đạo Quỷ Dị Tiên",
        "author": "狐尾的笔",
        "author_vi": "Hồ Vĩ Đích Bút",
        "category": "linh_di",
        "category_name": "Linh Dị / Huyền Nghi",
        "cover_url": "https://www.8tsw.com/files/article/image/105/105312/105312s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/105_105312/",
        "views": "9.8M",
        "views_count": 9800000,
        "rating": 9.9,
        "total_chapters": 1020,
        "tags": ["Cthulhu", "Tu Tiên Quái Dị", "Lý Hỏa Vượng", "Ảo Giác"],
        "description_vi": "Lý Hỏa Vượng chẩn đoán tâm thần phân liệt, giãy giụa giữa bệnh viện tâm thần hiện đại và thế giới tu tiên tràn ngập tà sùng, tế sống, quỷ dị. Đâu mới là ảo giác? Đâu mới là sự thật tàn khốc?"
    },
    {
        "id": "hh_11",
        "title": "赤心巡天",
        "title_vi": "Xích Tâm Tuần Thiên",
        "author": "情何以甚",
        "author_vi": "Tình Hà Dĩ Thậm",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.8tsw.com/files/article/image/42/42890/42890s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/42_42890/",
        "views": "7.9M",
        "views_count": 7900000,
        "rating": 9.9,
        "total_chapters": 2400,
        "tags": ["Tiên Hiệp", "Quyền Mưu", "Khương Vọng", "Đỉnh Cao"],
        "description_vi": "Thời đại sơn hà vỡ vụn, chư quốc tranh bá. Thiếu niên Khương Vọng ôm lòng xích tử, tay cầm trường kiếm, từng bước vượt qua sinh tử chông gai, tuần sát chư thiên vạn giới vì chính nghĩa nhân gian."
    },
    {
        "id": "hh_12",
        "title": "完美世界",
        "title_vi": "Hoàn Mỹ Thế Giới",
        "author": "辰东",
        "author_vi": "Thần Đông",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.8tsw.com/files/article/image/1/1004/1004s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/1_1004/",
        "views": "11.2M",
        "views_count": 11200000,
        "rating": 9.9,
        "total_chapters": 2014,
        "tags": ["Hoang Thiên Đế", "Đại Hoang", "Siêu Phẩm", "Thần Đông"],
        "description_vi": "Một hạt bụi có thể lấp biển, một cọng cỏ chém hết nhật nguyệt tinh thần. Thạch Hạo sinh ra mang Chí Tôn Cốt bị đoạt, từ Thạch Thôn đại hoang đi ra, tắm máu trưởng thành xưng là Hoang Thiên Đế độc đoán vạn cổ!"
    },
    {
        "id": "hh_13",
        "title": "一念永恒",
        "title_vi": "Nhất Niệm Vĩnh Hằng",
        "author": "耳根",
        "author_vi": "Nhĩ Căn",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.8tsw.com/files/article/image/0/681/681s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/0_681/",
        "views": "9.5M",
        "views_count": 9500000,
        "rating": 9.8,
        "total_chapters": 1314,
        "tags": ["Bạch Tiểu Thuần", "Hài Hước", "Trường Sinh", "Tu Tiên"],
        "description_vi": "Bạch Tiểu Thuần sợ chết vô cùng, một lòng chỉ muốn cầu trường sinh bất tử. Tính tình hài hước, gây họa khắp Linh Khê Tông nhưng khi tông môn lâm nguy lại sẵn sàng xông pha cứu vạn người!"
    },
    {
        "id": "hh_14",
        "title": "万古神帝",
        "title_vi": "Vạn Cổ Thần Đế",
        "author": "飞天鱼",
        "author_vi": "Phi Thiên Ngư",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.8tsw.com/files/article/image/0/786/786s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/0_786/",
        "views": "14.2M",
        "views_count": 14200000,
        "rating": 9.7,
        "total_chapters": 4200,
        "tags": ["Trương Nhược Trần", "Trọng Sinh", "Trả Thù", "Nữ Hoàng"],
        "description_vi": "800 năm trước, Trương Nhược Trần bị vị hôn thê là Trì Dao công chúa sát hại. 800 năm sau hắn tái sinh, vị hôn thê năm xưa nay đã là Đệ Nhất Nữ Hoàng uy chấn Côn Lôn giới!"
    },
    {
        "id": "hh_15",
        "title": "我师兄实在太稳健了",
        "title_vi": "Sư Huynh Ta Quá Cẩn Thận",
        "author": "言归正传",
        "author_vi": "Ngôn Quy Chính Truyện",
        "category": "huyen_huyen",
        "category_name": "Huyền Huyễn",
        "cover_url": "https://www.8tsw.com/files/article/image/39/39812/39812s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/39_39812/",
        "views": "8.8M",
        "views_count": 8800000,
        "rating": 9.8,
        "total_chapters": 776,
        "tags": ["Hồng Hoang", "Cẩu Đạo", "Hài Hước", "Lý Trường Thọ"],
        "description_vi": "Trọng sinh vào thời kỳ Hồng Hoang trước phong thần, Lý Trường Thọ tâm niệm chỉ có 'cẩn thận'. Giấu nghề 99 tầng, không có nắm chắc 98% thì quyết không xuất thủ, một đường an ổn phi thăng!"
    },
    {
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
    },
    {
        "id": "sys_9",
        "title": "不科学御兽",
        "title_vi": "Bất Khoa Học Ngự Thú",
        "author": "轻泉流响",
        "author_vi": "Khinh Tuyền Lưu Hưởng",
        "category": "he_thong",
        "category_name": "Hệ Thống",
        "cover_url": "https://www.8tsw.com/files/article/image/92/92415/92415s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/92_92415/",
        "views": "7.6M",
        "views_count": 7600000,
        "rating": 9.8,
        "total_chapters": 750,
        "tags": ["Ngự Thú", "Hài Hước", "Thời Vũ", "Tiến Hóa"],
        "description_vi": "Một thế giới ngự thú nơi thần sủng tung hoành. Thời Vũ nắm giữ kỹ năng 'sao chép dạy bù', dạy Panda bình thường học được Lôi Điện Chấn Động, biến sủng vật thành những quái vật phản khoa học!"
    },
    {
        "id": "ls_5",
        "title": "雪中悍刀行",
        "title_vi": "Tuyết Trung Hãn Đao Hành",
        "author": "烽火戏诸侯",
        "author_vi": "Phong Hỏa Hí Chư Hầu",
        "category": "lich_su",
        "category_name": "Lịch Sử",
        "cover_url": "https://www.8tsw.com/files/article/image/0/98/98s.jpg",
        "source_domain": "8tsw.com",
        "source_url": "https://www.8tsw.com/0_98/",
        "views": "13.8M",
        "views_count": 13800000,
        "rating": 9.9,
        "total_chapters": 1004,
        "tags": ["Giang Hồ", "Bắc Lương", "Từ Phượng Niên", "Võ Hiệp"],
        "description_vi": "Bắc Lương thế tử Từ Phượng Niên giả dạng ăn chơi trác táng, bước chân vào giang hồ đao quang kiếm ảnh, gánh vác 30 vạn thiết kỵ Bắc Lương chống lại Bắc Mãng bảo vệ Trung Nguyên."
    }
]

# Cache in-memory for live web novels
_CACHED_LIVE_NOVELS = None

def format_number_compact(n: int) -> str:
    if n >= 1_000_000:
        val = n / 1_000_000
        return f"{val:.1f}M" if val < 100 else f"{int(val)}M"
    elif n >= 1_000:
        val = n / 1_000
        return f"{val:.1f}k" if val < 100 else f"{int(val)}k"
    return str(n)

def enrich_novel_metrics(n: Dict[str, Any]) -> Dict[str, Any]:
    """Calculate realistic, consistent weekly, monthly, yearly, and total views and hot score"""
    seed = abs(hash(str(n.get("id", "")) + str(n.get("title", ""))))
    base_views = n.get("views_count") or (seed % 4000000 + 800000)
    rating = n.get("rating") or round(8.8 + (seed % 12) / 10.0, 1)

    # Weekly views: 1.5% to 4.5% of total
    week_ratio = 0.015 + ((seed % 30) / 1000.0)
    views_week_count = max(1000, int(base_views * week_ratio))

    # Monthly views: 8% to 18% of total
    month_ratio = 0.08 + ((seed % 100) / 1000.0)
    views_month_count = max(views_week_count * 3, int(base_views * month_ratio))

    # Yearly views: 45% to 75% of total
    year_ratio = 0.45 + ((seed % 300) / 1000.0)
    views_year_count = max(views_month_count * 4, int(base_views * year_ratio))

    views_total_count = max(views_year_count, base_views)

    # Hot scores (views * (rating / 8.0) * bonus)
    hot_week = int(views_week_count * (rating / 8.0) * (1.0 + (seed % 20) / 100.0))
    hot_month = int(views_month_count * (rating / 8.0) * (1.0 + (seed % 20) / 100.0))
    hot_year = int(views_year_count * (rating / 8.0) * (1.0 + (seed % 20) / 100.0))
    hot_total = int(views_total_count * (rating / 8.0))

    n["views_count"] = views_total_count
    n["views_total"] = format_number_compact(views_total_count)
    n["views_total_fmt"] = n["views_total"]
    n["views_week_count"] = views_week_count
    n["views_week"] = format_number_compact(views_week_count)
    n["views_week_fmt"] = n["views_week"]
    n["views_month_count"] = views_month_count
    n["views_month"] = format_number_compact(views_month_count)
    n["views_month_fmt"] = n["views_month"]
    n["views_year_count"] = views_year_count
    n["views_year"] = format_number_compact(views_year_count)
    n["views_year_fmt"] = n["views_year"]

    n["hot_week"] = hot_week
    n["hot_week_str"] = format_number_compact(hot_week)
    n["hot_week_fmt"] = n["hot_week_str"]
    n["hot_month"] = hot_month
    n["hot_month_str"] = format_number_compact(hot_month)
    n["hot_month_fmt"] = n["hot_month_str"]
    n["hot_year"] = hot_year
    n["hot_year_str"] = format_number_compact(hot_year)
    n["hot_year_fmt"] = n["hot_year_str"]
    n["hot_total"] = hot_total
    n["hot_total_str"] = format_number_compact(hot_total)
    n["hot_total_fmt"] = n["hot_total_str"]

    n["views"] = format_number_compact(views_total_count)
    return n

def load_live_web_novels() -> List[Dict[str, Any]]:
    """Load the 3,000 live Chinese novels parsed from 8tsw / Biquge cache"""
    global _CACHED_LIVE_NOVELS
    if _CACHED_LIVE_NOVELS is not None:
        return _CACHED_LIVE_NOVELS

    cache_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "web_novels_cache.json")
    if os.path.exists(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                _CACHED_LIVE_NOVELS = json.load(f)
                return _CACHED_LIVE_NOVELS
        except Exception as e:
            print(f"Error loading web_novels_cache: {e}")
            return []
    return []

def get_catalog_novels(
    category: str = "all",
    sort_by: str = "views",
    time_range: str = "all",
    search: Optional[str] = None,
    source_mode: str = "all",
    page: int = 1,
    page_size: int = 24
) -> Dict[str, Any]:
    """Query catalog combining curated masterpieces and 3,000+ live Chinese web novels with pagination, time ranges, and hot rankings"""
    curated = CURATED_NOVELS
    live = load_live_web_novels()

    if source_mode == "curated":
        raw_items = list(curated)
    elif source_mode == "live":
        raw_items = list(live)
    else: # all: curated on top, followed by live
        raw_items = list(curated) + list(live)

    # Enrich with weekly/monthly/yearly views and hot scores
    items = [enrich_novel_metrics(dict(n)) for n in raw_items]

    if category and category != "all":
        items = [n for n in items if n.get("category") == category]

    if search:
        q = search.lower().strip()
        items = [
            n for n in items
            if q in n.get("title", "").lower() or q in n.get("title_vi", "").lower()
            or q in n.get("author", "").lower() or q in n.get("author_vi", "").lower()
            or any(q in t.lower() for t in n.get("tags", []))
        ]

    # Time-based sorting for Hot and Views
    if sort_by == "hot":
        if time_range == "week":
            items = sorted(items, key=lambda x: x.get("hot_week", 0), reverse=True)
        elif time_range == "month":
            items = sorted(items, key=lambda x: x.get("hot_month", 0), reverse=True)
        elif time_range == "year":
            items = sorted(items, key=lambda x: x.get("hot_year", 0), reverse=True)
        else: # all
            items = sorted(items, key=lambda x: x.get("hot_total", 0), reverse=True)
    elif sort_by == "views":
        if time_range == "week":
            items = sorted(items, key=lambda x: x.get("views_week_count", 0), reverse=True)
        elif time_range == "month":
            items = sorted(items, key=lambda x: x.get("views_month_count", 0), reverse=True)
        elif time_range == "year":
            items = sorted(items, key=lambda x: x.get("views_year_count", 0), reverse=True)
        else: # all
            items = sorted(items, key=lambda x: x.get("views_total_count", 0), reverse=True)
    elif sort_by == "rating":
        items = sorted(items, key=lambda x: x.get("rating", 0), reverse=True)
    elif sort_by == "chapters":
        items = sorted(items, key=lambda x: x.get("total_chapters", 0), reverse=True)

    total = len(items)
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paged_items = items[start_idx:end_idx]

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "has_more": end_idx < total,
        "items": paged_items
    }

async def fetch_live_category_from_biquge(category_slug: str = "xuanhuanxiaoshuo") -> List[Dict[str, Any]]:
    """Live scraper from Chinese web novel mirror for real-time fresh novels"""
    url = f"https://www.8tsw.com/{category_slug}/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=12.0) as client:
            resp = await client.get(url)
            if resp.status_code != 200:
                return []

            html = detect_and_decode(resp.content, explicit_encoding="gb18030")
            soup = BeautifulSoup(html, "lxml")

            novels = []
            # Parse .item cards
            items = soup.select(".item")
            for it in items:
                img = it.find("img")
                a = it.select_one("dl dt a")
                author_el = it.select_one("dl dt span")
                desc_el = it.select_one("dl dd")

                if not a:
                    continue

                title = a.get_text(strip=True)
                href = urllib.parse.urljoin(url, a.get("href"))
                cover = urllib.parse.urljoin(url, img.get("src") if img else "")
                author = author_el.get_text(strip=True) if author_el else "Chưa rõ"
                desc = desc_el.get_text(strip=True) if desc_el else "Truyện thịnh hành đang được theo dõi nhiều trên web Trung Quốc."

                novels.append({
                    "id": f"live_{hash(href) % 1000000}",
                    "title": title,
                    "title_vi": title, # Can be viewed or translated
                    "author": author,
                    "author_vi": author,
                    "category": "huyen_huyen",
                    "category_name": "Web Trung Hot",
                    "cover_url": cover,
                    "source_domain": "8tsw.com",
                    "source_url": href,
                    "views": "Mới nổi",
                    "views_count": 1500000,
                    "rating": 9.5,
                    "total_chapters": 500,
                    "tags": ["Live Cào Web", "Thịnh Hành"],
                    "description_vi": desc
                })

            return novels
    except Exception as e:
        print(f"Error live fetching: {e}")
        return []
