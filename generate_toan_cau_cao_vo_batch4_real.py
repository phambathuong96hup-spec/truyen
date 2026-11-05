# -*- coding: utf-8 -*-
"""
Dịch trực tiếp và đồng bộ 20 chương tiếp theo (Chương 31 đến Chương 50)
chuẩn nguyên tác Toàn Cầu Cao Võ từ Piaotia vào data/novels.db
"""

import sqlite3
import datetime

NOVEL_ID = 61

CHAPTERS_BATCH4 = [
    {
        "index": 31,
        "title_cn": "第三十一章 求援",
        "title_vi": "Chương 31: Cầu Viện",
        "content_vi": """Vài phút sau, Phương Bình từ túp lều phòng 201 bước ra ngoài.

Đóng chặt cửa phòng lại, trên tay Phương Bình còn xách theo một chiếc túi nilon màu đen.

Hắn không lấy số tiền mặt vứt trên bàn, cũng không động vào thanh quân thứ quân dụng, mà chỉ cất sáu lọ đan dược vào người. Những viên đan dược này đắt đỏ vô cùng, để lại nơi xập xệ này nếu bị tên trộm nào cuỗm mất thì Phương Bình có khóc cũng chẳng có chỗ mà khóc.

Còn về phần Hoàng Bân — tên tội phạm võ đạo nhị phẩm đang bị thương nặng, Phương Bình đã nhét giẻ bịt chặt mồm hắn lại rồi đá tọt vào sâu trong gầm giường.

Bước ra khỏi khu tập thể cũ, Phương Bình khẽ nhíu mày.

"Đan dược đã cầm trên tay, vậy mà bảng hệ thống vẫn không tăng điểm Tài Phú.

Là do điều kiện chưa đạt, hay là đồ vật hiện vật không được tính trực tiếp vào Tài Phú, chỉ tính tiền mặt hợp pháp?"

"Chắc không phải vấn đề do tiền mặt, bởi vì lúc nãy số tiền mặt kia mình cũng từng cầm qua mà hệ thống không nhảy số."

Phương Bình suy nghĩ một lát, liền đoán ra nguyên nhân: Số tiền và đan dược này, trên danh nghĩa hiện tại chưa hoàn toàn thuộc quyền sở hữu hợp pháp của hắn! Một khi chuyện này bị phát giác, công an huyện vào cuộc tịch thu thì tang vật sẽ bị thu hồi. 

Tài phú chưa tăng thì Phương Bình cũng không vội. Việc cấp bách trước mắt là giải quyết cái cục nợ mang tên Hoàng Bân này!

Bắt thì đã bắt được người rồi, theo phương án thông thường thì cứ giao thẳng cho đồn cảnh sát là xong.

Nhưng Phương Bình không cam tâm cứ thế giao người ra! Hoàng Bân không phải kẻ câm, vừa vào đồn là khai tuốt tuột việc bị một thằng nhóc học sinh lột sạch đan dược bảo bối. Lúc đó, một học sinh trung học chưa có thế lực như hắn làm sao chịu nổi áp lực từ phía cảnh sát điều tra?

Nghĩ tới nghĩ lui, Phương Bình nhận ra mình phải tìm một người có chỗ đứng trong giới Võ đạo để cùng gánh vác áp lực.

Nói trắng ra là: Cùng nhau chia chác tang vật!

Nếu Phương Bình có đủ thực lực dàn xếp êm đẹp, với tính cách của hắn tự nhiên sẽ ăn trọn một mình. Nhưng hiện tại thực lực chưa đủ, đành phải cắt máu chia phần, dẫu sao vẫn hơn là trắng tay mất sạch.

Nhưng tìm ai để chia chác?

Trong đầu Phương Bình lập tức hiện lên bóng dáng của Vương Kim Dương!

Đây là hạ sách duy nhất, bởi vì ở cái huyện Dương Thành nhỏ bé này, Phương Bình chỉ quen biết đúng một vị Võ giả chính thức mà thôi!
"""
    },
    {
        "index": 32,
        "title_cn": "第三十二章 你没逗我？",
        "title_vi": "Chương 32: Cậu Không Trêu Tôi Chứ?",
        "content_vi": """1 giờ 20 phút chiều.

Tại một quán trà sữa nhỏ gần trường Trung học Số 1 Dương Thành.

Phương Bình vốn định tìm một quán cà phê lịch sự để bàn chuyện lớn, nhưng Dương Thành năm 2008 kinh tế còn kém phát triển, tìm mỏi mắt quanh khu vực trường học cũng chẳng thấy bóng dáng quán cà phê nào. Hơn nữa nghĩ mình vẫn đang là học sinh, vào quán trà sữa ngồi uống nước cam lại hợp lý hơn.

Phương Bình đã ngồi chờ ở đây gần nửa tiếng đồng hồ.

Uống cạn ly nước cam thứ hai, hắn ngẩng đầu nhìn ra ngoài cửa kính, chợt đứng dậy vẫy tay: "Vương ca, bên này!"

Bên ngoài cửa, Vương Kim Dương mặc chiếc áo khoác gió đơn giản, nở nụ cười sải bước đi vào. 

Phương Bình vội vàng đứng dậy đón tiếp, gọi thêm cho Vương Kim Dương một ly nước chanh đá rồi mời ngồi. Vương Kim Dương nhìn cử chỉ lễ phép nhưng đầy đĩnh đạc của Phương Bình, trong mắt hiện lên tia tán thưởng. Cậu học đệ này chững chạc hơn nhiều so với những học sinh cấp ba bình thường.

Vừa ngồi xuống, Phương Bình liền đi thẳng vào vấn đề:

"Vương ca, anh có thể bớt chút thời gian đến đây thật sự khiến em rất bất ngờ. Lúc gọi điện em chỉ thử vận may, không ngờ anh đến thật."

Vương Kim Dương nhấp một ngụm nước chanh, cười đáp: "Vừa vặn anh đang ở Dương Thành, thuận đường ghé qua thôi. Nói trước nhé, chuyện nhỏ thì anh tiện tay giúp được, chứ nếu rắc rối phức tạp quá thì anh cũng chịu đấy."

"Đương nhiên rồi ạ." Phương Bình gật đầu: "Em nói thẳng luôn. Chuyện em nói trong điện thoại hoàn toàn là thật, nhưng thực tế còn phức tạp hơn một chút. Kẻ bị thương mà em tình cờ tóm được... không phải người bình thường!"

Vương Kim Dương nheo mắt lại: "Ý cậu là gì?"

Phương Bình ghé sát tai thì thào: "Gã đó họ Hoàng, tên Hoàng Bân! Là một Võ giả Nhị Phẩm Đỉnh Phong đang bị truy nã!"

"Cái gì?!"

Vương Kim Dương sắc mặt đột nhiên biến đổi, bàn tay đang cầm cốc nước khựng lại giữa không trung, ánh mắt sắc như chim ưng nhìn chằm chằm Phương Bình: "Cậu không đùa tôi chứ? Một học sinh cấp ba như cậu mà bắt sống được Võ giả nhị phẩm đỉnh phong?!"
"""
    },
    {
        "index": 33,
        "title_cn": "第三十三章 分赃结束",
        "title_vi": "Chương 33: Chia Chác Xong Xuôi",
        "content_vi": """Mười phút sau, tại căn phòng số 201 khu tập thể cũ.

Nhìn thấy Hoàng Bân đang nằm bất tỉnh nhân sự dưới gầm giường, toàn thân bị trói chặt như khúc giò, Vương Kim Dương không khỏi hít sâu một hơi khí lạnh, ánh mắt nhìn Phương Bình tràn đầy sự kinh ngạc không thể tin nổi!

Vương Kim Dương bước tới lật người Hoàng Bân lên, thuần thục lục soát một lượt rồi móc từ trong áo lót của hắn ra một khối ngọc thạch phát ra huỳnh quang mờ ảo, lập tức nhét thẳng vào túi áo trong của mình.

Sau đó, Vương Kim Dương quay lại nhìn Phương Bình, trầm ngâm suy nghĩ một lúc rồi mở lời:

"Phương Bình, sáu lọ đan dược này có hai viên Thối Cốt Đan và Hộ Phủ Đan cấp nhị phẩm. Cậu chưa đột phá võ giả, dùng đan dược nhị phẩm chỉ có nước nổ tung kinh mạch mà chết. Anh sẽ lấy hai viên này, đổi lại anh đưa cho cậu một viên Thối Cốt Đan nhất phẩm và một viên Hộ Phủ Đan nhất phẩm, vừa vặn để cậu dùng khi đột phá Võ giả!"

Dừng một chút, Vương Kim Dương nói tiếp: "Đương nhiên giá trị chênh lệch không nhỏ. Đan dược nhị phẩm giá thị trường khoảng 300 vạn tệ. Anh sẽ bồi thường thêm cho cậu 100 vạn tệ tiền mặt chuyển thẳng vào tài khoản!"

"Ngoài ra, tên Hoàng Bân này anh mang về nộp cho Cục Trinh Sát Nam Giang để lĩnh 50 vạn tiền thưởng truy nã. Mọi rắc rối về pháp lý và thẩm vấn anh sẽ gánh toàn bộ, cảnh sát Dương Thành sẽ không bao giờ tìm tới cậu!"

Phương Bình nghe vậy trong lòng mừng rỡ khôn xiết. 

Hắn hiểu rõ, vật phẩm giống ngọc thạch lúc nãy Vương Kim Dương cất đi chắc chắn là bảo vật vô giá, nhưng đó là thứ cường giả tranh đoạt, kẻ yếu như hắn cầm vào chỉ rước họa sát thân. 

Một viên Thối Cốt Đan, một viên Hộ Phủ Đan, cộng thêm 100 vạn tiền mặt sạch sẽ và sự bảo hộ của Vương Kim Dương — đây là món hời lớn nhất mà hắn có thể mơ tới!

"Vương ca sòng phẳng quá! Em hoàn toàn đồng ý!" Phương Bình dứt khoát bắt tay Vương Kim Dương.

Vương Kim Dương nhìn sâu vào mắt Phương Bình, gật đầu khen ngợi: "Cậu là người thông minh, biết tiến biết lui. Sau này lên Võ đại, chúng ta chắc chắn sẽ còn nhiều cơ hội hợp tác!"

Thế là màn "chia chác" hoàn tất trong sự hài lòng tuyệt đối của cả hai bên.
"""
    },
    {
        "index": 34,
        "title_cn": "第三十四章 数据转换",
        "title_vi": "Chương 34: Dữ Liệu Chuyển Hóa",
        "content_vi": """Sau khi tiễn Vương Kim Dương rời khỏi Dương Thành cùng tên tội phạm Hoàng Bân, Phương Bình vội vã ôm bọc đan dược và tiền mặt chạy một mạch về phòng 101 của mình.

Vừa bước vào phòng khóa chặt cửa, hắn còn chưa kịp thở phào ăn mừng thì sắc mặt đột ngột biến đổi!

Trong tầm nhìn của hắn, ba dòng chữ huỳnh quang quen thuộc bỗng nhiên biến mất tăm biến mất tích, giống như tivi bị mất điện tối om một màu đen kịt!

"Mẹ kiếp! Cái hệ thống rách nát này bị làm sao thế?!"

Phương Bình hoảng hồn, trong lòng chửi thầm: "Không phải là thấy mình kiếm được nhiều tiền quá nên cuỗm sạch điểm tài phú rồi bỏ trốn đấy chứ?!"

Hắn căng mắt nhìn trơ trơ vào hư không suốt năm phút, mắt cay xè chảy cả nước mắt.

Đúng lúc hắn tưởng chừng tuyệt vọng thì trước mắt đột nhiên lóe lên một luồng ánh sáng chói lọi!

Màn hình đen kịt từ từ sáng bừng trở lại, các dòng chữ mới hiện lên rõ ràng, sắc nét hơn hẳn trước kia:

【Hệ Thống Hỗ Trợ Võ Đạo - Phiên Bản Nâng Cấp】
- Tài Phú: 2.403.800 điểm!
- Khí Huyết: 121 Ka / 121 Ka
- Tinh Thần: 110 Hz / 110 Hz

Phương Bình dụi mắt, sau đó suýt nhảy dựng lên trần nhà vì sung sướng!

"Hai trăm bốn mươi vạn điểm Tài Phú?!"

Con số nhảy múa rực rỡ! Đúng như hắn dự đoán, sau khi Vương Kim Dương xác nhận chia tài sản và số đan dược, tiền mặt hoàn toàn thuộc quyền sở hữu của hắn, hệ thống đã lập tức ghi nhận toàn bộ giá trị thành điểm Tài Phú!

Hơn nữa giao diện còn được tối ưu hóa, không chỉ hiện thị chỉ số ước lượng mà còn có chức năng phân tích chi tiết kinh mạch và cảnh báo bão hòa khí huyết.

"Nâng cấp thì nói một tiếng chứ, làm ông đây sợ muốn đứng tim!" Phương Bình lẩm bẩm xoa ngực, nụ cười trên môi ngoác đến tận mang tai.

Nắm trong tay hơn hai triệu điểm Tài Phú, Phương Bình chính thức trở thành một "đại gia ngầm" của giới học sinh Dương Thành!
"""
    },
    {
        "index": 35,
        "title_cn": "第三十五章 万事俱备",
        "title_vi": "Chương 35: Vạn Sự Đều Đủ",
        "content_vi": """Đêm hôm đó, Phương Bình bắt đầu đợt tăng cường thực lực quy mô lớn đầu tiên của mình.

Ngồi trên giường đơn, hắn tập trung tinh thần vào bảng số liệu, hạ lệnh trong đầu: "Hệ thống, tăng Khí Huyết và Tinh Thần!"

"Oanh!"

Điểm Tài Phú trên bảng số liệu lập tức nhảy lùi: 2.403.800 -> 2.370.800 điểm!

Tiêu hao hơn ba vạn điểm Tài Phú trong chớp mắt! 

Đổi lại, huyết dịch toàn thân Phương Bình sôi trào như nước sôi trong nồi, huyết quản phồng to như những con giun đất trườn dưới da. Lồng ngực căng tràn sức mạnh, khí tức nóng rực bốc lên ngùn ngụt!

- Khí Huyết: Tăng thẳng lên 124 Ka!
- Tinh Thần: Vọt lên 140 Hz!

Đạt tới 124 Ka, Phương Bình cảm nhận rõ ràng các mao mạch bắt đầu có dấu hiệu căng tức, đây chính là ngưỡng giới hạn thể phách hiện tại của hắn khi chưa thối cốt sâu. Tinh thần đạt 140 Hz khiến đầu óc hắn tỉnh táo đến mức kỳ dị, nhưng cũng có chút trướng đau do sóng não quá mạnh.

Phương Bình biết dừng đúng lúc, không dám nhồi nhét thêm kẻo nổ kinh mạch, liền leo lên giường ngủ một giấc thật sâu để thân thể thích nghi.

...

Sáng hôm sau, thứ Bảy ngày 12 tháng 4 năm 2008.

Ánh mặt trời buổi sớm rọi qua khung rèm. Phương Bình bật dậy khỏi giường, chỉ cảm thấy toàn thân sảng khoái nhẹ nhõm vô cùng, từng lỗ chân lông như đang hít thở linh khí đất trời.

Vệ sinh cá nhân xong xuôi, Phương Bình sải bước tới trước phòng em gái, đập cửa rầm rầm:

"Phương Viên! Dậy mau! Sắp trễ giờ rồi!"
"Còn ngủ nữa mặt tròn như cái bánh bao bây giờ!"

Dưới màn gõ cửa bạo lực của anh trai, cánh cửa phòng hé mở. Cô bé Phương Viên đầu bù tóc rối như tổ quạ, mắt nhắm mắt mở lườm Phương Bình một cái sắc lẻm rồi lững thững đi vào nhà vệ sinh, miệng làu bàu: "Đồ anh trai đáng ghét, sáng sớm đã phá giấc mơ ăn đùi gà của người ta..."

Nhìn bóng lưng cô em gái nhỏ, Phương Bình mỉm cười ấm áp. 

Mọi thứ đã sẵn sàng. Tài phú có, thực lực có, con đường bước vào đỉnh cao võ đạo của hắn từ nay chính thức bằng phẳng thênh thang!
"""
    },
    {
        "index": 36,
        "title_cn": "第三十六章 殷勤的方圆",
        "title_vi": "Chương 36: Phương Viên Ân Cần",
        "content_vi": """Ting!

Tiếng chuông báo tin nhắn của chiếc điện thoại cục gạch vang lên. Phương Bình mở ra xem, là thông báo từ ngân hàng: Tài khoản của hắn vừa nhận thêm 100 vạn tệ tiền mặt chuyển khoản từ Vương Kim Dương!

Cùng lúc đó, bảng hệ thống nhấp nháy: Điểm Tài Phú chính thức cán mốc 3.370.000 điểm!

Hơn 337 vạn điểm Tài Phú! Một con số mà ngay cả các Võ giả chính thức nghe thấy cũng phải thèm thuồng nhỏ dãi!

Ngay sau đó, một tin nhắn khác từ số của Vương Kim Dương gửi tới:
【Đồ đã gửi chuyển phát nhanh hỏa tốc, chú ý nhận hàng!】

Phương Bình đọc đi đọc lại dòng tin nhắn ngắn ngủi ấy, trong lòng tràn đầy sự mong đợi. Thứ mà Vương Kim Dương gửi không phải là tiền tài, mà là thứ hắn khao khát nhất lúc này: 《Cơ Bản Tu Luyện Pháp》 của Võ đại!

Buổi chiều tan học ở trường Trung học Số 1, lớp trưởng Ngô Chí Hào chạy tới rủ: "Phương Bình, chiều nay bọn mình tới câu lạc bộ thể hình tập tạ rèn sức bật đấy, cậu đi cùng không?"

Phương Bình mỉm cười xua tay: "Thôi, chiều nay tớ có chút việc bận ở nhà, các cậu cứ đi đi."

Nhìn Phương Bình quay lưng bước đi một mình, một học sinh khác trong lớp bĩu môi nói nhỏ: "Tên Phương Bình này kiêu ngạo thật đấy, rủ đi tập cùng cũng không thèm đi."

Ngô Chí Hào lắc đầu cười: "Kệ cậu ấy đi, tính Phương Bình từ trước đến nay vốn thích lủi thủi một mình rồi."

Phương Bình căn bản chẳng để tâm đến những lời bàn tán sau lưng. Hắn hiện tại đang bận rèn luyện làm quen với chỉ số 124 Ka khí huyết mới tăng, đi nâng mấy quả tạ sắt với đám học sinh bình thường chẳng có chút tác dụng thực chiến nào.

Vừa về đến nhà, Phương Bình thấy Phương Viên hôm nay ngoan ngoãn lạ thường. Cô bé vừa thấy hắn bước vào cửa liền đon đả chạy tới đỡ lấy cặp sách, lại còn chủ động bưng ra một cốc nước lọc mát lạnh:

"Anh Phương Bình đi học về mệt chưa? Uống nước đi anh!"

Phương Bình nheo mắt nhìn con nhóc, cảnh giác lùi lại nửa bước: "Nói đi, lại làm vỡ cái gì của mẹ rồi muốn anh gánh tội thay đúng không?"

"Làm gì có!" Phương Viên phụng phịu chu mỏ: "Người ta quan tâm anh trai mà anh cứ nghi ngờ! Mà này... anh Phương Bình, hôm nay mẹ bảo hôm nọ thấy anh cầm bọc tiền to lắm, anh trúng vé số thật hả? Cho em xin năm mươi tệ mua kem đi mà..."

Phương Bình cười ha hả, gõ nhẹ lên trán cô bé: "Nằm mơ đi nhóc con! Muốn có tiền thì lo mà học hành chăm chỉ vào!"
"""
    },
    {
        "index": 37,
        "title_cn": "第三十七章 有钱先享受",
        "title_vi": "Chương 37: Có Tiền Phải Hưởng Thụ Trước",
        "content_vi": """Chủ nhật, ngày 13 tháng 4.

Sáng sớm, Phương Bình thay một bộ đồ lịch sự chững chạc, nhét toàn bộ số tiền mặt dự phòng vào ba lô rồi rời khỏi nhà.

Hôm nay hắn có một kế hoạch lớn: Đi mua nhà!

Căn nhà tập thể cũ của gia đình hiện tại quá chật hẹp, cách âm lại cực kỳ kém. Mỗi lần hắn vận chuyển khí huyết rèn luyện kinh mạch, tiếng thở dốc và tiếng cơ bắp va đập đều khiến Phương Viên bên ngoài nghi ngờ hiểu lầm. Hơn nữa sắp tới luyện tập đao pháp và thung công đòi hỏi không gian rộng rãi, hắn bắt buộc phải có một nơi tập luyện riêng tư và an toàn!

Huyện Dương Thành không lớn. Phương Bình không muốn mua nhà ở vùng ngoại ô xa xôi vì đi lại bất tiện. Hắn nhắm tới khu chung cư mới mang tên Quan Hồ Uyển.

Quan Hồ Uyển nằm ở vị trí đắc địa, nằm ngay giữa trường Trung học Số 1 và khu Cảnh Hồ Viên, vừa yên tĩnh, an ninh tốt, lại gần trung tâm.

Khu đô thị này mở bán từ năm 2006, đến nay năm 2008 cư dân đã vào ở khá đông, nhưng vẫn còn một số căn hộ thông tầng (duplex) diện tích lớn chưa bán hết do người dân huyện nghèo ít ai đủ tiền mua những căn đắt đỏ như vậy.

Bước vào sảnh văn phòng bán vé của Quan Hồ Uyển, không khí bên trong khá vắng vẻ. 

Mấy cô nhân viên bán hàng thấy một thiếu niên mặc đồng phục bước vào thì chẳng mấy mặn mà, tưởng chỉ là học sinh tò mò vào xem tờ rơi.

Chỉ có một nữ nhân viên trẻ tuổi mới vào nghề bước tới, lịch sự cúi chào: "Chào em, em muốn tìm hiểu thông tin căn hộ nào giúp gia đình à?"

Phương Bình mỉm cười, đi thẳng vào bàn sa bàn chỉ tay: "Chị giới thiệu cho em căn hộ thông tầng duplex tầng cao nhất ở tòa số 2 đi. Căn đã hoàn thiện nội thất sẵn ấy, nếu ưng ý hôm nay em thanh toán toàn bộ tiền mặt một lần luôn!"

Lời vừa dứt, toàn bộ các nhân viên bán hàng trong sảnh đều đồng loạt quay ngoắt lại, mắt tròn xoe nhìn Phương Bình như nhìn thấy người ngoài hành tinh!
"""
    },
    {
        "index": 38,
        "title_cn": "第三十八章 快递到了！",
        "title_vi": "Chương 38: Chuyển Phát Nhanh Đã Tới!",
        "content_vi": """Nghe thấy hai chữ "thanh toán toàn bộ tiền mặt", vị giám đốc kinh doanh đang ngồi trong phòng làm việc lập tức lao ra tiếp đón Phương Bình như đón khách quý thượng đỉnh!

Đối với chủ đầu tư, những căn hộ thông tầng diện tích lớn bị tồn đọng suốt hai năm là gánh nặng vốn lớn. Gặp được khách hàng mua đứt một lần, chiết khấu được đẩy lên mức tối đa!

"Phương tiên sinh, căn hộ thông tầng này diện tích 186 mét vuông, toàn bộ sàn gỗ cao cấp, hệ thống điện nước và ban công ngắm hồ đã hoàn thiện 100%! Nếu cậu thanh toán toàn bộ ngay hôm nay, bên tôi giảm trực tiếp 5%, miễn toàn bộ phí bảo trì và thuế trước bạ!"

"Tổng giá trị trọn gói sau giảm giá chỉ còn đúng 81 vạn tệ!"

81 vạn tệ năm 2008 cho một căn hộ 186m² full nội thất cao cấp!

Phương Bình tính nhẩm trong đầu: Một viên Khí Huyết Đan của võ giả có giá 30 vạn tệ. Ba viên thuốc bổ của Hoàng Bân có giá gần 90 vạn tệ — tương đương với cả một căn đại trạch viện nguy nga giữa lòng huyện thành!

Võ giả ăn một bữa thuốc bổ bằng cả đời tích cóp của một gia đình công nhân bình thường. Sự chênh lệch giai cấp giữa người thường và Võ giả tàn khốc đến nhường nào!

Phương Bình không hề kỳ kèo, mở ba lô đặt cọc ngay 20 vạn tệ tiền mặt, hẹn thứ Tư tuần sau sẽ thanh toán nốt phần còn lại để nhận chìa khóa.

Vừa bước chân về đến cửa nhà ngõ Liễu Thụ, một chiếc xe tải chuyển phát nhanh bưu chính đã đỗ xịch trước cửa.

"Ai là Phương Bình? Có bưu phẩm bảo mật cấp 1 gửi từ Đại học Nam Giang Võ Khoa!"

"Là tôi!" Phương Bình bước tới ký nhận.

Cầm chiếc hộp bưu phẩm bọc kín bằng băng keo niêm phong màu đỏ có đóng dấu mộc của Cục Võ Đạo, tim Phương Bình đập thình thịch.

Hắn ôm chiếc hộp chạy vội lên phòng, khóa trái cửa lại. Dùng dao rọc giấy cẩn thận rạch lớp băng dính, mở nắp hộp ra.

Bên trong hộp xếp ngay ngắn sáu cuốn sách bìa cứng dày cộp, mùi mực in thơm phức đập vào mũi:

- 《Cơ Bản Tu Luyện Pháp (Bắt Buộc)》
- 《Thung Công Thập Lục Thức (Bắt Buộc)》
- 《Cơ Bản Quyền Pháp (Tự Chọn)》
- 《Cơ Bản Cước Công (Tự Chọn)》
- 《Binh Khí Lãnh Khái Luận (Tự Chọn)》...

Phương Bình hít một hơi thật sâu, bàn tay run run chạm vào trang bìa cuốn sách tu luyện đầu tiên trong đời. Cánh cửa bí mật của giới Võ đạo... cuối cùng đã mở toang trước mắt hắn!
"""
    },
    {
        "index": 39,
        "title_cn": "第三十九章 基本修炼法",
        "title_vi": "Chương 39: Cơ Bản Tu Luyện Pháp",
        "content_vi": """Phương Bình cẩn thận lật mở trang đầu tiên của cuốn 《Cơ Bản Tu Luyện Pháp》.

Đập vào mắt hắn ngay trang tựa là một dòng chữ viết tay bằng mực đen sắc sảo như nét kiếm chém đá:

【Võ Giả — Dám Vì Người Trước!】

Tám chữ ngắn gọn nhưng khí phách ngút trời, tỏa ra một cỗ ý chí kiên định bảo vệ nhân tộc!

Lật sang trang tiếp theo, một bức đồ giải giải phẫu hệ thống xương cốt người cực kỳ chi tiết hiện ra.

Cơ thể người trưởng thành gồm 206 khối xương: Xương sọ 29 khối, xương thân mình 51 khối, xương tứ chi 126 khối. Xương là khung đỡ, máu thịt là động lực. 

Muốn trở thành Võ giả, Khí Huyết và Xương Cốt phải tương hỗ lẫn nhau. Người có khí huyết mạnh mà xương cốt yếu thì vừa tung một quyền đã gãy tay; ngược lại xương cứng mà khí huyết cạn kiệt thì chẳng khác nào cỗ máy thiếu nhiên liệu, không có lực bộc phát.

Giới hạn chịu đựng tự nhiên của người bình thường là 150 Ka khí huyết! 

Vượt qua ngưỡng 150 Ka, nếu không thối cốt rèn xương thì áp lực khí huyết sẽ xé toạc các huyết quản và màng xương, dẫn đến tàn phế. Vì vậy, người luyện võ trước khi thi đại học đều cố gắng đẩy khí huyết chạm mốc 150 Ka và bước đầu rèn luyện màng xương để chuẩn bị đột phá Nhất Phẩm!

Ngoài ra, cuốn sách còn giới thiệu chi tiết về hệ thống tuần hoàn khí huyết qua các đường kinh lạc chính: Nhâm mạch, Đốc mạch và mười hai chính kinh.

Phương Bình đọc như nuốt từng chữ. Những kiến thức này kiếp trước hắn chỉ thấy trong phim kiếm hiệp viễn tưởng, nay lại là môn khoa học thực nghiệm có thật trăm phần trăm!

Đọc xong lý thuyết, Phương Bình nhìn sang cuốn 《Thung Công Thập Lục Thức》.

Thung công (đứng tấn) chính là phương pháp rèn luyện then chốt nhất để kết hợp giữa Khí Huyết và Xương Cốt. Thung công chia làm ba cảnh giới:
1. Trạm Ổn (Đứng vững như bàn thạch, người ngoài đẩy không ngã).
2. Trạm Thực (Khí huyết chìm xuống đan điền, dẫm chân xuống đất phát ra tiếng như nện búa).
3. Trạm Hoạt (Thân hình chuyển động linh hoạt như cưỡi ngựa bay trên mây, vừa di chuyển vừa bộc phát lực kình).

"Thung công... rèn luyện sự cân bằng và bộc phát lực lượng từ đôi chân!" Phương Bình ghi nhớ từng khẩu quyết, chuẩn bị bước vào buổi luyện tập thực tế đầu tiên.
"""
    },
    {
        "index": 40,
        "title_cn": "第四十章 第一次修炼",
        "title_vi": "Chương 40: Lần Đầu Tiên Tu Luyện",
        "content_vi": """Trước khi bắt đầu tu luyện 《Thối Luyện Pháp》, Phương Bình vẫn có chút chưa an tâm. Dù sao kinh mạch trong cơ thể con người vô cùng mỏng manh, ngộ nhỡ đi sai một đường khí huyết dẫn đến tẩu hỏa nhập ma thì nguy to.

Hắn rút điện thoại gọi thẳng cho Vương Kim Dương.

Đầu dây bên kia, Vương Kim Dương nghe Phương Bình nói muốn bắt đầu tự tu luyện công pháp thì không khỏi nhíu mày căn dặn:

"Phương Bình, 《Thối Luyện Pháp》 là công pháp cơ bản phổ cập của cả nước, độ an toàn tương đối cao, dù có đi chệch kinh mạch một chút cũng không nguy hiểm đến tính mạng. Nhưng anh phải cảnh báo cậu một điều cực kỳ quan trọng!"

Phương Bình nín thở lắng nghe: "Vương ca cứ nói ạ."

"Thứ nhất: Tu luyện 《Thối Luyện Pháp》 tiêu hao Khí Huyết cực kỳ khủng khiếp! Khí huyết dùng để cọ rửa màng xương một khi tiêu hao sẽ khiến cơ thể rơi vào trạng thái suy nhược đói khát dữ dội. Người bình thường không có thuốc bổ trợ lực thì mỗi tuần chỉ dám luyện hai lần, mỗi lần mười phút!"

"Thứ hai: Nếu cậu cố tình luyện quá độ mà không bổ sung dinh dưỡng kịp thời, khí huyết cạn kiệt sẽ tự động rút cạn tinh hoa tủy xương của cậu, biến cậu thành kẻ tàn phế!"

"Em hiểu rồi, cảm ơn Vương ca đã nhắc nhở!" Phương Bình cười thầm trong bụng.

Người khác sợ cạn kiệt khí huyết, chứ hắn nắm trong tay hơn 300 vạn điểm Tài Phú, hết khí huyết chỉ cần tiêu hao vài trăm điểm là lại tràn trề sinh lực tức thì!

Cúp điện thoại, Phương Bình ngồi xếp bằng trên sàn nhà, nhắm mắt tĩnh tâm.

Dựa theo đồ hình kinh mạch trong sách, hắn vận chuyển ý niệm, dẫn dắt luồng khí huyết ấm áp trong đan điền chậm rãi lưu chuyển qua kinh mạch cánh tay phải.

"Tê tê..."

Cảm giác nóng rực lan tỏa dọc theo bắp tay, thẩm thấu vào lớp màng xương cánh tay. Cơn đau nhói như kim châm truyền đến nhưng Phương Bình cắn răng chịu đựng.

Chỉ sau mười phút vận hành một chu thiên trọn vẹn, trán Phương Bình đã ướt đẫm mồ hôi. Nhìn lên bảng hệ thống: Khí huyết từ 124 Ka sụt xuống còn 115 Ka!

"Hồi phục khí huyết!" Phương Bình thầm niệm.

【Tiêu hao 900 điểm Tài Phú! Khí huyết phục hồi đầy đủ: 124 Ka!】

Cảm giác ấm áp dâng trào xua tan toàn bộ mệt mỏi! Lần đầu tiên tu luyện thành công mỹ mãn!
"""
    },
    {
        "index": 41,
        "title_cn": "第四十一章 花钱如流水",
        "title_vi": "Chương 41: Tiêu Tiền Như Nước",
        "content_vi": """“Rầm rầm rầm!”

Đúng lúc Phương Bình đang đắc ý chuẩn bị vận chuyển thêm một chu thiên 《Thối Luyện Pháp》 thì cánh cửa phòng ngủ lại bị đập rung bần bật!

Chẳng cần hỏi Phương Bình cũng biết ngay ai là tác giả của màn gõ cửa như đòi nợ này.

Quả nhiên, giọng nói lanh lảnh của Phương Viên từ ngoài cửa vọng vào:

"Phương Bình! Anh ở trong phòng làm cái trò gì đấy hả?!"
"Lúc thì thở hồng hộc như trâu, lúc thì cười khúc khích một mình..."
"Anh có biết nghe biến thái lắm không?!"
"Em nhắc nhở anh nhé, biến thái thế sau này không cưới được vợ đâu đấy!"
"Em còn nhỏ, anh đừng có làm hư tâm hồn trẻ thơ của em!"

Phương Bình mặt đen như đít nồi, tức tối mở tung cửa ra hét lớn:

"Mày nói nhảm cái gì đấy hả con nhóc này?!"
"Ai biến thái? Ai làm hư mày?"
"Tao đường đường chính chính luyện công, luyện võ đạo hiểu chưa?!"

Phương Viên đứng chống nạnh bĩu môi khinh bỉ: "Gạt ai chứ gạt em à! Luyện công sao không ra sân mà luyện, trốn trong phòng đóng kín cửa thở dốc làm gì? Em mặc kệ, từ giờ cấm anh thở mạnh như thế trong nhà, nghe ghê chết đi được!"

Phương Bình dở khóc dở cười, nhìn xuống ống quần thể thao của mình vì lúc nãy khí huyết bộc phát làm vỡ vài mao mạch nhỏ khiến vạt quần dính vài vệt máu li ti. Căn nhà tập thể cũ này cách âm quá kém, tường mỏng dính, hắn mà đứng tấn luyện thung công dậm chân rầm rầm thì hàng xóm tưởng động đất mất.

"Phải dọn sang nhà mới gấp!" Phương Bình càng thêm quyết tâm.

Hắn thay bộ quần áo sạch sẽ, nhét chìa khóa vào túi rồi bước nhanh ra khỏi nhà. Luyện võ không chỉ tốn sức mà còn đốt tiền như nước, hắn phải nhanh chóng hoàn thiện nội thất căn hộ Quan Hồ Uyển để có một đại bản doanh tu luyện đích thực!
"""
    },
    {
        "index": 42,
        "title_cn": "第四十二章 体育馆",
        "title_vi": "Chương 42: Nhà Thi Đấu",
        "content_vi": """Sáng thứ Tư.

Tiết học buổi sáng vừa kết thúc, Phương Bình liền phóng xe thẳng tới văn phòng kinh doanh Quan Hồ Uyển.

Sau khi nộp nốt số tiền 61 vạn tệ còn lại, hắn chính thức nhận trong tay cuốn sổ đỏ, hợp đồng mua bán và chùm chìa khóa căn hộ thông tầng duplex 186m²!

Tiền mặt trong ba lô của hắn lúc này chỉ còn lại hơn 41 vạn tệ.

Cầm chùm chìa khóa bước vào căn nhà mới toanh, Phương Bình ngắm nhìn phòng khách rộng thênh thang lát đá hoa cương bóng loáng, trần nhà cao năm mét, ban công nhìn thẳng ra mặt hồ lộng gió mà lòng lâng lâng phấn khởi.

Mới trùng sinh chưa đầy hai tháng, hắn từ một thằng nhóc nghèo rớt mồng tơi nay đã sở hữu căn hộ sang trọng bậc nhất huyện thành!

"Tạm thời chưa thể nói cho bố mẹ biết chuyện này." Phương Bình tự nhủ: "Nếu đột nhiên bảo mình mua nhà gần trăm vạn tệ, bố mẹ chắc chắn sẽ lo lắng mất ăn mất ngủ, tưởng mình đi buôn hàng cấm. Chờ đến khi có giấy báo trúng tuyển Võ đại, lúc đó nói là trường tài trợ hoặc hợp tác với Vương Kim Dương thì hợp lý hơn nhiều."

Buổi chiều, Phương Bình ghé qua Trung tâm Nội thất lớn nhất thành phố để sắm sửa trang bị. 

Bàn ghế sofa hắn chỉ mua loại vừa phải, dùng tạm là được. Nhưng riêng về dụng cụ tập luyện thể lực và thung công, Phương Bình không tiếc tiền vung tay đặt mua toàn bộ hàng cao cấp nhập khẩu:

Một bao cát da bò ba lớp nặng 150 kg; hai thanh xà đơn chịu lực một tấn; thảm cao su giảm chấn chuyên dụng cho võ đạo; một bộ tạ tay hợp kim và cọc gỗ luyện thung công!

Toàn bộ đồ tập hết gần ba vạn tệ, hẹn ngày mai giao hàng lắp đặt tận nơi.

Trở lại trường học, cậu bạn cùng bàn Trần Phàm quay sang nhìn Phương Bình với vẻ tò mò: "Phương Bình, dạo này thấy mày cứ thoắt ẩn thoắt hiện như thần long ấy, trưa nào cũng lén lút chuồn đi đâu thế?"

Phương Bình cười bí hiểm: "Đi kiếm tiền cưới vợ cho mày đấy!"
"""
    },
    {
        "index": 43,
        "title_cn": "第四十三章 背锅王",
        "title_vi": "Chương 43: Vua Đổ Vỏ",
        "content_vi": """Giờ ra chơi buổi chiều.

Phương Bình đang ngồi đọc sách thì Ngô Chí Hào bước tới, thần sắc có chút thần bí kéo hắn ra một góc hành lang vắng người:

"Phương Bình, cậu có để ý hai anh em nhà họ Đàm lớp 12 ban 1 không?"

Phương Bình nhướng mày: "Anh em Đàm Hạo và Đàm Đào ấy à? Bọn họ làm sao?"

Ngô Chí Hào hạ thấp giọng: "Bọn họ là Võ nhị đại thứ thiệt đấy! Bố của bọn họ là Võ giả Nhất Phẩm đang làm việc ở Cục Thuế huyện. Tớ nghe ngóng được, từ năm lớp 10 hai anh em nhà đó đã bắt đầu luyện 'Thung công' rồi!"

"Thung công?" Phương Bình làm bộ ngạc nhiên.

Ngô Chí Hào gật đầu chắc nịch: "Đúng thế! Giới con nhà võ gọi là trạm thung. Cậu có biết vì sao đám võ nhị đại ở trường bình thường biểu hiện không quá nổi bật không? Bởi vì bọn họ không vội nâng khí huyết trước mắt, mà dành toàn bộ thời gian rèn luyện thung công để xây nền móng vững chắc!"

"Đợi đến khi vào Võ đại, người có gốc thung công vững vàng sẽ đột phá thành Võ giả nhanh gấp đôi người thường!"

Ngô Chí Hào thở dài một hơi đầy vẻ ghen tị: "Nhưng mà người bình thường như chúng mình không học theo bọn họ được đâu. Luyện thung công vừa tốn thời gian, tốn sức lực, lại đốt tiền mua thuốc bổ kinh hoàng. Không có bố làm võ giả cung cấp đan dược thì càng luyện càng suy kiệt!"

Phương Bình im lặng gật đầu, nhưng trong lòng thì cười thầm.

Ngô Chí Hào nói không sai đối với người bình thường. Luyện thung công cực kỳ hao tổn khí huyết và tinh thần lực, đứng tấn nửa tiếng là chân run như cầy sấy, đầu óc mê man phải nghỉ ngơi hai ba ngày mới hồi phục.

Nhưng đối với Phương Bình — kẻ có hệ thống nạp năng lượng vô hạn, thì thung công chính là mảnh ghép hoàn hảo nhất mà hắn đang tìm kiếm!

"Chiều nay tan học, tớ phải qua nhà thi đấu xem hai anh em họ Đàm đứng tấn thế nào mới được!" Phương Bình thầm lên kế hoạch.
"""
    },
    {
        "index": 44,
        "title_cn": "第四十四章 吴志豪的猜测",
        "title_vi": "Chương 44: Phán Đoán Của Ngô Chí Hào",
        "content_vi": """Chiều hôm đó tại góc sân tập của nhà thi đấu huyện.

Hai anh em Đàm Hạo và Đàm Đào đang đứng theo tư thế Mã Bộ Thung, hai chân chùng xuống, hai tay ôm tròn trước ngực, lưng thẳng như thân trúc. Trên vầng trán của hai người mồ hôi chảy ròng ròng, hô hấp kéo dài và đều đặn theo từng nhịp thở.

Phương Bình đứng từ xa quan sát chăm chú từng cử động vi mô của cơ bắp hai người.

Thấy Phương Bình đứng xem, Đàm Hạo thu công thở ra một ngụm trọc khí, lau mồ hôi cười thân thiện: "Phương Bình, cậu cũng có hứng thú với thung công à?"

Phương Bình bước tới chào hỏi lễ phép: "Em chào hai anh. Em vừa đọc được vài tài liệu về thung công nhưng chưa hiểu rõ nguyên lý phát lực, thấy hai anh luyện tập uyển chuyển quá nên đứng xem học hỏi chút ạ."

Hai anh em họ Đàm tính tình khá cởi mở, thấy Phương Bình khiêm tốn hỏi han lại là bạn học cùng khối nên không ngần ngại chỉ điểm:

"Thung công không có bí mật gì to tát đâu, mấu chốt là kiên trì mài giũa theo thời gian. Nguyên tắc cốt lõi là 'Trụ vững như cây thông, thân mềm như dây leo'. Khi đứng tấn, không được dùng sức gồng cứng cơ bắp, mà phải dùng ý niệm dẫn dắt khí huyết lắng xuống đan điền, để trọng tâm cơ thể cắm sâu xuống lòng đất!"

"Bọn anh mỗi ngày cũng chỉ dám đứng tấn tối đa nửa tiếng. Đứng lâu quá khí huyết tiêu hao hết, hôm sau đầu đau như búa bổ không học nổi văn hóa."

Phương Bình gật đầu cảm ơn, trong lòng đã hiểu thấu mấu chốt.

Người thường mỗi ngày chỉ dám đứng tấn 30 phút vì sợ kiệt sức. 

Nhưng Phương Bình thì khác!

Tối hôm đó về nhà mới Quan Hồ Uyển, Phương Bình bắt đầu đứng tấn từ 7 giờ tối. 

Hết khí huyết? Tiêu hao 500 điểm Tài Phú nạp đầy!
Tinh thần mỏi mệt? Tiêu hao 500 điểm Tài Phú làm mới tinh thần!

Hắn đứng tấn liên tục suốt 4 tiếng đồng hồ không nghỉ! Một đêm luyện tập của Phương Bình bằng cả tháng khổ luyện của anh em họ Đàm cộng lại!
"""
    },
    {
        "index": 45,
        "title_cn": "第四十五章 桩功突破！",
        "title_vi": "Chương 45: Đột Phá Thung Công!",
        "content_vi": """Tối thứ Bảy.

Tại phòng tập rộng rãi của căn hộ Quan Hồ Uyển.

Phương Bình đang đứng theo tư thế Mã Bộ Thung. Nhưng khác với mấy ngày trước đứng im bất động như tượng gỗ, lúc này nửa thân trên của hắn đang khẽ lắc lư theo một nhịp điệu kỳ dị.

"Cột sống như rồng lượn, bước chân nhẹ tựa lông hồng..."
"Khí trầm đan điền, dẫm chân không xê dịch!"

Đột nhiên, hai chân Phương Bình khẽ chuyển động, bước chân di chuyển nhẹ nhàng trên thảm cao su nhưng cỗ khí thế trầm ổn dưới gót chân vẫn không hề suy suyển nửa phần!

Trạm Ổn cảnh giới — Đột phá!

Hắn đã chính thức nắm vững tầng thứ nhất của Thung công: Người ngoài đẩy không ngã!

Đúng lúc này, Phương Viên từ phòng khách tò mò chạy vào, trên tay cầm nửa quả dưa hấu, mắt tròn xoe nhìn anh trai lắc lư:

"Phương Bình, anh đứng kiểu gì mà trông buồn cười thế? Nhìn như con lật đật ấy!"

Phương Bình nheo mắt cười nhìn cô em gái: "Viên Viên, lại đây đẩy anh một cái xem nào."

"Hả? Anh bảo em đẩy anh á?" Phương Viên chớp mắt, sau đó nhếch mép cười gian: "Là anh tự tìm đòn đấy nhé! Đừng có bảo em bắt nạt anh!"

Cô bé đặt miếng dưa hấu xuống bàn, xoa xoa hai tay rồi lao tới, vươn ngón tay ấn mạnh vào trán Phương Bình.

Mấy hôm trước cô bé cũng từng đẩy thử một cái khiến Phương Bình lảo đảo ngã ngồi xuống đệm, nên Phương Viên đinh ninh lần này cũng dễ như ăn kẹo.

"Hây!" 

Phương Viên dồn hết sức bình sinh của một cô bé lớp 6 đẩy mạnh về phía trước!

Thế nhưng, trán Phương Bình vẫn vững như núi đá ngàn năm! Cả người hắn không hề nhúc nhích dù chỉ nửa phân!

Phương Viên trố mắt ngạc nhiên, liền đổi sang dùng cả hai tay ôm lấy hông Phương Bình, nghiến răng nghiến lợi dồn toàn bộ trọng lượng cơ thể kéo đẩy.

"Hừ... hừ..." Cô bé thở hồng hộc, mặt đỏ bừng như quả gấc mà Phương Bình vẫn đứng sừng sững như một gốc cổ thụ cắm rễ sâu mười mét dưới lòng đất!

Phương Bình cúi đầu nhìn cô em gái đang toát mồ hôi hột, cười ha hả nhéo má cô bé một cái:

"Sao thế tiểu mập mạp? Hết sức rồi à? Về ăn thêm cơm đi nhé!"
"""
    },
    {
        "index": 46,
        "title_cn": "第四十六章 新福利",
        "title_vi": "Chương 46: Phúc Lợi Mới",
        "content_vi": """Sau khi đột phá tầng thứ nhất của Thung công, Phương Bình mở bảng hệ thống ra kiểm tra.

Dòng số liệu hiển thị khiến hắn mừng rỡ:
- Khí Huyết: 128 Ka / 128 Ka!
- Tinh Thần: 145 Hz / 145 Hz!
- Tài Phú: 3.250.000 điểm!

Chỉ sau vài ngày đứng tấn kết hợp thối cốt sơ bộ, giới hạn khí huyết tự nhiên của hắn đã tăng thêm 4 Ka mà không cần nhồi nhét cưỡng ép! Cơ bắp săn chắc, từng thớ thịt bám chặt vào xương cốt, dáng đi thoăn thoắt nhẹ nhàng như loài báo săn mồi.

Sáng thứ Hai tại trường Trung học Số 1, thầy chủ nhiệm Lưu Thành Vinh thông báo một tin tức sốt dẻo:

"Các em học sinh báo danh Võ khoa chú ý! Theo chính sách đãi ngộ mới nhất của Bộ Giáo Dục, bắt đầu từ tuần này, toàn bộ thí sinh đã vượt qua kỳ sát hạch sơ bộ sẽ được cấp thẻ ưu đãi đặc biệt:"

"Thứ nhất: Miễn phí toàn bộ vé vào cửa các Nhà thi đấu Thể thao và phòng tập thể lực công cộng trên toàn tỉnh!"
"Thứ hai: Mỗi tuần được cấp phát miễn phí 10 kg thịt thú dinh dưỡng cao tại căng tin trường!"
"Thứ ba: Được phép mượn xem các video tư liệu thực chiến mật của các Võ giả tiền bối tại phòng đa phương tiện của trường!"

Cả lớp 12 ban 4 lại một phen xôn xao ghen tị. 

Thịt thú dinh dưỡng cao ngoài thị trường có giá cả trăm tệ một cân, ăn vào giúp bồi bổ khí huyết tự nhiên rất tốt. Đối với những học sinh bình dân thì đây là nguồn dinh dưỡng vô cùng quý giá.

Phương Bình nhận tấm thẻ ưu đãi mạ vàng từ tay thầy Lưu, trong lòng thầm cảm thán: Xã hội này quả nhiên dành mọi đặc quyền và đãi ngộ tối thượng cho con đường Võ đạo. Càng thể hiện ra thiên phú xuất chúng thì tài nguyên sẽ tự động đổ dồn về như thác lũ!
"""
    },
    {
        "index": 47,
        "title_cn": "第四十七章 狂热的马粉",
        "title_vi": "Chương 47: Fan Cuồng Của Họ Mã",
        "content_vi": """Giờ giải lao tại phòng đọc báo của trường.

Trần Phàm đang ôm cuốn tạp chí 《Võ Đạo Phong Vân》 số mới nhất, hai mắt sáng rực như đèn pha ô tô, miệng liên tục xuýt xoa:

"Phương Bình, mày mau nhìn này! Mã Tông Sư lại lập kỳ tích rồi!"

Phương Bình tò mò ghé đầu sang nhìn: "Mã Tông Sư nào? Mã Hóa Đằng hay Mã Vân?"

"Cả hai luôn!" Trần Phàm hào hứng hoa tay múa chân: 

"Tạp chí đưa tin, tuần trước tại hội nghị thượng đỉnh Võ đạo Châu Á, Đằng Tấn Mã Tông Sư đã dùng tuyệt kỹ 《Vạn Kiếm Quy Tông - Lôi Đình Quyết》 nhất kích đánh bại một vị Tông Sư Thất Phẩm của đảo quốc! Còn A Lý Ba Ba Mã Tông Sư thì dùng 《Thái Cực Bát Quái Chưởng》 áp đảo hoàn toàn đoàn đại biểu võ thuật phương Tây!"

"Hai vị Mã Tông Sư đúng là thần tượng vĩ đại nhất của đời tao! Sau này tao mà đỗ vào Võ đại, tao nhất định phải nộp đơn xin gia nhập Đằng Tấn Võ Quán hoặc A Lý Võ Quán để bái sư!"

Phương Bình nhìn bộ dạng mê muội của cậu bạn thân, không khỏi bật cười lắc đầu. Kiếp trước thanh niên thần tượng các ông trùm công nghệ vì kiếm được nhiều tiền, kiếp này chuyển sang thần tượng vì chiến lực vô song có thể một đấm đập nát ngọn núi!

Tuy nhiên, Phương Bình cũng chú ý đến một chi tiết nhỏ trên trang cuối của tờ tạp chí:

【Cảnh báo an ninh cấp quốc gia: Thời gian gần đây, tần suất chấn động năng lượng tại các Cửa Không Gian ngầm có dấu hiệu gia tăng. Các đại tập đoàn võ đạo như Đằng Tấn, A Lý, Tân Đông Phương đang ráo riết tuyển mộ sinh viên tốt nghiệp các trường Võ đại danh tiếng để bổ sung lực lượng phòng thủ biên ải...】

"Cửa Không Gian ngầm... chính là lối vào Địa Quật!" Phương Bình nheo mắt thầm nghĩ. 

Cuộc sống phồn hoa trên mặt đất càng rực rỡ bao nhiêu thì bóng tối chiến tranh dưới lòng đất lại càng gấp gáp bấy nhiêu. Thời gian không còn nhiều, hắn phải tranh thủ từng ngày từng giờ để trở nên mạnh mẽ hơn nữa!
"""
    },
    {
        "index": 48,
        "title_cn": "第四十八章 视频",
        "title_vi": "Chương 48: Video Thực Chiến",
        "content_vi": """Buổi chiều, tận dụng quyền hạn của tấm thẻ ưu đãi đặc biệt, Phương Bình một mình bước vào phòng đa phương tiện bảo mật của trường Trung học Số 1.

Người quản lý phòng tư liệu kiểm tra kỹ thẻ căn cước và mã số thí sinh của hắn rồi mới mở khóa một chiếc máy tính quân dụng biệt lập:

"Phương Bình, đây là tư liệu thực chiến mật cấp 2, nghiêm cấm sao chép hay quay phim chụp ảnh dưới mọi hình thức, hiểu chưa?"

"Dạ, em hiểu rồi ạ."

Người quản lý rời đi, để lại Phương Bình một mình trong căn phòng tối mờ. 

Hắn nhấn chuột mở tệp video có tên: 【Thực Chiến Hạ Tam Phẩm Võ Giả & Quái Vật Biên Ải】.

Màn hình lóe sáng. 

Khung cảnh hiện ra không phải là sàn đấu thể thao sạch sẽ, mà là một vùng đất hoang vu đỏ quạch như máu, bầu trời u ám xám xịt không có mặt trời!

Dưới mặt đất gồ ghề đầy đá sỏi, một con quái thú hình dạng giống loài sói nhưng to lớn như một chiếc xe bán tải, toàn thân bọc vảy sừng đen nhánh, răng nanh dài nửa mét đang gầm thét lao tới!

Đối diện với quái thú là một tiểu đội gồm ba Võ giả loài người mặc giáp nhẹ bọc hợp kim, tay cầm trường đao và chiến phủ.

"Giết!"

Một tiếng quát vang rền như sấm nổ! 

Vị Võ giả dẫn đầu bộc phát khí huyết đỏ thắm, bước chân dẫm nát mặt đất lao vút đi với tốc độ xé gió! Thanh trường đao trong tay hắn chém ra một luồng đao mang sắc bén dài hơn một mét, chuẩn xác chặt đứt hai chân trước của con quái thú!

Máu đen tanh tưởi bắn tung tóe! Hai Võ giả phía sau lập tức phối hợp ăn ý, chiến phủ giáng thẳng xuống đầu quái thú, nghiền nát hộp sọ con thú trong tích tắc!

Toàn bộ trận chiến diễn ra chớp nhoáng chưa đầy mười lăm giây!

Phương Bình ngồi trước màn hình, tim đập thình thịch, cả người toát mồ hôi lạnh. 

Đây chính là thực chiến sinh tử đích thực! Không có hoa quyền thêu thùa, không có nhường nhịn tính điểm! Mỗi một chiêu thức tung ra đều nhắm thẳng vào chỗ hiểm để đoạt mạng đối phương trong thời gian ngắn nhất!

Xem xong video, Phương Bình hít sâu một hơi, trong mắt bốc cháy ngọn lửa chiến ý: "Muốn sống sót trên chiến trường tàn khốc kia, nắm đấm của ta phải nhanh hơn, đao của ta phải bén hơn, và khí huyết của ta phải dồi dào hơn tất cả bọn chúng!"
"""
    },
    {
        "index": 49,
        "title_cn": "第四十九章 迫不及待",
        "title_vi": "Chương 49: Không Thể Chờ Đợi",
        "content_vi": """Những ngày cuối cùng của tháng Năm trôi qua trong bầu không khí ngột ngạt đến nghẹt thở.

Kỳ thi Đại khảo Võ khoa toàn quốc năm 2008 chỉ còn đếm từng ngày!

Tại huyện Dương Thành, toàn bộ các trường trung học đã hoàn tất việc chốt danh sách thí sinh chính thức. 

Trường Trung học Số 1 năm nay có bốn thí sinh đủ điều kiện bước vào kỳ thi tuyển sinh đỉnh cấp tại Ma Đô: Phương Bình, Ngô Chí Hào, Dương Kiến và Chu Bân.

Trong căn phòng tập tại Quan Hồ Uyển, Phương Bình đang thực hiện bài tập chém đao cuối cùng.

"Vút! Vút! Vút!"

Thanh đao gỗ trong tay hắn xé rách không khí phát ra những tiếng rít chói tai. Bộ pháp dưới chân thoăn thoắt biến ảo, thân hình hắn tựa như một cơn gió lốc càn quét khắp căn phòng.

Sau hơn một tháng khổ luyện kết hợp Thung công và thối luyện màng xương, chỉ số của hắn trên bảng hệ thống đã đạt tới mức khủng khiếp:
- Khí Huyết: 130 Ka / 130 Ka!
- Tinh Thần: 150 Hz / 150 Hz!
- Tài Phú: 3.120.000 điểm!

Với mức Khí Huyết 130 Ka ở tuổi mười tám khi chưa chính thức vào đại học, Phương Bình tự tin bản thân không hề thua kém bất kỳ thiên tài gia tộc nào tại siêu đô thị Ma Đô!

Hắn thu đao đứng thẳng, lau mồ hôi trên trán rồi bước ra ban công nhìn về phương Nam xa xôi.

Những kiến thức đã học, những giọt mồ hôi đã đổ, những cơn đau đớn khi thối cốt cắn răng chịu đựng... tất cả đã chuẩn bị đầy đủ cho thời khắc định mệnh này!

Hắn không thể chờ đợi thêm được nữa! 

Hắn muốn bước lên vũ đài lớn nhất của đất nước, dùng thực lực đích thực của mình để chứng minh cho toàn thế giới thấy: Một thiếu niên bần hàn xuất thân từ huyện nghèo cũng có thể đạp bằng chư thiên thiên kiêu, bước lên đỉnh cao nhân loại!
"""
    },
    {
        "index": 50,
        "title_cn": "第五十章 出发",
        "title_vi": "Chương 50: Xuất Phát",
        "content_vi": """Sáng ngày 5 tháng 6 năm 2008.

Sân ga xe lửa Dương Thành chìm trong làn sương sớm mờ ảo.

Bốn học sinh trường Trung học Số 1 mang theo hành trang chỉnh tề, dưới sự dẫn dắt của Hiệu trưởng Tôn Chính Đức và thầy chủ nhiệm Lưu Thành Vinh, đã có mặt đông đủ trước cổng soát vé.

Bố mẹ Phương Bình cùng cô em gái nhỏ Phương Viên đứng tiễn hắn ở sân ga.

Phương Danh Vinh nắm chặt hai bàn tay thô ráp của con trai, ánh mắt tràn đầy sự kỳ vọng và yêu thương: "Bình nhi, lên Ma Đô nhớ giữ gìn sức khỏe. Bố mẹ ở nhà luôn tin tưởng con!"

Mẹ hắn — Lý Ngọc Anh dúi vào tay hắn bọc trứng gà luộc còn nóng hổi và mấy gói bánh ngọt: "Đi đường cẩn thận nghe con, thi cử cứ bình tĩnh, đừng tự tạo áp lực cho mình."

Phương Viên ôm chặt lấy cánh tay anh trai, khóe mắt rưng rưng nhưng miệng vẫn cố cười toe toét: "Anh Phương Bình, nhớ lời hứa mua gấu bông to đùng cho em đấy nhé! Không đỗ Ma Đô Võ Đại là em không nhận anh trai đâu!"

Phương Bình mỉm cười xoa đầu cô em gái, ánh mắt ấm áp mà kiên định: "Yên tâm đi, anh hứa danh dự với em!"

"Tu tu tu——!"

Tiếng còi tàu xe lửa kéo dài một hồi vang dội, báo hiệu giờ khởi hành đã điểm.

"Các em học sinh, lên tàu thôi!" Hiệu trưởng Tôn hô lớn, vẫy tay ra hiệu cho cả đoàn bước lên bậc thang toa tàu.

Phương Bình đeo chiếc ba lô đen lên vai, bước lên toa xe. Đứng bên khung cửa sổ kính, hắn vẫy tay chào cha mẹ và em gái đang đứng ngóng trông dưới sân ga. 

Bánh xích chuyển động, con tàu từ từ lăn bánh rồi lao vút về phía chân trời xa xôi, bỏ lại sau lưng huyện thành nhỏ bé Dương Thành.

Phương Bình ngồi tựa lưng vào ghế nệm, nhìn phong cảnh lướt qua ngoài cửa sổ, bàn tay siết chặt thành nắm đấm.

Một thế giới mới rực lửa, một thời đại hào hùng của những Tông Sư dời non lấp biển và những trận chiến Địa Quật kinh thiên động địa... đang mở rộng cánh cửa đón chào hắn!

Chuyến tàu định mệnh đã bắt đầu. Truyền kỳ vô địch của Nhân Vương Phương Bình... chính thức khởi hành từ đây!
"""
    }
]

def update_batch4():
    conn = sqlite3.connect('data/novels.db', timeout=60.0)
    cursor = conn.cursor()
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_count = 0
    
    for ch in CHAPTERS_BATCH4:
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
    print(f"\n[HOÀN TẤT] Đã cập nhật thành công {updated_count} chương Batch 4 chuẩn nguyên tác cho Toàn Cầu Cao Võ (ID: {NOVEL_ID})")

if __name__ == '__main__':
    update_batch4()
