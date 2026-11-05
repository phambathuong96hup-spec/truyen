# -*- coding: utf-8 -*-
"""
Script dịch trực tiếp và cập nhật 10 chương đầu của siêu phẩm Toàn Cầu Cao Võ (ID: 61)
Tác giả: Lão Ưng Cật Tiểu Kê (老鹰吃小鸡)
Dịch thuật và biên tập chuẩn văn phong tiên hiệp - cao võ đô thị bởi Antigravity.
"""

import sqlite3
import datetime

NOVEL_ID = 61

CHAPTERS_DATA = [
    {
        "index": 1,
        "title_cn": "第一章 重生2008",
        "title_vi": "Chương 1: Trùng Sinh Năm 2008",
        "content_vi": """Ánh nắng ban chiều vàng vọt xuyên qua khung cửa sổ lớp học, rọi lên mặt bàn gỗ loang lổ vết mực. 

Phương Bình mơ màng mở mắt, chỉ cảm thấy đầu đau như búa bổ, cổ họng khô khốc như có ngọn lửa đang thiêu đốt. Hắn vô thức đưa tay xoa thái dương, nhưng bàn tay đập vào mắt lại khiến hắn giật mình sững sờ.

Bàn tay này... không có những vết chai sạn vì bôn ba nhiều năm nơi công sở, cũng không có làn da sạm màu vì khói thuốc và rượu bia. Đây rõ ràng là bàn tay của một thiếu niên, trắng trẻo, ngón tay thon dài, tràn đầy sức sống thanh xuân!

"Phương Bình, mày còn ngủ à? Lão Lưu sắp vào kiểm tra bài tập đấy, mau chép bài vật lý của tao đi này!"

Một giọng nói quen thuộc pha chút sốt ruột vang lên bên tai. Phương Bình giật nảy mình quay sang. 

Ngồi cạnh hắn là một thiếu niên vóc người nhỏ thẹo, đeo cặp kính cận dày cộp, trên người mặc bộ đồng phục thể dục xanh trắng quen thuộc đến tận xương tủy.

"Trần Phàm?" Phương Bình há hốc mồm, nghẹn ngào thốt lên.

"Chứ ai vào đây nữa? Mày ngủ đến lú lẫn rồi à?" Cậu bạn đẩy gọng kính, tức giận ném sang cuốn vở bài tập: "Hôm qua thức khuya xem đá bóng đúng không? Mau lên, chỉ còn mười phút nữa là vào tiết tự học rồi!"

Phương Bình nhìn quanh căn phòng. Bốn mươi mấy gương mặt non choẹt đang cặm cụi cúi đầu viết lách. Phía trên bảng đen bằng gỗ sơn xanh, dòng chữ đỏ chót đập vào mắt hắn:

【Khoảng cách tới Kỳ thi Đại học năm 2008 còn lại: 58 ngày!】

"Năm 2008? Mình... mình thật sự trùng sinh về năm lớp 12 rồi sao?!"

Một cỗ nhiệt huyết mãnh liệt dâng trào trong lồng ngực Phương Bình. Trái tim hắn đập thình thịch như trống trận. 

Kiếp trước, sau khi tốt nghiệp đại học hạng hai, hắn lăn lộn mười mấy năm ngoài xã hội, chịu đủ mọi chèn ép, cuối cùng chỉ là một nhân viên quản lý nhỏ nhoi ở thành phố hạng ba, mua không nổi nhà, cưới không nổi vợ, cha mẹ già yếu bệnh tật không có tiền chữa trị. 

Nhưng bây giờ là năm 2008! 

Năm 2008 có ý nghĩa gì? 

Đây là thời đại hoàng kim của bất động sản! Là thời điểm đồng Bitcoin sắp ra đời với giá chỉ vài xu một đồng! Là lúc Tencent, Alibaba, ByteDance chuẩn bị bùng nổ thống trị internet toàn cầu!

Chỉ cần bằng vào ký ức cùng tầm nhìn vượt trước mười mấy năm của một người hiện đại, dù hắn chỉ nằm im mua vài chục ngàn Bitcoin hay gom vài mảnh đất ở ngoại ô Ma Đô, hắn cũng có thể trở thành tỉ phú nghìn tỉ, sống một đời vinh hoa phú quý, đưa cả gia đình bước lên đỉnh cao nhân sinh!

Khóe miệng Phương Bình không kìm được nhếch lên một nụ cười ngây ngô sung sướng. Hắn đã nghĩ tới cảnh tượng mình ngậm xì gà, ngồi trong biệt thự ven sông Ma Đô, tùy ý đầu tư vài trăm triệu đô la...

"Cạch!"

Cửa lớp học đột ngột mở ra. Thầy giáo chủ nhiệm Lưu Thành Vinh bước vào. Lão Lưu vẫn mang dáng vẻ nghiêm nghị cố hữu, tay kẹp một xấp tài liệu dày cộp. Cả lớp lập tức im phăng phắc.

Lão Lưu đứng trên bục giảng, quét mắt nhìn một lượt quanh lớp rồi hắng giọng trầm giọng nói:

"Các em trật tự! Trước khi bắt đầu tiết học hôm nay, thầy có một thông báo đặc biệt quan trọng liên quan trực tiếp đến tiền đồ cả đời của các em!"

"Theo chỉ thị mới nhất từ Bộ Giáo Dục và Cục Võ Đạo tỉnh Giang Nam, kỳ thi sát hạch Võ khoa năm nay sẽ chính thức bắt đầu tiếp nhận đơn báo danh từ ngày mai. Thời hạn nộp hồ sơ và lệ phí là trong vòng một tuần!"

"Những em nào có nguyện vọng báo danh Võ khoa, tối nay về nhà nhất định phải bàn bạc kỹ lưỡng với gia đình. Lệ phí báo danh năm nay vẫn giữ nguyên như cũ: 10.000 tệ nộp cho Cục Khảo Thí! Gia đình nào có điều kiện và bản thân cảm thấy có cơ hội thì hãy suy nghĩ cẩn thận!"

"Được rồi, ai muốn đăng ký thì tan học lên gặp thầy lấy mẫu đơn!"

Trên bục giảng, Lão Lưu tiếp tục giảng giải, nhưng bên dưới, Phương Bình như bị sét đánh ngang tai, toàn thân cứng đờ.

Võ... Võ khoa? 

Lệ phí báo danh... 10.000 tệ?

Phương Bình trừng trừng mắt nhìn Lão Lưu, trong đầu như có ngàn vạn con tuấn mã chạy qua gào thét: 

"Cái quỷ gì thế này?! Không phải là thi đại học khối A, khối B bình thường sao? Võ khoa từ đâu chui ra vậy?!"
"""
    },
    {
        "index": 2,
        "title_cn": "第二章 这个世界不对劲",
        "title_vi": "Chương 2: Thế Giới Này Không Đúng!",
        "content_vi": """Phương Bình đưa tay véo thật mạnh vào đùi mình một cái.

"Ái ui!" Cơn đau nhói truyền đến khiến hắn suýt nhảy dựng khỏi ghế. Không phải mơ! Cơn đau chân thật trăm phần trăm!

Hắn nuốt nước bọt, quay sang ghé sát tai Trần Phàm thì thào: "Này Trần Phàm... cái 'Võ khoa' mà thầy Lưu vừa nói... là cái gì thế?"

Trần Phàm trừng mắt nhìn hắn, vươn tay sờ lên trán Phương Bình: "Mày có bị sốt không đấy? Hay trúng tà rồi? Võ khoa mà mày cũng hỏi là cái gì? Không thi Võ khoa chẳng lẽ đi thi Văn khoa để ra trường làm culi cả đời à?"

"Ý tao là... thi Võ khoa thì thi những môn gì? Quyền cước? Chạy bộ?"

"Mày đùa đấy à?" Trần Phàm trợn tròn mắt: "Kiểm tra Khí Huyết, khảo thí Thể Phách, sát hạch Thân Pháp và Thực Chiến! Nếu qua được kỳ sơ tuyển, lên đại học Võ khoa thì một bước lên trời, được phân phối đan dược, tu luyện chiến pháp, sau này tốt nghiệp ít nhất cũng là Võ giả tam phẩm, bổng lộc hàng năm cả triệu tệ, địa vị xã hội cao hơn cả thị trưởng!"

Phương Bình nghe mà da đầu tê rần.

"Keng keng keng..."

Tiếng chuông tan trường vừa vang lên, Phương Bình chẳng kịp chào Trần Phàm, vội vã vơ lấy cặp sách lao thẳng ra khỏi cổng trường Trung học Số 1 Dương Thành.

Hắn phải tự mình nhìn tận mắt xem thế giới này rốt cuộc đã xảy ra chuyện quái quỷ gì!

Đường phố Dương Thành vẫn mang dáng dấp của một huyện thành nhỏ năm 2008. Những quán nước vỉa hè, xe đạp Phượng Hoàng, những tiệm net cỏ bảng hiệu bạc màu... Mọi thứ nhìn bề ngoài vẫn vô cùng bình thường.

Thế nhưng, khi Phương Bình đi tới trước sạp báo lớn ở góc ngã tư quảng trường, tầm mắt hắn lập tức đông cứng lại.

Trên sạp báo, các tờ nhật báo và tạp chí lớn nhất Hoa Hạ được xếp trang trọng ở vị trí trung tâm:

Tờ 《Võ Đạo Nhật Báo》: 
【Tin chấn động: Đằng Tấn Mã Tông Sư vừa bế quan đột phá Bát Phẩm Kim Thân Cảnh, ngự không phi hành ba ngàn dặm, Đằng Tấn Võ Quán chính thức chiêu sinh đệ tử chân truyền!】

Tờ 《Kinh Đô Thời Báo》:
【A Lý Ba Ba Mã Tông Sư tại đỉnh núi Tây Hồ luận kiếm, nhất chưởng đẩy lùi phong vân, tuyên bố rót 100 tỷ tệ xây dựng Quỹ Bồi Dưỡng Võ Giả Trẻ!】

Tờ 《Hoàn Cầu Phong Vân》:
【Cổ Cáp (Google) người sáng lập tuyên bố đột phá Cửu Phẩm Tuyệt Đỉnh, khiêu chiến Tông sư bảng toàn cầu!】

Bên cạnh đó là bức ảnh màu chụp một người đàn ông mặc áo võ phục màu trắng phiêu dật, phong thái như thần tiên giáng thế — gương mặt ấy Phương Bình không thể nào nhận nhầm, chính là ông trùm công nghệ Mã Hóa Đằng kiếp trước! Nhưng trên bức ảnh này, Mã Hóa Đằng hai chân lơ lửng giữa hư không cách mặt đất mười trượng, quanh thân quấn quanh lôi đình điện quang rực rỡ!

"Má nó chứ... Mã Hóa Đằng ngự không phi hành? Đột phá Bát Phẩm Kim Thân?!"

Phương Bình lảo đảo lùi lại hai bước, ngực phập phồng dữ dội. 

Hắn tiếp tục nhìn sang các quầy tạp chí khác:
"Đại sư Cổ Cự Cơ độc bộ thiên hạ", "Tân Đông Phương Du Tông Sư kiếm pháp vô song dạy ngoại ngữ", "Mười đại cường giả Đỉnh Phong Hoa Hạ"...

Tất cả những danh nhân, chính trị gia, tỷ phú của thế giới trước... ở thế giới này đều là những đại cao thủ võ đạo cái thế!

Nơi này căn bản không phải là thế giới đô thị bình thường! Đây là một thế giới Cao Võ — nơi mà nắm đấm và sức mạnh cá nhân quyết định tất cả! 

Những ý tưởng làm giàu kiểu mua cổ phiếu công nghệ, đầu cơ bất động sản của hắn trong chớp mắt vỡ tan như bong bóng xà phòng. Ở một thế giới mà cường giả có thể một đấm đập tan tòa cao ốc, một chưởng xé toạc dòng sông, thì thương nhân hay tài phiệt không có võ lực bảo hộ chẳng khác nào con cừu béo chờ bị làm thịt!

"Võ đạo chí thượng... Chỉ có trở thành Võ giả mới có thể đứng thẳng lưng làm người!"

Phương Bình siết chặt hai nắm đấm, trong mắt lóe lên một tia sáng kiên định chưa từng có.
"""
    },
    {
        "index": 3,
        "title_cn": "第三章 武科考与一万块",
        "title_vi": "Chương 3: Khảo Thí Võ Khoa & 1 Vạn Tệ Lệ Phí",
        "content_vi": """Trời chập choạng tối. 

Phương Bình men theo con ngõ nhỏ Liễu Thụ quen thuộc, bước lên tầng ba của một khu nhà tập thể cũ kỹ xây từ thập niên 90. 

Đứng trước cánh cửa sắt sơn xanh đã tróc sơn từng mảng, Phương Bình hít một hơi thật sâu, gõ cửa.

"Cạch."

Cánh cửa mở ra. Xuất hiện trước mặt hắn là một cô bé chừng mười hai tuổi, mặc chiếc áo phông in hình hoạt hình rộng thùng thình, tóc buộc đuôi ngựa, hai má phúng phính như bánh bao trắng. 

Cô bé ngẩng khuôn mặt tròn xoe lên nhìn Phương Bình, nháy mắt tinh nghịch: "Phương Bình, sao hôm nay về muộn thế? Mẹ bảo nếu anh về trễ nữa là trừ tiền cơm tối nay đấy nhé!"

Nhìn thấy cô bé, trái tim Phương Bình mềm nhũn ra. Đây là em gái ruột của hắn — Phương Viên. Kiếp trước, vì hoàn cảnh gia đình khó khăn, cô bé sau khi tốt nghiệp cấp ba đã phải bươn chải đi làm thuê phụ giúp gia đình, chịu đủ mọi tủi nhục cay đắng. 

Phương Bình đưa tay xoa mạnh đầu Phương Viên, cười nói: "Nha đầu thối, dám gọi thẳng tên anh à?"

"A a! Làm hỏng tóc người ta rồi!" Phương Viên chu mỏ né tránh, giậm chân phụng phịu chạy tọt vào bếp: "Mẹ ơi! Anh Phương Bình bắt nạt con!"

Bên trong gian bếp nhỏ bốc lên mùi thơm ngào ngạt của thịt xào tiêu và canh cải ngọt. 

Cha hắn — Phương Danh Vinh, một người đàn ông trung niên chất phác, trên trán đã hằn sâu những nếp nhăn của sương gió cuộc đời, đang ngồi trên ghế gỗ xem thời sự. Mẹ hắn — Lý Ngọc Anh, tay đeo tạp dề bưng bát canh nóng đặt lên bàn, cười hiền từ: "Vào ăn cơm đi con, đói bụng cả ngày rồi."

Cả nhà bốn người ngồi quây quần bên mâm cơm đơn sơ. Cảm giác ấm áp của gia đình khiến Phương Bình kiếp này lần đầu tiên cảm nhận được ý nghĩa thực sự của việc được sống lại.

Phương Bình vừa và cơm, vừa giả vờ vô tình mở miệng hỏi:

"Bố... mẹ... Hôm nay trường con thông báo bắt đầu tiếp nhận hồ sơ báo danh thi Võ khoa."

Lời vừa dứt, đôi đũa trên tay Phương Danh Vinh đột nhiên khựng lại giữa không trung. Không khí trong căn phòng nhỏ bỗng chốc trở nên yên ắng lạ thường. Ngay cả cô em gái Phương Viên hay nói cười cũng im bặt, lén nhìn cha mẹ.

Phương Danh Vinh đặt chén cơm xuống bàn, im lặng một hồi lâu rồi mới trầm giọng hỏi: "Bình nhi, con... con muốn thi Võ khoa sao?"

"Dạ." Phương Bình ngẩng đầu, ánh mắt nhìn thẳng vào cha: "Con muốn thử một lần!"

Lý Ngọc Anh thở dài một tiếng, ánh mắt tràn đầy vẻ lo lắng: "Bình nhi, con cũng biết đấy... lệ phí báo danh một vạn tệ không phải là chuyện nhỏ. Nhà mình... bố mẹ tích cóp cả năm trời mới được ngần ấy. Quan trọng hơn là, nghe nói thi Võ khoa khắt khe lắm, một huyện Dương Thành này mỗi năm mấy ngàn học sinh thi mà đỗ được không quá ba mươi người! Nếu trượt thì số tiền đó..."

Một vạn tệ năm 2008! 

Lương công nhân của Phương Danh Vinh ở xưởng gốm một tháng chỉ tầm một ngàn tám trăm tệ, Lý Ngọc Anh làm ở xưởng may chỉ được một ngàn hai trăm tệ. Một vạn tệ gần như là toàn bộ số tiền tiết kiệm phòng thân của gia đình này!

Phương Bình biết rõ gánh nặng ấy. Nhưng nếu không bước chân vào con đường Võ đạo, hắn và cả gia đình này sẽ mãi mãi giậm chân ở tầng đáy xã hội, tương lai gặp phải đại nạn căn bản không có lực phản kháng!

Đúng lúc này, Phương Danh Vinh rút trong túi ra một điếu thuốc lá rẻ tiền, châm lửa rít một hơi sâu. 

Làn khói mờ ảo bao phủ lấy khuôn mặt phong sương của người cha. Sau một hồi im lặng kéo dài nghẹt thở, ông ngẩng đầu nhìn con trai, ánh mắt ánh lên vẻ kiên quyết:

"Thi! Ngày mai bố sẽ đi rút tiền tiết kiệm, nếu thiếu bố sẽ sang nhà bác cả mượn thêm! Con trai bố muốn có tiền đồ, người làm cha như bố dù có đập nồi bán sắt cũng phải ủng hộ con!"

"Bố..." Phương Bình nghẹn ngào, cổ họng như ứ nghẹn.

"Ăn cơm đi! Ăn nhiều thịt vào cho khỏe người!" Phương Danh Vinh gắp một miếng thịt nạc lớn nhất trong đĩa bỏ vào bát Phương Bình, nụ cười trên gương mặt đầy vẻ kiên định của tình phụ tử.
"""
    },
    {
        "index": 4,
        "title_cn": "第四章 属性面板与财富值",
        "title_vi": "Chương 4: Bảng Thuộc Tính & Điểm Tài Phú",
        "content_vi": """Đêm khuya, bốn bề tĩnh mịch.

Phương Bình nằm trên chiếc giường đơn chật hẹp trong căn phòng nhỏ của mình, nhìn trần nhà ố vàng mà trằn trọc không sao chợp mắt nổi.

Một vạn tệ của cha mẹ là mồ hôi nước mắt, hắn tuyệt đối không thể vung phí vô ích. Nhưng muốn đỗ Võ khoa, điều kiện tiên quyết là chỉ số Khí Huyết phải đạt chuẩn!

Theo tin tức hắn nghe ngóng được ở trường, chuẩn Khí Huyết sơ tuyển của Dương Thành năm ngoái là 112 Ka (đơn vị đo khí huyết), năm nay dự kiến còn tăng cao hơn, có thể lên tới 115 Ka trở lên! 

Mà học sinh bình thường chưa từng rèn luyện võ đạo, thể chất dinh dưỡng kém như hắn, khí huyết nhiều nhất chỉ tầm 100 đến 105 Ka. Muốn tăng khí huyết, những con nhà giàu phải uống thuốc bổ khí huyết giá hàng ngàn tệ một thang, ngâm bồn dược liệu đắt đỏ. Hắn lấy đâu ra tiền mà bồi bổ?

"Chẳng lẽ người trùng sinh như mình lại đành chịu chết trơ mắt nhìn cơ hội vụt mất sao?" Phương Bình nghiến răng lẩm bẩm.

"Ong——!"

Đúng lúc này, trong đầu Phương Bình vang lên một tiếng ngân dài kỳ dị. 

Trước mắt hắn, không gian bỗng dao động như sóng nước, một luồng ánh sáng huỳnh quang màu xanh nhạt ngưng tụ lại, hóa thành một khung bảng chữ nhật bán trong suốt lơ lửng ngay trong tầm nhìn:

【Hệ Thống Võ Đạo Hỗ Trợ】
- Túc chủ: Phương Bình
- Khí Huyết: 110 Ka / 110 Ka
- Tinh Thần: 100 Hz / 100 Hz
- Tài Phú: 0 điểm

"Đây... đây là?!"

Phương Bình giật thót người, hai mắt trợn tròn suýt nữa hét toáng lên! 

Hắn chớp chớp mắt, nhắm mắt lại rồi mở ra, bảng huỳnh quang vẫn hiện diện sừng sững trong võng mạc của hắn!

"Bảng thuộc tính?! Bàn tay vàng của người xuyên việt đã đến rồi!"

Trái tim Phương Bình đập thình thịch như trống trận. Hắn lập tức tập trung toàn bộ tinh thần để dò xét từng dòng chữ trên bảng giao diện.

Dưới bảng giao diện có một dòng chú thích nhỏ tự động hiện ra trong tâm trí hắn:

【Quy tắc hệ thống:】
1. Điểm Tài Phú được ghi nhận khi túc chủ sở hữu hoặc kiểm soát tiền tệ, tài sản hợp pháp. Tỷ lệ quy đổi: 1 tệ = 1 điểm Tài Phú. (Lưu ý: Tiền chỉ cần xác nhận quyền sở hữu của túc chủ là hệ thống sẽ cộng điểm, túc chủ tiêu dùng tiền thực tế ngoài đời sẽ KHÔNG bị trừ điểm Tài Phú của hệ thống!).
2. Túc chủ có thể tiêu hao điểm Tài Phú để trực tiếp gia tăng chỉ số Khí Huyết và Tinh Thần mà không để lại bất kỳ di chứng hay tổn thương kinh mạch nào. Tỷ lệ hoán đổi hiện tại: 10.000 điểm Tài Phú = 1 Ka Khí Huyết (hoặc 1 Hz Tinh Thần).

"Cái gì?!"

Phương Bình đọc đến dòng chú thích này mà toàn thân run rẩy vì kích động tột độ!

Tiền kiếm được ngoài đời, hệ thống tự động ghi nhận điểm Tài Phú! Dù hắn có đem tiền đó đi nộp học phí hay mua đồ ăn thì điểm Tài Phú trên hệ thống vẫn còn nguyên!

Và quan trọng nhất: Chỉ cần có tiền, hắn có thể trực tiếp mua Khí Huyết! 

Không cần khổ luyện mười năm rách da xé thịt, không cần sợ thuốc bổ có tạp chất làm nghẽn kinh mạch, chỉ cần có tiền, hắn có thể tăng vọt khí huyết một cách hoàn hảo nhất!

"Ha ha ha! Trời không tuyệt đường người!" Phương Bình suýt nữa cười ha hả thành tiếng giữa đêm khuya.

Nhưng ngay sau đó, hắn nhìn lại dòng cuối cùng:
【Tài Phú: 0】

Nụ cười trên môi Phương Bình lập tức tắt ngúm.

"Hiện tại trong người mình... một xu dính túi cũng không có! Làm sao để có tiền thử nghiệm hệ thống bây giờ?!"
"""
    },
    {
        "index": 5,
        "title_cn": "第五章 妹妹方圆与存钱罐",
        "title_vi": "Chương 5: Em Gái Phương Viên & Heo Đất",
        "content_vi": """Trong lúc Phương Bình đang vò đầu bứt tai thì bỗng nhiên, một hình bóng quen thuộc xẹt qua trong đầu hắn.

Phương Viên!

Con nhóc tì kia từ nhỏ đã có thói quen tích cóp tiền tiêu vặt. Bất kể là tiền mừng tuổi của ông bà bác chú, hay tiền thừa đi chợ mẹ cho, cô bé đều nhét hết vào một con lợn đất bằng sứ màu hồng giấu dưới gầm giường!

Kiếp trước, có lần Phương Bình tình cờ phát hiện con heo đất ấy nặng trịch, ước tính ít nhất cũng phải có vài trăm đến cả ngàn tệ!

"Viên Viên à Viên Viên, vì tiền đồ tương lai của anh trai mày, vì sự nghiệp Võ đạo cứu vớt nhân loại, đành phải mượn 'kho bạc' của mày dùng trước một lát vậy!"

Phương Bình rón rén bò dậy, mở cửa phòng ngủ, bước chân nhẹ như mèo sang phòng đối diện.

Cửa phòng Phương Viên khép hờ. Cô bé đang nằm ngủ say sưa trên giường, chăn bông đạp tung tóe, khóe miệng còn chảy một vệt nước miếng nhỏ xíu, trong miệng lẩm bẩm: "Đùi gà nướng... đùi gà thơm quá..."

Phương Bình nén cười, rón rén bò xuống sàn, thò tay vào sâu trong gầm giường. Quả nhiên, bàn tay hắn chạm phải một vật thể tròn trịa, mát lạnh và nặng trĩu.

Chính là nó! Con heo đất gốm màu hồng phấn!

Phương Bình ôm con heo đất nhẹ nhàng lui về phòng mình, khóa chặt cửa lại. 

Nhìn con heo đất được dán kín mít bằng băng dính ở khe bụng dưới, Phương Bình không nỡ đập vỡ. Hắn lấy một cây nhíp sắt nhỏ từ bàn học, kiên nhẫn khều từng tờ tiền qua khe nhét tiền phía trên.

"Xoạt... xoạt..."

Mười tệ, năm mươi tệ, một trăm tệ, tiền xu một tệ...

Sau gần nửa tiếng đồng hồ "câu cá", toàn bộ tài sản tích cóp suốt sáu năm của cô bé Phương Viên đã nằm gọn gàng trên bàn học của Phương Bình.

Hắn đếm đi đếm lại ba lần:
Tổng cộng: 868 tệ tiền mặt!

Phương Bình hít sâu một hơi, vươn hai tay nắm chặt lấy xấp tiền, trong lòng thầm niệm: "Đây là tiền của ta! Ta là chủ nhân của số tiền này!"

"Ong!"

Ngay khoảnh khắc ý niệm của hắn vừa phát ra, bảng huỳnh quang trước mắt hắn đột ngột lóe sáng:

【Phát hiện tài sản thuộc quyền sở hữu của túc chủ: 868 tệ】
【Điểm Tài Phú cập nhật: 868 điểm!】

"Thành công rồi! Thật sự tăng điểm rồi!"

Phương Bình mừng rỡ như điên. Hắn lập tức nhìn sang chỉ số Khí Huyết:
- Khí Huyết: 110 Ka / 110 Ka.
- Tinh Thần: 100 Hz / 100 Hz.
- Tài Phú: 868.

Theo quy tắc, 10.000 điểm tài phú mới đổi được 1 Ka khí huyết hoàn chỉnh. Nhưng 868 điểm tài phú này liệu có thể chuyển hóa thành một phần nhỏ khí huyết không?

Phương Bình tập trung suy nghĩ vào mục Khí Huyết, trong đầu hô lớn: "Tăng Khí Huyết! Tiêu hao toàn bộ 800 điểm tài phú!"

"Oanh——!"

Vừa dứt lời, điểm Tài Phú trên bảng lập tức nhảy lùi: 868 -> 68 điểm!

Đồng thời, một luồng nhiệt lưu ấm áp cực kỳ mãnh liệt tựa như nham thạch nóng bỏng từ đan điền hắn đột nhiên phun trào, điên cuồng tràn vào kinh mạch toàn thân!

Từng tế bào trong cơ thể Phương Bình như những mảnh đất khô hạn lâu ngày gặp phải mưa rào cam lộ, tham lam hấp thu nguồn năng lượng thần kỳ ấy. Các thớ cơ bắp vốn hơi nhão của hắn siết chặt lại, xương cốt phát ra những tiếng "răng rắc" giòn giã!

Cảm giác ấm áp, sảng khoái đến từng lỗ chân lông khiến Phương Bình suýt rên lên thành tiếng.

Mười giây sau, luồng nhiệt lưu dần lắng xuống. 

Phương Bình vội vàng nhìn lên bảng thuộc tính:
- Khí Huyết: 111 Ka / 111 Ka!
- Tinh Thần: 100 Hz
- Tài Phú: 68 điểm

Khí huyết từ 110 Ka tăng thẳng lên 111 Ka!

Phương Bình siết chặt nắm đấm. Hắn cảm nhận rõ ràng sức mạnh trong tay mình đã tăng lên một bậc, lồng ngực tràn trề sinh lực, hô hấp kéo dài và sâu hơn hẳn trước kia!

"Quá thần kỳ! Không cần ăn đan dược độc hại, trực tiếp tăng thuộc tính!"

Phương Bình nhìn 68 điểm tài phú còn lại và xấp tiền trên bàn, khóe miệng nhếch lên nụ cười tự tin: "Chỉ cần ngày mai nộp một vạn tệ lệ phí thi, mình sẽ có 10.000 điểm Tài Phú! Đến lúc đó, khí huyết của mình sẽ trực tiếp tăng vọt lên một tầm cao mới!"

Hắn cẩn thận xếp lại xấp tiền của Phương Viên, nhét ngược từng tờ vào bụng con heo đất rồi đem trả về chỗ cũ dưới gầm giường của cô bé. 

"Yên tâm đi nha đầu ngốc, sau này anh trai mày trở thành Đại Tông Sư, sẽ đền cho mày cả một con heo bằng vàng ròng!"
"""
    },
    {
        "index": 6,
        "title_cn": "第六章 报名武科与气血激荡",
        "title_vi": "Chương 6: Báo Danh Võ Khoa & Chấn Động Khí Huyết",
        "content_vi": """Sáng hôm sau, trường Trung học Số 1 Dương Thành tràn ngập bầu không khí sôi sục.

Tại lớp 12 ban 4, học sinh tụ tập thành từng nhóm nhỏ, chủ đề bàn tán duy nhất lúc này chỉ có một: Báo danh Võ khoa!

"Nghe nói lớp trưởng Ngô Chí Hào đã điền đơn rồi đấy!"
"Gia đình Ngô Chí Hào làm kinh doanh lớn, nghe đâu từ năm ngoái đã bỏ ra hơn mười vạn tệ mua Dưỡng Khí Đan cho cậu ấy uống bồi bổ, khí huyết tuần trước đo thử đã đạt 115 Ka rồi!"
"Trời ạ, 115 Ka sao? Thế thì nắm chắc một suất đỗ vào Đại học Võ khoa tỉnh rồi!"
"Đúng là con nhà giàu, chúng ta người bình thường làm sao so được..."

Giữa đám đông, Ngô Chí Hào mặc bộ đồ thể thao hàng hiệu đắt tiền, vóc người cao lớn, vẻ mặt đầy kiêu hãnh đang được các bạn cùng lớp vây quanh tâng bốc. 

Đúng lúc này, giáo viên chủ nhiệm Lưu Thành Vinh bước vào lớp, tay cầm xấp phiếu đăng ký: "Những em nào báo danh Võ khoa, lập tức lên bục giảng nhận hồ sơ!"

Ngô Chí Hào là người đầu tiên sải bước tự tin bước lên. Sau hắn, chỉ có thêm hai học sinh khác là Dương Kiến và Chu Bân — đều là những con em gia đình khá giả trong lớp. Cả lớp hơn bốn mươi học sinh, chỉ có đúng ba người dám bước lên.

Thầy Lưu gật đầu nhìn ba người: "Tốt lắm, còn em nào nữa không?"

Cả lớp im phăng phắc. Mọi người đều biết, một vạn tệ lệ phí thi không phải trò đùa, không có thực lực mà đâm đầu vào chỉ có mất trắng.

Đúng lúc Lão Lưu chuẩn bị cất xấp hồ sơ đi, từ góc cuối lớp, một bóng người thong thả đứng dậy.

"Thầy ơi, cho em xin một bản!"

Giọng nói vang lên rõ ràng, dứt khoát.

Toàn bộ lớp học trong nháy mắt rơi vào tĩnh lặng tuyệt đối. Mọi ánh mắt đồng loạt đổ dồn về phía cuối lớp.

Phương Bình!

Trần Phàm ngồi bên cạnh hoảng hốt kéo mạnh vạt áo Phương Bình: "Phương Bình! Mày điên rồi à?! Mau ngồi xuống!"

Ngô Chí Hào quay đầu lại nhìn thấy Phương Bình, khóe môi khẽ nhếch lên một nụ cười giễu cợt: "Phương Bình, cậu có biết đơn này là đơn gì không? Đơn báo danh Võ khoa đấy! Lệ phí một vạn tệ, không hoàn lại đâu!"

Dương Kiến cũng cười khẩy phụ họa: "Đúng đấy Phương Bình, nhà cậu hoàn cảnh thế nào cả lớp ai chẳng biết. Đừng có thấy người ta ăn khoai cũng vác mai đi đào, một vạn tệ để bố mẹ cậu mua đồ ăn bồi dưỡng không tốt hơn sao?"

Phương Bình căn bản không thèm liếc nhìn hai kẻ kia lấy một cái. Hắn bước từng bước vững chãi lên bục giảng, ánh mắt bình tĩnh nhìn thẳng vào thầy Lưu Thành Vinh:

"Thầy Lưu, em muốn đăng ký thi Võ khoa."

Lão Lưu nhìn chằm chằm vào Phương Bình. Trong ấn tượng của ông, Phương Bình là một học sinh học lực trung bình khá, tính cách hướng nội, gia cảnh bình thường. 

"Phương Bình, em đã bàn bạc kỹ với bố mẹ chưa?" Lão Lưu nghiêm túc hỏi: "Một vạn tệ này nếu thi trượt sẽ mất trắng, nhà trường và Cục Giáo Dục không chịu trách nhiệm đâu."

"Bố mẹ em đã đồng ý rồi ạ." Phương Bình đáp ngắn gọn, kiên định.

Nhìn thấy ánh mắt trong veo nhưng kiên định như đá tảng của Phương Bình, Lão Lưu khẽ gật đầu, rút một tờ đơn đưa cho hắn: "Cầm lấy, điền đầy đủ thông tin, chiều nay nộp lại cho thầy kèm theo lệ phí!"

"Cảm ơn thầy!" 

Phương Bình cầm lấy tờ đơn quay về chỗ ngồi. 

Sau lưng hắn, tiếng xì xào bàn tán của đám bạn học nổi lên như ong vỡ tổ. Có kẻ ngạc nhiên, có kẻ lắc đầu tiếc nuối, nhưng nhiều nhất vẫn là những ánh mắt chế giễu, chờ xem kịch vui của một kẻ nghèo thích học đòi làm sang.

Phương Bình ngồi xuống bàn, khóe môi nở một nụ cười lạnh lùng.

Chế giễu? Khinh thường? 

Cứ việc cười đi. Chờ đến ngày khảo thí khí huyết, ta sẽ cho tất cả các ngươi biết thế nào là chấn động thế gian!
"""
    },
    {
        "index": 7,
        "title_cn": "第七章 一万块与温暖家庭",
        "title_vi": "Chương 7: 1 Vạn Tệ Lệ Phí & Gia Đình Ấm Áp",
        "content_vi": """Chiều hôm đó, giờ ra chơi tiết thứ hai.

Bảo vệ trường Trung học Số 1 gọi với lên tầng ba: "Phương Bình lớp 12 ban 4, có phụ huynh tìm!"

Phương Bình vội vã chạy xuống sân trường. 

Dưới bóng râm của cây bàng cổ thụ gần cổng bảo vệ, Phương Danh Vinh đang đứng đó. Người cha mặc bộ quần áo bảo hộ lao động màu xám tro bạc màu của xưởng gốm sứ, trên lưng áo còn loang lổ vết bụi đất. Ông đứng co ro, hai bàn tay thô ráp xoa vào nhau vẻ lúng túng khi thấy các học sinh và thầy cô qua lại.

"Bố!" Phương Bình chạy tới gọi to.

Thấy con trai, gương mặt sạm nắng của Phương Danh Vinh giãn ra nụ cười ấm áp: "Bình nhi, tan học rồi à?"

Ông nhìn quanh một vòng, sau đó cẩn thận móc từ sâu trong túi áo khoác trong cùng ra một bọc vải đen được bọc nhiều lớp báo cũ dày cộp.

"Bố..." Phương Bình nhìn bọc tiền, lồng ngực thắt lại.

Phương Danh Vinh đưa bọc tiền vào tay Phương Bình, giọng nói trầm thấp nhưng đầy kiên quyết: 

"Trong này đủ đúng một vạn tệ. Buổi sáng bố đã đến ngân hàng rút toàn bộ tiền tiết kiệm được tám ngàn, còn thiếu hai ngàn bố vừa chạy sang xưởng vay trước tiền lương của quản đốc. Toàn bộ tiền mới, con cầm lấy nộp cho thầy giáo!"

Cầm bọc tiền trên tay, Phương Bình cảm thấy nó nặng tựa ngàn cân. 

Tám ngàn tiền tiết kiệm tích cóp bao năm trời, cộng thêm hai ngàn vay mượn muối mặt... Đây là toàn bộ gia sản, là mồ hôi và lòng tự trọng của người cha này đặt cược vào tương lai của hắn!

"Bố yên tâm!" Phương Bình ngẩng đầu, từng chữ từng câu như khắc sâu vào linh hồn: "Con nhất định sẽ không làm bố mẹ thất vọng! Con nhất định sẽ đỗ Võ khoa!"

Phương Danh Vinh vỗ mạnh lên vai con trai, ánh mắt tràn đầy vẻ tự hào: "Tốt! Bố tin con trai bố! Thôi con mau vào nộp đi, bố phải quay lại xưởng làm ca chiều kẻo bị trừ công."

Nói xong, người đàn ông ấy vẫy tay rồi vội vã đạp chiếc xe đạp cọc cạch rời đi, bóng lưng gầy gò khuất dần sau dòng người trên phố.

Phương Bình hít một hơi thật sâu, hai bàn tay siết chặt bọc tiền.

"Ong——!"

Một âm thanh thanh thúy quen thuộc vang lên trong thức hải hắn!

Bảng huỳnh quang tự động bật mở, ánh sáng rực rỡ chưa từng có:
【Phát hiện tài sản thuộc quyền sở hữu của túc chủ: 10.000 tệ!】
【Điểm Tài Phú tăng vọt: 68 + 10.000 = 10.068 điểm!】

Phương Bình thở phào một hơi nhẹ nhõm. Quả đúng như quy tắc của hệ thống: Chỉ cần số tiền này danh chính ngôn thuận thuộc về hắn, hệ thống sẽ lập tức quy đổi thành điểm Tài Phú! Dù lát nữa hắn đem một vạn tệ này nộp cho nhà trường thì 10.000 điểm tài phú trong hệ thống vẫn thuộc về hắn vĩnh viễn!

"Hệ thống, chuyển hóa 10.000 điểm Tài Phú! Tăng toàn bộ vào Khí Huyết!"

Phương Bình không ngần ngại ra lệnh trong đầu.

"Oanh!"

Trong nháy mắt, một tiếng gầm gừ như sấm sét nổ vang trong cơ thể hắn! 

Một luồng khí nóng cuồn cuộn mãnh liệt gấp mười lần đêm qua từ đan điền bộc phát, tựa như một dòng sông nham thạch sôi trào cuốn phăng mọi mệt mỏi trong kinh mạch. Tim hắn đập thình thịch như động cơ phản lực, máu trong huyết quản chảy xiết với tốc độ kinh hoàng!

Bên ngoài thân thể Phương Bình, làn da hắn ửng đỏ như tôm luộc, lỗ chân lông bốc lên một làn sương trắng mờ ảo do nhiệt độ cơ thể tăng vọt!

- Khí Huyết: 111 Ka -> 112 Ka -> 113 Ka... 
- Khí Huyết nhảy vọt lên: 121 Ka / 121 Ka!
- Tinh Thần: 105 Hz
- Tài Phú: 68 điểm!

Phương Bình thở ra một ngụm trọc khí nóng rực. 

121 Ka!

Hắn mở to hai mắt, cảm nhận một luồng sức mạnh dồi dào vô tận đang cuộn trào trong từng thớ cơ bắp. Cả người hắn nhẹ bẫng, thị lực và thính giác sắc bén gấp bội, tiếng gió thổi qua kẽ lá cách xa ba mươi mét hắn cũng nghe thấy rõ mồn một!

Ngô Chí Hào uống đan dược cả năm mới đạt 115 Ka? 

Mà hiện tại, Phương Bình hắn chưa đầy một ngày đã đạt tới 121 Ka! Vượt xa tiêu chuẩn sơ tuyển của bất kỳ trường đại học Võ khoa nào!

Hắn mỉm cười, xoay người sải bước hướng về phía phòng làm việc của giáo viên chủ nhiệm.
"""
    },
    {
        "index": 8,
        "title_cn": "第八章 体检测试与陈凡震惊",
        "title_vi": "Chương 8: Kiểm Tra Thể Chất Tại Trường & Trần Phàm Kinh Ngạc",
        "content_vi": """Ba ngày sau khi hoàn tất thủ tục báo danh, Cục Giáo Dục và Cục Võ Đạo huyện Dương Thành phối hợp tổ chức buổi "Kiểm tra Khí Huyết sơ bộ" cho toàn bộ thí sinh đăng ký thi Võ khoa của trường Trung học Số 1.

Buổi kiểm tra diễn ra tại Nhà thi đấu Thể thao đa năng của trường. 

Từ sáng sớm, hơn ba trăm học sinh lớp 12 của toàn trường đã có mặt đông đủ, xếp hàng ngay ngắn. Phía trước khán đài, một cỗ máy hình trụ bằng hợp kim màu bạc cao gần hai mét được đặt trang trọng — đó chính là Máy Đo Khí Huyết thế hệ mới do Bộ Võ Đạo đặc cấp!

Trên khán đài, Hiệu trưởng Tôn Chính Đức cùng các giáo viên thể dục và hai vị Võ giả thực thụ mặc đồng phục Cục Võ Đạo đang ngồi giám sát.

"Lớp 12 ban 1: Trương Cường, bước lên!" Giọng thầy giám khảo vang lên qua loa phóng thanh.

Một nam sinh run rẩy bước vào vòng cảm ứng kim loại của máy đo, nắm chặt hai tay cầm truyền dẫn.

Máy đo phát ra tiếng rè rè, cột đèn huỳnh quang màu đỏ từ từ dâng lên:
"Tích! Khí huyết: 104 Ka! Không đạt tiêu chuẩn khuyến nghị!"

Nam sinh kia mặt mày tái mét, thất vọng cúi đầu bước xuống. 

"Lớp 12 ban 2: Lý Duyệt! Khí huyết: 108 Ka! Tạm đạt!"
"Lớp 12 ban 3: Vương Đằng! Khí huyết: 101 Ka! Không đạt!"

Liên tiếp hàng chục học sinh bước lên nhưng phần lớn đều chỉ quanh quẩn ở mức 100 đến 105 Ka. Tiêu chuẩn sơ tuyển chính thức hàng năm thường dao động từ 110 đến 115 Ka. Với mức khí huyết dưới 110 Ka, cơ hội đỗ gần như bằng không!

Bầu không khí trong nhà thi đấu càng lúc càng trở nên căng thẳng ngột ngạt.

"Lớp 12 ban 4: Ngô Chí Hào!"

Nghe xướng tên, Ngô Chí Hào chỉnh lại cổ áo thể thao, ưỡn ngực ngẩng cao đầu bước lên khán đài trước những ánh mắt ngưỡng mộ của học sinh toàn trường.

Hắn đứng vững theo tư thế trung bình tấn, vận chuyển hô hấp pháp gia truyền, hai tay nắm chặt cần cảm ứng.

"Oanh!"

Cột đèn huỳnh quang lập tức vọt thẳng lên cao, ánh sáng xanh lục chói mắt bừng nở:
"Bíp bíp bíp! Khí huyết: 116 Ka! Đạt tiêu chuẩn xuất sắc!"

"Ồ——!" Toàn bộ nhà thi đấu bùng nổ một tràng pháo tay và những tiếng reo hò thán phục.

Hiệu trưởng Tôn trên khán đài khẽ mỉm cười gật đầu: "116 Ka, hạt giống tốt! Nếu duy trì đà này đến ngày thi chính thức, em ấy có hy vọng rất lớn đỗ vào Đại học Nam Giang Võ Khoa!"

Ngô Chí Hào đắc ý bước xuống, ánh mắt lướt qua hàng ngũ lớp 12 ban 4, dừng lại trên người Phương Bình với vẻ khiêu khích rõ rệt.

"Lớp 12 ban 4: Phương Bình!"

Tiếng loa vừa dứt, cả nhà thi đấu lại xôn xao.

"Phương Bình là ai thế?"
"Nghe bảo là một học sinh nghèo lớp ban 4, chẳng có bối cảnh gì cũng liều mạng nộp một vạn tệ đi thi!"
"Chắc lại là loại học sinh không biết lượng sức mình, khí huyết cao lắm cũng chỉ tầm 100 Ka là cùng!"

Trần Phàm đứng bên cạnh nắm chặt tay Phương Bình, lòng bàn tay ướt đẫm mồ hôi: "Phương Bình... cố lên mày! Đừng để bọn nó coi thường!"

Phương Bình mỉm cười vỗ vai bạn thân: "Yên tâm đi."

Hắn bình thản bước ra khỏi hàng, từng bước vững chãi tiến lên bục kiểm tra. Dưới ánh đèn sáng rực của nhà thi đấu, bóng lưng hắn thẳng tắp như ngọn thương cắm sâu vào lòng đất.
"""
    },
    {
        "index": 9,
        "title_cn": "第九章 气血破百二！震惊全场",
        "title_vi": "Chương 9: Khí Huyết Vượt Trăm Hai! Chấn Động Toàn Trường",
        "content_vi": """Bước vào vòng tròn cảm ứng kim loại, Phương Bình đặt hai bàn tay lên hai thanh trụ truyền dẫn bằng hợp kim lạnh ngắt.

Vị giám khảo của Cục Võ Đạo nhìn Phương Bình một cái, thấy thiếu niên này thần sắc bình tĩnh lạ thường, không hề có chút căng thẳng hay run rẩy như những học sinh trước, trong lòng không khỏi có chút tò mò.

"Chuẩn bị xong chưa?"

"Dạ xong rồi ạ." Phương Bình gật đầu.

"Bắt đầu đo!"

Giám khảo nhấn nút khởi động.

Trong khoảnh khắc ấy, Phương Bình hít một hơi thật dài. Trong lồng ngực hắn, luồng Khí Huyết hùng hậu 121 Ka tích lũy bấy lâu như một con rồng ngủ say bỗng nhiên bừng tỉnh!

"Oanh!"

Huyết mạch trong cơ thể Phương Bình sôi trào gầm thét! Một cỗ khí tràng vô hình mà sắc bén đột ngột phát tán từ người hắn. 

Máy đo Khí Huyết rung chuyển kịch liệt! Cột đèn huỳnh quang bên sườn máy không hề tăng từng chút một như những người khác, mà giống như một cột lửa phun trào, vọt thẳng đứng lên đỉnh!

100... 105... 110... 115!

Qua mốc 115 của Ngô Chí Hào trong chớp mắt!

Nhưng nó vẫn chưa dừng lại!

118... 120... 121... 122 Ka!

"TÍCH TÍCH TÍCH TÍCH——!"

Còi báo động của máy đo vang lên dồn dập, toàn bộ các dãy đèn xanh đỏ trên thân máy điên cuồng nhấp nháy, màn hình tinh thể lỏng hiện lên con số đỏ chót to tướng:

【Khí Huyết: 122 Ka! Thể Phách: Đỉnh cấp!】

Tiếng còi máy đo vang dội khắp nhà thi đấu đa năng.

Thế nhưng, toàn bộ hội trường rộng lớn chứa hàng trăm người lúc này lại rơi vào một sự im lặng chết chóc!

Không có tiếng reo hò, không có tiếng vỗ tay. 

Chỉ có những cặp mắt trợn tròn hết cỡ, những cái miệng há hốc không khép lại nổi!

"Cạch!" 

Chiếc cốc trà trên tay Hiệu trưởng Tôn Chính Đức rơi thẳng xuống bàn, nước trà bắn tung tóe nhưng ông ta dường như không hề hay biết. Cả người ông ta bật dậy khỏi ghế như một chiếc lò xo, hai mắt gắt gao nhìn chằm chằm vào con số 122 Ka trên màn hình!

"1... 122 Ka?!"

Hai vị Võ giả của Cục Võ Đạo huyện cũng giật nảy mình đứng phắt dậy, mặt mũi tràn đầy vẻ kinh hãi: 

"Làm sao có thể?! Một học sinh trung học bình thường, chưa từng ghi nhận sử dụng qua Dưỡng Khí Đan, mà Khí Huyết đạt tới 122 Ka?!"

"Thiên sinh Thần lực! Đây là dị bẩm thiên phú, Khí Huyết tự sinh của kỳ tài võ đạo!"

Bên dưới khán đài, Ngô Chí Hào toàn thân cứng đờ như hóa đá. Nụ cười ngạo nghễ trên mặt hắn vỡ vụn thành từng mảnh, sắc mặt từ đỏ chuyển sang trắng bệch, rồi từ trắng bệch chuyển sang xám như tro tàn:

"Không thể nào... Tuyệt đối không thể nào! Hắn là một tên nhà nghèo... làm sao khí huyết có thể cao hơn ta?!"

Còn Trần Phàm thì đứng ngây như phỗng giữa đám đông, sau đó bất thình lình nhảy cẫng lên ba thước, gào thét như phát cuồng: 

"Phương Bình! Mẹ kiếp, 122 Ka! Phương Bình là anh em của tao đấy! Ha ha ha ha!"

Trên bục kiểm tra, Phương Bình từ từ buông tay khỏi thanh cảm ứng. 

Hắn thở ra một hơi dài, phong thái thong dong tự tại. Con số 122 Ka này còn cao hơn 1 Ka so với hiển thị trên bảng thuộc tính tối qua, hẳn là do thể chất tự nhiên của hắn sau khi thích ứng với khí huyết đã tự động rèn luyện tăng thêm một chút.

Vị giám khảo run rẩy cầm bút ghi vào bảng vàng danh dự của trường: 
"Lớp 12 ban 4: Phương Bình — Khí Huyết 122 Ka! Xếp thứ nhất toàn trường Trung học Số 1 Dương Thành!"

Phương Bình khẽ cúi đầu chào các thầy cô rồi quay lưng bước xuống. 

Lúc này, toàn bộ ánh mắt nhìn về phía hắn đã hoàn toàn thay đổi. Không còn sự khinh thường, không còn sự chế giễu. Thay vào đó là sự kính sợ, ngưỡng mộ và tôn sùng tột bực dành cho một thiên tài võ đạo xuất thế!
"""
    },
    {
        "index": 10,
        "title_cn": "第十章 目标魔都武大！地窟揭秘",
        "title_vi": "Chương 10: Mục Tiêu Ma Đô Võ Đại & Bức Màn Địa Quật Hé Lộ",
        "content_vi": """Sau buổi kiểm tra chấn động toàn trường, cái tên Phương Bình trong một đêm đã trở thành truyền kỳ của toàn thể giáo viên và học sinh huyện Dương Thành.

Tại phòng hiệu trưởng, Hiệu trưởng Tôn Chính Đức đích thân rót trà cho Phương Bình, trên mặt cười rạng rỡ như hoa nở:

"Phương Bình! Em là niềm tự hào lớn nhất của trường Trung học Số 1 Dương Thành trong suốt mười năm qua! Với chỉ số 122 Ka này, trường đã quyết định đặc cách trao cho em Quỹ Khuyến học Võ Đạo trị giá 50.000 tệ tiền mặt để bồi dưỡng dinh dưỡng chuẩn bị cho kỳ thi chính thức!"

Năm vạn tệ tiền mặt!

Phương Bình nhận lấy chiếc phong bì dày cộp, trong lòng mừng thầm. Có số tiền này, hắn không những trả hết nợ cho cha mẹ mà điểm Tài Phú trên hệ thống chắc chắn sẽ lại tăng vọt lên một tầm cao mới!

"Thầy Hiệu trưởng, em muốn hỏi một chuyện." Phương Bình ngẩng đầu hỏi: "Với thành tích này của em, em có cơ hội thi vào hai trường võ đạo đỉnh tiêm nhất cả nước không?"

Hiệu trưởng Tôn nghe vậy thì ánh mắt sáng quắc: "Em muốn nói tới Ma Đô Võ Khoa Đại Học (Ma Đô Võ Đại) và Kinh Đô Võ Khoa Đại Học (Kinh Đô Võ Đại)?"

"Đúng vậy ạ!"

"Có hy vọng! Rất lớn là đằng khác!" Hiệu trưởng Tôn kích động đập bàn: "Đó là hai lò đào tạo Tông Sư hàng đầu của Hoa Hạ chúng ta! Sinh viên tốt nghiệp ở đó ra trường đều là rồng phượng giữa loài người! Tuy nhiên..."

Nói đến đây, nét mặt Hiệu trưởng Tôn bỗng chùng xuống, giọng nói trở nên trầm trọng và nghiêm túc chưa từng thấy:

"Phương Bình, em có biết vì sao đất nước ta lại dốc toàn lực bồi dưỡng Võ giả, dành cho Võ giả địa vị và tài nguyên tối cao như vậy không?"

Phương Bình lắc đầu. Đây cũng chính là điều hắn luôn thắc mắc từ khi trọng sinh tới nay.

Hiệu trưởng Tôn đứng dậy, đi tới bên cửa sổ, nhìn về phía đường chân trời xa xăm, giọng nói trầm như sấm rền:

"Bởi vì... thế giới này không hề thái bình như vẻ bề ngoài của nó!"

"Dưới lòng đất sâu hàng ngàn mét của những thành phố lớn trên thế giới, tồn tại những cánh cổng không gian dẫn tới một thế giới khác. Chúng ta gọi nơi đó là: ĐỊA QUẬT!"

"Địa Quật?!" Phương Bình giật mình lẩm bẩm.

"Đúng vậy! Trong Địa Quật có vô số quái vật hung tàn, có dị tộc cường đại ngút trời, luôn thèm khát xé toạc phòng tuyến để tràn lên mặt đất tàn sát nhân loại! Sự phồn hoa, yên bình của hàng tỷ con người trên mặt đất hiện nay... đều là nhờ máu và xương trắng của hàng vạn Võ giả, các Tông Sư tiền tuyến đang ngày đêm tử chiến dưới Địa Quật đổi lấy!"

"Võ giả, hưởng thụ đặc quyền tối cao của nhân loại, thì cũng phải gánh vác trách nhiệm bảo vệ giống nòi! Một khi bước chân vào Võ đại, các em không chỉ học võ thuật, mà là học cách giết địch, học cách sinh tồn giữa biển máu!"

Từng lời nói của Hiệu trưởng Tôn như búa tạ giáng mạnh vào tâm trí Phương Bình.

Địa Quật... Dị tộc... Tử chiến bảo vệ nhân loại!

Đến lúc này, Phương Bình mới thực sự hiểu được thế giới Cao Võ này tàn khốc và bi tráng đến nhường nào. Đây không chỉ là nơi để hắn làm giàu hay hưởng thụ vinh hoa phú quý. Nếu nhân loại diệt vong, gia đình hắn, cha mẹ hắn, cô em gái nhỏ Phương Viên của hắn... cũng sẽ bị quái vật Địa Quật nghiền nát thành tro bụi!

Phương Bình siết chặt nắm tay, trong lòng bùng lên một ngọn lửa ý chí ngập trời.

Hắn có Hệ thống Tài Phú! 
Hắn có thể vô hạn tăng tiến Khí Huyết và Tinh Thần!

"Ma Đô Võ Đại... Ta nhất định sẽ vào đó!" 

Phương Bình ngẩng cao đầu, ánh mắt rực sáng như tinh tú: "Địa Quật thì đã sao? Dị tộc thì đã sao? Kiếp này có Phương Bình ta ở đây, ta sẽ kiếm sạch tài phú thiên hạ, một kiếm trấn áp Địa Quật, bảo vệ gia đình, giữ vững thái bình cho nhân loại!"
"""
    }
]

def update_chapters():
    conn = sqlite3.connect('data/novels.db', timeout=60.0)
    cursor = conn.cursor()
    
    # Đảm bảo novel_id = 61 có tổng số chương hiển thị đúng
    cursor.execute("""
        UPDATE novels 
        SET total_chapters = 1432, 
            description = 'Phương Bình trọng sinh vào thế giới võ giả chí thượng, nơi nhân loại đang phải chiến đấu ngầm với Địa Quật quái vật dưới lòng đất. Với hệ thống kiếm tiền tăng khí huyết, Phương Bình điên cuồng làm giàu để bảo vệ nhân tộc!'
        WHERE id = ?
    """, (NOVEL_ID,))
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    updated_count = 0
    for ch in CHAPTERS_DATA:
        idx = ch["index"]
        title_cn = ch["title_cn"]
        title_vi = ch["title_vi"]
        content_vi = ch["content_vi"].strip()
        
        # Kiểm tra xem chương đã tồn tại chưa
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
    # Checkpoint WAL để ghi thẳng vào file novels.db
    cursor.execute("PRAGMA wal_checkpoint(FULL);")
    conn.close()
    print(f"\n[HOÀN TẤT] Đã cập nhật thành công {updated_count} chương cho truyện Toàn Cầu Cao Võ (ID: {NOVEL_ID})")

if __name__ == '__main__':
    update_chapters()
