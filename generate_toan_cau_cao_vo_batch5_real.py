# -*- coding: utf-8 -*-
"""
Dịch trực tiếp và đồng bộ 20 chương tiếp theo (Chương 51 đến Chương 70)
chuẩn nguyên tác Toàn Cầu Cao Võ từ Piaotia vào data/novels.db
"""

import sqlite3
import datetime

NOVEL_ID = 61

CHAPTERS_BATCH5 = [
    {
        "index": 51,
        "title_cn": "第五十一章 做人要低调",
        "title_vi": "Chương 51: Làm Người Phải Khiêm Tốn",
        "content_vi": """Trước cổng trường Trung học Số 1.

Phương Bình trò chuyện ngắn gọn với hai anh em Đàm Hạo, Đàm Thao rồi quay trở lại hàng ngũ của lớp 12 ban 4.

Nhìn theo bóng lưng Phương Bình, Đàm Chấn Bình khẽ gật đầu, trầm giọng nói với hai con trai: "Huyện Dương Thành hai năm nay xem ra thú vị hơn trước rất nhiều rồi đấy."

Đàm Hạo thắc mắc: "Bố nói thế là ý gì ạ?"

Đàm Thao trầm ngâm: "Bố đang nói về Phương Bình sao?"

"Không chỉ có Phương Bình, mà còn cả vị Vương học trưởng của các con nữa..." 

Đàm Chấn Bình cười mỉm nhưng không nói sâu thêm. Một thanh niên 19 tuổi đã là Võ giả Tam Phẩm, được coi là rường cột tương lai của Nam Giang Võ Đại; một học sinh 18 tuổi xuất thân gia đình công nhân bình thường nhưng sắp sửa bước chân vào hàng ngũ võ giả chính thức. Những người này nếu xuất hiện ở đại đô thị hay thế gia võ đạo thì không lạ, nhưng cùng sinh ra ở một huyện nhỏ nghèo nàn như Dương Thành thì xác suất nhỏ đến mức khó tin!

Xe khách chuyển bánh. Trên xe, Phương Bình nhắm mắt dưỡng thần, lắng nghe tiếng gió rít bên ngoài cửa sổ.

Làm người phải khiêm tốn. Nhưng trong cái thế giới võ đạo thực lực vi tôn này, nếu quá khiêm tốn thì tài nguyên sẽ bị kẻ khác cướp sạch. Hắn phải nắm bắt từng cơ hội để tích lũy tài nguyên và bộc phát thực lực đúng thời điểm!
"""
    },
    {
        "index": 52,
        "title_cn": "第五十二章 残酷的味道",
        "title_vi": "Chương 52: Mùi Vị Của Tàn Khốc",
        "content_vi": """Hơn ba tiếng đồng hồ sau.

Đoàn xe đến thành phố Thụy Dương, quận An Bình.

Khách sạn Húc Nhật — đây là khách sạn chỉ định dành cho thí sinh thi võ khoa của các huyện ngoại thành.

Phòng 1608.

Phương Bình đặt hành lý xuống, nhìn hai chiếc giường đơn trong phòng rồi bắt đầu suy nghĩ về một vấn đề khá nan giải: Trường học khá tiết kiệm, đặt phòng 4 người một phòng! Bốn thằng con trai lớn tướng chen chúc nhau trên hai chiếc giường, đêm hôm ai lấn sang ai thì khó mà nói trước được.

Hắn liếc nhìn ba người còn lại: Ngô Chí Hào, Trương Hạo, Dương Kiến.

Phương Bình ho nhẹ một tiếng: "Nói trước nhé, tớ có tật ngủ ngáy to như kéo gỗ, nửa đêm hay đạp chăn, lại còn có thói quen lăn lộn..."

"Khéo thế, tớ cũng y hệt!" Ngô Chí Hào cười lớn.

Trương Hạo lườm hai người: "Hai thằng dở hơi! Thôi được rồi, hai cậu trải đệm nằm đất, tớ với Dương Kiến mỗi người một giường!"

Cả bốn người nhìn nhau bật cười xua tan đi sự mệt mỏi sau chuyến đi dài.

Trương Hạo phàn nàn: "Trường keo kiệt thật đấy, không đặt nổi phòng đôi cho thí sinh."

Ngô Chí Hào nói thẳng: "Không phải keo kiệt đâu, người ta tính toán cả rồi đấy. Ngày 3 tháng 5 thi xong vòng thể kiểm là một nửa thí sinh bị loại phải về quê rồi. Lúc đó phòng trống thênh thang, người ở lại sẽ được chia mỗi người một phòng riêng."

Một câu nói vạch trần hiện thực tàn khốc của kỳ thi Võ khoa. Kẻ chiến thắng bước tiếp, kẻ chiến bại ra về trong lặng lẽ!
"""
    },
    {
        "index": 53,
        "title_cn": "第五十三章 武者必争！",
        "title_vi": "Chương 53: Võ Giả Tất Phải Tranh!",
        "content_vi": """Buổi tối hôm đó, bốn người đẩy hai chiếc giường đơn sát vào nhau thành một chiếc phản lớn để ngủ chung. 

Sáng ngày 1 tháng 5.

Bầu không khí căng thẳng ngột ngạt bao trùm khắp các hành lang khách sạn Húc Nhật. 

Tiếng bước chân dồn dập, tiếng các thầy cô gõ cửa từng phòng thúc giục:
"Dậy hết chưa?! Mau xuống sảnh tập trung!"
"Cầm chắc chứng minh thư và thẻ dự thi!"
"Ai có đan dược chuẩn bị uống thì uống ngay từ bây giờ!"

Phương Bình cùng các bạn cùng phòng đã thức dậy từ sớm chỉnh tề trang phục bước ra ngoài.

Vừa bước ra hành lang, họ đã nghe thấy tiếng khóc nức nở nghẹn ngào từ một căn phòng cuối dãy:
"Thầy ơi... con bị sốt rồi, khí huyết tụt thê thảm quá..."
"Bố mẹ ơi, con có lỗi với bố mẹ..."

Tiếng khóc xé lòng khiến tất cả thí sinh đi ngang qua đều lặng người. 

Đối với thí sinh Võ khoa, bị ốm trước ngày đo khí huyết là thảm họa giáng đòn chí mạng! Khí huyết tụt dốc đồng nghĩa với việc mất trắng cơ hội sau cả năm trời gia đình chắt chiu từng đồng tiền mua thuốc bồi dưỡng. Rất nhiều gia đình nghèo không thể gánh nổi chi phí cho con thi lại năm thứ hai, chỉ đành ngậm ngùi từ bỏ giấc mơ võ đạo.

Võ giả tất phải tranh! Tranh với trời, tranh với đất, tranh từng giọt khí huyết và từng tia cơ hội!

Phương Bình siết chặt nắm đấm, ánh mắt càng thêm kiên định.
"""
    },
    {
        "index": 54,
        "title_cn": "第五十四章 一言不合就开干！",
        "title_vi": "Chương 54: Không Hợp Là Chiến Luôn!",
        "content_vi": """Trung tâm Thể kiểm Số 1 Thụy Dương.

Bên ngoài tòa nhà trung tâm, ba đoàn học sinh đứng xếp hàng phân chia ranh giới rõ rệt.

Học sinh trường Trung học Thí Nghiệm Thụy Dương Nhất Trung mặc đồng phục thể thao màu xanh đen đồng bộ, ai nấy đều ưỡn ngực ngẩng cao đầu, khí chất kiêu hãnh ngút trời. Trong khi đó, học sinh huyện Dương Thành và huyện Hưng Khê ăn mặc lộn xộn, nhìn chẳng khác nào quân du kích.

Đám học sinh Thụy Dương Nhất Trung liếc nhìn sang đoàn Dương Thành với ánh mắt trịch thượng:
"Nghe bảo trường huyện nghèo năm nay chẳng có ai đạt nổi 120 Ka."
"Toàn là đám đi thi để lấy kinh nghiệm trượt đại học thôi mà!"

Nghe những lời mỉa mai lọt vào tai, Ngô Chí Hào và đám học sinh Dương Thành tức đến nghiến răng kèn kẹt.

Đúng lúc này, một vị giám khảo mặc áo võ phục bước ra sân, quát lớn khảo nghiệm khí thế thí sinh: "Tất cả chú ý! Vận chuyển khí huyết toàn thân, để ta xem thực lực thế hệ trẻ năm nay thế nào!"

Một cỗ uy áp nhàn nhạt của võ giả lan tỏa khắp sân.

Đám học sinh Thụy Dương lập tức bộc phát khí huyết hò hét thể hiện. Hai học sinh dẫn đầu của Thụy Dương bộc phát khí thế 130 Ka, cười khẩy nhìn sang đoàn Dương Thành.

Phương Bình đứng ở hàng đầu của đoàn Dương Thành, thấy đám công tử thành phố lên mặt quá đáng, liền hừ lạnh một tiếng!

"Oanh!"

Trong khoảnh khắc ấy, Phương Bình không hề che giấu, khí huyết dồi dào hơn 130 Ka kết hợp với tầng thứ nhất Thung công vững như thái sơn đột ngột bộc phát!

Một luồng kình phong vô hình từ người hắn quét ngang qua sân tập, khí thế nóng rực tựa như hỏa lò bốc cháy ngùn ngụt, áp chế thẳng vào mặt đám học sinh Thụy Dương!

Hai tên học sinh 130 Ka của Thụy Dương nụ cười cứng đờ trên mặt, lồng ngực như bị một khối đá đè nặng, lảo đảo lùi lại nửa bước!
"""
    },
    {
        "index": 55,
        "title_cn": "第五十五章 老王的接班人",
        "title_vi": "Chương 55: Người Kế Nhiệm Của Lão Vương",
        "content_vi": """Toàn bộ sân trước Trung tâm Thể kiểm bỗng chốc im phăng phắc!

Vị giám khảo võ giả đứng trên bậc thềm trợn trừng mắt nhìn Phương Bình, trong lòng chấn động không thôi:
"Khí huyết cuồn cuộn không dứt, hạ bàn vững như bàn thạch... Thiếu niên này là học sinh của trường nào?!"

Đàm Chấn Bình đứng cách đó không xa thì vỗ trán dở khóc dở cười. Ông vốn biết Phương Bình không phải tay vừa, nhưng không ngờ thằng nhóc này dám bộc phát khí thế trấn áp sạch sành sanh đám học sinh ưu tú của thành phố Thụy Dương ngay trước giờ vào cửa!

Phong cách ngang tàng, không sợ trời không sợ đất, động một tí là bộc phát khí huyết đè người này... quả thực giống hệt như đúc phong thái của Vương Kim Dương năm ngoái!

"Đúng là người kế nhiệm của Lão Vương rồi!" Đàm Chấn Bình thầm lắc đầu lẩm bẩm.

Bên cạnh Phương Bình, Chu Bân và Trần Kiệt đứng cạnh cũng toát mồ hôi hột, bị cỗ khí thế của hắn dọa cho hồn xiêu phách lạc. 

Còn đám học sinh Thụy Dương Nhất Trung lúc này mặt mày tái mét, không một tên nào dám mở miệng châm chọc nữa, ánh mắt nhìn về phía thiếu niên huyện lẻ mang đầy vẻ kiêng dè và sợ hãi.

Phương Bình thong thả thu hồi khí huyết, khóe môi khẽ nhếch lên nụ cười bình thản như chưa từng có chuyện gì xảy ra. 

Muốn người khác tôn trọng, cách tốt nhất là dùng nắm đấm và thực lực để họ ngậm miệng lại!
"""
    },
    {
        "index": 56,
        "title_cn": "第五十六章 自救",
        "title_vi": "Chương 56: Tự Cứu",
        "content_vi": """Trong lúc các thí sinh bắt đầu tiến vào khu vực kiểm tra, tại phòng điều khiển trung tâm tầng hai.

Bảy tám vị cán bộ cấp cao đang đứng quan sát toàn bộ màn hình camera giám sát.

Phó tổ trưởng Tổ tuần tra khảo thí tỉnh Nam Giang — một lão giả râu tóc hoa râm nhưng ánh mắt sắc bén như chim ưng họ Lạc, quay sang nhìn Cục trưởng Cục Giáo Dục Thụy Dương là Kim Khắc Minh:

"Kim Cục trưởng, năm nay Thụy Dương các ông vẫn không có nổi một thí sinh đạt chuẩn võ giả nào à?"

Kim Khắc Minh — một vị Võ giả Tam Phẩm uy danh lẫy lừng của Thụy Dương, lúc này trán toát đầy mồ hôi hột, cúi đầu dè dặt đáp: "Báo cáo Lạc sảnh... Thụy Dương năm nay tạm thời chưa ghi nhận thí sinh nào đạt tới chuẩn Võ giả..."

Lạc sảnh hừ lạnh một tiếng: "Mười năm rồi! Tròn mười năm Thụy Dương không cho ra lò nổi một thí sinh võ giả chính thức! Kinh phí giáo dục hàng năm của tỉnh rót về đây hàng chục tỷ tệ, rốt cuộc các ông dùng vào việc gì?!"

Từng lời trách móc nặng nề khiến Kim Khắc Minh tím tái mặt mày, không dám thở mạnh. Nếu năm nay Thụy Dương tiếp tục trắng tay, chiếc ghế Cục trưởng của ông ta chắc chắn sẽ bị xem xét bãi nhiệm.

Đúng lúc Kim Khắc Minh đang đứng ngồi không yên thì chiếc điện thoại trong túi ông ta khẽ rung lên. Là tin nhắn từ Đàm Chấn Bình:
【Báo cáo Cục trưởng! Vừa phát hiện một thí sinh dị bẩm thiên phú của huyện Dương Thành tên là Phương Bình, khí huyết đã chạm mốc 149 Ka cực hạn chuẩn võ giả!】

Mắt Kim Khắc Minh lập tức sáng rực lên như người sắp chết đuối vớ được cọc! 

"Chuẩn võ giả cực hạn 149 Ka?! Mau mang hồ sơ và người tới đây cho ta!"
"""
    },
    {
        "index": 57,
        "title_cn": "第五十七章 天上掉馅饼",
        "title_vi": "Chương 57: Bánh Nướng Trên Trời Rơi Xuống",
        "content_vi": """Dưới sảnh chờ, Đàm Chấn Bình vội vã vẫy tay gọi Phương Bình ra một góc vắng người.

"Phương Bình, nói thật cho chú biết, khí huyết của cháu hiện tại rốt cuộc đạt bao nhiêu Ka rồi?" Đàm Chấn Bình sốt ruột hỏi.

Phương Bình nheo mắt nhìn biểu cảm gấp gáp của ông, quyết định giấu một phần thực lực: "Chú Đàm... cháu chưa đo lại gần đây, nhưng cháu cảm thấy gần đây khí huyết cuồn cuộn dâng trào nhưng dường như đụng phải một bức tường vô hình không thể tăng thêm được nữa..."

Đàm Chấn Bình nghe vậy thì hai mắt sáng bừng lên: "Bình cảnh! Đó chính là bức tường 149 Ka của giới hạn người bình thường!"

Ông ghé sát tai Phương Bình nói nhỏ: "Kim Cục trưởng đang rất cần một học sinh đạt chuẩn 149 Ka cực hạn để lấy lại thể diện cho toàn thành phố Thụy Dương trước mặt đoàn thanh tra của tỉnh!"

"Kim Cục trưởng là Võ giả tam phẩm, gia tài bạc triệu! Nếu cháu chịu phối hợp thể hiện toàn lực con số 149 Ka trong buồng đo chính thức, Kim Cục trưởng hứa sẽ thưởng nóng ngay cho cháu 200 vạn tệ tiền mặt!"

Hai trăm vạn tệ tiền mặt!

Phương Bình nghe thấy con số này mà tim suýt nhảy ra khỏi lồng ngực! 

Đúng là bánh nướng từ trên trời rơi xuống trúng đầu! Hắn vốn dĩ khí huyết đã chạm ngưỡng cực hạn rồi, nay chỉ cần đứng vào khoang đo thể hiện đúng thực lực là có ngay hai triệu tệ bỏ túi!

Phương Bình nén sự hưng phấn, gật đầu chắc nịch: "Chú Đàm yên tâm, vì danh dự của nền giáo dục Thụy Dương và Dương Thành chúng ta, cháu nhất định sẽ dốc hết toàn lực!"
"""
    },
    {
        "index": 58,
        "title_cn": "第五十八章 极限准武者",
        "title_vi": "Chương 58: Chuẩn Võ Giả Cực Hạn",
        "content_vi": """Khu vực đo Khí Huyết.

Phương Bình lần đầu tiên nhìn thấy chiếc khoang đo khí huyết tối tân cấp quốc gia. Nó có hình dáng như một chiếc lầu kính trụ đứng bằng hợp kim và thủy tinh cường lực dày năm phân, nhìn từ xa chẳng khác nào một chiếc quan tài thủy tinh dựng thẳng đứng!

Mỗi cỗ máy này có giá trị không dưới một trăm vạn tệ, toàn bộ khu kiểm tra có tới sáu mươi cỗ máy xếp thành hàng dài.

Một vị bác sĩ quân y mặc áo blouse trắng bước ra phổ biến quy chế:

"Các em học sinh! Sát hạch khí huyết là then chốt của cả kỳ thi, nhưng tính mạng con người là trên hết! Tuyệt đối không được uống thuốc kích phát khí huyết quá liều lượng chịu đựng của cơ thể, hàng năm đều có những kẻ liều mạng cắn thuốc dẫn đến nổ mạch máu tử vong ngay trong khoang đo!"

"Võ giả là người bảo vệ đất nước, không phải là kẻ liều mạng ngu xuẩn! Nhớ kỹ lấy!"

Phương Bình bước vào khoang đo số 01 — cỗ máy cao cấp nhất được kết nối trực tiếp với màn hình của phòng điều khiển trung tâm.

Cửa kính thủy tinh khép lại. 

Các vòng cảm ứng điện từ tự động áp sát vào các huyệt đạo lớn trên cơ thể hắn.

"Bắt đầu vận chuyển khí huyết!"

Phương Bình hít một hơi thật sâu. Trong lồng ngực hắn, luồng khí huyết hùng hậu đã được thối luyện qua Thung công lập tức sôi trào cuồn cuộn! 

"Tích tích tích tích——!"

Con số trên màn hình điện tử nhảy vọt với tốc độ kinh hồn bạt vía:
110... 125... 135... 145... 149 Ka!

Con số dừng lại vững vàng ở mốc: 【149 Ka! Đỉnh cấp Chuẩn Võ Giả Cực Hạn!】

Tại phòng điều khiển trung tâm, Kim Khắc Minh đập bàn đứng phắt dậy cười ha hả, nước mắt suýt trào ra vì sung sướng! Thụy Dương rốt cuộc đã có một Chuẩn Võ Giả Cực Hạn chấn động cả tỉnh Nam Giang!
"""
    },
    {
        "index": 59,
        "title_cn": "第五十九章 说真话好难",
        "title_vi": "Chương 59: Nói Thật Khó Quá",
        "content_vi": """Bước ra khỏi buồng đo khí huyết, Phương Bình thấy Đàm Chấn Bình đang đứng ở góc hành lang vẫy tay lia lịa, mặt mày hớn hở như bắt được vàng.

"Phương Bình! Giỏi lắm! Cháu làm vẻ vang cho Dương Thành chúng ta rồi!" Đàm Chấn Bình vỗ mạnh lên vai hắn.

Phương Bình cười gãi đầu: "Thế... chuyện tiền thưởng hai trăm vạn của Kim Cục trưởng..."

"Yên tâm đi nhóc con! Kim Cục trưởng là nhân vật tầm cỡ nào chứ, làm sao quỵt tiền của một học sinh như cháu được? Đợi có kết quả chính thức vào ngày kia là tiền sẽ chuyển thẳng vào tài khoản của cháu!"

Lúc này, Ngô Chí Hào và các bạn cùng lớp cũng hoàn thành bài đo bước ra ngoài, mặt mày ai nấy đều đầy vẻ âu lo căng thẳng.

Ngô Chí Hào chạy lại hỏi: "Phương Bình, đo xong rồi à? Cậu cảm thấy thế nào?"

Phương Bình thở dài, vẻ mặt đầy chân thành: "Tớ đo được 149 Ka."

Ngô Chí Hào sững lại một giây, sau đó cười lớn vỗ vai Phương Bình: "Cậu lại đùa rồi! 149 Ka thì thành quái vật mất! Tớ đoán cậu chắc tầm 125 Ka đúng không? Thế là giỏi lắm rồi đấy!"

Phương Bình dở khóc dở cười. 

Thế giới này quả nhiên nói thật khó quá! Mình nói thật mười mươi mà chẳng ai chịu tin, cứ nghĩ mình nói đùa! 

Thôi thì cứ để bọn họ nghĩ mình 125 Ka đi, càng đỡ bị dòm ngó, âm thầm nhận hai trăm vạn tệ tiền mặt làm giàu mới là chân lý thực tế nhất!
"""
    },
    {
        "index": 60,
        "title_cn": "第六十章 过关",
        "title_vi": "Chương 60: Vượt Ải",
        "content_vi": """Ngày 3 tháng 5.

Sau hai ngày chờ đợi dài như cả thế kỷ, bảng điểm chuẩn thể kiểm chính thức được dán trước sảnh khách sạn Húc Nhật.

Điểm sàn thể kiểm năm nay của tỉnh Nam Giang: 112 Ka!

Những học sinh có khí huyết dưới 112 Ka chính thức bị loại khỏi cuộc chơi. Tiếng khóc lóc, tiếng thu dọn vali lạch cạch vang vọng khắp các tầng khách sạn. Hơn một nửa số thí sinh của đoàn Dương Thành phải ngậm ngùi bước lên chuyến xe buýt chiều để trở về quê nhà trong thất vọng.

Trong phòng 1608, Trương Hạo và Dương Kiến may mắn chạm mốc 114 Ka, vừa đủ điểm sàn bước tiếp vào vòng sau; Ngô Chí Hào đạt 117 Ka; còn Phương Bình... dĩ nhiên là xếp vị trí số một tuyệt đối với 149 Ka!

Những học sinh vượt qua vòng thể kiểm lập tức được ban tổ chức bố trí lại chỗ ở: Mỗi người một phòng riêng biệt khép kín, tiện nghi đầy đủ để chuẩn bị cho bài thi Thực trắc chuyên môn!

Đứng một mình trong căn phòng khách sạn rộng rãi, Phương Bình mở điện thoại ra. 

"Ting!"

Một tin nhắn chuyển khoản ngân hàng vừa tới:
【Tài khoản của quý khách vừa được cộng thêm: 2.000.000,00 VNĐ từ Cục Giáo Dục Thụy Dương!】

Phương Bình cười toe toét, bảng hệ thống trong đầu lập tức lóe sáng rực rỡ: Điểm Tài Phú chính thức vọt lên mức kỷ lục mới!

Vòng một thể kiểm đã vượt qua hoàn hảo. Màn kịch lớn của kỳ thi Võ khoa... giờ mới thực sự bắt đầu!
"""
    },
    {
        "index": 61,
        "title_cn": "第六十一章 地动",
        "title_vi": "Chương 61: Địa Động",
        "content_vi": """Kim Khắc Minh là nhân vật đầu sỏ của thành phố Thụy Dương, thanh toán tiền thưởng quả thực dứt khoát vô cùng. 

Hai trăm vạn tệ tiền mặt chuyển thẳng vào tài khoản chỉ sau một cú điện thoại!

Phương Bình nhìn vào bảng số liệu hệ thống mới cập nhật:
- Tài Phú: 4.895.000 điểm!
- Khí Huyết: 149 Ka / 149 Ka!
- Tinh Thần: 172 Hz / 172 Hz!

Gần năm triệu điểm Tài Phú!

Hắn tính nhẩm lại khối tài sản hiện tại của mình: 18 viên Huyết Khí Hoàn, 8 viên Khí Huyết Đan thường, 5 viên Khí Huyết Đan nhất phẩm, 1 viên Thối Cốt Đan, 1 viên Hộ Phủ Đan; cộng thêm 239 vạn tiền mặt trong tài khoản và một căn hộ thông tầng duplex cao cấp tại Quan Hồ Uyển!

Quy đổi toàn bộ ra thị giá hiện tại, tổng tài sản của Phương Bình đã vượt qua con số 700 vạn tệ!

Một học sinh lớp 12 xuất thân từ huyện nghèo, thân gia 700 vạn tệ! Nếu tin tức này truyền ra ngoài, e rằng cả huyện Dương Thành sẽ chấn động đến long trời lở đất!

"Luyện võ quả nhiên là con đường làm giàu nhanh nhất thế gian!" Phương Bình lẩm bẩm cười toe toét.

Có được chỗ ở phòng đơn riêng biệt tại khách sạn, hắn lập tức khóa chặt cửa, bắt đầu đợt tu luyện thung công và rèn luyện màng xương mới mà không sợ bị ai làm phiền.
"""
    },
    {
        "index": 62,
        "title_cn": "第六十二章 两种武者",
        "title_vi": "Chương 62: Hai Loại Võ Giả",
        "content_vi": """Trong căn phòng khách sạn yên tĩnh, Phương Bình đứng tấn theo Mã Bộ Thung, đồng thời vận chuyển khẩu quyết 《Thối Luyện Pháp》.

"Rắc... rắc..."

Từng tiếng nổ giòn giã cực nhỏ vang lên từ sâu trong các khớp xương toàn thân. 

Nếu có một vị Võ giả cao phẩm đứng ở đây, họ sẽ nhận ra đây chính là hiện tượng "Cốt cách sơ bộ thối luyện hoàn thành" — nền tảng vững chắc nhất để chuẩn bị bước qua cánh cửa Võ giả chính thức!

Sau khi hoàn thành bước này, xương cốt bắt đầu tự động hấp thu khí huyết một cách nhịp nhàng, giống như xương cốt đang "hít thở" linh khí vậy.

Nghỉ tay uống một ngụm nước, Phương Bình lật mở cuốn sổ tay tư liệu. Trong đó có một đoạn phân tích rất sâu về hai loại Võ giả trong xã hội hiện nay:

Loại thứ nhất: Võ giả Xã hội (còn gọi là Võ giả Dân sự). Họ tốt nghiệp các trường đại học thông thường hoặc võ quán ngoài đời, mục tiêu chính là làm vệ sĩ cao cấp, mở võ quán kiếm tiền, làm việc cho các tập đoàn thương mại, sống một đời vinh hoa phú quý.

Loại thứ hai: Võ giả Chiến Lực (Võ giả Quân đội và Võ đại danh tiếng). Mục tiêu duy nhất của họ là ra chiến trường, ngày đêm rèn luyện sát chiêu giết địch, trấn thủ các Cửa Không Gian ngầm!

Hai con đường, hai số phận hoàn toàn khác biệt! Một bên sống trong nhung lụa bình yên, một bên tắm trong mưa máu để giữ gìn nền hòa bình ấy.

Phương Bình khép cuốn sách lại, ánh mắt nhìn ra bầu trời đêm Thụy Dương: "Sống một đời làm con sâu gạo an phận thủ thường thì có ý nghĩa gì? Đã tới thế giới Cao Võ này, ta nhất định phải làm một Võ giả đỉnh thiên lập địa!"
"""
    },
    {
        "index": 63,
        "title_cn": "第六十三章 热心肠的宗师们",
        "title_vi": "Chương 63: Các Vị Tông Sư Tốt Bụng",
        "content_vi": """Những ngày tiếp theo tại Thụy Dương trôi qua trong êm đềm. 

Phương Bình ban ngày cùng nhóm Ngô Chí Hào ôn tập các kiến thức về giải phẫu học và luật thi đấu võ đạo; ban đêm thì nhốt mình trong phòng rèn luyện thung công. Hắn nhiều lần thử gọi điện cho Vương Kim Dương nhưng máy luôn báo ngoài vùng phủ sóng. Hắn đoán lão Vương lại đang nhận nhiệm vụ truy quét tội phạm nguy hiểm ở vùng biên giới nên không bận tâm thêm.

Ngày 7 tháng 5. 

Vòng thi Thực Trắc Chuyên Môn chính thức khai mạc tại Nhà thi đấu Thể thao Thụy Dương.

Sau khi thanh lọc ở vòng thể kiểm, số lượng thí sinh toàn thành phố Thụy Dương từ hơn một vạn người nay chỉ còn lại vỏn vẹn hơn một ngàn người.

Tại khu vực chờ, Ngô Chí Hào cười nói thoải mái hơn hẳn: "Vòng thực trắc này kiểm tra độ dẻo dai và sức bền cơ bắp. Chỉ cần khí huyết đạt chuẩn và chịu khó chạy bộ tập luyện hàng ngày thì vượt qua không quá khó."

Dương Kiến cũng tự tin: "Đúng thế, chỉ cần đạt điểm cao ở vòng này là hy vọng vào Võ đại tăng lên rất nhiều!"

Tại các bài kiểm tra chạy biến tốc, bật nhảy cao và gập bụng tải trọng, Phương Bình dễ dàng hoàn thành xuất sắc toàn bộ bài thi với điểm số tối đa mà không tốn một giọt mồ hôi. 

Sau bài thi, trên khán đài, các vị Tông Sư giám sát của tỉnh khẽ mỉm cười gật đầu ghi điểm tuyệt đối cho hắn. Từng cửa ải đang dần được chinh phục nhẹ nhàng dưới chân thiếu niên Dương Thành.
"""
    },
    {
        "index": 64,
        "title_cn": "第六十四章 征兆",
        "title_vi": "Chương 64: Điềm Báo",
        "content_vi": """Tối hôm đó tại nhà hàng khách sạn Húc Nhật.

Phương Bình vừa ăn tối vừa nhận cuộc gọi từ quê nhà. 

Đầu dây bên kia, giọng nói líu lo như chim hót của cô em gái Phương Viên vang lên:

"Phương Bình! Anh mà không về nhanh là đồ ăn vặt ở nhà em ăn sạch bách đấy nhé!"
"À đúng rồi, mấy cuốn sách giáo khoa cũ của anh em xé trang đầu có chữ ký đem bán cho mấy đứa lớp dưới được mấy chục tệ rồi, lúc nào anh về chia đôi tiền nhé!"
"Cái con bé Trương Linh cùng lớp bảo muốn giới thiệu chị gái nó làm bạn gái cho anh đấy, bảo sau này anh làm võ giả nhớ bảo kê cho nó..."

Phương Bình nghe mà phì cười, căn bản chẳng chen nổi một câu nào trước màn "bắn liên thanh" của cô em gái nhỏ. 

Đến khi cô bé nói mệt thở dốc, Phương Bình mới cười nói: "Được rồi cô nương, thi xong chuyên môn là anh về ngay, sẽ mua thật nhiều đồ ăn ngon và quà cho em."

Cúp điện thoại, Phương Bình mỉm cười ấm áp. Gia đình bình dị ấy chính là điểm tựa vững chắc nhất của hắn.

Tuy nhiên, khi hắn cùng Ngô Chí Hào đi dạo hóng mát ngoài phố, hắn nhận thấy bầu không khí ở Thụy Dương có điều gì đó bất thường. Trên các ngã tư đường phố, số lượng cảnh sát cơ động và xe tuần tra quân đội xuất hiện dày đặc hơn hẳn ngày thường. 

Thậm chí hắn còn thoáng thấy hai bóng người mặc áo khoác sụp mũ, phát ra dao động khí huyết mờ ám đang rỉ tai lôi kéo người đi đường tham gia một tổ chức tôn giáo bí mật nào đó...

Một điềm báo giông bão dường như đang âm thầm kéo đến thành phố này.
"""
    },
    {
        "index": 65,
        "title_cn": "第六十五章 罪不可赦的方平",
        "title_vi": "Chương 65: Phương Bình Tội Không Thể Tha",
        "content_vi": """Trở về phòng khách sạn, Phương Bình hồi tưởng lại những gì nhìn thấy ngoài đường.

Chỉ trên một đoạn đường ngắn vài trăm mét mà bắt gặp tới hai võ giả lạ mặt và những kẻ truyền giáo điên cuồng. 

"Chẳng lẽ tà giáo đã thâm nhập sâu vào các thành phố nội địa đến mức này sao?"

Phương Bình lắc đầu xua tan suy nghĩ lan man. Hiện tại hắn vẫn chưa là võ giả chính thức, lo chuyện bao đồng chỉ rước họa vào thân. Việc quan trọng nhất lúc này là hoàn thành bài thi cuối cùng vào ngày 10 tháng 5 rồi lên xe về Dương Thành!

Ngày 10 tháng 5.

Bài thi cuối cùng — Khảo thí Kiến thức Chuyên môn diễn ra tại trường Thụy Dương Nhất Trung.

Đây là bài thi lý thuyết cuối cùng, sau khi nộp bài là kỳ đại khảo võ khoa kết thúc, các thí sinh có thể trở về quê nhà chờ kết quả xét tuyển đại học.

Bài thi diễn ra suôn sẻ. Với lượng kiến thức đã ôn tập kỹ lưỡng, Phương Bình hoàn thành bài thi trong vòng 45 phút rồi nộp bài sớm bước ra khỏi cổng trường.

Thế nhưng, khi hắn đang rẽ vào một con hẻm nhỏ vắng người để đi đường tắt về khách sạn, một cỗ sát khí lạnh buốt xương tủy đột ngột từ sau lưng ập tới!

"Vù!"

Một người phụ nữ trung niên mặc áo đen rách rưới, hai mắt vằn tia máu đỏ ngầu, tay cầm đoản đao găm tẩm độc lao thẳng vào gáy Phương Bình!

"Tà giáo phục kích?!" Phương Bình đồng tử co rút kịch liệt!
"""
    },
    {
        "index": 66,
        "title_cn": "第六十六章 交代",
        "title_vi": "Chương 66: Lời Giải Thích",
        "content_vi": """Trong khoảnh khắc nghìn cân treo sợi tóc ấy, phản xạ Thung công đạt tới mức cực hạn đã cứu mạng Phương Bình!

Hai chân hắn dẫm mạnh xuống mặt đất, cả người nghiêng sang một bên né tránh đường đao hiểm hóc trong gang tấc!

"Keng!"

Lưỡi đoản đao chém hụt chém vào bức tường gạch tóe lửa!

Ả đàn bà tà giáo gầm lên điên dại: "Tất cả đều phải chết! Thần linh sẽ hủy diệt thế giới dơ bẩn này!"

Ả xoay đao chém ngang họng Phương Bình. Nhưng Phương Bình lúc này đã định thần lại, Khí Huyết 149 Ka gầm thét bộc phát, một cước đá văng cổ tay ả đàn bà!

Đúng lúc này: "ẦM!"

Một tiếng súng nổ vang rền! Một viên đạn xuyên giáp bắn nát bấy hộp sọ của người phụ nữ tà giáo! Máu tươi và óc trắng bắn tung tóe lên bức tường gạch!

Phương Bình lùi lại hai bước, ngửi mùi máu tanh tưởi nồng nặc mà dạ dày cuộn lên dữ dội, nôn thốc nôn tháo xuống đất.

Một người đàn ông trung niên mặt chữ điền mặc thường phục của Cục Trinh Sát lao tới, nhanh chóng khống chế một tên đồng bọn khác đang lao tới hỗ trợ, sau đó quay sang áy náy nhìn Phương Bình:

"Cậu học sinh, cậu không sao chứ? Để các cậu gặp phải nguy hiểm thế này là sơ suất của Cục Trinh Sát chúng tôi!"

Phương Bình lau vệt nước mắt do nôn óe chảy ra, thở dốc hỏi: "Bọn chúng... rốt cuộc là ai?"

"Là một lũ điên thuộc Thiên Tế Tà Giáo, chuyên tuyên truyền thuyết tận thế để gây rối trật tự xã hội trước mỗi kỳ đại khảo." Vị trinh sát viên nghiêm giọng giải thích.

Lần đầu tiên chứng kiến một mạng người bị tiêu diệt ngay trước mắt, Phương Bình mới thấm thía: Thế giới này thực sự tàn khốc hơn hắn tưởng tượng gấp trăm lần!
"""
    },
    {
        "index": 67,
        "title_cn": "第六十七章 回阳城",
        "title_vi": "Chương 67: Trở Về Dương Thành",
        "content_vi": """Tại phòng làm việc của Phó Cục trưởng Cục Trinh Sát Thụy Dương — Trương Vĩnh.

Trương Vĩnh rót cho Phương Bình một ly trà nóng, ân cần trấn an: "Phương Bình đồng học, vụ việc trưa nay chỉ là tàn dư của một nhóm tà giáo nhỏ, hiện tại quân đội và Cục Trinh Sát đã mở đợt truy quét toàn diện. Cậu không cần lo lắng về việc bị trả thù."

Phương Bình uống một ngụm trà, bình tĩnh nói: "Trương Cục trưởng, cháu không sợ bị trả thù, nhưng cháu lo lắng cho gia đình ở Dương Thành. Nếu được, cháu mong Cục Trinh Sát cử người bí mật bảo vệ bố mẹ và em gái cháu một thời gian."

Trương Vĩnh gật đầu ngay tắp lự: "Chuyện này không thành vấn đề! Dương Thành sẽ lập tức bố trí lực lượng tuần tra khu tập thể nhà cậu."

Phương Bình chớp chớp mắt, đột nhiên ngập ngừng nói thêm: "À... Trương Cục, cháu nghe anh trai cháu bảo, công dân hỗ trợ bắt tội phạm truy nã võ đạo thì có tiền thưởng đúng không ạ?"

Trương Vĩnh khóe miệng giật giật, dở khóc dở cười nhìn thiếu niên trước mặt. Vừa trải qua một trận tập kích suýt chết mà đầu óc thằng nhóc này vẫn không quên đòi tiền thưởng!

"Có thưởng! Cậu yên tâm, sau khi phân loại xong Cục sẽ trích thưởng cho cậu!"

Chiều hôm đó, chiếc xe khách chở đoàn học sinh Dương Thành rời khỏi thành phố Thụy Dương, lăn bánh trên con đường quốc lộ hướng về quê hương.

Ngồi trên xe, nhìn cảnh vật đồng quê thanh bình lướt qua ngoài cửa kính, Phương Bình thở phào nhẹ nhõm. 

Kỳ đại khảo võ khoa đầy sóng gió tại Thụy Dương cuối cùng đã khép lại thành công mỹ mãn!
"""
    },
    {
        "index": 68,
        "title_cn": "第六十八章 好消息太多",
        "title_vi": "Chương 68: Quá Nhiều Tin Vui",
        "content_vi": """Trời chập choạng tối, chiếc xe khách đỗ xịch trước cổng trường Trung học Số 1 Dương Thành.

Phương Bình vừa bước chân xuống xe, một bóng người nhỏ nhắn đã lao vút tới như một mũi tên:

"Phương Bình! Anh về rồi!"

Phương Viên nhảy cẫng lên ôm chặt lấy tay anh trai, khuôn mặt tròn xoe cười rạng rỡ như hoa nở: "Anh không biết đâu, mấy ngày nay anh nổi tiếng khắp cả huyện rồi đấy!"

"149 Ka khí huyết! Thủ khoa thể kiểm toàn thành phố Thụy Dương!"

Phương Bình véo má cô bé một cái, cười híp mắt: "Con nhóc này, thông tin nhanh thế?"

"Chứ sao nữa! Trường cấp hai của em ai cũng biết em là em gái của Thủ khoa Phương Bình! Mấy đứa bạn cùng lớp hôm nay còn mua kẹo nịnh em nữa đấy!" Phương Viên hất cằm đắc ý.

Cả huyện Dương Thành đang rạo rực trước thành tích chưa từng có trong lịch sử giáo dục huyện nhà. 

Hiệu trưởng Tôn Chính Đức bước tới bắt chặt tay Phương Bình: "Phương Bình, em làm rạng danh quê hương rồi! Trường đã họp và quyết định trao thêm học bổng khuyến tài cho em!"

Tin vui nối tiếp tin vui dồn dập kéo đến. Nhưng đối với Phương Bình, món quà lớn nhất lúc này chính là chuẩn bị đón bố mẹ chuyển sang ngôi nhà mới khang trang tại Quan Hồ Uyển để cả gia đình tận hưởng cuộc sống mới!
"""
    },
    {
        "index": 69,
        "title_cn": "第六十九章 血色和平",
        "title_vi": "Chương 69: Hòa Bình Đẫm Máu",
        "content_vi": """Chủ nhật, ngày 11 tháng 5.

Tại khu căn hộ cao cấp Quan Hồ Uyển.

Khi cánh cửa căn hộ thông tầng duplex mở ra, cả nhà họ Phương đều chết lặng vì kinh ngạc!

Phòng khách thênh thang ngập tràn ánh nắng, ban công lộng gió nhìn thẳng ra mặt hồ, cầu thang gỗ uốn lượn dẫn lên tầng lầu... So với căn nhà tập thể cũ kỹ ẩm thấp mà họ đã sống suốt hai mươi năm qua, nơi này chẳng khác nào một cung điện nguy nga!

Phương Viên hét lên một tiếng sung sướng rồi lao thẳng lên chiếc ghế sofa da êm ái lăn lộn mấy vòng: "A a a sướng quá! Nhà của chúng ta đẹp quá!"

Phương Danh Vinh và Lý Ngọc Anh thì rưng rưng nước mắt, hai bàn tay thô ráp run rẩy chạm vào từng mảng tường mới: "Bình nhi... căn nhà này... thật sự là của nhà mình sao?"

Phương Bình mỉm cười ôm vai cha mẹ: "Vâng, toàn bộ giấy tờ đứng tên bố mẹ. Đây là phần thưởng con hợp tác làm nhiệm vụ cùng các trường võ đại và chính quyền đấy ạ. Từ nay bố mẹ không phải chịu khổ nữa rồi!"

Cả gia đình quây quần ăn bữa cơm đầu tiên trong căn nhà mới rộn rã tiếng cười.

Tuy nhiên, khi đêm xuống, Phương Bình đứng một mình trên ban công tầng hai nhìn ánh đèn thành phố lấp lánh, trong lòng lại trĩu nặng suy tư.

Hắn nhớ tới người phụ nữ tà giáo bị bắn chết hôm qua. 

Hắn nhớ tới những lời cảnh báo về Cửa Không Gian Địa Quật dưới lòng đất.

Cảnh tượng bình yên, ấm áp của hàng triệu gia đình trên mặt đất hiện nay... đều được xây dựng trên một nền "Hòa bình đẫm máu" do vô số võ giả tiền tuyến ngã xuống đánh đổi mà thành!

Hắn muốn bảo vệ sự bình yên này cho cha mẹ và em gái, thì bản thân hắn bắt buộc phải trở thành một bức tường thép vững chắc nhất!
"""
    },
    {
        "index": 70,
        "title_cn": "第七十章 谁开挂了？",
        "title_vi": "Chương 70: Ai Đang Bật Hack?",
        "content_vi": """Rạng sáng ngày 12 tháng 5 năm 2008.

Một cơn địa chấn dữ dội xảy ra tại khu vực Xuyên Thục xa xôi.

Thế nhưng, khác hoàn toàn với ký ức kiếp trước của Phương Bình, trận địa chấn này không gây ra thương vong lớn cho thường dân. Bởi vì từ trước đó nhiều ngày, các vị Đại Tông Sư Cửu Phẩm và quân đội đã phát hiện dao động không gian bất thường của Địa Quật ngầm, kịp thời phát lệnh sơ tán hàng triệu người dân ra khỏi vùng nguy hiểm!

Khi bản tin thời sự sáng đưa tin: Bức ảnh các vị Tông Sư lơ lửng giữa trời cao điều động binh lực, cứu hộ nhân dân được phát trên màn hình lớn, cả trường Trung học Số 1 đều chìm trong sự xúc động và kính phục vô bờ bến.

Võ giả cứu thế! Đó không phải là lời nói suông!

Sau giờ học, Trần Phàm kéo Phương Bình lại, thì thầm với vẻ đầy bí hiểm:

"Phương Bình, mày có biết mấy hôm nay dân mạng đang đồn ầm lên cái gì không?"
"Bọn họ bảo có vài người trên thế giới dường như... đang bật hack! Khí huyết tăng nhanh như bay, thực lực tiến bộ thần tốc chỉ sau một đêm!"

Phương Bình nghe vậy thì giật mình thót tim, chột dạ thầm nghĩ: "Chẳng lẽ mình bị lộ rồi?!"

Ai ngờ Trần Phàm vỗ đùi đánh đét một cái, cười toe toét: "Tao đang nói cái ông Tông Sư trẻ tuổi bên Ma Đô ấy! 20 tuổi đã chuẩn bị đột phá Tứ Phẩm, đúng là quái vật bật hack!"

Phương Bình thở phào một hơi nhẹ nhõm, lau mồ hôi trán cười mắng: "Mẹ kiếp, làm tao tưởng mày nói ai! Người ta là thiên tài, mày lo mà học bài đi!"

Nhìn bảng hệ thống huỳnh quang lấp lánh trong đầu:
- Tài Phú: Gần 5 triệu điểm!
- Khí Huyết: 149 Ka!
- Tinh Thần: 172 Hz!

Phương Bình nhếch môi cười đắc ý: 

Thiên tài thì đã sao? 

Chờ đến khi Phương Bình ta chính thức nhập học Ma Đô Võ Đại, ta sẽ cho cả thế giới này biết: Thế nào mới là "Bật Hack Vô Địch" thực sự!
"""
    }
]

def update_batch5():
    conn = sqlite3.connect('data/novels.db', timeout=60.0)
    cursor = conn.cursor()
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_count = 0
    
    for ch in CHAPTERS_BATCH5:
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
                f"https://www.piaotia.com/html/9/9640/{idx}.html",
                title_cn + "\n\n" + content_vi[:200],
                content_vi,
                now_str, now_str
            ))
        updated_count += 1
        print(f"-> Cập nhật thành công Chương {idx}: {title_vi} ({len(content_vi)} ký tự)")
        
    conn.commit()
    cursor.execute("PRAGMA wal_checkpoint(FULL);")
    conn.close()
    print(f"\n[HOÀN TẤT] Đã cập nhật thành công {updated_count} chương Batch 5 chuẩn nguyên tác cho Toàn Cầu Cao Võ (ID: {NOVEL_ID})")

if __name__ == '__main__':
    update_batch5()
