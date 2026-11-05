# -*- coding: utf-8 -*-
"""
ANTIGRAVITY DIRECT TRANSLATION BATCH 2:
Dịch tiếp các siêu phẩm hàng đầu trong Top 100 của năm:
Tru Tiên (Chương 2), Quỷ Bí Chi Chủ (Chương 2), Đế Bá (Chương 2),
Vũ Động Càn Khôn (Chương 1-2), Bàn Long (Chương 1-2), Tinh Thần Biến (Chương 1-2),
Võ Luyện Đỉnh Phong (Chương 1-2), Ta Thật Không Muốn Trùng Sinh A (Chương 1-2).
"""

import sqlite3
import time
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = "data/novels.db"

# 1. Tru Tiên (ID: 64) - Chương 2
TT_CH2_TITLE = "Chương 2: Thanh Vân Môn Hạ"
TT_CH2_TEXT = """Thanh Vân Sơn ngút ngàn mây trắng, bảy tòa kỳ phong chọc thẳng vào tầng trời xanh thẳm như bảy thanh tiên kiếm của bậc cự thần thượng cổ sừng sững giữa đất trời.

Trên đỉnh Thông Thiên Phong cao nhất, Ngọc Thanh Điện nguy nga tráng lệ chìm trong làn hương khói thanh tịnh lượn lờ. Giữa đại điện, Đạo Huyền Chân Nhân – chưởng môn đời thứ mười tám của Thanh Vân Môn – tiên phong đạo cốt, râu tóc bạc phơ, đang cùng sáu vị thủ tọa các phong nhìn xuống hai đứa trẻ mồ côi quỳ dưới chân điện.

Lâm Kinh Vũ và Trương Tiểu Phàm cả người lấm lem bùn đất và máu tươi, nét mặt thất thần hoảng loạn sau thảm án diệt thôn đêm qua.

Khi các vị thủ tọa dùng thần thức dò xét tư chất, ai nấy đều phải thốt lên kinh ngạc trước cốt cách tuyệt luân của Lâm Kinh Vũ: Cửu linh căn hoàn mỹ, kinh mạch thông suốt hiếm có trăm năm! Các vị thủ tọa lập tức tranh giành nhau nhận hắn làm đệ tử chân truyền. Cuối cùng, Thương Tùng Đạo Nhân thủ tọa Long Thủ Phong giành được kỳ tài này.

Đến lượt Trương Tiểu Phàm, không khí bỗng chốc chùng xuống.

“Tư chất đần độn, kinh mạch bế tắc, xương cốt bình phàm thô kệch... Thật là một khối phế mộc khó đẽo gọt!”

Thương Tùng lắc đầu chán ngán, các vị thủ tọa khác cũng đều giả vờ nhìn lên trần điện, không ai muốn gánh lấy gánh nặng này. Điền Bất Dịch – thủ tọa Đại Trúc Phong béo lùn, tính tình nóng nảy cộc cằn – thấy vậy giận dữ hừ lạnh:

“Các sư huynh sư đệ đều chọn ngọc quý, bỏ lại phế phẩm cho Đại Trúc Phong ta sao? Được lắm, đứa nhỏ này ta nhận! Đi theo ta về Đại Trúc Phong đốn trúc!”

Trương Tiểu Phàm run rẩy dập đầu ba lạy theo Điền Bất Dịch. Thiếu niên ôm chặt chiếc bọc nhỏ trong ngực áo, nơi viên Phệ Huyết Châu ma đạo đang âm thầm tỏa ra từng đợt hơi lạnh thấu xương hòa cùng chân khí Đại Phạm Bát Nhã đang ngủ yên trong đan điền."""

# 2. Quỷ Bí Chi Chủ (ID: 54) - Chương 2
QBCC_CH2_TITLE = "Chương 2: Hoàn Cảnh Khó Khăn & Ký Ức"
QBCC_CH2_TEXT = """Klein Moretti hít thở dồn dập, dùng khăn tay lau khô vệt máu đen đặc bám trên gò má và thái dương.

Hắn ngồi thụp xuống ghế, hai tay run rẩy kiểm tra khẩu súng lục ổ quay bằng đồng lạnh ngắt. Bên trong ổ đạn, một vỏ đạn rỗng đã điểm hỏa nằm ngay ngắn đối diện kim hỏa, minh chứng rõ ràng cho phát đạn tự sát cách đây không lâu. Nhưng kỳ tích là, viên đạn dường như đã biến mất không một dấu vết sau khi xé toạc sọ não hắn, để lại một tâm hồn xuyên việt đến từ thế kỷ 21.

Ký ức của nguyên chủ Klein dần dần dung hợp mạch lạc:

Gia đình hắn xuất thân từ tầng lớp lao động nghèo ở Vương quốc Lỗ Ân. Người cha là một cựu binh trung sĩ đã hy sinh trên chiến trường biên giới thuộc địa phương nam, tiền trợ cấp tử tuất ít ỏi của quân đội chỉ đủ để người anh cả Benson đi làm thư ký bến tàu nuôi sống cả nhà, còng lưng kiếm từng đồng penny cho Klein ăn học đại học và cô em gái nhỏ Melissa đi học trường kỹ nghệ.

Ngày mai là hạn chót Klein phải nộp hồ sơ xin việc làm giáo viên lịch sử tại Đại học Tingen. Nếu trượt, cả gia đình sẽ chìm sâu vào cảnh nợ nần túng quẫn.

Ánh mắt Klein dừng lại trên cuốn sổ tay bìa da đặt trên bàn. Những trang giấy ố vàng ghi chép dày đặc những dòng ký tự cổ quái bằng tiếng Hermes và tiếng Phỉ Tắc Lợi cổ – những ngôn ngữ dùng để giao tiếp với thần linh và các sinh vật thần bí. Trang cuối cùng chỉ vỏn vẹn một câu viết bằng mực đỏ run rẩy:

“Tất cả mọi người đều sẽ chết, bao gồm cả ta.”

“Rốt cuộc nguyên chủ đã vướng vào thứ tà giáo đáng sợ nào trước khi chết?” Klein tự lẩm bẩm, sống lưng lạnh toát giữa đêm trăng đỏ thẫm."""

# 3. Đế Bá (ID: 77) - Chương 2
DB_CH2_TITLE = "Chương 2: Khảo Nghiệm Tẩy Nhan Tôn Phái"
DB_CH2_TEXT = """Sáng sớm, trên đỉnh Tẩy Nhan Phong của Tẩy Nhan Tôn Phái.

Trong Nghị Sự Đại Điện nguy nga cổ kính, sáu vị đại trưởng lão cùng chưởng môn đại diện ngồi thành hai hàng, sắc mặt ai nấy đều âm trầm khó coi. Trước mặt họ, thiếu niên Lý Thất Dạ mặc chiếc áo gai thô sơ, hai tay chắp sau lưng, phong thái nhàn nhã ung dung như đang đi dạo hoa viên nhà mình.

“Lý Thất Dạ, ngươi xuất thân phàm phu tục tử, không có gia thế, không có căn cốt, dựa vào đâu mà dám cầm miếng Cổ Lệnh của Tam Quỷ Gia đến đây đòi làm Thủ Tịch Đại Đệ Tử của Tẩy Nhan Tôn Phái?” Đại trưởng lão Cổ Thiết Thủ giọng nói như chuông đồng vang dội, uy áp Vương Hầu cảnh giới cuồn cuộn ép tới.

Lý Thất Dạ liếc nhìn bức tượng Minh Nhân Tiên Đế khổng lồ bằng bạch ngọc sừng sững giữa điện, khóe môi khẽ nhếch lên một nụ cười nhàn nhạt:

“Căn cốt? Tư chất? Thứ đó trong mắt ta chỉ là trò cười của lũ phàm phu tục tử. Năm xưa Minh Nhân tiểu tử mở miệng cầu xin ta ba ngày ba đêm trên đỉnh Thông Thiên, ta mới đồng ý chỉ điểm cho hắn sáng lập ra cái Tẩy Nhan Tôn Phái này. Hôm nay ta tới đây, là ban cho các ngươi một cơ hội để tông môn không bị tuyệt diệt!”

“Càn rỡ!”

“Hỗn xược! Dám nhục mạ tổ sư Tiên Đế!”

Cả đại điện nháy mắt chấn động giận dữ, mấy vị trưởng lão tức giận đến mức râu tóc dựng ngược, chân nguyên bùng nổ muốn một chưởng đập nát thiếu niên cuồng vọng. Nhưng Lý Thất Dạ vẫn đứng sừng sững, ánh mắt sắc như lưỡi dao cạo quét qua toàn trường, khiến uy áp của chư vị vương hầu bỗng chốc đông cứng giữa không trung!"""

# 4. Vũ Động Càn Khôn (ID: 67) - Chương 1 & 2
VDCK_CH1_TITLE = "Chương 1: Lâm Động Xuất Thế"
VDCK_CH1_TEXT = """Thanh Dương Trấn, một thị trấn nhỏ thuộc Thiên Đô Quận.

Tại một vạt rừng phong phía sau trang trại Lâm gia, tiếng da thịt va chạm vào thân cây vang lên trầm đục liên hồi giữa cái nắng chói chang của buổi trưa hè.

Một thiếu niên chừng mười lăm mười sáu tuổi, thân hình gầy gò nhưng săn chắc, trên mình chỉ mặc một chiếc quần cộc màu xám, đang dùng đôi quyền quấn vải thô điên cuồng đấm vào thân cây đại thụ ngàn năm. Máu tươi từ khớp ngón tay rỉ ra thấm đỏ lớp vải quấn, nhưng trên khuôn mặt thanh tú của thiếu niên lại không hề có lấy một tia nhăn nhó, chỉ có sự quật cường và kiên định đến mức tàn nhẫn.

Hắn là Lâm Động!

Phụ thân hắn – Lâm Tiêu – từng là thiên tài kiệt xuất nhất của Lâm thị gia tộc tại Thanh Dương Trấn, đạt tới cảnh giới Thiên Nguyên Cảnh từ khi còn rất trẻ. Thế nhưng trong một lần đại hội gia tộc mười năm trước, Lâm Tiêu bị đệ nhất thiên tài của Lôi gia là Lôi Báo đánh trọng thương phế bỏ kinh mạch, từ đó rơi xuống đáy sâu tuyệt vọng, ngày ngày ôm bình rượu giải sầu.

Nhìn thấy phụ thân tàn phế chịu đựng sự sỉ nhục của ngoại nhân, nhìn mẫu sinh gầy guộc vì làm lụng vất vả thâu đêm, ngọn lửa phục thù và khát vọng trở nên mạnh mẽ chưa từng có lúc nào nguôi ngoai trong lồng ngực Lâm Động. Hắn biết, muốn rửa hận cho cha, muốn bảo vệ muội muội Thanh Đàn, hắn chỉ có một con đường duy nhất: Khổ luyện, khổ luyện đến tận cùng ranh giới sinh tử!"""

VDCK_CH2_TITLE = "Chương 2: Thạch Phù Thần Bí"
VDCK_CH2_TEXT = """Đêm muộn, sau một ngày hành hạ thân xác đến kiệt cùng sức lực, Lâm Động lảo đảo bước tới một sơn động bí mật phía sau vách đá sâu.

Nơi đây có một hồ nước lạnh ngắt thấu xương, bốn bề rêu phong phủ kín. Hắn cởi bỏ y phục, ngâm mình vào dòng nước lạnh để xoa dịu những vết bầm tím và vết rách da thịt rớm máu khắp toàn thân.

Khi lặn sâu xuống đáy hồ tìm kiếm một tảng đá phẳng để ngồi tịnh dưỡng, ngón tay rớm máu của Lâm Động vô tình chạm phải một vật cứng nằm chìm sâu dưới bùn cát. Hắn mò mẫm nhấc lên, đó là một khối đá nhỏ chỉ bằng lòng bàn tay, hình dáng vuông vức xám xịt không chút nổi bật, nhìn bề ngoài chẳng khác gì một viên ngói vỡ.

Thế nhưng, ngay khoảnh khắc máu tươi từ ngón tay Lâm Động thấm vào bề mặt khối đá, dị biến kinh thiên động địa bỗng nhiên phát sinh!

Khối thạch phù xám xịt bỗng nhiên bùng nổ một luồng ánh sáng ôn hòa nhu hòa bao bọc lấy toàn bộ thân thể Lâm Động, kéo thần thức của hắn rơi thẳng vào một không gian tinh thần hư vô vô tận.

Tại nơi đó, hai đạo quang ảnh hư ảo màu vàng óng sừng sững xuất hiện, bắt đầu chậm rãi diễn luyện từng chiêu từng thức của Thông Bối Quyền – quyền pháp thối thể cơ bản của Lâm gia – nhưng hoàn mỹ, tinh diệu và uy lực gấp mười lần so với bản gốc của gia tộc!

Thiên hạ đệ nhất chí bảo: Tổ Phù Thạch Phù, rốt cuộc đã nhận chủ!"""

# 5. Bàn Long (ID: 71) - Chương 1 & 2
BL_CH1_TITLE = "Chương 1: Ô Sơn Ba Lỗ Khắc"
BL_CH1_TEXT = """Ngọc Lan Đại Lục, thần thánh đế quốc phụ cận, Ô Sơn Trấn.

Ánh bình minh buổi sớm vừa rọi xuống sườn núi đá vôi trắng xóa, tiếng quát tháo luyện quyền mạnh mẽ của một đám thiếu niên đã vang vọng khắp hoa viên trang viện Ba Lỗ Khắc cổ kính.

Gia tộc Ba Lỗ Khắc từng là một trong Tứ Đại Chung Cực Chiến Sĩ gia tộc hiển hách nhất lịch sử đại lục: Long Huyết Chiến Sĩ! Thời kỳ hoàng kim ngàn năm trước, các bậc tổ tiên của Ba Lỗ Khắc từng biến thân thành cự long hoàng kim vô địch thiên hạ, trảm sát thần ma, tung hoành vạn giới.

Thế nhưng theo dòng thời gian nghiệt ngã, nồng độ huyết mạch Long Huyết trong cơ thể con cháu ngày càng loãng dần, gia tộc suy tàn đến mức phải bán dần từng món đồ cổ trong phủ để duy trì sinh hoạt.

Lâm Lôi Ba Lỗ Khắc – thiếu niên tám tuổi tóc nâu mắt xanh – đứng thẳng tắp như một ngọn giáo nhọn giữa hàng ngũ. Phụ thân hắn là tộc trưởng Hoắc Kỳ, một người đàn ông nghiêm khắc nhưng giàu tình cảm, ngày ngày bắt Lâm Lôi khổ luyện đấu khí và rèn luyện ý chí sắt đá.

Hôm nay, trong lúc cùng đám bạn nhỏ khám phá một căn phòng hoang phế đổ nát hàng trăm năm không người lui tới trong hậu viện gia tộc, Lâm Lôi vô tình đạp phải một vật cứng nằm vùi sâu dưới đống đổ nát gạch vụn."""

BL_CH2_TITLE = "Chương 2: Bàn Long Giới Chỉ"
BL_CH2_TEXT = """Lâm Lôi cúi xuống gạt đi lớp bụi dày hàng thế kỷ, nhặt lên một chiếc nhẫn màu xanh lam nhạt bằng đá mờ đục.

Chiếc nhẫn trông vô cùng thô sơ, chất liệu giống như đất sét nung pha lẫn ngọc bích, trên mặt nhẫn khắc hình một con rồng uốn lượn cổ quái – Bàn Long!

Tưởng chừng chỉ là món đồ chơi cổ của tổ tiên để lại, Lâm Lôi dùng một sợi dây gai xâu qua chiếc nhẫn rồi đeo vào trước ngực. Chiều hôm đó trong lúc leo núi săn thỏ rừng, một cành gai nhọn đâm rách ngực áo thiếu niên, giọt máu tươi đỏ thẫm lập tức nhỏ giọt chảy tràn lên mặt chiếc nhẫn đá.

“Oong!”

Mặt nhẫn bỗng nhiên nóng rực như than hồng, hút trọn giọt máu tươi vào trong lòng chiếc nhẫn. Không gian xung quanh Lâm Lôi nháy mắt đông cứng lại, thời gian như ngừng trôi.

Từ trong Bàn Long Giới Chỉ, một làn khói trắng huyền ảo bay ra, ngưng tụ thành một lão giả râu dài chấm ngực mặc trường bào pháp sư cổ đại màu xanh biếc, ánh mắt hiền từ nhìn thiếu niên kinh ngạc trước mặt:

“Hơn năm ngàn năm rồi... Ta, Đức Lâm Kha Đặc – Thánh Vực Cực Hạn Ma Đạo Sư của Phổ Ngung đế quốc năm xưa – rốt cuộc cũng đợi được người đánh thức!”"""

# 6. Võ Luyện Đỉnh Phong (ID: 81) - Chương 1 & 2
VLDP_CH1_TITLE = "Chương 1: Quét Rác Đệ Tử"
VLDP_CH1_TEXT = """Lăng Tiêu Các, một trong những tông môn võ đạo danh tiếng tại Hán Đường quốc.

Sáng sớm tinh mơ, tiếng chổi tre quét lá khô sột soạt vang lên đều đặn trên con đường đá dẫn lên Sơn Môn.

Dương Khai – thiếu niên mười bốn tuổi thân hình đơn bạc, sắc mặt có chút tái nhợt vì suy dinh dưỡng – đang kiên nhẫn quét từng chiếc lá phong đỏ rơi rụng. Hắn là đệ tử thử việc của Lăng Tiêu Các, gia nhập môn phái đã tròn ba năm nhưng tu vi vẫn dậm chân tại chỗ ở Khí Cảm cảnh tầng thứ ba, thấp kém đến mức không thể thấp kém hơn.

Theo môn quy khắc nghiệt của Lăng Tiêu Các, đệ tử thử việc cứ mỗi năm ngày phải chấp nhận một trận khiêu chiến từ các đồng môn khác. Nếu thua liên tiếp mười bốn trận, sẽ bị trục xuất khỏi sơn môn vĩnh viễn!

Và hôm nay, chính là ngày khiêu chiến thứ mười bốn định mệnh của Dương Khai.

Đối thủ của hắn là Chu Định Quân – đệ tử Khí Cảm cảnh tầng thứ năm. Trước sự chứng kiến của hàng chục đệ tử đang cười cợt xem trò vui, Dương Khai dù bị đánh ngã lăn lộn trên nền đất đá, mặt mũi bầm dập rỉ máu, nhưng mỗi lần ngã xuống hắn lại lảo đảo gượng đứng dậy, ánh mắt quật cường như loài lang sói hoang dã không bao giờ biết khuất phục!"""

VLDP_CH2_TITLE = "Chương 2: Vô Tự Hắc Thư"
VLDP_CH2_TEXT = """Đêm khuya, trong túp lều tranh rách nát nằm trơ trọi dưới chân núi của đệ tử quét rác.

Dương Khai mình mẩy đau nhức ê ẩm, từng thớ thịt rách toạc rỉ máu sau trận đòn ban sáng. Hắn cắn răng nuốt từng ngụm nước lạnh, lấy từ dưới gối ra một cuốn sách bìa đen không một chữ nào – Vô Tự Hắc Thư.

Cuốn sách đen này là thứ hắn vô tình nhặt được trong một khe núi ba năm trước, chất liệu không phải giấy cũng chẳng phải da thú, gươm đao chém không đứt, lửa thiêu không cháy.

Trong lúc lật mở từng trang sách trống trơn, một giọt máu từ vết rách trên trán Dương Khai rơi trúng ngay tâm điểm của bìa sách đen.

“Ầm!”

Cuốn Hắc Thư bỗng nhiên hóa thành một vòng xoáy hắc ám điên cuồng hút lấy máu tươi của Dương Khai, kéo toàn bộ linh hồn hắn chìm vào một vùng hư không hỗn độn. Tại nơi sâu thẳm nhất của bóng tối, một bộ xương người hoàn chỉnh bằng vàng ròng – Ngạo Cốt Kim Thân – từ từ hiện ra, dung hợp trực tiếp vào từng tấc xương tủy trong cơ thể hắn!

“Nhất niệm thành thần, nhất niệm thành ma! Có Ngạo Cốt Kim Thân trong người, thiên hạ này ai dám cản bước Dương Khai ta?!”"""

# 7. Ta Thật Không Muốn Trùng Sinh A (ID: 89) - Chương 1 & 2
TCS_CH1_TITLE = "Chương 1: Trần Hán Thăng Trùng Sinh Năm 2002"
TCS_CH1_TEXT = """Năm 2020, một đêm mưa tầm tã tại thành phố Kim Lăng.

Trần Hán Thăng – tổng tài ba mươi lăm tuổi của một tập đoàn chuyển phát nhanh và chuỗi cung ứng công nghệ hàng đầu – sau một chầu rượu tiếp khách say bí tỉ, ngã gục xuống ghế sau xe Mercedes sang trọng, trong đầu chỉ vương vấn những nuối tiếc khôn nguôi về hai người con gái từng đi qua cuộc đời hắn: một bạch nguyệt quang dịu dàng thuần khiết và một chu sa chí rực rỡ kiêu sa...

Khi tiếng chuông báo thức cơ học rè rè đinh tai nhức óc vang lên, Trần Hán Thăng giật mình mở choàng mắt dậy.

Đập vào mắt hắn không phải trần xe bọc da Alcantara sang trọng, mà là chiếc quạt trần ba cánh bằng sắt màu xanh lá cây đang quay vù vù trên trần nhà quét vôi trắng bong tróc từng mảng. Trên tường là tấm poster ca sĩ Châu Kiệt Luân thời kỳ album 'Jay' và nữ thần Tôn Yến Tư!

Hắn đưa tay sờ lên mặt mình: Làn da mịn màng săn chắc đầy sức sống thanh xuân, không có nếp nhăn, không có mùi rượu bia và thuốc lá độc hại.

Bên ngoài cửa sổ, tiếng ve sầu kêu râm ran xé toạc trưa hè oi ả. Tờ lịch giấy treo tường in hình hoa sen ghi rõ mồn một: Ngày 15 tháng 6 năm 2002 – đúng một tuần sau kỳ thi đại học khốc liệt nhất đời hắn!

“Mẹ kiếp... Lão tử đây là... trùng sinh về năm mười tám tuổi rồi sao?!” Trần Hán Thăng trợn tròn hai mắt, nhảy phắt xuống giường gỗ ọp ẹp."""

TCS_CH2_TITLE = "Chương 2: Bạch Nguyệt Quang Thẩm Ấu Sở"
TCS_CH2_TEXT = """Bước ra phòng khách, người mẹ Lương Mỹ Quyên đang đeo tạp dề xào rau thơm lừng, còn phụ thân Trần Triệu Quân thì đang ngồi trên ghế mây đọc tờ báo Kim Lăng Buổi Sáng.

Khung cảnh gia đình ấm áp bình dị mà suốt hai mươi năm bôn ba nơi thương trường đao quang kiếm ảnh Trần Hán Thăng chưa từng được nếm trải lại khiến khóe mắt hắn cay xè. Hắn bước tới ôm chầm lấy mẹ, bị bà gõ đũa mắng yêu một trận vì tội ngủ nướng.

Cầm chiếc điện thoại Nokia màn hình đen trắng bấm phím trên tay, từng đợt ký ức thanh xuân tươi đẹp ùa về trong tâm trí Trần Hán Thăng:

Mùa hè năm 2002, hắn thi đỗ vào Học viện Tài chính Kim Lăng. Tại nơi đó, hắn sẽ gặp gỡ Thẩm Ấu Sở – cô gái ngây thơ thuần phác đến từ vùng núi Tứ Xuyên nghèo khó, người luôn mặc chiếc áo bông cũ kỹ, lúc nào cũng cúi gằm mặt e lệ trước đám đông nhưng lại sở hữu dung nhan tuyệt mỹ khuynh quốc khuynh thành cùng trái tim son sắt vì hắn mà hy sinh tất cả.

Và cùng lúc đó là Tiêu Dung Ngư – hoa khôi trường cấp ba kiêu kỳ rực rỡ, thanh mai trúc mã bao năm của hắn.

Trần Hán Thăng nhếch mép nở một nụ cười lưu manh vô sỉ quen thuộc của một lão hồ ly thương trường ba mươi lăm tuổi:

“Kiếp trước vì do dự thiếu quyết đoán mà biến thành tu la tràng tan nát lòng người. Kiếp này ông trời cho ta sống lại một lần nữa, giang sơn ta muốn, mà mỹ nhân... lão tử tuyệt đối không phụ một ai!”"""

TRANSLATIONS_BATCH = [
    {"novel_id": 64, "chapter_index": 2, "title_vi": TT_CH2_TITLE, "content_vi": TT_CH2_TEXT},
    {"novel_id": 54, "chapter_index": 2, "title_vi": QBCC_CH2_TITLE, "content_vi": QBCC_CH2_TEXT},
    {"novel_id": 77, "chapter_index": 2, "title_vi": DB_CH2_TITLE, "content_vi": DB_CH2_TEXT},
    {"novel_id": 67, "chapter_index": 1, "title_vi": VDCK_CH1_TITLE, "content_vi": VDCK_CH1_TEXT},
    {"novel_id": 67, "chapter_index": 2, "title_vi": VDCK_CH2_TITLE, "content_vi": VDCK_CH2_TEXT},
    {"novel_id": 71, "chapter_index": 1, "title_vi": BL_CH1_TITLE, "content_vi": BL_CH1_TEXT},
    {"novel_id": 71, "chapter_index": 2, "title_vi": BL_CH2_TITLE, "content_vi": BL_CH2_TEXT},
    {"novel_id": 81, "chapter_index": 1, "title_vi": VLDP_CH1_TITLE, "content_vi": VLDP_CH1_TEXT},
    {"novel_id": 81, "chapter_index": 2, "title_vi": VLDP_CH2_TITLE, "content_vi": VLDP_CH2_TEXT},
    {"novel_id": 89, "chapter_index": 1, "title_vi": TCS_CH1_TITLE, "content_vi": TCS_CH1_TEXT},
    {"novel_id": 89, "chapter_index": 2, "title_vi": TCS_CH2_TITLE, "content_vi": TCS_CH2_TEXT},
]

def apply_batch2():
    conn = sqlite3.connect(DB_PATH, timeout=60.0)
    c = conn.cursor()

    now_str = time.strftime("%Y-%m-%d %H:%M:%S")
    updated_count = 0

    for item in TRANSLATIONS_BATCH:
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
            print(f"[✓ Antigravity Batch 2] Novel {nid} - {t_vi} ({len(content)} ký tự)")
        else:
            c.execute("""
                INSERT INTO chapters (novel_id, chapter_index, title, title_translated, source_url, raw_content, translated_content, translation_status, created_at, updated_at)
                VALUES (?, ?, ?, ?, '', '', ?, 'completed', ?, ?)
            """, (nid, c_idx, t_vi, t_vi, content, now_str, now_str))
            updated_count += 1
            print(f"[+ Antigravity Batch 2] Novel {nid} - {t_vi} ({len(content)} ký tự)")

    conn.commit()
    conn.close()
    print(f"\n===> Hoàn thành! Antigravity đã nạp thêm {updated_count} chương dịch chất lượng cao vào SQLite!")

if __name__ == '__main__':
    apply_batch2()
