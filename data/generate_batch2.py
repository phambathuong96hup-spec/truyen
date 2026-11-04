import json
import os

ch6_content = """Trở về nơi ở của mình, Thẩm Lập chỉ cảm thấy toàn thân khoan khoái, tinh thần vô cùng sảng khoái.
Nỗi u uất đè nặng nơi đáy lòng bấy lâu nay tựa như mây đen bị một cơn gió thổi tan, những khối uất ức dồn nén suốt bao năm qua phút chốc tiêu tan không còn một mảnh.
"Chỉ mới là kiếm pháp cấp Đại Sư mà đã có uy lực bực này!"
Nhớ lại chiêu kiếm "Kiếm Đoạn Hồi Khúc" vừa rồi, Thẩm Lập không khỏi dâng lên lòng hướng tới vị tiên tổ Thẩm gia từng sáng lập nên tuyệt kỹ này.
Hắn không kìm được rút thanh bội kiếm mà nguyên thân từng dùng lúc tập võ ra.
Ngẩng đầu nhìn lên vòm trời, cổ tay khẽ rung, vung ra một đóa kiếm hoa.
Dưới sự kích động của nội lực cuồn cuộn, thân kiếm khẽ reo lên vo ve, tựa như rồng ngâm hổ gầm.
Đưa tay xuất kiếm, hàn quang tỏa ra bốn phía.
Thi triển trọn vẹn những kiếm chiêu tổ truyền của Thẩm gia, trong phạm vi ba thước nước tạt không lọt.
"Đây là loại kỳ tài bực nào chứ!" Ánh mắt Thẩm Lập tràn đầy hưng phấn.
Tương truyền tiên tổ Thẩm gia chính là khai quốc công thần, làm tiên phong dẫn đường cho quân vương, dấy khói lửa bình định Sóc Châu.
Giữa thời buổi thiên hạ đại loạn tranh giành, ông từng lưng đeo thanh kiếm sắt, cùng mấy chục thủ hạ tinh nhuệ bí mật vòng qua đại quân địch.
Vào một đêm tuyết rơi trắng trời, giơ tay không thấy năm ngón.
Tiên tổ Thẩm gia thi triển khinh công cước đạp phi yến, lăng không bay vọt qua tường thành Sóc Châu kiên cố.
Một kiếm chém đứt cánh cổng sắt nặng ngàn cân, huyết chiến với mấy ngàn quân thủ thành, giành lấy danh xưng lẫy lừng "Thôi Thành Kiếm".
Thậm chí thành Sóc Châu sau đó còn đổi tên thành Phi Nhạn thành để ghi nhớ chiến công hiển hách ấy.
Nhưng sau khi thiên hạ thái bình định đoạt, công lao ngất trời như thế lại không được triều đình vẽ tranh lưu danh trên Lăng Yên Các.
Quá đỗi phẫn uất và thất vọng, Thẩm tổ cùng mấy chục thủ hạ trung thành năm xưa bèn mai danh ẩn tích, khai sơn lập phái, sáng lập nên Lăng Yên Cốc.
Nơi phật đường của sơn cốc, đến nay vẫn còn phụng thờ bức họa Thẩm tổ tuyết dạ hạ Sóc Châu oai phong lẫm liệt.
Thẩm Lập vung mạnh một kiếm, một đạo kiếm khí sắc bén xé gió bay lên khỏi mặt đất, để lại trên vách tường một vết chém sâu nửa tấc.
Thẩm Lập thở phào một hơi, lúc này mới thu tay dừng kiếm.
Cúi xuống nhìn thanh thiết kiếm trong tay, trên gương mặt thoáng lộ ra nét hài lòng.
Thế nhưng khi tra kiếm vào vỏ, hắn lại cảm thấy có chút rít và nặng nề.
Thẩm Lập khẽ nhíu mày: "Thế mà đã rỉ sét rồi!"
Hắn ngẩng đầu trầm ngâm suy nghĩ: "Không biết trong các phần thưởng điểm danh sau này, có ban thưởng binh khí thần binh lợi khí hay không."

Ngày hôm sau.
Thành Phi Nhạn bỗng nhiên lại có chuyện náo nhiệt khác thường.
Đám người nhàn rỗi tụ tập trên phố Lục Lý, tận mắt nhìn thấy biển hiệu của Khai Sơn võ quán và Lâm An tiêu cục đã bị người ta đập nát vụn.
Từ hai tòa viện lạc nằm sát vách nhau thỉnh thoảng lại truyền ra tiếng kêu khóc van xin tha mạng thảm thiết, ngay sau đó là một tên xui xẻo bị ném bổng ra ngoài đường.
Mỗi lần như vậy, đám người vây xem lại ồ lên reo hò, vô cùng phấn khích.
Một gã lưu manh trẻ tuổi tò mò chen vào đám đông, hỏi gã đồng bọn đang hào hứng đứng xem: "Võ quán cùng tiêu cục này bị người ta đến đá quán sao?"
"Đá quán? Nếu thật sự chỉ là đá quán thì đã tốt!" Gã kia lắc đầu cười cợt.
"Đá quán cùng lắm chỉ vì cầu chút danh tiếng, còn hôm nay là có người muốn tính sổ lấy mạng cả hai nhà này đấy."
Gã lưu manh trẻ tuổi mở to hai mắt, vẻ mặt đầy vẻ không dám tin:
"Thành Sóc Châu này của chúng ta do người Thẩm gia che chở, còn có kẻ dám tới đây gây sự sao?"
Gã nhàn hán liếc xéo hắn một cái: "Kẻ muốn lấy mạng bọn chúng chính là người mang họ Thẩm đấy!"
"Không thể nào!" Gã trẻ tuổi lắc đầu quầy quậy: "Thẩm gia xưa nay vẫn luôn..."
Hắn đang định phản bác thì trong đầu bỗng lóe lên hình bóng của một người.
Đó là kẻ được mệnh danh là ác bá giữa đường, hỗn thế ma vương của thành Phi Nhạn – nhị công tử Thẩm Lập!
Gã nhàn hán cười hì hì: "Đoán ra rồi chứ gì?"
"Nhưng lần này, tên kia không phải tới quậy phá bừa bãi đâu."
"Hôm trước hai nhà này nhận bạc của Thẩm gia mà không làm việc, lại còn dám mở miệng bất kính với hắn, hôm nay hắn liền tới tận cửa đòi nợ sòng phẳng!"
Gã lưu manh trẻ tuổi giật mình, trong lòng bất giác dâng lên vài phần kính nể.
Giang hồ vốn dĩ phải như vậy, ân oán phân minh, khoái ý ân cừu.
Mọi người nhìn Thẩm Lập chỉ cách một ngày đã trực tiếp tới đòi nợ, trái lại sinh lòng khâm phục dũng khí và thủ đoạn của hắn.
Thấy âm thanh ầm ĩ bên trong dần dần lắng xuống, có kẻ nhanh nhảu vội hô to: "Mau giải tán thôi, Thẩm nhị công tử sắp bước ra rồi!"
Mọi người cười òa một tiếng rồi lập tức tản ra tứ phía.
Thế nhưng câu chuyện của đêm nay ở thành Phi Nhạn lại có thêm một đề tài đắt giá để bàn tán bên bàn rượu.
"Ầm!"
Một tiếng vang lớn truyền tới, một đôi ủng thêu kim tuyến dẫm lên mảnh vỡ biển hiệu bước ra ngoài cửa.
Chính là Thẩm Lập.
Hắn từng hứa trong vòng ba ngày sẽ khiến hai nhà này không thể tồn tại, hôm nay vừa đúng kỳ hạn ba ngày.
Nhìn thấy ngoài phố Lục Lý ngổn ngang những kẻ đang nằm lăn lộn rên rỉ, trong lòng hắn dâng lên một cỗ sảng khoái tràn trề.
Gân cốt toàn thân như được giãn ra mấy phần nhẹ nhõm.
"Kể từ hôm nay, hai nhà các ngươi nếu một ngày chưa dọn đi, ta sẽ mỗi ngày tới đây lĩnh giáo một lần!"
Lạnh lùng buông lại một câu răn đe, hắn chẳng thèm để ý đến những tiếng kêu khóc cầu xin phía sau nữa.
Hôm nay tới đòi nợ chỉ là tiện đường giải quyết, trong lòng hắn còn có một việc quan trọng hơn nhiều.
Đó chính là khảo sát các địa điểm có thể điểm danh trong thành Phi Nhạn.
Còn về lý do tại sao không tiếp tục điểm danh ở Lăng Yên Cốc, đương nhiên là vì kiêng kỵ người đại ca tốt kia của hắn.
Tuy hiện tại đã có hai phần thực lực tự vệ, nhưng hắn vẫn chưa muốn quá sớm đối đầu trực diện với rắc rối do Thẩm Ngọc mang lại.
"Ít nhất cũng phải tích lũy thêm một môn võ học cấp Hoàn Mỹ nữa."
Hạ quyết tâm trong lòng, hắn một mình thong thả dạo bước khắp các ngõ ngách trong thành.
Đi dạo suốt nửa ngày, hắn đại khái đã nắm được những địa điểm nào có thể kích hoạt điểm danh:
Sòng bạc, phường phong nguyệt, y quán, bến tàu, tiêu cục, quận phủ...
Thế nhưng những nơi như chợ rau, thư viện, khách điếm, tiệm phấn son hay tiệm nhang đèn lại không hề có bất kỳ gợi ý điểm danh nào.
Hiện tượng này khiến Thẩm Lập nảy sinh phán đoán: "Chẳng lẽ là... liên quan đến giang hồ và thế lực ngầm?"
Chính vì những nơi kia gắn liền với chốn giang hồ gió tanh mưa máu, tranh chấp thị phi, cho nên mới đủ tư cách để hệ thống mở điểm danh.
Để nghiệm chứng quy luật này, hắn một lần nữa cất bước đi tới Vạn Hoa Lâu.
Quả nhiên không ngoài dự đoán.

【Ting! Phát hiện địa điểm có thể điểm danh: Vạn Hoa Lâu. Túc chủ có muốn điểm danh không?】

Thẩm Lập khẽ nở nụ cười thầm.
Vừa định nhấc chân bước vào xem thử nơi này náo nhiệt ra sao.
Một gã quản sự tinh mắt vừa trông thấy vị tiểu tổ tông này liền thất kinh hồn vía.
Hắn hoảng hốt chạy vội tới trước mặt Thẩm Lập, hai tay ôm chặt lấy chân hắn, giọng run rẩy van lơn:
"Gia... gia gia của con ơi, hôm nay thật sự không phải lúc đâu ạ!"
"Tiểu điếm đang đón một vị hào khách lớn, các cô nương đều bận rộn cả rồi, không ai rảnh rỗi hầu hạ đâu ạ!"
Miệng hắn liến thoắng như bắn pháo hoa, vừa cầu xin vừa dập đầu lia lịa.
Thẩm Lập có chút không vui: "Bản công tử tới chỗ ngươi nghe hát uống rượu cũng chẳng ít lần, ngươi lại dám cản ta? Sợ ta không trả tiền sao?"
"Dám đem mấy lời này ra thoái thác với ta à!"
Gã quản sự trong lòng khổ không tả xiết. Thầm nghĩ mỗi lần ngài tới đây chỉ gọi mấy khúc nhạc thanh nhã, cắn đĩa hạt dưa, uống vài chén trà thanh, tiểu điếm kiếm được bao nhiêu tiền của ngài?
Lần trước ngài thẳng tay đốt cả xấp văn tự bán thân của các cô nương, chỗ tiền đó đủ để ngài uống trà cả vạn năm rồi.
Trong bụng oán thán đủ điều, nhưng ngoài mặt gã nào dám biểu lộ ra nửa phần.
Gã khẩn thiết giải thích: "Thật sự là không đúng dịp mà công tử!"
"Sáng nay có một vị khách hào phóng vung ra hai ngàn lượng bạc trắng, bao trọn toàn bộ Vạn Hoa Lâu."
"Bắt tất cả các cô nương đều phải ra tiếp đãi một mình hắn."
Hai ngàn lượng?
Thẩm Lập nghe xong cũng há hốc mồm, đây quả thực không phải con số nhỏ.
Ở Vạn Hoa Lâu này, tiền thưởng cho danh kỹ đứng đầu một đêm cũng chỉ mười lượng bạc, hai ngàn lượng đủ để nuôi dưỡng một đóa hoa khôi suốt mấy năm ròng.
Hắn bĩu môi hừ một tiếng: "Một mình hắn mà tiếp nổi sao? Bộ hắn mình đồng da sắt chắc?"
Gã quản sự cười gượng: "Vị quý khách kia tính tình kỳ quái vô cùng, chẳng hề động chạm đến cô nương nào cả."
"Hắn chỉ bắt các nàng tắm rửa sạch sẽ, trang điểm lộng lẫy, rồi từng người một xếp hàng đứng đó để hắn... ngắm nghía!"
"Hễ thấy ai dung mạo xuất chúng, phong thái đoan trang là hắn liền lập tức múa bút vẽ tranh, họa lại dáng vẻ của cô nương đó lên quạt!"
Nghe tới miêu tả này, trái tim Thẩm Lập khẽ giật thót.
Trong đầu hắn đột nhiên hiện lên hình bóng của một nhân vật truyền kỳ trong giới võ lâm.
Hắn vội vàng gặng hỏi: "Kẻ đó có phải luôn mang bên mình một chiếc quạt xếp, trên quạt vẽ toàn mỹ nhân tuyệt sắc hay không?"
Gã quản sự ngước đầu ngẫm nghĩ một lát rồi gật đầu lia lịa: "Đúng đúng! Chiếc quạt đó quả thực vẽ toàn mỹ nhân đẹp như tiên giáng trần!"
"Thôi hỏng rồi!"
Tâm thần Thẩm Lập chấn động dữ dội. Hắn không ngờ ở cái chốn Sóc Châu xa xôi hẻo lánh này lại có thể đụng độ nhân vật phong vân cỡ đó.
Hắn không kìm được nuốt một ngụm nước bọt.
Đó chính là đệ tử chân truyền của Tà Vương Thạch Chi Hiên phái Ma Môn – Đa Tình Công Tử Hầu Hi Bạch! Một kẻ có thực lực sâu không lường được, tính tình lại cực kỳ quái đản, kiểu cách, hành sự xưa nay chưa từng theo lẽ thường.
Nếu lỡ bị tên này để mắt quấn lấy thì sẽ là một mối phiền toái khôn lường.
Thẩm Lập vội gạt phắt tay gã quản sự ra, xoay người định lập tức rời khỏi nơi thị phi này.
Nhưng ngay khoảnh khắc quay lưng, trong đầu hắn bỗng nảy ra một ý nghĩ.
"Hệ thống, điểm danh tại Vạn Hoa Lâu!"

【Ting! Vị trí điểm danh hiện tại: Vạn Hoa Lâu.】

【Lần đầu điểm danh tại Vạn Hoa Lâu, kích hoạt cơ hội bạo kích phần thưởng, túc chủ có sử dụng không?】

"Sử dụng ngay!"

【Ting! Chúc mừng túc chủ điểm danh thành công, nhận được kỹ năng: Thiên Nhãn Thông (Cấp Hoàn Mỹ)!】"""

ch7_content = """【Thiên Nhãn Thông (Cấp Hoàn Mỹ): Danh xưng đầy đủ là Thiên Nhãn Trí Chứng Thông, còn gọi là Thiên Nhãn Trí Thông hoặc Thiên Nhãn Thông Chứng, là một môn đại thần thông của Phật môn dùng để thấu suốt vạn sự vạn vật trong cõi nhân gian.】

【Đặc tính 1: Cảnh Giới Sở Trì. Thuộc tính bị động bẩm sinh, không cần chủ động thôi động, hoàn toàn không tiêu hao nội lực chân khí.】

【Đặc tính 2: Ngũ Sắc Bất Mê. Thiên Nhãn Thông nhìn thấu sự vật qua chiều không gian nhân quả vượt ngoài ngũ sắc, không bị thuật dịch dung hay liễm tức che mắt, có thể xuyên qua lớp vỏ ngoài để nhìn thấu bản chất bên trong.】

【Đặc tính 3: Thanh Tịnh Thiên Nhãn. Sở hữu Thiên Nhãn Thông có thể phá tan mọi hư vọng ảo ảnh, miễn nhiễm với tất cả các loại công pháp mê hồn và huyễn thuật.】

【Đặc tính 4: Phật Pháp Chí Bảo. Gia tăng cực đại uy lực của các môn võ công thuộc Phật môn, giúp người tu luyện dễ dàng lĩnh ngộ Phật lý và thiền cơ thâm sâu.】

【Đặc tính 5: Sinh Tử Trí Chứng. Có khả năng cảm tri rõ ràng thiện ác nhân quả, người mang thần thông sẽ tự nhiên hướng thiện trừ ác, dần dần hun đúc tâm tính quang minh lỗi lạc.】

Năm đại đặc tính kinh người!
Nếu như Cửu Dương Thần Công vẫn còn nằm trong phạm trù võ học nhân gian có thể lý giải, thì môn Thiên Nhãn Thông này đã hoàn toàn vượt xa cảnh giới phàm trần.
"Thậm chí có thể nhìn thấu sự vật qua sợi dây nhân quả?"
Thẩm Lập vui mừng khôn xiết, nhưng khi đọc đến đặc tính thứ năm – Sinh Tử Trí Chứng, trong lòng hắn lại dâng lên chút băn khoăn:
"Dần dần hướng về hành hiệp trượng nghĩa, trừ gian diệt ác? Nói cách khác, tâm tính của mình sẽ chịu sự ảnh hưởng của kỹ năng này?"
"Vậy sau này mình đâu có bị biến thành hòa thượng xuất gia đấy chứ?"
Nhưng sau cùng, khát khao sở hữu thực lực cường đại đã chiến thắng chút lo âu mơ hồ ấy.
Hắn khẽ cười trừ: "Cứ sống sót qua cơn nguy khốn này trước đã rồi tính tiếp!"
Nói đoạn, Thẩm Lập lập tức vận dụng thử Thiên Nhãn Thông nhìn vào từng người đi đường xung quanh.

【Ngư Văn Quang, Tiềm năng võ học: 1.1】
【Úc Văn Bân, Tiềm năng võ học: 1.3】
【Hứa Thái Ninh, Tiềm năng võ học: 0.1】
【...】

Đa phần người bình thường đều chỉ dao động quanh mức 1 điểm, còn những người tàn tật ăn xin bên lề đường thậm chí rớt xuống mức 0.1.
Hắn cúi đầu nhìn gã quản sự đang khom lưng trước mặt:

【Trần Tam Thái, Tiềm năng võ học: 2.5】

Cũng tàm tạm!
Thẩm Lập khẽ gật đầu.
Đang lúc hắn nhìn ngó xung quanh, một bóng dáng đẫy đà bỗng xuất hiện trước mắt.
Một người đàn ông trung niên mang bộ mặt tươi cười giả lả, phía sau dẫn theo mấy tên hộ viện cao lớn, trên tay còn dắt một cô bé ăn mặc giản dị, dáng vẻ rụt rè sợ sệt.
Một chuỗi thông tin lập tức hiển hiện rõ ràng trong tầm mắt Thẩm Lập:

【Họ tên: Vạn Tra Kiệt.】
【Tuổi tác: 51 tuổi.】
【Cảnh giới: Hậu Thiên tứ trọng.】
【Võ học: Chọc Tâm Chỉ (Cao cấp), Đoạn Cân Thôi Cốt Tam Thập Tiên (Trung cấp)...】
【Khinh công: Linh Thử Quá Du Oa (Cao cấp).】
【Kỹ năng: Không có.】
【Binh khí: Roi da bò (Phổ thông), Thiết Câu Hoàn (Nhị phẩm), Hình Mệnh Châm (Nhất phẩm).】

Theo bản năng, trong ánh mắt Thẩm Lập thoáng hiện một tia chán ghét.
Kẻ này chính là chưởng quầy đứng sau Vạn Hoa Lâu, kẻ nắm giữ mạng lưới buôn bán tỳ nữ và khế ước lao dịch khét tiếng ở thành Sóc Châu – Vạn Tra Kiệt.
Một kẻ thủ đoạn âm hiểm như thế, thế mà ra ngoài vẫn được người đời xưng tụng là một vị danh túc giang hồ.
"Nhị công tử, hôm nay ngọn gió nào đưa ngài tới chốn này thưởng nhạc thế?"
Vạn Tra Kiệt bày ra bộ mặt hòa nhã, chắp tay chào hỏi.
Thẩm Lập thân là người trong giang hồ, cũng đành nén cơn khó chịu chắp tay đáp lễ:
"Vạn lão bản cũng được xem là tiền bối trong chốn giang hồ."
"Mấy hôm trước có gây chút phiền toái cho Vạn lão bản, hôm nay sao có thể không ghé qua ủng hộ việc làm ăn, bù đắp đôi chút."
Vạn Tra Kiệt cười lớn sảng khoái, dường như hoàn toàn không để bụng chuyện cũ.
Ngược lại gã còn cất giọng xoa dịu Thẩm Lập:
"Nhị công tử quả là người phóng khoáng, có thể để mắt tới tiểu điếm cũng là vinh hạnh của lão già này."
Nói đoạn, gã kéo cô bé đang run rẩy phía sau ra phía trước, cười giới thiệu:
"Hôm nay quả thực không khéo, để công tử phải đi một chuyến tay không."
"Nha đầu này tên là Tiểu Trân Châu, vừa mới vào lầu học việc, tính tình ngoan ngoãn. Quý khách trên lầu chê tuổi còn nhỏ nên chưa dùng tới."
"Công tử cứ việc dẫn nàng về phủ lo việc trà nước quét dọn, cũng xem như là chút lễ mọn tạ lỗi của lão Vạn ta."
Lời nói nghe qua thì khách khí chu đáo, nhưng trong lòng Vạn Tra Kiệt lại đang xót xa vô cùng.
Vừa rồi thấy Thẩm Lập cứ lượn lờ trước cửa lầu không chịu đi, gã dĩ nhiên chẳng ngây thơ nghĩ rằng đối phương tới xin lỗi mình.
Muốn tiễn bước vị ôn thần này, gã đành phải cắn răng dùng hạ sách này để dỗ dành.
Thế nhưng Thẩm Lập vốn chẳng hứng thú gì với việc nhận người, trái lại đối với hành vi coi người như đồ vật trao đổi của gã càng thêm phần chán ghét.
Đang định mở miệng cự tuyệt, ánh mắt Thẩm Lập bỗng nhiên bắt gặp phía sau cánh cửa có vài cái đầu nhỏ đang thập thò lén nhìn, khiến hắn bất giác sững người.
Vạn Tra Kiệt thấy thần sắc hắn khác lạ, vội quay đầu nhìn lại.
Hóa ra là mấy cô bé tỳ nữ học nghệ khác trong lầu, biết tin Tiểu Trân Châu sắp được đưa đi nên lén ra tiễn chân. Nhưng vì sợ hãi danh tiếng của Thẩm nhị công tử nên chỉ dám nép sau cánh cửa, không dám lộ diện.
"Đúng là kẻ lòng tham không đáy!" Vạn Tra Kiệt thầm rủa trong bụng, đoán chừng Thẩm Lập chê một người hầu là quá ít.
Ngoài mặt gã vẫn nở nụ cười đon đả, vẫy tay gọi mấy đứa nhỏ kia bước ra, đẩy tới trước mặt Thẩm Lập:
"Nhị công tử quả nhiên hào hoa phong nhã!"
Rồi gã quay sang bảo mấy đứa nhỏ: "Nếu các ngươi lưu luyến Tiểu Trân Châu, chi bằng cùng theo nàng về phủ Thẩm gia hầu hạ nhị công tử luôn thể."
Thế nhưng gã vạn lần không ngờ, lúc này Thẩm Lập đã bị chấn động tới mức lặng người.
Bởi vì trong số những gương mặt non nớt ấy, xuất hiện một dòng chữ khiến hắn kinh ngạc đến tột độ:

【Hương Tuyết, Tiềm năng võ học: 22.7!】

Đó là một cô bé mày thanh mắt sáng, nét mặt lộ rõ vẻ lanh lợi thông minh, nhưng trong đáy mắt thỉnh thoảng lại lóe lên một tia tinh quái.
Nghe thấy lời Vạn Tra Kiệt, Thẩm Lập bừng tỉnh khỏi cơn sững sờ.
Hắn bật cười lắc đầu: "Vạn lão bản hiểu lầm rồi, ta chỉ muốn đổi sang một người khác mà thôi."
Nói rồi hắn đưa ngón tay chỉ thẳng về phía cô bé tên Hương Tuyết: "Nếu Vạn lão bản chịu nhường lại cô bé này, ta sẽ dẫn nàng về."
"Không biết muốn chuộc khế ước cho nàng thì cần bao nhiêu bạc?"
Nghe thấy Thẩm Lập không đòi mang tất cả đi, Vạn Tra Kiệt thở phào nhẹ nhõm một hơi.
Gã lập tức vung tay hào phóng: "Nhị công tử cứ việc dẫn nàng đi, hà tất phải nhắc tới chuyện tiền nong làm gì cho tổn hại giao tình!"
Vừa nói gã vừa nhận lấy tờ văn tự khế ước từ tay tên thuộc hạ, nhét thẳng vào tay Thẩm Lập.
Thẩm Lập giả bộ khước từ đôi câu, cuối cùng đành nhận lấy tờ khế ước, chắp tay cảm tạ.
Sau đó hắn dẫn theo Hương Tuyết xoay người rời bước.
Nhìn thấy ôn thần đã đi xa, Vạn Tra Kiệt mới trút được gánh nặng trong lòng, lẩm bẩm chửi thề rồi quay bước vào trong.

Đi tới cuối con phố, Thẩm Lập không kìm được dừng bước, cúi đầu nhìn cô bé còn chưa cao tới nách mình.
"Ngươi tên là gì?"
Hương Tuyết đang lo lắng bồn chồn, nghe thấy tiếng hỏi liền giật nảy mình như một con thỏ con hoảng sợ.
Nàng vội vàng ngước lên: "Dạ... bẩm công tử, tên con là Hương Tuyết."
Trông thấy bộ dạng sợ sệt của nàng, Thẩm Lập biết nàng bị những lời đồn thổi hung ác về mình dọa sợ.
Hắn cố gắng nở một nụ cười ôn hòa, nói: "Đừng sợ, ta đâu phải loài mãnh thú ăn thịt người."
Hương Tuyết gượng gạo nặn ra một nụ cười cứng đờ: "Dạ... vâng ạ!"
Thẩm Lập khẽ thở dài, rồi dừng hẳn bước chân lại.
Hắn thò tay vào ngực áo, lấy ra tờ văn tự khế ước vừa nhận được, nhét thẳng vào đôi bàn tay nhỏ bé của nàng, nghiêm túc nhìn nàng nói:
"Ngươi thật sự không cần phải sợ hãi. Ta chuộc ngươi ra là muốn nhận ngươi làm đệ tử truyền thụ võ nghệ, chứ tuyệt đối không có ý làm hại ngươi."
"Nếu ngươi không muốn theo ta, cầm lấy tờ khế ước này, bất cứ lúc nào cũng có thể tự do rời đi."
Hương Tuyết ngẩn người kinh ngạc.
Nhìn vào ánh mắt chân thành, đĩnh đạc của Thẩm Lập, nàng nhận ra hắn hoàn toàn không nói dối. Sự sợ hãi trong lòng nàng phút chốc tan biến, thay vào đó là một niềm xúc động khó tả.
"Công tử, con... con..."
Hương Tuyết cảm thấy bối rối vô cùng, vừa mừng vừa sợ, nhất thời không biết nên mở lời thế nào.
Thẩm Lập mỉm cười, nắm lấy bàn tay nhỏ bé của nàng:
"Thời gian còn dài, ngươi chưa cần vội trả lời ngay."
"Đi thôi, trước tiên đi lấp đầy cái bụng đã."
Hương Tuyết ngoan ngoãn gật đầu, để mặc cho hắn nắm tay dắt đi.
Đi được một đoạn, nàng bỗng ngập ngừng ngước lên hỏi nhỏ:
"Công tử, từ nay về sau, con cũng được mang họ Thẩm chứ ạ?"
Thẩm Lập thuận miệng đáp: "Được chứ, gạt bỏ quá khứ đau buồn đi, sau này gọi là Thẩm Hương Tuyết nghe cũng rất êm tai."
"Dạ." Nàng cúi đầu, lí nhí đáp một tiếng nhẹ như tiếng muỗi kêu.
"Thẩm Hương Tuyết, ngươi..."
Thẩm Lập đang định hỏi nàng muốn ăn món gì, nhưng cái tên vừa thốt ra khỏi miệng bỗng khiến hắn cảm thấy quen thuộc lạ kỳ.
Chỉ một thoáng sau, hắn bừng tỉnh nhận ra, cả người như bị một tia sét đánh trúng!
Hắn mở to hai mắt, vẻ mặt tràn đầy kinh ngạc:
"Thẩm Hương Tuyết! Nàng chính là Thẩm Hương Tuyết của Ngọc Nữ Tông!"
"""

ch8_content = """Hai người bước vào một tửu lầu thanh nhã bậc nhất trong thành, gọi một bàn thức ăn thịnh soạn trị giá tới bảy lượng bạc trắng.
Hoa quả tươi ngon theo mùa, thịt rừng thơm phức do thợ săn liều mạng săn được nơi rừng sâu, cá chép vàng tươi rói vừa kéo lưới từ đáy sông.
Mùi hương ngào ngạt lan tỏa, nhìn thôi cũng đủ khiến người ta thèm thuồng.
Thế nhưng nhìn cô bé trước mặt đang háo hức ăn uống ngon lành, đầu óc Thẩm Lập vẫn còn ong ong từng hồi, chẳng còn tâm trí nào để đụng đũa.
Thẩm Hương Tuyết của Ngọc Nữ Tông, chính là một trong những nữ nhân vật kiệt xuất trong cuốn danh tác "Thiên Địa Minh Hoàn" của Hoàng lão gia tử.
Tính tình nàng thông minh lanh lợi, cổ quái tinh nghịch, có thể coi là một Hoàng Dung phiên bản của Hoàng lão.
Bản thân mình chỉ thuận chân đi dạo một vòng, thế mà lại nhặt được một vị nữ thiên kiêu tương lai về nhà?
Một cảm giác vận mệnh an bài trào dâng trong lòng hắn.
Tựa như có một bàn tay vô hình đang âm thầm thao túng số phận, khiến Thẩm Lập bất giác rùng mình.
Thấy công tử cứ ngồi nhìn mình chằm chằm, Thẩm Hương Tuyết dường như cũng nhận ra điều bất thường, ngượng ngùng đặt đôi đũa xuống bàn.
Nàng chớp mắt lo lắng: "Công... công tử, sao người không ăn gì thế ạ?"
Dù miệng hỏi đầy vẻ quan tâm, nhưng ánh mắt lém lỉnh của nàng vẫn không nhịn được liếc trộm đĩa chân giò pha lê bóng nhẫy thơm phức trước mặt Thẩm Lập mà hắn vẫn chưa hề đụng tới.
"Haha~"
Thẩm Lập không nhịn được bật cười, bèn đẩy cả đĩa chân giò sang trước mặt cô bé:
"Ăn đi, sau này nếu muốn theo ta học võ thì phải bồi dưỡng sức lực cho thật tốt."
Hương Tuyết thấy hắn không hề giận, lúc này mới an tâm ôm lấy món ngon mà thưởng thức.
Tuổi nhỏ đang tuổi ăn tuổi lớn, nàng đối với sơn hào hải vị tự nhiên chẳng có chút sức kháng cự nào.
Dáng vẻ ăn uống hồn nhiên của nàng khiến Thẩm Lập mỉm cười nhẹ nhõm, chút lo lắng mơ hồ trong lòng cũng theo đó tan biến.
Bình tâm suy nghĩ lại, Thẩm Lập không khỏi cảm thấy phấn chấn lạ thường.
Đó là Ngọc Nữ Tông cơ đấy, một siêu cấp tông môn trong tương lai đủ sức khuấy đảo đại thế thiên hạ!
Chuyện này chẳng khác nào trời ban cho hắn một chỗ dựa vững chắc mai sau hay sao?
Sau khi ăn no nê, mọi nghi ngại trong lòng Hương Tuyết hoàn toàn tan biến.
Nàng nghiêm túc dâng trà hành lễ bái sư ngay tại chỗ.
Bản tính ngây thơ vui tươi của cô bé cũng được giải phóng, suốt dọc đường về nhà ríu rít nói cười như một chú chim sẻ non rộn rã.
Điều đó khiến Thẩm Lập cảm thấy vô cùng an ủi:
"Bất luận nàng có phải là Thẩm Hương Tuyết khuấy đảo phong vân sau này hay không, chí ít hôm nay mình cũng đã cứu được một mảnh đời."
Chỉ có một điều khiến Thẩm Lập dở khóc dở cười là dù hắn nhắc nhở thế nào, cô bé bướng bỉnh này vẫn nhất quyết không chịu gọi hắn là sư phụ, mà chỉ khăng khăng gọi hắn là "công tử".
Thẩm Lập đành bất đắc dĩ chiều theo ý nàng.

Thẩm Lập đưa Thẩm Hương Tuyết về tiểu viện của mình, ngoài mặt xưng là tỳ nữ mới nhận vào phủ, nhưng trên thực tế hai người sống với nhau theo danh nghĩa thầy trò.
Những ngày sau đó, mang theo tâm niệm muốn bồi dưỡng một kỳ tài võ học, Thẩm Lập dốc lòng chỉ dạy cho nàng từng đường đi nước bước.
Tiềm năng võ học của Thẩm Hương Tuyết đạt tới 22.7, quả thực là thiên tài ngút trời hiếm thấy trong nhân gian.
Bất kỳ khẩu quyết kiếm pháp hay tâm pháp nào, chỉ cần Thẩm Lập giảng giải sơ qua là nàng đã có thể lĩnh hội thông suốt, thậm chí suy một ra ba.
Vì vậy, Thẩm Lập bèn chép lại những môn công pháp sơ nhập mà mình thu được từ các lần điểm danh trước đây đưa cho nàng rèn luyện.
Còn những bí tịch nguyên bản mà hệ thống ban thưởng, sợ người khác phát hiện sẽ kinh thế hãi tục, hắn cất kỹ trong kho không gian của hệ thống.
Chỉ trong vỏn vẹn vài ngày ngắn ngủi, Thẩm Hương Tuyết đã ngưng tụ ra chân khí, trực tiếp bước vào cảnh giới Hậu Thiên nhất trọng!
Tiến cảnh thần tốc ấy khiến Thẩm Lập vừa mừng rỡ lại vừa thầm thán phục.
Nhờ có công pháp bồi đắp và ăn uống đầy đủ, khí chất của nàng ngày càng thanh thoát, da dẻ trắng ngần mịn màng, ngũ quan xinh xắn toát lên vẻ linh động thoát tục, quả không hổ danh là hạt giống thiên kiêu của Ngọc Nữ Tông.
Thấy đệ tử tiến bộ như vũ bão, Thẩm Lập càng ý thức được bản thân không thể giậm chân tại chỗ, cần phải nỗ lực gấp bội để làm gương sáng cho đệ tử noi theo.

Những ngày tiếp theo, có lẽ do vận may đã dồn hết vào việc gặp được Thẩm Hương Tuyết, nên những phần thưởng điểm danh sau đó của hắn đều không mấy nổi bật:

【Túc chủ điểm danh thành công tại sòng bạc Thanh Vân, nhận được võ học: Tróc Điểu Công (Sơ cấp).】
【Túc chủ điểm danh thành công tại lò rèn Lưu Kim, nhận được binh khí: Hàn Tinh Kiếm (Thất phẩm).】
【Túc chủ điểm danh thành công tại Hành Viễn tiêu cục, nhận được ám khí: Kim Tiền Tiêu (Nhị phẩm).】
【Túc chủ điểm danh thành công tại nhà lao nha môn, nhận được đao pháp: Trảm Thủ Đao Pháp (Trung cấp).】
...

Không hề có thêm môn võ học hay kỹ năng nào đạt cấp Hoàn Mỹ.
Trong số các vật phẩm và trang bị nhận được, giá trị cao nhất chỉ có một con Kỳ Độc Đại Phúc Xà phẩm cấp bát phẩm và thanh Hàn Tinh Kiếm thất phẩm.
Những thứ còn lại đều chỉ là công phu giang hồ tầm thường.
Thanh Hàn Tinh Kiếm có xuất xứ từ kiếm phổ của một hào hiệp cảnh nội Lý Đường, thân kiếm dài hai thước rưỡi, hàn quang lấp lánh sắc bén, sát khí bức người.
Khi rót nội lực vào, mũi kiếm khẽ rung lên bần bật, kiếm mang co giãn bất định, khiến Thẩm Lập vô cùng ưng ý.
Còn con Kỳ Độc Đại Phúc Xà kia thì lai lịch lại quá đỗi quen thuộc đối với hắn!
Đó chính là con đại bảo xà từng xuất hiện trong "Anh Hùng Xạ Điêu", bảo vật mà lão độc vật Lương Tử Ông đã hao tổn biết bao kỳ hoa dị thảo quý hiếm trong suốt hai mươi năm ròng rã nuôi dưỡng, khiến máu của con rắn này trở thành linh dược đại bổ vô giá trong thiên hạ.
Năm xưa nhân vật chính Quách Tĩnh nhờ uống cạn máu của nó mà công lực tăng vọt hai mươi năm, bách độc bất xâm!
Thẩm Lập nhìn con rắn lớn thân to như trăn, vảy óng ánh, đầu rắn dữ tợn bốc lên mùi hương kỳ lạ, không khỏi cảm thán trước sự hào phóng của hệ thống.
Đối với người thường, nọc độc của con rắn này chạm vào là chết ngay lập tức, nhưng Thẩm Lập có Cửu Dương Thần Công hộ thể, căn bản không hề e ngại độc tính.
"Xoẹt!"
Hắn vung kiếm chém đứt đầu rắn.
Dòng máu đỏ thắm tuôn trào vào chiếc bát lớn, bốc lên từng làn sương huyết mờ ảo mang theo mùi thơm ngát lạ kỳ.
Thẩm Lập hít vào một hơi, chỉ cảm thấy kinh mạch toàn thân thư thái, tinh thần phấn chấn tột độ.
"Quả nhiên là đại bổ dược!"
Hắn bưng bát máu rắn linh dược lên, uống một hơi cạn sạch, thậm chí còn liếm sạch từng giọt còn vương nơi khóe miệng.
"Tiết kiệm là quốc sách, chẳng có gì phải xấu hổ cả!"
Ngay sau đó, một luồng nhiệt lưu cuồn cuộn như ngọn lửa bùng lên từ trong bụng, từ đan điền men theo các kinh mạch chảy xiết khắp toàn thân.
Chân khí trong khí hải sôi trào mãnh liệt, tựa như một đốm lửa rơi vào kho thuốc súng, tạo nên một vụ nổ kinh thiên động địa!
"Ầm!"
Chân khí bạo liệt như một con nộ long tung hoành ngang dọc trong cơ thể.
Chân khí Cửu Dương vốn dĩ mang sắc tím thuần hậu nay bỗng chuyển sang màu đỏ rực hung mãnh.
Không cần hắn phải chủ động điều khiển, Cửu Dương Thần Công tự động vận chuyển với tốc độ kinh hồn khiếp vía.
Trước đây một đại chu thiên phải mất ít nhất hai canh giờ, nay chỉ trong chớp mắt một hơi thở đã hoàn thành xong một vòng tuần hoàn!
Luồng chân khí cuồng bạo xé rách kinh mạch, nhưng công năng tự lành thần kỳ của Cửu Dương Thần Công lại lập tức chữa lành và mở rộng kinh mạch ra gấp bội.
Cơn đau đớn kịch liệt khiến Thẩm Lập toát mồ hôi hột, hắn chỉ có thể nghiến chặt răng kiên cường chống đỡ.
Cuối cùng, sau những đợt sóng xung kích dữ dội, chân khí dần dần bình ổn trở lại.
Màu đỏ rực rỡ thu liễm lại thành sắc tím thâm thúy quen thuộc.
Thẩm Lập lúc này mới có thời gian kiểm tra lại tình trạng cơ thể mình.
"Mình... đột phá tới Hậu Thiên cửu trọng rồi sao?"
Thẩm Lập giật mình kinh ngạc, quả thực không dám tin vào mắt mình!"""

ch9_content = """\"Hệ thống, mở bảng điều khiển!\"
Thẩm Lập thầm niệm trong đầu, một bảng giao diện lập tức hiện ra trước mắt hắn:

【Họ tên: Thẩm Lập】
【Tuổi tác: 17 tuổi】
【Nội công: Cửu Dương Thần Công (Cấp Hoàn Mỹ)】
【Cảnh giới: Hậu Thiên cửu trọng】
【Võ học: Thẩm Gia Bí Tịch (Cấp Đại Sư)】
【Khinh công: Chưa có】
【Binh khí: Hàn Tinh Kiếm, Kim Tiền Tiêu】
【Kỹ năng: Du Tường Công, Quy Tức Công, Súc Cốt Công】

Dòng chữ Hậu Thiên cửu trọng sáng rực trên giao diện khiến hắn không giấu nổi niềm vui sướng trào dâng.
Hậu Thiên cửu trọng là khái niệm thế nào?
Đại ca Thẩm Ngọc của hắn ba tuổi cầm kiếm, chín tuổi luyện đao, mười hai tuổi đã theo các đại tiêu cục áp tiêu bôn ba giang hồ.
Mười sáu tuổi đã chém giết hơn hai mươi tên đạo tặc khét tiếng, vang danh với biệt hiệu "Bạch Đoạn Đao".
Trải qua hơn hai mươi năm khổ tu rèn giũa, đến nay Thẩm Ngọc cũng chỉ mới đạt tới Hậu Thiên cửu trọng, thế mà đã được xưng tụng là kỳ tài trăm năm có một của Lăng Yên Cốc.
Toàn bộ giới võ lâm Sóc Châu đều đang ngóng chờ hắn một bước lên mây, tạo dựng thanh danh hiển hách khắp thiên hạ.
Thế nhưng Thẩm Lập hắn hiện tại nào có kém cạnh? Chỉ vỏn vẹn trong mười ngày ngắn ngủi, hắn đã từ một kẻ không có chút nội lực bước thẳng lên cùng một cảnh giới với Thẩm Ngọc!
Cảm nhận nội lực hùng hậu cuộn trào trong kinh mạch, Thẩm Lập tràn đầy tự tin. Ngày tính sổ món nợ cũ đã không còn xa nữa!
Đẩy cửa bước ra ngoài, Thẩm Hương Tuyết đang xách một hộp thức ăn đứng đợi.
Trông thấy Thẩm Lập, nàng vui vẻ chạy ùa tới:
"Công tử, tới giờ dùng bữa rồi ạ!"
Sau mấy ngày ở cạnh nhau, Thẩm Hương Tuyết đã không còn chút phòng bị nào với Thẩm Lập. Nàng hoàn toàn thích ứng với thân phận đệ tử của hắn, mỗi ngày đều ân cần lo liệu cơm nước cho sư phụ.
"Ùng ục~"
Một tiếng kêu bất hòa chợt vang lên từ bụng cô bé, Thẩm Hương Tuyết đỏ bừng mặt cúi gằm đầu xuống.
Thẩm Lập mỉm cười xoa đầu nàng:
"Đã bảo với ngươi bao nhiêu lần rồi, không cần phải đợi ta, hễ đói là cứ ăn trước đi!"
"Dạ..."
"Két~"
Tiếng then cửa khẽ lay động, Thẩm Lập ngẩng đầu lên, thấy mẫu thân Khúc Hiểu Hiểu đang đẩy cửa bước vào viện.
"Mẫu thân, sao người lại tới đây?"
Hắn vui mừng rảo bước đón chào.
Thế nhưng Khúc Hiểu Hiểu dường như chẳng để ý tới lời chào của con trai, ánh mắt bà lập tức dán chặt vào Thẩm Hương Tuyết đứng bên cạnh, hai mắt sáng rỡ:
"Cô bé thanh tú này là ai thế con?"
"À, đây là đệ tử mới thu nhận của con."
Thẩm Lập vỗ trán một cái, vội vàng bảo Hương Tuyết tiến lên chào hỏi.
Thẩm Hương Tuyết lập tức bước tới khẽ cúi người hành lễ vạn phúc, đôi mắt to tròn long lanh chớp chớp:
"Mẫu thân của công tử, cũng chính là mẫu thân của con!"
"Tốt lắm, tốt lắm!" Khúc Hiểu Hiểu cười tươi rói đến mức không khép miệng lại được, nắm lấy tay Hương Tuyết ngắm nghía mãi không thôi.
Khi nghe con trai giới thiệu cô bé đã tu luyện đạt tới Hậu Thiên nhất trọng, nét mặt bà lại càng thêm phần ưng ý tự hào.
Mãi cho đến khi Thẩm Lập giục Hương Tuyết lui về phòng nghỉ ngơi, Khúc Hiểu Hiểu vẫn còn nhìn theo đầy lưu luyến.
Bà dặn dò: "Sau này con nhớ bảo con bé thường xuyên qua chỗ nương trò chuyện nhé!"
Thẩm Lập mỉm cười gật đầu đồng ý.
Thế nhưng khi hắn đưa tay đỡ lấy tay Khúc Hiểu Hiểu định mời bà vào phòng uống trà, vết bầm tím cùng vết roi hằn sâu trên cổ tay bà bỗng đập vào mắt hắn.
Thần sắc Thẩm Lập lập tức biến đổi, hai mắt phun ra lửa giận ngút trời: "Là ai đã làm chuyện này?"
Khúc Hiểu Hiểu chỉ cúi đầu im lặng, khóe mắt tuôn rơi từng dòng nước mắt tủi hờn.
Nhìn thấy cảnh tượng ấy, Thẩm Lập làm sao còn không hiểu được cơ sự.
"Lại là mụ yêu phụ kia đúng không!"
Yêu phụ trong miệng hắn chính là Giang Tuyết – Đại phu nhân tôn quý của Thẩm gia.
"Đừng nói bậy!"
Khúc Hiểu Hiểu hoảng hốt vội lấy tay bịt miệng Thẩm Lập lại, thấp giọng quở trách:
"Đó là đích mẫu của con, con sao có thể ăn nói hàm hồ như thế được!"
Là Đại phu nhân, bà ta nghiễm nhiên là đích mẫu theo quy củ lễ giáo, danh phận cao hơn thân mẫu Khúc Hiểu Hiểu rất nhiều. Nếu sau này cưới vợ sinh con, Thẩm Lập quỳ lạy dâng trà cũng phải là dâng cho Đại phu nhân chứ không tới lượt Khúc Hiểu Hiểu.
Thế nhưng Thẩm Lập nào thèm bận tâm đến những hủ tục phong kiến bất công ấy!
Hắn là Thẩm Lập, nhưng không phải là tên nhị công tử nhu nhược hèn yếu cam chịu bị người ta ức hiếp đẩy xuống vực sâu năm xưa!
Hắn im lặng siết chặt chuôi kiếm, xoay người định đi tìm mụ ta đòi lại công bằng.
Làm người sống trên đời phải có tôn nghiêm.
Nếu trơ mắt nhìn mẫu thân chịu nhục nhã đòn roi mà khoanh tay đứng nhìn, hắn còn mặt mũi nào đứng trong trời đất này!
Khúc Hiểu Hiểu kinh hãi, vội vàng ôm chặt lấy cánh tay con trai, tha thiết van nài:
"Lập nhi, con tuyệt đối không được manh động! Nếu con làm liều, nương sẽ đâm đầu vào cột chết ngay tại đây cho con xem!"
Trước sự can ngăn quyết liệt và những giọt nước mắt nghẹn ngào của mẫu thân, Thẩm Lập đành phải nuốt ngược cơn thịnh nộ vào trong.
Thế nhưng mối hận ngày hôm nay, hắn đã khắc sâu vào tận xương tủy, nhất định sẽ có ngày bắt mụ yêu phụ kia phải trả giá đắt.
Đợi hai người bình tâm trở lại, Khúc Hiểu Hiểu mới nói rõ mục đích đến đây:
"Cái gì? Mẫu thân bảo con đi nghênh đón lão già đó sao?"
Thẩm Lập ngạc nhiên, trong lòng vạn phần không muốn.
"Lão già ấy hễ thấy mặt con là sa sầm nét mặt chửi mắng, con việc gì phải tự vác mặt đến chuốc lấy bực bội?"
Khúc Hiểu Hiểu thở dài: "Xem như là nương cầu xin con đấy. Hôm nay Cốc chủ trở về chuẩn bị đại thọ, con là con trai, nếu không xuất hiện sẽ lại bị người ta đem ra gièm pha chỉ trích."
Nghe mẫu thân nói tới mức đó, Thẩm Lập đành phải làm tròn bổn phận của một người con.

Đến khi ra cổng thành nghênh đón, trời đã ngả về chiều muộn.
Đại ca Thẩm Ngọc dẫn đầu toàn thể đệ tử Lăng Yên Cốc, xếp thành hàng ngũ chỉnh tề bên ngoài thành Phi Nhạn.
Thẩm Lập đứng lặng lẽ ở phía sau đội ngũ.
Đoàn người thắp sáng những chiếc đèn lồng bằng sừng cừu, rọi sáng cả con đường quan đạo như ban ngày.
Dưới ánh đèn lồng, Thẩm Ngọc dáng người cao ráo đĩnh đạc, diện mạo cương nghị, nổi bật giữa đám đông như hạc giữa bầy gà.
Quả là một phong thái thiếu hiệp lỗi lạc, khiến không ít nữ tử đứng xem phải thầm thương trộm nhớ, tấm tắc ngợi khen:
"Thanh danh Bạch Đoạn Đao quả nhiên danh bất hư truyền!"
"Thẩm gia sau bao năm im ắng, xem ra rốt cuộc cũng có hy vọng hưng thịnh trở lại rồi."
"Nhìn khí phách này xem, Thẩm đại lang phong độ tuyệt chẳng kém gì Cốc chủ Thẩm Tòng Giản hai mươi năm trước!"
Trước những lời khen ngợi của mọi người, Thẩm Ngọc vẫn giữ nét mặt điềm đạm, không lộ chút kiêu ngạo nào, càng khiến người ta thêm phần nể phục công phu hàm dưỡng của hắn.
Tuy nhiên, giữa muôn vàn lời tán dương ấy, cũng có không ít lời xì xào khó nghe lọt vào tai. Những lời này không nhắm vào Thẩm Ngọc, mà chĩa thẳng vào bóng dáng có năm phần nét mặt tương đồng đang đứng phía sau:
"Tên hỗn thế ma vương kia sao cũng mặt dày đứng ở đó thế?"
"Hắn không biết xấu hổ sao? Lát nữa anh hùng hào kiệt các châu đều tề tựu cả về đây rồi."
"Thật uổng công sinh ra trong Thẩm gia danh giá, đúng là một tên phế vật vô dụng!"
"Chẳng qua nhờ mẫu thân có chút nhan sắc mới được sống trong nhung lụa, chỉ biết ỷ thế hiếp người chứ có chút bản lĩnh nào đâu."
"So với người anh trai tài giỏi kia, quả đúng là một trời một vực. Chậc chậc, thế mà lại cùng một người cha sinh ra đấy!"
Nghe thấy thế, một gã nhàn hán trong đám đông bèn cười khẩy nói chen vào:
"Bảo hắn hoàn toàn là phế vật thì cũng chưa hẳn đâu nhé!"
Đoạn, gã kể lại đầu đuôi chuyện mấy hôm trước Thẩm Lập một thân một kiếm đến đập nát võ quán cùng tiêu cục để đòi nợ sòng phẳng.
Đám đông nghe xong, tuy chưa thể hoàn toàn thay đổi định kiến, nhưng cũng có cái nhìn khác đi đôi chút. Thậm chí có người lên tiếng công bằng:
"Dám làm dám chịu, có thù tất báo, ân oán phân minh, chí ít cũng ra dáng một đấng nam nhi giang hồ, chưa đến mức làm mất sạch thể diện của Thẩm gia."
Những lời bàn tán dần dần lắng xuống.
"Keng!"
Bỗng một tiếng thanh la vang rền xé toạc không gian.
Mọi người ngẩng đầu nhìn về phía chân trời, chỉ thấy một đoàn kỵ mã đang phi nhanh tới, bụi cuốn mù mịt dưới ráng chiều tà.
Dẫn đầu đoàn người là một lão giả râu tóc hoa râm, khí tức uy nghiêm, chính là Cốc chủ Lăng Yên Cốc – Thẩm Tòng Giản.
Đi cùng Thẩm Tòng Giản còn có không ít gương mặt xa lạ. Cờ hiệu giương cao trên lưng ngựa gồm có Hoàng Hà Bang, Lữ Lương Phái, Đại Giang Hội, Thiết Kỵ Hội...
Thẩm Lập lướt qua ký ức tiền kiếp, chỉ thấy những cái tên này có chút quen thuộc nhưng không để lại ấn tượng sâu sắc nào.
"Rốt cuộc cũng chỉ là những thế lực nhị lưu tầm thường trong võ lâm!" Hắn thầm cảm thán. Nếu là những đại phái đỉnh cấp như Tứ Đại Môn Phiệt hay Thánh Môn Ma Môn, tuyệt đối sẽ không dung nạp thứ thanh thế nửa vời thế này.
Thẩm Tòng Giản vừa tung người xuống ngựa, ánh mắt lập tức nhìn thấy Thẩm Ngọc nổi bật giữa đám đông.
Bỏ qua mọi ánh nhìn xung quanh, lão cười lớn sải bước tới ôm chầm lấy Thẩm Ngọc:
"Hahaha! Hảo nhi lang của ta!"
"""

ch10_content = """Sau khi hai cha con trò chuyện vài câu thân tình, Thẩm Ngọc liền dẫn dắt các sư huynh đệ đồng môn tiến lên thi lễ chào đón phụ thân và các vị chưởng môn tiền bối.
Khách quý nhìn thấy Thẩm Ngọc phong thái đĩnh đạc, ai nấy đều không ngớt lời khen ngợi.
Thẩm Ngọc ngoài mặt không lộ vẻ tự đắc, nhưng Thẩm Tòng Giản đứng bên cạnh thì mặt mày hớn hở, vô cùng nở mày nở mặt.
Đang lúc đắc ý dạt dào, ánh mắt Thẩm Tòng Giản chợt lướt qua đám đông, bất ngờ bắt gặp một gương mặt quen thuộc.
Nụ cười trên môi lão thoáng chốc đông cứng lại.
Đó là đứa con thứ từng bị rơi xuống vách núi, vốn dĩ phải chết từ lâu rồi mới phải.
Một đứa con thứ mà lão luôn xem là nỗi ô nhục của cả gia tộc.
"Nghịch tử này, sao năm đó không chết quách đi cho rảnh nợ?"
Trong đáy mắt lão hiện rõ vẻ chán ghét cùng cực.
Nhưng trước mặt đông đảo quan khách giang hồ, lão không thể nổi trận lôi đình, đành phải đè nén cơn giận dữ xuống đáy lòng.
Thẩm Tòng Giản xoay người, cất cao giọng giới thiệu các nhân vật trọng lượng với Thẩm Ngọc.
Đa phần trong số họ Thẩm Ngọc đều đã từng nghe danh.
Duy chỉ có hai người, khi nghe đến danh tính của họ, Thẩm Ngọc không khỏi giật mình biến sắc.
"Vị này chính là cao nhân của Chân Truyền Đạo, danh hiệu Tử Ngọ Kiếm – Tả Du Tiên, Tả đạo trưởng!"
Chân Truyền Đạo?
Đó là một trong Lục Đạo thuộc Lưỡng Phái Lục Đạo của Thánh Môn lừng danh, là thế lực đỉnh cấp khổng lồ trong cõi Đại Đường!
Thẩm Ngọc vội vàng bước lên cung kính hành lễ, miệng không ngớt lời bái kiến cao nhân.
"Tả Du Tiên?"
Đứng lẫn trong đám đông phía sau, Thẩm Lập nghe thấy cái tên này cũng tò mò ngước mắt nhìn sang.
Thế nhưng vừa nhìn thấy khuôn mặt của kẻ đó, trong lòng hắn lập tức dâng lên một cỗ căm ghét tột cùng.
Nhờ có thần thông Thiên Nhãn Thông, hắn có khả năng nhìn thấu thiện ác nhân quả của một người.
"Kẻ này trên mình sát khí ngập ngụa, nghiệp chướng nặng nề, quả đúng là một tên ác đồ tội ác tày trời!" Thẩm Lập lập tức đưa ra phán đoán.
Hơn nữa, trong ký ức tiền kiếp của hắn, Chân Truyền Đạo này vốn tu luyện tà công tổn hại nhân đạo, làm ra không biết bao nhiêu chuyện thương thiên hại lý.
Thế nhưng cái danh đầu môn phái hiển hách ấy lại khiến toàn thể đệ tử Lăng Yên Cốc cảm thấy vinh hạnh tột cùng, ai nấy đều vui mừng khôn xiết.
Thế nhưng nhân vật tiếp theo còn khiến tất cả mọi người ở đây phấn khích đến phát cuồng.
"Còn vị này chính là quý nhân của Độc Cô gia, Độc Cô Dương tiên sinh!"
Độc Cô Phiệt?
Mọi người nghe xong ai nấy đều thất sắc kinh hoàng, rồi ngay sau đó cả hiện trường như nổ tung trong những tiếng xôn xao kinh ngạc!
"Thẩm Cốc chủ thế mà lại có thể mời được quý nhân của Độc Cô gia tới dự thọ yến, đây là thể diện to lớn cỡ nào chứ?"
"Ngay cả người của Độc Cô Phiệt cũng mời tới được sao!"
Cũng khó trách bọn họ lại kinh ngạc đến mức thất thố như vậy.
Độc Cô Phiệt, Lũng Hữu Lý Phiệt, Tiền Triều Vũ Văn Phiệt, Lĩnh Nam Tống Phiệt.
Bốn đại môn phiệt sừng sững trấn áp thiên hạ suốt hàng trăm năm qua.
Lũng Hữu Lý Phiệt chính là hoàng tộc cai quản giang sơn Đại Đường ngày nay.
Độc Cô Phiệt là thế lực ngang hàng với hoàng tộc, ba cái bang hội cỏn con như Bát Bang Thập Hội thậm chí còn chẳng có tư cách xách giày cho họ.
Một Lăng Yên Cốc bé nhỏ ở đất Sóc Châu này có thể mời được nhân vật của cự đầu như thế hạ cố đến đây, quả thực là chuyện động trời chưa từng có!
Nghe thấy tiếng bàn tán trầm trồ của mọi người xung quanh, Thẩm Tòng Giản càng thêm phần đắc ý, vẻ mặt rạng rỡ như gió xuân tràn trề.
Lão chắp tay cười vang: "Chư vị hiểu lầm rồi! Độc Cô gia chịu nhận lời đến tham dự thọ yến lần này, hoàn toàn không phải vì nể mặt lão phu."
Lão giơ tay chỉ về phía Thẩm Ngọc, giọng điệu ngập tràn niềm kiêu hãnh:
"Quý nhân hạ cố đến đây, thực chất là vì đứa con trai tài giỏi của lão phu!"
"Độc Cô gia nghe danh hiệu Bạch Đoạn Đao của khuyển tử, trong lòng cũng vô cùng thưởng thức."
"Bởi vậy hôm nay mới đặc biệt tới đây để khảo hạch tài năng của nó một phen!"
Lời này tuy nói ra có phần khiêm tốn kín đáo, nhưng ẩn ý bên trong ai ai cũng hiểu. Cái gọi là khảo hạch, một khi vượt qua thì sẽ thế nào?
Chẳng phải là sẽ được bái nhập môn hạ của Độc Cô Phiệt, trở thành đệ tử dòng chính của đại gia tộc đỉnh cấp thiên hạ hay sao?
Tin tức này tựa như một quả lôi đình nổ tung giữa trời quang, khiến đầu óc mọi người choáng váng tê liệt.
"Bạch Đoạn Đao vậy mà lại lọt vào mắt xanh của Độc Cô gia rồi!"
Tin tức tựa như mọc thêm cánh, đoàn người còn chưa kịp trở về cốc thì toàn bộ giới võ lâm Sóc Châu đã rơi vào một cơn cuồng hoan chưa từng có.
Địa đầu xà của Sóc Châu là Lăng Yên Cốc.
Cốc chủ Lăng Yên Cốc do Thẩm gia đời đời thế tập truyền thừa.
Mà Thẩm Ngọc lại là kỳ tài trăm năm có một của Thẩm gia.
Điều này đồng nghĩa với việc võ lâm Sóc Châu sau hơn trăm năm trầm lắng kể từ thời Thẩm tổ, nay rốt cuộc cũng đã có một nhân vật kiệt xuất đủ sức làm rạng danh cả vùng đất này!
Để nghênh tiếp hai vị khách quý hiển hách, Lăng Yên Cốc dốc cạn toàn bộ gia sản tích cóp bao năm qua để bày biện tiệc tùng.
Lụa là gấm vóc khắp thành Sóc Châu bị Lăng Yên Cốc thu mua sạch sẽ, dùng để trải thảm dưới chân, căng làm bình phong che chắn.
Trong cốc nơi nơi giăng đèn kết hoa, rực rỡ huy hoàng.
Heo, bò, dê, gà, vịt bị giết mổ hàng ngàn con mỗi ngày để đãi tiệc.
Bạc trắng chảy ra như nước lũ.
Võ lâm nhân sĩ các châu nghe tin chấn động liền lục tục kéo đến, vô số hào kiệt mang đao vác kiếm nườm nượp đổ về dự yến.
Khách khứa ra vào tấp nập, ngựa xe như nước.
Nhất thời, uy danh của Thẩm gia lại vang dội lẫy lừng chẳng khác nào thời hoàng kim trăm năm về trước.
Đệ tử Lăng Yên Cốc đối với hai vị quý khách thì khúm núm cung kính hết mực.
Thẩm Ngọc lại càng sớm tối thỉnh an, hầu hạ từng li từng tí.
Tả Du Tiên và Độc Cô Dương thản nhiên đón nhận sự cung phụng ấy, bởi lẽ với thân phận cao quý của họ, sự đãi ngộ tâng bốc này vốn dĩ là điều quá đỗi bình thường.

Cứ thế suốt ba ngày trôi qua, cho đến chính nhật của ngày đại thọ.
Hôm nay không khí trong cốc lại càng thêm phần náo nhiệt long trọng.
Ngay giữa ban ngày, pháo hoa đã nổ rền vang không ngớt, tiếng chiêng trống và tiếng pháo đì đẹt suốt từ sáng sớm đến tận trưa.
Tiệc rượu chia thành hai khu nội ngoại rõ rệt.
Khu ngoài dành cho các hiệp khách giang hồ khắp nơi ngồi dự.
Còn khu nội sảnh bên trong là nơi tọa lạc của các vị trưởng bối danh túc và chưởng môn các phái.
Thẩm Tòng Giản thậm chí còn nhún nhường nhường lại vị trí chủ tọa cho hai vị khách quý:
"Hai vị tôn giá, ngày thọ yến cũng là tiệc rượu, trên bàn tiệc khách quý là lớn nhất, xin mời hai vị an tọa ghế trên!"
Bộ dạng cúi đầu nịnh bợ, liếm gót ton hót ấy khiến Thẩm Lập ngồi ở góc khuất bàn cuối nhìn mà phát buồn nôn.
"Một lão già vô liêm sỉ, bỉ ổi như thế này, mà lại là phụ thân của mình sao?"
Hắn cúi gầm mặt xuống, lười nhìn thêm một cái để khỏi bẩn mắt mình.
Thế nhưng hắn không muốn sinh sự, sự việc lại cứ tự tìm đến hắn.
Trên đại sảnh, các đệ tử trẻ tuổi bắt đầu tiến hành diễn võ chúc thọ, lần lượt ra sân múa kiếm so tài.
Đám đệ tử Lăng Yên Cốc đem hết bản lĩnh bú mớm từ thuở nhỏ ra trổ tài, ai nấy đều cố gắng ưỡn ngực xòe đuôi như chim công khoe sắc trước mặt khách quý.
Màn biểu diễn khiến Tả Du Tiên ngồi trên ghế chủ vị bật cười thích thú.
Bỗng nhiên, ánh mắt lão lướt qua góc sảnh, nhìn thấy một thiếu niên đang đứng im lìm ở cuối dãy bàn, hoàn toàn lạc lõng với bầu không khí huyên náo xung quanh.
Thấy tướng mạo của người này có tới năm phần tương đồng với Thẩm Ngọc, Tả Du Tiên tò mò cất tiếng hỏi:
"Người kia là ai vậy, sao không thấy tiến lên diễn kiếm giúp vui?"
Thẩm Tòng Giản nhìn theo hướng ngón tay chỉ của lão, trong mắt lập tức lóe lên tia chán ghét.
Lão vội vàng thoái thác: "Dạ bẩm Tả đạo trưởng, đó là đứa con út bất tài của tại hạ. Lát nữa nó còn phải tham gia lôi đài tỷ võ, nên cứ để nó ngồi nghỉ ngơi dưỡng sức một chút ạ."
Nghe vậy, Tả Du Tiên lại càng thêm phần hứng thú.
Bản lĩnh của Bạch Đoạn Đao Thẩm Ngọc mấy ngày qua lão cũng đã tận mắt chứng kiến, quả thực xứng đáng được Độc Cô gia để mắt tới.
Tả Du Tiên tuy thèm khát nhân tài nhưng cũng không dám tranh giành người với Độc Cô Phiệt.
Nhưng nếu người đệ đệ này của Thẩm Ngọc có tư chất không chênh lệch là bao, nếu lão có thể thu nhận vào môn hạ Chân Truyền Đạo, chẳng phải cũng là một giai thoại đẹp trong chốn giang hồ hay sao?
Nghĩ đến đó, lão liền ngỏ ý muốn Thẩm Lập lên sảnh diễn võ một phen.
Độc Cô Dương ngồi bên cạnh nghe nói Thẩm Ngọc còn có một người đệ đệ, cũng cảm thấy hiếu kỳ, gật đầu đồng ý muốn xem thử.
Thẩm Tòng Giản trong lòng vạn phần không muốn, nhưng trước mặt hai vị khách quý lão đâu dám chối từ.
Lão sa sầm nét mặt quát lớn: "Thẩm Lập! Ngươi cúi gằm đầu ở đó làm cái gì?"
"Mau bước lên đây, cùng các sư huynh đệ biểu diễn một bài kiếm pháp Thẩm gia cho các vị tiền bối giám định!"
Thẩm Lập ngẩng đầu lên, ánh mắt lạnh như băng liếc nhìn ba người trên đài cao.
Hắn cất giọng lạnh nhạt, dứt khoát từ chối:
"Thành thật xin lỗi phụ thân, lát nữa con còn phải lên lôi đài tỷ thí thực chiến, hiện tại không tiện múa may mua vui!"
"Bảo ngươi lên thì ngươi cứ lên!"
Thẩm Tòng Giản nổi cơn tam bành, trừng mắt nhìn đứa con thứ. Tên súc sinh này rõ ràng là đang cố tình làm lão bẽ mặt trước mặt quan khách!
Thế nhưng lần này Thẩm Lập đã quyết tâm, hắn ôm chặt thanh kiếm trước ngực, chậm rãi lắc đầu:
"Đêm qua ngủ không ngon giấc, chân tay bủn rủn, không dám lên bêu xấu trước mặt chư vị anh hùng!"
Bầu không khí trong đại sảnh phút chốc đông cứng lại, lạnh ngắt như tờ.
Sắc mặt Thẩm Tòng Giản tím tái vì tức giận, lão chỉ đành nặn ra nụ cười gượng gạo quay sang tạ lỗi với hai người:
"Nghịch tử ngu muội vô phép vô thiên, để hai vị chê cười rồi."
"Hay là để Thẩm Ngọc lên biểu diễn một bài kiếm pháp tạ tội nhé!"
Độc Cô Dương cười ha hả xua tay, không mấy để tâm: "Cũng được! Đao pháp của Thẩm Ngọc ta đã nghe danh từ lâu, nhưng kiếm pháp Thẩm gia thì quả thực chưa từng được chiêm ngưỡng."
Thế nhưng Tả Du Tiên lại đem chuyện này ghi hận vào tận đáy lòng.
Lão liếc mắt nhìn Thẩm Lập, trong đáy mắt xẹt qua một tia sát cơ u ám.
Kẻ này tính tình vốn ngụy quân tử lại mang bụng dạ hẹp hòi thù dai, ngay khoảnh khắc ấy lão đã thầm hạ quyết tâm, trong mấy ngày thọ yến này nhất định phải tìm cơ hội phế bỏ hoặc diệt khẩu tên tiểu tử dám cả gan công khai làm bẽ mặt lão giữa chốn đông người!"""

batch2_data = {
    "chapters": [
        {
            "chapter_id": 1437,
            "chapter_index": 6,
            "title_translated": "Chương 6: Đa Tình Công Tử Hầu Hi Bạch, Điểm Danh Vạn Hoa Thiên Nhãn Thông",
            "translated_content": ch6_content
        },
        {
            "chapter_id": 1438,
            "chapter_index": 7,
            "title_translated": "Chương 7: Ngũ Đại Đặc Tính Thiên Nhãn Thông, Ngọc Nữ Thiên Kiêu Thẩm Hương Tuyết",
            "translated_content": ch7_content
        },
        {
            "chapter_id": 1439,
            "chapter_index": 8,
            "title_translated": "Chương 8: Kỳ Độc Đại Bổ Xà, Một Đêm Phá Cửu Trùng",
            "translated_content": ch8_content
        },
        {
            "chapter_id": 1440,
            "chapter_index": 9,
            "title_translated": "Chương 9: Yêu Phụ Hại Mẫu, Thiếu Niên Ghi Thù",
            "translated_content": ch9_content
        },
        {
            "chapter_id": 1441,
            "chapter_index": 10,
            "title_translated": "Chương 10: Thọ Yến Bất Phân Thiện Ác, Thẩm Tòng Giản Lão Liếm Cẩu",
            "translated_content": ch10_content
        }
    ]
}

output_path = "data/translated_novel_5_batch2.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(batch2_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path} with {len(batch2_data['chapters'])} chapters.")
