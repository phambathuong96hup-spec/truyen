import asyncio
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from backend.database import init_db, AsyncSessionLocal
from backend.models import Novel, Chapter
from sqlalchemy import select
from backend.discover import CURATED_NOVELS

SAC_HIEP_NOVELS_TO_IMPORT = [
    # --- 1. SẮC HIỆP 18+ ---
    {
        "catalog_id": "sh_1",
        "title": "风流大法师",
        "title_vi": "Phong Lưu Đại Pháp Sư",
        "author": "Thiên Đường Bất Tịch Mịch (天堂不寂寞)",
        "cover_url": "https://www.biquge.tv/files/article/image/0/654/654s.jpg",
        "source_url": "https://www.biquge.tv/0_654/",
        "genre": "Sắc Hiệp (18+)",
        "description": "Tác phẩm huyền huyễn sắc hiệp kinh điển đời đầu làm say đắm biết bao độc giả! Long Nhất mang theo công pháp Lôi Thần Quyết xuyên việt đến dị giới ma pháp, bước vào con đường chinh phục vô số cực phẩm mỹ nhân từ tinh linh nữ vương, công chúa đế quốc đến nữ thần long tộc!",
        "total_chapters": 120,
        "sample_chapters": [
            ("第一章 重生异界狂少", "Chương 1: Trọng Sinh Dị Giới Cuồng Thiếu", 
             "Long Nhất chậm rãi mở mắt ra, đập vào mắt hắn là một căn phòng tráng lệ mang đậm phong cách cung đình châu Âu cổ xưa.\n\n"
             "Đầu óc hắn đau nhức như muốn nứt toác, từng đợt ký ức xa lạ cuồn cuộn ùa về. Hắn vốn là truyền nhân duy nhất của Lôi Thần Quyết ở Địa Cầu, trong một lần độ kiếp phi thăng thất bại lại vô tình tá thi hoàn hồn vào thân xác của một tên hoàn khố đại thiếu gia nức tiếng kinh thành tại dị giới ma pháp này.\n\n"
             "\"Thiếu gia, ngài rốt cuộc cũng tỉnh rồi!\"\n\n"
             "Một giọng nói mềm mại như chim oanh líu lo vang lên bên tai. Long Nhất quay đầu nhìn lại, không khỏi hít sâu một hơi khí lạnh. Trước mắt hắn là một thiếu nữ tuyệt sắc độ mười bảy mười tám tuổi, mái tóc dài óng ả buông lơi trên bờ vai gầy, khuôn mặt thanh tú diễm lệ mang theo vài phần e ấp. Nàng mặc bộ váy tơ tằm mỏng manh, đôi gò bồng đảo căng tròn thoắt ẩn thoắt hiện dưới lớp lụa mỏng khiến huyết mạch trong người Long Nhất sôi trào dồn dập.\n\n"
             "Long Nhất nhếch môi nở một nụ cười tà mị. Kiếp trước vì chấp niệm với tiên đạo mà bỏ lỡ trăm hoa, kiếp này đã làm cuồng thiếu dị giới, nếu không nếm hết mỹ vị nhân gian thì há chẳng uổng công sống lại một đời sao?"),
            ("第二章 绝色侍女的温存", "Chương 2: Ôn Tồn Cùng Tuyệt Sắc Thị Nữ", 
             "Bóng đêm dần buông xuống phủ đệ Đại tướng quân. Gió đêm mơn man qua rèm lụa lay động, mang theo hương thơm ngát tự nhiên từ da thịt của thiếu nữ bên cạnh.\n\n"
             "Thiếu nữ tên là Tuyết Nhi, thị nữ thân cận nhất của Long Nhất từ nhỏ. Nàng bưng chén canh sen nóng hổi bước vào, hai má ửng hồng khi bắt gặp ánh mắt nóng rực như ngọn lửa của thiếu gia.\n\n"
             "\"Thiếu gia... ngài sao lại nhìn Tuyết Nhi như vậy?\"\n\n"
             "Long Nhất không nói một lời, vươn tay kéo nhẹ một cái, thân thể mềm mại thơm tho của Tuyết Nhi đã rơi gọn vào trong lòng hắn. Cảm nhận được sự đàn hồi căng tràn cùng hơi thở gấp gáp dồn dập của nàng, Long Nhất khẽ cúi đầu ngậm lấy vành tai trắng nõn của giai nhân, khơi dậy từng đợt sóng tình triền miên trong căn phòng yên tĩnh."),
            ("第三章 帝国第一美人的婚约", "Chương 3: Hôn Ước Với Đệ Nhất Mỹ Nhân Đế Quốc", 
             "Sáng hôm sau, tiếng đao kiếm luyện tập cùng tiếng quát tháo ngoài hoa viên đánh thức Long Nhất.\n\n"
             "Một tin tức chấn động kinh thành vừa truyền tới: Công chúa Tiêu Nguyệt – đệ nhất mỹ nhân kiêu kỳ của đế quốc, vị hôn thê trên danh nghĩa của Long Nhất – chuẩn bị đích thân tới phủ để từ hôn!\n\n"
             "\"Từ hôn sao?\" Long Nhất cười lạnh, đứng dậy vận chuyển Lôi Thần Quyết một chu thiên. Luồng chân khí nóng rực chảy xuôi khắp kinh mạch tứ chi: \"Muốn từ hôn với Long Nhất ta, e rằng nàng còn chưa đủ tư cách! Hôm nay bổn thiếu gia sẽ cho nàng biết thế nào là quy phục dưới chân nam nhân!\"")
        ]
    },
    {
        "catalog_id": "sh_2",
        "title": "猎艳江湖梦",
        "title_vi": "Liệp Diễm Giang Hồ Mộng",
        "author": "Thần Khóc Quỷ Khiếu (神哭鬼啸)",
        "cover_url": "https://www.biquge.tv/files/article/image/2/2311/2311s.jpg",
        "source_url": "https://www.biquge.tv/2_2311/",
        "genre": "Sắc Hiệp (18+)",
        "description": "Đệ nhất kiếm hiệp sắc tình kinh điển! Thiếu niên Tô Triệt bước vào giang hồ ân oán tình thù, tu luyện Âm Dương Hoan Hỷ Thiền. Dưới đao kiếm phân tranh là những màn liệp diễm phong lưu, hàng phục các đại chưởng môn nữ phái, nữ hiệp băng thanh ngọc khiết và ma giáo yêu nữ.",
        "total_chapters": 100,
        "sample_chapters": [
            ("第一章 初涉江湖遇绝色", "Chương 1: Mới Vào Giang Hồ Gặp Tuyệt Sắc",
             "Rừng phong tháng mười đỏ thẫm như máu, lá rụng xào xạc theo từng cơn gió lạnh chiều thu.\n\n"
             "Tô Triệt lưng đeo trường kiếm, một thân áo xanh phiêu dật bước đi trên đường mòn núi Hành Sơn. Hắn vốn là đệ tử tục gia của Thiếu Lâm, cơ duyên xảo hợp lại nhặt được tàn thiên 'Âm Dương Hoan Hỷ Mật Quyển' từ một sơn động cổ xưa, từ đó bước chân vào con đường tu luyện song tu độc nhất vô nhị.\n\n"
             "Đang lúc dừng chân bên suối nước trong vắt, bỗng một tiếng thở dốc yêu kiều xen lẫn thống khổ truyền tới từ sau bụi hoa mẫu đơn hoang dại.\n\n"
             "Tô Triệt nhẹ nhàng lướt tới, chỉ thấy một nữ tử bạch y đang ngã gục bên tảng đá xanh. Nàng tuổi chừng hai mươi ba mươi, khuôn mặt thanh tú thoát tục tựa tiên tử giáng trần, nhưng lúc này hai gò má lại ửng hồng dị thường, hơi thở dồn dập nóng bỏng, vạt áo trước ngực hé mở để lộ làn da trắng ngần lấp lánh mồ hôi xuân."),
            ("第二章 阴阳合欢解奇毒", "Chương 2: Âm Dương Hợp Hoan Giải Kỳ Độc",
             "\"Cô nương... nàng bị trúng phải Âm Dương Dâm Cổ?\"\n\n"
             "Tô Triệt vừa chạm vào cổ tay nữ tử, một luồng nhiệt lưu cuồng bạo đã lập tức theo kinh mạch truyền sang. Nữ tử mở to đôi mắt long lanh ngấn nước mờ mịt dục vọng, run rẩy cắn môi:\n\n"
             "\"Ta là Thẩm Lạc Nhạn của phái Nga Mi... Mau giết ta... đừng để tà độc làm ô uế thanh danh của ta...\"\n\n"
             "\"Giết nàng thì dễ, nhưng cứu nàng mới là bản lĩnh của ta.\" Tô Triệt khẽ thở dài, vận chuyển nội lực Âm Dương Hoan Hỷ Thiền. Hắn cúi xuống ôm trọn thân thể mềm nhũn đang run rẩy vì xuân tình của chưởng môn nữ hiệp vào lòng, dùng bờ môi ấm áp chặn lại tiếng thở than nghẹn ngào giữa rừng phong hoang vắng.")
        ]
    },
    {
        "catalog_id": "sh_3",
        "title": "琼明剑典",
        "title_vi": "Quỳnh Minh Kiếm Điển",
        "author": "Kiếm Đoạn Cửu Châu (剑断九洲)",
        "cover_url": "https://www.8tsw.com/files/article/image/58/58210/58210s.jpg",
        "source_url": "https://www.8tsw.com/58_58210/",
        "genre": "Sắc Hiệp (18+)",
        "description": "Tuyệt phẩm tiên hiệp sắc diễm lệ bậc nhất văn đàn mạng! Thiếu niên Ô Hành Tuyết tu kiếm vấn đạo giữa hồng trần tình kiếp. Từng trang truyện là sự giao thoa đỉnh cao giữa kiếm ý ngút trời và dục vọng tình si, đan xen cùng những phân đoạn ân ái rung động tâm can giữa sư đồ, tuyệt sắc kiếm tiên.",
        "total_chapters": 90,
        "sample_chapters": [
            ("第一章 暮雪千山遇剑仙", "Chương 1: Mộ Tuyết Thiên Sơn Gặp Kiếm Tiên",
             "Tuyết rơi ngập tràn đỉnh Quỳnh Minh, trắng xóa một màu thê lương vạn cổ.\n\n"
             "Dưới tàng cây tùng cổ thụ nghìn năm tuổi, một bóng hình tuyệt mỹ đứng sừng sững như một thanh tiên kiếm cắm thẳng vào trời xanh. Nàng mặc trường bào màu tuyết trắng, mái tóc đen như gỗ mun buông dài chấm eo, trên dung nhan tuyệt thế ấy là sự băng lãnh ngạo nghễ không màng thế tục.\n\n"
             "Nàng chính là Quỳnh Minh Kiếm Tông đệ nhất nhân – Bùi Ngữ Hàm.\n\n"
             "\"Hành Tuyết, ngươi đã quỳ ở đây ba ngày ba đêm. Kiếm đạo của ngươi là gì?\"\n\n"
             "Thiếu niên quỳ dưới chân nàng ngẩng đầu lên, ánh mắt trong trẻo nhưng rực cháy ngọn lửa kiên định: \"Kiếm đạo của đệ tử không phải vì thiên hạ, cũng không phải vì trường sinh bất tử. Đệ tử luyện kiếm... chỉ để một ngày có thể sánh bước bên người, bảo vệ người khỏi biển lửa hồng trần!\""),
            ("第二章 剑意缠绵动春心", "Chương 2: Kiếm Ý Triền Miên Động Xuân Tâm",
             "Đêm trăng thanh tĩnh, trong mật thất tịnh tu của Bùi Ngữ Hàm.\n\n"
             "Kiếm ý Quỳnh Minh Lục quyết phản phệ khiến kinh mạch nàng lạnh buốt thấu xương, khí tức hỗn loạn trào dâng. Ô Hành Tuyết không màng tính mạng xông vào, vận chuyển chân nguyên nóng ấm áp chặt vào lưng ngọc của sư tôn.\n\n"
             "Làn da mềm mại thơm tho áp sát vào nhau qua làn lụa mỏng tang. Từng đợt chân khí giao hòa, kiếm ý sắc bén dần biến hóa thành sợi tơ tình si triền miên. Bùi Ngữ Hàm khẽ rên lên một tiếng, thân hình run rẩy ngã tựa vào ngực đệ tử, giọt lệ trong suốt rơi trên má ngọc giữa đêm trăng vằng vặc.")
        ]
    },

    # --- 2. SẮC HIỆP NẶNG ĐÔ 21+ ---
    {
        "catalog_id": "shn_1",
        "title": "朱颜血",
        "title_vi": "Chu Nhan Huyết (Trọn Bộ Hệ Liệt)",
        "author": "Hắc Diệp Tử / Lam Tinh (黑叶子 / 蓝晶)",
        "cover_url": "https://www.8tsw.com/files/article/image/19/19440/19440s.jpg",
        "source_url": "https://www.8tsw.com/19_19440/",
        "genre": "Sắc Hiệp Nặng Đô (21+)",
        "description": "Bộ tiểu thuyết sắc tình hắc ám nặng đô khét tiếng nhất lịch sử mạng Trung Quốc! Tuyệt đối không dành cho người yếu tim. Từng phần là những màn đoạt thê tử, lăng nhục thần thánh, đọa lạc tàn bạo, biến các bậc thánh nữ, hoàng hậu, phu nhân đài các thành tính nô trong vũng lầy nhục dục và bi kịch tột cùng.",
        "total_chapters": 80,
        "sample_chapters": [
            ("第一章 风雨欲来的江南古刹", "Chương 1: Mưa Gió Sắp Đến Tại Giang Nam Cổ Sát",
             "Cơn mưa rào đầu hạ như trút nước xuống ngôi cổ tự đổ nát ngoài thành Kim Lăng.\n\n"
             "Trong đại điện mờ ảo ánh đèn dầu, một đoàn người đang dừng chân trú mưa. Dẫn đầu là phu nhân đệ nhất danh môn vùng Giang Nam – Thẩm Nhược Lam. Nàng tuổi vừa ba mươi, khí chất đoan trang đài các, thân hình đẫy đà tròn trịa được bọc trong bộ y phục gấm hoa sang trọng.\n\n"
             "Nhưng nàng không hề hay biết rằng, trong bóng tối của ngôi chùa hoang phế này, từng đôi mắt hung tàn tà ác đang chăm chú nhìn chằm chằm vào dung nhan kiều diễm và đường cong mê người của nàng.\n\n"
             "Một chiếc bẫy tinh vi đã giăng sẵn, và đêm nay sẽ là khởi đầu của cơn ác mộng vĩnh viễn tước đi tôn nghiêm và trinh bạch của đệ nhất phu nhân."),
            ("第二章 跌落深渊的绝色贵妇", "Chương 2: Đọa Lạc Vực Sâu Của Quý Phụ Tuyệt Sắc",
             "Hương mê hồn thoang thoảng bốc lên từ chiếc lư hương cũ kỹ trên bàn thờ Phật.\n\n"
             "Thẩm Nhược Lam cảm thấy toàn thân mềm nhũn, độc hỏa từ bụng dưới bốc lên cuồn cuộn làm cháy rụi chút lý trí cuối cùng. Nàng muốn gọi hộ vệ nhưng cổ họng chỉ phát ra những tiếng rên rỉ nghẹn ngào quyến rũ.\n\n"
             "Cửa đại điện bật mở, bóng đen tà ác sải bước tiến vào. Từng lớp xiêm y quý phái bị xé rách rơi rụng trên nền gạch ẩm ướt, mở ra một đêm cuồng phong bão táp của nhục dục tàn bạo nuốt chửng đóa hoa phù dung đài các.")
        ]
    },
    {
        "catalog_id": "shn_2",
        "title": "魔刀丽影",
        "title_vi": "Ma Đao Lệ Ảnh",
        "author": "Tuyết Nguyệt Hoa (雪月花)",
        "cover_url": "https://www.8tsw.com/files/article/image/44/44120/44120s.jpg",
        "source_url": "https://www.8tsw.com/44_44120/",
        "genre": "Sắc Hiệp Nặng Đô (21+)",
        "description": "Tà phái ma đao xuất thế, dấy lên một trường dâm phong huyết vũ. Nữ hiệp giang hồ, tiểu thư khuê các lần lượt bị ma đao tà thuật khống chế tâm trí, biến đổi từ trinh bạch kiêu hãnh thành những dâm phụ dâm đãng vô liêm sỉ, phục tùng mọi thú vui bạo liệt.",
        "total_chapters": 85,
        "sample_chapters": [
            ("第一章 魔刀出鞘煞气冲霄", "Chương 1: Ma Đao Xuất Vỏ Sát Khí Xung Tiêu",
             "Thanh ma đao đẫm máu cắm sâu vào tảng đá hoa cương nơi tổng đàn phái Thúy Vân.\n\n"
             "Xung quanh là xác của hàng chục đệ tử chính đạo. Tiêu Dao Hầu tay cầm đoản đao, trên mặt nở nụ cười dữ tợn ma quỷ. Hắn chậm rãi bước tới trước mặt chưởng môn Thúy Vân phái – Vân Tố Tâm, nữ kiếm hiệp lừng lẫy với danh hiệu 'Lãnh Nguyệt Kiếm'.\n\n"
             "Vân Tố Tâm lúc này đã bị phong tỏa kỳ kinh bát mạch, quỳ gối trên mặt đất lạnh giá, nhưng đôi mắt phượng vẫn trợn trừng kiên trinh bất khuất.\n\n"
             "\"Giết ta đi! Bổn tọa thà chết chứ tuyệt không để tà ma nhục mạ!\"\n\n"
             "\"Chết? Ha ha ha... một tuyệt sắc mỹ phụ như ngươi, bổn hầu sao nỡ để ngươi chết dễ dàng như vậy?\" Tiêu Dao Hầu cười lớn, rút ma đao rạch một đường dài từ cổ áo xuống thắt lưng của nàng, để lộ cảnh xuân mê hồn khuynh đảo thế gian."),
            ("第二章 蚀骨销魂魔髓引", "Chương 2: Thực Cốt Tiêu Hồn Ma Tủy Dẫn",
             "Ma dịch màu đỏ thẫm được bôi lên vết thương trước ngực Vân Tố Tâm.\n\n"
             "Đó là 'Thực Cốt Tiêu Hồn Dâm Độc' bí truyền của Ma Môn. Chỉ trong vài nhịp thở, làn da trắng muốt của nữ hiệp đã ửng đỏ như lửa đốt, từng tế bào trên cơ thể gào thét đòi hỏi khoái cảm nhục dục.\n\n"
             "Sự kiêu hãnh của chưởng môn phái chính đạo từng bước sụp đổ. Trước sự chứng kiến của những kẻ tà phái, thân thể nàng bắt đầu vặn vẹo uốn éo theo từng cử chỉ điều khiển ma quái của Tiêu Dao Hầu.")
        ]
    },
    {
        "catalog_id": "shn_3",
        "title": "绿帽第一仙",
        "title_vi": "Lục Mũ Đệ Nhất Tiên",
        "author": "Lục Tiên Ông (绿仙翁)",
        "cover_url": "https://www.8tsw.com/files/article/image/61/61050/61050s.jpg",
        "source_url": "https://www.8tsw.com/61_61050/",
        "genre": "Sắc Hiệp Nặng Đô (21+)",
        "description": "Đỉnh cao thể loại lục sắc (NTR) tu tiên nặng đô! Nhân vật chính tận mắt chứng kiến đạo lữ tiên tử băng thanh ngọc khiết của mình từng bước bị các đại lão, ma tu và ác bá thao túng thể xác, từ kháng cự nhục nhã chuyển dần sang mê đắm khoái lạc nhục dục trước mắt trượng phu.",
        "total_chapters": 95,
        "sample_chapters": [
            ("第一章 秘境归来的变故", "Chương 1: Biến Cố Khi Trở Về Từ Bí Cảnh",
             "Lục Trường Sinh trải qua cửu tử nhất sinh trong Vạn Kiếp Bí Cảnh, ôm theo Chu Tước Thảo quý giá vội vã trở về động phủ.\n\n"
             "Hắn muốn dùng thánh dược này để giải độc cho vị đạo lữ yêu dấu – Nam Cung Tuyết. Nàng là đệ nhất tiên tử của Vạn Tiên Tông, người đã thề non hẹn biển cùng hắn từ thuở hàn vi.\n\n"
             "Nhưng khi bước tới trước cấm chế động phủ, hắn lại phát hiện cấm chế phòng ngự đã bị phá vỡ từ bên trong.\n\n"
             "Bên trong tĩnh thất, từng tràng âm thanh va chạm da thịt dồn dập vang lên cùng tiếng thở dốc êm ái ngập tràn xuân sắc của một nữ tử mà hắn khắc cốt ghi tâm..."),
            ("第二章 隔帘相望泪沾襟", "Chương 2: Ngăn Cách Bức Rèm Lệ Ướt Mi",
             "Qua khe hở của bức rèm ngọc châu buông rủ, Lục Trường Sinh trừng trừng hai mắt, máu dồn lên não như muốn nổ tung.\n\n"
             "Trên chiếc giường ngọc nơi hắn và đạo lữ từng triền miên âu yếm, Nam Cung Tuyết đang quỳ gối dưới thân của Thiếu tông chủ Vạn Tiên Tông. Đôi mắt nàng đẫm lệ nhưng đôi môi lại phát ra những thanh âm rên rỉ đê mê không dứt.\n\n"
             "Đạo tâm của Lục Trường Sinh hoàn toàn tan vỡ trong khoảnh khắc đó. Bi kịch tột cùng cùng khoái lạc méo mó bắt đầu nảy mầm trong bóng tối tu tiên.")
        ]
    },
    {
        "catalog_id": "shn_4",
        "title": "仙子堕落录: 圣女的调教",
        "title_vi": "Tiên Tử Đọa Lạc Lục: Thánh Nữ Điều Giáo",
        "author": "Tà Tình Thiên Tôn (邪情天尊)",
        "cover_url": "https://www.biquge.tv/files/article/image/29/29810/29810s.jpg",
        "source_url": "https://www.biquge.tv/29_29810/",
        "genre": "Sắc Hiệp Nặng Đô (21+)",
        "description": "Cao H thuần nhục, thánh nữ tông môn cao quý lãnh diễm dính dâm độc bị dạy dỗ thành tính nô. Trải qua trăm ngày điều giáo biến thành dâm tiện tính nô chuyên phục vụ thân xác, thân thể chỉ cần chạm nhẹ là run rẩy xuân thủy đầm đìa.",
        "total_chapters": 75,
        "sample_chapters": [
            ("第一章 圣女落难魔窟陷", "Chương 1: Thánh Nữ Sa Cơ Rơi Vào Ma Quật",
             "Thiên Âm Tông thánh nữ – Liễu Như Yên, người được xưng tụng là đóa hoa sen tuyết không vướng bụi trần của tu tiên giới.\n\n"
             "Trong một lần truy sát tà tăng, nàng trúng phải bẫy rập 'Thiên Ma Dâm Tác', toàn thân bị xích lại treo lơ lửng giữa mật thất U Hồn Động.\n\n"
             "Chiếc áo sa trắng mỏng tang bị xé rách từng mảnh, lộ ra cặp đùi ngọc thon dài cùng làn da trắng như tuyết mịn. Tà tăng sải bước tiến tới, trong tay cầm chén 'Vạn Dâm Hóa Cốt Tủy' màu tím sẫm, cười gằn từng tiếng ghê rợn."),
            ("第二章 百日调教春水泛", "Chương 2: Trăm Ngày Điều Giáo Xuân Thủy Tràn",
             "Ba mươi ngày trôi qua trong mật động tăm tối.\n\n"
             "Thánh nữ cao cao tại thượng thuở nào giờ đây hai mắt đờ đẫn mông lung, hai tay ngoan ngoãn bị trói sau lưng. Chỉ cần một ngón tay của tà ma lướt nhẹ qua ngọc phong căng tròn, thân thể nàng liền run rẩy kịch liệt, mật dịch xuân thủy lập tức rỉ ra nơi hoa kính sâu thẳm, cất lên tiếng nài nỉ cầu hoan vô cùng dâm đãng.")
        ]
    },
    {
        "catalog_id": "shn_5",
        "title": "母子艳录: 禁忌之花",
        "title_vi": "Mẫu Tử Diễm Lục: Cấm Kỵ Chi Hoa",
        "author": "Ám Dạ Du Hồn (暗夜游魂)",
        "cover_url": "https://www.8tsw.com/files/article/image/36/36720/36720s.jpg",
        "source_url": "https://www.8tsw.com/36_36720/",
        "genre": "Sắc Hiệp Nặng Đô (21+)",
        "description": "Thể loại cấm kỵ gia đình loạn luân nặng đô. Mối quan hệ mẫu tử thiêng liêng dần bị dục vọng cuồng si nuốt chửng sau những biến cố gia tộc. Những đêm dài triền miên tội lỗi, giữa sự cắn rứt của luân thường đạo lý và khoái lạc thể xác điên cuồng tột bực.",
        "total_chapters": 70,
        "sample_chapters": [
            ("第一章 暴雨之夜的独处", "Chương 1: Đêm Mưa Bão Cô Đơn",
             "Sấm chớp rạch ngang bầu trời đêm mùa hạ, tiếng sấm ầm ầm làm rung chuyển căn biệt thự ven hồ.\n\n"
             "Trần Mẫn – người mẹ kế tuổi ba mươi hai với thân hình đẫy đà quyến rũ bậc nhất – đang một mình ngồi co ro trên ghế sofa vì chứng sợ sấm sét. Chồng nàng đã đi công tác nước ngoài nửa năm không về, trong căn nhà rộng lớn chỉ còn nàng và người con riêng của chồng – Lâm Vỹ.\n\n"
             "Cúp điện, bóng tối bao trùm cả căn nhà. Trong ánh chớp lập lòe, chiếc áo ngủ bằng lụa mỏng màu đỏ rượu vang của Trần Mẫn bị nước mưa hắt ướt đẫm, dính sát vào cơ thể đẫy đà tròn trịa lộ rõ từng đường cong mê người."),
            ("第二章 冲破禁忌的交缠", "Chương 2: Phá Bỏ Cấm Kỵ Điên Cuồng Giao Triền",
             "Hơi thở ấm nóng của Lâm Vỹ phả vào gáy làm Trần Mẫn khẽ rùng mình.\n\n"
             "\"Tiểu Vỹ... không được... con là con trai của mẹ...\"\n\n"
             "\"Mẹ ơi, chúng ta không có quan hệ máu mủ... Con đã khao khát mẹ suốt ba năm nay rồi!\"\n\n"
             "Bàn tay thanh niên mạnh mẽ luồn vào lớp áo lụa, xoa nắn bờ ngực sữa căng mọng tràn đầy sức sống. Bức tường đạo đức cuối cùng sụp đổ trong tiếng rên rỉ ngạt ngào và những cái ôm siết điên dại giữa đêm giông bão.")
        ]
    },
    {
        "catalog_id": "shn_6",
        "title": "天魔淫录: 万艳鼎炉",
        "title_vi": "Thiên Ma Dâm Lục: Vạn Diễm Đỉnh Lô",
        "author": "Thị Huyết Cuồng Ma (嗜血狂魔)",
        "cover_url": "https://www.8tsw.com/files/article/image/51/51290/51290s.jpg",
        "source_url": "https://www.8tsw.com/51_51290/",
        "genre": "Sắc Hiệp Nặng Đô (21+)",
        "description": "Ma môn thiếu chủ tu luyện 'Cửu Chuyển Hóa Âm Bí Quyết', bắt giữ hàng trăm tiên tử, cung chủ, phu nhân của các danh môn chính phái giam cầm trong mật động tịnh thất. Từng đêm thải âm bổ dương bạo liệt, tiếng rên rỉ van xin vang vọng không dứt.",
        "total_chapters": 80,
        "sample_chapters": [
            ("第一章 擒获名门贵妇", "Chương 1: Bắt Giữ Danh Môn Quý Phụ",
             "Trận chiến Vạn Tiên Minh thảm bại, Ma Cung đại thắng.\n\n"
             "Trong địa lao Cửu U Ma Điện, mười hai vị nữ chưởng môn và tông chủ phu nhân của chính đạo đang bị trói bằng xích Khốn Tiên. Tất cả đều bị phong bế chân nguyên, trên người chỉ còn sót lại xiêm y tả tơi mỏng manh.\n\n"
             "Ma quân Tà Vô Nhai khoác hắc bào bước vào, ánh mắt quét qua từng thân hình kiều diễm tuyệt sắc: \"Chào mừng các vị tiên tử đến với Thiên Ma Cung. Từ hôm nay, các ngươi chính là những đỉnh lô thượng phẩm của bổn tọa!\""),
            ("第二章 鼎炉初试九重天", "Chương 2: Đỉnh Lô Khởi Động Chín Tầng Mây",
             "Hỏa độc bốc lên ngùn ngụt khắp đại điện.\n\n"
             "Từng vị phu nhân đài các lần lượt bị lột trần xiêm y đưa lên đàn tế hoan lạc. Tiếng rên xiết vang vọng suốt đêm dài khi công pháp thải âm bổ dương vận chuyển dồn dập, biến chốn địa lao tăm tối thành nơi hoan lạc bạo ngược tột cùng.")
        ]
    }
]

async def import_all():
    await init_db()
    async with AsyncSessionLocal() as session:
        imported_count = 0
        for item in SAC_HIEP_NOVELS_TO_IMPORT:
            # Check existing
            res = await session.execute(
                select(Novel).where(
                    (Novel.title == item["title_vi"]) | (Novel.source_url == item["source_url"])
                )
            )
            existing = res.scalar_one_or_none()
            if existing:
                print(f"[!] Đã có sẵn: {existing.title} (ID: {existing.id})")
                continue

            # Create Novel
            novel = Novel(
                title=item["title_vi"],
                author=item["author"],
                cover_url=item["cover_url"],
                source_url=item["source_url"],
                description=item["description"],
                genre=item["genre"],
                total_chapters=item["total_chapters"],
                last_read_index=1
            )
            session.add(novel)
            await session.flush()

            # Create chapters
            sample_caps = item.get("sample_chapters", [])
            for idx in range(1, item["total_chapters"] + 1):
                if idx <= len(sample_caps):
                    zh_title, vi_title, content_vi = sample_caps[idx - 1]
                    ch = Chapter(
                        novel_id=novel.id,
                        chapter_index=idx,
                        title=zh_title,
                        title_translated=vi_title,
                        source_url=f"{item['source_url']}{idx}.html",
                        raw_content=f"{zh_title}\n\n(Nội dung chương gốc tiếng Trung đang chờ cập nhật)",
                        translated_content=content_vi,
                        translation_status="completed"
                    )
                else:
                    ch = Chapter(
                        novel_id=novel.id,
                        chapter_index=idx,
                        title=f"第{idx}章",
                        title_translated=f"Chương {idx}",
                        source_url=f"{item['source_url']}{idx}.html",
                        raw_content=f"第{idx}章\n\n正文内容待抓取...",
                        translated_content="",
                        translation_status="pending"
                    )
                session.add(ch)
            
            await session.flush()
            # Set last_read_chapter_id to chapter 1
            ch1_res = await session.execute(
                select(Chapter.id).where(Chapter.novel_id == novel.id, Chapter.chapter_index == 1)
            )
            ch1_id = ch1_res.scalar_one_or_none()
            novel.last_read_chapter_id = ch1_id

            await session.commit()
            imported_count += 1
            print(f"[+] Đã thêm thành công: {novel.title} (ID: {novel.id}) - {item['total_chapters']} chương ({len(sample_caps)} chương đã dịch sẵn)")

        print(f"\n===> Hoàn thành! Đã nạp {imported_count} bộ truyện Sắc Hiệp & Nặng Đô mới vào Thư viện!")

if __name__ == "__main__":
    asyncio.run(import_all())
