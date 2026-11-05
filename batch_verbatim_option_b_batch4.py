# -*- coding: utf-8 -*-
"""
DỊCH THEO PHƯƠNG ÁN B (VERBATIM 100% NGUYÊN VĂN TỪNG CÂU TỪNG CHỮ)
Tác phẩm: Toàn Cầu Cao Võ (全球高武) - Lão Ưng Cật Tiểu Kê (老鹰吃小鸡)
Lưu toàn văn 100% nguyên bản chữ Hán từ Piaotia vào raw_content.
Bản dịch tiếng Việt văn phong cao võ trau chuốt, đầy đủ từng câu độc thoại, suy nghĩ và hội thoại.
Batch 4: Chương 16 đến Chương 20.
"""

import sqlite3
import datetime
import httpx
from bs4 import BeautifulSoup
import re

NOVEL_ID = 61

def clean_piaotia(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = httpx.get(url, headers=headers, timeout=20.0)
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='gbk')
    
    h1 = soup.find('h1')
    title = h1.get_text().strip() if h1 else ""
    title = re.sub(r'^全球高武\s*', '', title)
    
    for tag in soup(['script', 'style', 'table', 'center', 'ul', 'ol', 'form', 'nav', 'ins', 'span']):
        tag.decompose()
        
    text = soup.get_text()
    text = text.replace('\xa0\xa0\xa0\xa0', '\n\n').replace('\u3000\u3000', '\n\n')
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    filtered = []
    ad_kws = [
        "飘天文学", "返回目录", "上一章", "下一章", "加入书签", "推荐本书", 
        "收藏本书", "选择背景", "fontbig", "书籍介绍", "我的书架", "加入书架", 
        "繁體中文", "重要声明", "阅读更多小说最新章节"
    ]
    for l in lines:
        if len(l) < 150 and any(kw in l for kw in ad_kws):
            continue
        if any(ad in l for ad in ["重要声明：小说“全球高武”", "小说阅读网永久地址", "Copyright ©"]):
            continue
        if l == title or l == f"全球高武 {title}":
            continue
        filtered.append(l)
        
    return title, "\n\n".join(filtered)

CHAPTERS_DATA_VERBATIM = {
    16: {
        "url": "https://www.piaotia.com/html/9/9640/6523770.html",
        "title_vi": "Chương 16: Vương Kim Dương",
        "content_vi": """Ngày 9 tháng 4, Thứ Tư.

Khi Phương Bình tới cổng Trường Số 1 thì Ngô Chí Hào và Lưu Nhược Kỳ đã tới rồi, Dương Kiến vẫn chưa đến.

Bên cạnh hai người còn đứng một người đàn ông trung niên, bên cạnh đỗ một chiếc xe thương vụ bảy chỗ.

Thấy Phương Bình đến, Ngô Chí Hào vội vàng giới thiệu: "Phương Bình, đây là bác Trương của trường, hôm nay bác Trương phụ trách đưa đón chúng mình……"

Người đàn ông trung niên là tài xế do nhà trường sắp xếp, Phương Bình chào hỏi một tiếng, đối phương cũng khách khí gật đầu đáp lại.

Hàn huyên vài câu đơn giản, Ngô Chí Hào liếc nhìn Phương Bình một cái, hơi có chút ngạc nhiên nói: "Phương Bình, tinh thần trạng thái của cậu tốt ghê nhỉ, tớ cứ tưởng cậu cũng giống như tớ, kích động quá buổi tối ngủ không ngon giấc chứ."

Phương Bình hôm nay nhìn qua tinh thần vô cùng sung mãn, ánh mắt dường như còn sáng rực lên.

Phương Bình nghe vậy không khỏi cười nói: "Có sao? Chắc là người gặp chuyện vui tinh thần sảng khoái thôi, hôm nay tớ cũng dậy hơi muộn."

Ngô Chí Hào thấy vậy cũng không để tâm quá nhiều, lại bàn về việc sắp xếp đón người lát nữa.

Lát sau Dương Kiến cũng đến, tên này đêm qua cũng kích động ngủ không ngon, dậy muộn.

Mọi người không lãng phí thời gian, nhanh chóng lên xe hướng về phía ga xe lửa chạy tới.

……

Ga xe lửa Dương Thành.

Để tài xế ở ngoài ga, nhóm người Phương Bình cùng nhau vào trong ga, bắt đầu chờ đợi Vương Kim Dương.

Khoảng cách đến lúc xe lửa đến ga còn một đoạn thời gian, mấy người đứng ở cửa ra ga tán gẫu.

Trò chuyện một lát, Phương Bình chủ động lên tiếng hỏi: "Đám người chúng mình đều đang phấn đấu để trở thành võ giả.

Nhưng đến tận bây giờ, tớ vẫn chưa từng thấy qua một võ giả thực thụ nào.

Gần đây tớ cũng đọc một số tài liệu thi võ khoa, bao gồm cả trước kia lên mạng tra cứu, nhưng đều không nói làm sao để trở thành võ giả thực thụ.

Ngô Chí Hào, phương diện này cậu có hiểu biết gì không?"

Ngô Chí Hào nghe thấy câu này, suy nghĩ một lát mới nói: "Trước kia cậu không quan tâm lắm nên đại khái không hiểu rõ.

Đối với học sinh cấp ba chúng mình mà nói, nhiệm vụ chủ yếu là thi đỗ võ khoa, còn trở thành võ giả là chuyện của thời đại học.

Còn về việc làm sao trở thành võ giả thực thụ, trên mạng chắc chắn không tra được đâu.

Theo tớ được biết, muốn trở thành võ giả, hoặc là trong nhà có tiền bối là võ giả.

Hoặc là phải đến các lớp bồi dưỡng võ đạo……"

Nói đến đây, Ngô Chí Hào bổ sung thêm: "Không phải loại lớp bồi dưỡng võ đạo vớ vẩn ở Dương Thành đâu nhé, mà là lớp bồi dưỡng võ đạo thực thụ có giấy phép hành nghề của nhà nước.

Loại lớp bồi dưỡng này ở Dương Thành căn bản không có, theo luật định, người mở lớp võ đạo ít nhất phải là võ giả trung phẩm.

Đừng nói là Dương Thành, ngay cả toàn bộ tỉnh Nam Giang, những lớp võ đạo như vậy cũng chẳng có bao nhiêu."

"Phương pháp thứ ba, cũng là con đường chủ yếu nhất, chính là thi đỗ vào các trường đại học võ khoa."

Ngô Chí Hào tiếp tục: "Ngoài ba con đường này ra, còn có cách nào khác không thì tớ chịu chết.

Mà ba con đường này đều chẳng liên quan gì đến chúng mình lúc này, ít nhất trước khi thi đỗ đại học võ khoa, chúng mình không có hy vọng trở thành võ giả trước kỳ thi đại học đâu."

Phương Bình khẽ gật đầu, lại hỏi: "Vậy lứa thí sinh thi đại học năm nay, cậu nghĩ có thể xuất hiện bao nhiêu võ giả?"

Ngô Chí Hào còn chưa kịp mở miệng, Dương Kiến đã cười hì hì cướp lời: "Dương Thành thì đừng mơ mộng làm gì, không chỉ Dương Thành, ngay cả thành phố Thụy Dương cấp trên trực thuộc của chúng mình e rằng cũng chẳng có hy vọng có thí sinh nào là võ giả đâu.

Toàn bộ tỉnh Nam Giang năm ngoái trước kỳ thi đại học trở thành võ giả chính thức cũng chỉ có vẻn vẹn ba người, năm nay đại khái cũng chỉ tầm đó thôi.

Những người đó mới là thiên chi kiêu tử thực sự!"

Dương Kiến vẻ mặt đầy ngưỡng mộ, chưa lên đại học đã trở thành võ giả chính thức, chuyện như vậy bọn họ nghĩ cũng chẳng dám nghĩ tới.

Phương Bình còn muốn hỏi thêm vài câu, bỗng nhiên bên cạnh có người tiếp lời cười nói: "Cũng không cần phải tự ti coi thường bản thân như vậy, học sinh cấp ba trở thành võ giả đúng là thiên tài không sai, nhưng vạch xuất phát ban đầu của mọi người là khác nhau."

Lời này vừa thốt ra, mọi người đồng loạt ngẩng đầu nhìn sang.

Người vừa lên tiếng là một thanh niên có tuổi tác sàn sàn tương đương bọn họ, mặc một bộ đồ thường phục thường ngày, hai tay đút trong túi quần.

Nhìn qua không có điểm gì quá mức đặc biệt, tóc cắt cua đầu đinh, tướng mạo bình thường, nhưng đôi mắt lại sáng rực như tuyết.

Thấy mọi người nhìn sang, người thanh niên vừa mở miệng cười hỏi: "Các em là học sinh Trường Số 1 đúng không?"

Ngô Chí Hào vội vàng nói: "Anh là Vương sư huynh ạ?"

Vương Kim Dương mỉm cười lắc đầu: "Đừng dùng kính ngữ, cứ gọi thẳng tên tôi hoặc gọi anh Vương là được, mọi người đều là người cùng lứa tuổi cả, tôi chẳng qua chỉ là người đi trước một bước mà thôi."

Lời này cũng xem như thừa nhận thân phận của mình là Vương Kim Dương, người mà mọi người đang mòn mỏi chờ đợi.

Vương Kim Dương chỉ lớn hơn mọi người một khóa, nếu là mấy người ở lớp chọn năm ngoái thì Ngô Chí Hào thực ra có quen biết.

Nhưng Vương Kim Dương thì cậu ta không quen, chỉ từng nhìn thấy ảnh chụp trên bảng vàng danh dự của trường mà thôi.

Nghe đối phương nói vậy, Ngô Chí Hào thở phào nhẹ nhõm, vội vàng chào: "Chào anh Vương, chúng em là học sinh lớp 12 Trường Số 1……"

Ngô Chí Hào vội vã giới thiệu từng người một, Vương Kim Dương cũng không hề tỏ ra thiếu kiên nhẫn.

Đợi sau khi làm quen với mấy người xong, anh mới tiếp tục chủ đề dang dở ban nãy: "Điều tôi nói xuất phát điểm khác nhau, mọi người chắc hẳn đều hiểu ý tôi là gì.

Những học sinh có thể trở thành võ giả ngay từ thời cấp ba, không một ngoại lệ, đều là những người có gia cảnh vô cùng giàu có vượt trội.

Hoặc là cha mẹ là cường giả võ đạo, hoặc là gia tộc sau lưng có cường giả chống lưng bồi dưỡng.

Cường giả mà tôi nói ở đây ít nhất phải từ Tứ phẩm cảnh trở lên!

Những người xuất thân từ tầng lớp bình dân áo vải như chúng ta, những ai có thể thi đỗ vào võ khoa thì không một ai kém cỏi hơn bọn họ cả.

Thừa nhận thiên phú và thực lực của đối phương, nhưng không cần phải phủ nhận bản thân mình, cũng không cần cảm thấy mình thua kém bất kỳ ai!

Nếu như ngay cả điều này mà các em cũng không làm được, thì con đường tương lai sau này sẽ rất khó khăn để đi tiếp đấy!"

Đây đúng là những lời đúc kết từ kinh nghiệm xương máu quý báu, mọi người vội vàng nói lời cảm ơn.

Phương Bình vẫn luôn quan sát Vương Kim Dương, phát hiện đối phương khá cởi mở dễ gần, tính tình cũng rất tốt, trong lòng bất giác thở phào nhẹ nhõm.

Mọi người vừa rảo bước đi ra ngoài ga, vừa rôm rả trò chuyện.

Vương Kim Dương hỏi thăm tình hình của mấy người một chút, đợi đến khi biết được mấy người này đều có khí huyết từ 110 cal trở lên, không khỏi tán thưởng: "Đúng là khóa sau mạnh hơn khóa trước!

Ngay như năm ngoái khóa của chúng tôi, học sinh đạt 110 cal khí huyết cũng chẳng có mấy người đâu."

Anh chủ động nhắc tới đề tài này, Ngô Chí Hào cũng thuận nước đẩy thuyền hỏi ngay: "Anh Vương, anh thấy năm nay Đại học Võ thuật Nam Giang tuyển sinh thì tiêu chuẩn khí huyết đại khái khoảng bao nhiêu cal ạ?"

Vương Kim Dương mỉm cười, đây có lẽ là câu hỏi mà tất cả thí sinh thi võ khoa lớp 12 đều nóng lòng muốn biết.

Không có gì bất ngờ, năm ngoái bản thân anh há chẳng phải cũng như vậy sao.

Suy nghĩ một chút, Vương Kim Dương cân nhắc nói: "Tiêu chuẩn loại này đều phải căn cứ vào tình hình thực tế của năm đó mà thay đổi.

Năm ngoái mặt bằng khí huyết của mọi người nhìn chung không cao bằng năm nay.

Phía Dương Thành chúng ta thì còn đỡ, chứ bên thành phố Giang Thành thủ phủ tỉnh, trước đó trường trung học trực thuộc Đại học Võ thuật Nam Giang từng làm một đợt kiểm tra đo lường, tôi nghe nói học sinh đạt trên 120 cal có rất nhiều.

Nếu không có gì bất ngờ xảy ra, cửa ải khám thể chất năm nay tiêu chuẩn tối thiểu e rằng cũng phải tầm 110 cal rồi.

Còn để được tuyển chọn trúng tuyển, tốt nhất nên duy trì ở mức từ 115 cal trở lên."

Lời này vừa thốt ra, gương mặt Ngô Chí Hào lộ rõ vẻ vui mừng, trong khi Dương Kiến và Lưu Nhược Kỳ thì sắc mặt có phần ảm đạm đi trông thấy.

Vương Kim Dương cũng không nỡ tiếp tục đả kích mọi người, cười ha hả nói: "Đương nhiên cũng chưa chắc tuyệt đối là như vậy, các em hiện tại đều đã ở mức trên 110 cal rồi, nhân lúc còn chưa tới ngày khám thể chất vẫn còn cơ hội để nâng cao thêm.

Tại sao kỳ thi võ khoa hàng năm lại diễn ra cực kỳ sát nút với kỳ thi tốt nghiệp văn hóa?

Bởi vì mọi người đều đang trong độ tuổi lớn, mỗi ngày đều đang tiến bộ không ngừng, để tạo cho mọi người thêm nhiều cơ hội cạnh tranh công bằng hơn, cho nên thời gian thi võ khoa mới kéo dài đến sát thềm thi đại học mới tiến hành.

Hôm nay em được 110 cal, biết đâu ngày mai đã là 111 cal rồi, điều này hoàn toàn có khả năng xảy ra rất lớn."

Mọi người lại gật đầu, xem như tiếp nhận lời an ủi ấm áp này.

Ra khỏi nhà ga, Vương Kim Dương không vội lên xe, đưa mắt nhìn quanh khung cảnh ngoài bến xe, có chút cảm xúc bùi ngùi: "Thời cấp ba, suy nghĩ duy nhất trong đầu chính là thi đỗ võ khoa, nhất định phải thi đỗ võ khoa!

Vì để thi võ khoa mà đã phải từ bỏ quá nhiều thứ.

Thế nhưng khi thực sự thi đỗ vào võ khoa rồi, hiểu rõ một số chuyện trước kia chưa từng biết tới, bấy giờ mới phát hiện ra rằng, những ngày tháng sống thoải mái vô lo vô nghĩ như thế này đáng quý biết nhường nào!"

Vương Kim Dương mới chỉ là sinh viên năm nhất, chỉ lớn hơn bọn họ một khóa.

Nếu đổi thành sinh viên đại học ở kiếp trước thì chắc chắn sẽ không bao giờ có những cảm khái sâu sắc đến nhường này.

Thế nhưng sinh viên võ khoa ở thế giới này quả thực là thấm thía sâu sắc.

Thời cấp ba phấn đấu vì kỳ thi võ khoa.

Thi đỗ võ khoa rồi lại bắt đầu lao vào phấn đấu để trở thành võ giả.

Trở thành võ giả rồi lại phải tiếp tục phấn đấu để trở nên mạnh mẽ hơn.

Những gia đình giàu có thì còn đỡ khổ một chút, còn những người có gia cảnh bình thường bần hàn như Vương Kim Dương thì những đắng cay cực khổ phải nếm trải vượt xa sức tưởng tượng của người bình thường.

Cảm khái một câu xong, Vương Kim Dương cười nói: "Thôi không ngồi xe nữa, ngồi xe ê ẩm cả người rồi, nếu các em không bận gì thì cùng tôi đi dạo bộ một chút nhé."

Lời này vừa thốt ra, cả đám lập tức mừng rỡ khôn xiết. Bọn họ sở dĩ tranh nhau nhận nhiệm vụ đi đón Vương Kim Dương chẳng phải là để được tiếp xúc nhiều hơn, tìm hiểu thêm nhiều thông tin hữu ích sao.

Vương Kim Dương năm ngoái cũng là học sinh cấp ba, anh thấu hiểu tâm lý của đám đàn em này, cho nên nói như vậy xem như là chiếu cố ưu ái thêm cho bọn họ.

Ngô Chí Hào chạy lon ton lại chỗ xe thương vụ nói với bác tài xế Trương một tiếng, rồi nhanh chóng chạy ngược trở lại.

……

Men theo con đường bên ngoài nhà ga, Vương Kim Dương đi dạo một lát rồi cười nói: "Tìm chỗ nào ngồi một chút đi, đằng nào bên Trường Số 1 chiều mới tới, không vội."

Chuyện này chẳng ai nỡ chối từ, Ngô Chí Hào chủ động dẫn đường đi về phía một quán nước giải khát ở phía trước.

Phương Bình thấy Vương Kim Dương rất dễ gần nói chuyện, bèn nhân cơ hội dò hỏi: "Anh Vương ơi, nếu không phiền thì em có thể hỏi anh một chút được không, hiện tại anh là võ giả mấy phẩm rồi ạ?"

Không có một thí sinh thi võ khoa nào lại không tò mò về điều này cả!

Câu hỏi này vừa thốt ra, ngay cả Ngô Chí Hào đang đi dẫn đường phía trước cũng không nhịn được mà ngoái đầu nhìn chằm chằm vào Vương Kim Dương. Đối với vị học trưởng truyền kỳ này, bọn họ thực sự quá đỗi tò mò hứng thú!

Vương Kim Dương hơi ngẩn người ra một chút, kế đó liền nở nụ cười rạng rỡ nói: "Có một số chuyện, các em không biết thì tốt hơn, biết rồi chưa chắc đã là chuyện tốt lành gì.

Bản thân tôi thì tôi xin phép không nói ra, nếu sau này các em thi đỗ vào Đại học Võ thuật Nam Giang thì tự khắc sẽ biết thôi.

Tuy nhiên tôi có thể kể cho các em nghe một chút chuyện phiếm ngồi lê đôi mách của người khác……"

Trên mặt Vương Kim Dương thoáng hiện vẻ tinh quái trêu chọc: "Lý Nguyên Giang các em có biết không?"

Ngô Chí Hào lập tức đáp: "Biết ạ, năm ngoái anh ấy là học sinh lớp chọn của trường em, cũng thi đỗ vào Đại học Võ thuật Nam Giang."

Vương Kim Dương híp mắt cười nói: "Biết là tốt rồi, buôn chuyện của cái thằng nhóc đó tôi chẳng có chút gánh nặng tâm lý nào cả.

Thằng nhãi đó đừng có trách tôi làm nó mất mặt trước mặt đàn em khóa dưới nhé, hồi xưa trong đám học sinh lớp chọn chính nó là đứa ngạo mạn nhất trần đời.

Cùng là học sinh với nhau cả, không có việc gì tự nhiên cứ thích buông lời châm chọc mỉa mai tôi vài câu, các em nói xem có phải rảnh rỗi quá hóa rồ không chứ?

Đến lúc hai đứa cùng thi đỗ vào Đại học Võ thuật Nam Giang, cái tên đó còn dám bảo cùng học Nam Giang Võ Đại với tôi là một sự sỉ nhục mất mặt, mẹ kiếp, loại người đó đúng là ngứa đòn thiếu dạy dỗ!"

Những lời bộc bạch thẳng thắn này của Vương Kim Dương khiến đám người Ngô Chí Hào nghe xong mà trố mắt nghẹn họng. Vị học trưởng nhìn bề ngoài nho nhã ôn hòa ban nãy, giờ xem ra cũng chẳng hề hiền lành dịu dàng như bọn họ tưởng tượng.

Vương Kim Dương cũng chẳng buồn bận tâm xem bọn họ nghĩ gì, trên mặt lại nở nụ cười trêu ngươi: "Lý Nguyên Giang nhập học cùng lúc với tôi, bây giờ năm nhất sắp kết thúc rồi mà cái tên đó đến giờ vẫn chưa trở thành võ giả đâu.

Hơn nữa nhìn tình hình này, năm hai liệu có thành được không còn khó nói lắm, chắc phải đợi đến năm ba thì may ra mới có cửa."

Ý tứ sâu xa trong câu nói này, Phương Bình vừa nghe là hiểu ngay tắp lự: Vương Kim Dương hiện tại chắc chắn đã là một võ giả hàng thật giá thật rồi!

Còn về phẩm cấp cụ thể, Phương Bình thậm chí còn ngấm ngầm hoài nghi: Có khi không đơn thuần chỉ là Nhất phẩm đâu, nếu không anh ta việc gì phải giấu giếm không chịu nói ra.

Lại đem so sánh đối chiếu với một Lý Nguyên Giang xuất thân từ lớp chọn cùng thi đỗ vào Nam Giang Võ Đại, có thể thấy Vương Kim Dương cho dù đặt vào trong Đại học Võ thuật Nam Giang thì thành tích chắc chắn cũng thuộc hàng xuất sắc không hề tầm thường.

Trong chốc lát, ngay cả Phương Bình cũng dấy lên sự hứng thú không nhỏ đối với vị học trưởng truyền kỳ này…… đương nhiên, không phải loại hứng thú lệch lạc kia."""
    },
    17: {
        "url": "https://www.piaotia.com/html/9/9640/6523771.html",
        "title_vi": "Chương 17: Vô Tri Là Phúc",
        "content_vi": """Trong lúc Vương Kim Dương nói chuyện, mọi người đã bước chân vào quán nước giải khát.

Ngô Chí Hào đi tới quầy gọi đồ uống, chẳng có ai tranh giành thanh toán, dù sao tiền này nhà trường cũng sẽ thanh toán hóa đơn công tác phí.

Những người khác thì tìm một góc tương đối vắng người ngồi xuống, tiếp tục chăm chú lắng nghe Vương Kim Dương trò chuyện.

"Mấy chuyện võ giả này đối với các em hiện tại còn hơi xa vời, vào thời điểm này, nói nhiều cũng vô ích, mấu chốt vẫn là phải thi đỗ võ khoa đã."

"Võ khoa tuy xưng là qua năm ải chém sáu tướng, nhưng trên thực tế cũng không đến mức đáng sợ như vậy.

Trong năm cửa ải, cửa ải thẩm tra chính trị thì không cần phải bàn, còn thi môn chuyên nghiệp và thi văn hóa thì hoàn toàn phụ thuộc vào mức độ dụng công chăm chỉ của chính các em.

Mấu chốt sinh tử chỉ nằm ở hai cửa ải: Khám thể chất và Kiểm tra thực tế (Thực trắc) mà thôi!"

Ngô Chí Hào vừa bưng đồ uống quay trở lại bàn nghe vậy liền phụ họa ngay: "Anh Vương nói hoàn toàn chính xác, hai cửa ải này chính là hai cửa ải có tỷ lệ đào thải tàn khốc nhất hàng năm."

Vương Kim Dương mỉm cười nói: "Khí huyết của các em đều ở mức trên 110 cal cả rồi, việc vượt qua điểm sàn khám thể chất không khó, cái khó là làm sao vượt qua được điểm chuẩn trúng tuyển của trường?

Thực ra đối với các em lúc này, chênh lệch khí huyết giữa người với người không quá lớn.

Trước kỳ thi chuẩn bị một viên thuốc tốt một chút, ví dụ như Khí Huyết Đan, là đã có thể thay đổi vận mệnh của rất nhiều người rồi.

Đương nhiên, nếu như Khí Huyết Đan vẫn chưa đủ chắc chắn, vậy thì tôi có thể truyền thụ cho các em một mẹo nhỏ……"

Đối với Vương Kim Dương thì đây chỉ là mẹo vặt nhỏ nhoi, nhưng đối với đám người Ngô Chí Hào, lời chỉ điểm từ một võ giả thực thụ — cho dù thực sự chỉ là mẹo vặt đi chăng nữa — thì đối với bọn họ cũng có giá trị quý như vàng ròng.

Sắc mặt mấy người ai nấy đều kích động đỏ bừng, không ai dám hó hé nửa lời, đồng loạt vểnh tai lên lắng nghe từng câu từng chữ.

"Sự bộc phát của khí huyết không đơn thuần chỉ là vấn đề lượng máu trong cơ thể, mà nó còn liên quan mật thiết tới trạng thái.

Trạng thái thân thể, trạng thái tinh khí thần, và trạng thái cảm xúc.

Trước khi bước vào phòng khám thể chất, chỉ cần làm một vài động tác khởi động làm nóng người nhẹ nhàng là được, tuyệt đối không được vận động quá sức làm hao tổn thân thể, phải giữ cho tinh khí thần luôn ở trạng thái no đủ sung mãn nhất, đừng dại dột nghĩ tới chuyện tập luyện tăng cường vào ngày cuối cùng.

Còn về phương diện cảm xúc, học được cách điều động cảm xúc để đạt tới mức tối đa là một việc vô cùng khó khăn.

Hỷ nộ ái ố, khi những cảm xúc này đạt tới cực hạn sẽ khiến cho khí huyết trong người các em sôi sục cuộn trào lên, kết quả đo kiểm tra khí huyết thông thường sẽ cao hơn mức bình thường một chút.

Thế nhưng các em tuổi đời còn quá trẻ, chưa từng trải qua nhiều biến cố sóng gió cuộc đời, muốn điều động những cảm xúc này chạm tới đỉnh cao tột cùng là việc cực kỳ khó!"

"Điều động cảm xúc ư?"

Thấy mấy cô cậu học trò rơi vào trạng thái trầm ngâm suy tư, Vương Kim Dương bỗng nhiên bật cười nói: "Thực ra, tôi có một cách cực kỳ hiệu quả để giúp các em đẩy cảm xúc lên tới đỉnh điểm cao nhất!"

Mặt mày mọi người lập tức hớn hở mừng rỡ. Riêng Phương Bình thì lại dùng ánh mắt đầy vẻ hồ nghi liếc nhìn Vương Kim Dương một cái. Thực ra chuyện này hắn chẳng mấy bận tâm, đằng nào hắn cũng có thể nhanh chóng nâng cao điểm khí huyết thông qua hệ thống.

Vương Kim Dương lúc nói câu này, nét mặt và nụ cười chẳng khác gì vẻ mặt lúc trêu chọc bêu rếu Lý Nguyên Giang ban nãy, Phương Bình linh cảm thấy đây tuyệt đối chẳng phải là chuyện tốt lành gì.

Quả nhiên, Vương Kim Dương híp mắt cười tủm tỉm nói: "Có một số loại cảm xúc rất khó điều động, nhưng chữ 'Nộ' (tức giận) thì lại vô cùng đơn giản dễ làm.

Bây giờ, tôi giẫm đạp lên mặt từng đứa các em, nhổ thêm vài bãi nước bọt vào mặt, đợi đến khi các em bước vào phòng khám thể chất, cứ việc nhớ lại nỗi nhục nhã ê chề mà mình vừa phải chịu đựng……"

"Khụ khụ khụ!"

Ngô Chí Hào và mấy người suýt chút nữa thì sặc nước ngọt nghẹn chết tại chỗ! Vị học trưởng truyền kỳ này, sao càng lúc càng cảm thấy phong cách làm việc chẳng đáng tin cậy chút nào thế này?

"Hahaha……"

Vương Kim Dương cười phá lên sảng khoái, cười một hồi lâu mới thong thả nói tiếp: "Mặc dù tôi chỉ nói đùa vậy thôi, nhưng các em quả thực có thể thử áp dụng xem sao.

Hỷ, ái, lạc những cảm xúc đó rất khó chạm tới cực hạn, duy chỉ có cơn giận dữ phẫn nộ là dễ đạt tới nhất. Dưới cơn thịnh nộ bốc hỏa ngút trời, khí huyết bộc phát tăng thêm được một hai cal là chuyện hoàn toàn không có gì bất ngờ."

Lời nói đùa này của Vương Kim Dương, đám người Ngô Chí Hào thế mà lại thực sự khắc cốt ghi tâm, coi như một bí kíp nghiêm túc trong lòng.

Nếu như thực sự có thể tăng thêm được một hai cal quý giá, vậy thì…… bị giẫm đạp lên mặt hình như cũng đâu phải là chuyện không thể chấp nhận được?

Nhìn thấy vẻ mặt rục rịch động tâm của mấy tên này, Phương Bình bất giác rùng mình ớn lạnh cả sống lưng. Mấy cái thằng nhóc này, không lẽ thật sự có sở thích khổ dâm thích tìm người ngược đãi đấy chứ?

Mà nói đi cũng phải nói lại, khả năng bọn chúng dám làm chuyện này lên tới chín mươi chín phần trăm!

Vì để thi đỗ vào võ khoa, chịu chút nhục nhã thể xác thì có là cái thá gì đâu.

Vương Kim Dương cũng chẳng buồn quan tâm xem bọn họ có thực sự thử nghiệm trò này hay không, lại tiếp tục giảng giải: "Vượt qua được cửa ải thể kiểm rồi, thì cửa ải thực trắc phía sau cũng không quá mức khó khăn.

Chẳng qua cũng chỉ là sát hạch trên mấy phương diện: Lực bộc phát, sức bền dẻo dai và độ linh hoạt của cơ thể mà thôi.

Những yếu tố này đều có mối quan hệ vô cùng mật thiết với khí huyết, khí huyết càng cao thì xác suất vượt qua cửa ải càng lớn.

Đương nhiên, cũng không loại trừ trường hợp một số kẻ phế vật từ nhỏ đã ngâm mình lớn lên trong hũ thuốc bổ, chỉ có mỗi cái vỏ khí huyết rỗng tuếch bên ngoài, còn những phương diện khác thì dốt nát kém cỏi, loại người đó bị loại thẳng tay là đáng đời.

Ngay trước mặt ném cho một con gà sống mà còn không có gan đập chết nổi, thì sau này còn mơ tưởng đập chết ai?

Giết người, so với giết gà khó hơn gấp vạn lần……"

"Giết người ư?"

Ánh mắt Phương Bình khẽ ngưng tụ lại thành một điểm. Vương Kim Dương lúc thốt ra hai chữ "giết người", cảm xúc trên mặt hoàn toàn không hề có chút gợn sóng dao động nào, giọng điệu thản nhiên giống hệt như anh ta thực sự đã từng tự tay giết người rồi vậy.

Thế nhưng trong thời đại pháp quyền văn minh này, ngay cả võ giả cũng phải chịu sự ước thúc nghiêm ngặt của luật pháp, làm sao có cơ hội tùy tiện giết người được chứ?

Huống chi đối phương mới chỉ là một cậu sinh viên năm nhất đại học……

Dường như nhận ra được ánh mắt dò xét chăm chú của Phương Bình, Vương Kim Dương nở một nụ cười nhàn nhạt: "Có một số chuyện, đến lúc đó tự khắc các em sẽ hiểu ra thôi.

Đương nhiên, tiền đề là các em phải thi đỗ vào võ khoa, phải trở thành võ giả thực thụ cái đã.

Người người đều điên cuồng theo đuổi võ đạo, ai ai cũng khao khát trở thành võ giả, thế nhưng người bình thường, lại có được mấy ai thực sự hiểu rõ hai chữ 'Võ Giả' rốt cuộc mang ý nghĩa nặng nề đến nhường nào?

Những năm gần đây, không ít người bình thường tỏ ra bất mãn oán thán: Tại sao xã hội lại quá mức thiên vị ưu ái võ giả đến như vậy?

Cường giả mở công ty doanh nghiệp thì được giảm thuế, thậm chí được miễn thuế hoàn toàn.

Cường giả ra làm quan chức chính quyền, dẫu cho năng lực xử lý chính vụ có kém cỏi một chút thì cũng chẳng ảnh hưởng gì lớn.

Cường giả nắm giữ vô số đặc quyền trong tay, đặc quyền nhiều đến mức khiến cho vô số người phải đỏ mắt ghen ghét bất bình.

Thế nhưng thì đã sao nào!

Thế giới này, có bỏ công sức hy sinh thì mới có hồi báo, bất kỳ thứ gì trên đời này cũng không bao giờ có chuyện tự nhiên từ trên trời rơi xuống.

Bọn họ cảm thấy không cam lòng, cảm thấy xã hội bất công, nhưng đâu ai biết rằng, bản thân những cường giả kia cũng cảm thấy thế giới này đầy rẫy sự bất công!"

Vương Kim Dương nói đến đây bỗng nhiên dừng bặt lại, trên mặt lại khôi phục lại nụ cười thoải mái ban đầu, cười nói: "Nói hơi nhiều rồi, có dịp quay trở về Dương Thành một chuyến bỗng thấy mình nhiều tâm sự cảm khái quá."

Đám người Ngô Chí Hào cũng không quá để tâm tới những lời này, rốt cuộc việc võ giả được hưởng đặc quyền trong mắt bọn họ từ lâu đã là chuyện hiển nhiên lẽ thường tình rồi.

Thế nhưng Phương Bình thì lại đặc biệt để tâm ghi nhớ sâu sắc trong lòng. Trước đây hắn thực ra cũng từng có chút thắc mắc hoài nghi: Võ giả cho dù có năng lực lấy một địch một trăm đi chăng nữa, nhưng người bình thường đông đảo như vậy, việc gì xã hội phải tâng bốc sùng bái võ giả đến mức độ cuồng nhiệt như thế?

Trong thời đại đã có vũ khí nóng hiện đại, một người bình thường không làm gì được, nhưng cả trăm người, cả ngàn người, ai nấy đều cầm súng đạn xả vào, Tông sư liệu có né tránh nổi làn mưa đạn hay không?

Bây giờ nghe Vương Kim Dương bóng gió nói như vậy, dường như đằng sau thế giới này còn ẩn chứa những bí mật nội tình kinh thiên động địa nào đó mà người ngoài không hề hay biết.

Đáng tiếc, Vương Kim Dương không muốn nói sâu thêm, Phương Bình cũng không tiện gặng hỏi tiếp, những chuyện cơ mật này xem ra chỉ đành đợi đến khi chính mình trở thành võ giả thì mới có tư cách để tìm hiểu rõ ràng.

Mấy người đang ngồi trò chuyện rôm rả thì chiếc điện thoại di động trong túi quần Vương Kim Dương bỗng nhiên đổ chuông reo vang.

Bấm nút nghe máy, Vương Kim Dương cũng không hề né tránh mọi người, cất tiếng trao đổi ngắn gọn vài câu, cuối cùng mới trầm giọng đáp: "Buổi chiều tôi phải qua Trường Số 1 một chuyến, tối tôi sẽ trực tiếp qua chỗ các ông."

Nói xong, Vương Kim Dương liền dứt khoát cúp máy, cũng không giải thích gì thêm với mấy đứa học sinh.

Mọi người cũng không dám tò mò hỏi han nhiều, ngồi tán gẫu thêm một lát rồi cả nhóm cùng nhau rời khỏi quán nước.

Theo như kế hoạch ban đầu của nhà trường, buổi trưa mấy đứa bọn họ sẽ tháp tùng mời cơm Vương Kim Dương, thế nhưng Vương Kim Dương vốn dĩ là người gốc Dương Thành, nhà ở ngay tại đây, cho nên bước ra khỏi quán nước anh liền quyết định muốn về nhà trước.

Phương Bình và mấy người bạn cũng không tiện lẽo đẽo đi theo làm phiền, bèn hẹn đúng giờ chiều nay sẽ tới đón người, như vậy là nhiệm vụ đón tiếp buổi sáng coi như hoàn thành êm đẹp.

……

Vương Kim Dương vừa rời đi, trên gương mặt Ngô Chí Hào lập tức ngập tràn vẻ phấn khởi đắc ý: "Thu hoạch lớn thật đấy!"

Chưa bàn tới những chuyện khác, chỉ riêng cái mẹo điều động cảm xúc phẫn nộ kia thôi, trước đây bọn họ căn bản chưa từng nghe ai nhắc tới bao giờ.

Còn về các bài kiểm tra thực trắc, Vương Kim Dương cũng đã tận tình chỉ điểm cho mấy người một số tiểu xảo vận động quý báu. Ngô Chí Hào vốn dĩ đã có hy vọng lớn thi đỗ võ khoa, giờ phút này lại càng thêm phần nắm chắc mười mươi.

Ngay cả Dương Kiến và Lưu Nhược Kỳ cũng cảm thấy mình thu hoạch được quá nhiều điều bổ ích, hoàn toàn có thể mạnh dạn thử sức dốc toàn lực xung kích vào Đại học Võ thuật Nam Giang một phen.

Ngoài ra, Vương Kim Dương còn vô tình tiết lộ một thông tin chấn động: Trương Tổng Đốc của tỉnh Nam Giang quả thực đang bế quan xung kích vào cảnh giới Tông sư Thất phẩm!

Sở dĩ anh tiết lộ điều này là vì muốn khuyên nhủ mọi người năm nay nên ưu tiên nộp hồ sơ thi vào Đại học Võ thuật Nam Giang.

Trương Tổng Đốc vốn xuất thân tốt nghiệp từ Nam Giang Võ Đại, mà Nam Giang Võ Đại lại là trường đại học chuyên biệt về võ thuật duy nhất của toàn tỉnh Nam Giang. Tuy rằng trong tỉnh vẫn còn hai trường đại học khác tuyển sinh song song cả văn lẫn võ, danh tiếng thậm chí không hề thua kém Nam Giang Võ Đại.

Thế nhưng Trương Tổng Đốc là cựu sinh viên của Nam Giang Võ Đại, một khi năm nay ngài ấy đột phá thành công lên cảnh giới Tông sư, chắc chắn sẽ dốc sức tranh thủ thêm nhiều nguồn tài nguyên võ đạo khổng lồ từ trung ương về cho trường cũ của mình.

Đến lúc đó, những ai bước chân vào Nam Giang Võ Đại chắc chắn sẽ được hưởng trọn vẹn sự nghiêng về tài nguyên tu luyện của toàn tỉnh.

Điểm này Vương Kim Dương vô cùng quả quyết và chắc chắn.

Chính vì vậy, vào lúc này, mục tiêu phấn đấu của mấy cô cậu học trò đều đồng loạt hướng trọn vẹn về phía Đại học Võ thuật Nam Giang.

Vương Kim Dương đã đi rồi, mấy người hẹn nhau giờ giấc chiều nay cùng đi đón người, kế đó liền ai về nhà nấy, đường ai nấy đi.

……

Ở một hướng khác.

Vương Kim Dương đang rảo bước chuẩn bị về nhà thì chiếc điện thoại trong túi lại một lần nữa rung chuông inh ỏi.

Rút điện thoại ra liếc nhìn màn hình một cái, Vương Kim Dương khẽ nhíu mày, bấm nút nhận cuộc gọi: "Chẳng phải đã bảo tối nay tôi mới qua sao? Lại có chuyện gì nữa à?"

Đầu dây bên kia lập tức truyền đến giọng nói trung niên vô cùng cung kính khép nép: "Thưa Vương tiên sinh, vô cùng xin lỗi vì đã làm phiền ngài vào lúc này. Thế nhưng vừa có tin mật báo gửi về: Nghi phạm đã trốn vào trong dãy núi Thương Sơn rồi ạ! Thương Sơn kéo dài vắt ngang qua ranh giới của hai tỉnh, một khi để cho hắn ta trốn thoát sang tỉnh bạn thì……"

Vương Kim Dương nhíu chặt đôi lông mày, giọng điệu lộ rõ vẻ bất mãn: "Trước đó chẳng phải đã giao kèo rõ ràng là đối phương vẫn ở yên tại chỗ, đợi tôi tới nơi rồi mới cùng hành động sao?

Bây giờ người đã bỏ trốn rồi, không phải là do bên các ông đánh rắn động cỏ đấy chứ?"

Đầu dây bên kia im lặng một hồi lâu không dám thanh minh, hiển nhiên là đã bị Vương Kim Dương đoán trúng phóc tim đen.

Vương Kim Dương trong lòng vô cùng bực bội, khẽ thở hắt ra một ngụm khí lạnh, một lát sau mới lạnh lùng cất giọng: "Ban đầu thỏa thuận giá 30 vạn tệ, bây giờ phải nâng lên 50 vạn tệ! Bất kể sống hay chết! Lát nữa cử người mang toàn bộ hồ sơ tư liệu của hắn tới nhà tôi, những chuyện khác không cần các ông phải bận tâm nhúng tay vào nữa!"

"Vương tiên sinh, 50 vạn tệ liệu có phải là hơi quá……"

"Vậy thì để đích thân Cục trưởng của các ông tự mình vác xác đi mà bắt người! Ông ta chẳng phải cũng là sinh viên tốt nghiệp Nam Giang Võ Đại sao?

Tốt nghiệp đã được hai mươi năm trời rồi, dừng chân ở cảnh giới Nhị phẩm võ giả, giờ còn có gan ra tay đánh nhau được nữa không?

Đúng 50 vạn tệ! Không đồng ý thì các ông đi mà tìm người khác!"

Vương Kim Dương nói năng vô cùng gay gắt không nể nang chút thể diện nào, hừ lạnh một tiếng rồi bồi thêm: "Hoặc là các ông đi mà nhờ vả bên Thụy Dương, hay cầu cứu lên tận cấp tỉnh đi! Nếu không phải do đợt này tôi sắp sửa đột phá cần tiêu tốn một lượng tài nguyên khổng lồ, lại tiện đường nhà ở ngay Dương Thành thì cái nhiệm vụ rách việc này tôi thèm vào mà nhận!"

Người ở đầu dây bên kia ngập ngừng do dự một lát, cuối cùng đành cắn răng chấp thuận: "Được rồi, điều kiện này chúng tôi đồng ý! Thế nhưng người bắt buộc phải bắt quy án, ngoài ra…… chiến công bắt giữ phải được ghi nhận là do phía Dương Thành độc lập hoàn thành nhiệm vụ truy bắt!"

Vương Kim Dương nhàn nhạt đáp: "Dĩ nhiên rồi, nhận tiền của người thì thay người tiêu tai trừ họa, lần này tôi về Dương Thành thuần túy chỉ là để chỉ điểm kỳ thi võ khoa cho các đàn em khóa dưới ở Trường Số 1 mà thôi."

"Vâng vâng, tài liệu chúng tôi sẽ lập tức cho người mang tới tận nhà ngài, chỉ mong ngài nhanh chóng ra tay giải quyết êm xuôi."

"Cứ yên tâm."

"……"

Trao đổi thêm vài câu ngắn gọn, Vương Kim Dương liền dứt khoát ngắt máy, đưa tay lên xoa xoa hai bên thái dương, khẽ thở dài một tiếng: "Hy vọng thằng nhãi đó chưa chạy quá xa, nếu không thì lấy đâu ra nhiều kẻ ngu ngốc sẵn sàng chi tiền béo bở như thế này nữa chứ."

Nghĩ tới lượng tài nguyên tu luyện khổng lồ cần thiết cho đợt đột phá cảnh giới sắp tới, Vương Kim Dương đầu cũng to như cái đấu.

Nhà trường hỗ trợ cung cấp một nửa, nửa còn lại bắt buộc bản thân anh phải tự mình bươn chải gom góp. Nếu đổi thành những sinh viên có gia cảnh giàu có sung túc thì lấy đâu ra cảnh phải vất vả tính toán từng li từng tí như thế này.

Thế nhưng đối với một kẻ xuất thân bình dân như anh, tất cả chỉ có thể dựa vào chính đôi bàn tay và nắm đấm của bản thân mà thôi.

Nghĩ lại mấy đứa học sinh Trường Số 1 ban nãy, Vương Kim Dương khẽ lắc đầu ngao ngán: Người người ai nấy đều khao khát trở thành võ giả, nhưng nào có ai thấu hiểu được nỗi cay đắng trăm bề của võ giả đâu.

Mấy đứa nhóc đó, ngay cả Ngô Chí Hào, trong mắt anh gia cảnh cũng chỉ thuộc hàng bình thường mà thôi.

Đợi đến khi thực sự bước chân vào đại học võ thuật rồi, đám nhóc đó e rằng mới thấm thía thế nào là sự tuyệt vọng tột cùng.

Lý Nguyên Giang mãi mà không thể đột phá trở thành võ giả, đâu phải là do vấn đề thiên phú của cậu ta kém cỏi đâu.

"Hừ hừ!"

Khẽ cười khẩy một tiếng, cũng chẳng rõ là đang cười nhạo ai hay là đang tự cười giễu chính bản thân mình.

Vương Kim Dương hai tay đút túi quần, thong thả cất từng bước chân chậm rãi đi về phía khu dân cư của gia đình mình.

Đôi khi, sống trong sự vô tri thực sự là một điều vô cùng hạnh phúc."""
    },
    18: {
        "url": "https://www.piaotia.com/html/9/9640/6523772.html",
        "title_vi": "Chương 18: Uống Thuốc Rồi À?",
        "content_vi": """Chia tay nhóm người Ngô Chí Hào, buổi sáng không phải lên lớp học.

Thấy thời gian vẫn còn khá sớm, Phương Bình cũng chẳng có tâm trí đâu mà quay trở lại trường, hắn thong thả rảo bước đi về phía khu dân cư Cảnh Hồ Viên.

Vừa đi từng bước chậm rãi, trong đầu Phương Bình vừa không ngừng suy ngẫm về những lời nói của Vương Kim Dương ban nãy.

Mấy cái mẹo vặt mà đám người Ngô Chí Hào quan tâm sốt sắng, Phương Bình tuy cũng lắng nghe đầy đủ, nhưng thực chất không quá để tâm trong lòng, điều cốt lõi khiến hắn bận tâm lại là những thứ ẩn sâu đằng sau câu chuyện.

Vương Kim Dương chẳng qua cũng chỉ là một cậu sinh viên năm nhất đại học mà thôi, thế nhưng rõ ràng phong thái và suy nghĩ trưởng thành hơn hẳn đám học sinh lớp 12 rất nhiều.

Từ những lời nói vô tình buông ra của anh ta có thể nhận thấy: Giới võ giả có lẽ hoàn toàn không hề tốt đẹp lung linh như người ngoài vẫn hằng tưởng tượng.

Trong xã hội hiện đại ngày nay, võ giả nhìn bề ngoài dường như hòa lẫn chung sống cùng người bình thường, nhưng trên thực tế chưa chắc đã là như vậy, họ có thế giới riêng biệt của họ, có rất nhiều bí mật đen tối mà người bình thường căn bản cả đời cũng không bao giờ có cơ hội được tiếp cận hay hiểu rõ.

Hiện nay tuy rằng thông tin trên mạng internet lan truyền vô cùng nhanh chóng, nhưng đừng bao giờ quên rằng: Ở quốc gia này, mạng lưới internet dẫu có nới lỏng đến đâu thì cũng là do chính phủ cho phép nó được nới lỏng mà thôi.

Những thông tin cơ mật nào mà chính quyền không mong muốn người bình thường biết tới, thì tuyệt đối vĩnh viễn không bao giờ có thể xuất hiện trên mạng xã hội.

"Võ giả……"

Phương Bình khẽ lẩm bẩm trong miệng: "Võ giả rốt cuộc có sự chênh lệch lớn đến nhường nào so với người bình thường? Chẳng lẽ thuần túy chỉ là sự chênh lệch về mặt vũ lực thôi sao?"

Mấy ngày trước đây, Phương Bình bận rộn đến mức không có thời gian để tĩnh tâm suy xét về những điều này.

Thế nhưng lần này sau khi được tiếp xúc trực tiếp với một võ giả thực thụ bằng xương bằng thịt như Vương Kim Dương, Phương Bình bất giác suy nghĩ sâu xa hơn rất nhiều.

"Tầng thứ vị thế của mình rốt cuộc vẫn còn quá thấp bé……"

Phương Bình khẽ lắc đầu, sự khác biệt về địa vị xã hội dẫn tới việc nguồn tin tức mà hắn có thể nắm bắt được là quá đỗi ít ỏi nghèo nàn.

Có những thứ đúng như lời Vương Kim Dương đã nói: Đôi khi không biết còn tốt hơn là biết quá sớm.

Đợi đến khi bản thân hắn chính thức trở thành võ giả rồi, những điều thắc mắc bí ẩn này tự khắc sẽ dần dần được mở ra, cũng không cần thiết phải nóng vội nhất thời làm gì.

Đi bộ được một đoạn đường, Phương Bình lại suy tính một hồi, quyết định dứt khoát đem nốt 10.000 điểm tài phú còn lại trên hệ thống ra để chuyển hóa thành khí huyết.

Năm nay rõ ràng mức độ cạnh tranh khốc liệt và khó khăn hơn năm ngoái rất nhiều. Ngô Chí Hào khí huyết đã đạt tới 115 cal, lại chuẩn bị sẵn Khí Huyết Đan đắt đỏ, lại học được cả kỹ năng bộc phát cảm xúc giận dữ, thế mà dẫu có như vậy bản thân cậu ta vẫn chưa dám vỗ ngực khẳng định có chắc suất trúng tuyển hay không.

Từ đó có thể thấy rõ ràng áp lực cạnh tranh của kỳ thi năm nay sẽ khủng khiếp đến mức độ nào.

Bản thân mình hiện tại mới chỉ lẹt đẹt ở mức 110 cal khí huyết, nếu như không nhanh chóng nâng cấp lên, lỡ như cái hệ thống dở dở ương ương không đáng tin cậy này đột nhiên dở chứng gặp trục trặc thì đúng là tai họa ngập đầu.

Sau khi đã hạ quyết tâm chắc chắn, Phương Bình liền tập trung cao độ tinh thần, trong đầu bắt đầu suy nghĩ mãnh liệt về việc thăng cấp cho khí huyết.

Rất nhanh sau đó, dãy số liệu hiển thị trong tầm mắt hắn liền xuất hiện sự biến đổi:

Tài phú: 0

Khí huyết: 1.2

Tinh thần: 1.1

……

Đúng lúc Phương Bình đang chuẩn bị sẵn sàng tâm lý để đón nhận cảm giác sung sướng sảng khoái đê mê giống như lần thăng cấp khí huyết đầu tiên, thì đột nhiên, từ sâu trong cơ thể hắn bỗng truyền đến một cơn đau đớn dữ dội khiến Phương Bình phải bật ra một tiếng rên rỉ đau đớn nghẹn ngào!

Những vùng da thịt để lộ ra bên ngoài như cánh tay, vùng cổ, mu bàn tay……

Tất cả những nơi đó, từng đường gân xanh bỗng nhiên thi nhau lồi hẳn lên trên bề mặt da, căng phồng giật giật liên hồi, nhìn qua trông vô cùng dữ tợn và đáng sợ!

Phương Bình nghiến chặt hai hàm răng đến mức phát ra tiếng kèn kẹt, cả người hắn phải tựa hẳn vào bức tường của một cửa tiệm ven đường, hai bàn tay siết chặt lại thành nắm đấm đến trắng bệch, cắn răng gồng mình chịu đựng cơn đau đớn xé thịt xé da, quyết không để mình gào thét thảm thiết ra ngoài đường.

Chẳng biết đã trôi qua bao nhiêu thời gian, trên gương mặt Phương Bình mồ hôi mồ kê đã vã ra nhễ nhại ướt đẫm như vừa vớt dưới nước lên.

"Phù……!"

Thở hắt ra một ngụm trọc khí nặng nề, rất nhanh sau đó Phương Bình liền hạ thấp giọng chửi thề một câu: "Đm nó chứ, đây là đang muốn chơi xỏ mình đấy à?!"

Lần thăng cấp đầu tiên sướng biết bao nhiêu cơ chứ!

Thế mà lần này, cơn đau dữ dội suýt chút nữa đã làm cho hắn phải lăn lộn quằn quại dưới mặt đất.

Ngay tại khoảnh khắc khí huyết tăng vọt lên ban nãy, hắn thậm chí còn có cảm giác huyết quản trong toàn bộ cơ thể mình sắp sửa bị luồng khí huyết cuồn cuộn kia căng nứt toác ra đến nơi.

May mà cơn đau này đến nhanh mà đi cũng cực kỳ nhanh chóng. Nếu như nó kéo dài thêm một lát nữa thôi thì Phương Bình cũng không dám chắc liệu bản thân mình có mất hết liêm sỉ mà nằm lăn đùng ra giữa phố gào khóc lăn lộn hay không.

Vẫn còn chưa hết cảm giác bàng hoàng kinh hãi sau cơn thập tử nhất sinh, Phương Bình đưa tay vuốt vuốt bắp tay mình, đôi lông mày nhíu chặt lại: "Tố chất thân thể của mình không theo kịp sao?"

Lần đầu tiên tăng điểm khí huyết hắn không quá để ý tới điều này.

Thế nhưng lần này Phương Bình đã cảm nhận được vô cùng rõ ràng: Rất có thể là do thành mạch máu và thể chất của hắn quá mức yếu ớt mỏng manh, cho nên khi khí huyết đột ngột tăng vọt lên đã suýt chút nữa làm nổ tung huyết quản.

Đây mới chỉ là lần thứ hai tăng điểm khí huyết mà thôi đấy nhé! Phương Bình vô cùng hoài nghi nếu như mình dám liều mạng tăng thêm một lần nữa, thì khéo bản thân hắn sẽ lập tức biến thành một đài phun nước hình người sống động, mà thứ phun ra lại chính là máu tươi đỏ lòm!

"Chỉ có một thể phách cường tráng dẻo dai thì mới có thể chống đỡ nổi sự thăng tiến của khí huyết hùng hậu……"

"Xem ra, việc rèn luyện tố chất thân thể cũng bắt buộc phải đưa vào lịch trình khẩn cấp ngay từ bây giờ rồi."

Khối lượng nhiệm vụ vốn dĩ đã vô cùng bận rộn ngập đầu, giờ đây lại càng thêm nặng nề gấp bội.

Thế nhưng việc nâng cao thể chất là điều vô cùng cấp thiết và bắt buộc phải làm. Cho dù không phải vì mục đích tăng thêm khí huyết, thì riêng cửa ải thực trắc phía sau cũng đòi hỏi thí sinh phải có một nền tảng thể chất cực kỳ tốt thì mới mong vượt qua nổi.

Phương Bình lúc này đem so sánh ra thì chẳng khác gì mấy tên phế vật "ngâm mình trong hũ thuốc bổ lớn lên" mà ban nãy Vương Kim Dương vừa nhắc tới cả.

Cứ nghĩ tới điều này Phương Bình lại dở khóc dở cười: Người khác thì lo ngay ngáy chuyện khí huyết không cách nào tăng lên nổi, còn bản thân hắn thì lại hoàn toàn ngược lại, thân thể yếu ớt không chịu nổi sự bùng nổ của khí huyết.

Lại liếc nhìn bảng số liệu trong tầm mắt một lần nữa, Phương Bình thầm nghĩ: Hiện tại mình đã chạm tới mốc 120 cal rồi đúng không?

Hắn căn bản không hề có ý định chạy qua nhà Ngô Chí Hào để đo kiểm tra lại một lần nữa. Mới chỉ cách nhau có đúng một ngày trời, nếu hôm nay hắn vác xác qua đó đo ra con số đỉnh cao lên tới 125 cal thì e rằng Ngô Chí Hào sẽ tức đến mức nhảy lầu tự tử mất.

Đương nhiên, khả năng cao hơn là tên đó sẽ lôi Phương Bình cùng nhảy lầu chung cho có bạn có bè.

……

Đúng 2 giờ chiều, mọi người lại một lần nữa tề tựu đông đủ trước cổng trường.

Mấy người cùng leo lên chiếc xe thương vụ của trường, chạy thẳng tới khu nhà của Vương Kim Dương để đón vị học trưởng này tới trường.

Khu dân cư nơi gia đình Vương Kim Dương sinh sống môi trường cảnh quan cũng rất bình thường, cùng lắm chỉ nhỉnh hơn khu Cảnh Hồ Viên của nhà Phương Bình một chút xíu mà thôi.

Lúc xe chạy tới nơi thì Vương Kim Dương đã đứng sẵn ở cổng khu nhà chờ đợi từ bao giờ.

Buổi sáng trở về hai bàn tay trắng, thế nhưng lúc này trên tay Vương Kim Dương lại xách theo một chiếc ba lô du lịch căng phồng, chẳng biết bên trong nhét những thứ gì.

Mọi người cũng không dám tò mò hỏi han nhiều, người ta về quê một chuyến, mang theo ít đặc sản quê hương mang lên trường cũng là chuyện hết sức bình thường.

Vương Kim Dương xách ba lô chuẩn bị bước chân lên xe, bỗng nhiên anh khựng người lại, quay phắt đầu nhìn chằm chằm vào Phương Bình đang đứng bên cạnh. Trong đáy mắt anh thoáng hiện lên một tia nghi hoặc sâu sắc, đôi lông mày khẽ nhíu lại: "Phương Bình, buổi trưa em làm cái gì đấy?"

"Dạ?"

Phương Bình sững sờ ngơ ngác, ngay sau đó trong lòng bỗng dâng lên một cỗ cảm giác căng thẳng tột độ: Chẳng lẽ võ giả thực thụ lại có khả năng cảm nhận được sự gia tăng khí huyết của người khác sao?

Kết quả quả thực không ngoài dự liệu của hắn, Vương Kim Dương nhíu chặt mày, nghiêm giọng nói: "Mặc dù tôi rất thấu hiểu tâm lý của các em, vì kỳ thi võ khoa có thể không tiếc bất kỳ giá nào để đánh đổi.

Thế nhưng thân thể mới chính là gốc rễ căn bản!

Có một số loại thuốc hổ lang cực độc, vạn lần tuyệt đối không được phép uống bừa bãi!

Chỉ cần sơ sẩy một chút thôi là có thể rước lấy đại họa sát thân vào người!

Tôi không biết buổi trưa em đã uống loại dược phẩm quỷ quái gì, thế nhưng khí huyết của em đột ngột tăng vọt lên quá nhiều, trạng thái này cực kỳ dễ xảy ra sự cố nguy hiểm.

Khoảng thời gian này em phải tăng cường vận động rèn luyện thân thể thật nhiều để cho luồng khí huyết này bình ổn lắng dịu xuống. Trong vòng một tuần lễ tới, vạn lần tuyệt đối không được tiếp tục sử dụng thêm bất kỳ loại thuốc bổ khí huyết nào nữa!"

Phương Bình nghe vậy tảng đá trong lòng rốt cuộc cũng được trút bỏ, vội vàng gật đầu lia lịa: "Em hiểu rồi ạ! Cảm ơn anh Vương đã chỉ bảo. Trước đây em chưa từng có kinh nghiệm, lần này cũng là lần đầu tiên em uống thuốc bổ, ban nãy em cũng cảm thấy các mạch máu trong người căng phồng lên đau nhức lắm ạ."

"Hóa ra là lần đầu tiên, thảo nào……"

Vương Kim Dương khẽ lẩm bẩm một câu. Là một võ giả thực thụ, cảm quan và trực giác của anh cực kỳ nhạy bén sắc sảo.

Buổi sáng khí huyết của Phương Bình rõ ràng còn thấp hơn Ngô Chí Hào một chút, thế nhưng hiện tại, trong mắt anh, khí huyết trên người Phương Bình lại bốc lên ngùn ngụt, thậm chí còn vượt mặt cả Ngô Chí Hào, huyết khí dâng trào vô cùng mãnh liệt.

Anh không biết Phương Bình rốt cuộc đã uống loại thuốc gì, thế nhưng hiệu quả của loại thuốc này quá đỗi kinh người, rất có khả năng là một loại cấm dược có tác dụng tiêu hao vắt kiệt tiềm năng thân thể.

Thế nhưng nghĩ tới việc đối phương mới chỉ là lần đầu tiên dùng thuốc, đối với những kiến thức này hoàn toàn mù tịt không hiểu rõ, lại thêm đến tận thời điểm nước sôi lửa bỏng này mới lần đầu tiên được uống thuốc bổ, gia cảnh chắc chắn cũng chẳng mấy khá giả gì.

Nghĩ tới đây, Vương Kim Dương cũng không truy cứu gặng hỏi xem hắn đã uống loại thuốc gì nữa, chỉ trầm giọng nhắc nhở thêm một câu: "Sau này có mua thuốc, trước khi nắm rõ dược tính và công hiệu của nó thì bắt buộc phải tìm đến các hiệu thuốc lớn chính quy của nhà nước mà mua!

Ngoài xã hội có rất nhiều kẻ bất lương tự ý phối trộn thuốc bừa bãi, các thành phần dược liệu xung khắc lẫn nhau, gây ra tác hại cực kỳ khủng khiếp cho thân thể.

Không phải lúc nào em cũng may mắn thoát chết như lần này đâu. Những người vì uống thuốc bừa bãi mà dẫn đến mất mạng hoặc tàn phế cả đời, hàng năm trên cả nước nhiều vô số kể đấy.

Tuy nhiên vì em là lần đầu tiên sử dụng, nền tảng thể chất trước đây tích lũy cũng tạm coi là ổn định nên mới miễn cưỡng chống đỡ vượt qua được. Tuyệt đối không được coi sự may mắn là điều hiển nhiên thường tình, sau này phải hết sức chú ý cẩn trọng!"

"Vâng ạ, em nhất định sẽ ghi nhớ kỹ lời anh dặn, cảm ơn anh Vương nhiều lắm ạ."

"Đừng khách sáo làm gì."

Thái độ của Vương Kim Dương đối với Phương Bình rõ ràng đã hòa hoãn và thân thiện hơn trước rất nhiều, kế đó anh lại mỉm cười nói: "Tuy nhiên lần này em mạo hiểm cũng không coi là lỗ vốn đâu. Đợi luồng khí huyết này hoàn toàn lắng dịu ổn định trở lại, chịu khó rèn giũa tôi luyện thân thể thêm một chút, năm nay cánh cửa võ khoa đối với em tràn đầy hy vọng đấy."

Màn đối thoại giữa hai người, đám người Ngô Chí Hào ngồi bên cạnh đều nghe thấy không sót một chữ nào.

Ban đầu mọi người ai nấy đều nghe ra được rằng buổi trưa Phương Bình chắc chắn đã lén lút uống loại thuốc bổ khí huyết nào đó, dường như còn gây ra tổn thương không nhỏ cho thân thể.

Thế nhưng ai mà ngờ được, nghe đến đoạn cuối cùng, Vương Kim Dương thế mà lại buông ra lời khẳng định chắc nịch rằng Phương Bình thi võ khoa tràn đầy hy vọng!

Phải biết rằng ngay cả Ngô Chí Hào vào buổi sáng nay cũng chưa từng nhận được một lời đánh giá cao ngút trời đến như vậy từ miệng của vị học trưởng truyền kỳ này!

Cho nên vừa nghe thấy câu nói đó, Ngô Chí Hào lập tức không kiềm chế nổi sự kinh hãi chấn động trong lòng, thốt lên: "Anh Vương ơi, khí huyết của Phương Bình tăng vọt lên nhiều lắm sao anh?"

Vương Kim Dương khẽ cười đáp: "Tôi đâu phải là chiếc máy đo khí huyết di động đâu, chỉ có thể cảm nhận và nhìn ra được một phần đại khái mà thôi. Thế nhưng dẫu có là như vậy thì cũng đủ để nhìn thấy thằng nhóc này quả thực đã gia tăng khí huyết không hề thấp chút nào đâu."

Phương Bình vội vàng cười gượng giả lả: "Bình thường thôi ạ, em tự cảm thấy cũng chẳng khác gì so với trước kia là bao."

"Hahaha……"

Vương Kim Dương cười lớn một tiếng, cũng không buồn vạch trần lời nói dối vụng về của hắn, nhưng quay sang nghiêm túc dặn dò đám người Ngô Chí Hào: "Các em tuyệt đối không được học theo cái thói liều lĩnh của cậu ta đâu đấy nhé! Cậu ta là vì không hiểu biết gì nên lần này mới dám mạo hiểm làm liều như vậy.

Dược phẩm tuyệt đối không thể tùy tiện sử dụng bừa bãi, đặc biệt là những loại thuốc nằm ngoài danh mục thuốc thông thường như Huyết Khí Hoàn hay Khí Huyết Đan thì càng không được phép uống bừa!

Cậu ta lần này thuần túy là do vận may chó ngáp phải ruồi mà thôi, nếu như vận may kém đi một chút thì bây giờ mạch máu đã nổ tung toàn thân rồi, hậu quả khôn lường không thể cứu vãn nổi đâu.

Sự vô tri quả thực là quá đỗi đáng sợ!"

Vương Kim Dương lắc đầu ngao ngán, nếu đổi thành những học sinh đã từng được trang bị đầy đủ kiến thức võ đạo bài bản thì đánh chết bọn họ cũng không bao giờ dám làm ra cái hành động điên rồ liều mạng như thế này.

Vừa nghe thấy hậu quả ghê rợn "mạch máu nổ tung", cả ba người Ngô Chí Hào, Dương Kiến và Lưu Nhược Kỳ lập tức rụt cổ lại, trong mắt ánh lên nỗi khiếp sợ kinh hoàng tột độ.

Ngô Chí Hào hạ thấp giọng thì thầm hỏi nhỏ: "Phương Bình, rốt cuộc cậu đã mua loại thuốc quỷ quái gì về uống thế hả?"

Phương Bình gãi đầu gãi tai, làm ra vẻ mặt ngượng ngùng讪讪 đáp: "Hôm qua chẳng phải vừa đo ở nhà cậu xong sao, về nhà bố tớ liền bấm bụng đưa cho tớ một khoản tiền lớn, bảo tớ cầm đi mua thuốc bổ về uống tẩm bổ để cố gắng thi đỗ võ khoa.

Sáng nay lúc chúng mình vừa chia tay nhau xong, tớ đang trên đường đi bộ về nhà thì bỗng nhiên trên đường có người kéo lại hỏi tớ có muốn mua thuốc đại bổ không, giá rẻ bèo nhèo à, thế là tớ cắn răng mua đại một viên……"

"Cậu……!"

Ngô Chí Hào trố mắt há hốc mồm, cảm thấy khó tin đến mức không thể tưởng tượng nổi: "Cậu bị điên rồi sao?! Lũ lừa đảo bán thuốc dạo ngoài đường mà cậu cũng dám tin à?!"

"Thì tại vì nó rẻ mà lị! Người ta bảo đó là Huyết Khí Hoàn, giá chỉ có vài ngàn tệ thôi. Hôm qua chẳng phải cậu bảo ở hiệu thuốc bán tận 3 vạn tệ một viên sao?"

"Cậu bị ngốc hay là thằng bán thuốc nó bị thiểu năng hả?! Món đồ trị giá 3 vạn tệ mà người ta lại đem bán cho cậu với giá vài ngàn tệ chắc?!"

Ngô Chí Hào hoàn toàn cạn lời không còn từ ngữ nào để diễn tả nổi sự ngán ngẩm nữa. Dương Kiến ngồi bên cạnh cũng gãi đầu ngơ ngác, lẩm bẩm: "Đến tao mà còn chẳng dám liều mạng như thế, Phương Bình, thằng nhóc mày đúng là đồ điên rồ số một rồi."

Ban đầu bọn họ còn tò mò muốn gặng hỏi xem Phương Bình rốt cuộc đã uống loại thần dược gì, giờ thì đã hoàn toàn dẹp bỏ sạch sành sanh mọi ý định đó ra khỏi đầu.

Cái loại thuốc vô danh trôi nổi không rõ nguồn gốc xuất xứ như thế này, nếu thực sự uống bừa vào người thì có chết cũng chẳng biết vì sao mình chết.

Huống chi đối phương đã lừa Phương Bình một vố rồi thì giờ này chắc đã cao chạy xa bay biến mất tăm mất tích từ lâu rồi, có tìm vào mắt.

Cái hành vi đánh cược cả tính mạng để cưỡng ép tăng cường khí huyết như thế này, trừ phi thực sự bị dồn vào bước đường cùng không còn lối thoát, nếu không thì chẳng có đứa học sinh cấp ba nào đủ gan to tày trời để mang mạng sống ra đánh cược cả.

"Sự vô tri quả thực là quá đỗi đáng sợ!"

Đây có lẽ là suy nghĩ duy nhất đang hiện lên trong đầu óc của tất cả mọi người có mặt trên xe lúc này. Đổi thành bọn họ thì ai rảnh rỗi mà đi mua thuốc dạo ngoài đường về nhét vào mồm cơ chứ?

Phương Bình thấy cảnh tượng này thì trong lòng rốt cuộc cũng thở phào một cái nhẹ nhõm: Cuối cùng cũng lừa gạt cho qua chuyện êm xuôi được rồi.

Trước đó hắn cũng hoàn toàn không thể ngờ tới việc một võ giả thực thụ như Vương Kim Dương lại có thể nhạy bén cảm nhận được sự biến đổi khí huyết trên người mình rõ ràng đến như vậy.

Giờ nhìn lại mới thấy võ giả thực sự đáng sợ hơn rất nhiều so với những gì hắn hằng tưởng tượng, hoặc giả là do thực lực của bản thân Vương Kim Dương vượt trội hơn hẳn người bình thường rất nhiều.

Thế nhưng bị người ta "vạch trần" theo cái kịch bản này cũng không phải là chuyện xấu gì: Đến lúc khám thể chất chính thức đo ra điểm số cao vọt lên thì đám người Ngô Chí Hào cũng sẽ không cảm thấy quá mức bất ngờ hay nghi ngờ nữa.

Ngoài ra còn có thêm một điểm lợi ích to lớn ngoài dự liệu: Vương Kim Dương có lẽ cảm thấy tiềm năng thi đỗ võ khoa của Phương Bình là rất lớn, cho nên trên suốt quãng đường xe chạy về trường, anh đã tận tình chỉ điểm thêm cho Phương Bình rất nhiều kinh nghiệm quý báu.

Chủ yếu đều là các phương pháp rèn luyện và tôi dưỡng tố chất thân thể, cuối cùng anh thậm chí còn mỉm cười nói: "Năm nay Trường Số 1 chúng ta e rằng lại sắp sửa xuất hiện thêm một bất ngờ chấn động nữa rồi đây. Hy vọng em đừng để bị sẩy chân ở những môn thi khác, biết đâu chừng chỉ vài tháng nữa thôi, chúng ta lại trở thành bạn đồng môn chung trường đấy."

Lời này vừa thốt ra, đám người Ngô Chí Hào ngồi bên cạnh thực sự là vừa ghen tị lại vừa ngưỡng mộ đến đỏ cả mắt. Thế nhưng bảo bọn họ có đủ dũng khí chạy ra đường mua thuốc dạo về uống liều mạng như Phương Bình thì đánh chết bọn họ cũng không có cái lá gan đó."""
    },
    19: {
        "url": "https://www.piaotia.com/html/9/9640/6523773.html",
        "title_vi": "Chương 19: Thời Gian Biểu",
        "content_vi": """Trong lúc trò chuyện rôm rả, chiếc xe thương vụ đã nhanh chóng lăn bánh tới trước cổng Trường Số 1.

Từ đằng xa xa đã có thể nhìn thấy rất đông người đang đứng tập trung chờ đón ở bên ngoài cổng trường.

Người dẫn đầu đoàn tiếp đón không ai khác chính là thầy chủ nhiệm phòng giáo vụ của Trường Số 1.

Hiệu trưởng hiện tại không có mặt ở trường, thầy chủ nhiệm phòng giáo vụ đích thân dẫn đầu phái đoàn đứng túc trực ngay cổng trường đón tiếp, mức độ đãi ngộ long trọng này so với việc đón tiếp các vị lãnh đạo cấp thành phố về trường thanh tra thị sát chẳng có chút khác biệt nào.

Mà Vương Kim Dương hiện tại mới chỉ là một cậu sinh viên năm nhất đại học mà thôi, thứ thực sự khiến cho ban giám hiệu nhà trường phải coi trọng và cung kính đến nhường này chính là thân phận "Võ Giả" cao quý của anh ta.

Nếu đặt vào thời điểm này của năm ngoái, vị chủ nhiệm phòng giáo vụ quyền cao chức trọng kia e rằng đến một cái liếc mắt nhìn thẳng cũng chẳng thèm đoái hoài tới Vương Kim Dương.

Chỉ cách nhau một bước chân ngắn ngủi, mà địa vị lại một trời một vực.

……

Vương Kim Dương bước xuống xe bắt tay trò chuyện với các vị lãnh đạo nhà trường, còn nhóm người Phương Bình thì rảo bước tiến về phía thầy Lưu An Quốc đang đứng chờ.

Lưu An Quốc cũng có mặt trong dòng người đứng đón tiếp, ngoài các thầy cô giáo ra thì còn có sự góp mặt của một số học sinh ưu tú.

Phương Bình đối với những học sinh này không mấy quen mặt, nhưng Ngô Chí Hào thì lại nắm rất rõ, bèn hạ thấp giọng giải thích: "Phần lớn đều là học sinh của các lớp chọn, ngoài ra còn có thêm một vài gương mặt xuất sắc đứng đầu của các lớp thường."

Thứ mà cậu ta nhắc tới ở đây dĩ nhiên không phải là thành tích các môn văn hóa, mà là các hạt giống tiềm năng của môn võ khoa.

Những người có đủ tư cách đứng ở đây hôm nay đều là những niềm hy vọng sáng giá nhất của Trường Số 1 trong kỳ thi võ khoa năm nay.

Nếu không phải do mấy đứa Phương Bình được giao trọng trách đi đón tiếp Vương Kim Dương từ trước, thì vào thời điểm này ngoại trừ Ngô Chí Hào ra, những người còn lại căn bản không có đủ tư cách để bước chân vào hàng ngũ này.

Đương nhiên, đó là chuyện của trước kia, còn Phương Bình của ngày hôm nay thì hiển nhiên đã thừa sức có được tư cách đó rồi.

Lưu An Quốc không phải là lãnh đạo cấp cao của trường, cho nên lúc Vương Kim Dương đang mải mê trò chuyện với các vị lãnh đạo, ông cũng không tiện chen ngang bước tới bắt chuyện.

Thấy mấy đứa học trò cưng của lớp mình đã quay trở về, Lưu An Quốc liền hạ thấp giọng hỏi han: "Thế nào rồi các em, chuyến đi này có gặt hái được thu hoạch gì bổ ích không?"

Ngô Chí Hào trước tiên gật đầu lia lịa biểu thị thu hoạch lần này là vô cùng to lớn.

Kế đó cậu ta lại dùng ánh mắt vừa ghen tị vừa ngưỡng mộ nhìn sang Phương Bình, khẽ thở dài: "Người có thu hoạch to lớn nhất chính là Phương Bình thầy ạ. Thầy ơi, khí huyết của Phương Bình lại vừa tăng vọt lên nữa rồi, khéo bây giờ còn cao hơn cả em nữa ấy chứ……"

"Làm sao có thể như thế được?!"

Lưu An Quốc ngẩn người ra một lúc, gương mặt ngập tràn vẻ khó tin đến tột cùng.

Sự gia tăng của khí huyết đâu phải là chuyện ngày một ngày hai mà làm được.

Huống chi gia cảnh nhà Phương Bình chỉ ở mức bình dân lao động bình thường, làm sao có thể dễ dàng vượt mặt một người có điều kiện tẩm bổ đủ đầy như Ngô Chí Hào được chứ?

Ngô Chí Hào đương nhiên hiểu rõ nỗi kinh ngạc sững sờ của thầy chủ nhiệm, bèn vội vàng ghé tai thầy thì thầm giải thích đầu đuôi câu chuyện.

Đợi đến khi nghe xong chuyện thằng nhóc Phương Bình này dám to gan lớn mật mua thuốc dạo ngoài đường về uống bừa bãi, Lưu An Quốc cũng hoàn toàn cạn lời không thốt lên nổi một câu: Đám thanh niên trẻ tuổi thời nay không biết sợ chết là cái gì nữa rồi sao?

Thế nhưng chuyện nguy hiểm dù sao cũng đã trôi qua rồi, Phương Bình lại nhân họa đắc phúc thu về kết quả mỹ mãn, Lưu An Quốc bấy giờ mới vỡ òa trong niềm vui sướng khôn xiết: "Nói như vậy tức là năm nay lớp 12 ban 4 của chúng ta rất có thể sẽ tạo nên một kỳ tích chấn động rồi!"

Ngô Chí Hào thi đỗ võ khoa vốn dĩ đã tràn trề hy vọng, giờ đây lại xuất hiện thêm một Phương Bình bùng nổ vượt bậc nữa, một lớp thường bình thường mà đào tạo ra được hẳn hai sinh viên đại học võ khoa……

Chỉ cần nghĩ tới viễn cảnh huy hoàng đó thôi là Lưu An Quốc đã kích động đến mức toàn thân run rẩy run rẩy không thôi rồi.

Năm ngoái Vương Kim Dương và một học sinh lớp thường khác thi đỗ vào đại học võ khoa, bản thân hai học sinh đó đỗ đạt dĩ nhiên là công thành danh toại rạng rỡ tổ tông.

Thế nhưng điều khiến cho những giáo viên già như Lưu An Quốc phải đỏ mắt thèm thuồng ngưỡng mộ lại không phải là bản thân hai học sinh đó, mà chính là hai vị giáo viên chủ nhiệm của hai lớp thường kia!

Bởi vì trong lớp dạy dỗ xuất hiện học sinh thi đỗ võ khoa — mà lại còn là xuất thân từ lớp thường nữa chứ — cho nên hai vị giáo viên chủ nhiệm đó vào năm ngoái chỉ riêng tiền thưởng nóng của nhà trường và ngành giáo dục trao tặng đã lên tới hơn mười vạn tệ!

Con số khổng lồ đó tương đương với tiền lương tích cóp cày cuốc suốt hai năm trời ròng rã của những giáo viên chủ nhiệm như các ông!

Ngoài tiền bạc vật chất ra thì còn có biết bao nhiêu bổng lộc danh vọng khác đi kèm: Cơ hội thăng quan tiến chức rộng mở, cơ hội được xét tặng danh hiệu giáo viên ưu tú xuất sắc cấp tỉnh……

Một lớp có một học sinh thi đỗ đã vẻ vang lẫy lừng đến nhường ấy rồi, vậy nếu như có hẳn hai học sinh cùng thi đỗ thì sẽ khủng khiếp đến mức độ nào nữa chứ?

Lưu An Quốc cảm thấy đầu óc mình hơi choáng váng quay cuồng. Chẳng lẽ năm nay chính bản thân ông lão này sẽ trở thành vị giáo viên chủ nhiệm xuất sắc nhất trong lịch sử của Trường Số 1: Người đầu tiên bồi dưỡng ra được hai võ giả thực thụ từ một lớp thường bình thường sao?

Chưa hết đâu…… Dương Kiến và Lưu Nhược Kỳ trong lớp cũng chưa chắc đã hoàn toàn hết hy vọng……

Càng nghĩ sâu xa, Lưu An Quốc lại càng cảm thấy say sưa đê mê ngây ngất cõi lòng.

Một người đàn ông đã ngoài năm mươi tuổi đầu rồi, thế mà vào lúc này lại không kiềm chế nổi mà toét miệng cười toe toét ngây ngô chẳng khác nào một đứa trẻ con vừa được cho kẹo.

Đứng ngay bên cạnh còn có các giáo viên chủ nhiệm của những lớp khác, bao gồm cả hai vị giáo viên chủ nhiệm đầy quyền uy của hai lớp chọn.

Một người nhìn thấy nụ cười đắc ý đến kỳ quặc của Lưu An Quốc liền không nhịn được buông lời trêu chọc: "Này ông Lưu, chú ý giữ gìn hình tượng một chút đi chứ, học sinh còn đang đứng đầy xung quanh kia kìa."

Lưu An Quốc vẻ mặt đầy tự hào hãnh diện, theo bản năng đưa tay dang rộng che chắn mấy đứa học trò Ngô Chí Hào và Phương Bình ở phía sau lưng mình, cười tủm tỉm đáp: "Tôi vui vẻ cười một tí mà cũng phạm pháp à? Này ông Lý, nghe đồn dạo gần đây ông đắc ý lắm đúng không, đi đâu gặp ai cũng vỗ ngực khoe khoang rằng danh hiệu giáo viên chủ nhiệm ưu tú năm nay đã nằm chắc trong túi ông rồi?"

Người được Lưu An Quốc gọi là "ông Lý" cũng là một giáo viên kỳ cựu trạc tuổi năm mươi, thế nhưng hoàn cảnh và vị thế của đối phương thì xịn xò hơn Lưu An Quốc rất nhiều: Ông ấy là giáo viên chủ nhiệm của lớp chọn danh giá nhất trường.

Nghe thấy lời mỉa mai của Lưu An Quốc, ông Lý cười ha hả đáp: "Sao nào? Không phải tôi đoạt giải thì ông tưởng là lão Trương chắc?

Chu Bân của lớp chúng tôi năm nay chắc chắn một trăm phần trăm sẽ thi đỗ vào đại học võ khoa, nếu như vận may bùng nổ một chút thì ngay cả hai ngôi trường danh giá hàng đầu là Đại học Võ thuật Bắc Kinh và Đại học Võ thuật Ma Đô cũng tràn trề hy vọng đấy nhé……"

Hai trường đại học võ khoa này chính là hai ngôi trường danh giá và uy quyền bậc nhất trên toàn lãnh thổ quốc gia.

Nam có Ma Võ, Bắc có Kinh Vũ.

So với Đại học Võ thuật Nam Giang thì hai ngôi trường huyền thoại này có độ khó thi tuyển cao hơn gấp bội phần.

Đối với màn khoe khoang khoác lác của ông Lý, Lưu An Quốc tuy rằng bĩu môi khinh bỉ trong bụng, nhưng ngoài mặt cũng không tiện lên tiếng phản bác.

Chu Bân thi đỗ vào đại học võ khoa là chuyện nắm chắc chín mươi chín phần trăm trong tay, thế nhưng muốn với tới hai trường danh giáo kia thì hy vọng thực sự không quá lớn.

Tuy nhiên lúc này Chu Bân cũng đang đứng sừng sững trong đám đông học sinh đằng kia, là một người thầy giáo dục, tự nhiên ông không thể buông lời đả kích làm nhụt chí của học trò được.

Lưu An Quốc giữ nụ cười rạng rỡ trên môi, hoàn toàn không thèm cãi cọ đôi co, chỉ khẽ liếc mắt nhìn sang Phương Bình và Ngô Chí Hào một cái: Năm nay lớp 12 ban 4 chỉ cần có hai học sinh thi đỗ võ khoa thì danh hiệu giáo viên chủ nhiệm ưu tú nhất trường chắc chắn sẽ rơi thẳng vào đầu ông, không chạy đi đâu cho thoát!

Cho dù lớp chọn của ông Lý có số lượng học sinh đỗ nhiều hơn đi chăng nữa, thì lớp chọn vốn dĩ là cái nôi được nhà trường dồn toàn bộ nguồn lực tinh hoa nhất để bồi dưỡng võ khoa, thi đỗ là chuyện đương nhiên lẽ thường tình, thi trượt thì mới là tội đồ đáng trách.

Chỉ cần Chu Bân không thi đỗ vào hai trường danh giáo hàng đầu kia, thì lớp chọn của ông Lý có đỗ nhiều hơn lớp 12 ban 4 cũng chẳng có nghĩa lý gì.

Ông Lý đứng bên cạnh bị nụ cười đầy ẩn ý của Lưu An Quốc làm cho rợn cả tóc gáy: Cái lão già này hôm nay bị trúng gió hay sao mà nhìn mình cười ghê rợn thế không biết?

Không chỉ có các giáo viên xung quanh cảm thấy kỳ lạ, mà ngay cả Phương Bình và Ngô Chí Hào cũng cảm thấy rùng mình ớn lạnh cả người: Ánh mắt của Lão Ban lúc này nhìn hai đứa bọn hắn đâu phải là nhìn học trò nữa, nhìn con trai ruột thịt khéo cũng chỉ âu yếm và cưng chiều đến mức độ này là cùng!

Phương Bình đại khái có thể hiểu thấu được tâm tư suy nghĩ của người thầy chủ nhiệm già này, trong lòng bất giác dở khóc dở cười.

Giữa lúc mấy thầy trò đang thì thầm to nhỏ bàn tán với nhau thì phía đằng trước Vương Kim Dương cũng đã kết thúc màn chào hỏi xã giao với ban giám hiệu nhà trường.

Rất nhanh sau đó, Vương Kim Dương liền cất bước tiến về phía đám học sinh ưu tú đang đứng xếp hàng chờ đợi.

Đưa mắt nhìn lướt qua một lượt, Vương Kim Dương mỉm cười gật đầu tán thưởng: "Đúng là khóa sau mạnh hơn khóa trước, lứa đàn em khóa này của trường ta mạnh mẽ hơn hẳn so với lứa học sinh năm ngoái của chúng tôi rất nhiều.

Thành tích giáo dục của Trường Số 1 ngày càng rực rỡ xuất sắc, công lao to lớn này không thể tách rời khỏi sự dạy dỗ tận tụy của quý thầy cô giáo."

Mặc dù mới chỉ là sinh viên năm nhất, thế nhưng những lời ăn tiếng nói khách sáo, những câu từ chuẩn mực chính thống nơi quan trường lại được Vương Kim Dương thốt ra một cách vô cùng trôi chảy đường hoàng đĩnh đạc, khiến cho vị chủ nhiệm phòng giáo vụ đứng bên cạnh nghe xong mà mặt mày nở hoa, cười rạng rỡ hồng hào cả khuôn mặt.

Đây rốt cuộc là lời khen ngợi đích thân thốt ra từ miệng của một võ giả chính thức cơ mà!

Các vị lãnh đạo của Trường Số 1 trên thực tế vẫn luôn âm thầm theo dõi sát sao tình hình của những cựu học sinh từng thi đỗ vào các trường võ đại. Tình hình cụ thể chi tiết ra sao, do có một số tin tức cơ mật không được phép truyền ra ngoài nên các thầy cũng không nắm bắt được tường tận.

Thế nhưng trên dưới Trường Số 1 ai nấy đều biết rất rõ: Trong số 5 học sinh thi đỗ vào võ đại năm ngoái, đến thời điểm hiện tại chỉ có vẻn vẹn hai người thực sự trở thành võ giả chính thức mà thôi.

Mà trong số hai người kiệt xuất đó, danh tiếng của Vương Kim Dương lại vang dội vượt trội hơn hẳn. Ngay cả một số cựu sinh viên võ đại khóa trước vẫn còn giữ liên lạc với nhà trường, mỗi lần trong các cuộc trò chuyện nhắc tới cái tên Vương Kim Dương đều lộ vẻ mặt vô cùng phức tạp, thở dài thán phục không thôi.

Từ miệng của các cựu sinh viên khóa trước truyền về, ban giám hiệu Trường Số 1 cũng đã nắm được thông tin Vương Kim Dương ở Nam Giang Võ Đại có thành tích cực kỳ xuất chúng nổi trội, đó mới chính là nguyên nhân sâu xa khiến nhà trường tha thiết mời bằng được Vương Kim Dương về trường giao lưu đợt này.

Cũng may là đợt này Vương Kim Dương vừa vặn có việc phải quay trở về Dương Thành, sau khi nhận được lời mời nhiệt tình từ phía nhà trường, anh cũng không do dự nhiều mà gật đầu nhận lời ngay.

Nếu không thì chưa chắc anh đã chịu bớt chút thời gian quý báu để ghé qua Trường Số 1.

Vương Kim Dương nói lời khách sáo vài câu, ánh mắt lại bất giác đảo qua nhìn Phương Bình một cái. Trong cảm nhận nhạy bén của anh, trong số đám học sinh ưu tú đang đứng ở đây hôm nay, những người có khí huyết dồi dào sung mãn nhất chắc chắn có sự hiện diện của Phương Bình.

Thậm chí, độ hùng hậu của khí huyết trên người Phương Bình lúc này chỉ xếp sau mỗi một mình Chu Bân — người đang được toàn thể ban giám hiệu nhà trường đặt trọn niềm tin và kỳ vọng mà thôi.

Cứ nghĩ tới việc sáng sớm nay khí huyết của thằng nhóc này còn ở mức vô cùng bình thường làng nhàng, thế mà chỉ sau một bữa cơm trưa ngắn ngủi đã có được bước đột phá kinh thiên động địa đến nhường này, Vương Kim Dương cũng không khỏi thầm cảm thán trong lòng: Thời vận thế sự quả thực là biến ảo khôn lường.

Nhìn thấy cảnh tượng toàn bộ thầy trò Trường Số 1 lúc này hầu như chẳng có một ai buồn để mắt chú ý tới Phương Bình, Vương Kim Dương thầm cười trộm trong bụng: Năm ngoái trường học này đã xuất hiện một biến số bất ngờ là bản thân mình rồi, năm nay e rằng lại chuẩn bị làm cho các vị giáo viên ở đây phải rớt cằm kinh ngạc một lần nữa cho mà xem.

Chẳng biết đến lúc đó, liệu có khiến cho các vị lãnh đạo nhà trường phải tự ôm đầu nghi ngờ lại năng lực nhìn người của chính bản thân mình hay không nữa.

Vương Kim Dương cũng lười bận tâm tới những chuyện bao đồng này, càng không rảnh rỗi đi nhắc nhở cảnh báo ai làm gì, hoàn toàn chẳng có chút cần thiết nào cả.

Thuận miệng buông lời khen ngợi động viên đám học sinh ưu tú vài câu xong, anh liền cùng vị chủ nhiệm phòng giáo vụ rảo bước tiến về phía hội trường đa năng của nhà trường.

……

Nhóm người Phương Bình cũng hòa vào dòng người học sinh, cùng nhau cất bước tiến về phía hội trường đa năng.

Lúc bước chân vào bên trong hội trường, bên dưới đã có rất đông học sinh ngồi kín các hàng ghế, nhìn sơ qua một lượt e rằng không dưới 200 người.

Đây cũng chính là toàn bộ số lượng học sinh lớp 12 đăng ký dự thi võ khoa của Trường Số 1 năm nay, tính gộp cả nhóm người Phương Bình vào nữa thì ngót nghét tầm khoảng gần 300 học sinh.

Nhóm người Phương Bình vừa bước chân vào cửa đã nhìn thấy Trương Hạo đang vẫy tay rối rít ở phía xa xa, mấy người liền nhanh chóng rảo bước đi về phía đó. Những thí sinh thi võ khoa khác của lớp 12 ban 4 đều đang tập trung ngồi quây quần ở khu vực này.

Vừa mới ngồi ngay ngắn vào chỗ, Trương Hạo đã sốt sắng không nhịn nổi tò mò ghé sát lại hỏi dồn: "Mấy đứa chúng mày đi đón Vương học trưởng có gặt hái được gì không? Vương học trưởng rốt cuộc mạnh mẽ đến mức độ nào vậy?"

Phương Bình còn chưa kịp mở miệng đáp lời thì Ngô Chí Hào đã mỉm cười nói: "Bọn tao làm sao biết được anh ấy mạnh đến mức nào chứ, Vương sư huynh đâu có ra tay đánh nhau với ai đâu.

Những thứ khác lát nữa lên bục giảng Vương sư huynh sẽ nói rõ cho cả trường cùng nghe."

Cậu ta hoàn toàn không hé răng nửa lời về cái mẹo bộc phát cảm xúc phẫn nộ kia, Dương Kiến và Lưu Nhược Kỳ cũng tuyệt đối ngậm chặt miệng không nhắc tới một chữ bẻ đôi.

Bọn họ không biết liệu lát nữa Vương Kim Dương có công khai chia sẻ bí quyết đó trước toàn thể học sinh hay không. Nếu anh ấy nói ra thì việc bọn họ kể hay không kể cũng chẳng khác gì nhau; còn nếu như anh ấy không nói, thì đó lại chính là lợi thế cạnh tranh độc quyền vô cùng to lớn của riêng mấy đứa bọn họ.

Nói cho Trương Hạo biết thì không sao, thế nhưng cái mồm loa mép giải của cái thằng nhóc này chẳng mấy chốc sẽ đi buôn dưa lê rêu rao khắp toàn trường, đến lúc đó thì chút lợi thế khó khăn lắm mới giành được sẽ lập tức tan thành mây khói.

Con người ai nấy đều có chút tâm lý tư lợi ích kỷ cho riêng mình, Phương Bình thấy bọn họ giữ kín như bưng tự nhiên cũng sẽ không dại dột gì mà chủ động đứng ra nói toạc móng heo làm gì.

……

Trong lúc mấy đứa học sinh đang rầm rì trao đổi với nhau thì Vương Kim Dương cùng đoàn đại biểu lãnh đạo nhà trường cũng đã bước chân vào bên trong hội trường.

Bóng dáng của anh vừa xuất hiện ở cửa ra vào, bên dưới khán phòng lập tức vang lên những tràng pháo tay ròn rã nhiệt liệt như sấm dậy!

Một vài bạn nữ sinh thậm chí còn kích động reo hò la hét thất thanh liên hồi.

Chứng kiến cảnh tượng rực rỡ huy hoàng này, bao gồm cả Ngô Chí Hào, gần như toàn bộ học sinh có mặt trong hội trường ánh mắt đều ngập tràn vẻ ngưỡng mộ, sùng bái và khao khát đến tột cùng.

Rất nhiều nam sinh trong lòng bất giác dâng trào lên một cỗ cảm xúc mãnh liệt tráng chí: Làm đấng nam nhi đại trượng phu sống trên đời, nhất định phải được như vậy!

Đây mới chính là hình tượng võ giả mà lũ học trò luôn tôn sùng, ngưỡng mộ và ao ước được trở thành.

Một bước lên mây, bay thẳng lên chín tầng trời xanh, quả đúng là không có gì quá đáng hơn thế.

Thế nhưng Phương Bình vào lúc này lại không có quá nhiều cảm giác kích động bồi hồi như những người xung quanh. Trong khi người khác đang dán chặt mắt vào từng cử chỉ của Vương Kim Dương trên bục giảng, thì hắn lại chăm chú cúi đầu nghiên cứu tờ thời gian biểu của kỳ thi võ khoa vừa được nhà trường phát xuống tận tay.

Từ sau ngày 10 tháng 4, khâu thẩm tra chính trị (Chính thẩm) sẽ chính thức bắt đầu khởi động, đến cuối tháng 4 sẽ kết thúc toàn bộ công tác thẩm tra, những thí sinh nào vượt qua cửa ải này sẽ được cấp thẻ dự thi võ khoa chính thức.

Ngày 1 tháng 5, toàn bộ thí sinh thi võ khoa sẽ tập trung di chuyển lên thành phố Thụy Dương cấp trên trực thuộc để tiến hành kiểm tra thể chất (Thể kiểm).

Ngày 3 tháng 5, kết quả khám thể chất sẽ được công bố chính thức, các trường đại học võ thuật lớn trên toàn quốc và Bộ Giáo Dục sẽ nhận được toàn bộ dữ liệu phản hồi thể chất của thí sinh, trước ngày 5 tháng 5 sẽ thống nhất ban hành mức điểm sàn khí huyết tối thiểu để vượt qua vòng thể kiểm.

Ngày 7 tháng 5, cửa ải Kiểm tra thực tế (Thực trắc) sẽ chính thức bắt đầu diễn ra.

Ngày 10 tháng 5, toàn bộ thí sinh vượt qua các vòng trên sẽ tham gia kỳ thi chuyên nghiệp võ khoa do trung ương thống nhất tổ chức trên phạm vi toàn quốc……

Đây chính là toàn bộ lịch trình thi cử dày đặc của các thí sinh thi võ khoa trong thời gian tới. Sau khi hoàn thành xong kỳ thi chuyên nghiệp thì chỉ còn việc ngồi chờ tham gia kỳ thi văn hóa tốt nghiệp đại học toàn quốc nữa là xong.

Lịch trình thi cử được sắp xếp vô cùng gấp gáp và chặt chẽ, việc dồn nén thời gian lại sát nút như vậy cũng là để tạo điều kiện tối đa cho các thí sinh có thêm thời gian phát triển thể chất đến cực hạn, tránh làm lỡ dở tương lai của những học sinh có độ tuổi còn nhỏ.

Ở ngưỡng tuổi 18 bẻ gãy sừng trâu này, có những học sinh cơ thể phát triển vượt bậc qua từng ngày từng giờ.

Nhìn vào tờ thời gian biểu chi tiết này, trong lòng Phương Bình bất giác dâng lên một cỗ cảm giác cấp bách vô cùng nặng nề.

Khoảng cách từ giờ cho tới ngày khám thể chất chỉ còn lại vỏn vẹn tầm khoảng 20 ngày nữa mà thôi. Trong vòng 20 ngày ngắn ngủi này, liệu bản thân mình có thực sự kịp xoay xở giải quyết ổn thỏa hết tất cả mọi chuyện hay không?

Vấn đề khí huyết thì còn dễ nói, nhưng kỳ thi chuyên nghiệp đối với người khác thì không quá khó khăn, còn đối với một người mới toanh như hắn thì lại là cả một ngọn núi chướng ngại vật khổng lồ, bắt buộc phải nhanh chóng nghĩ cách gia tăng thêm thật nhiều điểm tinh thần thì mới mong vượt qua nổi."""
    },
    20: {
        "url": "https://www.piaotia.com/html/9/9640/6523774.html",
        "title_vi": "Chương 20: Khách Thuê Nhà",
        "content_vi": """Hội trường đa năng Trường Số 1.

Trong khi Phương Bình đang mải mê suy tính trăm phương ngàn kế làm sao để kiếm tiền nâng cấp điểm tinh thần, thì trên bục giảng Vương Kim Dương cũng vô cùng nghiêm túc và nhiệt tình giảng giải cho các em học sinh về những vấn đề cốt lõi liên quan tới kỳ thi võ khoa sắp tới.

……

Cùng lúc đó.

Khu dân cư Cảnh Hồ Viên.

Tòa 6 phòng 201.

Một người đàn ông trung niên trạc tuổi ngoài bốn mươi, gương mặt toát lên vẻ chất phác hiền lành đang cất giọng khẩn khoản: "Chị đại à, chị cứ yên tâm đi, tôi cam đoan sẽ không làm hỏng hóc bất kỳ đồ đạc bàn ghế nào trong nhà đâu.

Nếu như thực sự làm hỏng chỗ nào thì chị cứ việc trừ thẳng vào tiền đặt cọc của tôi!"

Đứng đối diện với người đàn ông là một người phụ nữ lớn tuổi, nghe thấy những lời bảo đảm chắc nịch đó bấy giờ mới nở nụ cười hài lòng đáp: "Được như thế thì tốt quá, căn nhà này của tôi mới sửa sang trang trí lại cách đây mấy năm thôi đấy nhé.

Đừng thấy khu Cảnh Hồ Viên này là khu dân cư cũ mà xem thường, môi trường ở đây trong lành và tốt lắm đấy!

Xung quanh quán ăn, siêu thị tiện lợi cái gì cũng có đủ cả, trạm xe buýt thì nằm ngay trước cổng khu nhà……

Giá 600 tệ một tháng là anh đã vớ bẫm món hời to rồi đấy nhé.

Cũng là do nhà tôi không thiếu thốn tiền bạc gì cho cam, chứ nếu không thì với giá 600 tệ đố anh tìm đâu ra được căn nhà ngon nghẻ thế này để mà thuê?"

"Đúng thế đúng thế, thật sự cảm ơn chị Trần đã chiếu cố giúp đỡ tôi rất nhiều." Người đàn ông trung niên nở nụ cười chất phác xoa tay đáp lại.

Chị Trần suy nghĩ một lát rồi lại lên tiếng dặn dò kỹ càng: "Anh bảo anh chỉ ở có một mình, đàn ông con trai ở một mình thì nhớ phải giữ gìn nhà cửa cho thật sạch sẽ gọn gàng đấy nhé.

Tôi là thấy anh ăn mặc tươm tất sạch sẽ nên mới đồng ý cho anh thuê đấy chứ……"

"À đúng rồi, khu dân cư của chúng tôi ở đây bà con chòm xóm ai nấy đều quen biết mặt nhau cả, anh tuyệt đối không được dẫn mấy thành phần lộn xộn linh tinh về nhà tụ tập đâu đấy nhé."

"Còn nữa, lúc tắm rửa nhớ dùng chậu hứng nước cẩn thận, nhà chung cư cũ đường ống hơi có hiện tượng thấm nước một chút."

"Ở tầng dưới có một đứa nhỏ chuẩn bị thi đại học đấy, đừng có ở trong nhà làm ầm ĩ phát ra tiếng động quá lớn, tường nhà cũ cách âm hơi kém……"

"Ngoài ra, sau này nếu như nhà chúng tôi muốn dọn về đây ở lại thì anh bắt buộc phải chuyển đi nơi khác ngay đấy nhé……"

Người phụ nữ liên tục dặn dò nhắc nhở một hồi dông dài, người đàn ông đối diện cũng không hề tỏ ra chút khó chịu hay thiếu kiên nhẫn nào, suốt từ đầu đến cuối chỉ luôn nở nụ cười chất phác gật đầu lia lịa.

Người phụ nữ thấy thái độ của anh ta thành thật hiền lành như vậy trong lòng cũng cảm thấy an tâm và tin tưởng hơn rất nhiều, cuối cùng bà rút chùm chìa khóa đưa tận tay cho đối phương: "Trong nhà không bẩn thỉu lắm đâu, thỉnh thoảng tôi vẫn ghé qua đây dọn dẹp quét tước.

Đồ đạc cơ bản đều có sẵn cả rồi, anh chỉ cần mua sắm thêm một ít đồ dùng sinh hoạt cá nhân nữa là ở được."

"Vâng ạ, cảm ơn chị nhiều lắm."

"Đừng khách sáo, thôi tôi xin phép về trước đây."

Chị Trần cũng không nán lại lâu làm gì, đợi sau khi bóng dáng bà bước ra khỏi cửa, người đàn ông trung niên liền nhanh chóng đóng sập cánh cửa sắt lại, kế đó khẽ thở phào ra một hơi nhẹ nhõm, lẩm bẩm trong miệng: "Những khu dân cư cũ kỹ tồi tàn như thế này, chắc hẳn là không có gắn camera giám sát đâu nhỉ?"

Tự thì thào một câu, người đàn ông chậm rãi cất bước đi ra mép ban công, đưa mắt nhìn ngó ra khung cảnh bên ngoài một lát, đứng chôn chân tại chỗ nhíu chặt đôi lông mày, trầm giọng nói nhỏ: "Chẳng biết đám người bên phía chính quyền Dương Thành liệu có lần mò phát hiện ra được những manh mối mà mình cố tình để lại hay không nữa……"

Việc cố tình dẫn dụ tai mắt của lực lượng chức năng Dương Thành hướng về phía dãy núi Thương Sơn, khiến cho bọn chúng lầm tưởng rằng hắn đã vượt qua Thương Sơn để trốn thoát sang tỉnh bạn, hắn tính toán rằng một khi nghi phạm đã chạy ra khỏi phạm vi địa giới quản lý của mình thì phía Dương Thành cũng sẽ chẳng còn mấy mặn mà hay dốc toàn lực ra truy bắt nữa.

Trong đầu âm thầm tính toán những mưu mô này, người đàn ông khẽ đưa tay lên xoa xoa hai bên thái dương. Mấy con tôm con tép quèn ở cái huyện thành Dương Thành nhỏ bé này hắn thực chất căn bản chẳng thèm để vào mắt.

Dẫu cho có bị bọn chúng phát hiện ra tung tích đi chăng nữa thì cũng chẳng có gì ghê gớm to tát.

Thế nhưng điều khiến hắn sợ hãi nhất chính là tiếng động quá lớn sẽ kinh động và thu hút sự chú ý của các cấp lãnh đạo cấp cao bên trên.

Với chút thực lực ít ỏi này của hắn, ở những vùng đất hẻo lánh nhỏ bé như Dương Thành thì còn có thể ra oai xưng hùng xưng bá được, chứ một khi đã lọt vào tầm ngắm của các đại đô thị lớn thì có chết cũng chẳng biết vì sao mình chết.

Nghĩ tới đây, người đàn ông cũng thở dài một hơi đầy bất đắc dĩ: Vẫn bắt buộc phải tìm mọi cách để vượt biên trốn ra nước ngoài mới được. Chạy trốn sang mấy quốc gia nhỏ bé hỗn loạn vô chính phủ, dẫu sao vẫn an toàn và dễ thở hơn là ngày ngày phải sống trong cảnh nơm nớp lo sợ ở Hoa Quốc.

Hoa Quốc tuy rằng vô cùng rộng lớn mênh mông, thế nhưng đôi khi đối với những kẻ đào tẩu như hắn lại chật hẹp và ngột ngạt tới cùng cực.

Thời buổi ngày nay hệ thống camera giám sát được lắp đặt dày đặc khắp nơi, trừ phi chui rúc vào tận hang cùng ngõ hẻm nơi thâm sơn cùng cốc hẻo lánh, nếu không thì một kẻ mang thân phận như hắn rất khó để không bị phát hiện hành tung.

Thế nhưng nếu thực sự phải chui rúc sống đời người rừng nơi rừng sâu núi thẳm thì chuyện ăn uống đại tiểu tiện sinh hoạt hàng ngày đều là cả một vấn đề nan giải lớn, võ giả rốt cuộc cũng đâu phải là thần tiên mà có thể nhịn ăn nhịn uống sống qua ngày được.

Chưa kể ở những vùng thôn quê hẻo lánh làng trên xóm dưới ai nấy đều quen mặt biết tên nhau cả, bỗng nhiên lòi ra một người lạ mặt xuất hiện thì dấu vết để lại lại càng thêm lộ liễu rõ ràng.

Thở hắt ra một ngụm trọc khí nặng nề, hắn quyết định không nghĩ ngợi nhiều nữa. Ở Dương Thành căn bản chẳng có nhân vật nào đủ sức tạo ra sự uy hiếp đối với hắn, cứ tạm thời ẩn nấp an toàn ở nơi này một thời gian ngắn rồi tính tiếp.

Đợi đến khi tu vi võ đạo đột phá thành công, móc nối được đường dây buôn lậu vượt biên an toàn thì sẽ lập tức tìm cách rời khỏi lãnh thổ Hoa Quốc ngay lập tức.

Cái loại khu dân cư cũ kỹ tồi tàn này đến cả ban quản lý tòa nhà còn chẳng thèm có, chắc chắn sẽ chẳng có ai rảnh rỗi mà để ý chú ý tới sự hiện diện của một người thuê nhà như hắn.

Xung quanh quán xá ăn uống, tiệm tạp hóa tiện lợi đều đầy đủ cả, sinh hoạt vô cùng thuận tiện, sẽ không để lại quá nhiều dấu vết đáng ngờ.

Sau khi cẩn thận rà soát lại toàn bộ kế hoạch một lượt, cảm thấy không còn bất kỳ sơ hở nào nữa, người đàn ông bấy giờ mới thở phào nhẹ nhõm một hơi.

Thế nhưng sâu thẳm trong lòng hắn lại ngấm ngầm dâng lên một cỗ cảm giác hối hận khôn nguôi: Biết thế ngày xưa mình đã không dại dột làm ra chuyện phạm pháp đó.

Nếu như không phải vì một phút hồ đồ mù quáng, thì chỉ cần cắn răng kiên nhẫn chờ đợi thêm vài năm nữa, bản thân hắn cũng có thể tự mình gom góp đủ số tài nguyên cần thiết để đột phá.

Thế nhưng con đường võ đạo của võ giả vốn dĩ là tranh từng tấc từng khắc, bản thân hắn tuổi tác nay đã ngoài bốn mươi rồi, nếu còn chần chừ đợi thêm vài năm nữa thì làm sao còn cơ hội để tiếp tục bước đi trên con đường võ đạo được nữa chứ.

Tuổi tác ngày càng già đi, khí huyết trong cơ thể đã bắt đầu có dấu hiệu tụt dốc suy thoái, điều đó làm sao không khiến cho hắn phải sốt ruột như lửa đốt trong lòng cho được.

Rốt cuộc vẫn là do tâm lý không cam lòng mà ra cả thôi!

……

Trường Số 1.

Suốt gần hai tiếng đồng hồ trôi qua, buổi hướng dẫn chỉ điểm trước kỳ thi võ khoa rốt cuộc cũng khép lại tốt đẹp trong những tràng pháo tay giòn giã vang dội khắp hội trường.

Phương Bình vốn dĩ còn muốn nán lại bước tới chào hỏi Vương Kim Dương một câu, thế nhưng nhìn thấy cảnh tượng đối phương đang bị hàng trăm học sinh vây kín mít như kiến cỏ, Phương Bình liền lập tức từ bỏ ngay ý định đó.

Buổi hướng dẫn kết thúc, đám học sinh bọn họ cũng không cần phải quay trở lại lớp học làm gì nữa, được phép trực tiếp đi thẳng về nhà.

Chào hỏi nhóm người Ngô Chí Hào vài câu, Phương Bình đang định quay người cất bước rời đi thì Ngô Chí Hào bỗng nhiên bước tới, vẻ mặt tràn đầy tha thiết mong mỏi cất tiếng: "Phương Bình ơi, tối nay qua nhà tớ chơi nhé?"

Mặt Phương Bình lập tức đen thui như đít nồi: Cái câu này nếu như để cho một người phụ nữ xinh đẹp như hoa thốt ra thì hoàn toàn không có vấn đề gì, đằng này cậu là một thằng đàn ông to xác, mở mồm ra rủ rê như thế rốt cuộc là có ý đồ đen tối gì đây hả?

Ngô Chí Hào hoàn toàn không nhận thức được sự biến đổi sắc mặt kỳ dị của Phương Bình, trên mặt vẫn nở nụ cười tươi rói nói tiếp: "Cậu chẳng lẽ không cảm thấy tò mò muốn biết rốt cuộc khí huyết thực tế của mình đạt được bao nhiêu cal sao?

Anh Vương đã khẳng định là cậu tràn trề hy vọng thi đỗ võ khoa rồi, khí huyết chắc chắn đã tăng lên không hề thấp đâu, hay là cậu qua nhà tớ đo kiểm tra lại thêm một lần nữa xem sao?"

Phương Bình thở phào nhẹ nhõm một hơi: Mẹ kiếp, cậu nói trọn vẹn một câu ngay từ đầu có được không hả!

Người ngoài không biết chuyện mà nghe thấy nửa câu đầu của cậu thì khéo lại tưởng hai thằng đàn ông chúng mình có mối quan hệ mờ ám bất chính gì với nhau ấy chứ.

"Thôi bỏ đi cậu ơi, không dám làm phiền gia đình cậu nữa đâu."

"Phiền phức cái gì mà phiền phức, Phương Bình, cứ qua đi mà!"

"Thật sự không cần đâu, tối nay tớ còn có chút chuyện gia đình phải giải quyết, để hôm nào có dịp thuận tiện thì tớ qua sau vậy."

Phương Bình căn bản chẳng dại gì mà đi kích thích tâm lý của tên này. Lòng ghen tị có thể khiến cho con người ta phát điên lên đấy chứ chẳng đùa. Hiện tại Ngô Chí Hào chưa nắm rõ khí huyết thực tế của hắn là bao nhiêu thì tâm lý vẫn còn giữ được sự bình tĩnh; nếu như bây giờ để cho cậu ta biết được khí huyết của Phương Bình đã chạm tới mốc 120 cal rồi thì e rằng cậu ta sẽ hoàn toàn phát điên và sụp đổ tâm lý mất.

Ngô Chí Hào tính tình nhìn chung cũng rất tốt và biết cư xử, lỡ như bị hắn đả kích cho tinh thần suy sụp một đi không trở lại thì đúng là tội lỗi ngập đầu.

Thấy thái độ của Phương Bình vô cùng kiên quyết chối từ, Ngô Chí Hào tuy rằng trong lòng vẫn vô cùng khao khát muốn biết được con số khí huyết thực tế của bạn mình, thế nhưng lúc này cũng đành ngậm ngùi từ bỏ ý định.

Cất tiếng chào hỏi thêm mấy người bạn cùng lớp vài câu nữa, Phương Bình liền đi thẳng ra khỏi cổng trường, rảo bước đi bộ về nhà.

……

Không lâu sau khi Phương Bình rời khỏi trường, Vương Kim Dương cũng khéo léo từ chối lời mời cơm tối thịnh tình từ phía ban giám hiệu nhà trường.

Đối với Vương Kim Dương mà nói, việc ghé qua Trường Số 1 này thực chất chỉ là một chuyến đi tiện đường ghé thăm mà thôi.

Tiện tay làm một món ân tình thuận nước đẩy thuyền, nhân tiện kiếm thêm một khoản thù lao nho nhỏ cho vào túi, vừa có tiếng lại vừa có miếng.

Thế nhưng món tiền béo bở thực sự lại nằm ở bên phía Cục Trinh Sát Dương Thành kia. 50 vạn tệ tuy đối với các đại đô thị không phải là số tiền quá mức kinh khủng, thế nhưng đối với một huyện thành nhỏ bé như Dương Thành thì 50 vạn tệ đã là một khoản ngân sách khổng lồ rồi.

Hơn nữa nhiệm vụ ở các thành phố nhỏ thông thường cũng dễ giải quyết hơn, mức độ rủi ro nguy hiểm không quá cao, nếu như mọi chuyện diễn ra suôn sẻ thuận lợi thì rất nhanh chóng là có thể hoàn thành xong xuôi.

Xách theo chiếc ba lô căng phồng bước chân ra khỏi cổng trường, chỉ một lát sau, một chiếc xe ô tô Volkswagen màu đen bóng loáng đã từ từ tấp vào lề đường đỗ ngay trước mặt Vương Kim Dương.

Vương Kim Dương mở cửa bước thẳng lên xe ngồi xuống ghế sau, vừa yên vị liền cất tiếng hỏi ngay: "Trong hồ sơ báo cáo nói rằng nghi phạm đã trốn vào trong Thương Sơn, ban ngày ở Thương Sơn vẫn có một số du khách rảnh rỗi lui tới tham quan, đối phương chắc chắn sẽ không dám manh động vào ban ngày. Nói cách khác, hiện tại hắn ta vẫn còn đang lẩn trốn trong phạm vi địa giới của huyện Dương Thành chúng ta đúng không?"

Người tài xế đang cầm lái nghe vậy liền vội vàng đáp lời: "Vương tiên sinh, ngài phán đoán hoàn toàn chính xác ạ! Đối phương chắc chắn vẫn đang nằm trong phạm vi kiểm soát của Dương Thành chúng ta.

Nếu như hắn ta thực sự trốn thoát ra khỏi địa phận Dương Thành thì bên phía chúng tôi chắc chắn đã nhận được tin báo rồi.

Cục trưởng đã căn dặn rồi ạ: Nếu như đối phương thực sự vượt qua Thương Sơn chạy sang tỉnh khác thì chúng tôi sẽ kịp thời thông báo cho ngài, đến lúc đó ngài không cần phải tiếp tục đuổi theo nữa đâu ạ."

Vương Kim Dương khẽ nhíu mày lại. Tên tội phạm một khi đã chạy thoát ra khỏi địa bàn Dương Thành thì các cơ quan chức năng ở đây dẫu có muốn lập công chuộc tội đi chăng nữa cũng không thể nào vượt quyền sang địa phương khác để thi hành công vụ được.

Bảo không cần đuổi theo nữa đâu có nghĩa là nhiệm vụ đã hoàn thành, mà đồng nghĩa với việc nhiệm vụ lần này coi như kết thúc trong thất bại.

Mà theo cái tính cách kẹo kéo thực dụng của đám người bên Cục Trinh Sát này thì người không bắt được dĩ nhiên tiền thưởng cũng sẽ tan thành mây khói, bố thí cho vài đồng bạc lẻ gọi là tiền xăng xe lộ phí đã là may mắn lắm rồi.

Suy nghĩ một lát, Vương Kim Dương lại cất tiếng hỏi: "Đối phương đã lẩn trốn cư trú ở Dương Thành suốt một khoảng thời gian dài như vậy rồi, bên phía các ông chưa từng có một lần nào trực tiếp tiếp xúc với hắn sao?"

Người tài xế cười gượng gạo đáp: "Dạ thưa ngài, đối phương hành tung vô cùng cảnh giác và giảo hoạt ạ……"

"Vị Cục trưởng của các ông, ngay cả một lần thăm dò thực lực cũng không dám làm sao?"

"Dạ chuyện này……"

Vương Kim Dương bĩu môi khinh bỉ một cái, mấy cái lão cáo già sống lâu năm này ai nấy đều quý tính mạng như vàng như ngọc, làm sao dám liều lĩnh tùy tiện đi thăm dò nguy hiểm.

"Đối phương thật sự là võ giả Nhị phẩm chứ?"

"Dạ chuyện này……"

Người tài xế có chút ngượng ngùng lúng túng, từ gương chiếu hậu nhìn thấy sắc mặt Vương Kim Dương càng lúc càng trở nên lạnh lẽo khó coi, bèn vội vàng cất giọng khẳng định chắc nịch: "Là Nhị phẩm ạ! Chuyện này tuyệt đối là sự thật một trăm phần trăm!

Tên này trước đây từng gây ra vài vụ án cướp bóc ở các địa phương khác, tất cả các vụ án đó đều là nhằm mục đích cướp đoạt các nguồn tài nguyên phục vụ cho việc đột phá cảnh giới tu vi.

Thế nhưng theo như tình hình điều tra hiện tại thì dường như hắn ta vẫn chưa gom góp đủ số lượng tài nguyên cần thiết.

Cho dù tài nguyên có gom đủ đi chăng nữa thì hắn cũng hoàn toàn không có đủ thời gian và không gian an toàn để tiến hành đột phá đâu ạ. Trong suốt những ngày hắn ẩn nấp ở Dương Thành này chúng tôi vẫn luôn cử người theo dõi sát sao từ xa.

Mọi thứ vẫn diễn ra hoàn toàn bình thường, nếu như hắn thực sự tiến hành bế quan đột phá thì chúng tôi chắc chắn sẽ phát hiện ra ngay lập tức."

Lời giải thích này nghe qua quả thực rất hợp lý và không có vấn đề gì đáng ngờ cả. Quá trình đột phá cảnh giới của võ giả đâu phải là chuyện chớp mắt một cái là có thể hoàn thành xong ngay được.

Khẽ gật đầu đồng ý, Vương Kim Dương không tiếp tục lên tiếng nói thêm câu nào nữa.

Đợi đến khi nhiệm vụ lần này được giải quyết êm đẹp, nhận được trọn vẹn 50 vạn tệ tiền thưởng từ Cục Trinh Sát, cộng thêm 6 vạn tệ thù lao từ phía Trường Số 1 chi trả, thì trong tay anh ngót nghét cũng đã có được gần 200 vạn tệ tiền vốn tích lũy rồi.

Xin thêm một phần hỗ trợ tài nguyên từ phía nhà trường nữa là vừa vặn đủ cho nhu cầu đột phá cảnh giới sắp tới của bản thân.

Nhớ lại thời điểm cách đây tròn một năm trước, bản thân anh đến một viên Bổ Huyết Hoàn trị giá vài ngàn tệ cũng không có đủ tiền mà mua.

Thế mà giờ đây, số tiền tiết kiệm trong tay đã được tính bằng con số hàng trăm vạn tệ rồi, vậy mà vẫn cảm thấy thiếu thốn và không đủ để chi dùng.

Người bình thường ngoài xã hội e rằng không thể nào tưởng tượng nổi việc chỉ trong vòng một năm ngắn ngủi anh lại có thể kiếm được một khoản tiền khổng lồ đến nhường này.

Vương Kim Dương nghĩ tới đây lại khẽ nở nụ cười tự giễu chính mình: Kiếm được nhiều tiền đến mấy thì cũng chẳng bao giờ là đủ để tiêu xài cho con đường võ đạo.

Đối với võ giả mà nói, trừ phi là những vị cường giả cao phẩm đứng đầu mở đại công ty kinh doanh kiếm tiền tấn tiền tạ, chứ nếu không dẫu cho có là người làm việc trong bộ máy chính quyền đi chăng nữa thì nguồn tài nguyên được nhà nước cung cấp cũng vô cùng eo hẹp có hạn.

Một sinh viên nghèo như anh có thể kiếm tiền nhanh chóng đến mức độ này đã là một kỳ tích vô cùng hiếm thấy trong giới rồi.

Có rất nhiều võ giả không có quan hệ, không có môn lộ kiếm tiền, những người tốt nghiệp từ các trường đại học võ thuật chính quy thì còn đỡ khổ, chứ những võ giả xuất thân từ các lớp bồi dưỡng võ đạo tự do ngoài xã hội thì cuộc đời mới thực sự là thê thảm cùng cực.

Rất nhiều người trong số họ thường thường cả đời này đều bị mắc kẹt vĩnh viễn ở cảnh giới Nhất phẩm, không cách nào tiến thêm được nửa bước.

Giống như cái gã nghi phạm trong vụ án lần này chẳng hạn: Nếu đổi thành sinh viên hay cựu sinh viên của các trường võ đại danh giá, thì chỉ vì vài trăm vạn tệ tài nguyên tu luyện ai rảnh rỗi điên rồ mà mang cả tính mạng và danh dự ra mạo hiểm phạm pháp làm liều?

Thế nhưng gã kia cuối cùng vẫn không nhịn được mà ra tay hạ sát cướp đoạt, từ đó có thể thấy rõ ràng có những võ giả cuộc sống thực tế hoàn toàn không hề hào nhoáng rực rỡ như người ngoài vẫn hằng lầm tưởng.

Hy vọng sau đợt đột phá cảnh giới lần này, bản thân mình có thể tìm kiếm được những mối làm ăn kiếm được nhiều tiền hơn nữa.

Biết đâu chừng, chạy đến một vài doanh nghiệp nhỏ để treo tên làm chức danh cố vấn pháp nhân cũng là một ý kiến không tồi?

Thế nhưng suy đi tính lại một hồi, Vương Kim Dương vẫn quyết định gạt bỏ ý nghĩ đó ra khỏi đầu: Treo tên làm pháp nhân ở các công ty nhỏ tuy việc làm không nhiều, thế nhưng thường xuyên phải đích thân đứng ra mặt giải quyết những rắc rối linh tinh vụn vặt vô cùng phiền toái.

Số lần phải ra mặt giải quyết quá nhiều thì chi bằng tự mình nhận lấy một vài nhiệm vụ truy bắt như thế này còn kiếm được nhiều tiền hơn mà lại nhanh gọn dứt khoát.

Đó cũng chính là lý do vì sao rất hiếm khi có võ giả thực thụ nào chịu hạ mình đi treo tên làm người đại diện pháp luật cho các doanh nghiệp nhỏ: Quá mức phiền toái và chẳng bõ công sức bỏ ra.

Những kẻ sẵn sàng đi treo tên làm pháp nhân đại đa số đều là những võ giả nhàn rỗi lang bạt ngoài xã hội mà thôi.

Thế nhưng cũng đâu phải ai muốn đi treo tên là cũng được: Các doanh nghiệp vẫn luôn có xu hướng muốn tìm những người có lý lịch trong sạch, những sinh viên tốt nghiệp từ các trường đại học võ thuật danh giá về nắm giữ vị trí này hơn.

Rốt cuộc theo như quy định của pháp luật, toàn bộ tài sản của doanh nghiệp đều thuộc về quyền sở hữu của người đại diện pháp luật.

Nếu như gặp phải kẻ có nhân phẩm tồi tệ, sau khi treo tên xong mà đối phương nảy lòng tham nuốt trọn luôn cả công ty của bạn thì bạn cũng chỉ biết ngậm đắng nuốt cay mà không thể thốt lên lời nào.

Đó cũng chính là nguyên nhân sâu xa khiến cho đám võ giả tự do ngoài xã hội có cuộc sống vô cùng thê thảm bế tắc: Trừ phi tự mình đứng ra thành lập công ty, nếu không thì các doanh nghiệp nhỏ bên ngoài cũng chẳng có ai đủ gan to mà dám thuê mướn bọn họ về làm người đại diện pháp nhân cả.

Trong lúc Vương Kim Dương còn đang trầm ngâm suy nghĩ miên man trong đầu, chiếc xe ô tô màu đen đã nhanh chóng tăng tốc lao vút về phía dãy núi Thương Sơn mịt mờ sương khói."""
    }
}

def main():
    conn = sqlite3.connect("data/novels.db")
    cur = conn.cursor()
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    total_vi_chars = 0
    total_raw_chars = 0
    
    print("=" * 60)
    print("BẮT ĐẦU CẬP NHẬT PHƯƠNG ÁN B - BATCH 4 (CHƯƠNG 16 - 20)")
    print("=" * 60)
    
    for ch_idx, data in CHAPTERS_DATA_VERBATIM.items():
        url = data["url"]
        title_vi = data["title_vi"]
        content_vi = data["content_vi"].strip()
        
        # Scrape 100% authentic raw Chinese text from Piaotia
        print(f"\n[+] Đang tải raw tiếng Trung chương {ch_idx}: {url}...")
        raw_title, raw_content = clean_piaotia(url)
        
        len_raw = len(raw_content)
        len_vi = len(content_vi)
        total_raw_chars += len_raw
        total_vi_chars += len_vi
        
        print(f"    - Tiêu đề gốc: {raw_title}")
        print(f"    - Tiêu đề dịch: {title_vi}")
        print(f"    - Độ dài raw Trung: {len_raw:,} ký tự")
        print(f"    - Độ dài dịch Việt: {len_vi:,} ký tự")
        
        cur.execute("""
            UPDATE chapters
            SET title = ?,
                title_translated = ?,
                source_url = ?,
                raw_content = ?,
                translated_content = ?,
                translation_status = 'completed',
                updated_at = ?
            WHERE novel_id = ? AND chapter_index = ?
        """, (
            raw_title,
            title_vi,
            url,
            raw_content,
            content_vi,
            now,
            NOVEL_ID,
            ch_idx
        ))
        
    conn.commit()
    # Checkpoint WAL
    cur.execute("PRAGMA wal_checkpoint(FULL);")
    conn.close()
    
    print("\n" + "=" * 60)
    print(f"HOÀN TẤT BATCH 4! Tổng raw: {total_raw_chars:,} ký tự | Tổng dịch: {total_vi_chars:,} ký tự")
    print("=" * 60)

if __name__ == "__main__":
    main()
