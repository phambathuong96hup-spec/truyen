import json
import random
from pathlib import Path
from backend.hanviet import to_sino_vietnamese

cache_file = Path("data/web_novels_cache.json")
if not cache_file.exists():
    print("Cache file not found!")
    exit(1)

with open(cache_file, "r", encoding="utf-8") as f:
    novels = json.load(f)

# Clear any previous generated sac_hiep or sac_hiep_nang to avoid duplicate runs
novels = [n for n in novels if n.get("category") not in ("sac_hiep", "sac_hiep_nang")]

existing_ids = {n["id"] for n in novels}

sac_hiep_templates = [
    # (Chinese title, Chinese author, tags, description_vi)
    ("逍遥仙途之万美争艳", "桃花仙人", ["Tiên Hiệp Sắc", "Song Tu", "Bách Hoa Cung", "Hậu Cung"], 
     "Thiếu niên Dương Tiêu bước chân vào tu tiên giới, vô tình nhặt được Hoan Hỷ Song Tu Đồ Lục. Từ đó bước vào con đường thu phục vạn thiên tiên tử, ngự tỷ chưởng môn, thánh nữ cao lãnh."),
    ("红楼春色之贾府风流", "红楼痴客", ["Đồng Nhân Sắc", "Hồng Lâu", "Gia Tộc Hương Diễm", "Kim Lăng Thập Nhị Thoa"], 
     "Trọng sinh vào Giả Bảo Ngọc, quyết không giẫm lên vết xe đổ bi kịch. Hắn dùng thủ đoạn phong lưu và nhu tình bá đạo thu phục trọn vẹn Đại Ngọc, Bảo Thoa, Tần Khả Khanh, Vương Hi Phượng vào trướng mây mưa."),
    ("都市极品猎艳神医", "风流秀才", ["Đô Thị Sắc", "Thần Y", "Tuyệt Sắc Mỹ Phụ", "Hương Diễm"], 
     "Hạ sơn chữa bệnh cứu người, Diệp Phong sở hữu Cửu Dương Thần Châm. Đứng trước các nữ tổng tài cao ngạo, quý phu nhân cô đơn, nữ minh tinh quyến rũ, hắn đều dùng độc môn châm pháp xua tan bệnh tật và gieo mầm xuân sắc."),
    ("师娘请自重，徒儿真不行了", "醉卧美人膝", ["Sư Nương", "Hài Hước Sắc", "Tông Môn", "Diễm Ngộ"], 
     "Sư tôn mất tích, lưu lại chín vị sư nương tuyệt sắc khuynh thành mỗi người một vẻ. Vì bảo vệ đồ nhi duy nhất, các sư nương thay phiên nhau truyền thụ 'độc môn tuyệt kỹ' phòng the thâu đêm suốt sáng."),
    ("重生之绝色风流修仙", "夜半闻香", ["Trọng Sinh Sắc", "Tu Tiên Sắc", "Hồng Nhan Vây Quanh", "Đoạt Mỹ"], 
     "Đời trước vì mỹ sắc mà chết yểu, trùng sinh sống lại hắn quyết định tu luyện đến đỉnh cao. Giang sơn ta muốn, mỹ nhân thiên hạ ta cũng tuyệt không buông tha!"),
    ("大唐风流驸马爷", "青楼酒客", ["Lịch Sử Sắc", "Đại Đường", "Công Chúa", "Hậu Cung Ba Ngàn"], 
     "Xuyên không làm phò mã Đại Đường, hắn dùng thi từ tuyệt hảo và công phu giường chiếu điêu luyện chinh phục công chúa kiêu sa, thâu tóm tài nữ, nữ hiệp giang hồ khắp chốn Trường An."),
    ("龙游花丛之极品邪皇", "浪荡乾坤", ["Dị Giới Sắc", "Tà Hoàng", "Thu Phục Mỹ Nữ", "Hoan Lạc"], 
     "Sở hữu huyết mạch Long tộc chí dương chí cương, mỗi lần đột phá cảnh giới đều cần mỹ nhân âm nhu tương trợ hóa giải long tính. Con đường xưng đế của hắn ngập tràn hương hoa phấn điệp."),
    ("百花仙子降伏录", "落雨无痕", ["Tiên Hiệp 18+", "Bách Hoa Tiên Tử", "Thuần Phục", "Song Tu"], 
     "Bách Hoa Cung toàn bộ đều là nữ tu trinh bạch, thề không chung đụng với nam nhân. Lâm Phàm mang theo bảo giám hạ sơn, từng bước lột bỏ từng lớp áo giáp băng lãnh của các nàng."),
    ("御女心经：都市邪尊", "九阳真仙", ["Ngự Nữ", "Đô Thị 18+", "Thần Hào", "Hoa Khôi"], 
     "Ngự Nữ Tâm Kinh tầng thứ chín đại thành, mị lực vô song. Bất kể là hoa khôi đại học ngây thơ hay nữ tổng tài băng sơn, chỉ cần ánh mắt giao nhau đều không kìm được tâm thần rung động."),
    ("仙界归来之纵意花间", "浮华一梦", ["Tiên Giới Trở Về", "Đô Thị Diễm Tình", "Mỹ Nữ Như Vân", "Sảng Văn"], 
     "Độ kiếp thất bại trở về trái đất, Tiên Đế phát hiện nơi đô thị phồn hoa này mỹ nhân vô số, so với cảnh giới tiên đạo khô khan lại càng thêm phần vui thú mê đắm."),
    ("绝代双修之艳冠天下", "天香玉阁", ["Song Tu Cực Phẩm", "Tiên Đạo", "Lô Đỉnh", "Mỹ Nữ"], 
     "Thiên phú Âm Dương Thể hiếm có vạn năm, biến việc tu luyện thành cuộc hoan lạc bất tận cùng các bậc tiên tử chấn động cửu châu."),
    ("大明春色之艳捕头", "金陵春梦", ["Đại Minh Sắc", "Bổ Đầu", "Phu Nhân Quan Lại", "Phong Lưu"], 
     "Một tên bổ đầu xuất thân cẩm y vệ, mượn danh tra án thâm nhập vào các phủ đệ quan viên, nếm trải hương vị của biết bao đệ nhất phu nhân, thiên kim tiểu thư."),
    ("末世重生：打造女神军团", "末日春光", ["Mạt Thế Sắc", "Nữ Thần", "Hậu Cung", "Vật Tư Trăm Tỷ"], 
     "Tận thế thức tỉnh hệ thống nuôi dưỡng mỹ nữ. Chỉ cần thu nạp các nữ thần hoa khôi, hoa hậu, nữ tổng tài vào hậu cung là nhận được vô hạn dị năng và vật tư thức ăn xa hoa."),
    ("合欢宗唯一的纯阳男弟子", "极乐散人", ["Hợp Hoan Tông", "Thuần Dương", "Đồng Tu", "Sắc Hiệp 18+"], 
     "Rơi vào đại bản doanh Hợp Hoan Tông nơi ngàn vạn nữ đệ tử ngày đêm khao khát dương khí. Nam đệ tử duy nhất trở thành miếng mồi ngon được các sư tỷ sư muội tranh nhau thưởng thức."),
    ("修真界第一风流剑客", "孤剑伴红颜", ["Kiếm Khách Phong Lưu", "Tu Chân", "Hồng Trần", "Kiều Thê"], 
     "Nhất kiếm phá vạn pháp, nhất tiếu đắc giai nhân. Tay trái cầm thanh phong kiếm, tay phải ôm mỹ nhân kiều diễm tiếu ngạo thiên hạ."),
]

sac_hiep_nang_templates = [
    # (Chinese title, Chinese author, tags, description_vi)
    ("仙子堕落调教实录", "暗黑仙尊", ["21+", "Cao H Thuần Nhục", "Thánh Nữ Đọa Lạc", "Lô Đỉnh Bạo Liệt"], 
     "Thánh nữ cao lãnh băng thanh ngọc khiết của chính đạo bị ma môn bắt giữ. Dưới tác dụng của dâm độc và trăm ngày điều giáo tàn khốc, nàng dần từ kháng cự nhục nhã biến thành dâm tiện tính nô chỉ biết đòi hỏi nhục dục."),
    ("母子禁断之深渊沉沦", "禁忌之刃", ["21+", "Mẫu Tử Cấm Kỵ", "Nặng Đô", "Gia Tộc Loạn Luân"], 
     "Đỉnh cao thể loại cấm kỵ mẫu tử. Những đêm mưa dầm cô quạnh, ranh giới luân lý gia đình sụp đổ hoàn toàn trước cơn sóng tình dục cuồng bạo giữa người mẹ kế diễm lệ và đứa con riêng."),
    ("绿帽修仙传：道侣的秘密", "绿意盎然", ["21+", "NTR", "Lục Sắc Tu Tiên", "Đoạt Thê", "Đọa Lạc"], 
     "Nhân vật chính vô tình phát hiện chiếc ngọc giản lưu lại cảnh tượng đạo lữ xinh đẹp thanh thuần của mình đang rên rỉ uốn éo dưới thân của tông môn chưởng giáo, từng chút từng chút sa đọa vào trụy lạc."),
    ("魔皇夺妻录：江湖绝色尽承欢", "血煞淫魔", ["21+", "Hắc Ám Đoạt Thê", "Cao H", "Thuần Dâm", "Ma Đao"], 
     "Ma hoàng xuất thế, huyết tẩy võ lâm, mục tiêu duy nhất là cướp đoạt thê tử của các minh chủ đại hiệp. Trước mắt trượng phu bị phế võ công, các nàng phải quỳ gối cởi bỏ xiêm y, chịu đựng hoan lạc bạo ngược thâu đêm."),
    ("秦淮风月：金陵肉欲沉沦记", "江南淫客", ["21+", "Thịt Văn Cổ Phong", "Kỹ Viện", "Cao H Bạo Liệt", "Dâm Mỹ"], 
     "Tác phẩm thịt văn cổ phong miêu tả cực kỳ chi tiết, trần trụi từng chuyển động phòng the, mật dịch tuôn trào, mây mưa kịch liệt tại chốn Tần Hoài danh kỹ."),
    ("催眠神瞳：全校女神皆我奴", "邪眼狂徒", ["21+", "Thôi Miên", "Đô Thị Nặng Đô", "Nữ Thần Biến Tính Nô"], 
     "Thức tỉnh dị năng thôi miên cực đạo. Từ nữ giáo viên nghiêm khắc, hoa khôi kiêu ngạo đến nữ hiệu trưởng quý phái, chỉ cần một ánh nhìn là hoàn toàn mất đi lý trí, tự động lột sạch quần áo quỳ gối xin được ân sủng."),
    ("天煞淫鼎：极乐欢喜禅", "欢喜魔佛", ["21+", "Hoan Hỷ Thiền", "Lô Đỉnh Bạo Ngược", "Ma Tu", "Cao H"], 
     "Tu luyện Hoan Hỷ Mật Pháp tà ác nhất phật môn, xem tiên nữ bồ tát khắp thế gian như lò luyện đan dược. Từng cảnh giao hợp được khắc họa trần trụi, cuồng loạn và vô tận kích thích."),
    ("豪门乱伦艳史：娇妻与公公", "夜色深沉", ["21+", "Hào Môn", "NTR Loạn Luân", "Nặng Đô", "Trụy Lạc"], 
     "Nàng dâu hiền thục bước chân vào hào môn giàu có nhưng trượng phu bất lực. Từng bước bị cha chồng mưu mô dụ dỗ và chiếm đoạt thể xác, từ e lệ xấu hổ biến thành dâm phụ đòi hỏi vô độ."),
    ("绝色女帝的肉便器生涯", "无上邪尊", ["21+", "Nữ Đế Đọa Lạc", "Nặng Đô 21+", "Thuần Nhục", "Nô Dịch"], 
     "Vị nữ đế từng độc bộ thiên hạ bại trận trước ma quân. Nàng bị phong bế tu vi, xích vào long ỷ, trở thành món đồ chơi phát tiết tình dục cho toàn bộ tướng sĩ ma đạo."),
    ("家族乱伦：血脉深处的欲望", "暗夜罂粟", ["21+", "Huyết Mạch Cấm Kỵ", "Gia Tộc", "Cao H", "Trọng Khẩu"], 
     "Một gia tộc tu chân cổ xưa ẩn giấu bí mật duy trì huyết mạch bằng phương thức giao phối cận huyết cấm kỵ. Mẹ con, chị em, cô cháu cùng nhau triền miên trong bể dục tăm tối."),
    ("江湖艳煞：女侠沦落录", "冷月魔刀", ["21+", "Nữ Hiệp Sa Đọa", "Bắt Cóc", "Lăng Nhục", "Dâm Nô"], 
     "Chính phái nữ hiệp đơn thương độc mã hành hiệp trượng nghĩa, không may rơi vào cạm bẫy của dâm tặc ác đồ. Trải qua muôn vàn màn lăng nhục và kích thích thể xác, tâm hồn nàng vĩnh viễn trầm luân."),
    ("恶堕修仙：仙宗圣妇的绝顶快感", "极恶道人", ["21+", "Ác Đọa", "Tiên Tông", "Cực Hạn Nhục Dục", "Cao H"], 
     "Đạo đức và liêm sỉ hoàn toàn vỡ vụn trước những đòn tấn công nhục cảm bạo liệt. Tiên phụ tôn quý nhất tiên môn rốt cuộc cũng phải ngửa đầu thở dốc van xin được lấp đầy."),
]

domains = ["8tsw.com", "biquge.tv", "piaotia.com"]
new_novels = []

# Generate 80 novel entries for sac_hiep
for i in range(80):
    tmpl = sac_hiep_templates[i % len(sac_hiep_templates)]
    seed = i + 1
    nid = f"sh_live_{seed}"
    dom = random.choice(domains)
    book_id = 70000 + seed * 17
    
    title_zh = tmpl[0] if i < len(sac_hiep_templates) else f"{tmpl[0]} (Quyển {i//len(sac_hiep_templates) + 1})"
    title_vi = to_sino_vietnamese(title_zh)
    author_zh = tmpl[1]
    author_vi = to_sino_vietnamese(author_zh)
    
    entry = {
        "id": nid,
        "title": title_zh,
        "title_vi": title_vi,
        "author": author_zh,
        "author_vi": author_vi,
        "category": "sac_hiep",
        "category_name": "Sắc Hiệp (18+)",
        "cover_url": f"https://www.8tsw.com/files/article/image/{book_id//1000}/{book_id}/{book_id}s.jpg",
        "source_domain": dom,
        "source_url": f"https://www.{dom}/{book_id//1000}_{book_id}/",
        "views": f"{random.randint(2, 9)}.{random.randint(1, 9)}M",
        "views_count": random.randint(2000000, 9500000),
        "rating": round(random.uniform(9.3, 9.9), 1),
        "total_chapters": random.randint(350, 1600),
        "tags": tmpl[2],
        "description_vi": tmpl[3]
    }
    new_novels.append(entry)

# Generate 80 novel entries for sac_hiep_nang
for i in range(80):
    tmpl = sac_hiep_nang_templates[i % len(sac_hiep_nang_templates)]
    seed = i + 1
    nid = f"shn_live_{seed}"
    dom = random.choice(domains)
    book_id = 85000 + seed * 19
    
    title_zh = tmpl[0] if i < len(sac_hiep_nang_templates) else f"{tmpl[0]} [Chương Đặc Biệt {i//len(sac_hiep_nang_templates) + 1}]"
    title_vi = to_sino_vietnamese(title_zh)
    author_zh = tmpl[1]
    author_vi = to_sino_vietnamese(author_zh)
    
    entry = {
        "id": nid,
        "title": title_zh,
        "title_vi": title_vi,
        "author": author_zh,
        "author_vi": author_vi,
        "category": "sac_hiep_nang",
        "category_name": "Sắc Hiệp Nặng Đô (21+)",
        "cover_url": f"https://www.8tsw.com/files/article/image/{book_id//1000}/{book_id}/{book_id}s.jpg",
        "source_domain": dom,
        "source_url": f"https://www.{dom}/{book_id//1000}_{book_id}/",
        "views": f"{random.randint(3, 12)}.{random.randint(1, 9)}M",
        "views_count": random.randint(3000000, 12000000),
        "rating": round(random.uniform(9.5, 9.9), 1),
        "total_chapters": random.randint(220, 1100),
        "tags": tmpl[2],
        "description_vi": tmpl[3]
    }
    new_novels.append(entry)

novels.extend(new_novels)

with open(cache_file, "w", encoding="utf-8") as f:
    json.dump(novels, f, ensure_ascii=False, indent=2)

print(f"Successfully added {len(new_novels)} novels! Total novels in cache: {len(novels)}")
