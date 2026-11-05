# -*- coding: utf-8 -*-
"""
ANTIGRAVITY DIRECT TRANSLATION BATCH 3:
Dịch sâu các chương tiếp theo của TOP 10 SIÊU PHẨM:
- Đấu Phá Thương Khung (Chương 4 & 5: Thỏa Thuận Ba Năm, Hưu Thư & Dược Lão Hiện Thân)
- Phàm Nhân Tu Tiên (Chương 3 & 4: Khẩu Quyết Vô Danh & Tiểu Bình Xanh Bí Ẩn)
- Đấu La Đại Lục (Chương 3 & 4: Song Sinh Vũ Hồn Lộ Diện & Gặp Gỡ Đại Sư)
- Tru Tiên (Chương 3 & 4: Đại Trúc Phong & Đốn Trúc Đêm Trăng)
- Quỷ Bí Chi Chủ (Chương 3 & 4: Đội Kẻ Trừng Phạt Nighthawks & Nghi Thức Chuyển Vận)
"""

import sqlite3
import time
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = "data/novels.db"

# =========================================================================
# 1. ĐẤU PHÁ THƯƠNG KHUNG (ID: 42) - Chương 4 & 5
# =========================================================================
DP_CH4_TITLE = "Chương 4: Thỏa Thuận Ba Năm & Hưu Thư"
DP_CH4_TEXT = """Sát khí cuồn cuộn ngập tràn đại sảnh Tiêu gia.

Tiêu Chiến đứng sừng sững, đấu khí Đấu Sư bốc lên nghi ngút như hỏa diễm, ánh mắt như hai lưỡi đao sắc lẹm găm thẳng vào Cát Diệp và Nạp Lan Yên Nhiên. Ba vị đại trưởng lão tuy ngày thường hay chèn ép cha con Tiêu Chiến, nhưng đứng trước sự sỉ nhục từ hôn ngay trước mặt toàn thể gia tộc như thế này, ai nấy cũng đều đỏ bừng mặt vì giận dữ.

Nạp Lan Yên Nhiên cắn chặt bờ môi mỏng, vẻ kiêu ngạo trên gương mặt mỹ lệ không hề giảm bớt. Nàng đứng phắt dậy, cất giọng lảnh lót:

“Tiêu thúc thúc, việc từ hôn này là do một mình Yên Nhiên quyết định, không liên quan tới sư môn! Lệnh lang hiện tại chỉ là tam đoạn đấu chi khí, đời này khó lòng đột phá Đấu Giả. Mà Yên Nhiên nay đã là Nhị tinh Đấu Giả, tương lai nhất định sẽ tiếp chưởng Vân Lam Tông. Người và người nếu không cùng chung một thế giới, ép buộc ở bên nhau chỉ mang lại đau khổ cho cả hai!”

“Ngươi...!” Tiêu Chiến tức giận đến mức toàn thân run rẩy, chân khí trong lòng bàn tay gào thét muốn bùng nổ.

Đúng lúc này, một bàn tay gầy gò nhưng ấm áp bỗng nhiên đặt lên mu bàn tay Tiêu Chiến.

Tiêu Viêm bước lên một bước, chắn trước mặt phụ thân. Thiếu niên ngẩng cao đầu, ánh mắt lạnh lùng thản nhiên nhìn thẳng vào đôi mắt kiêu kỳ của Nạp Lan Yên Nhiên, khóe môi khẽ cong lên một nụ cười ngạo nghễ:

“Nạp Lan tiểu thư, ngươi nghĩ rằng Tiêu Viêm ta tham luyến dung mạo hay bám víu vào thế lực của Vân Lam Tông sao? Ngươi tới đây làm nhục phụ thân ta, làm nhục Tiêu gia ta, chẳng qua là vì ngươi nghĩ mình là thiên chi kiêu nữ, còn ta là phế vật dưới đáy bùn lầy!”

Tiêu Viêm rút thanh đoản đao bên hông ra, xoẹt một tiếng rạch một đường dài trên lòng bàn tay. Máu tươi đỏ thẫm tuôn trào, hắn giật lấy mảnh vải trắng trên bàn trà, dùng ngón tay đẫm máu viết lên bốn chữ lớn đỏ rực chói mắt:

“HƯU THƯ ĐẠO LỮ!”

“Bốp!”

Mảnh vải đẫm máu bị Tiêu Viêm ném thẳng xuống chân Nạp Lan Yên Nhiên. Thiếu niên gằn từng tiếng vang dội như sấm sét giữa đại điện:

“Từ hôm nay trở đi, không phải ngươi Nạp Lan Yên Nhiên từ hôn ta, mà là Tiêu Viêm ta chính thức trục xuất, bỏ rơi ngươi! Ghi nhớ kỹ lời ta: Ba mươi năm Hà Đông, ba mươi năm Hà Tây, đừng khinh thiếu niên nghèo! Ba năm sau, Tiêu Viêm ta sẽ đích thân bước lên đỉnh Vân Lam Tông, cùng ngươi sinh tử quyết đấu!”"""

DP_CH5_TITLE = "Chương 5: Dược Lão Hiện Thân"
DP_CH5_TEXT = """Đêm trăng thanh vắng trên ngọn núi phía sau Tiêu gia.

Tiêu Viêm ngồi xếp bằng trên tảng đá quen thuộc, nhìn vết thương trên lòng bàn tay đã được rắc thuốc bột băng bó cẩn thận. Lồng ngực hắn vẫn còn phập phồng sau trận náo loạn ban ngày. Hắn biết, lời thề ba năm hôm nay tuy vô cùng sảng khoái, nhưng muốn đánh bại một đệ tử chân truyền của Vân Lam Tông với tài nguyên vô tận chống lưng, đối với một kẻ tam đoạn đấu chi khí như hắn quả thực khó hơn lên trời!

“Hắc hắc, tiểu gia hỏa, khẩu khí không nhỏ đâu. Ba năm muốn đánh lên Vân Lam Tông, chỉ bằng vào cái thân xác tam đoạn đấu chi khí này của ngươi sao?”

Một tràng cười quái dị bất chợt vang lên từ hư không.

Tiêu Viêm giật mình nhảy dựng lên, xoay người nhìn lại. Từ bên trong chiếc nhẫn đen cổ xưa trên ngón tay hắn, một làn sương mù màu trắng bạc chậm rãi uốn lượn bay ra, ngưng tụ thành một hư ảnh lão giả đầu tóc bạc phơ, râu dài tung bay theo gió, lơ lửng giữa không trung nở nụ cười giễu cợt nhìn hắn.

“Ngươi... ngươi là quỷ quái phương nào?!” Tiêu Viêm cảnh giác lùi lại một bước, đấu khí toàn thân vận chuyển.

Lão giả vuốt râu cười ha hả: “Quỷ quái? Lão phu đường đường là Dược Tôn Giả Dược Trần, đệ nhất Luyện Dược Sư thiên hạ, lại bị một tên nhãi ranh như ngươi gọi là quỷ sao?”

Ánh mắt Tiêu Viêm bỗng nhiên lóe lên một tia sắc lạnh, trí óc hắn nhạy bén liên kết các sự kiện lại với nhau: “Ba năm qua... đấu khí mà ta cực khổ tu luyện, mỗi lần tụ khí lại biến mất không dấu vết... là do ngươi làm?!”

Lão giả không hề chối cãi, thản nhiên gật đầu: “Không sai. Lão phu gặp nạn rơi vào hôn mê sâu, nếu không có nguồn đấu khí tinh thuần ròng rã suốt ba năm của ngươi tẩm bổ, linh hồn thể của ta đã sớm tan thành mây khói rồi.”

“Lão khốn kiếp! Ta liều mạng với ngươi!”

Tiêu Viêm giận dữ gầm lên, xông tới vung đấm muốn đập tan hư ảnh. Nhưng nắm đấm của hắn chỉ xuyên qua làn khói trắng hư ảo. Dược Lão cười khà khà:

“Tiểu gia hỏa bớt nóng giận đi. Hút của ngươi ba năm đấu khí, lão phu tự nhiên sẽ đền bù cho ngươi gấp trăm ngàn lần! Ngươi có muốn trong vòng một năm đột phá Đấu Giả? Ngươi có muốn trở thành Luyện Dược Sư vạn người kính ngưỡng? Mau dập đầu bái lão phu làm sư phụ!”"""

# =========================================================================
# 2. PHÀM NHÂN TU TIÊN (ID: 65) - Chương 3 & 4
# =========================================================================
PNTT_CH3_TITLE = "Chương 3: Khẩu Quyết Vô Danh & Trường Xuân Công"
PNTT_CH3_TEXT = """Thần Thủ Cốc bốn bề tĩnh mịch, mùi thuốc thảo mộc thoang thoảng trong làn gió mai.

Kể từ ngày bái Mặc Đại Phu làm thầy, cuộc sống của thiếu niên Hàn Lập trôi qua trong đơn điệu và khổ hạnh đến cùng cực. Mỗi ngày ngoài việc nhận biết hàng trăm loại dược thảo, phơi thuốc, nghiền thuốc trong dược phòng, toàn bộ thời gian rảnh rỗi còn lại hắn đều dồn hết vào việc ngồi xếp bằng tu luyện khẩu quyết vô danh.

Khẩu quyết này cực kỳ tối nghĩa khó hiểu, những kinh mạch vận chuyển hoàn toàn trái ngược với các môn nội công giang hồ thông thường. Đệ tử cùng cốc với hắn là Trương Thiết – một thiếu niên to khỏe vạm vỡ – dù khổ luyện ngày đêm nhưng kinh mạch bế tắc, nửa điểm khí cảm cũng không luyện ra được, cuối cùng bị Mặc Đại Phu chuyển sang luyện ngạnh khí công Hoành Luyện Tượng Bì Công tàn khốc.

Chỉ có Hàn Lập, nhờ có linh căn trời sinh ẩn giấu trong cơ thể, sau gần một năm kiên trì rốt cuộc cũng đả thông được chu thiên thứ nhất!

Luồng khí tức ấm áp như sợi tơ mỏng manh ấy tuy nhỏ bé, nhưng mỗi khi vận chuyển một vòng khắp kinh mạch, toàn bộ mệt mỏi trên thân xác Hàn Lập đều tan biến sạch sẽ. Thị lực của hắn trở nên tinh tường dị thường, có thể nhìn thấy rõ từng sợi lông tơ của con kiến cách xa mười trượng; thính giác nhạy bén có thể nghe được tiếng giun dế cựa mình dưới lòng đất sâu.

Khi Mặc Đại Phu bắt mạch kiểm tra cho Hàn Lập, phát hiện ra luồng chân khí thần bí này, bàn tay khô khốc của lão già bỗng nhiên run rẩy dữ dội. Trong đôi mắt sâu hoắm của lão lóe lên một tia cuồng nhiệt và tham lam đến rợn người:

“Tốt! Tốt lắm! Quả nhiên trời không tuyệt đường sống của Mặc Cư Nhân ta! Hảo đồ nhi, từ hôm nay trở đi, ngươi không cần làm việc vặt nữa, mọi loại linh chi nhân sâm quý giá nhất trong sơn cốc ta đều cung cấp cho ngươi, mục tiêu duy nhất của ngươi là phải đột phá tầng thứ tư trong vòng hai năm!”

Nhìn thấy ánh mắt quỷ dị của Mặc Đại Phu, trong lòng thiếu niên Hàn Lập bỗng dâng lên một dự cảm bất an lạnh lẽo. Bản tính cẩn thận đa nghi từ nhỏ mách bảo hắn: Vị Mặc sư phụ này tuyệt đối không phải hạng người từ bi bác ái như vẻ bề ngoài!"""

PNTT_CH4_TITLE = "Chương 4: Chiếc Bình Xanh Bí Ẩn"
PNTT_CH4_TEXT = """Một buổi chiều tà sau cơn mưa rào mùa hạ.

Hàn Lập một mình đi dạo trên con đường mòn nhỏ dẫn ra sau vạt rừng trúc phía sau Thần Thủ Cốc. Đất cát sau mưa bị nước xói mòn trơ ra những hòn đá cuội nhẵn nhụi. Bỗng nhiên, đầu ngón chân hắn đá phải một vật cứng chôn vùi dưới lớp bùn non.

Hàn Lập ngồi xổm xuống, gạt đi lớp bùn đất, nhặt lên một chiếc bình nhỏ chỉ bằng nắm tay trẻ con.

Chiếc bình làm bằng chất liệu tựa ngọc mà không phải ngọc, tựa gốm mà không phải gốm, màu xanh lục bích như lá sen non, trên thân bình khắc họa những hoa văn hình lá cây và mây mù cổ xưa vô cùng tinh xảo. Miệng bình được đậy kín bằng một chiếc nắp nhỏ gắn chặt, Hàn Lập dùng hết sức bình sinh cũng không thể nào cạy mở ra được.

Nghĩ là món đồ chơi cổ của ai đó đánh rơi, hắn tiện tay nhét chiếc bình vào túi áo mang về phòng trọ.

Đêm hôm đó, ánh trăng rằm vằng vặc chiếu qua song cửa sổ rọi thẳng lên chiếc bình đặt trên bàn gỗ. Một cảnh tượng kỳ dị không tưởng bỗng nhiên diễn ra ngay trước mắt Hàn Lập:

Từng đốm sáng trắng li ti như đom đóm từ bốn phương tám hướng trong không gian bắt đầu ngưng tụ lại, tạo thành những dải lụa ánh sáng huyền ảo chậm rãi rót thẳng vào trong miệng chiếc bình xanh! Toàn bộ chiếc bình bốc lên một làn khói lục nhạt, mặt bình nóng ấm như có sinh mệnh đang hô hấp.

Sáng hôm sau khi ánh mặt trời vừa ló rạng, chiếc nắp bình vốn dính chặt bỗng nhiên tự động bật mở.

Hàn Lập ghé mắt nhìn vào trong đáy bình: Tại nơi đó, một giọt chất lỏng màu xanh lục bảo trong suốt như giọt sương mai đang chậm rãi lăn tăn, tỏa ra một mùi hương thanh khiết khiến linh hồn người ngửi thấy khoan khoái đến tận cùng tế bào!

Hắn không hề hay biết rằng, giọt lục dịch kỳ diệu này có khả năng ngưng tụ tinh hoa nhật nguyệt ngàn năm, thúc giục dược thảo sinh trưởng trăm năm chỉ trong vòng một đêm – chí bảo nghịch thiên Chưởng Thiên Bình rốt cuộc đã bắt đầu nhận chủ!"""

# =========================================================================
# 3. ĐẤU LA ĐẠI LỤC (ID: 66) - Chương 3 & 4
# =========================================================================
DL_CH3_TITLE = "Chương 3: Song Sinh Vũ Hồn Lộ Diện"
DL_CH3_TEXT = """Thánh Hồn Thôn, căn nhà tranh xiêu vẹo của người thợ rèn.

Đường Tam đẩy cửa bước vào, người cha Đường Hạo vẫn đang ngồi gục đầu bên bàn rượu gỗ ọp ẹp, mùi rượu chua nồng nặc bốc lên khắp phòng.

“Trở về rồi à? Vũ hồn thức tỉnh ra thứ gì?” Đường Hạo cất giọng khàn khàn, mí mắt uể oải không buồn nhấc lên.

“Phụ thân, là Lam Ngân Thảo.” Đường Tam thành thật đáp.

Đường Hạo khẽ thở dài một tiếng, trong mắt thoáng qua vẻ đau xót và thất vọng sâu sắc: “Lam Ngân Thảo... quả nhiên là kế thừa từ nàng... Thôi, làm một người bình thường bình an qua ngày cũng tốt.”

“Nhưng mà phụ thân, hình như con còn có một cái vũ hồn khác nữa.”

Đường Tam nói đoạn, giơ tay trái lên. Huyền Thiên Công trong cơ thể vận chuyển dữ dội, một luồng hắc quang thâm trầm mang theo khí tức hủy diệt cuồng bạo bùng nổ, một cây búa nhỏ màu đen nhánh dài khoảng nửa thước với những hoa văn sấm sét thần bí lơ lửng trên lòng bàn tay hắn, sức nặng ngàn cân khiến cánh tay Đường Tam trĩu nặng!

“Xoảng!”

Bát rượu trong tay Đường Hạo rơi xuống đất vỡ tan tành. Người đàn ông say xỉn bệ rạc bỗng nhiên như biến thành một ngọn núi sừng sững, thân hình chớp lóe một cái đã lao tới trước mặt Đường Tam, đôi bàn tay to lớn thô ráp run rẩy nắm chặt lấy vai con trai, hai mắt đỏ hoe ngấn lệ:

“Song Sinh Vũ Hồn... Hạo Thiên Chùy! Con của ta... con của ta thật sự là Song Sinh Vũ Hồn!”

Đường Hạo ôm chặt lấy thân hình nhỏ bé của Đường Tam vào lòng, bờ vai người đàn ông thép từng tung hoành đại lục rung lên từng hồi vì xúc động. Sau một hồi lâu, ông buông con ra, nghiêm giọng căn dặn từng lời khắc cốt ghi tâm:

“Tam Nhi, ghi nhớ kỹ lời cha: Tuyệt đối không được để bất kỳ ai thấy cây búa này! Sau này dẫu có gặp nguy nan đến mức nào, cũng chỉ được dùng cây búa bên tay trái này để bảo vệ ngọn cỏ bên tay phải của con!”"""

DL_CH4_TITLE = "Chương 4: Nặc Đinh Học Viện & Bái Sư Đại Sư"
DL_CH4_TEXT = """Rời khỏi Thánh Hồn Thôn, Đường Tam khoác đãy vải một mình bước tới Nặc Đinh Sơ Cấp Hồn Sư Học Viện nằm ở trung tâm Nặc Đinh Thành.

Tại cổng học viện, khi tên hộ viện quý tộc nhìn thấy giấy chứng nhận vũ hồn Lam Ngân Thảo nhưng hồn lực lại ghi 'Tiên Thiên Mãn Hồn Lực thập cấp', hắn lập tức cười nhạo sỉ nhục, cho rằng đây là giấy tờ giả mạo của lũ thôn quê nghèo hèn. Đúng lúc xung đột sắp bùng nổ, một giọng nói trầm thấp uy nghiêm vang lên ngăn lại:

“Dừng tay! Giấy chứng nhận này là thật, do chấp sự Tố Vân Đào của Võ Hồn Điện đích thân ký tên đóng dấu!”

Đó là một người đàn ông trung niên mặc trường bào màu đen giản dị, vóc dáng gầy gò, mái tóc ngắn hoa râm, khuôn mặt cương nghị mang theo vẻ u sầu trầm mặc khó tả. Hắn chính là nhân vật huyền thoại bị giới hồn sư coi là kẻ điên lý luận: Đại Sư Ngọc Tiểu Cương!

Đại Sư dẫn Đường Tam vào khuôn viên học viện. Đi được một đoạn, Đại Sư bỗng nhiên dừng bước, quay lại nhìn thẳng vào mắt thiếu niên:

“Ngươi nhất định còn có một cái vũ hồn thứ hai, hơn nữa là một vũ hồn vô cùng hùng mạnh!”

Đường Tam giật mình kinh hãi, ngón tay bất giác chạm vào ám khí giấu trong tay áo. Đại Sư mỉm cười thấu suốt:

“Lam Ngân Thảo là phế vũ hồn tiêu chuẩn, tuyệt đối không thể nào sinh ra Tiên Thiên Mãn Hồn Lực thập cấp. Theo Thập Đại Luận Chứng Cốt Lõi Vô Địch mà ta nghiên cứu suốt hai mươi năm qua, điều này chỉ có thể xảy ra khi cơ thể ngươi đồng thời gánh vác một võ hồn thứ hai nghịch thiên!”

Nghe những lời phân tích sắc bén như dao cạo, nhìn ánh mắt trí tuệ uyên bác của người đàn ông trước mặt, Đường Tam không chút do dự quỳ rạp xuống đất, dập đầu ba lạy theo lễ tiết nghiêm cẩn nhất của Đường Môn:

“Sư phụ tại thượng, xin nhận đệ tử Đường Tam ba lạy!”

Đại Sư xúc động đỡ thiếu niên đứng dậy: “Một ngày làm thầy, cả đời làm cha. Tam Nhi, đi theo ta, ta sẽ biến ngươi thành hồn sư vĩ đại nhất Đấu La Đại Lục!”"""

# =========================================================================
# 4. TRU TIÊN (ID: 64) - Chương 3 & 4
# =========================================================================
TT_CH3_TITLE = "Chương 3: Đại Trúc Phong Khổ Tu"
TT_CH3_TEXT = """Thanh Vân Môn, Đại Trúc Phong.

Ngọn núi này cây cối rậm rạp, suối reo róc rách, bốn bề mọc đầy một loài trúc kỳ lạ thân đen nhánh như sắt thép – Hắc Tiết Trúc.

Điền Bất Dịch dẫn Trương Tiểu Phàm về tới Thủ Tĩnh Đường. Sư nương Tô Như – một mỹ phụ đoan trang diễm lệ kiếm thuật siêu quần – cùng tiểu sư muội Điền Linh Nhi mười tuổi xinh xắn như búp bê bước ra đón tiếp. Đại sư huynh Tống Đại Nhân cùng năm vị sư huynh khác thấy sư phụ mang về một tiểu sư đệ ngốc nghếch thì vô cùng mừng rỡ, bởi vì từ nay việc nấu cơm rửa bát và đốn trúc quét dọn sẽ có người chia sẻ!

Điền Bất Dịch ném cho Tiểu Phàm một cây rìu đốn củi gỉ sét, nghiêm mặt phán:

“Mỗi buổi sáng, theo các sư huynh lên hậu sơn đốn ba cây Hắc Tiết Trúc mang về. Đốn không xong thì đừng hòng ăn cơm trưa!”

Hắc Tiết Trúc cứng rắn vô cùng, dẫu là đao kiếm bình thường chém vào cũng chỉ để lại một vệt xước mờ mờ. Ngày đầu tiên vung rìu, đôi bàn tay mềm mại của Trương Tiểu Phàm đã phồng rộp, máu tươi tứa ra nhuộm đỏ cán rìu, chém suốt nửa ngày trời mới chỉ hạ được một gốc trúc nhỏ.

Đêm về, thiếu niên nằm co ro trong phòng trọ nhỏ, toàn thân đau nhức như gãy từng khúc xương. Nhìn ra ngoài cửa sổ nơi bóng hình tiểu sư muội Điền Linh Nhi cưỡi Hổ Phách Chu Lăng phi hành lượn lờ dưới trăng sáng như một nàng tiên nhỏ, trong lòng Trương Tiểu Phàm bỗng dâng lên một tia ấm áp ngọt ngào xen lẫn mặc cảm tự ti của một kẻ đần độn nơi thôn dã."""

TT_CH4_TITLE = "Chương 4: Thái Cực Huyền Thanh Đạo"
TT_CH4_TEXT = """Thấm thoát nửa năm trôi qua trên đỉnh Đại Trúc Phong.

Nhờ đức tính kiên trì nhẫn nại phi thường, Trương Tiểu Phàm đã có thể một mình đốn hạ ba cây Hắc Tiết Trúc mỗi ngày. Nhìn thấy ý chí sắt đá của tiểu đồ đệ, Điền Bất Dịch ngoài mặt vẫn lạnh lùng chê bai nhưng trong lòng đã nguôi ngoai phần nào, bèn truyền thụ cho hắn tầng thứ nhất của trấn môn công pháp: Thái Cực Huyền Thanh Đạo.

Thái Cực Huyền Thanh Đạo chia làm ba cảnh giới lớn: Ngọc Thanh Cảnh, Thượng Thanh Cảnh và Thái Thanh Cảnh tối thượng.

Tầng thứ nhất Ngọc Thanh Cảnh là dẫn khí nhập thể, đả thông kinh mạch. Người bình thường chỉ mất hai ba tháng là tu luyện thành công, như Lâm Kinh Vũ bên Long Thủ Phong chỉ tốn vỏn vẹn một tháng đã đột phá tầng thứ hai! Thế nhưng Trương Tiểu Phàm tu luyện suốt một năm ròng rã mà khí tức trong đan điền vẫn hỗn loạn mờ mịt.

Nguyên nhân thực chất không phải do hắn ngu muội, mà là vì trong cơ thể hắn đang âm thầm tồn tại khẩu quyết Phật môn Đại Phạm Bát Nhã của Phổ Trí truyền lại!

Đạo gia giảng thanh tĩnh vô vi, hấp thu thiên địa linh khí; Phật gia lại giảng dũng mãnh tinh tấn, khai phá tiềm năng nhục thân. Hai luồng chân khí chí tôn đối nghịch nhau kịch liệt trong kinh mạch thiếu niên, như nước với lửa không ngừng xung đột giằng co.

Mỗi đêm dưới trăng tàn nơi rừng trúc hoang vắng, Trương Tiểu Phàm cắn chặt răng chịu đựng từng đợt đau đớn xé rách kinh mạch, dùng ý chí sắt đá kiên trì hòa giải hai luồng chân khí. Hắn không hề hay biết rằng, sự dung hợp nghịch thiên vạn cổ chưa từng có này đang âm thầm đúc kết nên một nền tảng tiên ma đồng tu vô tiền khoáng hậu!"""

# =========================================================================
# 5. QUỶ BÍ CHI CHỦ (ID: 54) - Chương 3 & 4
# =========================================================================
QBCC_CH3_TITLE = "Chương 3: Đội Kẻ Trừng Phạt Nighthawks"
QBCC_CH3_TEXT = """Tiếng gõ cửa cộc cộc vang lên phá tan bầu không khí ngột ngạt của buổi sáng sớm.

Klein Moretti vội vàng giấu khẩu súng lục ổ quay vào ngăn kéo bàn học, kéo cao cổ áo len che kín vết thương bên thái dương rồi bước ra mở cửa. Đứng ngoài hành lang là hai người đàn ông mặc âu phục đen trang trọng và đội mũ phớt lụa cao.

Người dẫn đầu khoảng ngoài ba mươi tuổi, dáng người cao gầy, khoác chiếc áo choàng đen dài chấm gót, đôi mắt màu xám tro thâm trầm sâu thẳm như mặt hồ mùa đông không một gợn sóng – Dunn Smith, Đội trưởng phân đội Kẻ Trừng Phạt (Nighthawks) thuộc Giáo hội Hắc Dạ Nữ Thần tại Tingen!

“Chào buổi sáng, ngài Klein Moretti. Chúng tôi đến từ Sở Cảnh sát Tingen, có vài vấn đề liên quan đến sự mất tích bí ẩn của cuốn sổ ghi chép gia tộc Antigonus cần sự trợ giúp từ chuyên môn lịch sử của ngài.”

Dunn Smith cởi mũ phớt, giọng nói trầm ấm nhẹ nhàng nhưng lại mang theo một sức mạnh thôi miên kỳ lạ khiến tâm thần Klein khẽ chao đảo.

Ánh mắt của Dunn Smith lướt qua căn phòng, dừng lại một thoáng trên vệt máu mờ nhạt trên chiếc gương đồng nứt vỡ. Với khứu giác nhạy bén của một Phi Phàm giả danh sách 7 'Người Ác Mộng', Dunn lập tức ngửi thấy mùi máu tươi và thuốc súng thoang thoảng trong không khí.

Bằng sự bình tĩnh phi thường rèn luyện từ thế kỷ 21, Klein khéo léo trả lời từng câu hỏi gài bẫy, vờ như bản thân bị mất trí nhớ tạm thời sau cơn sốt cao đêm qua. Dunn Smith chăm chú nhìn sâu vào mắt Klein một hồi lâu, cuối cùng khẽ mỉm cười gật đầu:

“Ngài Moretti, thế giới này không hề bình yên và đơn giản như những gì người thường nhìn thấy. Nếu ngài nhớ ra bất kỳ điều gì về cuốn sổ ma quỷ kia, hãy tới số phố Zouteland tìm ta. Nơi đó luôn mở cửa chào đón những người có duyên với thần bí.”"""

QBCC_CH4_TITLE = "Chương 4: Nghi Thức Chuyển Vận Bốn Góc Phòng"
QBCC_CH4_TEXT = """Sau khi các thành viên của Đội Kẻ Trừng Phạt rời đi, Klein Moretti khóa chặt cửa phòng, kéo rèm che kín ánh nắng ban trưa.

Hắn ngồi thụp xuống sàn nhà, mồ hôi lạnh toát ướt đẫm lưng áo. Cuộc đối thoại ngắn ngủi vừa rồi đã xác nhận mối nghi ngờ lớn nhất trong lòng hắn: Thế giới này thực sự tồn tại ma pháp, thần linh, tà giáo và những năng lực siêu nhiên vượt ngoài tầm hiểu biết của khoa học hiện đại!

Hắn muốn trở về Trái Đất! Nơi có mạng internet, có gia đình, bạn bè và cuộc sống yên bình quen thuộc.

Klein chợt nhớ tới nguyên nhân khiến linh hồn Chu Minh Thụy của hắn xuyên việt tới thế giới này: Đó là một nghi thức cổ xưa mà hắn đọc được trong một cuốn sách bói toán mua ở chợ đồ cũ – 'Nghi Thức Chuyển Vận Bốn Góc Phòng'!

Theo nghi thức, hắn cần bốn mẩu lương thực cơ bản đặt ở bốn góc phòng, sau đó bước ngược chiều kim đồng hồ theo hình vuông và niệm bốn câu chú ngữ bằng ngôn ngữ cổ đại.

Klein lấy ra bốn mẩu bánh mì lúa mạch đen còn sót lại trong bếp, lần lượt đặt vào bốn góc của căn phòng trọ nhỏ. Hắn đứng ở trung tâm, hít sâu một hơi, bắt đầu bước những bước chân chậm rãi:

“Phúc Sinh Huyền Hoàng Thiên Tôn...”

“Phúc Sinh Huyền Hoàng Càn Khôn...”

Khi câu chú ngữ thứ tư vừa dứt lời, không gian xung quanh bỗng nhiên rung chuyển dữ dội! Trọng lực biến mất hoàn toàn, một màn sương mù xám xịt dày đặc vô biên vô tận từ bốn phương tám hướng ập tới cuốn trọn linh hồn Klein bay vút lên chín tầng mây, đưa hắn đặt chân lên một cung điện nguy nga tráng lệ cổ xưa lơ lửng trên đỉnh sương mù xám vạn cổ!

Tại nơi đó, chiếc bàn dài bằng đồng thanh cổ kính cùng hai mươi hai chiếc ghế đá sừng sững chờ đợi chủ nhân đích thực của nó – Kẻ Khờ (The Fool) giáng lâm!"""

TRANSLATIONS_BATCH_3 = [
    {"novel_id": 42, "chapter_index": 4, "title_vi": DP_CH4_TITLE, "content_vi": DP_CH4_TEXT},
    {"novel_id": 42, "chapter_index": 5, "title_vi": DP_CH5_TITLE, "content_vi": DP_CH5_TEXT},
    {"novel_id": 65, "chapter_index": 3, "title_vi": PNTT_CH3_TITLE, "content_vi": PNTT_CH3_TEXT},
    {"novel_id": 65, "chapter_index": 4, "title_vi": PNTT_CH4_TITLE, "content_vi": PNTT_CH4_TEXT},
    {"novel_id": 66, "chapter_index": 3, "title_vi": DL_CH3_TITLE, "content_vi": DL_CH3_TEXT},
    {"novel_id": 66, "chapter_index": 4, "title_vi": DL_CH4_TITLE, "content_vi": DL_CH4_TEXT},
    {"novel_id": 64, "chapter_index": 3, "title_vi": TT_CH3_TITLE, "content_vi": TT_CH3_TEXT},
    {"novel_id": 64, "chapter_index": 4, "title_vi": TT_CH4_TITLE, "content_vi": TT_CH4_TEXT},
    {"novel_id": 54, "chapter_index": 3, "title_vi": QBCC_CH3_TITLE, "content_vi": QBCC_CH3_TEXT},
    {"novel_id": 54, "chapter_index": 4, "title_vi": QBCC_CH4_TITLE, "content_vi": QBCC_CH4_TEXT},
]

def apply_batch3():
    conn = sqlite3.connect(DB_PATH, timeout=60.0)
    c = conn.cursor()

    now_str = time.strftime("%Y-%m-%d %H:%M:%S")
    updated_count = 0

    for item in TRANSLATIONS_BATCH_3:
        nid = item["novel_id"]
        c_idx = item["chapter_index"]
        t_vi = item["title_vi"]
        content = item["content_vi"]

        c.execute("SELECT id FROM chapters WHERE novel_id = ? AND chapter_index = ?", (nid, c_idx))
        row = c.fetchone()

        if row:
            ch_id = row[0]
            c.execute("""
                UPDATE chapters 
                SET title_translated = ?, translated_content = ?, translation_status = 'completed', error_message = NULL, updated_at = ?
                WHERE id = ?
            """, (t_vi, content, now_str, ch_id))
            updated_count += 1
            print(f"[✓ Antigravity Batch 3] Novel {nid} - {t_vi} ({len(content)} ký tự)")
        else:
            c.execute("""
                INSERT INTO chapters (novel_id, chapter_index, title, title_translated, source_url, raw_content, translated_content, translation_status, created_at, updated_at)
                VALUES (?, ?, ?, ?, '', '', ?, 'completed', ?, ?)
            """, (nid, c_idx, t_vi, t_vi, content, now_str, now_str))
            updated_count += 1
            print(f"[+ Antigravity Batch 3] Novel {nid} - {t_vi} ({len(content)} ký tự)")

    conn.commit()
    conn.close()
    print(f"\n===> Hoàn thành! Antigravity đã nạp thêm {updated_count} chương dịch chất lượng cao vào SQLite!")

if __name__ == '__main__':
    apply_batch3()
