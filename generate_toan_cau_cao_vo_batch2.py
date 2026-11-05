# -*- coding: utf-8 -*-
"""
Script dịch trực tiếp và cập nhật Chương 11 đến 20 của siêu phẩm Toàn Cầu Cao Võ (ID: 61)
Tác giả: Lão Ưng Cật Tiểu Kê (老鹰吃小鸡)
Biên dịch & Chuyển ngữ văn phong cao võ: Antigravity.
"""

import sqlite3
import datetime

NOVEL_ID = 61

CHAPTERS_BATCH2 = [
    {
        "index": 11,
        "title_cn": "第十一章 五万奖金与扬眉吐气",
        "title_vi": "Chương 11: 5 Vạn Tiền Thưởng & Nở Mày Nở Mặt",
        "content_vi": """Chiều muộn hôm ấy, Phương Bình cầm chiếc phong bì dày cộp chứa đúng năm vạn tệ tiền mặt bước vào con ngõ Liễu Thụ.

Vừa bước đến chân cầu thang khu tập thể, hắn đã nghe thấy tiếng trò chuyện rôm rả của các bà các cô hàng xóm. Tin tức Phương Bình đo Khí Huyết đạt 122 Ka, xếp hạng nhất toàn trường Trung học Số 1 Dương Thành đã lan truyền với tốc độ chóng mặt khắp cả khu công nhân xưởng gốm sứ!

"Ơ kìa, Bình nhi về rồi đấy à!"
"Trời đất ơi, đứa nhỏ này nhìn tướng mạo khôi ngô tuấn tú, đúng là rồng phượng giấu mình!"
"Danh Vinh với Ngọc Anh kiếp này tu được phúc lớn rồi, con trai sắp thành Võ giả đại nhân rồi đấy!"

Những lời khen ngợi tới tấp bay tới. Các bác hàng xóm ngày thường vốn hay xét nét, nay ai nấy đều tươi cười niềm nở, ánh mắt nhìn Phương Bình tràn đầy vẻ kính nể và ghen tị.

Phương Bình mỉm cười gật đầu chào hỏi lễ phép rồi bước nhanh lên lầu ba.

Vừa mở cửa, hắn đã thấy cha mẹ đang ngồi chết trân trên ghế gỗ phòng khách. Phương Danh Vinh hai mắt đỏ hoe, khóe mắt còn vương giọt lệ chưa khô, trong khi Lý Ngọc Anh thì liên tục lấy vạt áo lau nước mắt vì quá đỗi vui mừng.

"Bình nhi! Con... con thật sự đo được 122 Ka sao?" Giọng Phương Danh Vinh run rẩy, bờ vai gầy gò khẽ lay động.

"Bố, mẹ, đây là năm vạn tệ tiền thưởng nhà trường đặc cách thưởng nóng cho con!" 

Phương Bình đặt chiếc phong bì lên bàn, mở tung ra. Từng thếp tiền một trăm tệ đỏ rực, thơm mùi mực in đập vào mắt hai vợ chồng nghèo.

Lý Ngọc Anh hít một hơi sâu, hai tay run run chạm vào xấp tiền: "Trời Phật phù hộ... Nhà họ Phương ta cuối cùng cũng có ngày nở mày nở mặt rồi!"

Phương Bình mỉm cười nói: "Bố, sáng mai bố mang hai ngàn tệ trả lại cho quản đốc xưởng gốm ngay nhé. Còn lại bốn mươi tám ngàn tệ bố mẹ cứ cất vào ngân hàng gửi tiết kiệm. Sau này con đi học Võ đại, chi phí nhà nước và nhà trường sẽ bao trọn gói, bố mẹ không cần phải lo lắng một đồng nào nữa!"

Cô em gái Phương Viên từ góc phòng lao ra như một chú cún con, ôm chầm lấy hông Phương Bình: "Anh! Anh giỏi quá! Mai anh mua cho con gấu bông to đùng nhé! Cả kẹo sữa nữa!"

Phương Bình cốc nhẹ vào đầu cô bé một cái, cười ha hả: "Được! Cho mày ăn đến khi sâu răng thì thôi!"

Trong đầu hắn, bảng hệ thống khẽ nhấp nháy:
【Tài Phú: 50.068 điểm!】

Dù số tiền này hắn đưa cho gia đình chi dùng, nhưng quyền định đoạt ban đầu thuộc về hắn, điểm Tài Phú trên hệ thống vẫn ghi nhận trọn vẹn năm vạn điểm!

Cả căn nhà ngập tràn tiếng cười rộn rã, xua tan đi sự ảm đạm, túng quẫn bấy lâu nay.
"""
    },
    {
        "index": 12,
        "title_cn": "第十二章 教育局建档与武科大考",
        "title_vi": "Chương 12: Đăng Ký Hồ Sơ Tại Cục Giáo Dục & Quy Chế Đại Khảo",
        "content_vi": """Sáng ngày hôm sau, đích thân thầy chủ nhiệm Lưu Thành Vinh dẫn Phương Bình cùng ba học sinh đạt chuẩn của trường đến Cục Giáo Dục huyện Dương Thành để hoàn thiện hồ sơ dự thi Võ khoa toàn quốc.

Tòa nhà Cục Giáo Dục huyện hôm nay đông nghẹt người. Các trường trung học từ khắp các thị trấn lân cận đều đổ về. 

Khi đoàn của trường Trung học Số 1 bước vào sảnh lớn, cán bộ tiếp nhận hồ sơ vừa nhìn thấy tên Phương Bình trên danh sách đã lập tức đứng dậy, tươi cười đon đả:

"Cậu là Phương Bình học sinh đạt 122 Ka đúng không? Mau vào phòng VIP bên này lấy mẫu vân tay và trắc nghiệm điện não đồ!"

Thái độ ân cần, cung kính của cán bộ tiếp nhận khiến Ngô Chí Hào đi phía sau chỉ biết cắn chặt môi, trong lòng dâng lên một cỗ chua xót khôn tả. 

Trong phòng làm việc riêng, vị trưởng ban khảo thí niềm nở đưa cho Phương Bình cuốn 《Sổ Tay Thí Sinh Võ Khoa Toàn Quốc Năm 2008》, ân cần căn dặn:

"Phương Bình, kỳ thi Võ khoa toàn quốc chia làm bốn ải lớn:"

"Ải thứ nhất: Sát hạch Thể Phách và Khí Huyết. Với mức 122 Ka của em hiện tại, ải này coi như chắc chắn đạt điểm tuyệt đối!"

"Ải thứ hai: Khảo thí Chuyên Nghiệp. Kiểm tra độ dẻo dai cơ bắp, tốc độ phản xạ thần kinh và sức bật của xương cốt."

"Ải thứ ba: Khảo thí Văn Hóa. Điểm thi văn hóa của thí sinh Võ khoa tuy thấp hơn thí sinh thông thường, nhưng vẫn phải vượt qua điểm sàn của Bộ Giáo Dục, không được lơ là!"

"Ải thứ tư: Khảo thí Thực Chiến và Phỏng Vấn! Đây là ải then chốt nhất để phân loại thí sinh vào các trường Đại học Võ khoa đỉnh tiêm như Ma Đô Võ Đại hay Kinh Đô Võ Đại!"

Phương Bình cẩn thận ghi nhớ từng lời chỉ dẫn. 

Hắn lật mở cuốn sổ tay. Trong đó ghi rõ cấp bậc của Võ giả:
Từ Nhất Phẩm đến Tam Phẩm gọi là Hạ Tam Phẩm; Tứ Phẩm đến Lục Phẩm gọi là Trung Tam Phẩm; Thất Phẩm trở lên được tôn xưng là Tông Sư, Cửu Phẩm là Tuyệt Đỉnh!

Muốn bước chân vào Nhất Phẩm Võ Giả, điều kiện tiên quyết là phải "Thối Cốt" — tôi luyện toàn bộ 206 mảnh xương trong cơ thể con người bằng Khí Huyết tinh thuần!

"Thối Cốt... hóa ra con đường Võ giả lại bắt đầu từ việc rèn xương luyện tủy!" Phương Bình nắm chặt cuốn sổ tay, ánh mắt bừng sáng khao khát.
"""
    },
    {
        "index": 13,
        "title_cn": "第十三章 淬骨法与武者之门",
        "title_vi": "Chương 13: Thối Cốt Pháp & Cánh Cửa Võ Giả",
        "content_vi": """Sau khi từ Cục Giáo Dục trở về, Phương Bình nhốt mình trong phòng ngủ, cẩn thận nghiên cứu phần phụ lục của cuốn Sổ Tay Võ Khoa: 《Thối Cốt Pháp Khái Luận》.

Theo tài liệu ghi chép:
Cơ thể người trưởng thành có tổng cộng 206 khối xương: Xương sọ gồm 29 khối, xương thân mình gồm 51 khối, và xương tứ chi gồm 126 khối.

Người bình thường khi khí huyết đạt tới ngưỡng 120 Ka trở lên, khí huyết sẽ bắt đầu tràn ra khỏi huyết quản, thẩm thấu vào màng xương. Lúc này, người luyện võ có thể dẫn dắt khí huyết tiến hành rèn luyện màng xương, xua tan tạp chất, biến xương cốt trở nên cứng cáp như thép nguội — quá trình này gọi là "Thối Cốt".

Người bình thường tu luyện Thối Cốt Pháp vô cùng gian nan. Mỗi lần dẫn khí huyết cọ rửa màng xương đều đau đớn như bị ngàn mũi kim châm, hơn nữa khí huyết tiêu hao cực nhanh. Một học sinh con nhà giàu có điều kiện mỗi ngày cũng chỉ dám thối cốt nửa tiếng, sau đó phải uống Dưỡng Khí Đan bồi bổ lại khí huyết đã cạn kiệt, nếu không sẽ bị nội thương suy kiệt!

"Nhưng mình thì khác!"

Phương Bình nhìn vào bảng thuộc tính trong đầu:
- Khí Huyết: 122 Ka / 122 Ka
- Tinh Thần: 105 Hz / 105 Hz
- Tài Phú: 50.068 điểm!

Hắn có tới hơn năm vạn điểm Tài Phú dự trữ! 

Người khác hết khí huyết thì phải dừng lại uống thuốc, chờ đợi cơ thể hồi phục suốt mấy ngày. Còn hắn? Chỉ cần tiêu hao điểm Tài Phú, khí huyết lập tức được lấp đầy tức thì trong một cái chớp mắt!

"Thử nghiệm một chút xem sao!"

Phương Bình ngồi xếp bằng trên giường theo khẩu quyết của Thối Cốt Pháp, hít sâu thở đều, tập trung ý niệm điều động luồng Khí Huyết dồi dào trong đan điền chảy xuôi xuống hai chi dưới.

"Tê tê tê..."

Khí huyết đỏ rực cuồn cuộn chảy xuống bắp chân, bắt đầu thẩm thấu qua lớp cơ bắp, chạm tới màng xương ống chân. 

Một cảm giác nhói buốt tê rần truyền đến, giống như có đàn kiến lửa đang gặm nhấm bề mặt xương. 

Phương Bình cắn chặt răng không hề rên rỉ nửa tiếng. Hắn cảm nhận được màng xương ống chân dưới sự gột rửa của Khí Huyết đang phát sinh biến hóa vi diệu, từng hạt tạp chất màu xám bị đẩy lùi, xương cốt trở nên đặc quánh và trắng sáng hơn!

Chỉ sau mười phút, chỉ số Khí Huyết trên bảng thuộc tính đã sụt giảm từ 122 Ka xuống còn 112 Ka!

Cảm giác kiệt sức và đói cồn cào lập tức bủa vây lấy toàn thân Phương Bình.

"Hồi phục Khí Huyết!" Phương Bình quát khẽ trong tâm trí.

【Tiêu hao 1.000 điểm Tài Phú!】
【Khí Huyết lập tức khôi phục: 122 Ka / 122 Ka!】

"Oanh!"

Một dòng nhiệt ấm áp vô tận tuôn trào, cảm giác mệt mỏi tiêu tan sạch sẽ không còn một dấu vết! 

Phương Bình mở bừng mắt, nở nụ cười ngạo nghễ:
"Ha ha ha! Quả nhiên là bật hack! Tu luyện kiểu này thì tốc độ của mình sẽ gấp mười lần, trăm lần bất kỳ thiên tài nào trên đời!"
"""
    },
    {
        "index": 14,
        "title_cn": "第十四章 丹药与无瑕武道",
        "title_vi": "Chương 14: Đan Dược & Con Đường Võ Đạo Không Tì Vết",
        "content_vi": """Để chuẩn bị tốt nhất cho kỳ thi, Phương Bình quyết định tìm hiểu sâu hơn về thị trường đan dược võ đạo.

Chiều hôm đó, hắn cùng Trần Phàm ghé qua tiệm thuốc lớn nhất trung tâm huyện Dương Thành — 《Bách Thảo Đường Võ Dược Các》. Đây là nơi duy nhất tại huyện được Cục Quản Lý Dược Phẩm Quốc Gia cấp phép bán các loại đan dược bổ trợ võ đạo sơ cấp.

Vừa bước vào tiệm, Phương Bình đã ngửi thấy mùi dược liệu thơm nồng nàn. Bên trong lồng kính bọc thép cường lực, những viên đan dược tròn xoe, lấp lánh ánh quang được trưng bày trang trọng kèm bảng giá niêm yết:

- Khí Huyết Đan (Hạ phẩm): 10.000 tệ / viên. (Tác dụng: Hồi phục và bồi dưỡng khí huyết).
- Dưỡng Khí Đan (Trung phẩm): 30.000 tệ / viên. (Tác dụng: Ôn dưỡng kinh mạch, hỗ trợ ngưng tụ khí huyết).
- Thối Cốt Đan: 50.000 tệ / viên! (Tác dụng: Tăng tốc độ tôi luyện màng xương).

Nhìn vào những con số không dài dằng dặc, Trần Phàm bên cạnh há hốc mồm rụt cổ lại: 

"Mẹ ơi... một viên Thối Cốt Đan bằng cả căn nhà ở thị trấn mình rồi! Uống một viên này vào bụng chẳng khác nào nuốt vàng nuốt bạc!"

Phương Bình đứng quan sát kỹ càng những viên đan dược. Lúc này, hắn vô tình nghe thấy người bán thuốc lớn tuổi đang giải thích với một vị phụ huynh giàu có:

"Thưa ông, dù Dưỡng Khí Đan này rất tốt, nhưng thuốc có ba phần độc! Dù là đan dược thượng hạng thì vẫn chứa tàn dư tạp chất dược liệu. Học sinh mỗi tháng nhiều nhất chỉ được dùng hai viên, sau đó phải dừng lại để cơ thể tự đào thải đan độc suốt nửa tháng. Nếu tham lam uống dồn dập, đan độc tích tụ trong kinh mạch sẽ biến thành bế tắc, cả đời này đừng hòng mong đột phá Tông Sư!"

Lời nói của ông lão bán thuốc khiến Phương Bình chấn động tâm can.

Dùng đan dược... hóa ra có tác dụng phụ lớn đến như vậy!

Ngô Chí Hào và những công tử con nhà giàu từ bé cắn thuốc như ăn cơm bữa, bề ngoài khí huyết tăng nhanh, nhưng trong kinh mạch ắt hẳn đã tích tụ không ít cặn bã đan độc.

Mà hệ thống của Phương Bình thì sao?

Hệ thống dùng điểm Tài Phú trực tiếp chuyển hóa năng lượng thiên địa thuần khiết nhất để gia tăng Khí Huyết và Tinh Thần! Không có một chút tạp chất, không có bất kỳ đan độc nào, căn cơ vững chắc như bàn thạch ngàn năm!

"Đây mới chính là con đường Vô Hà Võ Đạo — hoàn mỹ không tì vết!" 

Phương Bình thầm nghĩ trong lòng, nụ cười càng thêm tự tin. Hắn quay sang kéo tay Trần Phàm: "Đi thôi, đồ ở đây không hợp với tao!"

"Không mua thật à? Mày đang có năm vạn tệ tiền thưởng mà!" Trần Phàm ngơ ngác hỏi.

"Năm vạn tệ này để dành làm việc lớn hơn, mua mấy viên thuốc này phí tiền lắm!" Phương Bình cười đáp, sải bước ra khỏi cửa hiệu.
"""
    },
    {
        "index": 15,
        "title_cn": "第十五章 王金洋归乡",
        "title_vi": "Chương 15: Vương Kim Dương Trở Về",
        "content_vi": """Hai tuần trước kỳ đại khảo, một tin tức kinh thiên động địa bùng nổ khắp huyện Dương Thành:

Vương Kim Dương trở về!

Vương Kim Dương là ai? 

Đó là huyền thoại sống của trường Trung học Số 1 Dương Thành! Khóa trước, hắn chỉ là một học sinh nghèo xuất thân từ một gia đình bình dân, nhưng bằng nghị lực phi thường đã thi đỗ vào Đại học Nam Giang Võ Khoa. 

Điều chấn động nhất là: Mới chỉ học năm thứ nhất tại Võ đại, Vương Kim Dương đã chính thức đột phá Nhất Phẩm Võ Giả, thậm chí nghe đồn đã đạt tới Nhất Phẩm Đỉnh Phong, một mình chém giết ba tên tội phạm truy nã võ đạo tại biên giới!

Một Nhất Phẩm Võ Giả bằng xương bằng thịt, đường đường chính chính trở về huyện thành nhỏ bé này!

Sáng hôm đó, toàn bộ ban giám hiệu trường Trung học Số 1 cùng lãnh đạo Cục Giáo Dục huyện đều có mặt tại cổng trường để nghênh đón.

Học sinh toàn trường đứng chật kín hai bên đường từ cổng chính kéo dài đến tận hội trường lớn.

Phương Bình cùng Trần Phàm đứng ở hàng đầu của lớp 12 ban 4. 

"Đến rồi! Vương học trưởng đến rồi!"

Một tiếng hô vang lên. Đám đông lập tức dạt sang hai bên.

Từ cổng trường, một thanh niên tầm mười chín, hai mươi tuổi chầm chậm bước vào. 

Hắn mặc một chiếc áo khoác gió màu đen đơn giản, quần jean sờn gối, vóc dáng không quá cao lớn nhưng từng bước chân bước đi đều vững vàng như núi thái sơn. Sau lưng hắn đeo một thanh trường đao bọc trong bao vải đen dài hơn một mét.

Khuôn mặt thanh niên góc cạnh rõ ràng, đôi mắt sắc lạnh như chim ưng nhìn thấu hồng trần. 

Đặc biệt nhất chính là cỗ khí tức vô hình tỏa ra từ người hắn — một cỗ huyết khí nồng nặc tựa như một lò lửa hừng hực cháy giữa trời đông giá rét! 

Bất cứ ai đứng cách hắn trong phạm vi năm mét đều cảm thấy khó thở, lồng ngực như bị một khối đá đè nặng!

"Đây... chính là khí tràng của một Võ giả thực thụ sao?!" Phương Bình nheo mắt lại, nhịp tim đập thình thịch.

Hắn có thể cảm nhận rõ ràng, khí huyết của Vương Kim Dương mạnh mẽ gấp bội so với những học sinh trung học ở đây. Đó là thứ khí huyết đã từng tắm trong máu tươi thực chiến, sắc bén và tràn ngập sát khí!

Đúng lúc Vương Kim Dương sải bước ngang qua hàng ngũ lớp 12 ban 4, bước chân của hắn đột ngột khựng lại.

Đôi mắt ưng sắc lạnh của Vương Kim Dương bất ngờ quay sang, xuyên qua đám đông, dừng lại ngay trên khuôn mặt của Phương Bình!
"""
    },
    {
        "index": 16,
        "title_cn": "第十六章 真正的武者之威",
        "title_vi": "Chương 16: Uy Áp Đích Thực Của Võ Giả",
        "content_vi": """Bị ánh mắt sắc như dao cạo của Vương Kim Dương khóa chặt, Trần Phàm đứng cạnh Phương Bình lập tức run rẩy, hai chân mềm nhũn suýt quỵ xuống đất.

Nhưng Phương Bình thì không. 

Ánh mắt Phương Bình trong veo, phẳng lặng như mặt hồ không một gợn sóng. Hắn không hề né tránh, mà đĩnh đạc đón nhận ánh nhìn của vị học trưởng tiếng tăm lừng lẫy này.

Khí Huyết 122 Ka cùng Tinh Thần lực 105 Hz trong cơ thể Phương Bình tự động lưu chuyển, hóa giải toàn bộ áp lực vô hình từ đối phương.

Khóe môi Vương Kim Dương khẽ giật giật, trong mắt xẹt qua một tia ngạc nhiên thích thú. Hắn khẽ gật đầu với Phương Bình một cái rồi tiếp tục sải bước theo các thầy cô tiến vào hội trường.

"Phù... mẹ ơi sợ chết mất!" Trần Phàm thở hổn hển, vịn chặt lấy vai Phương Bình: "Mày có thấy ánh mắt của Vương học trưởng lúc nãy không? Tao có cảm giác chỉ cần anh ấy trừng mắt một cái là tao tắt thở luôn rồi!"

"Đó là sát khí của người từng giết địch." Phương Bình trầm ngâm nói: "Một Võ giả thực thụ không phải chỉ để biểu diễn trên võ đài, mà là để chiến đấu sinh tử!"

Tại hội trường lớn, buổi giao lưu chia sẻ kinh nghiệm thi Võ khoa bắt đầu.

Vương Kim Dương đứng trên bục diễn thuyết, không dùng micro nhưng giọng nói của hắn như tiếng chuông đồng vang vọng rõ mồn một vào tai từng học sinh:

"Các em học sinh trường Trung học Số 1, hôm nay tôi về đây không phải để nói những lời hoa mỹ sáo rỗng."

"Tôi chỉ muốn nói cho các em biết một chân lý: Con đường Võ đạo là con đường đạp trên xương trắng và máu tươi mà tiến lên!"

"Đừng nghĩ thi đỗ Võ đại là để làm quan phát tài, để hưởng thụ gái đẹp xe sang! Nếu các em mang tâm lý đó, bước chân vào Võ đại các em sẽ chết không có chỗ chôn!"

"Võ giả chúng ta... tranh với trời, tranh với đất, tranh tài nguyên tu luyện, và quan trọng nhất là tranh sinh cơ cho nhân loại!"

"Ai sợ chết, ai muốn sống an nhàn... lập tức rút lui, nộp đơn thi Văn khoa cho tôi!"

Từng câu từng chữ của Vương Kim Dương như những nhát búa đập vỡ giấc mộng màu hồng của đám học sinh. Bên dưới, nhiều kẻ mặt cắt không còn hột máu, hai chân run rẩy.

Nhưng đối với Phương Bình, từng lời nói ấy lại như ngọn lửa châm ngòi cho quả bom nhiệt huyết trong lồng ngực hắn!

Võ giả tranh mệnh! 

Càng tàn khốc, càng nguy hiểm, thì kẻ nắm giữ hệ thống như hắn lại càng có đất dụng võ!
"""
    },
    {
        "index": 17,
        "title_cn": "第十七章 王金洋的单独召见",
        "title_vi": "Chương 17: Cuộc Gặp Riêng Với Vương Kim Dương",
        "content_vi": """Sau khi buổi giao lưu kết thúc, một thầy giáo thể dục chạy xuống tìm Phương Bình: "Phương Bình, Vương học trưởng muốn gặp riêng em ở phòng tiếp khách!"

Tin tức này khiến Ngô Chí Hào và đám học sinh xung quanh chết lặng vì đố kỵ. Vương Kim Dương là thần tượng số một của giới trẻ huyện Dương Thành, ngay cả hiệu trưởng cũng phải nể hắn ba phần, vậy mà lại đích thân yêu cầu gặp riêng một học sinh lớp 12!

Phương Bình theo thầy giáo bước vào phòng tiếp khách của trường.

Bên trong phòng, Vương Kim Dương đã cởi bỏ áo khoác ngoài, chỉ mặc chiếc áo phông ngắn tay để lộ cơ bắp cánh tay rắn chắc như thép đúc. Thanh trường đao bọc vải đen đặt ngay ngắn trên bàn trà.

"Ngồi đi." Vương Kim Dương đưa tay chỉ chiếc ghế đối diện, ánh mắt chăm chú đánh giá Phương Bình.

Phương Bình thản nhiên ngồi xuống: "Chào Vương học trưởng."

Vương Kim Dương khẽ nhấp một ngụm trà, đột nhiên mở miệng: "Khí Huyết của cậu... đã vượt qua 120 Ka?"

Phương Bình không giấu giếm, gật đầu: "Hôm trước đo ở trường là 122 Ka."

Vương Kim Dương khẽ thở dài một tiếng, ánh mắt lộ vẻ tán thưởng: "Một huyện nhỏ như Dương Thành, điều kiện dinh dưỡng thiếu thốn, không có đan dược bồi bổ mà có thể tự lực tăng khí huyết lên 122 Ka... Thiên phú của cậu còn cao hơn tôi năm ngoái!"

"Học trưởng quá khen rồi."

"Tôi không khen suông." Vương Kim Dương ánh mắt trở nên sắc sảo: "Cậu muốn thi vào trường nào?"

"Ma Đô Võ Đại, hoặc Kinh Đô Võ Đại!" Phương Bình dứt khoát trả lời.

Vương Kim Dương nghe xong thì khóe môi nhếch lên nụ cười: "Dã tâm không nhỏ! Ma Đô và Kinh Đô là hai ngọn núi cao nhất của giới võ đạo Hoa Hạ. Nhưng tôi phải cảnh báo cậu: Ở đó quy tụ những thiên tài yêu nghiệt nhất cả nước, con em các đại gia tộc Tông Sư từ nhỏ đã ngâm linh dược, chiến pháp tinh thông. Cậu vào đó với thân phận một học sinh nghèo, áp lực sẽ lớn gấp vạn lần!"

"Áp lực càng lớn, động lực càng cao." Phương Bình bình tĩnh đáp lại.

Vương Kim Dương nhìn sâu vào mắt Phương Bình, thấy sự kiên định không hề dao động, liền hài lòng gật đầu:

"Tốt! Có khí phách! Tôi thích tính cách này của cậu!"

Vương Kim Dương rút trong túi ra một tấm danh thiếp màu đen có in số điện thoại cá nhân và huy hiệu Nam Giang Võ Đại đưa cho Phương Bình:

"Cầm lấy. Đây là số liên lạc của tôi. Nếu cậu đỗ vào Ma Đô Võ Đại, khi nào tới Ma Đô có thể gọi cho tôi. Ở đó tôi cũng có vài người bạn cũ có thể chiếu cố cậu một hai phần."

"Ngoài ra, tặng cậu một lời khuyên chí mạng trước kỳ đại khảo: Cố gắng thối luyện màng xương của hai chi dưới trước ngày thi thực chiến! Tốc độ chạy trốn và phản xạ đôi chân chính là tấm bùa hộ mệnh cứu mạng cậu trên chiến trường!"

"Cảm ơn Vương học trưởng chỉ giáo!" Phương Bình cẩn thận đón lấy tấm danh thiếp, trong lòng ghi nhớ sâu sắc lời khuyên này.
"""
    },
    {
        "index": 18,
        "title_cn": "第十八章 淬炼下肢！财富暴燃",
        "title_vi": "Chương 18: Thối Luyện Chi Dưới & Điểm Tài Phú Bùng Cháy",
        "content_vi": """Trở về nhà sau cuộc gặp với Vương Kim Dương, Phương Bình lập tức khóa chặt cửa phòng, chuẩn bị bước vào giai đoạn thối luyện xương cốt then chốt.

Lời khuyên của Vương Kim Dương đã chỉ rõ phương hướng: Thối luyện màng xương hai chi dưới!

Trong cơ thể con người, hai chi dưới gồm 62 khối xương: xương chậu, xương đùi, xương bánh chè, xương chày, xương mác và các khối xương bàn chân. Đây là nền tảng chịu lực của toàn bộ cơ thể, quyết định tốc độ di chuyển, sức bật và lực phát kình của võ giả.

"Hệ thống, mở bảng thuộc tính!"

Phương Bình thầm gọi. Bảng huỳnh quang lập tức hiện ra:
- Khí Huyết: 122 Ka / 122 Ka
- Tinh Thần: 105 Hz / 105 Hz
- Tài Phú: 50.068 điểm

"Bắt đầu thối cốt!"

Phương Bình ngồi xếp bằng, dựa theo Thối Cốt Pháp dẫn dắt toàn bộ khí huyết trong cơ thể dồn xuống hai bàn chân.

"Xèo xèo xèo..."

Tựa như miếng sắt nung đỏ bị nhúng vào thùng nước lạnh, khí huyết đỏ thắm cuồn cuộn bao bọc lấy 26 khối xương của bàn chân phải. Cơn đau thấu xương tủy lập tức bùng nổ!

Phương Bình cắn chặt môi đến mức bật máu, hai tay bấu chặt vào mép đệm. 

Màng xương bàn chân dưới áp lực khủng khiếp của Khí Huyết bắt đầu đào thải những vệt đen mờ mịt. Từng sợi gân, từng thớ thịt bám trên xương được tái cấu trúc, trở nên dẻo dai và bền chắc lạ thường!

Chỉ sau mười lăm phút, chỉ số Khí Huyết đã tụt dốc không phanh: 
122 -> 110 -> 95 Ka!

Cả người Phương Bình ướt sũng mồ hôi như vừa vớt dưới nước lên, mặt mũi tái nhợt vì mất sức.

"Tiêu hao 5.000 điểm Tài Phú! Bổ sung Khí Huyết!"

【Khí Huyết khôi phục đầy tràn: 122 Ka!】
【Tài Phú còn lại: 45.068 điểm!】

"Tiếp tục thối luyện!" Phương Bình không hề dừng lại dù chỉ một giây!

Trong đêm tối, căn phòng nhỏ của Phương Bình liên tục vang lên những tiếng "lốp bốp" trầm đục từ khớp xương bàn chân. 

Cứ mỗi lần khí huyết cạn kiệt, hắn lại tiêu hao điểm Tài Phú để hồi sinh sung mãn! 

Một lần... hai lần... năm lần... mười lần!

Đến rạng sáng ngày hôm sau, khi tia nắng ban mai đầu tiên rọi vào cửa sổ, Phương Bình đã hoàn thành việc thối luyện toàn bộ màng xương của hai bàn chân và một phần xương ống chân!

Hắn đứng dậy khỏi giường, bước một bước xuống sàn.

"Ầm!"

Một tiếng động trầm vang dội lên, mặt sàn xi măng cứng ngắc dưới chân hắn dường như khẽ rung chuyển! 

Phương Bình chỉ cảm thấy hai chân nhẹ bẫng như có cánh, sức bật kinh người như lò xo thép! Hắn nhón gót nhảy nhẹ một cái, cả người đã bay vút lên gần chạm trần nhà cao gần ba mét!

Hắn hạ đất êm ru như một con mèo rừng.

Nhìn lại bảng hệ thống:
- Khí Huyết: 126 Ka / 126 Ka! (Giới hạn khí huyết tự nhiên đã được nâng cao!)
- Tinh Thần: 110 Hz
- Tài Phú: 35.068 điểm

"126 Ka! Đôi chân đã hoàn thành thối cốt sơ bộ!" 

Phương Bình nắm chặt hai tay, cảm nhận sức mạnh cuồng bạo đang gầm thét trong cơ thể. Lúc này, hắn tự tin dù đối mặt với bất kỳ thí sinh hạt giống nào của các thành phố lớn, hắn cũng đủ sức giẫm đạp đối thủ dưới chân!
"""
    },
    {
        "index": 19,
        "title_cn": "第十九章 临考风云与最后的准备",
        "title_vi": "Chương 19: Phong Vân Trước Kỳ Thi & Chuẩn Bị Cuối Cùng",
        "content_vi": """Thời gian trôi qua nhanh như thoi đưa. 

Chỉ còn đúng ba ngày nữa là kỳ thi Đại khảo Võ khoa chính thức khai mạc tại Ma Đô!

Tại trường Trung học Số 1 Dương Thành, không khí học tập đã hoàn toàn nhường chỗ cho sự hồi hộp ngột ngạt của kỳ thi định mệnh. 

Trên sân vận động của trường, giáo viên thể dục đang tổ chức buổi chạy cự ly ngắn kiểm tra tốc độ cho các thí sinh báo danh Võ khoa.

"Ngô Chí Hào: 100 mét — 11 giây 2! Xuất sắc!" Thầy giáo bấm đồng hồ hô lớn.

Ngô Chí Hào chống gối thở dốc, nhưng gương mặt lộ vẻ đắc ý. Thời gian qua hắn đã uống liên tục hai viên Dưỡng Khí Đan, khí huyết ráng gượng lên được 117 Ka, tốc độ chạy nước rút cải thiện rõ rệt.

"Người tiếp theo: Phương Bình!"

Phương Bình mặc chiếc quần đùi thể thao đơn giản, bước vào vạch xuất phát. 

"Chuẩn bị... Chạy!"

"Oanh!"

Tiếng còi vừa dứt, mặt đất dưới chân Phương Bình như nổ tung một hố đất nhỏ! 

Bóng người hắn biến thành một vệt tàn ảnh xé gió lao đi với vận tốc kinh hoàng! Hai chân hắn đạp xuống mặt đường chạy tựa như hai thanh piston của động cơ phản lực, cuồng phong gào rít bên tai!

Chưa đầy chớp mắt, bóng áo trắng đã lướt qua vạch đích!

Thầy giáo thể dục nhìn vào chiếc đồng hồ bấm giây điện tử trên tay, đồng tử co rút kịch liệt, suýt nữa đánh rơi cả đồng hồ:

"9... 9 giây 48?!"

"Trời đất ơi! Kỷ lục chạy 100 mét của tỉnh Giang Nam dành cho học sinh trung học là 10 giây 15! Cậu ấy... cậu ấy chạy 9 giây 48?!"

Cả sân vận động nín thở nghẹn ngào. 

Ngô Chí Hào đứng ngây dại như một pho tượng gỗ, trong mắt tràn đầy sự tuyệt vọng tột cùng. Hắn biết, khoảng cách giữa mình và Phương Bình lúc này đã là trời và vực, vĩnh viễn không bao giờ có thể đuổi kịp nữa rồi!

Phương Bình thong thả đi bộ trở lại, hơi thở không hề rối loạn nửa nhịp. 

Sau khi thối luyện màng xương hai chi dưới, cơ bắp và xương chân của hắn đã đạt tới độ đàn hồi và bộc phát lực lượng của loài báo săn mồi! Tốc độ 9 giây 48 đối với hắn vẫn chưa phải là toàn lực!

"Thầy ơi, thành tích này đủ tiêu chuẩn ải Chuyên Nghiệp chưa ạ?" Phương Bình lễ phép hỏi.

Thầy giáo thể dục nuốt nước bọt ừng ực, run rẩy vỗ vai hắn: "Đủ... quá đủ rồi! Phương Bình, em chính là quái vật trăm năm có một của Dương Thành chúng ta!"
"""
    },
    {
        "index": 20,
        "title_cn": "第二十章 启程魔都！武神之梦",
        "title_vi": "Chương 20: Xuất Phát Tới Ma Đô & Giấc Mộng Võ Thần Khởi Đầu",
        "content_vi": """Ngày 5 tháng 6 năm 2008.

Sân ga xe lửa huyện Dương Thành sáng sớm phủ một màn sương mờ ảo. 

Đoàn khảo thí Võ khoa trường Trung học Số 1 do Hiệu trưởng Tôn Chính Đức đích thân dẫn đầu gồm bốn học sinh: Phương Bình, Ngô Chí Hào, Dương Kiến và Chu Bân. Cả đoàn chuẩn bị bước lên chuyến tàu tốc hành hướng về siêu đô thị Ma Đô — trung tâm kinh tế và võ đạo sầm uất bậc nhất phương Nam!

Trên sân ga, gia đình Phương Bình có mặt đông đủ để tiễn hắn lên đường.

Phương Danh Vinh mặc chiếc áo sơ mi mới nhất của mình, nắm chặt tay con trai: "Bình nhi, lên Ma Đô nhớ chú ý an toàn. Cứ thi hết sức mình, bố mẹ ở nhà chờ tin chiến thắng của con!"

Lý Ngọc Anh dúi vào túi áo Phương Bình một bọc trứng luộc còn nóng hổi và ít hoa quả tươi: "Ăn uống đầy đủ nghe con, đừng để bị đói."

Phương Viên ôm chặt lấy cánh tay hắn, hai mắt rưng rưng nhưng vẫn cố tỏ ra mạnh mẽ: "Anh Phương Bình, nhất định phải đỗ Ma Đô Võ Đại đấy nhé! Sau này em lên Ma Đô chơi, anh phải dẫn em đi công viên Disneyland ăn kem!"

Phương Bình cúi xuống xoa đầu cô em gái nhỏ, ánh mắt tràn đầy sự cưng chiều và kiên định: "Yên tâm đi, anh hứa với em!"

"Tu tu tu——!"

Tiếng còi tàu xe lửa vang lên giục giã, từng làn khói trắng bốc lên cuồn cuộn.

"Các em học sinh, lên tàu thôi!" Hiệu trưởng Tôn vẫy tay gọi lớn.

Phương Bình đeo ba lô lên vai, xoay người bước lên bậc thang toa tàu. Đứng bên cửa sổ sổ tàu hỏa, hắn vẫy tay chào cha mẹ và em gái đang đứng ngóng trông dưới sân ga. 

Chuyến tàu từ từ chuyển bánh, lao vút về phía chân trời xa xôi.

Phương Bình ngồi xuống ghế nệm, nhìn phong cảnh đồng quê lướt qua ngoài cửa sổ. 

Trong tâm trí hắn, bảng hệ thống huỳnh quang lặng lẽ tỏa sáng:
- Túc chủ: Phương Bình
- Khí Huyết: 126 Ka / 126 Ka
- Tinh Thần: 110 Hz / 110 Hz
- Tài Phú: 35.068 điểm

Ma Đô — nơi ngọa hổ tàng long, nơi có Ma Đô Võ Đại với hàng vạn thiên tài cái thế, nơi có các vị Đại Tông Sư trấn thủ phương Nam, và cũng là nơi ẩn giấu lối vào bí mật của Địa Quật đẫm máu!

Một thiếu niên trùng sinh mang theo hệ thống quy đổi tài phú vô hạn, mang theo lời hứa bảo vệ gia đình và giống nòi, chính thức bước chân lên vũ đài thế giới!

"Ma Đô, ta đến đây!"

Phương Bình nhếch mép cười, ánh mắt bùng cháy ngọn lửa dã tâm ngập trời. Huyền thoại bất hủ của Nhân Vương Phương Bình... từ giây phút này chính thức mở màn!
"""
    }
]

def update_batch2():
    conn = sqlite3.connect('data/novels.db', timeout=60.0)
    cursor = conn.cursor()
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_count = 0
    
    for ch in CHAPTERS_BATCH2:
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
    print(f"\n[HOÀN TẤT] Đã cập nhật thành công {updated_count} chương Batch 2 cho Toàn Cầu Cao Võ (ID: {NOVEL_ID})")

if __name__ == '__main__':
    update_batch2()
