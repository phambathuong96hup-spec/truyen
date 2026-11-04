# -*- coding: utf-8 -*-
import json
from pathlib import Path

# Data for Novel 2
novel_2_data = {
  "chapters": [
    {
      "chapter_id": 708,
      "chapter_index": 1,
      "title_translated": "Chương 1: Bản Tự Truyện Của Ta?",
      "translated_content": """“Cốc cốc!” Tiếng gõ cửa vang lên.

“Xin chào, bưu kiện của anh, phiền anh ký nhận.”

“Cảm ơn anh!”

Mạnh Lãng nhận lấy hộp giấy, vẻ mặt lại có chút khó hiểu.

Dạo này mình có săn sale mua sắm gì trên mạng đâu nhỉ? Không lý nào? Huống chi dạo này thực lực tài chính cũng đâu có cho phép.

Chẳng lẽ lại là “đặc sản quê nhà” mẹ gửi lên cho?

“Rẹt!” Dùng chìa khóa rạch băng keo, Mạnh Lãng nhìn thấy đồ vật bên trong thì lập tức ngẩn người.

Cái gì thế này? Một cuốn sách ư?

Trong hộp giấy, một cuốn sách mỏng với tông màu đen trắng mộc mạc đang lặng lẽ nằm đó.

Mạnh Lãng tò mò lật cuốn sách lại, ngay khoảnh khắc tiếp theo, hắn sững sờ chết trân tại chỗ.

Chỉ vì trên bìa cuốn sách kia rõ ràng in dòng chữ: 《Cuộc Đời Bi Thảm Của Mạnh Lãng》...

Mạnh Lãng cẩn thận nhìn lại tựa sách một lần nữa.

Chữ Mạnh trong Mạnh Tử, chữ Lãng trong sóng lãng, không sai, chính là tên của hắn!

Gân xanh trên trán hắn giật giật.

Đứa nào thiếu đạo đức đến bốc khói lại đem trò này ra đùa dai với hắn thế không biết?

Còn bi thảm cả đời? Bi thảm cái con khỉ mốc nhà mày ấy!

Chẳng lẽ là thằng Hiền?

Không không không, khả năng này không cao, thằng ranh đó tự xưng là “bậc thầy quản lý thời gian”, là hải vương chính hiệu, có thời gian rảnh rỗi không lo bơi lội dưới biển thả thính, cớ sao lại chịu vì anh em mà nhảy lên bờ?

Không phải nó, chẳng lẽ mình vô tình đắc tội với ai rồi?

Mạnh Lãng nén cơn bốc hỏa muốn đập cuốn sách xuống đất, lật mở trang đầu.

Đập vào mắt hắn là một tấm ảnh chân dung tác giả.

Người trong ảnh mặc áo bệnh nhân, khuôn mặt trắng bệch yếu ớt không gợn một tia cười.

Quan trọng là nhìn diện mạo... cứ như chính hắn khi già đi mấy chục tuổi vậy?

Khóe miệng Mạnh Lãng giật giật.

Biết photoshop ghép ảnh thì ghê gớm lắm à? Kỹ xảo này chắc tốn hơn năm hào chứ chẳng đùa!

Cố kìm nén ý định xé nát bức ảnh ra từng mảnh, Mạnh Lãng vận dụng hết phẩm chất và sự tu dưỡng tích lũy suốt hai mươi tư năm qua để đọc tiếp xuống dưới.

【Thuở nhỏ, ước mơ của tôi là trở thành chú công an, sau này ước mơ hoàn thành được một nửa: tôi đã biến thành một ông chú.

Lớn lên một chút, ước mơ của tôi là lương năm triệu tệ, cưới được cô giáo hướng dẫn xinh đẹp, bước lên đỉnh cao nhân sinh. Kết quả là tôi vừa chạm mốc lương năm vạn tệ một năm thì cô giáo hướng dẫn đã lên xe hoa, chú rể dĩ nhiên không phải tôi.

Thế là tôi hiểu ra, làm người thì phải biết chân lấm tay bùn, trước hết cứ đặt ra một mục tiêu nhỏ: gia nhập một công ty thuộc top 500 thế giới!

...

Tôi đã thành công! Tôi vào làm việc tại Bảo hiểm Nhân thọ Hoa Hạ, trở thành một nhân viên kinh doanh bảo hiểm!

...

Đến cuối cùng, tôi rốt cuộc cũng vỡ lẽ làm người tuyệt đối không thể cứ an phận thủ thường, giống như lời Tony lão sư từng nói, phải để tiền đẻ ra tiền thì mới không trở thành nô lệ của kim tiền.

Tôi vay khắp lượt họ hàng, quẹt sạch hạn mức thẻ tín dụng, thậm chí còn vay thêm đòn bẩy tài chính để trở thành cổ đông của Dầu khí Hoa Hạ, rồi đâm đầu ngay vào cuộc khủng hoảng sụp đổ thị trường chứng khoán năm 2018, chỉ sau một đêm liền biến thành kẻ nợ nần chây ì.

...

Vét cạn ba cái ví tiền, bố mẹ kéo tôi trở về từ bờ vực thẳm. Cái giá phải trả là bố mẹ vốn đã đến tuổi nghỉ hưu lại phải tiếp tục còng lưng bươn chải kiếm sống, trong chớp mắt như già đi cả chục tuổi.

...

Trải qua những đòn quật tơi bời của xã hội, tôi rốt cuộc tỉnh ngộ hoàn toàn. Tôi trút bỏ gánh nặng ước mơ viển vông, quyết định ở lại một thành phố, chờ đợi một người, an phận trải qua phần đời bình dị có vợ có con, tối về quây quần bên mâm cơm ấm cúng.

Người ấy xuất hiện đúng như kỳ vọng, tựa như một thiên sứ thắp sáng tôi nơi đáy sâu tăm tối.

Tình yêu ập đến bất ngờ tựa cơn mưa rào. Ngày thứ hai sau khi quen biết, bên ngoài trời đổ mưa to, cả hai chúng tôi đều không về nhà được, vừa khéo khách sạn lại chỉ còn đúng một phòng...

Tôi đinh ninh đó chính là tình yêu, chẳng bao lâu sau đã nắm tay cô ấy, mỉm cười bước vào Cục Dân chính làm thủ tục kết hôn.

Cơn gió ngày hôm ấy dịu dàng biết bao, ngập tràn hương vị của hạnh phúc.

Thậm chí nhiều năm về sau, tôi vẫn nhớ như in nụ cười chúc phúc của người nhân viên phát giấy chứng nhận khi nhắc tôi buộc lại dây giày.

...

Tết năm ấy, đứa bé chào đời, một bé trai bụ bẫm nặng 3,85 cân, nhóm máu B.

Bên ngoài pháo hoa rợp trời, dường như cả thế giới đang cùng hân hoan chúc mừng cho tôi...

Ngay cả trận dịch bệnh bùng phát vào năm sau đó cũng chẳng thể làm phai nhạt dù chỉ một chút niềm vui sướng trong lòng tôi.

...

Mười tám năm sau, trong một vụ tai nạn xe tình cờ, tôi mới phát hiện bệnh viện truyền cho đứa nhỏ nhóm máu A...

Tôi từng nghĩ, chỉ cần thật lòng thích một người là có thể làm người đó cảm động. Nhưng hóa ra, người duy nhất tôi làm cảm động lại chỉ có chính bản thân mình.

Hôm ấy tôi uống rất nhiều rượu, nôn ra máu phải nhập viện, bác sĩ kết luận đã ung thư dạ dày giai đoạn cuối.

Bố mẹ không chịu nổi những đòn giáng nặng nề liên tiếp, cuối cùng đã ra đi trước tôi.

Vạn niệm như tro tàn, tôi tự tay rút ống thở oxy của mình ra.

Trong giờ phút lâm chung, cẩn dâng cuốn sách này để tế điện cho một đời đầy bi kịch của tôi...】

Mạnh Lãng cầm cuốn sách, im lặng hồi lâu tựa như một pho tượng đá, rồi sau đó biểu cảm trên mặt dần dần vặn vẹo.

“Cuộc đời bi thảm cái con khỉ nhà mày ấy!” Mạnh Lãng giận sôi máu, hung hăng ném phăng cuốn sách xuống sàn.

Hắn nghiến răng nghiến lợi giẫm thêm mấy phát thật mạnh.

“Đừng để bố mày biết là đứa nào làm trò này, nếu không bố nhất định sẽ quay cho mày một bộ '72h nhân gian vô thảm.avi'!”

Tức đến đau cả gan, Mạnh Lãng ngồi phịch xuống ghế sofa ừng ực nốc mấy ngụm nước lọc nguội ngắt, lúc này mới miễn cưỡng đè nén được ngọn lửa giận đang bốc hừng hực trong lòng xuống.

Mãi một hồi lâu sau, khi đã hơi bình tĩnh lại, Mạnh Lãng mới đè nén xúc động muốn giết người để ngẫm nghĩ xem rốt cuộc mình đã đắc tội với ai, mà đối phương lại tốn công tốn sức thuê hẳn một tay viết chuyên nghiệp về nguyền rủa mình như thế.

Cũng phải công nhận, trình độ của tay viết này mà không từng đạt “văn mẫu điểm tuyệt đối” thì tuyệt đối không viết nổi, ngay cả chính hắn đọc xong suýt nữa cũng rơi nước mắt!

Bỏ ra vốn liếng lớn như vậy chỉ để chọc tức mình thôi ư?

Có thù oán sâu nặng gì cơ chứ? Mình ăn hết gạo nhà nó hay là đào mồ cuốc mả tổ tiên nhà nó lên?

Là thù giết cha hay là hận cướp vợ... Khoan đã! Thân trai tân thanh khiết như ngọc của mình thì làm sao dính líu đến chuyện cướp vợ được?

Chẳng lẽ là thằng Kiều? Tháng trước mình lỡ làm hỏng mấy mối khách của nó, nhưng với cái đầu toàn cơ bắp của nó thì sao nghĩ ra được trò chơi khăm đầy tính sáng tạo cỡ này.

Chủ nhà trọ ư? Cũng không đúng, chỉ mới nợ có một tháng tiền nhà thôi mà, thời buổi này đứa nào nợ tiền đứa đó chẳng là ông nội?

Hay là chủ quán bán đồ ăn tháng trước bị mình cho đánh giá một sao không phục?

Thế thì lấy đâu ra lý do để biết cả nhóm máu của mình chứ?

Màn trả thù đến từ bạn gái cũ ư? Ồ! Mình làm quái gì có bạn gái cũ, thế thì dẹp đi.

Nghĩ tới nghĩ lui một hồi lâu, rà soát lại toàn bộ những người mình từng đắc tội gần đây, Mạnh Lãng vẫn chẳng thể tìm ra nổi một đối tượng khả nghi nào.

Hơn nữa càng suy xét kỹ, hắn lại càng thấy chuyện này lộ ra vẻ kỳ quặc khắp nơi.

Sau khi hoàn toàn bình tĩnh lại, hắn nhíu mày, cố nén cơn bực dọc nhặt cuốn sách đã dính đầy bụi bẩn dưới sàn lên, rồi lật ra đọc lại một lượt thật chăm chú.

Sau đó hắn lấy ra một tờ giấy và cây bút.

“Thuở nhỏ ước mơ làm cảnh sát”, “yêu thầm cô giáo hướng dẫn xinh đẹp”, “vừa vào làm tại doanh nghiệp top 500 thế giới”, “nhóm máu A”.

Nhìn bốn cụm từ được khoanh tròn trên giấy, mắt Mạnh Lãng lộ rõ vẻ kinh hãi.

“Trúng hết toàn bộ!”

Hơn nữa mốc thời gian trải dài từ thời thơ ấu, thời đại học cho đến lúc bước chân ra xã hội...

Rốt cuộc là ai lại có thể hiểu rõ về mình đến mức độ này?

Trừ phi... kẻ này thực ra đã âm thầm theo dõi sát sao mình từ tận thời mẫu giáo?

Chẳng lẽ là “cô vợ mẫu giáo” trong truyền thuyết?

Chỉ vì mình quên mất lời “thề non hẹn biển” năm xưa nên nàng mới sinh lòng thù hận vì tình?

Mạnh Lãng vắt óc suy nghĩ, nhưng cũng không tài nào nhớ nổi hồi còn học mẫu giáo mình có từng hứa lèo câu “sau này lớn lên anh sẽ cưới em” hay không.

Thế nhưng cho dù có đi chăng nữa, chuyện mình thầm thương trộm nhớ cô giáo hướng dẫn xinh đẹp tuyệt đối là bí mật cấp độ tối mật, ngay cả thằng bạn chí cốt như thằng Hiền mà mình còn ngượng không dám mở miệng, thế mà kẻ này lại có thể nói toẹt ra một cách vanh vách.

Đây chắc chắn không phải chuyện mà một “cô vợ mẫu giáo” có thể giải thích thỏa đáng được.

Suy nghĩ một lát, Mạnh Lãng cầm lấy điện thoại.

“Alo, bố ạ.”

“Con trai à, có chuyện gì thế? Loảng xoảng xoảng~” Đầu dây bên kia truyền đến tiếng xóc mạt chược lách cách quen thuộc.

“Hồi nhỏ ước mơ của con là gì hở bố?”

Tiếng động bên kia khựng lại một nhịp, một lúc sau mới vang lên giọng nói không mấy chắc chắn của ông bố: “Phi hành gia vũ trụ?”

“Thế con nhóm máu gì?” Mạnh Lãng lại hỏi tiếp.

“... Nhóm máu O hả?” Giọng nói bên kia càng yếu ớt hơn.

“Cạch!” Mạnh Lãng dập máy cái rụp.

Có thể loại trừ đối tượng tình nghi này rồi.

Hắn vùi cả người vào ghế sofa, đôi mắt thẫn thờ nhìn chăm chú lên trần nhà.

Người này... rốt cuộc là ai cơ chứ?

...

Ngày hôm sau, Mạnh Lãng mang theo đôi mắt thâm quầng như gấu trúc đến công ty quẹt thẻ chấm công, quét mặt điểm danh.

Sau đó hắn còn chẳng buồn bước vào cửa văn phòng, mà lững thững đi bộ sang quán ăn sáng quen thuộc ngoài cổng công ty.

“Bác chủ quán ơi, cho cháu một bát hoành thánh với một lồng bánh bao hấp nhỏ nhé.”

“Có ngay đây!”

Chẳng mấy chốc, đồ ăn nóng hổi nghi ngút khói đã được bưng ra đặt trước mặt. Mạnh Lãng lơ đãng rưới thêm gia vị.

Vừa mới đưa một miếng vào miệng, vẻ mặt Mạnh Lãng liền đờ đẫn cứng đờ.

Cho quá tay giấm rồi...

“Haizz!” Hắn khẽ thở dài một tiếng.

Hắn rốt cuộc cũng thấu hiểu thế nào gọi là “như nghẹn ở cổ họng, ăn ngủ không yên”.

Cả đêm hôm qua trằn trọc suy nghĩ, hắn vẫn chẳng thể tìm ra được chút manh mối nào ra ngô ra khoai.

Cảm giác cứ như thể sau lưng luôn có một đôi mắt âm thầm theo dõi mình từng giây từng phút, nắm rõ mười mươi mọi chuyện về mình lại còn ôm đầy ác ý, cảm giác ấy khó chịu và bứt rứt không sao tả xiết.

“Này người anh em, sắc mặt trông tệ thế, có phải đang gặp chuyện gì khó khăn không?”

Đúng lúc này, bên cạnh truyền đến một giọng nói. Mạnh Lãng ngước mắt nhìn sang, mới nhận ra cạnh mình còn có một thực khách khác đang ngồi.

Người đàn ông này tầm ba mươi tuổi, để hai hàng ria mép tỉa tót gọn gàng, comple phẳng phiu, giày da bóng loáng, cổ tay đeo đồng hồ Longines, tay cầm cặp tài liệu, phong thái nho nhã với cặp kính gọng vàng, nụ cười ôn hòa nở trên môi rất dễ tạo thiện cảm cho người đối diện.

Trên bàn đặt một phần bữa sáng, dường như cũng là dân công sở đi làm quanh đây.

Tục ngữ có câu không ai nỡ đánh kẻ mặt cười, Mạnh Lãng bèn lịch sự đáp lại bằng một nụ cười: “Không có gì ạ, chỉ là đêm qua em ngủ không ngon giấc thôi.”

“Ồ... Nhìn tuổi của chú em chắc là cũng mới ra trường đi làm chưa lâu nhỉ?

Ở cái độ tuổi này của chú mày, nỗi phiền muộn nếu không vì đàn bà thì cũng chỉ xoay quanh công việc mà thôi.”

“Vâng.” Mạnh Lãng hờ hững ừ một tiếng, không có ý định bắt chuyện sâu hơn.

Thế nhưng biểu cảm này rơi vào mắt một “tay kinh doanh lão làng” thì chẳng khác nào một “chú cừu non đang lạc lối” cả!

“Ông anh đây là người từng trải rồi. Hồi anh bằng tuổi chú, ngày nào cũng bù đầu bù cổ vì mấy đồng lương còm cõi, rốt cuộc bạn gái cũng chia tay.

Làm việc quần quật 996 bán sống bán chết, cầm về được vài nghìn đồng bạc lẻ, trả xong tiền nhà với điện nước thì trong túi còn sót lại được mấy đồng?

Nói cho cùng, chẳng phải cũng tại đồng tiền mà ra sao, một đồng tiền bẻ đôi cũng làm khó được bậc anh hùng hào kiệt đấy chứ!”

Gã đàn ông mặc âu phục cất giọng đầy cảm thán, ra vẻ vô cùng đồng cảm với Mạnh Lãng.

Chiêu trò này gã áp dụng trăm lần đều trúng cả trăm. Quả nhiên, Mạnh Lãng rốt cuộc cũng ngẩng đầu nhìn thẳng vào gã, dường như đã bị gã nói trúng tim đen.

“Anh dùng kinh nghiệm hơn nửa đời người đúc kết ra một chân lý: chỉ trông chờ vào mấy đồng lương chết mà muốn ngẩng mặt lên làm rạng danh tổ tông thì khó hơn lên trời!

Bởi vậy, phải để tiền đẻ ra tiền thì mới không trở thành nô lệ của kim tiền.” Gã đàn ông vỗ nhẹ lên vai Mạnh Lãng, đoạn rút khăn lau miệng, đứng dậy ra chiều chuẩn bị rời đi.

“Khoan đã!”

Tiếng gọi với theo sau lưng khiến khóe miệng gã đàn ông cong lên thành một nụ cười đắc thắng. Lúc xoay người lại, gã đã lập tức đổi về vẻ mặt vô hại, hiền lành như ban đầu.

“Sao thế chú em?”

“Câu anh vừa nói lúc nãy, anh nói lại lần nữa được không?”

“Câu nào cơ? À! Anh bảo là phải để tiền đẻ ra tiền thì mới không trở thành nô lệ của kim tiền chứ gì? Đây là lời của người giàu nhất thế giới Buffett từng nói đấy, ngộ ra được thì cả đời này hưởng dùng không hết đâu.”

Gã đàn ông nói xong, chợt nhận ra vẻ mặt của đối phương dường như không giống với những gì mình tưởng tượng cho lắm, trông quái dị vô cùng.

Mạnh Lãng đặt đũa xuống, nhìn gã đàn ông với vẻ mặt nghiêm túc khác thường.

“Dám hỏi đại ca đây xưng hô thế nào ạ?”

Tới rồi, tới rồi! Doanh số tháng này tới rồi!

Gã đàn ông nhe hàm răng trắng bóng cười tươi rói: “Anh họ Ngưu.”

Mạnh Lãng thở phào nhẹ nhõm một hơi, quả nhiên là do mình nghĩ nhiều rồi...

“Có điều mọi người đều thích gọi anh là Tony lão sư.”

Mạnh Lãng: “...”"""
    },
    {
      "chapter_id": 709,
      "chapter_index": 2,
      "title_translated": "Chương 2: Lời Tiên Tri?",
      "translated_content": """Im lặng giây lát, Mạnh Lãng thầm nghĩ chuyện này có lẽ chỉ là một sự trùng hợp ngẫu nhiên. Hắn ngập ngừng thăm dò tiếp:

“Xin hỏi nghề nghiệp của anh là gì ạ?”

“À! Anh là cố vấn đầu tư cao cấp của Công ty Chứng khoán Tinh Hà, làm việc ngay bên tòa nhà Tinh Hà đằng kia, đây là danh thiếp của anh.”

Tony lão sư đưa một tấm danh thiếp mạ vàng vô cùng tinh xảo cho Mạnh Lãng, đậm chất phong thái của giới tinh anh công sở.

【Ngưu Bôn (Tony): Cố vấn đầu tư cao cấp Chứng khoán Tinh Hà, Số điện thoại: XXXXX...】

Lại đúng là dân làm đầu tư thật à?

Mạnh Lãng nhìn tấm danh thiếp trong tay, sắc mặt càng lúc càng trở nên kỳ quặc.

Trùng hợp lần thứ hai ư?

Hắn lại ngẩng đầu lên nhìn Tony lão sư.

“Cái đó... Em thấy những lời Tony lão sư vừa nói ban nãy rất có lý. Dạo gần đây em cũng đang có hứng thú tìm hiểu về đầu tư chứng khoán, không biết Tony lão sư có lời khuyên nào cho em không?”

Hai mắt Tony lão sư sáng rực lên, nhưng gã hiểu rất rõ nguyên tắc: đối với con mồi vừa mới cắn câu thì tuyệt đối không được vội vàng giật cần.

Gã vờ ngập ngừng một lát, sau đó mới chậm rãi ngồi xuống trở lại.

“Chú em à, anh thấy chú em có duyên với anh, thôi thì anh phân tích cho chú nghe một chút nhé.

Dạo gần đây có theo dõi tin tức tài chính kinh tế không? Chỉ số thị trường chung hai năm liền ảm đạm không khởi sắc, thế mà mấy ngày gần đây lại tăng liên tiếp ba phiên, kéo lên cả mấy trăm điểm đấy.

Đặc biệt là các mã cổ phiếu công nghệ, cổ phiếu năng lượng, những mã tăng trần kịch trần liên tiếp mấy phiên liền có tới cả vài chục mã, có biết vì sao không?”

Mạnh Lãng nhớ lại “cuộc đời bi thảm” mình đọc được ngày hôm qua, có chút không chắc chắn nhìn về phía đối phương.

“Bởi vì... rau hẹ vào sòng ạ?”

Nụ cười trên mặt Tony lão sư khựng lại.

Thằng nhóc này sao không nói chuyện theo kịch bản thông thường thế nhỉ?

“Ha ha, chú em đùa vui tính quá, rau hẹ nào mà có được thực lực kinh khủng cỡ đó chứ! Đây là các tay to đầu cơ trong nước cùng với các tổ chức tài chính nước ngoài đang ồ ạt bắt đáy gom hàng đấy!”

“Ồ...” Mạnh Lãng gật gù như hiểu như không, “Thế rồi sao nữa anh?”

Tony lão sư thấy Mạnh Lãng mang dáng vẻ của một kẻ mù tịt như vậy, trong lòng càng thêm phần chắc thắng.

“Có biết câu nói 'chỉ cần đứng đúng đầu ngọn gió thì ngay cả một con lợn cũng có thể bay lên' không? Đây chính là ngọn gió lớn đấy!

Thời buổi này tiền gửi ngân hàng thì không đuổi kịp lạm phát, mang đi mua nhà thì vấp phải chính sách điều tiết vĩ mô siết chặt, kinh tế sản xuất thực tế thì lại suy thoái đìu hiu.

Chú mày bảo xem tiền trong tay người dân rốt cuộc còn có thể chảy đi đâu được nữa?

Bằng kinh nghiệm đầu tư hơn hai mươi năm của anh, thời điểm này bước chân vào thị trường chứng khoán chính là thời cơ hoàng kim tốt nhất! Chỉ cần vận may không quá tệ thì tài sản nhân đôi mỗi năm là chuyện dễ như trở bàn tay!”

Tony lão sư tiếp tục bày ra vẻ mặt đầy cảm thán.

“Đời người ta ấy mà, cả một đời có thể gặp được những ngã rẽ đủ sức thay đổi số phận thực ra chẳng có mấy lần đâu. Ngày xưa là thi đại học, lấy vợ, mua nhà, còn trong mười năm tới thì đó chính là thị trường chứng khoán!

Lần này mà không nắm bắt lấy thì thật sự cả đời này chỉ có nước đi làm thuê còng lưng thôi.”

Thú thật, đối với cái món chứng khoán này thì Mạnh Lãng đúng là dốt đặc cán mai.

Bởi lẽ chơi chứng khoán cần phải có vốn, mà ngặt một nỗi Mạnh Lãng lại chẳng có xu nào.

Nếu không phải trong lòng đang có tâm sự trĩu nặng, thì những lời lẽ đầy bài bản, giàu sức thuyết phục và truyền cảm thế này của Tony lão sư quả thực có tính mê hoặc cực kỳ lớn.

Ai mà chẳng mơ mộng nằm dài cũng có thể kiếm ra tiền chứ?

Thế nhưng lúc này tâm trí Mạnh Lãng hoàn toàn không đặt vào chuyện kiếm tiền, lại thêm “cuộc đời bi thảm” kia cứ lởn vởn lắc lư trước mắt, hắn càng nghe lại càng thấy chói tai, lập tức kéo mức độ cảnh giác lên kịch trần.

“Dạ dạ dạ! Nghe anh nói một hồi, đúng là như nghe một hồi nói.” Mạnh Lãng bày ra vẻ mặt khiêm tốn lắng nghe gật đầu lia lịa, rồi bất thình lình chuyển hướng câu chuyện.

“Thế anh bảo, liệu có khả năng nào năm nay thị trường chứng khoán sẽ sụp đổ luôn không anh?”

Tony lão sư còn chưa kịp nghĩ xem hai câu “nghe một hồi” có gì khác nhau, thì đã nghe thấy hai chữ “sụp đổ”.

“Sụp đổ thị trường? A ha ha ha...” Gã lập tức như vừa nghe thấy câu chuyện cười hài hước nhất trần đời, ngửa mặt cười to ha hả.

“Chú em ơi, anh nói thế này cho chú hiểu nhé. Sau đợt khủng hoảng chứng khoán năm 2015 thì chỉ số thị trường cơ bản đã chạm đáy rồi, năm nay mới là năm 2018 thôi đấy! Điểm số thị trường vừa mới ngóc đầu lên được mấy trăm điểm, làm sao có chuyện xảy ra sụp đổ thị trường được nữa?

Cho dù có xảy ra khủng hoảng tài chính đi chăng nữa thì chu kỳ cũng phải mười năm một lần, cả đời chú mày lấy đâu ra mà lắm đợt khủng hoảng thế?

Cái gọi là giảm đến mức không thể giảm thêm được nữa chính là thời điểm hiện tại, đây là thời cơ bắt đáy tuyệt vời nhất! Chú mày tưởng các tổ chức tài chính lớn người ta ngốc cả lũ chắc?

Chú em à, nghe lời ông anh khuyên một câu, muốn học cách quản lý tài chính là điều tốt, nhưng người trẻ tuổi thì phải chịu khó đọc nhiều sách vào, cái thị trường cổ phiếu này không phải cứ đọc dăm ba bài viết ba lăng nhăng trên mấy trang tin vỉa hè là kiếm ăn được đâu.”

Tony lão sư nhìn Mạnh Lãng bằng ánh mắt như thể tiếc nuối cho một nhân tài.

“Haizz! Nhìn chú em anh lại nhớ đến bản thân mình hồi còn trẻ, có hoài bão đấy nhưng quá mức ngây thơ.

Thế này đi, nếu chú mày thật lòng muốn học, khi nào rảnh anh có thể dành thời gian giảng giải cho chú biết trò chơi cổ phiếu này rốt cuộc phải chơi như thế nào.”

“Dạ... Thế có mã nào cụ thể hơn không anh? Ví dụ như mã nào được anh đánh giá cao chẳng hạn?” Mạnh Lãng giả vờ tỏ ra động lòng, tiếp tục gặng hỏi đến cùng.

“Haizz! Người trẻ tuổi bây giờ đúng là nóng vội quá!” Tony lão sư lắc đầu, đoạn thở dài một tiếng: “Nhưng anh cũng hiểu được tâm trạng sốt ruột của chú em.”

Gã làm bộ làm tịch giữ kẽ một hồi, sau đó mới hạ giọng nói tiếp:

“Mấy năm gần đây anh đều dốc lòng nghiên cứu một mã cổ phiếu, đó là cổ phiếu năng lượng cốt lõi mang thương hiệu quốc gia.

Sau khi trải qua một đợt giảm sâu điều chỉnh dài hạn, gần đây nó vừa đóng một cây nến xanh lớn kèm theo khối lượng giao dịch bùng nổ, sau đó lại liên tiếp xuất hiện ba cây nến xanh nhỏ đi lên cùng nến chữ thập, khối lượng thanh khoản cũng tăng dần theo từng giai đoạn. Dạng mô hình kỹ thuật này chứng tỏ xác suất cổ phiếu bứt phá tăng mạnh trong thời gian tới là cực kỳ lớn...”

Liên tiếp tung ra một tràng thuật ngữ chuyên môn, sau khi nhìn vào ánh mắt xác nhận đã bắn cho gã thanh niên trước mặt một cú choáng váng hoa mắt chóng mặt, Tony lão sư mới dáo dác nhìn quanh bốn phía, cẩn thận hạ giọng thì thầm:

“Điểm mấu chốt nhất là anh có một cậu bạn học thời đại học đang làm lãnh đạo cấp cao ở trong đó... Chuyện còn lại thì anh không thể tiết lộ thêm được nữa đâu.”

Hơi thở của Mạnh Lãng bắt đầu trở nên dồn dập: “Thế mã cổ phiếu đó rốt cuộc là...”

“Nó chính là... Năng Lượng Hoa Hạ!”

Năng Lượng Hoa Hạ ư?!

Khi bốn chữ này thực sự thốt ra từ miệng đối phương, trái tim Mạnh Lãng không khỏi run lên bần bật, mí mắt giật loạn xạ.

Một lần có thể là trùng hợp, hai lần có thể là tình cờ, thế nhưng đến lần thứ ba thì sao?

Tâm trạng Mạnh Lãng lúc này là sự bàng hoàng đan xen kinh ngạc, kinh ngạc đan xen với niềm phấn khích khó lòng kìm nén, cảm xúc trong lòng chẳng khác nào ngàn vạn con chiến mã đang phi nước đại gầm vang!

Còn Tony lão sư ngồi ngay bên cạnh, thông qua biểu cảm biến ảo khôn lường, thậm chí có phần méo mó vì quá đỗi hưng phấn của Mạnh Lãng, lại chỉ đọc ra được bốn chữ: như nhặt được báu vật!

Gã có chút hoang mang đẩy lại cặp kính trên sống mũi.

Bị mình lừa đến mức u mê đầu óc nhanh thế này cơ à?

Chiêu bài kết hợp giữa “phân tích kỹ thuật” và “tin tức nội gián” của mình từ bao giờ lại có uy lực khủng khiếp đến mức độ này nhỉ?

Người ngoài nhìn vào khéo lại tưởng mình vừa phím cho nó một mã cổ phiếu siêu tiềm năng, còn ai không biết có khi lại ngỡ thằng nhóc này vừa kiếm được vài cái mục tiêu nhỏ trăm triệu tệ rồi ấy chứ!

Người ta thường bảo kẻ nào độc thân quá lâu thì chỉ cần liếc mắt nhìn người khác giới một cái thôi là trong đầu đã nghĩ xong cả tên cho đứa con tương lai rồi, chẳng lẽ thằng này lại thuộc tuýp người có trí tưởng tượng bay xa siêu việt đến mức ấy?

Tuy rằng đòn đánh này có vẻ trúng chí mạng làm sát thương kỹ năng bị tràn quá mức, nhưng Tony lão sư cảm thấy chỉ tiêu doanh số của tháng này coi như đã chắc mẩm nằm gọn trong túi rồi!

Gã đưa mắt liếc nhìn chiếc đồng hồ Longines trên cổ tay, cố ý hay vô tình ngầm khoe khoang hình tượng một người thành đạt “không thiếu tiền”.

“Ôi chao, muộn giờ mất rồi, sáng nay anh còn một cuộc họp quan trọng nữa nên không ngồi buôn dưa lê lâu hơn được. Chú em nếu có nhu cầu thì cứ việc gọi điện cho anh bất cứ lúc nào nhé.”

Tony lão sư vỗ vỗ vai Mạnh Lãng, ung dung đứng dậy sải bước rời đi.

Mồi câu đã thả xuống, giờ chỉ còn chờ xem lúc nào cá cắn câu mà thôi. Tony lão sư tin chắc rằng chú cừu non lạc lối kia sẽ rất nhanh chóng chủ động liên lạc lại với gã.

Thế nhưng Mạnh Lãng căn bản chẳng hề nghe lọt tai câu nào trong những lời cuối cùng đối phương vừa nói. Tâm trí hắn lúc này hoàn toàn chìm đắm trong sự chấn động và ngỡ ngàng tột độ do “lời tiên tri thần kỳ” trong cuốn tự truyện kia mang lại.

Thấu hiểu mọi chuyện về mình đến chân tơ kẽ tóc, lại còn dự đoán chuẩn xác những việc sắp sửa xảy ra trong tương lai.

Tony lão sư, Dầu khí Hoa Hạ...

Những việc vừa mới diễn ra rành rành trong buổi sáng hôm nay, lại được ghi chép rõ ràng mạch lạc trong cuốn sách nhận được từ ngày hôm qua.

Đây không phải là tiên tri thì còn là cái gì nữa?

“Bình tĩnh! Phải bình tĩnh! Chưa thể vội vàng kết luận sớm được. Mặc dù sau khi loại trừ tất cả những điều bất khả thi, thì điều còn lại dù có khó tin đến đâu đi chăng nữa chắc chắn cũng chính là chân tướng sự thật.

Thế nhưng kết luận này phi khoa học quá...”

Trong lòng Mạnh Lãng lại bắt đầu rơi vào cảnh thấp thỏm nửa tin nửa ngờ.

“Khoan đã! Liệu đây có phải là một chương trình truyền hình thực tế chơi khăm giấu camera không?”

Nghe nói ở nước ngoài từng có một gã đàn ông mua một tờ vé số, sau đó phát lại đoạn video quay thưởng đã qua cắt dựng chỉnh sửa, thành công khiến cô bạn gái tin sái cổ rằng gã là người xuyên không trở về và đã trúng giải độc đắc.

Tuy rằng kết cục cuối cùng là gã mất toi cô bạn gái...

Nhưng chuyện đó chứng minh một điều: những gì mắt thấy tai nghe chưa chắc đã là sự thật.

Liệu có khi nào có kẻ cố tình gửi sách cho mình, rồi sắp xếp diễn viên quần chúng diễn một màn “tương lai” y hệt như những manh mối trong sách để gài bẫy mình không?

Mạnh Lãng lập tức điều chỉnh lại biểu cảm sang vẻ mặt điềm nhiên ung dung để tránh bị bẽ mặt làm trò cười cho thiên hạ.

Hắn cẩn thận quan sát bốn phía chung quanh một lượt, nhưng không hề phát hiện ra bất kỳ góc đặt máy quay lén hay thiết bị ghi hình giấu kín nào.

Những thực khách xung quanh vẫn đang bình thản ăn bữa sáng của họ, người đi đường bên ngoài bước chân vội vã hối hả, nhìn thế nào cũng không thấy có dấu hiệu của diễn viên đóng thế.

Hắn chẳng màng ăn nốt bữa sáng nữa, bước thẳng đến trước mặt ông chủ quán, vừa tính tiền vừa cất tiếng hỏi:

“Bác chủ quán ơi, cháu hỏi thăm bác chút chuyện với.”

“Chuyện gì thế chú em, cứ nói đi.” Đều là khách quen cả nên ông chủ quán cũng nhẵn mặt Mạnh Lãng, vừa nhào bột vừa niềm nở đáp lời.

“Cái người đàn ông vừa ngồi cạnh cháu ban nãy ấy, cái người xách cặp tài liệu, đeo kính, mặc âu phục phẳng phiu trông đúng chuẩn dân công sở ấy, bác từng gặp anh ta trước đây chưa ạ?”

“À, chú em hỏi người đó hả, gặp suốt chứ sao không. Cứ thỉnh thoảng anh ta lại ghé qua quán tôi ăn sáng, tính tình xởi lởi nói chuyện rôm rả lắm, gặp ai cũng bắt chuyện như bạn bè thân thiết ấy.

Anh ta cũng từng rủ tôi chơi cổ phiếu gì đấy nữa cơ, nhưng tôi là dân lao động chân tay thô kệch thì biết gì về ba cái trò đầu tư đó đâu.”

Nếu đã là khách quen thường xuyên ghé qua, lại còn là “kẻ tái phạm quen tay” chuyên đi rải lưới diện rộng, thì khả năng là diễn viên quần chúng được thuê tạm thời gần như bằng không rồi...

Mạnh Lãng nhìn ông chủ quán, một người nông dân chất phác thật thà, nhìn chẳng có nét nào giống đang nói dối cả.

Nếu như một ông chủ quán ăn sáng bình thường mà cũng thuê được hẳn ảnh đế đến diễn xuất, lại còn nằm vùng mở quán ăn sáng ròng rã suốt mấy năm trời, thì chương trình chơi khăm này chịu chi vốn liếng quá khủng khiếp rồi!

Đâu phải đang quay phim 'The Truman Show' chứ.

“Dạ vậy à, cháu cảm ơn bác nhé.”

Mạnh Lãng bước chân ra khỏi quán ăn sáng, ngước nhìn vầng thái dương buổi sớm đang từ từ nhô lên cao, khóe miệng dần dần toe toét nở nụ cười...

“He he he...”

“Mẹ ơi, mẹ nhìn kìa, đằng kia có một chú bị ngốc kìa!”

“Mau đi nhanh lên con! Kẻo bị lây bệnh đấy.”

...

“Huýt~ huýt huýt~” Mạnh Lãng vừa huýt sáo vừa thong thả bước vào tòa nhà công ty. Cửa thang máy vừa mở ra, bóng người đứng sừng sững bên trong lại khiến khúc nhạc giọng Đô thứ vui tươi của hắn đột ngột tắt lịm.

Nếu phải bàn xem tình huống nào là ngượng ngùng nhất khi đi làm muộn, thì chắc chắn không gì bằng việc chạm mặt lãnh đạo ngay trong thang máy.

Mà tình huống còn khó xử hơn nữa... chính là trong thang máy chỉ có duy nhất một mình vị lãnh đạo đó...

“Quản lý Vương, chào buổi sáng ạ!” Mạnh Lãng gượng gạo nở nụ cười, cắn răng bước vào trong thang máy.

“Mạnh Lãng, cậu có biết bây giờ là mấy giờ rồi không? Không biết sáng nay có cuộc họp giao ban à?” Vương Chí Bình chải mái tóc vuốt ngược bóng lộn không một sợi xộc xệch, sa sầm nét mặt quát.

“Dạ, sáng nay em vừa ra ngoài gặp một khách hàng, chẳng phải vừa xong việc là em vội vàng chạy thắt đuôi về ngay đây sao ạ.”

Phải nói rằng làm nghề nhân viên kinh doanh có một điểm rất tốt, đó là lý do không có mặt ở văn phòng luôn luôn hoàn hảo không thể bắt bẻ...

“Thế cơ à? Sáng sớm tinh mơ thế này đã có khách hàng để gặp rồi, xem ra doanh số tháng này không phải đội sổ nữa rồi nhỉ?” Vương Chí Bình cười khẩy mỉa mai châm chọc.

Mạnh Lãng ngạc nhiên liếc nhìn gã một cái. Dẫu cho ngày thường tên này cũng chẳng ưa gì mình, nhưng cũng đâu đến mức vừa gặp mặt đã xỉa xói gay gắt thế chứ? Nụ cười xã giao giả tạo chốn công sở của ông đâu mất rồi?

Chẳng lẽ sáng nay không ăn sáng mà lại đổi sang ăn thuốc súng rồi à?

Thế nhưng chút chuyện vặt vãnh này chẳng thể nào làm ảnh hưởng đến tâm trạng đang vô cùng phấn chấn của Mạnh Lãng.

“Vâng ạ! Chim dậy sớm mới có sâu ăn mà, em cũng là đang noi gương học tập Quản lý Vương thôi ạ.”

Chỉ cho phép quan lại phóng hỏa, không cho bách tính thắp đèn chắc? Lãnh đạo đi muộn được, còn tôi thì không được muộn à?

“Cậu...” Vốn dĩ trong lòng đang bực bội, không ngờ lại bị cấp dưới thọc cho một gậy mềm nhũn thế này, sắc mặt Vương Chí Bình ngay tại chỗ càng thêm khó coi.

Mạnh Lãng ngoảnh mặt sang hướng khác, không thèm để ý đến gã nữa.

Đùa à, ai chiều cho cái thói ấy!

Lương tháng một trăm nghìn thì lãnh đạo nói cái quái gì cũng đúng. Lương tháng mười nghìn thì lãnh đạo thích nói gì thì nói.

Còn lương tháng có ba nghìn bạc... thì liệu mà cẩn thận cái mồm khi nói chuyện với bố mày đấy nhé?"""
    },
    {
      "chapter_id": 710,
      "chapter_index": 3,
      "title_translated": "Chương 3: Không Lọc Lõi, Và Ngây Thơ",
      "translated_content": """“Cuộc họp giao ban sáng nay chủ yếu là để thông báo tình hình doanh số tháng này. Ở đây tôi phê bình đích danh lão Trương, tổ ba các anh đợt này doanh số lại tiếp tục đội sổ.”

Lão Trương đang bưng chiếc bình giữ nhiệt nhâm nhi ngụm trà kỷ tử, nghe thấy vậy thì động tác uống nước liền khựng lại.

Mấy chục con người ngồi kín phòng họp đồng loạt dồn ánh mắt về phía tổ ba.

Trong ánh nhìn đó, có sự đồng cảm, nhưng cũng không thiếu những kẻ hả hê xem kịch vui.

“Tôi xin nhấn mạnh lại một lần nữa, với tư cách là một tổ trưởng, ngoài việc tự mình khai thác và chăm sóc tốt khách hàng của bản thân ra, còn phải dành nhiều tâm sức hơn nữa vào công tác xây dựng đội ngũ.

Đối với những thành phần suốt ngày chỉ biết sống lay lắt qua ngày đoạn tháng thì nên dứt khoát buông bỏ đi, sớm chuyển hướng năng lượng sang những nhân tố mới có tiềm năng hơn.

Công ty chúng ta cần văn hóa bầy sói chứ không cần những con cừu non nhu nhược, những kẻ không theo kịp hàng ngũ sẽ chỉ làm kéo lùi bước tiến của cả một tập thể mà thôi!

Nếu ngay cả đội ngũ của mình mà còn không quản lý tốt, thì năm nay chúng ta lấy cái gì để tranh vị trí số một toàn phân khu...”

Lão Trương ngước mắt nhìn Vương Chí Bình đang thao thao bất tuyệt trên bục với khuôn mặt lạnh tanh như đưa đám, khẽ cau mày lại.

Mới sáng sớm ngày ra đã bóng gió xa xôi, mắng chửi xéo xắt, dạo này mình đâu có đắc tội gì với tên này đâu nhỉ?

Ông khẽ quay đầu nhìn ra phía sau lưng.

Quả nhiên, thằng nhóc Mạnh Lãng đang nhún vai bất đắc dĩ nhìn ông.

Thôi rồi! Xem ra lại là do thằng ranh con này gây họa rồi...

...

Nửa tiếng sau, cuộc họp kết thúc.

Thế nhưng Vương Chí Bình lại gọi giật lão Trương vào phòng làm việc riêng, sau đó lại là một tràng xả giận dữ dội. Cách qua lớp cửa kính trong suốt cũng có thể nhìn thấy nước bọt của gã bắn tung tóe liên hồi về phía lão Trương.

“Này! Có phải chú em mày lại đắc tội với người ta rồi không đấy?”

Mạnh Lãng đang cau mày quan sát trận chiến bên trong phòng làm việc, thì bên cạnh bỗng có một anh chàng vạm vỡ cao tới một mét tám đầu đinh húi cua ghé sát lại, cất giọng trêu chọc.

“Ban nãy anh nghe là hiểu ngay rồi, 'Nam Ba Vạn' ngoài miệng thì nói tổ ba chúng ta, nhưng từng câu từng chữ đều đang nhắm thẳng vào đầu chú mày đấy...”

Người này tên là Mã Kiều, cũng là nhân viên kinh doanh của tổ ba giống như Mạnh Lãng.

Còn cái danh xưng “Nam Ba Vạn” kia là biệt danh bọn họ lén đặt cho Vương Chí Bình sau lưng, bởi vì thói hống hách thích làm màu của gã, hơn nữa mỗi lần họp hành mở miệng ra là lại ra rả đòi tranh vị trí số một (No.1).

“Ai mà biết được chứ, lúc nãy trong thang máy em có lỡ mồm vặn lại lão một câu, ai ngờ tâm lý lão yếu đuối mong manh đến thế, lại còn chơi trò phạt lây cả họ. Lần này bác Trương coi như gánh đạn thay em rồi.

Cũng chẳng biết hôm nay lão có quên uống thuốc trước khi ra khỏi nhà hay không mà gặp ai cũng cắn...” Mạnh Lãng bất đắc dĩ thở dài.

“Hì! Chẳng có gì lạ cả, chú mày mới vào làm nên không biết, tháng nào Nam Ba Vạn cũng có vài ngày như thế đấy.

Khả năng cao là ở nhà bị vợ đè đầu cưỡi cổ chịu uất ức, nên mới chạy đến công ty tìm bao cát xả giận thôi.”

“Ủa? Anh lại hóng hớt được tin gì rồi à?” Mạnh Lãng nhướng mày ngạc nhiên.

Nhìn bề ngoài thì chắc chắn chẳng một ai có thể tin nổi một anh chàng cao to một mét tám, thân hình chuẩn gymer đầy nam tính như thế này lại là một kẻ siêu cấp nhiều chuyện, buôn dưa lê số một.

Trong công ty này, từ chuyện quan hệ ngầm giữa các sếp cho đến ba cái tin đồn hành lang vụn vặt, không có chuyện gì là hắn không tò mò hứng thú.

“Hê hê, chú mày chưa biết chứ gì? Bố vợ của Nam Ba Vạn là lãnh đạo cốt cán ở tận trụ sở công ty cấp tỉnh đấy, nếu không chú mày tưởng với cái tuổi này của lão mà ngồi được vào cái ghế này, dưới trướng chỉ huy cả trăm con người chắc?

Cơ mà cái trò chọn đi đường tắt để bớt phấn đấu hai mươi năm ấy, cũng phải trả cái giá đắt đỏ lắm chứ bộ...” Mã Kiều nháy mắt làm ra vẻ “chú mày tự hiểu đi nhé”.

“Sao cơ? Vợ lão dùng bạo lực gia đình với lão à?” Hai mắt Mạnh Lãng sáng rực lên vì hóng chuyện.

“Thế thì chưa đến mức đấy, nhưng vợ lão bạo hành tinh thần lão thì chắc chắn là có thật, nghe đồn cân nặng của bả không dưới con số này đâu!” Mã Kiều giơ ngón trỏ và ngón giữa lên lắc lắc trước mặt Mạnh Lãng.

“Xì~” Mạnh Lãng không kìm được hít vào một ngụm khí lạnh.

Thử tưởng tượng sơ sơ khung cảnh đó một chút, Mạnh Lãng bỗng cảm thấy mỗi tháng người ta có vài ngày bốc hỏa như thế kể ra cũng là điều hoàn toàn có thể cảm thông được.

Kẻ đáng ghét ắt có chỗ đáng thương.

Sáng nay mình bật lại người ta như thế, xem ra cũng hơi thiếu tính nhân đạo rồi.

“Cho nên ấy, chú mày là đâm đầu ngay vào họng súng của người ta rồi hiểu chưa? Anh khuyên chú dạo này cứ liệu hồn mà ngoan ngoãn khiêm tốn lại, không thì chẳng mấy chốc là bị tống cổ ra đường đấy.”

“Em mà bị đuổi việc thì chẳng phải anh nên mở tiệc ăn mừng sao?”

“Mừng chứ, sao lại không mừng, anh còn phải khui hẳn một chai sâm panh ăn mừng ấy chứ! Từ ngày lão Trương giao chú mày cho anh kèm cặp, chú mày thử đếm xem chú mày đã phá hỏng của anh bao nhiêu hợp đồng rồi?”

Nhắc đến chuyện mấy hôm trước, khóe miệng Mã Kiều lại không kìm được mà co giật liên hồi.

“Ngay như lần trước, anh đây nói đến khô cả cổ họng, rát cả lưỡi, người ta khó khăn lắm mới xuôi xuôi chuẩn bị ký hợp đồng mua bảo hiểm nhân thọ chia lãi, chú mày nhảy bổ vào phán một câu xanh rờn: 'Trừ phí quản lý đi thì tiền lãi còn thấp hơn cả gửi tiết kiệm định kỳ ở ngân hàng'.

Còn lần trước nữa, anh chào bán gói bảo hiểm y tế triệu tệ, lạy chúa tôi, chú mày suýt chút nữa thì ngồi phân tích luôn cả tiền sử bệnh tật của cả dòng họ người ta ra ngay tại chỗ.

Anh hỏi chú có ai đi làm nhân viên kinh doanh như chú mày không hả?

Bộ không biết thế nào là chỉ chọn lời hay ý đẹp mà nói à?

Có bệnh thì bảo hiểm chi trả, không bệnh thì hoàn lại tiền, người ta thích nghe là thích nghe cái đó!”

“Nhưng mà vị khách đó đã hơn năm mươi tuổi rồi, lại chẳng có con cái gì, nếu đem hết tiền dưỡng già gửi vào đó, tiền chia lãi đã thấp thì chớ, sau này lỡ như giữa chừng có việc gấp cần rút tiền ra thì khó khăn vô cùng.

Hủy hợp đồng giữa chừng thì số tiền lấy lại được chắc chưa nổi một nửa, thế nửa đời sau của người ta biết sống làm sao?

Còn cả cái gói bảo hiểm y tế kia nữa, mấy chục trang điều khoản lắt léo gài bẫy thế nào chẳng lẽ anh không rõ? Đến lúc có bệnh thật liệu có được bồi thường hay không còn chưa biết chừng, ít nhất cũng phải giải thích rõ ràng ngọn ngành cho người ta hiểu chứ?”

Mã Kiều cạn lời nhìn Mạnh Lãng như nhìn sinh vật lạ.

“Anh nói thật nhé, rốt cuộc chú mày là gián điệp do Bảo hiểm Bình An phái sang, hay là nội gián của Thái Bình Dương cài cắm vào đây thế?

Rốt cuộc là vị thần thánh phương nào đã đào tạo ra một viên mãnh tướng như chú mày vậy, các người định đánh sập đối thủ từ bên trong nội bộ đấy à?”

Mạnh Lãng ưỡn ngực, ngẩng cao đầu: “Gia huấn của nhà họ Mạnh bọn em: Bất nghĩa mà giàu sang, đối với ta như mây nổi!”

“Hình như câu này là do Khổng Tử nói mà, cụ Mạnh Tử ở dưới suối vàng mà biết con cháu mình đem câu này ra làm gia huấn chắc tức đến bật nắp quan tài nhảy dựng lên mất.”

“Ủa? Không nhìn ra đấy nhé, trong cái đầu toàn cơ bắp của anh thế mà cũng có chút chữ nghĩa đấy nhỉ! Nhưng anh đâu có biết, hai nhà Khổng - Mạnh đời đời giao hảo, chúng em là chỗ quen biết thế giao nhiều đời, gia huấn dùng chung thì đã làm sao.”

“Đừng có tưởng anh ít học mà lừa anh nhé, Khổng Tử với Mạnh Tử tuy đều là người thời Xuân Thu Chiến Quốc, nhưng căn bản đâu có sống cùng thời đại, hai cụ làm sao mà gặp nhau được!

Mạnh Tử cùng lắm chỉ được tính là học trò đời sau của Khổng Tử thôi, xét về vai vế thì Mạnh Tử phải gọi Khổng Tử một tiếng sư công đấy!”

“Khé...” Mạnh Lãng có cảm giác như vừa bị đống kiến thức chữ nghĩa của thằng cha này làm cho sặc nước bọt.

“Biết vụ lấn sân ngoạn mục nhất thế kỷ 21 là gì không? Là một nhân viên bán bảo hiểm, không thèm đọc 'Đắc nhân tâm' với sách làm giàu của Carnegie, mà lại đi nghiên cứu kinh Xuân Thu!”

“Hê hê! Đừng tưởng dân bán hàng thì không có học thức nhé. Cốt lõi của nghề bán hàng là giao tiếp kết nối giữa con người với con người, mà trên cõi đời này bất cứ chuyện gì dính dáng đến kiếm tiền thì bản chất cũng đều là đạo đối nhân xử thế cả thôi.

Đừng thấy bây giờ mấy ngành tài chính với IT được người ta tung hô săn đón, nhưng cái nghề dễ kiếm được một triệu tệ đầu tiên trong đời nhất vẫn chính là nghề bán hàng!

Đại đa số các ông chủ doanh nghiệp vừa và nhỏ trong nước đều đi lên từ nghề bán hàng, trong số các CEO của top 500 doanh nghiệp hàng đầu thế giới có hơn 50% từng xuất thân từ dân kinh doanh đấy.

Lý Gia Thành, Tông Khánh Hậu, Đổng Minh Châu, những tấm gương sáng ngời như thế nhiều vô số kể, sóng lớn đãi cát mới lộ rõ bản lĩnh anh hùng.”

Mạnh Lãng tròn xoe mắt kinh ngạc nhìn “kho báu ngầm” trước mặt mình.

“Em bảo này, anh không phải là cậu ấm con nhà tài phiệt nào đó xuống cơ sở trải nghiệm rèn luyện cuộc sống đấy chứ?”

“Ồ! Bị chú mày nhìn thấu rồi à?” Mã Kiều cười toe toét để lộ hàm răng trắng: “Được rồi không giấu nữa, nếu không phải thấy chú mày nhìn cũng vừa mắt thì người bình thường anh đây chẳng thèm nói nhiều thế đâu.

Sao nào, hôm nào rảnh ngồi xe Lamborghini của anh đi làm một chầu nhé?”

“Thôi xin can, anh tưởng búp bê Rambo mặc thêm bộ bikini vào thì biến thành Lamborghini chắc? Thôi anh em mình cứ sống thực tế chút đi, ráng ký được hợp đồng lớn rồi gom tiền mua con Ngũ Lăng Mini là mừng rơi nước mắt rồi.”

Hai người đang đứng ba hoa bốc phét thì “cạch” một tiếng, cánh cửa phòng làm việc bật mở, lão Trương mặt đen như đít nồi từ bên trong bước ra.

“Mạnh Lãng, theo tôi qua đây.” Lão Trương buông lại một câu rồi đi thẳng vào phòng họp chuyên dụng của tổ ba.

Dưới ánh mắt trêu chọc đầy thương hại của Mã Kiều, Mạnh Lãng bất đắc dĩ lê bước đi theo vào trong, đoạn kéo cửa đóng lại.

Cứ ngỡ sắp sửa phải hứng trọn một trận mắng mỏ té tát xối xả, chẳng ngờ lão Trương vừa ngồi xuống ghế liền lập tức thay đổi sắc mặt cái rụp, trở lại với dáng vẻ ung dung tự tại của một cán bộ hưu trí, thong dong bưng bình trà kỷ tử lên nhấp một ngụm.

“Khụ... Bác Trương, cháu xin lỗi ạ, đã làm phiền bác với cả tổ ba rồi. Hay là để cháu vào phòng xin lỗi Quản lý Vương một câu nhé?” Mạnh Lãng áy náy nói.

“Thôi dẹp đi cho tôi nhờ, cái đức tính của cậu thế nào tôi còn lạ gì nữa, bước chân vào chưa đầy ba phút khéo lại nhảy vào tay đôi với nó cho mà xem.

Nhiệm vụ bây giờ của cậu là coi như chưa có chuyện gì xảy ra, ngoan ngoãn ngồi yên làm một chàng mỹ nam an tĩnh giùm tôi!” Lão Trương liếc xéo hắn một cái, tiếp tục nhẩn nha uống trà.

“Thế bác không mắng cháu hai câu ạ?”

“Tôi chẳng đang mắng cậu đây còn gì?” Lão Trương “rầm” một tiếng đập mạnh tay xuống mặt bàn. Tiếng động bất thình lình khiến Mạnh Lãng giật nảy mình, nhưng ngay sau đó hắn liền hiểu ra: đây là làm màu cho cái thằng họ Vương bên ngoài nhìn thấy thôi.

“Cháu cảm ơn bác Trương.”

“Hừ! Ai bảo bố cậu gửi gắm cậu cho tôi chăm sóc làm chi. Nhưng nói thật lòng nhé, với cái tính nết này của cậu thì căn bản không thích hợp làm cái nghề bán hàng này đâu.

Dù sao với cái thành tích đội sổ này của cậu thì cũng chẳng bám trụ lại được bao lâu nữa đâu.

Nghe lời khuyên chân thành của bác đi, khăn gói về quê, ngoan ngoãn kế thừa trại nuôi mấy trăm con lợn nái của bố cậu đi cho lành.”

“Không bao giờ! Cháu không muốn rúc mãi ở cái huyện lẻ bé tí tẹo đó đâu, khó khăn lắm mới ra được thành phố lớn, cháu đời nào chịu quay về!” Mạnh Lãng bướng bỉnh cãi lại.

“Được rồi, người trẻ tuổi có chí tiến thủ là điều tốt, bác cũng chẳng ngăn cản. Đợi đến khi cậu bị đời vùi dập cho tơi bời hoa lá rồi, lúc về quê nhớ gửi lời hỏi thăm của tôi tới bố cậu là được.”

“Cốp! Cốp! Cốp!” Lão Trương lại cầm chiếc bình giữ nhiệt gõ thật mạnh xuống mặt bàn thêm mấy phát nữa.

Mạnh Lãng dở khóc dở cười: “Mọi người coi thường cháu đến thế cơ à?”

“Hì hì! Làm cái nghề này của chúng ta ấy, một là cậu phải tâm đen tay độc, hai là phải 'biết sự đời mà không lọc lõi, nếm trải thói đời trơn tru mà vẫn giữ được nét ngây thơ'.

Điều thứ nhất cậu không làm nổi, còn điều thứ hai ấy à... cậu mới học được có một nửa thôi.”

“Thế ạ? Cháu đã bảo là cháu vẫn có tiến bộ mà lị! Bác Trương, thế bác bảo cháu đã học được nửa nào rồi?” Hai mắt Mạnh Lãng sáng rực lên.

Lão Trương liếc nhìn Mạnh Lãng, khoan thai nhấp một ngụm trà.

“Chẹp chẹp~”

“Không lọc lõi, và ngây thơ.”

Mạnh Lãng: “...”"""
    }
  ]
}

# Data for Novel 1
novel_1_data = {
  "chapters": [
    {
      "chapter_id": 1,
      "chapter_index": 1,
      "title_translated": "Chương 708: Người Chưởng Khống Thật Sự",
      "translated_content": """Người đàn ông cao lớn khoác trường bào màu bạc trắng vừa nghe thấy vậy, biểu cảm lập tức trở nên vặn vẹo dữ tợn: “Muốn chưởng khống hỗn độn vũ trụ này ư, ngươi nằm mơ đi!”

“Nằm mơ? Ha ha, vậy sao?” Bạch Vân khẽ cười đầy ý vị, không gian quanh thân hắn bỗng chốc vặn vẹo sụp đổ dữ dội, năng lượng bản nguyên hỗn độn vũ trụ vô tận tựa như thác lũ cuồng nộ điên cuồng trút xuống giáng lâm.

Nhìn thấy nguồn năng lượng bản nguyên vũ trụ đang bị Bạch Vân điên cuồng thôn phệ hấp thu, người đàn ông cao lớn áo bào bạc sững sờ trong thoáng chốc, ngay sau đó dường như chợt nhận ra điều gì, trừng trừng đôi mắt gầm lên một tiếng kinh thiên động địa, thân hình lóe lên lao thẳng về phía Bạch Vân đánh tới tấp nập sát chiêu.

Thế nhưng, đối với một người đã chưởng khống Thời Không Chung Cực Chi Đạo như Bạch Vân mà nói, công kích của hắn chẳng khác nào một trò cười ấu trĩ.

Mặc cho công kích kia hung hãn bén nhọn đến nhường nào, khi giáng xuống người Bạch Vân đều tan biến vào hư không, tựa như đòn đánh đã rơi vào một tầng thời không hoàn toàn cách biệt khác vậy.

Khí tức quanh thân Bạch Vân tăng vọt một cách chóng mặt, hắn chỉ khẽ chuyển động tâm ý, ý niệm đã bao trùm lấy toàn bộ cõi hỗn độn vũ trụ, dễ dàng thẩm thấu sâu vào bản nguyên hỗn độn, triệt để luyện hóa và chưởng khống phiến hỗn độn vũ trụ này.

Vào khoảnh khắc Bạch Vân hoàn toàn chưởng khống hỗn độn vũ trụ, chưởng khống giả của Tây Tư tộc vũ trụ là Thái Sơ, chưởng khống giả của Mãng Hoang vũ trụ là Kỷ Ninh, cùng hai vị cường giả chưởng khống hai tòa hỗn độn vũ trụ khác là Ngọc Lam Phong và Vô Thường Đế Quân đều đồng loạt sinh ra cảm ứng. Ánh mắt của bọn họ xuyên qua vô số tầng không gian trông lại. Cảm nhận được uy năng thời không mênh mông cuồn cuộn thâm sâu khôn lường kia, sắc mặt bọn họ không khỏi khẽ biến đổi. Chung Cực Thời Không Chi Đạo so với những Chung Cực Chi Đạo mà bọn họ nắm giữ còn quỷ dị và khó chơi hơn gấp bội phần.

“Để có thể trở thành chưởng khống giả hỗn độn vũ trụ, sau khi bước chân vào tầng thứ Chung Cực Đế Quân, ngươi đã vội vã bày mưu tính kế hại chết chính ân sư từng dốc hết tâm can dạy dỗ ngươi không chút tư lợi. Ngươi quả thực chết cũng không hết tội.” Sau khi chưởng khống hỗn độn vũ trụ này, tâm ý vừa động là có thể thấu suốt toàn bộ những gì từng xảy ra trong vũ trụ, Bạch Vân hiểu rõ nguyên nhân chém giết giữa hai vị Chung Cực Đế Quân khi trước, không khỏi lắc đầu nhìn người đàn ông cao lớn mặc áo bào bạc bằng ánh mắt lạnh lùng, tâm niệm khẽ động liền dễ dàng xóa sổ gã chẳng khác nào bóp chết một con kiến hôi.

Khoảnh khắc tiếp theo, Bạch Vân sải một bước dài, trực tiếp tiến vào bên trong bản nguyên của hỗn độn vũ trụ này, cẩn thận tĩnh tâm cảm ứng toàn bộ cõi vũ trụ.

Không lâu sau đó, bốn vị chưởng khống giả hỗn độn vũ trụ còn lại bao gồm Kỷ Ninh đều đồng loạt rơi vào chấn kinh tột độ, bởi vì bọn họ phát hiện tòa hỗn độn vũ trụ vừa mới bị Bạch Vân chưởng khống kia vậy mà lại biến mất một cách đầy quỷ dị. Một tòa hỗn độn vũ trụ khổng lồ vô biên vô tận lại cứ thế biến mất không một dấu vết, điều này thực sự quá mức khó tin.

Tuy rằng bọn họ đều đoán được có lẽ đây là một thủ đoạn che giấu thuộc về không gian, nhưng thủ đoạn bực này cũng đủ để khiến bọn họ chấn động tâm can.

Ngay sau đó, một sự việc còn chấn động hơn nữa đã xảy ra. Người đầu tiên phát giác ra điểm bất thường chính là Vô Thường Đế Quân – vị cường giả cũng là một chưởng khống giả hỗn độn vũ trụ. Ngay trong chính vũ trụ do bản thân luyện hóa chưởng khống, hắn cảm nhận rõ ràng một luồng uy năng đáng sợ không hề thua kém bản nguyên vũ trụ của hắn đang giáng lâm, một tòa hỗn độn vũ trụ hư ảo như ẩn như hiện tiến nhập vào cõi vũ trụ của hắn, tựa như đang dung hợp cùng vũ trụ của hắn vậy.

“Cái này...” Khi hắn còn đang bàng hoàng không dám tin vào mắt mình, thì ngay sau đó liền cảm nhận được một luồng khí tức vô cùng quen thuộc. Đó là luồng khí tức mà cả đời này hắn vĩnh viễn không bao giờ quên được, chính là khí tức phân thân đệ nhị nguyên thần của Vân Thiên – bản tôn trước kia của Bạch Vân.

Hai mắt kinh hãi trừng lớn, vẻ mặt hắn không kìm được trở nên dữ tợn: “Là ngươi sao? Ngươi chưa chết, lại còn chưởng khống một phương hỗn độn vũ trụ? Thật không ngờ, ngươi lại nắm giữ được Chung Cực Thời Không Chi Đạo, lại còn có được thủ đoạn bực này. Thế nhưng, nếu ngươi đã dám tự tìm đến đây, vậy thì ngoan ngoãn ở lại cho ta!”

Vô Thường Đế Quân muốn trấn áp Bạch Vân, ngặt nỗi Bạch Vân lúc này cũng đang chưởng khống một phương hỗn độn vũ trụ, há phải nói muốn trấn áp là có thể trấn áp được sao?

Hơn nữa rất nhanh sau đó, Vô Thường Đế Quân bàng hoàng nhận ra, cùng là chưởng khống một phương hỗn độn vũ trụ, nhưng sự vận dụng uy năng bản nguyên vũ trụ của Bạch Vân lại vượt xa hắn. Uy năng bùng phát ra lại đang áp chế ngược lại hắn, điều quỷ dị hơn cả là hỗn độn vũ trụ của Bạch Vân dường như đang thôn phệ hấp thu năng lượng bản nguyên từ vũ trụ của chính hắn.

“Không...” Phát hiện ra điều này, Vô Thường Đế Quân lập tức hoảng loạn tột cùng. Thế nhưng hắn lại bi ai nhận ra bản thân hoàn toàn bất lực không thể kháng cự, hỗn độn vũ trụ do hắn chưởng khống chẳng khác nào một con cừu non nằm chờ bị làm thịt, hắn chỉ có thể trơ mắt nhìn bản nguyên vũ trụ của mình ngày càng suy yếu đi. Cứ tiếp tục thế này, e rằng chẳng bao lâu nữa, tòa hỗn độn vũ trụ này của hắn sẽ trở nên suy kiệt cùng cực, thậm chí sụp đổ hủy diệt hoàn toàn.

Vô Thường Đế Quân căm hận đến phát cuồng, nhưng lại cảm thấy một sự bất lực sâu sắc tận đáy lòng. Uy năng bản nguyên vũ trụ suy thoái khiến cho nguồn sức mạnh mà hắn có thể điều động cũng giảm sút nghiêm trọng.

Đợi đến khi vũ trụ của đối phương suy yếu tới một mức độ nhất định, Bạch Vân cười khẩy một tiếng, trực tiếp mượn uy năng bản nguyên hùng mạnh hơn của hỗn độn vũ trụ mình đang chưởng khống, triệt để trấn sát Vô Thường Đế Quân đang ngập tràn bi phẫn và không cam lòng.

Giữa bọn họ vốn dĩ chẳng có ai đúng ai sai tuyệt đối, nhưng Bạch Vân trước giờ chưa từng là kẻ chịu cam phận chịu thiệt. Lần ra tay này, ngoài việc báo mối thù năm xưa từng bị đám người Vô Thường Đế Quân bức bách tới mức phải tự bạo, Bạch Vân còn muốn nghiệm chứng một vài suy đoán của bản thân. Sự thực đã chứng minh, chưởng khống Chung Cực Thời Không Chi Đạo mới chính là phương pháp hoàn mỹ nhất để luyện hóa và làm chủ một phương hỗn độn vũ trụ.

Nhờ vào thủ đoạn thời không, hắn có thể tùy ý dịch chuyển vị trí của hỗn độn vũ trụ do mình chưởng khống, thậm chí tiến thẳng vào bên trong một hỗn độn vũ trụ khác để thôn phệ hấp thu hỗn độn bản nguyên của đối phương. So với những chưởng khống giả khác vốn chỉ có thể mượn dùng uy năng bản nguyên vũ trụ, thì Bạch Vân mới thực sự gọi là người chưởng khống đích thực của một phương vũ trụ, biến hỗn độn vũ trụ trở nên tùy tâm sai khiến như cánh tay chỉ ngón, hóa thành một món vũ khí mang uy năng hủy thiên diệt địa trong tay hắn.

Sau cùng, Bạch Vân cũng không thực sự thôn phệ cạn kiệt toàn bộ bản nguyên của hỗn độn vũ trụ này, chỉ tiêu diệt ba vị cường giả Chí Tôn còn sót lại bên trong, sau đó liền điều khiển hỗn độn vũ trụ của mình rời đi, cũng không hề ra tay với những hỗn độn vũ trụ khác.

Thế nhưng những việc diễn ra trước đó đã khiến cho Thái Sơ, Ngọc Lam Phong cho đến cả Kỷ Ninh đều chấn động khôn nguôi, trong lòng dấy lên nỗi bất an sâu sắc. Bởi vì Bạch Vân lúc này đã hoàn toàn vượt xa bọn họ, sở hữu thực lực đủ sức uy hiếp tính mạng của bọn họ. Đứng trước một đối thủ không thể nào chiến thắng nổi như vậy, sau này bọn họ chỉ đành phải sống dưới cái bóng của hắn mà thôi.

Kỷ Ninh và Ngọc Lam Phong thì còn đỡ, quan hệ giữa Bạch Vân với bọn họ vốn dĩ khá tốt. Riêng Thái Sơ của Tây Tư tộc thì lại kinh hoàng lo sợ khôn xiết, năm xưa hắn từng kết thù oán sâu nặng với Mãng Hoang vũ trụ và Kỷ Ninh. Trước kia Kỷ Ninh không làm gì được hắn, ân oán đành phải gác lại, nay đã có được sức mạnh đủ sức uy hiếp thậm chí xóa sổ hắn, khó lòng bảo đảm Kỷ Ninh sẽ không mượn tay Bạch Vân để trừ khử hắn và hủy diệt Tây Tư tộc vũ trụ.

Có điều lần này gã quả thực đã lo lắng thừa thãi rồi, Bạch Vân lúc này đâu có rảnh rỗi mà bận tâm đến gã! Chưởng khống được một phương hỗn độn vũ trụ, Bạch Vân cứ như vừa có được một món đồ chơi vô cùng thú vị, đang dồn hết tâm trí vào mày mò nghiên cứu kia kìa!

Gác lại chuyện này, lại nói về chốn hỗn độn vô tận bên ngoài Hồng Hoang thế giới. Trong một phương thế giới do Càn Khôn Lão Tổ khai mở, trải qua vô vàn tuế nguyệt sinh sôi nảy nở, nơi đây từ lâu đã trở nên phồn thịnh tột bậc, cường giả xuất hiện nhiều như mây. Tu sĩ nơi này tuy chia thành rất nhiều thế lực, có tranh đoạt có thù oán, nhưng không thể nghi ngờ rằng bọn họ đều thuộc về Càn Khôn nhất mạch, tôn sùng Càn Khôn Lão Tổ đến tột cùng, không một ai dám làm trái ý chí của Lão Tổ.

Sâu bên trong thế giới này, tại không gian bản nguyên, Càn Khôn Lão Tổ vốn đang tĩnh tâm nhắm mắt xếp bằng bỗng nhiên thân thể như hư hóa đi. Thân ảnh hư ảo của người cấp tốc bành trướng, lớn vượt qua cả toàn bộ thế giới, sau đó thân thể lại dần dần ngưng thực thu nhỏ lại. Đến khi người trở về với vóc dáng bình thường, thì trong chốn hỗn độn đã chẳng còn tung tích của phương thế giới kia nữa, hiển nhiên đã bị người hoàn mỹ chưởng khống thu vào trong cơ thể tựa như một món pháp bảo.

“Ha ha, đây mới thực sự là Người Chưởng Khống đích thực a! Trên cảnh giới Thánh Nhân, ắt hẳn chính là Cảnh giới Chưởng Khống Giả chăng? Một phương thế giới vũ trụ tùy ý đùa giỡn trong lòng bàn tay, chư thiên vạn giới mặc ta ngao du, chẳng còn bất cứ chướng ngại nào nữa, đây mới chính là vị tiên nhân tiêu dao tự tại thực thụ a!” Càn Khôn Lão Tổ cất tiếng cười vang sảng khoái, tâm ý khẽ động thân hình đã trong nháy mắt tan biến lặng lẽ không một tiếng động, chẳng ai biết người đã phiêu bạt về phương nào.

Cùng lúc đó, trong chư thiên vạn giới, không chỉ có một vị đại năng dường như sinh ra cảm ứng, khẽ mỉm cười cất lời: “Sáng nghe đạo lý, chiều chết cũng cam lòng! Rốt cuộc lại có thêm một vị đạo hữu bước lên đứng chung hàng ngũ cùng chúng ta rồi!”

(Toàn thư hoàn)"""
    },
    {
      "chapter_id": 2,
      "chapter_index": 2,
      "title_translated": "Chương 707: Chung Cực Thời Không",
      "translated_content": """Kèm theo tiếng quát tháo uy nghiêm sắc lạnh vang vọng khắp thế giới này, trên chín tầng trời phong vân biến sắc, một khuôn mặt khổng lồ hư ảo lặng lẽ hiện lên, lạnh lùng rủ mắt nhìn xuống vô số sinh linh bên dưới tựa như đang quan sát lũ sâu kiến hèn mọn. Một luồng khí tức vô hình kinh hoàng tràn ngập khắp nơi, dường như hắn chính là chúa tể tối cao, là chủ nhân duy nhất của phiến thế giới này vậy.

“Khí linh sao? Quả nhiên không nằm ngoài dự đoán của ta, thế giới này thực chất là một động thiên thế giới.” Bạch Vân híp mắt ngước nhìn khuôn mặt khổng lồ trên chín tầng trời, trong lòng không khỏi thoáng chút kinh ngạc: “Nguyên thần của ta xuyên qua trùng trùng không gian, vậy mà lại lạc vào một động thiên thế giới, đúng là trùng hợp thật.”

Cảm nhận được uy năng của toàn bộ động thiên thế giới đang trút xuống hòng trói buộc lấy mình, Bạch Vân khẽ cau mày, lạnh lùng nhìn khuôn mặt khổng lồ do động thiên chi linh huyễn hóa ra, đang định ra tay thì chợt ngạc nhiên phát hiện động thiên chi linh bỗng nhiên phát ra một tiếng rên rỉ đầy bi thương rồi tan biến trong sự bất cam. Ngay sau đó, cả động thiên thế giới bắt đầu rung chuyển dữ dội, chao đảo chực chờ sụp đổ.

“Chuyện này...” Bạch Vân ngẩn người trong chớp mắt, lập tức chuyển động tâm niệm, thần thức ý niệm vô hình quét mạnh ra xung quanh, gần như trong khoảnh khắc đã bao trùm lấy toàn bộ thế giới này, rồi từ đó thẩm thấu thoát ra ngoài. Hắn nhìn thấy bên ngoài là một cơn bão năng lượng cuộn trào khủng khiếp, một pháp bảo động thiên tựa như viên linh châu màu đen đang chìm nổi rung lắc kịch liệt giữa tâm bão.

Hắn lập tức chuyển động tâm ý điều khiển không gian, mượn nhờ uy năng bản nguyên không gian của cõi hỗn độn vũ trụ này để làm suy yếu sức tàn phá của cơn bão năng lượng, khống chế kiện pháp bảo động thiên vốn đã bị trọng thương đến mức khí linh cũng tan rã này phiêu bạt giữa cơn bão tố năng lượng vô tận, từng bước tiếp cận về phía vùng không gian ổn định mà hắn vừa cảm ứng được từ đằng xa.

“Được rồi, không sao nữa rồi!” Bên trong một phương thế giới của pháp bảo động thiên, trên bầu trời của Bạch Man bộ lạc, Bạch Vân vốn đang dồn phần lớn tâm thần vào việc điều khiển động thiên pháp bảo tiến lên, bèn phân tách một chút tâm thần truyền âm cho lão tổ Bạch Man bộ lạc cùng mọi người: “Bảo các tộc nhân không cần hoang mang, nguy cơ đã trôi qua rồi. Kể từ nay về sau, phương thế giới này sẽ hoàn toàn do Bạch Man bộ lạc chúng ta làm chủ.”

Bạch Man lão tổ sững sờ há hốc mồm nhìn Bạch Vân, tuy cảm thấy khó tin nhưng nhớ lại những thủ đoạn phi phàm mà Bạch Vân vừa triển lộ, dám nói ra những lời này ắt hẳn không phải là chuyện ăn ốc nói mò. Nghĩ tới đây, dẫu cho tâm tính lão luyện từng trải phong sương, Bạch Man lão tổ cũng không khỏi cảm thấy một phen run rẩy kích động. Để Bạch Man bộ lạc trở thành chúa tể của cả phương thế giới này, đó là điều mà trước đây ngay cả trong mơ lão cũng chưa từng dám nghĩ tới!

Sau khi xác định thế giới này chỉ là một động thiên thế giới, Bạch Vân cũng chẳng còn mấy bận tâm đến tình hình bên trong nữa. Ngay khi giải phóng thần thức ý niệm, hắn đã đồng thời luyện hóa và làm chủ kiện động thiên pháp bảo này, mọi sự việc bên trong đều nằm trọn trong một ý niệm của hắn.

Tâm trí hắn lúc này đã dồn cả ra thế giới bên ngoài, dấy lên sự tò mò vô hạn. Bởi vì khi phóng xuất thần thức ra ngoài, hắn cảm nhận rõ rệt nơi ngoại giới đang tràn ngập uy năng thời không hỗn loạn vô hình, mọi thứ dường như đều bị đảo lộn xáo trộn, đây hẳn là một nơi vô cùng đặc thù bên trong cõi hỗn độn vũ trụ này.

Sau khi trôi dạt hồi lâu trong cơn bão tố vô tận, pháp bảo động thiên hình viên linh châu màu đen rốt cuộc cũng trôi dạt tới một vùng đất đặc thù. Nơi đây tựa như một hòn đảo nằm trơ trọi giữa cơn bão cuồng nộ, có một lớp màng ngăn vô hình cách tuyệt bên trong với bên ngoài. Bên trong là một ngọn núi hoang vu tiêu điều, trên núi có một hang đá trống không, ngoài ra chẳng còn bất cứ thứ gì khác.

Thân ảnh Bạch Vân lặng lẽ xuất hiện trong hang đá, hắn khẽ chuyển động tâm ý thu viên linh châu động thiên vào trong cơ thể, đoạn cau mày quan sát hang đá trống trải xung quanh: “Dao động thời gian nơi này sao lại quỷ dị thế này, lúc thì đột ngột tăng tốc cực nhanh, lúc lại ngưng trệ, thậm chí đảo ngược thoái lui. Hỗn độn vũ trụ sinh sôi bình thường, làm sao lại có thể xuất hiện một nơi như thế này được?”

“Tuy nhiên, nơi này đối với việc ta cảm ngộ Thời Gian Chi Đạo, lĩnh ngộ Chung Cực Thời Gian Chi Đạo lại có trợ lực cực kỳ to lớn,” khẽ lẩm bẩm một câu, Bạch Vân liền trực tiếp ngồi xếp bằng xuống: “Có điều trước đó, ta phải nâng cao tu vi của mình lên cái đã. Tu vi hiện tại quả thực quá mức yếu ớt rồi.”

Bạch Vân nhắm mắt tĩnh tọa, ngay sau đó không gian quanh thân hắn liền bắt đầu vặn vẹo, năng lượng hỗn độn tinh thuần điên cuồng ùa vào, bị hắn thôn phệ hấp thu như cá gặp nước.

Nhục thân lột xác được cường hóa với tốc độ chóng mặt, tu vi của Bạch Vân cũng không ngừng thăng tiến, dễ dàng chạm tới cảnh giới Thế Giới Thần, sau đó dùng Thời Không Chi Đạo bước lên Đạo Quân, từng bước một thăng hoa, nhẹ nhàng đạt tới cảnh giới Vĩnh Hằng Đế Quân, hơn nữa còn là Vĩnh Hằng Đế Quân ở tầng thứ chúa tể đỉnh phong nhất.

Thực ra chỉ cần Bạch Vân muốn, hắn có thể dễ dàng dựa vào Thời Không Chi Đạo để trở thành Chí Tôn, muốn tìm hiểu thấu đáo Không Gian Chi Đạo của hỗn độn vũ trụ này để trở thành Chung Cực Không Gian Chí Tôn cũng chẳng phải chuyện gì quá mức khó khăn. Thế nhưng hắn lại không cam lòng dừng lại ở đó, mà muốn ngộ thấu Chung Cực Thời Không Chi Đạo chân chính. Bởi vì hắn có một dự cảm mãnh liệt: chỉ khi dựa vào Chung Cực Thời Không Chi Đạo hoàn mỹ nhất, phù hợp nhất với hỗn độn vũ trụ, mới có thể triệt để luyện hóa và làm chủ cõi hỗn độn vũ trụ này một cách hoàn hảo nhất.

Muốn thấu suốt Chung Cực Thời Không Chi Đạo để thành tựu Chí Tôn là điều vô cùng gian nan, nhưng với kinh nghiệm từng bước lên Chung Cực Chí Tôn trên Không Gian Chi Đạo trước đây, Bạch Vân tin chắc mình hoàn toàn có hy vọng. Hơn nữa, Thời Không Chi Đạo quá đỗi đặc thù, không có thời không thì vạn vật đều là hư vô, cho nên mọi đạo pháp khác thảy đều được dung nạp bên trong Thời Không Chi Đạo. Nắm giữ được thời không, tức là nắm giữ được tất cả.

Sau khi trở thành chúa tể đỉnh phong nhất, Bạch Vân dốc trọn một lòng tĩnh tu tham ngộ, suy ngẫm về Chung Cực Thời Gian Chi Đạo. Dựa vào cảnh giới cao thâm nhìn xa trông rộng, cộng thêm việc vốn đã có nhận thức cực sâu về Thời Gian Chi Đạo từ trước, lại có nơi có lưu tốc thời gian đặc thù này phụ trợ, tiến độ cảm ngộ của Bạch Vân suôn sẻ hơn nhiều so với dự liệu.

Thời gian chầm chậm trôi qua, chẳng rõ đã qua bao lâu, Bạch Vân vốn đã bước chân vào ngưỡng cửa lĩnh ngộ Chung Cực Thời Gian Chi Đạo, chỉ còn cách việc nắm giữ bản nguyên thời gian đúng một bước ngắn ngủi. Vào ngày hôm đó, hắn bỗng nhiên cảm nhận được từ bên ngoài có một luồng uy năng đáng sợ vô hình đang ập tới, trong đó ẩn chứa uy lực hỏa diễm rực cháy bản nguyên cùng sự cuồng bạo tột cùng của thời gian, khiến Bạch Vân giật mình bừng tỉnh khỏi cơn tĩnh tu.

Đột ngột mở bừng đôi mắt, ánh mắt Bạch Vân xuyên qua không gian nhìn thấy rõ ràng giữa cơn bão thời không vô tận đằng xa có hai bóng người đang điên cuồng chém giết lẫn nhau vô cùng thảm liệt.

“Hai vị Chung Cực Đế Quân ư? Một người theo Chung Cực Hỏa Diễm Chi Đạo, một người theo Chung Cực Thời Gian Chi Đạo? Theo tin tức ta nắm được, cõi hỗn độn vũ trụ này chỉ có duy nhất một vị Chung Cực Đế Quân, kẻ chưởng khống thời gian kia e là một Chung Cực Đế Quân mới thăng cấp chăng? Bọn họ sao lại đánh nhau thế này? Lẽ nào là vì tranh đoạt quyền chưởng khống phiến vũ trụ này?” Trong lòng Bạch Vân dấy lên mối nghi ngờ thầm kín.

Dựa vào cảm ứng không gian dò xét, Bạch Vân thấy rõ và cảm nhận được sự huyền diệu trong uy năng Chung Cực Chi Đạo khi hai người giao đấu. Đặc biệt là vị Vĩnh Hằng Đế Quân theo Chung Cực Thời Gian Chi Đạo kia, Chung Cực Thời Gian Chi Đạo mà người đó thi triển khiến Bạch Vân không khỏi kích động trong lòng, cẩn thận quan sát cảm nhận, chẳng mấy chốc đã lý giải sâu sắc và thấu suốt hơn về Chung Cực Thời Gian Chi Đạo đích thực.

Bất tri bất giác chìm đắm trong việc cảm ngộ Chung Cực Thời Gian Chi Đạo, Bạch Vân không hề nhận ra hai vị Chung Cực Vĩnh Hằng Đế Quân kia chém giết ngày một thảm liệt hơn, và chiến trường của bọn họ đang dần dần tiến sát về nơi hắn đang ẩn thân.

“Oành!” Cơn bão năng lượng rực cháy cuồng bạo tựa như một phương vũ trụ bị hủy diệt quét tràn ra bốn phương tám hướng. Bạch Vân lập tức bừng tỉnh, chỉ cảm thấy vạn vật xung quanh dường như đều bị ngọn lửa cuồng bạo vô tận quét sạch xóa nhòa, bao gồm cả không gian, và thứ duy nhất còn sót lại chính là thời gian vĩnh hằng.

“Thời gian vĩnh hằng... Ta hiểu rồi, hóa ra đây mới thực sự là Vĩnh Hằng Thời Gian Chi Đạo chân chính,” khẽ thì thầm một tiếng, quanh thân Bạch Vân bỗng tỏa ra ánh hào quang màu bạc trắng rực rỡ chói lòa. Uy năng chung cực đại diện cho thời gian vĩnh hằng lập tức quét tan cơn bão lửa cuồng bạo xung quanh.

Ánh mắt sáng rực rỡ, Bạch Vân ngay sau đó dường như chợt ngộ ra điều gì, không kìm được ngửa mặt cười lớn: “Thời gian, không gian, ha ha hóa ra là như vậy! Tuyệt diệu, quá đỗi tuyệt diệu! Chung Cực Thời Không hóa ra là như thế này, thời gian chung cực và không gian chung cực dung hợp làm một thể, đó mới chính là Đạo hoàn mỹ đích thực, Đạo bản nguyên nhất, Chung Cực Chi Đạo phù hợp nhất với hỗn độn bản nguyên. Quả nhiên đúng như ta suy đoán!”

“Ngươi là ai?” Giữa tiếng quát tháo kinh nộ, giữa cơn bão năng lượng hỗn loạn cuồng bạo đằng xa, người đàn ông cao lớn khoác trường bào màu bạc trắng lạnh lùng rõ ràng đã bị trọng thương nặng nề, ánh mắt sắc bén như điện nhìn chằm chằm vào Bạch Vân, trên khuôn mặt mơ hồ lộ ra một tia hoảng loạn bất an.

Ngước mắt nhìn gã, khóe miệng Bạch Vân khẽ nhếch lên một nụ cười đầy ý vị trêu ngươi: “Ta là ai ư? Ha ha, ta chính là chủ nhân của cõi hỗn độn vũ trụ này.”"""
    },
    {
      "chapter_id": 3,
      "chapter_index": 3,
      "title_translated": "Chương 706: Tiên Nhân?",
      "translated_content": """Không ngoài dự đoán, làn mây mù mỏng manh kia dưới sự tàn phá của cơn bão phong lôi cuồng bạo đã dễ dàng bị đánh tan tác, cơn bão lại càng thêm phần hung hãn cuồn cuộn quét thẳng xuống dưới.

Trên bầu trời cao, một lão giả gầy gò khoác áo bào trắng, trên đầu lơ thơ chẳng còn mấy sợi tóc, vẻ mặt phong trần đang điều khiển một pháp bảo tựa tấm gương hàn băng lơ lửng trên đỉnh đầu. Lão trừng mắt muốn rách cả khóe mi nhìn cơn bão phong lôi đang điên cuồng ập xuống, toàn thân bỗng bùng nổ ánh sáng trắng chói lòa, nhưng cũng chỉ miễn cưỡng chống đỡ được phạm vi vài trăm mét xung quanh mà thôi.

Phần lớn cơn bão còn lại điên cuồng tàn phá quét qua, nơi nó đi qua không gian đều vặn vẹo biến dạng, ánh chớp lôi điện rọi sáng vô số khuôn mặt hoảng sợ tuyệt vọng của người dân bên dưới Bạch Man bộ lạc.

Phía trước thánh điện của thành Bạch Man trong bộ lạc, Tam trưởng lão, Bạch Chước cùng ba vị lão giả khác vừa lao ra khỏi thánh điện. Đầy đủ năm vị cường giả cảnh giới Động Chân, nhưng đối mặt với cơn bão sấm sét rợp trời kia, bọn họ cũng không khỏi lộ rõ vẻ tuyệt vọng và bi phẫn.

“Chẳng lẽ trời thật sự muốn diệt vong Bạch Man bộ lạc ta sao?” Tam trưởng lão toàn thân run rẩy phát ra tiếng gầm đầy bất cam.

“Là Bạch Vân! Tất cả những tai họa này đều do Bạch Vân giáng xuống đầu Bạch Man bộ lạc! Hắn chính là tội nhân thiên cổ của toàn bộ tộc ta!” Một lão giả gầy gò mũi diều hâu gào thét căm hận.

Tiếng gào thét của lão vừa dứt, âm thanh sấm gió gào rít trên không trung bỗng nhiên im bặt tựa như biến mất, cơn bão phong lôi như bị ngưng đọng lại giữa hư không. Cùng lúc đó, một bóng người lặng lẽ xuất hiện giữa không trung, chính là Bạch Vân trong bộ áo bào trắng phiêu dật.

“Tán!” Ngước nhìn cơn bão phong lôi đang ngưng trệ, Bạch Vân chỉ khẽ quát lên một tiếng, ngay khoảnh khắc tiếp theo cơn bão phong lôi khủng khiếp kia liền trực tiếp tan biến không còn một dấu vết.

Bầu trời trong xanh trở lại, không gian bị ngưng trệ cũng hồi phục như thường. Mọi người trong Bạch Man bộ lạc định thần lại, nhìn thấy Bạch Vân đang lơ lửng giữa không trung với tà áo tung bay phần phật, nhìn thấy bóng lưng còng gầy guộc lộ vẻ suy yếu của Bạch Man lão tổ, và cũng nhìn thấy một gã đàn ông vạm vỡ khoác áo bào đen trên tầng trời cao tít tắp cùng một pháp bảo tựa như chiếc đại ấn khổng lồ rực sáng lôi quang đang lơ lửng trước mặt gã.

“Ngươi là kẻ nào? Dám to gan cản đường ta!” Gã đàn ông vạm vỡ áo đen ánh mắt sắc như điện nhìn chằm chằm Bạch Vân, xung quanh thân thể gã bão đen tự dưng sinh ra cuộn trào vần vũ.

“Bạch Vân!” Bạch Vân khẽ ngẩng đầu nhìn gã đàn ông áo đen, cất giọng nhẹ thoảng như mây gió thoảng, âm thanh trong trẻo vang vọng ngân nga giữa không trung.

Gã đàn ông áo đen ngẩn người. Với thân phận của gã, dĩ nhiên gã chẳng bao giờ thèm để mắt tới một hậu bối tép riu của Bạch Man bộ lạc. Hơn nữa trong số các cường giả Nguyên Thần mà gã biết, cũng tuyệt nhiên không có ai tên là Bạch Vân cả. Cho nên sau khi định thần lại, gã liền hừ lạnh một tiếng, tâm niệm khẽ động, chiếc đại ấn lấp lánh lôi quang trước mặt lập tức ầm ầm giáng thẳng xuống đầu Bạch Vân. Tia sét cuồng bạo xé rách không gian khiến hư không rung chuyển vặn vẹo.

Thế nhưng, đối mặt với chiếc lôi điện đại ấn mang uy năng hủy diệt cuồng bạo ấy, Bạch Vân chỉ hờ hững đưa tay lên hư ấn một cái. Một luồng uy năng trói buộc không gian vô hình lập tức khiến chiếc đại ấn kia bị giảm tốc độ rồi khựng lại giữa không trung. Tiếp đó Bạch Vân tùy ý phất tay một cái, chiếc đại ấn sấm sét liền bay vạt sang một khoảng hư không bên cạnh.

“Không Gian Chi Đạo sao?” Sắc mặt gã đàn ông vạm vỡ áo đen biến đổi thất thanh kêu lên.

Gần như ngay khi giọng nói của gã vừa dứt, thân hình Bạch Vân khẽ biến ảo lập tức xuất hiện ngay trước mặt gã, vung một ngón tay điểm tới, đầu ngón tay xuyên qua hư không trong chớp mắt hạ xuống ngay giữa mi tâm của gã.

“Xoẹt!” Một đạo đao mang sắc bén từ mi tâm gã đàn ông áo đen bắn vọt ra va chạm dữ dội với đầu ngón tay Bạch Vân, không gian chấn động mãnh liệt. Khoảnh khắc tiếp theo, đầu của gã đàn ông áo đen liền hóa thành tro bụi tan biến vào cõi hư vô.

“Oành!” Chiếc đại ấn sấm sét vừa bị đánh bay ra xa bỗng nhiên quay ngược trở lại, hung hãn đập mạnh về phía Bạch Vân.

Thân hình Bạch Vân lại biến ảo thuấn di né tránh, chiếc lôi điện đại ấn nện thẳng vào thi thể không đầu của gã áo đen, biến cái xác lập tức thành một khối than cháy đen sì.

“Ầm ầm ầm!” Đằng xa tiếng sấm rền vang rền rĩ, lực lượng phong lôi cuộn trào tụ hội, nửa bầu trời nhanh chóng tối sầm lại. Trong bão tố sấm sét mịt mù, thấp thoáng thấy một bóng người đang đạp gió cưỡi sấm cấp tốc lao vút tới.

“Lại thêm một cường giả Nguyên Thần nữa sao? Thỉ Dã thị này quả nhiên nội tình thâm hậu thật đấy!” Bạch Vân khẽ nhướng mày nhìn bóng người mang khí tức cuồn cuộn đang ngự phong lôi lao tới.

“Dám giết cường giả Nguyên Thần của Thỉ Dã thị ta, lá gan của ngươi không nhỏ đâu! Bất kể ngươi là ai, hôm nay ngươi chắc chắn phải chết!” Tiếng gầm thét giận dữ như sấm rền vang ra từ cơn bão phong lôi vô tận. Khoảnh khắc tiếp theo, chiếc lôi điện đại ấn đã cấp tốc bành trướng hóa thành một ngọn núi khổng lồ mang theo uy năng sấm sét điên cuồng ập xuống đầu Bạch Vân.

Bạch Vân cau mày ngẩng đầu, không hề có ý định né tránh, tùy ý giơ tay bắn ra một đạo kiếm quang từ đầu ngón tay, bắn thẳng vào bên trong ngọn núi đại ấn sấm sét.

Thế nhưng đạo kiếm quang kia lại không hề va chạm với chiếc đại ấn sấm sét, tựa như chiếc đại ấn khổng lồ kia chỉ là hư vô, kiếm quang xuyên thẳng qua đại ấn bay vút về phía bóng người giữa cơn bão phong lôi đằng xa.

Đồng thời chiếc lôi điện đại ấn nện thẳng xuống cũng trực tiếp xuyên qua thân thể Bạch Vân rơi tụt xuống dưới, cứ như thể hai bên vốn chẳng hề tồn tại trong cùng một tầng thời không vậy.

“Oành!” Trong tiếng nổ năng lượng cuồng bạo, cường giả Nguyên Thần của Thỉ Dã thị đối mặt với đạo kiếm quang quỷ dị kia bèn tung ra một quyền, lực lượng phong lôi cuộn trào nghênh đón kiếm quang.

“A!” Giây tiếp theo, một tiếng gầm rú đau đớn kìm nén đầy kinh nộ vang lên từ trong phong lôi, hiển nhiên đạo kiếm quang kia đã khiến đối phương bị trọng thương.

Khóe miệng Bạch Vân nhếch lên một nụ cười lạnh lùng, thân hình hắn biến ảo lao thẳng vào khu vực bão tố phong lôi kia. Ngay sau đó là một tiếng thét gào tuyệt vọng đầy sợ hãi vang lên, bão phong lôi tan biến hoàn toàn, trên bầu trời cao chỉ còn trơ trọi lại bóng hình Bạch Vân, và ngay trước mặt hắn là một vết nứt không gian dài hẹp.

“Chết rồi? Lão quái vật của Thỉ Dã thị cứ thế chết dưới tay Bạch Vân rồi sao?” Lão tổ Bạch Man bộ lạc trừng trừng mắt không dám tin vào những gì mình vừa chứng kiến.

Sau một thoáng im ắng đến nghẹt thở, ngay khi người dân Bạch Man bộ lạc đang vỡ òa trong niềm vui mừng khôn xiết và hò reo vang dội, thì trên bầu trời cao vết nứt không gian vốn dĩ sắp khép miệng lại đột ngột bị một luồng sức mạnh vô hình xé toạc ra lần nữa. Cùng lúc đó, một luồng khí tức kinh hoàng từ bên trong tràn ra ngoài, khiến toàn bộ người dân Bạch Man bộ lạc phía dưới lập tức nín bặt, từng người một vô thức kinh hãi ngước nhìn lên bầu trời cao.

“Hửm?” Bạch Vân khẽ cau mày cũng nhìn về phía vết nứt không gian vừa bị xé toạc ra kia. Chỉ thấy từ trong đó có ba người đàn ông khoác khôi giáp màu trắng bay vọt ra, khí tức đáng sợ kia chính là tỏa ra từ trên người bọn họ, khiến không gian xung quanh khẽ run rẩy như muốn vỡ vụn.

Trong cõi hư không cách đó không xa, lão tổ Bạch Man bộ lạc vừa kinh vừa sợ, toàn thân run rẩy trừng mắt run giọng thốt lên: “Tiên... Tiên nhân?”

“Tiên nhân ư?” Bạch Vân nhếch mép nở nụ cười giễu cợt nhìn ba người kia, bởi vì hắn cảm nhận rõ ràng ánh mắt ba kẻ đó nhìn về phía hắn lộ vẻ lạnh lẽo hờ hững, chẳng khác nào đang nhìn một con kiến hôi hèn mọn.

Khoảnh khắc tiếp theo, không một lời thừa thãi, ba người đàn ông mặc khôi giáp trắng liền đồng loạt vung ra ba sợi xích sắt màu trắng tựa như pháp bảo, hung hãn quấn về phía Bạch Vân.

Cảm nhận được uy năng trói buộc vô hình từ ba sợi xích trắng kia, ánh mắt Bạch Vân lạnh lùng, thân hình quỷ dị hòa vào hư không rồi biến mất tăm.

Thấy cảnh tượng đó, ba người đàn ông mặc khôi giáp trắng biến sắc. Còn chưa kịp có phản ứng gì, phía trên đầu bọn họ Bạch Vân đã lặng lẽ xuất hiện không một tiếng động, vung một chưởng từ trên cao giáng xuống. Không gian như ngưng trệ, thân hình cả ba người cứng đờ toàn thân chấn động dữ dội, ngay sau đó nhục thân tan rã hóa thành hư vô, chỉ còn sót lại ba bộ khôi giáp trắng cùng nhẫn trữ vật và các loại pháp bảo thần binh bản mệnh rơi rụng lại.

“Phóng túng!” Giữa tiếng quát uy nghiêm giận dữ, không gian vặn vẹo dữ dội, ngay sau đó một cự nhân cao hơn một trượng tựa như Kim Giáp Thiên Thần xuất hiện giữa bầu trời cao, vung chiếc búa vàng khổng lồ trong tay bỗng chốc to lớn như ngọn núi nhỏ đập thẳng xuống đầu Bạch Vân.

“Xoẹt!” Thân hình Bạch Vân biến ảo xuất hiện ngay trước mặt Kim Giáp Thiên Thần, chỉ tay điểm một cái, kiếm quang sắc bén đâm thẳng vào mắt gã khổng lồ.

Tận mắt nhìn thấy Kim Giáp Thiên Thần cứ thế bỏ mạng dưới tay Bạch Vân, lão tổ Bạch Man bộ lạc cùng toàn thể người dân bên dưới đều hóa đá chết lặng. Đó chính là tiên thần a! Bạch Vân vậy mà nói giết là giết nhẹ tựa lông hồng, chẳng lẽ hắn chính là chuyển thế của một vị đại năng tiên thần còn lợi hại hơn sao? Nếu không thì làm sao có thể đột nhiên trở nên khủng khiếp đến mức độ này?

“Lũ sâu kiến hèn mọn, dám to gan giết hại tiên binh thiên tướng, đáng chết!” Trên chín tầng trời phong vân biến sắc, một tiếng quát chói tai uy nghiêm rúng động khắp cả thế giới cõi hoàn vũ này."""
    }
  ]
}

Path("data").mkdir(exist_ok=True)

with open("data/translated_novel_2.json", "w", encoding="utf-8") as f:
    json.dump(novel_2_data, f, ensure_ascii=False, indent=2)

with open("data/translated_novel_1.json", "w", encoding="utf-8") as f:
    json.dump(novel_1_data, f, ensure_ascii=False, indent=2)

print("Generated data/translated_novel_2.json and data/translated_novel_1.json successfully!")
