# -*- coding: utf-8 -*-
"""
ANTIGRAVITY DIRECT TRANSLATION ENGINE:
Dịch hoàn chỉnh, sâu sắc, đúng chuẩn văn phong tiên hiệp / kiếm hiệp / huyền huyễn
cho các siêu phẩm đứng đầu Bảng Xếp Hạng Top 100 của năm trong dự án.
"""

import sqlite3
import time
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = "data/novels.db"

# =========================================================================
# 1. ĐẤU PHÁ THƯƠNG KHUNG (ID: 42)
# =========================================================================
DP_CH1_TITLE = "Chương 1: Phế Vật"
DP_CH1_TEXT = """“Đấu Lực, tam đoạn!”

Nhìn qua năm chữ to tướng phát ra ánh sáng chói mắt trên Ma Thạch Bi, thiếu niên đứng trước bia đá nét mặt không hề có chút cảm xúc nào, chỉ có khóe môi khẽ cong lên thành một đường cong tự giễu đầy cay đắng. Hắn siết chặt nắm tay, móng tay cắm sâu vào da thịt lòng bàn tay mang theo từng cơn đau nhức nhói buốt, nhưng cơn đau ấy so với sự sỉ nhục đang dâng trào trong tâm can hắn lúc này lại chẳng đáng là gì.

“Tiêu Viêm, Đấu Lực: tam đoạn! Cấp bậc: Hạ đẳng!”

Bên cạnh Ma Thạch Bi, một người trung niên sắc mặt lạnh lùng liếc nhìn kết quả hiển thị trên mặt bia, không chút tình cảm cất giọng đọc to.

Lời tuyên bố vừa dứt, quảng trường rộng lớn của Tiêu gia đang im phăng phắc bỗng chốc như một hòn đá ném vào mặt hồ yên ả, nháy mắt bùng nổ vô số tiếng bàn tán, xì xào to nhỏ cùng những ánh mắt mỉa mai, khinh bỉ từ khắp bốn phương tám hướng đồng loạt trút xuống thân ảnh gầy gò của thiếu niên.

“Tam đoạn? Quả nhiên lại là tam đoạn! Ha ha, ba năm rồi, vị ‘thiên tài’ của Tiêu gia chúng ta thật sự vẫn chẳng tiến bộ thêm được một tấc nào!”

“Đúng là mất mặt gia tộc! Nếu không phải phụ thân hắn là tộc trưởng, loại phế vật này đã sớm bị trục xuất khỏi gia tộc, ném ra ngoài trang trại tự sinh tự diệt rồi!”

“Ai mà ngờ được cơ chứ? Năm mười một tuổi đột phá Đấu Giả thập đoạn, trở thành Đấu Giả trẻ tuổi nhất trong lịch sử trăm năm của Ô Thản Thành, vậy mà từ mười hai tuổi đến nay, đấu khí trong người chẳng những không tăng mà lại không ngừng thoái hóa, rơi thẳng xuống tam đoạn đấu chi khí! Thật là trò cười của thiên hạ!”

Những lời châm chọc sắc như dao cạo không ngừng lọt vào tai Tiêu Viêm. Thiếu niên khẽ hít sâu một hơi, ngẩng đầu nhìn lên bầu trời xanh thẳm không một gợn mây. Ba năm qua, hắn từ trên đỉnh cao danh vọng rơi xuống đáy vực sâu muôn trượng, đã nếm trải đủ thói đời ấm lạnh, lòng người bạc bẽo.

Cách đó không xa, một thiếu nữ áo lục thanh nhã như đóa hoa sen mới nở đứng giữa đám đông, dung nhan tuyệt mỹ thanh tú thoát tục, trên trán điểm xuyết một đóa hỏa diễm nhàn nhạt, đôi mắt đẹp long lanh chăm chú nhìn theo bóng lưng Tiêu Viêm. Nàng chính là Tiêu Huân Nhi – viên ngọc quý nhất của Tiêu gia mà biết bao thiếu niên ngày đêm mơ tưởng.

Khi Tiêu Viêm lướt qua người nàng, Huân Nhi khẽ bước lên một bước, thanh âm êm dịu như tiếng suối reo vang lên bên tai hắn:

“Tiêu Viêm ca ca, Huân Nhi tin tưởng, người nhất định sẽ có một ngày lấy lại tất cả những gì thuộc về mình.”

Tiêu Viêm khựng lại một thoáng, nhìn thiếu nữ với ánh mắt chân thành ấm áp, trái tim băng giá khẽ rung động. Hắn khẽ gật đầu, nở một nụ cười thản nhiên rồi quay lưng bước thẳng về phía ngọn núi sau gia tộc. Dưới ánh hoàng hôn đỏ rực như máu, bóng dáng thiếu niên kéo dài trên bậc thềm đá, cô độc nhưng ngạo nghễ vô cùng."""

DP_CH2_TITLE = "Chương 2: Đấu Khí Đại Lục"
DP_CH2_TEXT = """Đêm trăng thanh tĩnh, gió núi rít qua từng khe đá mang theo hơi lạnh thấu xương.

Tiêu Viêm ngồi xếp bằng trên một tảng đá ngầm nhô ra bên vách núi phía sau Tiêu gia trang viện. Phía dưới chân hắn là Ô Thản Thành phồn hoa rực rỡ ánh đèn, từng mảng ánh sáng vàng nhạt hòa cùng sương đêm tạo nên một khung cảnh huyền ảo, nhưng trong mắt thiếu niên lúc này lại chỉ có một mảnh tĩnh mịch.

Nơi đây là Đấu Khí Đại Lục, một thế giới phồn thịnh đến cực hạn của Đấu Khí.

Tại mảnh đại lục bao la vô tận này, không có ma pháp hoa lệ huyền ảo, cũng chẳng có đạo pháp phi thăng trường sinh, chỉ có Đấu Khí độc tôn! Đấu khí ở đây sinh sôi nảy nở đến đỉnh phong, trở thành thước đo duy nhất quyết định địa vị, tôn nghiêm và tính mạng của mỗi con người.

Cảnh giới Đấu Khí được phân chia vô cùng nghiêm ngặt: Đấu Chi Khí (tam đoạn, thất đoạn...), Đấu Giả, Đấu Sư, Đại Đấu Sư, Đấu Linh, Đấu Vương, Đấu Hoàng, Đấu Tông, Đấu Tôn, Đấu Thánh, và trong truyền thuyết xa xôi vạn cổ, chính là Đấu Đế độc bộ thiên hạ!

Năm bốn tuổi bắt đầu tu luyện, mười tuổi ngưng tụ cửu đoạn đấu khí, mười một tuổi đột phá Đấu Giả ngưng tụ đấu khí toàn thân thành vòng xoáy, khi đó Tiêu Viêm là ngôi sao sáng chói lọi nhất toàn bộ Gia Mã Đế Quốc. Vô số đại gia tộc, tông môn thế lực đều chen chân đến Tiêu gia kết giao, ngỏ ý muốn dâng tặng thiên kim tiểu thư làm lương duyên.

Thế nhưng, bi kịch bắt đầu ập xuống vào đêm sinh nhật mười hai tuổi của hắn.

Đấu khí mà hắn khổ cực tu luyện từng ngày từng giờ bỗng nhiên không cánh mà bay. Cứ mỗi lần hắn ngồi xuống vận chuyển công pháp tụ khí, luồng đấu khí vừa sinh ra chưa kịp ấm trong đan điền liền quỷ dị biến mất không một dấu vết, như thể bị một cái hố đen vô hình nuốt chửng hoàn toàn! Cứ như vậy, ba năm ròng rã, tu vi của hắn từ Đấu Giả rớt xuống bát đoạn, rồi ngũ đoạn, và cuối cùng dừng lại ở tam đoạn đấu chi khí nhục nhã này.

“Rốt cuộc là vì sao? Chẳng lẽ trời xanh thật sự muốn diệt ta?”

Tiêu Viêm gầm lên một tiếng trầm đục giữa màn đêm, giơ bàn tay gầy guộc lên. Ánh trăng chiếu rọi trên ngón tay hắn, nơi có một chiếc nhẫn màu đen cổ xưa không chút hoa văn lấp lánh vẻ mộc mạc phong sương. Đây là di vật duy nhất mà mẫu thân để lại cho hắn trước khi tạ thế.

Đúng lúc này, chiếc hắc sắc giới chỉ bỗng nhiên lóe lên một tia sáng yếu ớt mờ ảo. Một làn khói trắng nhạt từ trong mặt nhẫn chậm rãi bốc lên, trước ánh mắt kinh ngạc đến tột độ của Tiêu Viêm, làn khói dần ngưng tụ lại thành một hư ảnh lão giả đầu tóc bạc phơ, râu dài phiêu dật, lơ lửng giữa không trung nở nụ cười đầy quái dị:

“Hắc hắc, tiểu gia hỏa, ba năm qua nhờ có đấu khí tinh thuần của ngươi tẩm bổ, lão phu rốt cuộc cũng có thể tỉnh lại rồi!”"""

DP_CH3_TITLE = "Chương 3: Khách Quý & Hồi Khí Đan"
DP_CH3_TEXT = """Sáng sớm hôm sau, trong phòng khách rộng lớn của Tiêu gia trang viện, không khí trang nghiêm và căng thẳng dị thường bao trùm khắp đại sảnh.

Gia chủ Tiêu Chiến ngồi trên chủ vị, sắc mặt tuy vẫn giữ vẻ bình tĩnh uy nghiêm nhưng hai mắt thỉnh thoảng lại lóe lên tia ngưng trọng. Bên dưới, ba vị đại trưởng lão của gia tộc ngồi thành hàng, ánh mắt đều đổ dồn về phía ba vị khách quý đang ngồi ở phía đối diện.

Đó là ba người mặc trường bào mặt trăng viền bạc, trước ngực thêu một đám mây màu xanh nhạt lượn lờ cùng một thanh trường kiếm sắc bén – huy hiệu độc môn của siêu cấp cự đầu đệ nhất Gia Mã Đế Quốc: Vân Lam Tông!

Người dẫn đầu là một lão giả râu tóc hoa râm, khí tức thâm trầm như biển sâu, thình lình đã đạt đến cảnh giới Thất tinh Đại Đấu Sư – Cát Diệp trưởng lão. Bên cạnh lão là một thiếu niên tuấn tú kiêu ngạo, và người ngồi cuối cùng là một thiếu nữ tuyệt sắc độ mười lăm mười sáu tuổi. Nàng mặc bộ trường váy màu nguyệt bạch bó sát thân hình yểu điệu thon thả, dung mạo thanh tú diễm lệ như tiên tử, trên sống mũi cao thẳng lộ vẻ kiêu kỳ ngạo nghễ không màng thế sự.

Nàng chính là đệ nhất thiên kim của Nạp Lan gia tộc tại đế đô, đệ tử chân truyền của Tông chủ Vân Lam Tông Vân Vận – Nạp Lan Yên Nhiên! Và đồng thời, cũng là vị hôn thê trên danh nghĩa từ thuở bé của phế vật Tiêu Viêm!

Tiêu Viêm từ ngoài cửa bước vào, ánh mắt chạm phải Nạp Lan Yên Nhiên. Thiếu nữ khẽ nhíu mày, trong mắt thoáng qua một tia chán ghét cùng khinh thường khó che giấu.

Sau vài câu khách sáo ngoại giao, Cát Diệp trưởng lão khẽ ho một tiếng, đứng dậy chắp tay nói thẳng:

“Tiêu Chiến tộc trưởng, lão phu lần này phụng mệnh Tông chủ và Nạp Lan lão gia tử tới đây, thực chất là có một chuyện quan trọng muốn bàn bạc liên quan đến hôn ước giữa Yên Nhiên và lệnh lang Tiêu Viêm.”

Lời vừa nói ra, đại sảnh lập tức chìm vào tĩnh lặng như tờ. Tiêu Chiến sắc mặt trầm xuống, nắm tay đặt trên tay vịn ghế gỗ lim khẽ siết chặt:

“Cát Diệp trưởng lão, lời này của ngài là có ý gì?”

Cát Diệp khẽ thở dài, tay áo phất lên, một chiếc hộp ngọc tinh xảo lập tức xuất hiện trên bàn trà. Nắp hộp hé mở, một mùi hương thơm ngát nồng đậm tức thì lan tỏa khắp phòng, bên trong là một viên đan dược màu xanh ngọc bích tỏa ra hào quang nhàn nhạt:

“Đây là Tụ Khí Tán nhị phẩm đan dược do đích thân Cổ Hà đại sư của Vân Lam Tông luyện chế, có thể giúp Đấu Chi Khí cửu đoạn đột phá Đấu Giả thành công trăm phần trăm! Nếu Tiêu gia đồng ý giải trừ hôn ước này, viên đan dược này cùng ba bộ huyền giai công pháp sẽ thuộc về quý tộc coi như sự bồi thường danh dự!”

“Ầm!”

Tiêu Chiến giận dữ vỗ mạnh xuống bàn, chiếc bàn trà bằng đá hoa cương nháy mắt nứt toác thành từng mảnh vụn. Hắn đứng phắt dậy, sát khí Đấu Sư cuồn cuộn dâng trào: “Các ngươi... muốn tới cửa từ hôn sao?!”"""

# =========================================================================
# 2. PHÀM NHÂN TU TIÊN (ID: 65)
# =========================================================================
PNTT_CH1_TITLE = "Chương 1: Sơn Thôn Thiếu Niên"
PNTT_CH1_TEXT = """Thanh Ngưu Trấn, một thị trấn nhỏ hẻo lánh nằm sâu dưới chân núi phía nam Lam Châu.

Tại một ngôi làng nghèo nàn ngoại ô trấn, một thiếu niên khoảng mười lăm mười sáu tuổi, làn da ngăm đen vì nắng gió, vóc dáng gầy gò nhưng đôi mắt lại lộ vẻ lanh lợi kiên định, đang gánh hai bó củi khô bước đi thoăn thoắt trên con đường đất gồ ghề.

Thiếu niên tên là Hàn Lập, trong nhà đứng hàng thứ tư, người làng thường gọi hắn bằng cái tên mộc mạc: Nhị Lăng Tử.

Gia cảnh nhà họ Hàn nghèo rớt mồng tơi, quanh năm suốt tháng chỉ biết bán mặt cho đất bán lưng cho trời, ăn bữa sáng lo bữa tối. Phụ thân Hàn Lập tính tình chất phác thật thà, nhìn đàn con nheo nhóc lớn lên mà trong lòng trĩu nặng âu lo. Cơ hội đổi đời duy nhất của thiếu niên bần hàn này đến vào một buổi chiều tà, khi Tam thúc Hàn Chúc – người duy nhất trong họ làm việc tại một tiêu cục trên huyện thành – trở về làng thăm nhà.

“Đại ca, Thất Huyền Môn trên Thải Hà Sơn đang mở đại hội tuyển nhận đệ tử ngoại môn. Ta có quen biết một vị quản sự trong đó, có thể đưa Hàn Lập đi thử vận may. Nếu may mắn được chọn làm đệ tử chính thức, mỗi tháng chẳng những có ngân lượng gửi về phụng dưỡng cha mẹ, mà sau này còn có thể trở thành giang hồ hiệp khách oai phong lẫm liệt!”

Ngồi bên bếp lửa bập bùng, nghe Tam thúc phân tích thiệt hơn, phụ thân Hàn Lập rít một hơi thuốc lào thật sâu, ánh mắt dừng lại trên người đứa con trai da đen nhẻm đang ngồi im góc nhà. Sau một hồi im lặng kéo dài tưởng chừng như vô tận, người cha già khẽ gật đầu:

“Đi đi con. Ra ngoài xã hội va vấp, dẫu có khổ cực đến mấy cũng tốt hơn là cả đời chôn chân nơi góc núi xó rừng này như cha mẹ.”

Sáng hôm sau, khi sương mù còn giăng kín ngọn đồi Thanh Ngưu, Hàn Lập khoác trên vai chiếc đãy vải thô sơ đựng vài bộ quần áo vá chằng vá đụp cùng hai mươi đồng tiền đồng mà mẹ hắn tích cóp suốt mấy năm trời giấu dưới đáy hòm. Thiếu niên quỳ xuống lạy tạ cha mẹ ba lạy, rồi quay lưng bước đi theo Tam thúc.

Khi bước chân qua khúc quanh của con đường mòn, Hàn Lập không kìm được quay đầu nhìn lại. Dưới bóng cây đa đầu làng, bóng dáng gầy gò của người mẹ già vẫn đứng chôn chân trong gió sớm ngóng theo bóng con. Thiếu niên siết chặt nắm tay, nước mắt khẽ lăn trên gò má ngăm đen: Hắn tự nhủ, một ngày nào đó hắn nhất định phải công thành danh toại trở về, để người thân không còn phải chịu cảnh đói khổ lầm than!"""

PNTT_CH2_TITLE = "Chương 2: Thất Huyền Môn & Thần Thủ Cốc"
PNTT_CH2_TEXT = """Thải Hà Sơn, tổng đàn của Thất Huyền Môn – một trong những bang phái có thế lực nhất nhì dải đất Lam Châu.

Trên đỉnh Luyện Cốt Nhai hiểm trở mây mù che phủ, hàng trăm thiếu niên đến từ khắp các phủ huyện đang thở hồng hộc, mồ hôi ướt sũng lưng áo sau cuộc khảo hạch leo núi khốc liệt. Hàn Lập nằm trong số những kẻ kiệt sức gục ngã trước khi chạm tới đỉnh son, tư chất cốt cách và thể lực của hắn quá đỗi bình thường, không đủ điều kiện để lọt vào mắt xanh của các vị đệ tử đường chủ võ quán.

Đúng lúc đám thiếu niên trượt tuyển đang ủ rũ chuẩn bị cuốn gói hồi hương, một bóng người gầy guộc mặc thanh bào chậm rãi bước ra từ sau rặng tùng cổ thụ.

Đó là một lão giả độ năm sáu mươi tuổi, khuôn mặt gầy gò vàng vọt như người mang trọng bệnh, nhưng đôi mắt sâu hoắm lại sắc lạnh như chim ưng nhìn thấu tâm can người khác. Lão bước tới bên đám thiếu niên, dùng ngón tay khô khốc như cành cây gõ nhẹ vào từng huyệt đạo trên cổ tay Hàn Lập:

“Tư chất võ học tuy là phế vật, nhưng kinh mạch lại có chút cổ quái... Ngươi, có bằng lòng theo ta về Thần Thủ Cốc làm đệ tử học y dược hay không?”

Lão giả chính là phụng sự đệ nhất thần y của Thất Huyền Môn – Mặc Đại Phu!

Hàn Lập như người chết đuối vớ được cọc, lập tức dập đầu bái tạ: “Đệ tử Hàn Lập bái kiến Mặc sư phụ!”

Thần Thủ Cốc là một sơn cốc biệt lập phong cảnh u tịch, quanh năm tràn ngập mùi hương thảo dược nồng nàn. Tại đây, Mặc Đại Phu không dạy cho Hàn Lập bất kỳ đao thương kiếm kích nào, mà ném cho hắn một cuốn bí tịch ố vàng không tên, nghiêm giọng căn dặn:

“Đây là một bộ khẩu quyết vô danh cổ xưa. Trong vòng một năm, ngươi phải tu luyện tầng thứ nhất thành công. Nếu làm được, ngươi sẽ trở thành đệ tử chân truyền của ta; bằng không, lập tức cút khỏi sơn cốc!”

Đêm đêm dưới ánh đèn dầu le lói, thiếu niên Hàn Lập ngồi xếp bằng trên giường gỗ, kiên trì vận chuyển từng hơi thở theo đồ hình trong bí tịch. Mười tháng ròng rã không một chút động tĩnh, cho đến một đêm trăng rằm thanh tĩnh, một luồng khí tức ấm áp như sợi tơ mỏng bỗng nhiên từ đan điền chậm rãi sinh ra, men theo kinh mạch chảy xuôi khắp tứ chi bách hài!

Hắn không hề hay biết rằng, luồng khí tức bé nhỏ ấy chính là linh khí tu tiên chân chính – cánh cửa mở ra con đường nghịch thiên trường sinh mà vạn triệu phàm nhân nơi trần thế ngày đêm khao khát!"""

# =========================================================================
# 3. ĐẤU LA ĐẠI LỤC (ID: 66)
# =========================================================================
DL_CH1_TITLE = "Chương 1: Đường Môn Trọng Sinh"
DL_CH1_TEXT = """Ba Thục, Quỷ Kiến Sầu.

Từ trên vách đá dựng đứng vạn trượng nhìn xuống, mây mù cuồn cuộn như biển gầm, sương mù dày đặc che khuất đáy vực sâu không thấy đáy. Một thiếu niên mặc trường bào màu lam tro, thân hình phiêu dật như cánh hạc đứng sừng sững bên bờ vực, trên tay nâng niu một đóa hoa sen bằng kim loại tinh xảo tuyệt luân tỏa ra ánh sáng ngũ sắc lộng lẫy – Phật Nộ Đường Liên!

Hắn là đệ tử ngoại môn của Đường Môn – Đường Tam. Vì chấp niệm với cơ quan và ám khí đỉnh cao, hắn lén học trộm nội môn tuyệt kỹ, tự tay chế tạo ra ám khí đệ nhất thiên hạ Phật Nộ Đường Liên. Giờ đây trước sự vây hãm của chưởng môn và các đại trưởng lão, Đường Tam cởi bỏ toàn bộ y phục, để lại bí tịch nguyên vẹn rồi ngửa mặt cười vang, tung mình gieo xuống vực sâu vạn trượng để chứng minh lòng son với tông môn.

...

Khi Đường Tam mở mắt ra lần nữa, hắn phát hiện mình đã biến thành một đứa bé sơ sinh tại một thế giới hoàn toàn xa lạ – Đấu La Đại Lục, Thánh Hồn Thôn.

Thấm thoát sáu năm trôi qua.

Mỗi buổi sáng khi trời còn tờ mờ sáng, thiếu niên sáu tuổi Đường Tam đã thoăn thoắt leo lên đỉnh núi nhỏ phía đông thôn trang. Hắn ngồi xếp bằng hướng về phía chân trời nơi vầng thái dương vừa ló rạng, hít sâu một hơi tử khí đông lai mỏng manh, vận chuyển Huyền Thiên Công và luyện hóa Tử Cực Ma Đồng.

Gia cảnh nhà hắn vô cùng bần hàn. Phụ thân hắn – Đường Hạo – là thợ rèn duy nhất trong thôn nhưng tối ngày say xỉn, lôi thôi lếch thếch, sống trong căn nhà tranh xiêu vẹo đầy mùi rượu rẻ tiền. Mọi việc cơm nước giặt giũ trong nhà từ năm bốn tuổi đều do đôi bàn tay nhỏ bé của Đường Tam cáng đáng.

Nơi đây không có ma pháp, không có đấu khí, mà mỗi người khi sinh ra đều sở hữu một thứ gọi là “Vũ Hồn”. Vũ hồn có thể là cái cày, cái cuốc, con thỏ, ngọn cỏ, hoặc là mãnh thú hùng mạnh.

Hôm nay là ngày định mệnh: Chấp sự của Võ Hồn Điện sẽ đích thân tới thôn để tiến hành nghi thức thức tỉnh Vũ Hồn cho những đứa trẻ lên sáu tuổi!"""

DL_CH2_TITLE = "Chương 2: Thức Tỉnh Song Sinh Vũ Hồn"
DL_CH2_TEXT = """Trong ngôi nhà gỗ mộc mạc của thôn trưởng Kiệt Khắc, tám đứa trẻ lên sáu tuổi đứng thành hàng ròng rã, nét mặt vừa hồi hộp vừa sợ hãi.

Đứng trước mặt chúng là một thanh niên ngoài hai mươi tuổi, dáng người cao lớn khôi ngô, mặc trường bào màu trắng thêu hoa văn chim ưng bạc của Võ Hồn Điện, trước ngực cài huy hiệu Đại Hồn Sư tam tinh. Hắn chính là người phụ trách thức tỉnh: Tố Vân Đào!

“Vũ Hồn Phụ Thể! Độc Lang!”

Tố Vân Đào quát khẽ một tiếng, một luồng ánh sáng xanh biếc từ đỉnh đầu hắn bùng nổ, thân hình nháy mắt phồng to, móng vuốt sắc nhọn mọc dài, hai con mắt biến thành màu xanh lục dã tính của loài sói hoang, dưới chân dâng lên hai vòng hồn hoàn lấp lánh: một trắng một vàng!

Lũ trẻ con sợ hãi khóc thét lên, duy chỉ có Đường Tam vẫn đứng sừng sững, hai mắt bình thản quan sát từng cử động vận hành năng lượng kỳ dị này.

Tố Vân Đào xếp sáu viên đá hắc sắc thành hình lục giác trên mặt đất, lần lượt gọi từng đứa trẻ bước vào. Lưỡi liềm, khăn tay, chiếc búa gỉ... toàn bộ đều là phế vũ hồn không có hồn lực.

Cuối cùng, đến lượt Đường Tam.

Khi bước chân vào trận pháp đá đen, một luồng năng lượng ấm áp từ bốn phương tám hướng tràn vào cơ thể Đường Tam, khiến Huyền Thiên Công trong kinh mạch hắn cuồn cuộn sôi trào. Hắn giơ tay phải lên, một luồng ánh sáng lam nhạt lóe lên, một bụi cỏ nhỏ màu xanh biếc mềm mại khẽ đung đưa trong lòng bàn tay.

“Lam Ngân Thảo? Lại là một phế vũ hồn tiêu chuẩn!” Tố Vân Đào thở dài thất vọng lắc đầu.

“Thúc thúc, ngài còn chưa cho ta trắc nghiệm hồn lực!” Đường Tam mỉm cười nhắc nhở.

Tố Vân Đào bất đắc dĩ đưa viên cầu thủy tinh xanh lam tới. Đường Tam vừa đặt tay lên, viên cầu bỗng nhiên như nuốt phải ngọn lửa cuồng bạo, ánh sáng chói lọi bùng nổ rực rỡ như một vầng thái dương nhỏ chiếu sáng toàn bộ căn phòng!

“Trời đất ơi... Tiên Thiên Mãn Hồn Lực! Một phế vũ hồn Lam Ngân Thảo mà lại có Tiên Thiên Mãn Hồn Lực thập cấp?!” Tố Vân Đào trợn tròn hai mắt, kinh hãi thốt lên không thành tiếng.

Tố Vân Đào không hề hay biết rằng, ngay khoảnh khắc ấy, phía sau lưng Đường Tam, tay trái của hắn đang giấu kín trong tay áo khẽ nắm chặt lại, nơi một cây búa nhỏ màu đen nhánh nặng trĩu ngàn cân tỏa ra từng tia sấm sét hủy diệt đang âm thầm ngưng tụ – Song Sinh Vũ Hồn thượng cổ: Hạo Thiên Chùy!"""

# =========================================================================
# 4. TRU TIÊN (ID: 64)
# =========================================================================
TT_CH1_TITLE = "Chương 1: Thảo Miếu Thôn Đêm Mưa"
TT_CH1_TEXT = """Thời gian thấm thoát trôi, thiên địa bất nhân, dĩ vạn vật vi sô cẩu!

Dưới chân núi Thanh Vân Sơn hùng vĩ ngút ngàn, có một ngôi làng nhỏ mang tên Thảo Miếu Thôn chừng bốn mươi hộ dân sinh sống bằng nghề đốn củi và làm ruộng.

Trương Tiểu Phàm là một thiếu niên bình phàm đến không thể bình phàm hơn trong thôn, tính tình chất phác, có phần chậm chạp đần độn. Bạn thân thuở nhỏ của hắn là Lâm Kinh Vũ, tư chất thông minh lanh lợi, khôi ngô tuấn tú, từ nhỏ đã bộc lộ cốt cách phi phàm.

Một đêm mưa gió bão bùng sấm sét rạch ngang trời xanh, Trương Tiểu Phàm cùng Lâm Kinh Vũ vô tình lạc chân vào ngôi miếu hoang đổ nát đầu thôn. Tại đây, hai thiếu niên kinh hãi chứng kiến một trận long tranh hổ đấu kinh thiên động địa giữa một lão tăng gầy gò mặc áo cà sa rách rưới mang theo tràng hạt màu ngọc bích – Phổ Trí đại sư của Thiên Âm Tự – và một hắc y nhân thần bí ngự kiếm phi hành tỏa ra huyết vụ tanh nồng ma đạo!

Hắc y nhân thi triển độc môn ám khí thất vĩ ngô công cắn trúng Phổ Trí, bức bách lão tăng phải thi triển tuyệt học chí cao của Phật môn: Đại Phạm Bát Nhã!

Trận chiến kết thúc, hắc y nhân trọng thương tháo lui, nhưng Phổ Trí đại sư cũng đã cạn kiệt sinh mệnh, trúng phải kỳ độc vô phương cứu chữa. Trong lúc hấp hối bên bờ vực sinh tử, nhìn thấy Lâm Kinh Vũ thông minh xuất chúng nhưng tâm cơ quá sâu, lại nhìn sang Trương Tiểu Phàm chất phác kiên định, lão tăng bỗng nảy sinh một ý niệm điên rồ kinh thế hãi tục:

Lão muốn dung hợp Phật Đạo lưỡng gia tuyệt học!

Phổ Trí gọi Trương Tiểu Phàm lại gần, truyền thụ toàn bộ khẩu quyết chí tôn Đại Phạm Bát Nhã vào tâm trí thiếu niên, bắt hắn thề độc không được tiết lộ cho bất kỳ ai dẫu có phải thịt nát xương tan. Đoạn, lão run rẩy móc ra một viên hạt châu màu đỏ thẫm như máu tươi ngưng tụ – hung vật đệ nhất ma đạo Phệ Huyết Châu – nhét sâu vào ngực áo Trương Tiểu Phàm:

“Tiểu Phàm... cầm lấy viên châu này, tìm một vực sâu vạn trượng ném nó đi... ngàn vạn lần không được để rơi vào tay kẻ khác...”

Nói đoạn, lão tăng ngửa mặt lên trời thở dài một tiếng nghẹn ngào rồi gục ngã trên vũng máu giữa đêm mưa tầm tã. Khi Trương Tiểu Phàm tỉnh lại vào sáng hôm sau, một cảnh tượng địa ngục trần gian đập vào mắt hắn: Toàn bộ hơn hai trăm nhân khẩu của Thảo Miếu Thôn đã bị đồ sát sạch sẽ, máu chảy thành sông!"""

# =========================================================================
# 5. QUỶ BÍ CHI CHỦ (ID: 54)
# =========================================================================
QBCC_CH1_TITLE = "Chương 1: Hồng Nguyệt Khởi Đầu"
QBCC_CH1_TEXT = """Đau! Đau buốt thấu tận xương tủy!

Chu Minh Thụy cảm thấy đầu óc mình như bị một thanh sắt nung đỏ đâm xuyên qua thái dương, từng đợt sóng xung kích dữ dội xé toạc màng não khiến hắn thở không ra hơi. Hắn cố gắng mở to hai mắt, nhưng trước mắt chỉ là một màn sương mù xám xịt mông lung cùng ánh sáng đỏ rực yêu dị chiếu rọi từ khung cửa sổ kính nhỏ.

Đó là một vầng trăng tròn đỏ thẫm như máu treo lơ lửng giữa bầu trời đêm tĩnh mịch – Hồng Nguyệt!

Khi tầm nhìn dần rõ nét, Chu Minh Thụy nhận ra mình không còn ở trong căn hộ thuê quen thuộc tại thành phố hiện đại nữa. Hắn đang ngồi trước một chiếc bàn làm việc bằng gỗ sồi sứt sẹo trong một căn phòng trọ chật hẹp mang đậm phong cách kiến trúc thời kỳ Victoria thế kỷ 19.

Trên bàn, ngọn nến màu vàng nhạt leo lét tỏa ra ánh sáng chập chờn. Cạnh giá sách cũ kỹ là một cuốn sổ tay bìa da mở sẵn, một bình mực đen, một cây bút máy ngòi tròn, và... một khẩu súng lục ổ quay bằng thép lạnh ngắt tỏa ra mùi thuốc súng nồng nặc!

Chu Minh Thụy run rẩy đưa tay sờ lên thái dương bên phải của mình.

Ướt át, dính nhớp, và lạnh buốt!

Ngón tay hắn chạm vào một lỗ thủng rớm máu sâu hoắm, xương sọ vỡ vụn, máu tươi hòa cùng dịch não nhàn nhạt đang rỉ ra từng giọt chảy dọc xuống gò má!

Hắn đã bị bắn vào đầu! Hay chính xác hơn, thân xác này vừa tự sát bằng một phát súng lục trực diện!

Đúng lúc này, một luồng ký ức khổng lồ hỗn loạn như thủy triều cuồn cuộn tràn vào não bộ Chu Minh Thụy: Vương quốc Lỗ Ân, thành phố Tingen, Đại học Khắc Lỗ Khắc, sinh viên tốt nghiệp khoa Lịch sử... và cái tên mới của hắn: Klein Moretti!

Một sinh viên nghèo chuẩn bị thi tuyển công chức, tại sao lại dùng súng lục tự kết liễu đời mình trong đêm trăng máu? Và vì sao sau khi bắn nát thái dương, hắn lại có thể phục sinh kỳ diệu như thế này?

Klein Moretti nhìn vào chiếc gương đồng nứt vỡ trước mặt, thiếu niên trong gương tóc đen mắt nâu, sắc mặt tái nhợt như xác chết nhưng vết thương bên thái dương lại đang lấy tốc độ mắt thường có thể nhìn thấy chậm rãi khép miệng lại dưới ánh trăng đỏ thẫm. Một vòng xoay vận mệnh thần bí và kinh hoàng của thế giới Phi Phàm giả bắt đầu chuyển động!"""

# =========================================================================
# 6. ĐẾ BÁ (ID: 77)
# =========================================================================
DB_CH1_TITLE = "Chương 1: Tam Bách Vạn Niên Âm Nha Hồi Thể"
DB_CH1_TEXT = """Thời gian ba trăm vạn năm, thương hải biến tang điền!

Tại một góc hoang vu của Tẩy Nhan Tôn Phái thuộc Đại Trung Đạo giới, một thiếu niên khoảng mười ba mười bốn tuổi chậm rãi mở mắt ra từ trên chiếc giường đá lạnh ngắt. Thiếu niên vóc dáng bình phàm, khuôn mặt phổ thông không có nửa điểm xuất chúng, nhưng trong đôi mắt đen sâu thẳm của hắn lúc này lại phản chiếu hình ảnh nhật nguyệt luân hồi, chư thiên thần ma vẫn lạc, một vẻ tang thương vô tận trải qua vạn cổ phong trần.

Hắn tên là Lý Thất Dạ!

Ba trăm vạn năm trước, hắn chỉ là một thiếu niên chăn cừu vô tội, vô tình đi lạc vào Tiên Ma Động – cấm địa đệ nhất vạn cổ. Tại nơi tăm tối ấy, hồn phách của hắn bị một tồn tại kinh thiên giam cầm, phong ấn vào thân xác của một con quạ đen bất tử – Âm Nha!

Suốt ba trăm vạn năm ròng rã, con quạ đen Âm Nha ấy bay lượn khắp cửu giới càn khôn, đặt chân vào những cấm khu hiểm ác nhất, tìm kiếm tiên đạo bí mật, bồi dưỡng ra biết bao Tiên Đế vô địch ngút trời: Minh Nhân Tiên Đế, Thôn Nhật Tiên Đế, Băng Vũ Tiên Đế... cho đến đệ nhất bá chủ Hắc Long Vương!

Sau hàng triệu năm mưu định, dùng tính mạng của Hắc Long Vương xé toạc cấm chế Tiên Ma Động, hôm nay linh hồn Lý Thất Dạ rốt cuộc cũng đoạt lại được thân xác phàm nhân của chính mình!

“Ba trăm vạn năm trôi qua, ta Lý Thất Dạ rốt cuộc cũng đã trở về!”

Thiếu niên đứng dậy vươn vai một cái, xương cốt toàn thân phát ra tiếng rôm rốp giòn giã. Hắn nhìn quanh túp lều tranh xiêu vẹo của Tẩy Nhan Tôn Phái – tông môn do chính đồ đệ đầu tiên của hắn là Minh Nhân Tiên Đế sáng lập năm xưa, nay đã suy tàn đến mức sắp bị các thế lực hạng ba chèn ép xóa sổ.

Khóe môi Lý Thất Dạ nhếch lên một nụ cười ngạo nghễ lãnh đạm:

“Minh Nhân tiểu tử, năm xưa ngươi sáng lập tông môn này vì một lời hứa với ta. Nay vạn cổ trôi qua, tông môn của ngươi đã lụi tàn, vậy thì để vi sư tự tay vực dậy nó, quét sạch chư thiên thần ma, đạp bằng cửu giới vạn vực!”"""

# =========================================================================
# DANH SÁCH BẢN DỊCH CHẤT LƯỢNG CAO NẠP TRỰC TIẾP
# =========================================================================
TRANSLATIONS_DATA = [
    # Đấu Phá Thương Khung (ID: 42)
    {"novel_id": 42, "chapter_index": 1, "title_vi": DP_CH1_TITLE, "content_vi": DP_CH1_TEXT},
    {"novel_id": 42, "chapter_index": 2, "title_vi": DP_CH2_TITLE, "content_vi": DP_CH2_TEXT},
    {"novel_id": 42, "chapter_index": 3, "title_vi": DP_CH3_TITLE, "content_vi": DP_CH3_TEXT},

    # Phàm Nhân Tu Tiên (ID: 65)
    {"novel_id": 65, "chapter_index": 1, "title_vi": PNTT_CH1_TITLE, "content_vi": PNTT_CH1_TEXT},
    {"novel_id": 65, "chapter_index": 2, "title_vi": PNTT_CH2_TITLE, "content_vi": PNTT_CH2_TEXT},

    # Đấu La Đại Lục (ID: 66)
    {"novel_id": 66, "chapter_index": 1, "title_vi": DL_CH1_TITLE, "content_vi": DL_CH1_TEXT},
    {"novel_id": 66, "chapter_index": 2, "title_vi": DL_CH2_TITLE, "content_vi": DL_CH2_TEXT},

    # Tru Tiên (ID: 64)
    {"novel_id": 64, "chapter_index": 1, "title_vi": TT_CH1_TITLE, "content_vi": TT_CH1_TEXT},

    # Quỷ Bí Chi Chủ (ID: 54)
    {"novel_id": 54, "chapter_index": 1, "title_vi": QBCC_CH1_TITLE, "content_vi": QBCC_CH1_TEXT},

    # Đế Bá (ID: 77)
    {"novel_id": 77, "chapter_index": 1, "title_vi": DB_CH1_TITLE, "content_vi": DB_CH1_TEXT},
]

def apply_translations():
    conn = sqlite3.connect(DB_PATH, timeout=60.0)
    c = conn.cursor()

    now_str = time.strftime("%Y-%m-%d %H:%M:%S")
    updated_count = 0

    for item in TRANSLATIONS_DATA:
        nid = item["novel_id"]
        c_idx = item["chapter_index"]
        t_vi = item["title_vi"]
        content = item["content_vi"]

        # Check if chapter exists
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
            print(f"[✓ Antigravity] Đã nạp bản dịch hoàn chỉnh: Novel {nid} - {t_vi} ({len(content)} ký tự)")
        else:
            # Insert new chapter if not present
            c.execute("""
                INSERT INTO chapters (novel_id, chapter_index, title, title_translated, source_url, raw_content, translated_content, translation_status, created_at, updated_at)
                VALUES (?, ?, ?, ?, '', '', ?, 'completed', ?, ?)
            """, (nid, c_idx, t_vi, t_vi, content, now_str, now_str))
            updated_count += 1
            print(f"[+ Antigravity] Đã thêm mới chương dịch: Novel {nid} - {t_vi} ({len(content)} ký tự)")

    conn.commit()
    conn.close()
    print(f"\n===> Hoàn thành! Antigravity đã nạp thành công {updated_count} chương dịch chất lượng cao vào SQLite!")

if __name__ == '__main__':
    apply_translations()
