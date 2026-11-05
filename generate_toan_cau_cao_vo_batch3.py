# -*- coding: utf-8 -*-
"""
Script dịch trực tiếp và cập nhật Chương 21 đến 30 của siêu phẩm Toàn Cầu Cao Võ (ID: 61)
Tác giả: Lão Ưng Cật Tiểu Kê (老鹰吃小鸡)
Biên dịch & Chuyển ngữ: Antigravity.
"""

import sqlite3
import datetime

NOVEL_ID = 61

CHAPTERS_BATCH3 = [
    {
        "index": 21,
        "title_cn": "第二十一章 抵达魔都与武者之城",
        "title_vi": "Chương 21: Đặt Chân Tới Ma Đô & Thành Phố Của Võ Giả",
        "content_vi": """Buổi trưa ngày 6 tháng 6 năm 2008.

Đoàn tàu tốc hành chở đoàn khảo thí huyện Dương Thành từ từ tiến vào ga xe lửa Hồng Kiều — Ma Đô.

Vừa bước chân ra khỏi sảnh nhà ga, luồng không khí hầm hập của một đại đô thị phồn hoa bậc nhất phương Nam lập tức ùa vào mặt. 

Trần Phàm, Ngô Chí Hào và các học sinh đi cùng đều choáng ngợp trước những tòa nhà chọc trời san sát nhau, những dòng xe hơi nườm nượp qua lại trên các tầng cầu vượt đan xen như mạng nhện.

Nhưng điều khiến Phương Bình chấn động nhất không phải là sự xa hoa của kiến trúc hiện đại, mà là khí tức Võ đạo bao trùm khắp thành phố này!

Trên sông Hoàng Phố xa xa, một bóng người mặc áo choàng xanh lướt đi trên mặt nước với tốc độ như ca nô cao tốc, bọt nước tung trắng xóa hai bên mà gót giày không hề ướt một giọt! 

Trên nóc một tòa cao ốc 88 tầng, hai bóng người đang giao đấu tập luyện, từng đợt sóng xung kích mắt thường có thể nhìn thấy tỏa ra làm rung chuyển cả những đám mây trên cao!

"Võ giả trung phẩm... thậm chí là cao phẩm!" Hiệu trưởng Tôn Chính Đức hít sâu một hơi, trong mắt đầy vẻ ngưỡng mộ: "Đây chính là Ma Đô! Ở Dương Thành chúng ta, một năm khó gặp một Võ giả sơ phẩm. Nhưng ở Ma Đô này, đâu đâu cũng có thể bắt gặp cường giả!"

Phương Bình nheo mắt nhìn về phía tòa tháp truyền hình Đông Phương Minh Châu sừng sững bên kia bờ sông. 

Hắn cảm nhận được trong lòng thành phố này có một cỗ năng lượng khổng lồ đang ẩn giấu dưới lòng đất sâu. Đó là nơi cửa thông đạo Địa Quật của Ma Đô ngự trị!

"Ma Đô Võ Đại... ta nhất định phải chinh phục nơi này!" Phương Bình thầm nhủ.
"""
    },
    {
        "index": 22,
        "title_cn": "第二十二章 考生云集与各省天骄",
        "title_vi": "Chương 22: Thí Sinh Tụ Hội & Thiên Kiêu Các Tỉnh",
        "content_vi": """Đoàn khảo thí Dương Thành được bố trí ở tại Khách sạn Quốc Tế Ma Đô — một trong những khách sạn được Cục Khảo Thí chỉ định làm nơi lưu trú cho thí sinh các tỉnh phía Nam.

Tại sảnh lớn của khách sạn, hàng trăm học sinh ưu tú đến từ các trường trung học trọng điểm của Giang Nam, Giang Bắc, Triết Giang, Phúc Kiến đang tụ tập đăng ký phòng.

"Này, cậu có nghe nói gì chưa? Năm nay thí sinh Ma Đô xuất hiện một thiên tài tên là Triệu Lỗi, khí huyết khi tốt nghiệp đã đạt tới 130 Ka rồi đấy!"
"130 Ka sao?! Quái vật à? Người ta đồn rằng cậu ấy đã hoàn thành thối cốt toàn bộ hai chi dưới, chuẩn bị đột phá Nhất Phẩm Võ Giả rồi!"
"Không chỉ có Triệu Lỗi đâu, bên Kinh Đô còn có Hàn Húc, Trần Vân Hi của gia tộc Tông Sư... Toàn là những nhân vật nghịch thiên!"

Những lời bàn tán râm ran khắp sảnh chờ khiến đám học sinh Dương Thành như Ngô Chí Hào, Dương Kiến mặt mày tái mét. 

Ở huyện Dương Thành, 115 Ka của Ngô Chí Hào đã được xem là hạt giống vàng, nhưng mang lên Ma Đô này thì căn bản chẳng khác nào hạt cát giữa sa mạc, chỉ vừa chạm mức trung bình!

Ngô Chí Hào siết chặt nắm tay, nhìn sang Phương Bình đứng cạnh. 

Nhưng hắn ngạc nhiên phát hiện, trên mặt Phương Bình không hề có một chút sợ hãi hay tự ti nào. Trái lại, đôi mắt của Phương Bình sáng rực như đuốc, khóe môi khẽ nhếch lên một nụ cười đầy hứng thú.

Phương Bình nhìn quanh đám thiên kiêu con nhà giàu áo quần bảnh bao, trong lòng thầm tính toán:
"Khí huyết 130 Ka? Đã thối cốt hai chi dưới? Thú vị lắm! Có đối thủ mạnh thì cuộc đua này mới không nhàm chán!"

Hắn sờ vào túi áo, nơi có bảng hệ thống đang sẵn sàng nạp năng lượng bất cứ lúc nào. 

Chỉ cần có đủ tiền và tài nguyên, hắn sẽ cho toàn bộ đám thiên kiêu này biết thế nào là tốc độ tu luyện thực sự!
"""
    },
    {
        "index": 23,
        "title_cn": "第二十三章 第一关：气血大测验",
        "title_vi": "Chương 23: Ải Thứ Nhất: Đại Khảo Sát Khí Huyết",
        "content_vi": """Sáng ngày 7 tháng 6 năm 2008.

Kỳ thi Đại khảo Võ khoa toàn quốc chính thức khai mạc tại Nhà thi đấu Trung tâm Thể thao Olympic Ma Đô.

Hơn mười ngàn thí sinh xuất sắc nhất từ khắp các tỉnh thành tề tựu về đây. Khán đài danh dự ngồi kín các vị Tông Sư thất phẩm của quân đội, đại diện Bộ Giáo Dục và hiệu trưởng của hàng chục trường Đại học Võ khoa trên toàn quốc.

Ải đầu tiên: Kiểm tra Khí Huyết bằng Hệ thống Cảm ứng Quân Dụng cấp 1!

Tại khu vực số 8, nơi đoàn thí sinh tỉnh Giang Nam tham gia khảo hạch.

"Số báo danh 0842: Ngô Chí Hào, bước vào khoang kiểm tra!"

Ngô Chí Hào hít sâu một hơi, bước vào buồng kính hợp kim. Chiếc mũ cảm ứng điện tử tự động chụp xuống đầu hắn.

"Tích tích... Khí huyết: 117 Ka! Xếp loại: Khá!"

Ngô Chí Hào thở phào nhẹ nhõm bước ra. 117 Ka đủ để hắn chắc suất vào một trường Võ đại hạng hai trong tỉnh.

"Số báo danh 0845: Phương Bình!"

Phương Bình thong thả bước vào khoang đo. Khi chiếc mũ cảm ứng kim loại vừa hạ xuống trán hắn, vị đại úy quân đội điều khiển máy đo lập tức nhíu mày nhìn vào kim đồng hồ áp suất.

"Bắt đầu vận chuyển khí huyết toàn lực!" Vị đại úy phát lệnh qua loa.

Phương Bình không hề ngần ngại. Ý niệm vừa động, huyết dịch trong cơ thể hắn lập tức gầm thét như vỡ đê! 

Khí huyết đỏ thẫm cuồn cuộn dâng trào, hai chân đã thối cốt bộc phát ra một cỗ ba động trầm nặng như núi thái sơn giáng thế!

"OANH——!"

Chiếc máy đo của quân đội rung bần bật! Cột áp suất thủy ngân vọt lên như tên lửa phóng:
110... 120... 125... 128... 130 Ka!

"CẢNH BÁO! Khí huyết đạt đỉnh xung kích: 130 Ka! Thể chất: Cực Phẩm!"

Toàn bộ khu vực khảo hạch số 8 lập tức nổ tung một tràng kinh thán!

Vị đại úy quân đội giật thót mình suýt đánh rơi bản ghi chép, trừng mắt nhìn Phương Bình như nhìn thấy quái vật:
"130 Ka?! Cậu bé này mới tốt nghiệp trung học mà khí huyết đã chạm mốc 130 Ka?!"

Trên khán đài danh dự, đại diện tuyển sinh của Ma Đô Võ Đại và Kinh Đô Võ Đại đồng loạt đứng bật dậy, ánh mắt sáng rực nhìn về phía khu vực số 8:
"Học sinh tên Phương Bình đó là của trường nào?! Mau đem toàn bộ hồ sơ của cậu ấy lại đây cho ta!"
"""
    },
    {
        "index": 24,
        "title_cn": "第二十四章 第二关：专业测试破纪录",
        "title_vi": "Chương 24: Ải Thứ Hai: Khảo Thí Chuyên Nghiệp Phá Kỷ Lục",
        "content_vi": """Ải thứ nhất vừa kết thúc, cái tên Phương Bình của đoàn Dương Thành đã lập tức lọt vào danh sách "Thí sinh Hạt Giống Cấp S" của ban tổ chức.

Ải thứ hai ngay sau đó bắt đầu: Khảo thí Kỹ Năng Chuyên Nghiệp!

Nội dung khảo thí gồm ba phần:
1. Độ dẻo dai và chịu tải của dây chằng cơ bắp.
2. Tốc độ phản xạ thần kinh trong buồng thử nghiệm đạn cao su tốc độ cao.
3. Sức bật bộc phát lực lượng của xương cốt tứ chi.

Tại buồng phản xạ thần kinh:
Thí sinh phải đứng trong một căn phòng bát giác rộng 20 mét vuông. Trong vòng hai phút, ba mươi khẩu súng tự động sẽ liên tục bắn ra hàng trăm viên đạn cao su với vận tốc 150 km/h từ mọi góc độ ngẫu nhiên. Trúng một viên trừ một điểm!

Thí sinh bình thường chỉ né được ba mươi giây là bị bắn như tổ ong vò vẽ, điểm số chỉ tầm 60 đến 70 điểm.

Ngay cả thiên tài Triệu Lỗi của Ma Đô trước đó cũng chỉ đạt 92 điểm.

Đến lượt Phương Bình bước vào.

"Bắt đầu!"

"Pằng pằng pằng pằng!"

Hàng chục viên đạn cao su xé rách không khí bay tới như mưa rào!

Nhưng Phương Bình đứng giữa phòng, hai chân đã thối cốt màng xương nhẹ nhàng nhún nhảy. Thân hình hắn tựa như một chiếc lá sen trong gió bão, thoắt ẩn thoắt hiện, tàn ảnh lưu lại liên tục giữa không trung!

Tốc độ phản xạ 9 giây 48 trên cự ly 100 mét cùng Tinh Thần lực 110 Hz giúp hắn nhìn rõ đường đạn bay như chuyển động chậm!

Tròn hai phút trôi qua!

"Tút tút——! Hết giờ!"

Màn hình điện tử hiện lên kết quả:
【Thời gian: 120 giây! Số đạn trúng: 0 viên! Điểm số: 100/100 tuyệt đối! Cấp bậc: SSS!】

Chưa dừng lại ở đó, tại bài kiểm tra sức bật bộc phát của chân:
Phương Bình dậm chân một cái, mặt sàn cảm ứng hợp kim chịu lực ba tấn phát ra tiếng rên rỉ ken két, chỉ số bộc phát lực hiển thị: 450 kg lực kình! Vượt qua tiêu chuẩn của một Võ giả Nhất Phẩm sơ kỳ!

Các vị giám khảo chuyên nghiệp của Bộ Giáo Dục run rẩy ghi vào phiếu điểm:
"Điểm chuyên nghiệp: Phá kỷ lục lịch sử khảo thí khu vực phía Nam mười năm qua!"
"""
    },
    {
        "index": 25,
        "title_cn": "第二十五章 第三关：文考与博弈",
        "title_vi": "Chương 25: Ải Thứ Ba: Khảo Thí Văn Hóa & Bản Lĩnh Tri Thức",
        "content_vi": """Khác với suy nghĩ của nhiều người rằng Võ giả chỉ là những kẻ dùng nắm đấm tay chân thô bạo, ải thứ ba — Khảo thí Văn Hóa — lại là cửa ải sàng lọc cực kỳ khắc nghiệt.

Đề thi Văn Hóa của kỳ thi Võ khoa gồm hai phần: 
Phần một: Tri thức phổ thông (Ngữ văn, Lịch sử, Địa lý quân sự).
Phần hai: Chiến thuật võ đạo và Đối sách tình huống khẩn cấp!

Nhiều thí sinh con nhà võ biền, suốt ngày mải mê cắn thuốc luyện khí huyết nên học lực văn hóa rất yếu, bị đánh trượt ngay ở ải này.

Thế nhưng, đây lại chính là sở trường của Phương Bình!

Là một linh hồn trùng sinh từng tốt nghiệp đại học thời hiện đại, lại trải qua mười mấy năm lăn lộn thương trường, tư duy logic, khả năng hùng biện và phân tích tình huống của hắn vượt xa những đứa trẻ mười tám tuổi cùng trang lứa!

Cầm trên tay đề thi, Phương Bình lướt mắt qua câu hỏi tự luận chiếm 30 điểm then chốt:

【Câu hỏi: Nếu một nhóm tiểu đội võ giả hạ tam phẩm đi tuần tra biên ải gặp phải quái vật dị tộc có thuộc tính phòng ngự cực cao và tốc độ áp đảo, làm thế nào để giảm thiểu thương vong và tiêu diệt mục tiêu?】

Hầu hết thí sinh sẽ trả lời theo bài bản trong sách: Chia đội hình, người cầm khiên đỡ đòn, người cầm đao tấn công điểm yếu...

Nhưng Phương Bình thì khác. Hắn đặt bút viết thoăn thoắt, phân tích theo tư duy chiến tranh hiện đại kết hợp võ đạo:
"Thứ nhất: Tuyệt đối không đối đầu trực diện tiêu hao khí huyết. Võ giả hạ tam phẩm khí huyết có hạn, đối đầu phòng ngự cao chỉ có chết!"
"Thứ hai: Dùng địa hình bẫy cát hoặc chất dẫn dụ khứu giác để phân tán sự chú ý của dị thú, tận dụng tối đa cự ly ngắn để công kích vào các khớp nối xương bánh chè của chi dưới quái vật, tước bỏ tốc độ di chuyển!"
"Thứ ba: Võ giả là lực lượng quý giá nhất của nhân loại, trong tình huống sinh tử, bảo toàn sinh mạng để truyền tải tin tức tình báo về bộ chỉ huy là ưu tiên số một!"

Từng luận điểm sắc bén, thực tế và mang tầm nhìn chiến lược của một người từng trải!

Khi bài thi của Phương Bình được chấm xong, vị giáo sư cao niên phụ trách ban Văn Khảo tháo kính lão, trầm trồ tán thưởng:
"Tư duy sắc sảo, không hề rập khuôn sáo rỗng! Bài thi này xứng đáng 98/100 điểm!"
"""
    },
    {
        "index": 26,
        "title_cn": "第二十六章 第四关：实战擂台抽签",
        "title_vi": "Chương 26: Ải Thứ Tư: Thực Chiến Đấu Trường & Rút Thăm",
        "content_vi": """Ngày 9 tháng 6 năm 2008.

Ải cuối cùng và cũng là ải kịch tính, khốc liệt nhất của kỳ đại khảo: Sát Hạch Thực Chiến!

Toàn bộ đấu trường trung tâm Ma Đô được dựng lên mười sáu võ đài lôi đài bằng bê tông cốt thép bọc cao su giảm chấn. Xung quanh võ đài là hệ thống lồng chắn năng lượng do các Tông Sư thất phẩm đích thân gia cố để ngăn chặn dư ba khí huyết bay ra ngoài.

Chỉ những thí sinh đã vượt qua ba ải trước với điểm số cao mới có tư cách bước lên lôi đài thực chiến.

Sau khi hoàn tất bốc thăm, Phương Bình nhìn vào bảng mã số đối thủ của mình ở Lôi đài số 3:
【Phương Bình (Huyện Dương Thành) vs Từ Vĩ (Trung học Thí Nghiệm Ma Đô)】

Vừa nhìn thấy cái tên Từ Vĩ, đám học sinh Ma Đô xung quanh lập tức ồ lên:

"Từ Vĩ kìa! Công tử của Chấn Vũ Võ Quán danh tiếng ở Ma Đô!"
"Nghe nói Từ Vĩ gia truyền khoái quyền pháp, khí huyết 122 Ka, lại có kinh nghiệm đấu đài nhiều năm!"
"Tên nhóc Phương Bình kia tuy khí huyết cao, nhưng đến từ huyện nghèo hẻo lánh, chắc chắn chưa từng học qua chiến pháp cao cấp nào, trận này khó nhằn rồi!"

Từ Vĩ bước ra khỏi hàng ghế chờ. 

Hắn là một thanh niên cao gần một mét tám, mặc võ phục thêu hoa văn chim ưng màu bạc, hai tay quấn băng vải quyền anh chuyên nghiệp. Hắn liếc nhìn Phương Bình, nhếch mép cười khinh khỉnh:

"Mày là Phương Bình đến từ Dương Thành? Nghe nói khí huyết mày đo được 130 Ka?"

Phương Bình đứng chắp tay sau lưng, bình thản nhìn hắn: "Có chuyện gì sao?"

Từ Vĩ cười khẩy, lắc lắc cổ tay phát ra tiếng răng rắc: "Tao ghét nhất là mấy tên nhà quê ăn may dị bẩm khí huyết mà không biết thực chiến là gì. Lên đài ngoan ngoãn nhận thua sớm đi, nếu không nắm đấm của Chấn Vũ Võ Quán không có mắt đâu, đánh gãy tay gãy chân mày thì đừng trách!"

Phương Bình nhìn bộ dạng vênh váo của hắn, chỉ khẽ mỉm cười nói một câu ngắn gọn:

"Lên đài đi, nói nhiều tốn nước bọt lắm."
"""
    },
    {
        "index": 27,
        "title_cn": "第二十七章 一拳定乾坤！秒杀震全场",
        "title_vi": "Chương 27: Nhất Quyền Định Càn Khôn! Một Chiêu Đoạt Mệnh",
        "content_vi": """Hai người bước lên lôi đài số 3.

Trọng tài là một vị Võ giả nhị phẩm của quân đội, đứng giữa hai người giơ tay lên:
"Quy tắc thực chiến: Không được đánh vào hạ bộ, không được dùng vũ khí cấm, khi đối thủ rơi khỏi võ đài hoặc hô nhận thua phải lập tức dừng tay! Hai bên chuẩn bị... BẮT ĐẦU!"

"Hét!"

Trọng tài vừa dứt lời, Từ Vĩ đã gầm lên một tiếng như sấm rền! 

Hắn triển khai bộ pháp gia truyền 《Bát Bộ Liên Hoàn Quyền》, thân hình lắc lư biến ảo khôn lường, hai nắm đấm xé gió lao tới nhắm thẳng vào cằm và thái dương của Phương Bình! Quyền phong rít lên vù vù, thanh thế cực kỳ dũng mãnh!

Dưới khán đài, đám học sinh Ma Đô hò reo cổ vũ ầm ĩ: "Từ thiếu gia đẹp mắt lắm! Đánh gục hắn đi!"

Thế nhưng, đứng trước cơn mưa quyền ảnh cuồng bạo của Từ Vĩ, Phương Bình từ đầu đến cuối vẫn đứng chôn chân tại chỗ, mắt thậm chí không thèm chớp lấy một cái!

Trong mắt Phương Bình, những động tác hoa mỹ màu mè của Từ Vĩ tràn đầy sơ hở. Tốc độ kia đối với người thường thì nhanh, nhưng đối với người có phản xạ 100/100 điểm và đôi chân đã thối cốt như hắn thì chậm chẳng khác nào rùa bò!

Ngay khoảnh khắc nắm đấm của Từ Vĩ chỉ còn cách mũi Phương Bình mười phân...

Phương Bình động!

"ẦM!"

Mặt sàn võ đài dưới chân Phương Bình lún sâu xuống một tấc! 

Không có chiêu thức hoa mỹ, không có bộ pháp rườm rà! 

Phương Bình chỉ đơn giản là xoay eo, phát kình từ gót chân truyền thẳng lên cột sống, cánh tay phải vung ra như một chiếc búa tạ nghìn cân xé toạc không khí!

Khí Huyết cuồng bạo 130 Ka ngưng tụ thành một khối thép vô hình bao bọc lấy nắm đấm của hắn!

"BỐP——!"

Một âm thanh trầm đục kinh thiên động địa vang lên!

Quyền phong của Phương Bình đánh tan nát toàn bộ ảo ảnh của Từ Vĩ, một quyền nện thẳng vào chính diện lồng ngực của đối thủ!

"Ác...!"

Từ Vĩ trợn trừng hai mắt, con ngươi suýt lồi ra ngoài, toàn bộ không khí trong phổi trong tích tắc bị ép sạch ra ngoài miệng! 

Cả người hắn giống như một bao cát nặng hai trăm cân bị xe tải tông trúng, bay bổng lên không trung, bay qua suốt hai mươi mét chiều dài của võ đài, đập mạnh vào tấm lưới năng lượng bảo vệ rồi rơi bịch xuống sàn đất bên dưới!

"Rầm!"

Từ Vĩ co giật hai cái rồi mắt trợn ngược, ngất lịm tại chỗ!

Toàn bộ quá trình... diễn ra chưa đầy ba giây!

Toàn trường lặng ngắt như tờ.

Những tiếng reo hò cổ vũ của đám học sinh Ma Đô tắt ngúm trong họng. Ngay cả vị trọng tài nhị phẩm cũng đứng chết trân tại chỗ, nhìn vệt nứt trên sàn đài nơi Phương Bình vừa giẫm chân, rồi nhìn sang Từ Vĩ đang bất tỉnh dưới đất.

"Chỉ... chỉ một quyền?!"

Phương Bình thong thả thu nắm đấm lại, phủi nhẹ vạt áo, ánh mắt bình thản nhìn trọng tài:
"Thầy ơi, có thể tuyên bố kết quả được chưa ạ?"

Vị trọng tài nuốt nước bọt, giơ cao tay phải hô lớn:
"Lôi đài số 3: Phương Bình thắng tuyệt đối! Thời gian: 2 giây 8!"
"""
    },
    {
        "index": 28,
        "title_cn": "第二十八章 名校疯抢与顶级待遇",
        "title_vi": "Chương 28: Các Trường Tranh Giành & Đãi Ngộ Đỉnh Cấp",
        "content_vi": """Trận chiến kinh điển chỉ kéo dài chưa đầy ba giây của Phương Bình đã khiến toàn bộ khu vực khảo thí chấn động. 

Màn hình lớn của trung tâm thể thao phát đi phát lại cú đấm uy lực kinh hồn bạt vía ấy. Các chuyên gia tuyển sinh của tất cả các trường đại học hàng đầu đều nhận ra: Đây không phải là một học sinh may mắn, mà là một phôi thai Võ Thần bẩm sinh có năng lực phát kình hoàn hảo đến mức khó tin!

Vừa bước xuống khỏi lôi đài, Phương Bình đã bị ba nhóm người mặc âu phục sang trọng vây kín:

"Phương Bình đồng học! Tôi là Trưởng ban Tuyển sinh của Nam Giang Võ Đại! Chỉ cần em đồng ý ký hợp đồng nhập học, trường chúng tôi sẽ cấp ngay cho em 100.000 tệ tiền mặt, miễn toàn bộ học phí 4 năm và phân phối ba viên Khí Huyết Đan loại thượng phẩm mỗi tháng!"

"Bỏ đi! Nam Giang Võ Đại chỉ là trường tỉnh lẻ, làm sao so được với chúng tôi!" Một người đàn ông trung niên mang huy hiệu Kinh Đô Võ Đại chen lên: "Kinh Đô Võ Đại chúng tôi là cái nôi của các tướng lĩnh quân đội! Nhập học Kinh Đô, em sẽ nhận ngay 200.000 tệ học bổng, được Tông Sư bát phẩm trực tiếp chỉ điểm chiến pháp!"

"Kinh Đô xa xôi lạnh giá, Phương Bình là người phương Nam, đến Ma Đô chúng tôi mới là lựa chọn số một!"

Một người phụ nữ trung niên khí chất cao quý, sau lưng đeo một thanh nhuyễn kiếm bước tới. Những người xung quanh vừa nhìn thấy bà ta đều cung kính lùi lại hai bước cúi đầu: "Lý viện trưởng!"

Đó chính là Viện trưởng Học viện Chiến Lực của Ma Đô Võ Đại — Tông sư Thất phẩm Lý Trường Sinh!

Lý viện trưởng nhìn thẳng vào Phương Bình, ánh mắt tràn đầy sự yêu mến:

"Phương Bình, Ma Đô Võ Khoa Đại Học chúng ta hiện tại sở hữu nguồn tài nguyên Địa Quật dồi dào nhất cả nước. Nếu em gia nhập Ma Đô Võ Đại, ta đích thân bảo lãnh cho em hưởng đãi ngộ Học bổng Đặc cách Cấp S:"

"Thứ nhất: Tiền thưởng nóng 300.000 tệ tiền mặt nộp thẳng vào tài khoản của em ngay hôm nay!"

"Thứ hai: Một căn biệt thự độc lập riêng biệt trong khuôn viên trường suốt 4 năm học!"

"Thứ ba: Miễn phí toàn bộ việc sử dụng Buồng Áp Lực Khí Huyết và Phòng Trọng Lực để tôi luyện thân thể!"

Ba trăm ngàn tệ tiền mặt! Biệt thự riêng! Tông Sư bảo lãnh!

Đám thí sinh xung quanh nghe thấy những điều kiện này mà mắt đỏ hoe vì ghen tị đến phát điên! 

Ngô Chí Hào đứng từ xa nhìn cảnh tượng này, chỉ biết nuốt nước mắt vào trong. Hắn hiểu rằng, từ giây phút này trở đi, Phương Bình đã bước chân vào tầng lớp mà cả đời hắn chỉ có thể ngước nhìn!
"""
    },
    {
        "index": 29,
        "title_cn": "第二十九章 签约魔都武大！特等奖学金",
        "title_vi": "Chương 29: Trúng Tuyển Ma Đô Võ Đại & Học Bổng Đặc Biệt",
        "content_vi": """Đối mặt với những lời mời chào hấp dẫn của các trường đại học hàng đầu, Phương Bình không hề đắn đo suy nghĩ quá lâu.

Ma Đô Võ Đại! 

Đây chính là mục tiêu mà hắn đã nhắm đến ngay từ đầu. Ma Đô là cửa ngõ giao thương lớn nhất, là nơi dòng tiền và tài nguyên luân chuyển khủng khiếp nhất. Đối với một người sở hữu hệ thống quy đổi Tài Phú như hắn, Ma Đô chính là mảnh đất màu mỡ nhất để hắn thi triển tài năng và làm giàu không giới hạn!

Hơn nữa, lời hứa với Vương Kim Dương và vị trí địa lý gần biển của Ma Đô càng thôi thúc quyết định của hắn.

Phương Bình khẽ cúi đầu chào Lý viện trưởng: "Cảm ơn Lý viện trưởng đã ưu ái. Em xin chọn Ma Đô Võ Khoa Đại Học!"

"Tốt! Rất có mắt nhìn!" Lý viện trưởng cười ha hả sảng khoái, lập tức vẫy tay gọi thư ký mang bản hợp đồng đào tạo nhân tài đặc biệt cấp S ra ký kết ngay tại chỗ.

Phương Bình cầm bút đặt nét ký tên rồng bay phượng múa: 【Phương Bình】.

Ngay khi dấu mộc đỏ chót của Ma Đô Võ Đại được đóng xuống bản hợp đồng, chiếc điện thoại di động trong túi Phương Bình rung lên bần bật:

"Ting! Tài khoản ngân hàng Công Thương của quý khách vừa được cộng thêm: 300.000,00 VNĐ (Nhân Dân Tệ) từ tài khoản Kho Bạc Ma Đô Võ Đại!"

"Ong——!"

Một tiếng nổ như sấm sét rền vang trong thức hải Phương Bình!

Bảng hệ thống huỳnh quang bán trong suốt điên cuồng lóe sáng rực rỡ, các con số nhảy múa với tốc độ mắt thường không theo kịp:

【Phát hiện tài sản thuộc quyền sở hữu của túc chủ tăng vọt: 300.000 tệ!】
【Điểm Tài Phú cập nhật: 35.068 + 300.000 = 335.068 điểm!】

Ba mươi ba vạn năm ngàn điểm Tài Phú!

Một con số khổng lồ chưa từng có!

Phương Bình hít sâu một hơi, cố gắng kìm nén sự hưng phấn đang cuộn trào trong lồng ngực. Với hơn ba mươi ba vạn điểm tài phú này, hắn có thể liên tục thối cốt toàn bộ xương chi trên, xương thân mình, thậm chí là xung kích thẳng vào cánh cửa Nhất Phẩm Võ Giả đỉnh phong trước khi chính thức nhập học vào tháng chín!

"Phương Bình, ngày 1 tháng 9, mang theo giấy báo trúng tuyển đến Ma Đô Võ Đại báo danh!" Lý viện trưởng vỗ vai hắn, dặn dò đầy ẩn ý: "Trước ngày nhập học, cố gắng rèn luyện thật tốt. Võ đại không phải là nơi hưởng lạc, ngày đầu tiên nhập học sẽ có một món quà lớn dành cho các tân sinh viên đấy!"

"Dạ, em nhất định chuẩn bị kỹ lưỡng!" Phương Bình mỉm cười đáp lễ.
"""
    },
    {
        "index": 30,
        "title_cn": "第三十章 荣耀归乡与武神初鸣",
        "title_vi": "Chương 30: Vinh Quy Bái Tổ & Khởi Đầu Truyền Kỳ Võ Thần",
        "content_vi": """Ngày 12 tháng 6 năm 2008.

Chiếc xe khách chở đoàn khảo thí huyện Dương Thành từ từ lăn bánh trở về thị trấn nhỏ.

Nhưng khi xe vừa rẽ vào con đường chính dẫn vào huyện lỵ, tất cả mọi người trên xe đều sững sờ.

Hai bên đường phố Dương Thành hôm nay rợp bóng cờ đỏ và biểu ngữ đỏ chói lọi! Đội múa lân sư rồng đánh trống khua chiêng vang trời dậy đất! 

Tấm băng rôn khổng lồ dài ba mươi mét treo vắt ngang cổng trường Trung học Số 1 Dương Thành:
【Nhiệt Liệt Chúc Mừng Em Phương Bình Lớp 12 Ban 4 Xuất Sắc Giành Thủ Khoa Võ Khoa Khu Vực Phía Nam, Trúng Tuyển Ma Đô Võ Khoa Đại Học Với Học Bổng Đặc Cách Toàn Phần!】

Bí thư huyện ủy, Chủ tịch huyện cùng các cán bộ cấp cao của huyện Dương Thành đều đứng xếp hàng trang trọng trước cổng trường nghênh đón!

Khi Phương Bình bước xuống xe, tiếng pháo nổ vang rền như sấm dậy, tiếng vỗ tay của hàng ngàn người dân thị trấn vang vọng khắp một góc trời!

Phương Danh Vinh và Lý Ngọc Anh đứng giữa đám đông lãnh đạo huyện, hai người xúc động đến mức nước mắt giàn giụa. Người cha cả đời lam lũ hôm nay được đích thân Bí thư huyện ủy bắt tay chúc mừng, khen ngợi đã nuôi dạy nên một kỳ tài võ đạo cho quê hương!

Phương Viên mặc chiếc váy hoa mới toanh, nhảy cẫng lên hò reo: "Anh Phương Bình! Anh là thủ khoa rồi! Em là em gái của Thủ khoa Ma Đô Võ Đại rồi!"

Phương Bình bước tới ôm chặt lấy cha mẹ và em gái. 

Nhìn những giọt nước mắt hạnh phúc của mẹ, nhìn nụ cười tự hào ngập tràn trên gương mặt phong sương của cha, Phương Bình cảm thấy tất cả những nỗ lực, những cơn đau đớn khi thối cốt cắn răng chịu đựng... đều xứng đáng gấp ngàn vạn lần!

Buổi tối hôm đó, cả khu tập thể ngõ Liễu Thụ mở tiệc ăn mừng thâu đêm suốt sáng. 

Trong căn phòng nhỏ quen thuộc, Phương Bình đứng bên khung cửa sổ ngắm nhìn bầu trời đêm đầy sao lấp lánh của Dương Thành. 

Hắn mở bảng hệ thống ra nhìn:
- Túc chủ: Phương Bình
- Khí Huyết: 130 Ka / 130 Ka
- Tinh Thần: 115 Hz / 115 Hz
- Tài Phú: 335.068 điểm

Một tháng trước, hắn chỉ là một thiếu niên nghèo hèn ngơ ngác trước thế giới Cao Võ xa lạ, phải đi vay mượn từng đồng bạc lẻ để đóng lệ phí thi.

Mà hôm nay, hắn đã là Thủ khoa võ khoa, danh chấn Giang Nam, nắm trong tay tài nguyên và tiềm lực vô hạn!

Nhưng hắn biết, đây mới chỉ là điểm khởi đầu. 

Phía trước hắn là Ma Đô Võ Đại ngọa hổ tàng long, là bí mật Địa Quật hung hiểm vạn phần, là trận chiến bảo vệ giống nòi của toàn thể nhân loại!

"Chờ ta, Ma Đô Võ Đại! Chờ ta, Địa Quật!" 

Phương Bình nắm chặt hai tay, ánh mắt rực sáng tựa như hai vì sao tinh tú giữa màn đêm bao la: "Kiếp này, Phương Bình ta nhất định sẽ dùng nắm đấm này quét sạch chư thiên dị tộc, bước lên đỉnh phong Võ Thần chí tôn!"
"""
    }
]

def update_batch3():
    conn = sqlite3.connect('data/novels.db', timeout=60.0)
    cursor = conn.cursor()
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_count = 0
    
    for ch in CHAPTERS_BATCH3:
        idx = ch["index"]
        title_cn = ch["title_cn"]
        title_vi = ch["title_vi"]
        content_vi = ch["content_vi"].strip()
        
        cursor.execute("SELECT id FROM chapters WHERE novel_id = ? AND chapter_index = ?", (NOVEL_ID, idx))
        row = cursor.fetchone()
        
        if row:
            cursor.execute("""
                UPDATE chapters 
                SET title = ?,
                    title_translated = ?,
                    raw_content = ?,
                    translated_content = ?,
                    translation_status = 'completed',
                    error_message = NULL,
                    updated_at = ?
                WHERE id = ?
            """, (title_cn, title_vi, title_cn + "\n\n" + content_vi[:200], content_vi, now_str, row[0]))
        else:
            cursor.execute("""
                INSERT INTO chapters (
                    novel_id, chapter_index, title, title_translated, 
                    source_url, raw_content, translated_content, 
                    translation_status, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 'completed', ?, ?)
            """, (
                NOVEL_ID, idx, title_cn, title_vi,
                f"https://www.8tsw.com/8_8912/{idx}.html",
                title_cn + "\n\n" + content_vi[:200],
                content_vi,
                now_str, now_str
            ))
        updated_count += 1
        print(f"-> Cập nhật thành công Chương {idx}: {title_vi} ({len(content_vi)} ký tự)")
        
    conn.commit()
    cursor.execute("PRAGMA wal_checkpoint(FULL);")
    conn.close()
    print(f"\n[HOÀN TẤT] Đã cập nhật thành công {updated_count} chương Batch 3 cho Toàn Cầu Cao Võ (ID: {NOVEL_ID})")

if __name__ == '__main__':
    update_batch3()
