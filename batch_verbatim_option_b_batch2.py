# -*- coding: utf-8 -*-
"""
DỊCH THEO PHƯƠNG ÁN B (VERBATIM 100% NGUYÊN VĂN TỪNG CÂU TỪNG CHỮ)
Tác phẩm: Toàn Cầu Cao Võ (全球高武) - Lão Ưng Cật Tiểu Kê (老鹰吃小鸡)
Lưu toàn văn 100% nguyên bản chữ Hán từ Piaotia vào raw_content.
Bản dịch tiếng Việt văn phong cao võ trau chuốt, đầy đủ từng câu độc thoại, suy nghĩ và hội thoại.
Batch 2: Chương 6 đến Chương 10.
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
    6: {
        "url": "https://www.piaotia.com/html/9/9640/6523760.html",
        "title_vi": "Chương 6: Sự Nghèo Đói Đã Hạn Chế Trí Tưởng Tượng Của Tôi",
        "content_vi": """Cảnh Hồ Viên.

Tòa 6 phòng 101.

Phương Bình vừa về đến nhà, liền tự nhốt mình vào trong căn phòng nhỏ riêng của mình.

Ngoài cửa, Phương Viên đập cửa "rầm rầm" mấy bận, đều bị Phương Bình cự tuyệt ngoài cửa, tức giận đến mức Phương Viên hận không thể phá cửa xông vào.

Lúc này Phương Bình chẳng có tâm trí đâu mà để ý Phương Viên có tức giận hay không.

Khoảnh khắc rút tiền ở cây ATM kia, nếu không phải có vài chỗ chưa tìm hiểu rõ ràng, Phương Bình đã sớm tìm chỗ để nghiên cứu rồi.

……

Trong căn phòng nhỏ.

1 vạn tệ vừa rút về được Phương Bình đặt ở bên tay trái, bên tay phải thì đặt một tờ 10 tệ, đây cũng chính là toàn bộ tổng tài sản của Phương Bình.

Sắc mặt Phương Bình đã khôi phục bình thường, nhưng trên mặt vẫn còn mang theo vài phần nghi hoặc.

Ngay tại khoảnh khắc rút tiền từ cây ATM kia, Phương Bình vừa cầm 2000 tệ tới tay, bỗng nhiên trước mắt hoa lên, giống hệt như triệu chứng ruồi bay trước mắt, trong tầm mắt đột ngột xuất hiện thêm một chút đồ vật.

Lúc đó hắn ngẩn người chính là vì nguyên nhân này.

Khác với triệu chứng ruồi bay mơ hồ không rõ, thứ đột nhiên xuất hiện trong tầm mắt hắn là mấy dòng chữ nhỏ rõ ràng.

Phương Bình còn nhớ, lúc đó xuất hiện là ba dòng chữ nhỏ:

Tài phú: 2000

Khí huyết: 1

Tinh thần: 1

Mấy dòng chữ vô cùng đơn giản, mấy từ ngữ cũng rất dễ hiểu, điều đầu tiên Phương Bình nghĩ đến chính là hệ thống.

Đối với những thứ này, Phương Bình chẳng hề xa lạ, chưa từng ăn thịt heo thì cũng từng thấy heo chạy.

Nhưng Phương Bình lại phát hiện, thứ xuất hiện trước mắt mình quá mức sơ sài!

Chỉ có mấy dòng chữ như vậy, không giải thích, không hướng dẫn, thời buổi này, hệ thống đến cả sách hướng dẫn sử dụng cũng không phát kèm sao?

Hay là nói, cái thứ này chỉ là một món hàng thứ phẩm kém chất lượng được sản xuất trên dây chuyền công nghiệp?

Hơn nữa nó xuất hiện quá mức đột ngột, Phương Bình hoàn toàn không có chút chuẩn bị nào.

Nếu như nói, ngày hôm qua lúc tỉnh lại trong lớp học mà thứ này xuất hiện, Phương Bình còn có thể thản nhiên đón nhận không chút nghi ngờ, đằng này đều đã qua hẳn một ngày rồi, sao lại đột nhiên nhảy ra thế này?

Liên tưởng tới con số Tài phú 2000, Phương Bình lúc đó liền đại khái hiểu rõ một số tình hình.

Để xác định xem con số này có phải liên quan đến tiền bạc hay không, Phương Bình đã ngay tại chỗ làm một vài thí nghiệm.

Kết quả cũng không ngoài dự liệu của hắn, theo từng đợt tiền được rút ra, trị số tài phú trong tầm mắt hắn quả nhiên không ngừng tăng lên.

Lần này, Phương Bình coi như đã hiểu được hàm nghĩa đại biểu của tài phú.

Thế nhưng sau nhiều lần thử nghiệm, Phương Bình vẫn có vài điểm không cách nào hiểu nổi.

Tỷ như điểm thứ nhất, ngày hôm qua trên người hắn cũng có 28 tệ, bây giờ còn lại 10 tệ.

Nhưng vì sao ngày hôm qua lại không xuất hiện tình huống này?

Nghĩ ngợi hồi lâu, cộng thêm trên tay mình còn sót lại 10 tệ không hề được thống kê vào trong tài phú, trong lòng Phương Bình rốt cuộc có chút hiểu ra.

Nói một cách đơn giản — hắn quá nghèo!

Cái hệ thống theo định nghĩa của mình có lẽ là một kẻ có tiền, dưới 100 tệ thì căn bản không thèm thống kê, nếu đổi thành người trọng sinh nào có tài sản vượt quá 100 tệ, e rằng hôm qua đã sớm phát giác ra rồi.

Nhưng Phương Bình nghèo rớt mồng tơi mà!

Nếu không phải bởi vì báo danh võ khoa cần rút tiền nộp lệ phí, với tình hình hiện tại của hắn, xác suất cha mẹ cho một lần 100 tệ là không lớn, rất có thể trong một khoảng thời gian dài Phương Bình sẽ chẳng thể phát hiện ra cái thứ này.

Ngày hôm qua Phương Bình còn oán trách ông trời không có mắt, hại kẻ trọng sinh như mình lưu lạc thê thảm.

Giờ nhìn lại, xem ra là trách oan ông trời rồi, mấu chốt là do hắn là một tên nghèo kiết xác.

"Nghèo đói quả nhiên là nguyên tội!"

Đại thể nghĩ thông suốt điểm này, Phương Bình vô cùng cảm thán, thời buổi này, ngay cả ông trời cũng coi thường kẻ nghèo hèn.

Có nghĩ tới cảm nhận của mình hay không chứ?

Lỡ như cứ mãi không có cơ hội kiếm được 100 tệ, chẳng phải là uổng phí cái hệ thống này sao?

Dĩ nhiên, khả năng này cũng không lớn cho lắm.

Đây mới chỉ là điểm nghi hoặc thứ nhất.

Điểm thứ hai, theo quá trình rút tiền của Phương Bình, hắn lại phát hiện ra một số điểm khác biệt.

Khi trị số tài phú của hắn tăng lên đến 10.000, sau đó, Phương Bình lại rút thêm một ít tiền trong thẻ ra, nhưng tài phú lại không thèm tăng thêm nữa!

Thử nghiệm nhiều lần, con số tài phú vẫn đóng đinh bất động ở mức 10.000.

Bởi vì chỉ có mấy dòng chữ cộc lốc, trong đầu cũng chẳng đột ngột vang lên thanh âm nào giải thích cho hắn, sách hướng dẫn cũng không có, Phương Bình đành phải tự mình đưa ra một vài phán đoán.

Theo cách hiểu của Phương Bình, 1 vạn tệ rút ra hôm nay, vì là cha mẹ cho hắn dùng để nộp phí báo danh, hẳn là được tính là tiền của chính hắn.

Còn những đồng tiền rút ra sau đó lại là tiền của cha mẹ.

Việc thống kê trị số tài phú này, rất có khả năng là thống kê tài sản thuộc về chính bản thân hắn.

Nếu không, lúc đó Phương Bình đã nghĩ, nếu chỉ cần chạm tay vào tiền một cái là có thể được thống kê vào trong tài phú, vậy thì kế tiếp hắn chẳng cần làm việc gì khác nữa, cứ dứt khoát xin vào ngân hàng làm việc, tìm công việc nào tiếp xúc với tiền mặt là xong.

Cho dù không vào ngân hàng thì trong xã hội những ngành nghề giao dịch tiền mặt còn rất nhiều, có những nghề yêu cầu tiêu chuẩn chẳng cao, hắn hoàn toàn có thể thông qua những công việc này để không ngừng gia tăng trị số tài phú của mình, mặc dù hiện tại hắn vẫn chưa rõ việc tài phú tăng lên rốt cuộc có hiệu quả gì.

Không rõ cũng chẳng sao, Phương Bình biết, khẳng định không phải chuyện xấu là được rồi.

"Tài phú, là thống kê tài sản của chính mình. Mặc dù độ thông minh hơi cao một chút, không tương xứng lắm với cái hệ thống sơ sài tồi tàn này, nhưng thôi đành tạm thời chấp nhận vậy."

Phương Bình tự lẩm bẩm một câu, sau đó lại hơi nhíu mày, thì thào: "Là tiền mặt đơn thuần, hay có thể bao gồm cả những thứ có giá trị tương đương? Ví dụ như vàng bạc châu báu?"

Khi tiền ít, tiền mặt thống kê còn không sao, nhưng nếu tiền nhiều lên, chẳng lẽ tất cả đều phải là tiền mặt?

Hơn nữa, chẳng lẽ mỗi lần tài phú gia tăng, đều phải do chính mình trực tiếp chạm vào mới được?

Nhưng xã hội hiện nay có cổ phiếu, có tiền ảo.

Những thứ này đều là tài sản vô hình, muốn sờ cũng đâu thể sờ được?

Phương Bình cảm thấy có chút tiếc nuối, bởi vì sự hạn chế của nghèo đói dẫn tới việc hắn bây giờ căn bản không thể nào đưa ra phán đoán chính xác.

Nếu như trong tay có chút vàng bạc châu báu thuộc về mình, hay cổ phiếu có giá trị, vậy thì ngược lại có thể làm thí nghiệm một chút, những thứ này chỉ đành để lại đến khi có điều kiện cho phép mới làm tiếp thôi.

"Quả nhiên, sự nghèo đói đã hạn chế trí tưởng tượng của mình..."

Hơi có chút tiếc nuối, nhưng Phương Bình cũng không vội vã đi chứng minh những điều này, sớm muộn gì cũng tới lượt thôi.

Ngoài hai điểm nghi hoặc mà hắn đã đưa ra phán đoán trên, Phương Bình còn suy xét tới một điểm nữa.

Đó chính là việc thống kê tài phú, là tính theo tài sản ròng, hay là cộng dồn cả nợ nần?

Nghe thì có vẻ hơi gượng ép kỳ cục, nhưng điều này lại liên quan trực tiếp đến những hành động tiếp theo mà Phương Bình có thể sẽ làm.

Lần này, 1 vạn tệ này là cha mẹ cho, có thể tính là quà tặng cho đứt, sẽ không đòi lại.

Nhưng rốt cuộc không phải do chính hắn kiếm được. Nếu tiền của mình thì được tính, vậy nếu hắn đi vay mượn tiền người khác, cái đó có được tính là tiền của hắn không?

Lại thêm, 1 vạn tệ này sau khi nộp lệ phí báo danh xong xuôi, trị số tài phú có bị khấu trừ đi không?

Có tiền thì phải tiêu, đây là chuyện tất nhiên.

Nếu như cứ tiêu tiền là trị số tài phú bị trừ đi, vậy nếu Phương Bình muốn tích lũy một lượng lớn tài phú, tiếp theo đây chỉ có thể biến thành một kẻ thủ tài nô ki bo bủn xỉn mà thôi.

Những điều trên, bởi vì điều kiện hạn chế, Phương Bình tạm thời chưa thể có được đáp án chính xác, chỉ đành để lại cho sau này.

Mà điều khiến Phương Bình chú ý nhất vẫn là hai cột Khí huyết và Tinh thần.

Trên thực tế, Phương Bình đã đoán ra được một số điều.

Hai từ "Khí huyết" và "Tinh thần" này, ngày hôm qua lúc lướt mạng hắn nhìn thấy không chỉ một hai lần.

Võ giả hiện đại, tuy số lượng không quá nhiều, nhưng cũng không phải là quá ít.

Thêm vào đó hiện nay thông tin phát triển, trên mạng luôn có những thứ được lưu truyền rò rỉ ra ngoài.

Dù là đại chúng bình dân cũng đều có chút hiểu biết: Khí huyết và Tinh thần chính là căn bản của võ giả.

Võ giả cấp thấp ít khi bàn tới tinh thần, không quá chú trọng.

Mà một số luận điểm trên mạng lại cho rằng, võ giả cao đoạn, đặc biệt là những cường giả cấp bậc Tông sư, sự chênh lệch chủ yếu giữa họ và võ giả tầng dưới chính là ở tinh thần.

Nhưng khoảng cách đó còn hơi xa xôi đối với Phương Bình. Đối với võ giả cấp thấp mà nói, chủ yếu vẫn là chú trọng tới khí huyết.

Khí huyết đủ, bách bệnh tiêu trừ!

Ngay cả ở kiếp trước của Phương Bình, khí huyết cũng thường xuyên được nhắc tới. Trung y dưỡng sinh, dưỡng chính là khí huyết.

Người có khí huyết dồi dào, thân thể sẽ khỏe mạnh hơn người khác.

Một số thứ đại bổ, bổ chính là bổ khí huyết.

Đối với võ giả, hoặc những người đang chuẩn bị trở thành võ giả mà nói, người khí huyết dồi dào chưa chắc đã là võ giả, nhưng võ giả nhất định phải có khí huyết dồi dào!

Luyện võ không phải là ngồi đả tọa, so với đạo gia vẫn có sự khác biệt rất lớn.

Võ giả thực chất chính là người bình thường rèn luyện tới cực hạn, đột phá ranh giới thân thể của người bình thường, đó mới là nguồn gốc của võ giả.

Có sự chống đỡ của khí huyết sung túc, thân thể khỏe mạnh, chịu được tiêu hao, đó mới là nền tảng để thân thể trở nên cường đại.

"Nói cách khác, tăng cường khí huyết có thể giúp mình dễ dàng trở thành võ giả hơn.

Sau khi trở thành võ giả, cũng dễ dàng thích ứng với những bài rèn luyện tiếp theo, từng bước một đột phá lên trên..."

Phương Bình lẩm bẩm một câu, lại tự hỏi tự trả lời: "Đã xuất hiện trị số tài phú, khí huyết và tinh thần đều được lượng hóa bằng con số, vậy có phải mang ý nghĩa là có thể dùng trị số tài phú để hoán đổi chuyển hóa?

Tỷ lệ chuyển hóa này rốt cuộc là bao nhiêu?"

Một đổi một, Phương Bình chưa từng nghĩ tới.

Hiện tại, trị số khí huyết và tinh thần của hắn đều là 1.

Nếu như là tỷ lệ một đổi một, chẳng phải chỉ cần 1 đồng tiền là có thể làm cho khí huyết của mình cao gấp đôi người thường sao? Phương Bình đánh chết cũng không tin lại có chuyện dễ dàng như vậy trên đời.

"Vậy thì phải làm thế nào để chuyển hóa?"

Phương Bình nói, có chút bất đắc dĩ: "Dù sao cũng phải cho cuốn sách hướng dẫn chứ, cứ tự mình mò mẫm thế này phiền toái quá."

Lúc này Phương Bình chỉ cần tập trung tinh thần nhìn là có thể thấy mấy dòng số liệu trong tầm mắt mình.

Chằm chằm nhìn vào những con số một hồi, Phương Bình thăm dò mở miệng: "Hệ thống hệ thống, cộng cho tao chút khí huyết xem nào?"

Hoàn toàn không có động tĩnh!

"Hệ thống đại gia, tao dùng tài phú đổi khí huyết được không?"

"..."

"Đại thần, đại gia ơi, còn sống không đấy? Ho một tiếng đi?"

"..."

"Vừng ơi mở ra?"

"..."

"Thỏ con ngoan ngoãn mở cửa ra nào?"

"..."

"Tam Thanh ở trên? Nam mô A Di Đà Phật? Chúa trời phù hộ..."

"Mẹ kiếp nhà mày!"

Thử một hồi lâu, ba dòng con số vẫn sừng sững bất động như bàn thạch, Phương Bình hoàn toàn tuyệt vọng chết tâm, xem ra chẳng liên quan gì tới mấy câu khẩu lệnh này.

Suy nghĩ một chút, Phương Bình lại tập trung ngưng thần nhìn trừng trừng vào mấy dòng số liệu này, muốn xem xem phía sau các con số có dấu cộng "+" nào bị mình bỏ sót hay không.

Đáng tiếc, vẫn không có.

Lần này Phương Bình nhức đầu thật rồi, hoàn toàn không biết dùng thế nào, không lẽ bị hư rồi sao?

Cái thứ quỷ này rốt cuộc có đáng tin cậy hay không vậy?

Trong lòng ngấm ngầm oán trách, mày dứt khoát một lần tới nơi tới chốn luôn có phải tốt không, giờ làm cho người ta lơ lửng dở dở ương ương thế này, có nghĩ tới cảm nhận của tao không hả?

"Cộng chút khí huyết đi, không cộng tao đánh chết mày bây giờ!"

Phương Bình trừng mắt nhìn mấy dòng chữ nhỏ trong tầm mắt, thuận miệng thốt ra một câu. Ai ngờ tiếng nói vừa dứt, con số trước mắt hắn đột nhiên biến đổi!

"Tài phú: 0

Khí huyết: 1.1

Tinh thần: 1

……"

"Đậu xanh rau má!"

Phương Bình lập tức ngây ngốc, còn có cả thao tác kiểu này nữa sao?

Cái thứ của nợ này hóa ra phải dùng đến vũ lực đe dọa mới chịu nghe lời?

Giữa lúc trợn mắt há hốc mồm, thân thể Phương Bình cũng có chút khó chịu mà vặn vẹo uốn éo một phen.

Nhưng rất nhanh, cảm giác khó chịu này liền biến mất.

Phương Bình thở dài ra một hơi thật dài, bỗng nhiên cảm thấy cả người nhẹ nhõm đi rất nhiều.

Nếu muốn nói về cảm nhận, thì giống như người bị bệnh hen suyễn đột nhiên hết thở khò khè, người thiếu máu bỗng nhiên không còn thiếu máu nữa.

Nói lớn hơn một chút thì dường như lực hút của Trái Đất cũng nhỏ đi một chút xíu so với trước kia, mặc dù cảm giác này vô cùng mờ mịt phiêu miêu.

"Thoải mái!"

Mặc dù vẻn vẹn chỉ tăng thêm 0.1 trị số khí huyết mà thôi, nhưng Phương Bình lại cảm thấy sung sướng còn hơn cả đi massage đại bảo kiếm.

Tuy nhiên cảm giác sảng khoái này cũng giống như đàn ông sau khi xong việc vậy, duy trì thời gian không được bao lâu, rất nhanh liền thoái trào tan biến.

Thoái trào thì thoái trào, Phương Bình vẫn lờ mờ phát giác ra được thân thể mình đã khỏe mạnh hơn so với trước kia một chút. Bản thân mình mới là người hiểu rõ cơ thể mình nhất, thân thể trong nháy mắt xuất hiện biến hóa, hắn khẳng định có thể cảm nhận được.

Thế nhưng khi nhìn thấy tài phú biến thành số 0, mày Phương Bình lập tức nhíu chặt lại!

Hắn biết tỷ lệ chuyển hóa khẳng định không cao, nhưng 100.000:1 thì cũng quá hố người rồi đấy chứ!

10.000 điểm tài phú chỉ đổi lấy 0.1 khí huyết gia tăng. Hắn đâu có biến thành siêu nhân, cùng lắm chỉ là khí huyết dồi dào hơn người bình thường một chút mà thôi.

Vậy nếu hắn muốn đạt tới tiêu chuẩn khí huyết của võ giả, thì phải cần bao nhiêu điểm tài phú mới đủ đây?

Nghĩ đến đây, Phương Bình đột nhiên nhìn về phía bàn học, đợi đến khi thấy xấp tiền giấy màu đỏ vẫn còn nguyên vẹn ở đó, Phương Bình mới thở phào một cái nhẹ nhõm, may quá may quá, chưa xuất hiện tình huống tồi tệ nhất.

Nếu như điểm tài phú tiêu hao mà tiền mặt cũng biến mất theo, vậy thì kế tiếp hắn thật sự chẳng biết ăn nói thế nào với cha mẹ.

Thò tay nắm lấy xấp tiền trên bàn vào trong lòng bàn tay, Phương Bình lại một lần nữa rơi vào trầm tư.

Xem ra, kế tiếp hắn phải cố gắng nỗ lực kiếm tiền thật tốt mới được. Rõ ràng, muốn thi đậu võ khoa, trở thành võ giả, thì hiện tại con đường dễ dàng nhất chính là thông qua điểm tài phú để chuyển hóa thành khí huyết.

Huống chi không đề cập tới những thứ này, cho dù có thi đậu đại học võ khoa đi chăng nữa, muốn trở thành võ giả cường đại thì cũng cần tiêu hao vô số tiền của để mua sắm tài nguyên tu luyện.

Nói cách khác, hết thảy mọi thứ đều không thể tách rời khỏi tiền.

"Quả nhiên, người nghèo căn bản không có tư cách trở nên mạnh mẽ, đây là đang ép mình phải nghĩ mọi cách để kiếm tiền mà!\""""
    },
    7: {
        "url": "https://www.piaotia.com/html/9/9640/6523761.html",
        "title_vi": "Chương 7: Năm Cửa Ải Lớn Của Võ Khoa",
        "content_vi": """Phương Bình đầy đầu óc ý niệm kiếm tiền, rất nhanh liền bị hiện thực tàn khốc đánh cho tơi bời.

Vừa bước ra khỏi cửa phòng, Phương Viên đã sớm đứng chờ sẵn ở ngoài cửa.

Nhìn thấy Phương Bình vừa bước ra, Phương Viên lập tức làm ra bộ mặt đau khổ mếu máo: "Đói bụng rồi!"

"Đói bụng thì đi ăn cơm chứ sao?"

Phương Bình nói một cách đương nhiên, còn Phương Viên thì phồng cái má nhỏ phúng phính lên, tức giận nói: "Không có tiền, ở nhà hết cơm nguội rồi.

Hôm kia mẹ đưa 50 tệ, là tiền cơm trưa ba ngày của hai đứa mình.

Bây giờ tiền đều nằm ở chỗ anh, đi đâu mà ăn cơm?"

"Ăn cơm mà cũng cần tiền á?" Phương Bình phảng phất như vừa phải hứng chịu một đòn bạo kích kinh hoàng, khô khốc nói: "Sáng nay em đâu có nói chuyện này?"

Lúc mua xiên nướng cho con nhóc này, nó ăn vui vẻ hớn hở biết bao nhiêu!

Nếu không phải Phương Bình tiếc tiền không nỡ tiêu, thì 10 tệ còn lại cũng đã bị con bé này ăn sạch sành sanh rồi.

Mãi đến tận bây giờ Phương Bình mới biết, hóa ra số tiền đó bao gồm cả tiền cơm trưa ngày hôm nay.

Mấu chốt là, bây giờ trên người hắn chỉ còn đúng 10 tệ, còn 5 tệ của con nhóc này thì nó nhất quyết không chịu đụng tới, chẳng lẽ nó muốn ăn sạch bách túi tiền của hắn sao?

Sự thật cũng chẳng ngoài dự liệu, Phương Viên nói với vẻ đương nhiên: "Ăn cơm dĩ nhiên phải tốn tiền rồi, tiền đều bị anh cầm hết rồi, em lại không phải lo chuyện ăn uống.

Phương Bình, em đói rồi, gần 1 giờ trưa rồi đấy, em muốn ăn cơm!"

"Hơ hơ!"

"Phương Bình, em đói lắm rồi, đói đến mức sắp đi không nổi nữa rồi nè..." Phương Viên xoa xoa cái bụng nhỏ, không ngừng bắt đầu giở trò bán thảm kể khổ.

Phương Bình dở khóc dở cười, đưa tay nhéo nhéo gò má núng nính thịt của cô bé, bất đắc dĩ nói: "Ăn, đi ăn cơm, thảo nào anh cứ tưởng là anh tiêu tiền tiêu vặt của em, hóa ra toàn bộ đều là tiền cơm.

Chính anh còn quên khuấy mất việc này, em ngược lại nhớ rõ ràng gớm nhỉ.

Cái con nhóc thối này, có ai đi tính kế anh trai mình như em không hả?

Những điều kiện hứa hẹn trước đó coi như hủy bỏ hết..."

"Không chịu đâu!" Phương Viên vội vàng lắc đầu nguầy nguậy, vẻ mặt tràn đầy tiếc nuối không nỡ, một hồi lâu sau mới từ trong túi móc ra tờ tiền 5 tệ của mình, lưu luyến không rời nói: "Đưa cho anh này, anh đã nói sau này mua đồ ăn ngon cho em, mua quần áo đẹp, mua máy vi tính... tất cả đều phải giữ lời đấy nhé."

Đùa nghịch với Phương Bình thì đùa thế thôi, nhưng trên thực tế quan hệ giữa Phương Viên và người anh trai này vô cùng tốt đẹp.

Phương Bình đã nói sau này mua đồ ăn ngon, mua quần áo đẹp cho cô bé, tuy hiện tại là chuyện không thể, nhưng cô bé vẫn ôm ấp niềm ao ước Phương Bình sau khi tốt nghiệp đại học sẽ làm được điều đó.

Vì tương lai tươi sáng, Phương Viên quyết định cống hiến toàn bộ tổng tài sản của mình, dù sao sáng nay cô bé cũng đã ăn mất 5 tệ tiền xiên nướng của Phương Bình rồi.

Bàn tính nhỏ của cô bé gảy lách cách vang dội, Phương Bình vừa buồn cười lại vừa có chút bất đắc dĩ.

Trên người không có đồng bạc nào, quả nhiên nói chuyện chẳng thể có chút tự tin khí phách nào.

Nếu không, việc gì phải vì mấy đồng bạc lẻ mà đôi co ầm ĩ với con bé này chứ.

……

Ăn cơm trưa trở về, Phương Bình hoàn toàn rơi vào cảnh phá sản. Nếu như 1 vạn tệ trên người không phải dùng để nộp học phí, thì hắn cũng được coi là một phú hào nho nhỏ rồi.

May mà buổi trưa hai anh em đều ăn cơm phần giá 5 tệ một suất, 10 tệ vừa vặn đủ trả.

Tờ 5 tệ của cô bé, Phương Bình rốt cuộc vẫn không nỡ dùng tới, dù sao cũng đã là học sinh cấp hai rồi, con gái nhỏ cũng không thể không để lại cho nó một chút tiền tiêu vặt phòng thân.

Không có tiền, buổi chiều hai anh em cũng chẳng có tâm trí đâu mà ra ngoài.

Nói một câu thực tế một chút, nếu Phương Bình không mang theo 1 vạn tệ kia ra cửa, lỡ đi giữa đường buồn đi vệ sinh, gặp phải nhà vệ sinh công cộng thu phí khéo hắn còn chẳng có tiền mà bước vào.

Phương Viên còn có bài tập phải làm, biết ông anh trai mình nghèo rớt mồng tơi leng keng cắc keng, cũng không tiếp tục hố anh nữa, ngoan ngoãn trở về phòng làm bài tập.

Còn Phương Bình cũng bước vào phòng mình, bắt đầu vạch ra quy hoạch cho tương lai.

Hiện giờ, trong đầu óc Phương Bình chỉ có hai việc đại sự: Thứ nhất, chuẩn bị thi võ khoa; Thứ hai, kiếm tiền.

Cải thiện điều kiện gia đình thực ra chỉ là thứ yếu, chuyện này tạm thời không cần quá gấp gáp.

Mấu chốt là nếu không có tiền, hắn chưa chắc đã có thể thi đậu võ khoa.

Tuy rằng có cái hệ thống không quá đáng tin cậy kia, Phương Bình cảm thấy cho dù mình không bước chân vào trường đại học võ khoa thì tương lai cũng có thể trở thành võ giả.

Nhưng vấn đề là, võ giả chẳng lẽ chỉ đơn thuần là khí huyết mạnh mẽ thôi sao?

Còn công pháp thì sao?

Rèn luyện thân thể thế nào để đột phá cực hạn?

Đối với những thứ này, Phương Bình dốt đặc cán mai, hoàn toàn mù tịt. Nếu không có sự đào tạo chuyên nghiệp thì trời mới biết bao giờ mới học được những kiến thức này, thi đại học hiển nhiên là con đường tắt nhanh nhất.

Đối với những điều này, tự nhiên vẫn phải làm một số kế hoạch quy hoạch.

……

Buổi chiều hơn 3 giờ, mẹ Lý Ngọc Anh đã đi làm về, thuận tiện mua cả thức ăn cho bữa tối.

Nói là làm nửa ngày, nhưng trên thực tế thời gian làm việc cũng đã ngót nghét gần 8 tiếng đồng hồ, hoàn toàn không hề nhẹ nhàng thoải mái như người ngoài tưởng tượng.

Phương Bình nộp lại thẻ ngân hàng, đồng thời lấy 1 vạn tệ tiền mặt ra cho mẹ xem một chút, Lý Ngọc Anh cũng không thu lại, bảo Phương Bình ngày mai tự mình cầm đi nộp lệ phí báo danh là được.

Có lẽ biết con trai và con gái đều cạn túi rồi, Lý Ngọc Anh lại đưa cho Phương Bình 50 tệ tiền cơm.

Có lẽ lo lắng con gái lại bị con trai lừa gạt, lần này Lý Ngọc Anh đưa riêng cho Phương Viên 20 tệ, cô bé cầm được tiền trong tay, mừng rỡ cười không khép miệng lại được.

Phương Bình rất muốn nói cho mẹ biết: Làm gì có chuyện con lừa gạt con bé đó, con nhóc kia quỷ quyệt tinh ranh thấy mồ, toàn nó gài bẫy hố anh nó thôi!

……

Ngày 7 tháng 4, Thứ Hai.

So với sự hoang mang mờ mịt của ngày hôm kia, hôm nay quay trở lại trường học, Phương Bình đã thản nhiên tự nhiên hơn rất nhiều.

Cậu bạn cùng bàn Trần Phàm đến lớp còn sớm hơn cả Phương Bình.

Lúc Phương Bình tới nơi, xấp đề thi trước mặt Trần Phàm đã làm được một nửa rồi, cũng chẳng biết là sáng sớm nay tới làm hay đã làm từ trước đó một phần.

Trần Phàm không báo danh thi võ khoa, đương nhiên đem trọng tâm đặt toàn bộ lên văn khoa.

Không thi đậu võ khoa, thì thi đậu vào một trường đại học văn khoa danh tiếng, sau khi tốt nghiệp cũng được săn đón hơn hẳn đám sinh viên văn khoa tốt nghiệp từ các trường đại học bình thường.

Thấy Phương Bình đến, Trần Phàm cũng đặt bút xuống, ngẩng đầu nói: "Phương Bình, xấp đề toán hôm kia thầy phát cậu làm xong chưa? Chúng mình đối chiếu đáp án chút đi."

"Hả?"

Phương Bình cười gượng một tiếng, ai mà biết mình đã làm xong hay chưa chứ, hôm kia phát bài, hai ngày nay cái cặp sách hắn còn chưa thèm động tới, ma mới biết trước kia mình đã làm hay chưa.

Trần Phàm thấy bộ dạng đó liền đại khái đoán ra, không khỏi nhíu mày nói: "Phương Bình, kỳ thi đại học chẳng còn bao nhiêu thời gian nữa đâu. Tuy bây giờ chúng mình không còn nhiều tiết học mới, chủ yếu là tự ôn tập, nhưng làm thêm vài câu hỏi, biết đâu thi đại học lại trúng vào thì sao?"

"Đúng đúng đúng, Tiểu Phàm Phàm nói chí phải, mấy hôm nay đầu óc tớ hơi váng vất quay cuồng, lát nữa tớ làm liền."

"Cậu..."

Trần Phàm có chút bất đắc dĩ, không phải vì cách xưng hô của Phương Bình, tên này gọi hắn như thế đâu phải ngày một ngày hai.

Cậu ta chỉ cảm thấy Phương Bình dạo này có chút tự sa ngã buông thả bản thân.

Xã hội này, tuy rằng địa vị của võ giả cao hơn người bình thường một bậc, nhưng người bình thường cũng phân chia tầng lớp giai cấp rạch ròi.

Có tiền, không có tiền, có chút chức quyền nhỏ, làm công ăn lương cho người khác, vào doanh nghiệp lớn làm việc, hay vào nhà máy làm công nhân...

Những cái đó đều là những mức đãi ngộ hoàn toàn khác biệt một trời một vực.

Trường Số 1 là trường cấp ba tốt nhất của Dương Thành, thành tích của Phương Bình ở lớp 12 ban 4 tuy không phải thuộc top đầu xuất sắc, nhưng cũng không hề kém cỏi.

Cố gắng thêm một chút, thi vào một trường đại học trọng điểm vẫn tràn đầy hy vọng.

Vận may bùng nổ thêm một tí, sau khi những học sinh ưu tú nhất rẽ hướng thi võ khoa, thì việc thi vào một trường danh tiếng cũng chưa chắc đã không có cửa.

Nhưng bây giờ nếu từ bỏ, thì đừng nói là trường danh tiếng, ngay cả trường trọng điểm cũng thấy bấp bênh nguy ngập.

Trần Phàm cùng bàn với Phương Bình suốt hai năm trời, hiểu rõ gia cảnh của Phương Bình cũng chẳng khác nhà mình là bao, thậm chí nhà Phương Bình còn khó khăn hơn nhà cậu ta một chút, bởi vì chi phí nuôi hai đứa con dù sao cũng tốn kém hơn nhà chỉ có một con như cậu ta.

Có lòng muốn khuyên bảo thêm vài câu, nhưng lời đến khóe miệng lại nuốt ngược trở vào, dù sao Phương Bình cũng chỉ mới lười biếng hai ngày nay thôi.

Hai người đang nói chuyện thì gã tương lai râu quai nón Dương Kiến ở bàn trước lại quay đầu lại, mặt mày hớn hở toe toét cười nói: "Phương Bình, Trần Phàm, đã xem tin tức chưa?"

Phương Bình đảo trắng mắt, một gã tráng hán thô kệch râu ria xồm xoàm như cậu, lấy đâu ra cái tâm hồn hóng hớt buôn dưa lê dữ vậy trời.

Trần Phàm cũng chẳng buồn tiếp lời, có thời gian rảnh thà giải thêm mấy bài tập, ai rảnh đâu mà xem tin tức.

Dương Kiến cũng chẳng bận tâm tới phản ứng của hai người, cười ha hả nói: "Trên mạng lại có tin tức rò rỉ ra rồi, trận tỉ thí võ thuật giữa Mã Tông Sư và Thần Tượng Taylor, đã được ấn định vào cuối tháng này.

Hơn nữa còn tiết lộ địa điểm quyết đấu, ngay tại Hoa Quốc chúng ta!

Bây giờ rất nhiều phóng viên đã đổ xô kéo tới đó rồi, khéo đến lúc đó còn có video được truyền ra ngoài nữa đấy..."

Dương Kiến nói đến mức nước bọt bay tứ tung, quyết đấu của Tông sư Bát phẩm, ngay cả trên toàn thế giới cũng cực kỳ hiếm thấy.

Trước kia có lẽ cũng từng có, nhưng hoặc là lúc đó tuổi bọn họ còn quá nhỏ nên không có ấn tượng sâu sắc, hoặc là đối phương âm thầm so tài trong bóng tối, người ngoài chỉ có thể biết được kết quả chứ căn bản không biết được quá trình diễn ra thế nào.

Lần này thì khác, có thể liên quan tới việc mạng internet hiện nay phát triển bùng nổ, tin tức lan truyền quá nhanh, mọi người đều nhận được thông tin từ trước, nhờ vào mạng internet, nói không chừng bọn họ cũng có thể thông qua video mà theo dõi trận chiến.

Hóng hớt buôn chuyện một hồi về sự kiện quyết đấu của Tiểu Mã ca xong, Dương Kiến rất nhanh lại chuyển dời chủ đề, nói sang chính bản thân mình: "Hôm nay bắt đầu báo danh thi võ khoa rồi đấy. Bố tao bảo rồi, tốn bao nhiêu tiền cũng phải báo danh, cả cái nhà họ Dương này chỉ trông cậy vào mỗi tao thi đỗ võ khoa, trở thành võ giả thôi.

Ai dà, áp lực lớn quá chừng, nếu mà thi trượt thì hai đứa mày bảo tao phải làm sao bây giờ?"

Phương Bình cười trêu chọc: "Tao bảo này, mày là đang khoe khoang trá hình đấy, hay là đang khoe khoang thật thế hả?"

Dương Kiến cười ngây ngô chất phác, vội vàng lắc đầu nói: "Tao thèm vào mà khoe khoang, áp lực lớn thật sự đấy chứ. Hai đứa mày đâu phải không biết tình hình của tao, năm cửa ải lớn của võ khoa, tao vượt qua được ba cửa ải đã là thắp hương bái Phật rồi, mấy cửa ải còn lại mờ mịt lắm."

"Năm cửa ải lớn của võ khoa?"

Vốn dĩ đối với mấy chủ đề buôn chuyện của Dương Kiến, Phương Bình cũng chẳng có bao nhiêu hứng thú.

Nhưng ngay lúc này, hai mắt Phương Bình bỗng nhiên sáng rực lên."""
    },
    8: {
        "url": "https://www.piaotia.com/html/9/9640/6523762.html",
        "title_vi": "Chương 8: Tim Đau Nhói",
        "content_vi": """Phương Bình hôm kia tuy rằng có tới quán net tra cứu một ít tư liệu, nhưng thời gian có hạn, đương nhiên, nguyên nhân chủ yếu nhất vẫn là tiền giờ net có hạn.

Có những thứ hắn vẫn chưa thể tra cứu rõ ràng tường tận, ví dụ như chuyện đại khảo võ khoa, thực ra trên mạng cũng nói năng mập mờ chẳng mấy rõ ràng.

Không có điện thoại thông minh, trong nhà lại không có máy vi tính, Phương Bình hiện tại nếu không ra quán net thì muốn tìm hiểu bất cứ thứ gì cũng vô cùng khó khăn trắc trở.

Có những vấn đề lại không tiện đi hỏi người khác một cách quá lộ liễu, dù sao trong mắt đại đa số mọi người thì đây đều là những kiến thức thường thức cơ bản.

"Xem ra nên mua một chiếc máy vi tính rồi." Phương Bình thầm nghĩ trong lòng, theo bản năng lờ tịt đi việc mua máy tính cũng cần phải tốn bộn tiền mới được.

Tuy bản thân mình không hiểu rõ lắm, nhưng kẻ một lòng muốn thi võ khoa như Dương Kiến khẳng định là nắm rất vững.

Tiếng nói của Dương Kiến vừa dứt, Phương Bình làm ra vẻ lơ đễnh thuận miệng hỏi: "Tao nhớ năm ngoái kỳ thi võ khoa đâu có khó lắm đâu, với điều kiện của mày chẳng lẽ đến bốn cửa ải cũng không qua nổi, hay là chính sách năm nay lại có biến động gì mới?"

Câu này hắn nói nửa nạc nửa mỡ lập lờ nước đôi, dù sao mỗi năm chính sách thi cử có chút thay đổi cũng là chuyện bình thường, Phương Bình không sợ Dương Kiến nảy sinh nghi ngờ.

Tiện thể tâng bốc thằng nhóc này một câu, biết đâu lại moi thêm được nhiều thông tin hữu ích.

Quả nhiên, Dương Kiến đối với sự "vô tri" của Phương Bình chẳng mảy may để tâm, nụ cười trên mặt lại càng thêm phần rạng rỡ đắc ý.

Hiếm khi thấy Phương Bình chịu chủ động nói chuyện võ khoa với mình, Dương Kiến ước gì được nói thêm vài ba câu nữa.

Giống như Trần Phàm thì căn bản chẳng có hứng thú gì, lúc nãy Phương Bình chưa tới, cậu ta nói cũng bằng thừa, nói cho không khí nghe.

Lúc này thấy Phương Bình nổi hứng tò mò, Dương Kiến lập tức mặt mày hớn hở nói: "Mày thật sự đánh giá tao quá cao rồi đấy, với lại kỳ thi võ khoa năm nào mà chẳng khó như lên trời.

Tuy nhiên năm nay đúng là có một vài thay đổi về chính sách, cụ thể thi thế nào thì bây giờ tao cũng chưa rõ lắm, đợi ngày kia Vương học trưởng về trường chắc sẽ nói rõ.

Nhưng mấy ngày nay tao cũng đã đi tra cứu khắp nơi, còn hỏi cả thầy giáo nữa, so với năm ngoái thì quả thật có vài điểm khác biệt đấy."

Thấy cậu ta nói đến đây thì dừng lại không nói tiếp, Phương Bình dĩ nhiên thừa biết cái gã tương lai râu quai nón này đang cố tình treo khẩu vị người khác, hắn bèn dứt khoát ngậm miệng không thèm hỏi thêm câu nào.

Mấy thằng nhóc miệng còn hôi sữa này, lại thêm cái mồm loa mép giải của Dương Kiến, mình càng không hỏi, hắn mở đầu câu chuyện rồi thì tự khắc nhịn không nổi đâu.

Quả nhiên không ngoài dự liệu, thấy Phương Bình không tiếp tục hùa theo tâng bốc, Dương Kiến cảm thấy có chút chưa đã thèm, đành phải tự mình tiếp tục ba hoa: "Cứ nói về cửa ải thứ nhất đi, cửa ải Thẩm tra chính trị (Chính thẩm)."

Lông mày Phương Bình hơi nhúc nhích, liền nghe Dương Kiến nói tiếp: "Cửa ải chính thẩm trước kia, phải điều tra thân nhân trực hệ ba đời xem có tiền án tiền sự phạm tội gì hay không.

Năm nay điều kiện nới lỏng hơn rồi, chỉ điều tra hai đời thân nhân có quan hệ huyết thống như cha mẹ, anh chị em ruột thôi.

Tuy nhiên chuyện này đối với bọn mình cũng chẳng ảnh hưởng gì lớn, trừ phi đời ông nội chúng mình từng có tiền án vi phạm pháp luật."

Cửa ải đầu tiên của kỳ thi võ khoa: Thẩm tra chính trị.

Đây cũng là lẽ thường tình của con người, võ giả rốt cuộc không phải người bình thường, sức tàn phá lớn hơn người bình thường gấp bội.

Ngành võ khoa của các trường đại học, chính phủ hàng năm rót vào nguồn kinh phí khổng lồ.

Tiêu hao một lượng lớn tài nguyên để bồi dưỡng ra võ giả, tuyệt đối không phải để cho bọn họ đi làm chuyện phi pháp phạm tội, mặc dù chẳng ai quy định cha mẹ là người xấu thì con cái nhất định phải là kẻ xấu.

Nhưng trong điều kiện tuyển chọn nhân tài có giới hạn, tự nhiên càng nghiêm ngặt chừng nào thì càng tốt chừng nấy, bạn có không cam lòng thì cũng chẳng làm gì được.

"Thẩm tra chính trị tuy nới lỏng, nhưng đối với chúng mình lại chẳng có ưu thế gì, ngược lại còn là thế yếu, dù sao số lượng người có thể báo danh lại tăng thêm một chút.

Thế nhưng cửa ải thứ hai cũng có một số thay đổi, cái này thì có lợi cho chúng mình rồi."

Dương Kiến hớn hở nói: "Cửa ải thứ hai, Kiểm tra thể chất võ khoa (Thể kiểm).

Mấu chốt không nằm ở các hạng mục kiểm tra sức khỏe có thay đổi, mà chủ yếu là về độ tuổi.

Trước kia, giới hạn tối đa là 22 tuổi, nhưng năm nay chính sách thay đổi rồi, giới hạn trên bị rút xuống còn 20 tuổi, để tao xem đám rùa rụt cổ kia còn mặt mũi nào mà ở lại lưu ban thi lại nữa, tức chết cái lũ bọn chúng đi!"

Võ giả không phải cứ tuổi tác càng nhỏ là càng tốt. Tuổi còn nhỏ, xương cốt thân thể chưa phát triển hoàn thiện, tâm lý cũng chưa chín chắn.

Tuổi còn quá nhỏ mà luyện võ, ngược lại rất dễ làm tổn thương thân thể, cũng dễ dẫn tới việc một số thiếu niên vị thành niên vì sở hữu sức mạnh vượt trội hơn người thường mà làm ra những hành vi xốc nổi vượt quá giới hạn.

Đây cũng chính là nguyên nhân chủ yếu khiến quốc gia chỉ thành lập hệ võ khoa ở bậc đại học!

Trải qua nhiều năm giáo dục tư tưởng, đến bước đại học này, suy nghĩ của sinh viên nhìn chung đều đã chín chắn trưởng thành, cộng thêm thân thể đã phát triển hoàn chỉnh, lúc này luyện võ thực chất sẽ làm ít công to, võ giả về sau xuất hiện vấn đề cũng sẽ không quá nhiều.

Trước kia, có một số học sinh năm nay thi không đỗ, chọn phương án ôn thi lại để năm sau thi tiếp, đó là chuyện hết sức bình thường.

Có nhiều kinh nghiệm hơn người khác, sau khi đã thi qua một lần cũng biết rõ khuyết điểm của mình nằm ở đâu, có thể căn cứ vào tình hình thực tế mà bù đắp rèn luyện.

Học sinh thi đỗ võ khoa hàng năm, thí sinh thi lại cũng chiếm một tỷ lệ không nhỏ.

Trước kia giới hạn ở mức 22 tuổi, có người thậm chí còn thi lại mấy năm liền.

Năm nay trực tiếp chém thẳng tay xuống 20 tuổi, lần này e rằng trong nháy mắt đã dập tắt hy vọng của rất nhiều thí sinh thi lại.

Dù sao học sinh lớp 12 tuổi từ 18 đến 20 là bình thường, có người chỉ cần thi lại một năm là đã có thể vượt quá 20 tuổi rồi.

Phương Bình thì chẳng cần lo lắng điều này, tính ra hắn mới có 18 tuổi tròn, có thi lại thêm hai năm nữa cũng vẫn vô tư.

Suy nghĩ một chút, Phương Bình hỏi: "Vậy phía thí sinh thi lại bên kia không có phản ứng gì sao?"

Dương Kiến hí hửng nói: "Làm sao mà không có, nghe nói mấy hôm trước náo loạn cào cào cả lên, nhưng có ích gì đâu chứ?

Ai bảo ban đầu mày thi không đỗ, đã ngoài 20 tuổi đầu rồi, cho dù có thi đỗ thì cũng chỉ tổ kéo chân sau người ta.

Dù sao thì kháng nghị cũng vô dụng, rốt cuộc thí sinh thi võ khoa vẫn là học sinh khóa mới chiếm đa số, mọi người chỉ mong lũ đó không được phép thi, bên văn khoa thì không hạn chế cái này, có thể chuyển sang thi văn khoa."

Phương Bình hiểu rõ, quay lại chủ đề chính hỏi: "Khám thể chất võ khoa và khám thể chất văn khoa có chênh lệch lớn không?"

Dương Kiến gãi gãi đầu, nhịn không được liếc nhìn hắn một cái.

Trần Phàm nãy giờ vẫn im lặng không nói gì, lúc này cũng cạn lời thốt lên: "Nói nhảm, chênh lệch sao lại không lớn cho được? Phương Bình, cậu không phải ngủ mê sảng đấy chứ?

Chuyện khám thể chất võ khoa tớ cũng từng nghe qua không ít lần rồi.

Cậu tưởng 1 vạn tệ tiền lệ phí báo danh là nộp cho vui đấy à?

Khám thể chất võ khoa, cái đó phải tiến hành kiểm tra tầng sâu toàn diện, bao gồm cả việc xương cốt có từng bị tổn thương hay dị tật gì không.

Thị lực kém, xương cốt có vết thương, trên thân thể có vết sẹo lớn, những trường hợp này đều không được trúng tuyển đâu.

Hơn nữa, quan trọng nhất chính là kiểm tra khí huyết, khí huyết không đủ, thân thể suy nhược thì các điều kiện khác có tốt đến mấy cũng vứt đi. Có những người trời sinh thể trạng hư nhược, có bồi bổ thế nào cũng chẳng thể bù đắp lại được, cả đời này vô duyên với võ giả.

Bình thường nhà nào ăn uống kham khổ, tiêu chuẩn khí huyết thông thường đều không đạt chuẩn, cho nên tỷ lệ trúng tuyển của các thành phố lớn luôn cao hơn các thành phố nhỏ của chúng ta.

Thành phố nhỏ lại cao hơn các thị trấn thôn quê.

Nơi nào càng nghèo thì võ giả càng ít, dù sao cho dù cậu và người khác không chênh lệch bao nhiêu, nhưng võ khoa mỗi năm đều có chỉ tiêu cố định, chọn người ưu tú trong những người ưu tú, đương nhiên người ta phải chọn nhóm người tốt nhất rồi."

Phương Bình gật đầu, hồi tưởng lại một chút, bản thân mình hẳn là không có vấn đề gì quá lớn mới phải, dù sao khí huyết của mình vừa mới tăng lên không ít, chắc chắn phải mạnh hơn người bình thường.

Nếu đổi thành Phương Bình trước kia thì thật sự chưa chắc đã qua nổi, dù sao mọi người đều là người bình thường, cậu cũng chẳng có gì đặc biệt xuất chúng hơn người.

Thế nhưng mức khí huyết 1.1 liệu có đạt chuẩn hay không thì cũng rất khó nói, xem ra trước khi khám thể chất, tốt nhất nên tìm cách tăng thêm một chút nữa mới yên tâm.

Ngoài ra Phương Bình có chút tò mò, nghe giọng điệu của Trần Phàm thì hiện nay hẳn là có môn kiểm tra khí huyết chuyên nghiệp.

Mà trong ký ức của Phương Bình, khí huyết có dồi dào hay không thực chất là cách nói của Trung y, không có máy móc chuyên dụng kiểm tra, chỉ có thể thông qua Trung y vọng văn vấn thiết mới đưa ra được kết luận.

Dưới quy mô kiểm tra quy mô lớn của kỳ thi đại học thế này, khả năng dựa vào Trung y để phân biệt là không lớn, khả năng cao hơn là đã hình thành nên một bộ quy trình hoàn thiện, bao gồm cả các thiết bị y tế chuyên dụng.

Trong lúc Phương Bình đang thầm tính toán, Dương Kiến mở miệng nói: "Ngoài hai điểm này ra, những thứ khác biến động không quá lớn.

Cửa ải chính thẩm qua rồi, cửa ải thể kiểm qua rồi, quét rớt một lượng lớn người, những người còn lại sẽ tham gia cửa ải thứ ba: Thực trắc (Kiểm tra thực tế).

Sau đó chính là hai cửa ải khó nhằn nhất: Văn hóa khóa và Chuyên nghiệp khảo..."

"Khụ khụ khụ!"

Phương Bình nhớ lại hôm kia lướt mạng hình như cũng thấy nhắc tới chuyện thi văn hóa khóa, lúc đó hắn còn chưa để ý, giờ phút này lại nhịn không được hỏi: "Điểm văn hóa thì có gì ghê gớm đâu, đến cái này mà mày cũng không có tự tin à?"

Theo suy nghĩ của Phương Bình, cái này cũng tương tự như thi năng khiếu nghệ thuật kiếp trước thôi, các điều kiện khác đã phù hợp rồi thì điểm thi văn hóa hẳn là rất dễ qua, chỉ cần hơi để tâm một chút thì 90% học sinh Trường Số 1 đều có thể vượt qua ngon lành.

Ai ngờ lời hắn vừa thốt ra, Dương Kiến đã cười khổ nói: "Phương Bình ơi, đổi thành mày thì còn có cửa, chứ tao thì khó như lên trời rồi.

Năm ngoái điểm chuẩn trúng tuyển thấp nhất của võ khoa cũng cao hơn điểm chuẩn đại học trọng điểm văn khoa tận 10 điểm đấy! Cái thành tích lẹt đẹt này của tao, thật sự chưa chắc đã lết qua nổi điểm sàn đâu."

"Võ giả văn võ song toàn, chứ đâu phải chỉ là đám mãng phu lỗ mãng đơn thuần. Điểm cao hơn điểm sàn đại học trọng điểm văn khoa một chút là bình thường, nếu không võ giả toàn là phường thất phu lỗ mãng thì lấy đâu ra tư cách mà leo lên làm tầng lớp lãnh đạo cấp cao."

Câu này là do Trần Phàm nói, giọng điệu rất bình thản, nói ra một cách vô cùng đương nhiên.

Văn võ song toàn, đó mới chính là võ giả!

Võ giả được ca tụng là tầng lớp tinh anh của xã hội, nếu chỉ là phường mãng phu lỗ mãng đơn thuần thì có thể trị quốc, có thể quản lý tốt các đại doanh nghiệp được sao?

Truyện cổ tích toàn là lừa người cả thôi!

Trên phim truyền hình, cứ tùy tùy tiện tiện một gã mù chữ nào đó nhặt được cuốn bí kíp là có thể trở thành cao thủ tuyệt đỉnh, đúng là nói nhảm nhí xằng bậy!

Mãng phu có thể đạt được chút thành tựu nhỏ trên võ đạo, nhưng tuyệt đối không bao giờ bước lên được đỉnh cao.

Một cuốn bí kíp đưa đến tận tay mày, đến mặt chữ mày còn không nhận biết nổi thì mày học võ cái nỗi gì?

Nhận biết mặt chữ rồi, nhưng ý tứ sâu xa bên trong mày lại chẳng hiểu lấy một phân, vậy thì còn học võ cái quái gì nữa?

Không hiểu ý tứ của công pháp là chuyện có xác suất cực kỳ lớn, một số công pháp tối nghĩa trúc trắc, ngay cả sinh viên đại học kiếp trước đọc vào cũng chẳng hiểu nổi, chẳng khác nào đọc thiên thư chữ trời.

Cho nên võ giả còn phải am hiểu rất nhiều kiến thức linh tinh hỗn tạp khác, ví dụ như y học, nhân thể học, bao gồm cả sơ đồ xương cốt cơ thể người, sơ đồ đường đi của kinh mạch, những thứ này đều phải nắm rõ như lòng bàn tay.

Đây mới chỉ là học sinh lớp 12 thôi đấy, lên đến đại học, những người theo học ngành võ khoa còn phải học thêm rất nhiều môn học so với sinh viên văn khoa.

Ví dụ như khoáng vật học, dinh dưỡng học...

Cửa ải "Chuyên nghiệp khảo" trong miệng Dương Kiến thực chất chính là thi sát hạch những kiến thức linh tinh tạp nham này.

Vừa phải gánh vác việc học văn hóa, vừa phải gánh vác việc rèn luyện tố chất thân thể, đồng thời lại còn phải tiếp thu học tập những kiến thức chuyên môn này, có thể nói, những học sinh có thể thi đỗ vào võ khoa không một ngoại lệ, đều là những thiên tài đích thực.

Thành tích văn hóa phải cao hơn cả điểm sàn đại học trọng điểm, thân thể phải khỏe mạnh dẻo dai bừng bừng sức sống, lại còn phải đọc rộng hiểu sâu những kiến thức chuyên ngành nằm ngoài phạm vi sách giáo khoa văn hóa...

Nghe xong toàn bộ năm cửa ải lớn của kỳ thi võ khoa, Phương Bình cảm thấy mệt mỏi thấu tận tâm can.

Ba cửa ải đầu tiên, nhờ có cái hệ thống không mấy đáng tin cậy kia, Phương Bình cảm thấy bản thân mình hẳn là không có vấn đề gì lớn, cũng có biện pháp để khắc phục vượt qua.

Nhưng đây là thi võ khoa cơ mà trời đất ơi!

Rõ ràng đã nói là sát hạch tố chất thân thể, sao lại còn phải thi cả văn hóa, mà điểm thi lại còn phải cao hơn cả điểm sàn trường trọng điểm nữa chứ?

Cái này thì thôi cũng đành chấp nhận đi, sách giáo khoa Phương Bình cũng đã xem qua rồi, so với kiếp trước không có chênh lệch quá lớn, chỉ có sách lịch sử là có chút khác biệt, bên trong được thêm thắt vào nhiều yếu tố võ đạo hơn.

Nhưng cái "Chuyên nghiệp khảo" này là cái quỷ gì vậy trời?

Những kiến thức chuyên môn này, Phương Bình hoàn toàn chưa từng được tiếp xúc qua lấy một chữ bẻ đôi!

Hiện tại khoảng cách đến kỳ thi đại học chẳng còn bao lâu nữa, bản thân mình thật sự có thể gánh vác quán xuyến nổi hết tất cả mọi thứ này hay sao?

Đm nó chứ!

Trong bụng Phương Bình ngập tràn nỗi uất ức oan ức khôn nguôi, hay là dứt khoát nằm ườn ra làm một con cá mặn phơi khô cho rồi?"""
    },
    9: {
        "url": "https://www.piaotia.com/html/9/9640/6523763.html",
        "title_vi": "Chương 9: Tiêu Chuẩn Khí Huyết",
        "content_vi": """Oán niệm dẫu có sâu nặng ngập trời thì cuộc sống vẫn phải tiếp diễn, Phương Bình chỉ có thể bị động đón nhận tất cả những điều này.

Tán gẫu một hồi, thầy chủ nhiệm với mái tóc đã hoa râm thong thả cất bước bước vào phòng học.

Đợi đến khi cả lớp học đã hoàn toàn yên tĩnh trở lại, Lão Ban liền đi thẳng vào chủ đề chính: "Những em nào báo danh tham gia kỳ thi võ khoa, lát nữa tới văn phòng của tôi để nộp lệ phí và đăng ký, điền vào phiếu báo danh, sau đó phòng giáo vụ nhà trường sẽ thống nhất làm thủ tục báo danh cho các em."

Lúc nói những lời này, ánh mắt của thầy chủ nhiệm chủ yếu nhìn về phía những học sinh có ý định báo danh.

Trên thực tế, kỳ thi võ khoa không phải là chuyện không có dấu vết để lần mò.

Là giáo viên chủ nhiệm, trong lớp những em nào sẽ báo danh, Lão Ban trong lòng đại khái đều đã nắm rõ như lòng bàn tay.

Thành tích học tập phải thuộc hàng xuất sắc, thân thể phải khỏe mạnh dẻo dai, gia cảnh cũng phải khá giả vững vàng. Trải qua mấy tầng tuyển chọn sàng lọc như vậy, lớp 12 ban 4 ai sẽ báo danh, các học sinh trong lớp cũng đều tự hiểu rõ.

Dương Thành nằm sâu trong nội địa, tuy rằng tên gọi đầy đủ là thành phố Dương Thành, nhưng trên thực tế chỉ là một thành phố cấp huyện.

So với các huyện thành khác, kinh tế Dương Thành có khá khẩm hơn một chút, nhưng cũng tốt có hạn độ, đây không phải là thành phố cấp huyện vùng duyên hải ven biển, những thành phố cấp huyện ven biển có nơi còn phát triển vượt bậc hơn cả các thành phố cấp địa khu trong nội địa.

Tại Dương Thành, những người không coi 1 vạn tệ ra gì cũng chẳng có mấy ai.

Bởi vậy, chỉ riêng một khoản lệ phí báo danh thôi cũng đã đủ để chặn đứng biết bao nhiêu người ở ngoài ngưỡng cửa.

Nói xong những lời này, thầy chủ nhiệm liền rời khỏi phòng học.

Mà những học sinh chuẩn bị báo danh lúc này cũng lục tục đứng dậy, chuẩn bị tiến về phía văn phòng giáo viên.

Dương Kiến ngồi bàn phía trước Phương Bình lúc này cũng đứng bật dậy.

Bàn học bên cạnh, cái cậu bạn tên Trương Hạo — người hôm kia vừa tiết lộ tin tức Tiểu Mã ca đột phá Bát phẩm — lúc này cũng bước ra khỏi chỗ ngồi.

Ngay khi hai người chuẩn bị cất bước bước đi, Phương Bình liền ung dung nhàn nhã đứng dậy theo.

Cậu bạn cùng bàn Trần Phàm có chút sững sờ ngơ ngác, nghiêng đầu hỏi: "Đi vệ sinh hả?"

"Đi báo danh."

"..."

Trần Phàm sững sờ chết lặng, Phương Bình muốn báo danh á?

Đâu chỉ có mỗi mình Trần Phàm, Dương Kiến cũng không nhịn được mà ngoái đầu nhìn chằm chằm vào Phương Bình, kinh ngạc thốt lên: "Phương Bình, mày cũng báo danh đấy à?"

Thằng nhóc này, trong lời nói chưa chắc đã mang theo ác ý gì, nhưng quả thật là bị những lời Phương Bình vừa nói làm cho kinh hãi không nhỏ, âm lượng giọng nói cũng chẳng hề bé chút nào.

Lời này vừa thốt ra, không ít bạn học trong lớp đều đồng loạt quay đầu nhìn sang.

Mọi người làm bạn học với nhau suốt mấy năm trời, tình hình của các bạn khác trong lớp thế nào, đại khái ai nấy đều có chút hiểu biết.

Đâu phải nói là Phương Bình không được quyền báo danh, nhưng với cái thân hình nhỏ thó gầy gò kia của Phương Bình...

Thực ra Phương Bình vẫn còn vạm vỡ hơn Trần Phàm một chút, nhưng so với gã Dương Kiến hộ pháp ngồi bàn trước thì căn bản chẳng có cửa để so sánh.

Điểm văn hóa và chuyên nghiệp khảo thì còn dễ nói, chứ hai cửa ải khám thể chất và kiểm tra thực tế, Phương Bình liệu có qua nổi không?

Bên này Dương Kiến vừa mới kinh ngạc xong, Trương Hạo ở bên cạnh cũng chậc chậc lưỡi cất tiếng: "Phương Bình, thằng nhóc mày được đấy nhé, thâm hiểm thật!

Bình thường mọi người tan học rủ nhau đi rèn luyện thân thể mày đều không tham gia, về nhà chắc chắn lén lút tập thêm không ít chứ gì, thằng ranh mày quá thâm hiểm rồi!"

Trương Hạo nói những lời này với vẻ mặt phóng đại, nhưng ngữ khí hoàn toàn không hề mang ý mỉa mai châm chọc, chỉ cảm thấy thằng nhóc Phương Bình này giấu nghề quá sâu. Nếu không có chút tự tin nắm chắc thì với gia cảnh nghèo khó của Phương Bình, làm sao dám lãng phí đứt đuôi 1 vạn tệ tiền lệ phí báo danh kia chứ?

Phương Bình cũng chẳng thèm để bụng, cười ha hả nói: "Đừng nghĩ nhiều quá làm gì, tao đây thiên phú dị bẩm, cần quái gì phải tập thêm?

Tao nghĩ kỹ rồi, chẳng qua chỉ là 1 vạn tệ thôi mà?

Không thử một phen thì ai biết được có thi đỗ hay không, biết đâu năm nay nhà nước bỗng nhiên mở rộng chỉ tiêu tuyển sinh, thế chẳng phải tao vớ bẫm lời to rồi sao."

"Hahaha, mày chỉ được cái nghĩ bở là giỏi!"

Trương Hạo cười ha hả, thế nhưng lời này của Phương Bình vừa thốt ra, những học sinh khác trong lớp vốn dĩ không có ý định báo danh lại có chút rục rịch động tâm.

Lời Phương Bình nói dường như cũng đâu phải không có lý chứ?

Ai mà biết được năm nay liệu có mở rộng chỉ tiêu tuyển sinh hay không?

Mấy năm trước, Trường Số 1 mỗi năm thi đỗ võ khoa cũng chỉ có hai ba người, nhưng năm ngoái lại đỗ tận năm người.

Năm nay, nói không chừng con số sẽ còn nhiều hơn một chút thì sao?

Nghĩ thì nghĩ vậy thôi, nhưng một khi đã không chuẩn bị báo danh thì tự nhiên là có nguyên nhân của nó, lời nói của Phương Bình cũng chỉ dấy lên một chút gợn sóng lăn tăn, chứ không thể làm cho những người khác thay đổi quyết định được.

Ánh mắt của người bạn cùng bàn Trần Phàm có chút phức tạp, mặc dù chỉ là báo danh chứ không đại biểu là sẽ thi đỗ.

Nhưng gia cảnh của Phương Bình còn khó khăn hơn nhà cậu ta một chút, ngay cả Phương Bình còn dám liều mạng thử một lần, còn cậu ta thì căn bản ngay cả ý nghĩ đó cũng chẳng dám nảy ra trong đầu, đem ra so sánh ngược lại càng làm nổi bật lên việc cậu ta ngay cả dũng khí thử sức cũng chẳng có lấy một phần.

Bàn tay cầm bút siết chặt lại thêm một chút, cuối cùng Trần Phàm vẫn không thay đổi quyết định của mình.

Cho dù có báo danh đi chăng nữa, hy vọng cậu ta có thể thi đỗ còn mờ mịt hơn cả Phương Bình.

Thay vì lãng phí thời gian và tiền bạc vào chuyện này, chi bằng dồn thêm công sức vào các môn văn hóa còn thực tế hơn nhiều.

……

Tâm tư của những người khác trong lớp, Phương Bình tự nhiên chẳng có tâm trạng đâu mà bận tâm để ý.

Hắn cùng những bạn học chuẩn bị báo danh khác bước ra khỏi lớp học, mọi người cùng nhau rảo bước đi lên văn phòng của thầy chủ nhiệm ở tầng trên.

Lớp 12 ban 4 số học sinh chuẩn bị báo danh không nhiều.

Dù sao xác suất quá nhỏ bé, một số điều kiện cứng nhìn qua là biết không đạt chuẩn thì tự nhiên sẽ không báo danh làm gì cho tốn tiền.

Cuối cùng, những người cùng bước ra khỏi lớp cũng chỉ có vẻn vẹn 8 người.

Thế này đã là tỷ lệ báo danh của lớp thường thuộc hàng cao trong mấy năm gần đây rồi đấy, nếu không phải nhờ hai học sinh lớp thường năm ngoái thi đỗ võ khoa làm tấm gương sáng thì lớp thường có được bốn năm người đăng ký đã là tốt lắm rồi.

Ở một số trường cấp ba bình thường khác, cả trường gom lại số học sinh báo danh cũng chỉ đếm trên đầu ngón tay.

Phương Bình đưa mắt quét nhanh qua nhóm học sinh đi cùng, quả nhiên toàn là những gương mặt nổi bật nhất nhì trong lớp.

Không chỉ có thành tích học tập thuộc top đầu, mà mấu chốt là thể chất ai nấy đều rất tốt, vóc dáng cân đối săn chắc.

Ngay cả gã râu quai nón Dương Kiến này, thành tích học tập tuy không phải quá xuất sắc nhưng cũng không hề kém cỏi, nếu không cậu ta cũng chẳng dám báo danh.

Trong số đó còn có hai bạn nữ, tuy nhan sắc không đến mức quá mức kinh diễm nghiêng nước nghiêng thành, nhưng vóc dáng nhìn qua quả thực rất chuẩn mực.

So với đám học sinh nữ còi cọc như cọng giá đỗ trong lớp đến giờ vẫn chưa phát triển hoàn thiện, hai bạn nữ này vì chuẩn bị thi võ khoa nên ăn uống dinh dưỡng đầy đủ, rèn luyện chăm chỉ, ngực nở mông cong, khiến Dương Kiến và Trương Hạo đi bên cạnh Phương Bình cứ chốc chốc lại đưa mắt liếc trộm sang người hai cô bạn.

Ngoại trừ Phương Bình ra, những người khác thực ra đều khá quen thuộc và thân thiết với nhau.

Thi võ khoa không phải là chuyện ngày một ngày hai, buổi tối có thời gian rảnh rỗi mọi người đều cùng nhau rèn luyện thân thể, có vài người còn cùng nhau đăng ký tham gia lớp bồi dưỡng võ khoa ở ngoài trường.

Phương Bình được coi là kiểu người đột ngột nhảy bổ ra từ trên trời rơi xuống.

Lúc này mọi người chẳng có hứng thú gì với những người cũ, ngược lại đều hết sức tò mò về Phương Bình.

Một trong hai bạn nữ mà đám Dương Kiến đang nhòm ngó chốc chốc lại đánh giá Phương Bình một lượt, đi được một đoạn liền nhịn không được cất tiếng hỏi: "Phương Bình, khí huyết của cậu được bao nhiêu?"

"Hả?"

Phương Bình có chút lúng túng chẳng biết phải trả lời thế nào, chẳng lẽ lại nói huỵch toẹt ra là khí huyết của mình là 1.1?

Mấu chốt là hắn căn bản không biết trong hiện thực cuộc sống, người ta rốt cuộc thống kê khí huyết thế nào và dùng đơn vị gì để đo lường.

May mà không đợi Phương Bình phải trả lời, Dương Kiến đã chen ngang cười nói: "Trương Nam, tao thấy Phương Bình căn bản chưa từng đi kiểm tra đâu.

Cái tên này, nếu mà thật sự từng đi đo kiểm tra rồi thì e rằng đã sớm bốc phét khoe khoang với chúng mình từ lâu rồi."

Trương Hạo cũng phụ họa vào: "Chắc là chưa từng đi kiểm tra thật rồi, nhưng nhìn cái thân hình nhỏ con kia của cậu ta thì khẳng định không thể cao bằng tớ được."

"Xì, bớt bốc phét đi có được không hả."

Trương Nam cũng chỉ thuận miệng hỏi vậy thôi, Phương Bình đã không nói, bất kể là chưa đi kiểm tra hay không muốn tiết lộ thì cô nàng cũng lười gặng hỏi thêm làm gì.

Khinh bỉ Trương Hạo một câu xong, Trương Nam vừa đi vừa lắc đầu thở dài: "Lớp chúng mình đợt này chắc lại mang số phận làm bia đỡ đạn, đi bồi thái tử đọc sách rồi.

Hôm kia tớ lại đi kiểm tra một lần nữa, dao động khí huyết lúc đỉnh cao nhất của tớ cũng chỉ mới đạt có 108 cal thôi.

Haizz, trước khi khám thể chất chỉ đành nghĩ cách ăn thêm chút thuốc bổ, xem xem có thể kéo nó nhích lên được chút nào hay không."

Trương Nam vừa dứt lời, Dương Kiến liền toét miệng cười ha hả: "Tao khá hơn mày một tẹo, lần đo kiểm tra trước, đỉnh cao nhất của tao đã lên tới 112 cal rồi."

"Cal" hiển nhiên chính là đơn vị đo kiểm tra khí huyết, nghe qua thì có vẻ như con số càng cao thì càng tốt.

Phương Bình chưa từng đi kiểm tra, lúc này cũng chẳng sợ lộ ra sự thiếu hiểu biết của mình, nghe vậy bèn hỏi: "Trong lớp chúng mình ai có khí huyết cao nhất?"

Một thiếu niên mang vẻ ngoài xán lạn rạng rỡ đi ở tít phía trước nghe vậy liền quay đầu lại cười nói: "Căn cứ theo kết quả lần kiểm tra trước thì chắc là tớ cao nhất, thời kỳ đỉnh cao đạt 115 cal."

Người này Phương Bình thực ra có quen biết, tuy rằng thế giới hiện tại có chút biến đổi, nhưng con người vẫn là con người đó.

Người vừa lên tiếng chính là người có thành tích các môn văn hóa tốt nhất trong lớp, đương nhiên hiện tại có phải còn giữ vị trí đó hay không thì Phương Bình chưa rõ lắm.

Tuy nhiên cậu bạn này không phải là lớp trưởng, trên thực tế những người có mặt ở đây chẳng có ai là cán bộ lớp cả, bởi vì không ai muốn lãng phí thời gian và cũng chẳng rảnh rỗi đâu mà đi phục vụ những người khác.

Tên là gì nhỉ, Phương Bình hồi tưởng lại một chút, hình như tên là Ngô Chí Hào.

Ngô Chí Hào nói xong lại lắc đầu thở dài: "Tuy rằng khí huyết của tớ cũng tàm tạm, nhưng mấy tên bên lớp chọn mới gọi là khủng khiếp, người cao nhất là Chu Bân, lần trước nghe người trong lớp cậu ta kể, trị số đỉnh cao đã vượt qua 120 cal rồi đấy.

Trường chúng ta người khác thì khó nói, chứ Chu Bân thì khả năng thi đỗ lên tới chín mươi chín phần trăm, chỉ cần giữa chừng không xảy ra tai nạn bất trắc gì ngoài ý muốn."

"Hahaha, Chí Hào ơi, hay là cậu bỏ tiền thuê người đánh gãy chân nó đi, bọn mình cũng bớt đi được một đối thủ cạnh tranh nặng ký?" Trương Hạo cười ha ha trêu chọc.

Ngô Chí Hào đảo trắng mắt, cạn lời đáp: "Có phải là tuyển chọn nội bộ trong trường mình đâu, Chu Bân cho dù có thi trượt thì cũng chẳng liên quan gì nhiều đến chúng mình, nếu không thì tớ thật sự cũng có ý định đó đấy."

Trương Hạo cười hì hì một tiếng, thuận miệng nói: "Dù sao thì cứ thử xem sao, biết đâu may mắn lại thi đỗ thì sao.

Năm ngoái tiêu chuẩn tuyển sinh của Đại học Võ thuật Nam Giang, khí huyết 112 cal là đủ điều kiện rồi.

Năm nay cho dù có nhích lên một chút thì cũng cao lên có hạn thôi, dù sao tớ thấy cậu cơ hội rất lớn đấy..."

Ngô Chí Hào lại lắc đầu một lần nữa: "Mong manh lắm, mấy năm nay năm nào tiêu chuẩn cũng tăng vọt lên, tớ thấy năm nay bèo nhất cũng phải từ 115 cal trở lên.

Hơn nữa, đâu phải chỉ cần khí huyết đạt chuẩn là xong, những thứ khác thì sao?

Mấu chốt không phải nhìn vào cái này, mà còn phải nhìn vào những người khác nữa kìa. Nếu như những người khác đều thấp mà chúng mình cao, thì chúng mình mới có cơ hội.

Còn nếu những người khác ai nấy đều cao chót vót, thì chúng mình có thi tốt đến mấy cũng vẫn bị đánh trượt như thường."

Những tiêu chuẩn tuyển sinh này cũng giống hệt như các kỳ thi văn hóa vậy, hoàn toàn không cố định, chỉ tiêu sinh viên võ khoa chỉ có bấy nhiêu đó suất mà thôi.

Có thể thành tích năm nay của bạn nếu chiếu theo thang điểm năm ngoái thì đã thừa sức thi đỗ võ khoa, nhưng năm nay mặt bằng chung ai cũng mạnh mẽ vượt trội thì bạn vẫn phải ngậm ngùi rớt đài.

Hoặc giả năm nay bạn thi kém, nhưng kết quả mọi người xung quanh đều kém như nhau, thì bạn dù không mạnh bằng lứa năm ngoái cũng vẫn có thể trúng tuyển.

Thế nhưng trong thời đại ngày nay, điều kiện sống của mọi người ngày càng khấm khá ấm no, hầu như năm nào tiêu chuẩn cũng lũy tiến tăng lên, xác suất hạ điểm chuẩn xuống là cực kỳ thấp bé.

Theo lời của Ngô Chí Hào, lớp 12 ban 4 cộng thêm cả Phương Bình là tổng cộng có 8 người báo danh, nhưng người có khí huyết vượt qua 110 cal cũng chỉ có vẻn vẹn ba người.

Ngô Chí Hào, Dương Kiến, và ngoài ra còn có cô bạn nữ ít khi mở miệng nói chuyện tên là Lưu Nhược Kỳ.

Những người khác, bao gồm cả Trương Hạo, đều chưa chạm tới mốc 110 cal.

Tuy nhiên Trương Hạo cách cột mốc 110 cal cũng không còn xa, trước kỳ thi cố gắng tẩm bổ thêm nhiều dược phẩm bổ khí huyết thì vẫn tràn trề hy vọng.

Đây không tính là gian lận thi cử. Ở thời đại này, những loại thuốc bổ thực sự có tác dụng bồi bổ khí huyết đều có giá cả vô cùng đắt đỏ trên trời.

Những gia đình có đủ điều kiện kinh tế để mua loại này ăn uống tẩm bổ thì gia cảnh đều thuộc hàng khá giả giàu có.

Mà võ giả thì lại rất cần đến sự hậu thuẫn chống lưng của tài phú tiền bạc.

Gia đình có tiền hay không có tiền, mức độ trợ lực ủng hộ cho tương lai của võ giả là hoàn toàn khác biệt nhau. Tài phú quyết định tương lai, tuy rằng không phải là hiện trạng mang tính tuyệt đối, nhưng lại là hiện trạng mang tính phổ biến trong xã hội.

Cho nên cho dù hiện tại chưa đạt tới 110 cal, Trương Hạo vẫn dám mạnh dạn báo danh, chính là bởi vì gia đình cậu ta đã chuẩn bị sẵn sàng thuốc bổ quý giá cho cậu ta rồi.

Sở dĩ bây giờ chưa uống là vì sợ sau khi tiêu hóa xong, dược lực sẽ bị hao hụt trôi mất một phần, không đạt được hiệu quả tối đa vào đúng ngày thi.

Còn nếu uống ngay trước thềm khám thể chất, tuy rằng trong thời gian ngắn không thể hấp thụ chuyển hóa toàn bộ, nhưng đối với những người mới chập chững muốn nhập môn thì lại là chuyện vô cùng tốt, có thể bộc phát ra nhiều dược hiệu nhất trong thời điểm kiểm tra.

Chuyện này Trương Hạo không nói toẹt ra, nhưng trên thực tế những người khác đều có những sự chuẩn bị tương tự như vậy.

Đương nhiên cũng có ngoại lệ, ví dụ như Phương Bình.

Việc hắn báo danh thi võ khoa quá mức đường đột bất ngờ, cha mẹ căn bản không hề nghĩ tới việc hắn lại muốn đăng ký dự thi.

Mà trên thực tế, ngay trong lúc Phương Bình hoàn toàn không hay biết gì, thì ông bố Phương Danh Vinh đã bắt đầu cân nhắc suy tính xem có nên gom góp tiền bạc mua cho con trai một ít thuốc bổ khí huyết hay không rồi.

Đáng tiếc là những loại thuốc bổ dưỡng khí huyết đó đều quá mức đắt đỏ xa xỉ, động một tí là bắt đầu từ con số hàng vạn tệ trở lên, lão Phương đến giờ phút này vẫn chưa thể hạ nổi quyết tâm.

Lắng nghe mọi người rôm rả trò chuyện, Phương Bình âm thầm tính toán trong lòng: "Liệu 1.1 điểm khí huyết này của mình có phải có thể quy đổi thành 110 cal trong thực tế hay không?"

Khả năng này quả thực là rất lớn.

Thế nhưng cho dù có là 110 cal đi chăng nữa thì dường như cũng chẳng có chút ưu thế nào, dù sao Ngô Chí Hào ở lớp thường cũng đã đạt 115 cal rồi, bên các lớp chọn thì số người vượt qua 110 cal chắc chắn không hề ít.

Năm ngoái Đại học Võ thuật Nam Giang lấy tiêu chuẩn tuyển sinh tối thiểu là 112 cal thì đúng là vậy thật, nhưng năm nay thì chưa biết chừng đâu được.

"Xem ra mình vẫn phải bỏ thêm chút công phu vào phương diện này mới được, ít nhất phải vượt qua được ba cửa ải đầu tiên thì mới có thời gian mà tính toán đến những chuyện phía sau."

Trong lúc Phương Bình đang mải mê suy nghĩ miên man trong đầu, mọi người cũng đã cùng nhau bước tới trước cửa văn phòng giáo viên."""
    },
    10: {
        "url": "https://www.piaotia.com/html/9/9640/6523764.html",
        "title_vi": "Chương 10: Kiểm Tra Khí Huyết",
        "content_vi": """Bên trong văn phòng giáo viên.

Nộp tiền, điểm danh đăng ký, điền vào phiếu báo danh, các bước quy trình diễn ra vô cùng đơn giản gọn gàng.

Nhân lúc những người khác không chú ý, Phương Bình lại một lần nữa làm một thí nghiệm nhỏ: hắn vờ như vô tình đưa tay chạm nhẹ sờ vào mấy cọc tiền lệ phí báo danh mà các bạn học khác vừa nộp lên.

Kết quả cũng chẳng nằm ngoài dự liệu của hắn: Điểm số tài phú hoàn toàn không hề nhúc nhích tăng lên lấy một điểm.

Điểm này Phương Bình đã sớm liệu trước được từ sớm, cho nên cũng chẳng hề cảm thấy thất vọng là bao.

Số lượng người không nhiều, việc báo danh rất nhanh liền kết thúc êm xuôi.

Thầy chủ nhiệm gom toàn bộ phiếu báo danh của học sinh lại với nhau, đưa mắt đảo nhìn một lượt 8 gương mặt đang đứng trước mặt mình. Đây cũng chính là toàn bộ niềm hy vọng thi đỗ võ khoa của lớp 12 ban 4 năm nay.

Những người khác, thầy chủ nhiệm từ trước đó đều đã nắm bắt đại khái tình hình, trường hợp ngoại lệ duy nhất không ai khác chính là Phương Bình.

Là giáo viên chủ nhiệm của Phương Bình, Phương Danh Vinh cũng từng tới trường tham dự các buổi họp phụ huynh, hoàn cảnh gia đình họ Phương thế nào, Lưu An Quốc trong lòng đều biết rất rõ.

Thế nhưng hàng năm vào thời điểm này, số lượng học sinh ôm tâm lý muốn đánh cược liều mạng một phen nhiều vô số kể, chuyện này quả thực nằm ngoài dự kiến nhưng lại vô cùng hợp tình hợp lý.

Thu lại tâm tư suy nghĩ, Lưu An Quốc mở miệng dặn dò: "Ngày kia, tức là ngày 9 tháng 4, em Vương Kim Dương của Đại học Võ thuật Nam Giang sẽ quay trở lại trường để giải đáp thắc mắc trước kỳ thi cho mọi người. Chắc hẳn các em đều đã biết tin tức này rồi, nhớ kỹ đến lúc đó phải đi tham dự đầy đủ đấy nhé."

Mọi người vội vàng gật đầu lia lịa, có tiền bối đi trước về truyền thụ kinh nghiệm thực chiến quý báu, đối với mọi người ít nhiều đều mang lại sự trợ giúp vô cùng to lớn.

"Đến lúc đó, nhà trường sẽ phát thời gian biểu cụ thể của các kỳ thi sát hạch võ khoa, cũng như các hạng mục cần chú ý cẩn trọng, các em phải xem cho thật kỹ càng."

Lưu An Quốc tuy là giáo viên chủ nhiệm của cả lớp, nhưng mô hình lớp học phổ thông hướng tới đại chúng học sinh như thế này chủ yếu vẫn là giảng dạy các kiến thức văn hóa, võ khoa chỉ thỉnh thoảng nhắc tới một vài nét sơ lược mà thôi.

Tuy nhiên nhà trường có mở lớp bồi dưỡng võ khoa, bên ngoài xã hội cũng có các lớp phụ đạo võ khoa chuyên nghiệp, đó mới chính là trọng tâm học tập của các học sinh có chí hướng thi võ khoa.

Những người khác ít nhiều đều từng tham gia các khóa học đó, hoặc dứt khoát thuê cả gia sư võ khoa về tận nhà kèm cặp.

Trong số những người đang có mặt ở đây, Lưu An Quốc quét mắt nhìn một vòng, e rằng chỉ có mỗi mình Phương Bình là chưa từng tham gia bất kỳ khóa học nào.

Điểm này chẳng cần hỏi cũng biết, nếu thực sự từng đi học thì Phương Bình không nói ra, bố cậu ta khi đi họp phụ huynh cũng không đến mức giấu giếm không hé răng nửa lời.

Trong lòng khẽ thở dài một tiếng, Lưu An Quốc bỗng nhiên đứng dậy rời khỏi chỗ ngồi, cúi người mở ngăn tủ dưới bàn làm việc của mình ra.

Một lát sau, Lưu An Quốc đứng thẳng dậy, trên hai tay ôm một chồng sách dày cộp, đặt "bịch" một tiếng lên mặt bàn làm việc, quay sang nói với Phương Bình: "Em xem xem có cuốn nào cần dùng tới không. Các bạn khác đều đã từng tham gia lớp bồi dưỡng võ khoa của trường, những tài liệu này các bạn ấy đều có đủ cả rồi, bên em còn thiếu thứ gì thì cứ cầm về mà xem trước."

Phương Bình hơi có chút bất ngờ ngạc nhiên, thế nhưng đây quả thực chính là những thứ mà hắn đang vô cùng cấp bách cần dùng tới lúc này. Nghe vậy, hắn vội vàng cúi đầu cảm kích: "Em cảm ơn thầy nhiều lắm ạ!"

Lưu An Quốc không hề dài dòng kể công về chuyện này. Mặc dù số tài liệu này giá cả không hề rẻ mạt chút nào, cho dù có ra hiệu sách bên ngoài mua thì cũng phải tốn tới mấy trăm tệ, nhưng đối với những học sinh có gia cảnh bần hàn nghèo khó, có thể chiếu cố giúp đỡ được chút nào thì người làm thầy như ông cũng chẳng ngại ngần đưa tay giúp đỡ một chút ân huệ nhỏ nhoi.

Thấy Phương Bình không hề khách khí chối từ, mặt mày hớn hở ôm trọn toàn bộ chồng sách vở tài liệu vào lòng, Lưu An Quốc có chút dở khóc dở cười.

Nhìn tình hình này thì e rằng thằng nhóc này thực sự chẳng có chút chuẩn bị nào trong đầu cả, nếu không thì một số cuốn sách mang tính chất phổ cập đại trà thế kia việc gì phải ôm hết mang đi làm gì.

Mặc dù trong lòng không ôm quá nhiều hy vọng đối với Phương Bình, nhưng với tư cách là giáo viên chủ nhiệm, Lưu An Quốc do dự một lát rồi vẫn quay sang nói với Ngô Chí Hào: "Em Phương Bình hiểu biết về kỳ thi võ khoa không bằng các em, kiến thức về kỳ thi chuyên nghiệp cũng chưa nắm bắt được bao nhiêu.

Những cuốn sách này bây giờ muốn đọc hết sạch toàn bộ thì e rằng độ khó quá lớn. Ngô Chí Hào, em xem xem cuốn vở ghi chép ôn thi chuyên nghiệp của em có thể cho Phương Bình mượn đi photo một bản được không?"

So với sách vở giáo trình dày cộp, những cuốn sổ tay ghi chép do chính các học sinh ôn thi võ khoa tự mình đúc kết lại có hiệu quả vượt trội hơn rất nhiều!

Trọng tâm sát hạch ở đâu, quy nạp thống nhất các dạng câu hỏi thế nào, những thứ tinh túy đó đều do chính bản thân các học sinh tự tay đúc kết chắt lọc lại.

Ngô Chí Hào là học sinh có thành tích xuất sắc nhất lớp 12 ban 4, hy vọng thi đỗ võ khoa cũng là lớn nhất.

Mượn được cuốn sổ tay ghi chép của cậu ta để ôn tập thì có thể tiết kiệm được biết bao nhiêu thời gian và tâm sức quý báu.

Tuy nhiên sổ ghi chép là tài sản cá nhân riêng tư của học sinh, cho dù là giáo viên chủ nhiệm đi chăng nữa cũng không có quyền hạn cưỡng ép yêu cầu, chỉ có thể dùng lời lẽ thương lượng bàn bạc.

Ban đầu Lão Ban tặng sách cho mình, Phương Bình đã cảm thấy vô cùng cảm kích mang ơn rồi, không ngờ Lão Ban lại còn chủ động mở lời với Ngô Chí Hào để xin photo sổ tay ghi chép cho mình nữa.

Ở kiếp trước, giáo viên chủ nhiệm của hắn cũng là một người thầy tốt, nhưng thành tích của Phương Bình lúc đó chỉ ở mức làng nhàng nửa nạc nửa mỡ, quan hệ với Lão Ban cũng rất bình thường, không tiếp xúc giao lưu nhiều.

Không ngờ tới thế giới này, người thầy chủ nhiệm lại có tinh thần trách nhiệm cao hơn nhiều so với hắn tưởng tượng.

Phương Bình hắn tự mình không chuẩn bị chu đáo thì đâu phải là trách nhiệm của người làm thầy giáo như ông, tặng sách đã là phần ân tình phụ thêm rồi, bây giờ lại còn chủ động đứng ra giúp hắn hỏi mượn vở ghi chép nữa.

Phương Bình không đợi Ngô Chí Hào kịp mở miệng, vội vàng xua tay nói: "Thầy Lưu ơi, không cần phiền phức thế đâu ạ..."

Lời hắn còn chưa dứt, Ngô Chí Hào ở bên cạnh đã nở nụ cười hào sảng nói: "Không sao đâu, lát nữa cầm vở của tớ đi photo một bản là được, cũng chẳng phải bí kíp ghê gớm gì cho cam.

Nói một câu thực tế một chút, có dùng tới được hay không còn là cả một vấn đề đấy chứ."

Ngô Chí Hào cũng chẳng sợ làm tổn thương lòng tự trọng của Phương Bình, trên thực tế ai nấy đều hiểu rõ như ban ngày, ngay cả bản thân Ngô Chí Hào cũng chưa chắc đã có hy vọng lọt vào cửa ải thứ tư — Chuyên nghiệp khảo.

Thầy chủ nhiệm đã mở lời rồi, Ngô Chí Hào cũng không muốn gạt phăng đi thể diện của thầy.

Ngô Chí Hào đã nói đến nước này rồi, Phương Bình cũng không thèm kiểu cách khách sáo làm bộ làm tịch nữa, vội vàng cất lời cảm ơn rối rít.

Quả thật, nhìn đống sách vở tài liệu chất đống trong tay, Phương Bình đầu óc cũng to như cái đấu.

Có thể mượn được cuốn sổ ghi chép của Ngô Chí Hào để tham khảo, hắn cũng có thể biết được những trọng tâm kiến thức nào cần phải học, không đến mức mù mịt rối bời, phải cắm đầu cắm cổ đọc sạch từ đầu đến cuối toàn bộ chồng sách kia.

Nói xong xuôi những chuyện này, việc báo danh coi như hoàn tất tốt đẹp.

Lưu An Quốc bảo mấy người quay trở lại lớp học, còn bản thân mình thì tiếp tục cúi đầu chấm bài thi dang dở.

……

Bước ra khỏi văn phòng giáo viên, Ngô Chí Hào chủ động quay sang nói với Phương Bình: "Mấy cuốn sổ ghi chép đó của tớ có một số để ở nhà, nếu cậu đang cần gấp thì tối nay cùng tớ về nhà lấy, còn nếu không gấp thì ngày mai tớ mang đến lớp cho cậu."

Đã nhận ân tình của người ta rồi, Phương Bình làm sao còn mặt mũi nào mà để đối phương phải cất công mang tới cho mình nữa, vội vàng nói: "Tối nay tớ qua nhà cậu lấy là được rồi, lần này thật sự cảm ơn cậu nhiều lắm."

"Đừng khách khí làm gì, đều là bạn học cùng lớp với nhau cả mà."

Ngô Chí Hào hoàn toàn không có vẻ kiêu ngạo tự phụ của học sinh giỏi, cười ha hả nói: "Lớp thường của chúng mình, xác suất thi đỗ võ khoa quá đỗi nhỏ bé mong manh, chúng mình vốn dĩ đâu phải là đối thủ cạnh tranh sống còn của nhau.

Tuy nhiên tớ nói một câu thật lòng thế này, cậu đừng để bụng nhé.

Ít nhất là trước khi vượt qua được kỳ khám thể chất, đống tài liệu này cậu hoàn toàn không cần phải tốn công đọc làm gì cho mất thời gian.

Đợi đến khi khám thể chất đậu rồi, cậu hẵng dành nhiều thời gian hơn vào đống kiến thức này.

Kỳ thi chuyên nghiệp của võ khoa tuy rằng các hạng mục thi cử rất tạp nham, nội dung thi lại nhiều, nhưng so với văn khoa thì có đôi chút khác biệt: Nội dung sát hạch hàng năm đại thể đều xoay quanh những thứ cơ bản đó mà thôi.

Thực ra đối với những học sinh thi võ khoa như chúng mình, cửa ải khó khăn nhất không phải là chuyên nghiệp khảo hay các môn văn hóa, mà mấu chốt vẫn nằm ở khám thể chất và kiểm tra thực tế.

Mấy thứ này hầu như đều là những yêu cầu cứng ngắc, cũng chính là hai cửa ải có tỷ lệ đào thải tàn khốc nhất."

Ngô Chí Hào vừa dứt lời, Dương Kiến đi bên cạnh liền buồn bực thốt lên: "Thế á? Sao tao lại thấy thi chuyên nghiệp với thi văn hóa khó muốn chết vậy trời?"

Ngô Chí Hào lười thèm đoái hoài tiếp lời tên này, chuyện này mỗi người một cảm nhận, kẻ trí thấy trí người nhân thấy nhân.

Phương Bình lại gật đầu lia lịa, hắn bây giờ chỉ là một tấm chiếu mới toanh, lắng nghe thật nhiều kinh nghiệm quý báu của những người đi trước này hoàn toàn chẳng có gì thiệt thòi cả.

Suy nghĩ một chút, Phương Bình cất tiếng hỏi: "Cái đó... kiểm tra khí huyết thì phải đến đâu để kiểm tra vậy?"

Là một thí sinh võ khoa đột ngột nhảy ngang vào cuộc chơi, Phương Bình không cảm thấy sự thiếu hiểu biết của mình có vấn đề gì đáng xấu hổ cả.

Những người khác quả thực cũng không cảm thấy bất ngờ, Dương Kiến lập tức nhanh nhảu đáp: "Máy đo khí huyết để kiểm tra thì ở Dương Thành chúng mình chỉ có duy nhất Bệnh viện Nhân dân Số 1 mới có thôi. Cái thứ máy móc đó giá thành chế tạo quá đỗi đắt đỏ, Dương Thành chúng mình rốt cuộc cũng chỉ là thành phố nhỏ, số lượng người dùng tới không nhiều, cho nên căn bản chẳng có sự lựa chọn nào khác cả."

Dương Kiến vừa dứt lời, Trương Hạo cũng lập tức lên tiếng nhắc nhở: "Phương Bình, tớ mà là cậu thì tớ chẳng dại gì mà đi kiểm tra đâu, không phải tớ đả kích cậu đâu nhé, dù sao bây giờ cậu có muốn bồi bổ khí huyết thì cũng chẳng kịp nữa rồi.

Cái thứ đó chi phí kiểm tra đắt đến cắt cổ, 5000 tệ một lần, giá chuẩn không bớt một xu.

Khoảng cách đến ngày khám thể chất cũng chẳng còn bao xa nữa, chi bằng cứ dứt khoát đợi đến lúc khám thể chất rồi hẵng xem kết quả luôn thể."

"5000 tệ á?"

Phương Bình tặc lưỡi kinh hãi, cái này mẹ nó chứ chẳng khác nào đi cướp cạn ban ngày giữa phố à!

Thế nhưng đây là việc làm ăn độc quyền độc nhất vô nhị, đối với những thí sinh đang ráo riết chuẩn bị thi võ khoa mà nói, việc nắm bắt trước tình hình sức khỏe thực tế của bản thân là điều bắt buộc phải làm, cho nên bệnh viện cũng chẳng bao giờ phải lo lắng chuyện thiếu khách hàng.

Vốn dĩ Phương Bình còn muốn đi đo đạc tìm hiểu rõ ràng tình hình bản thân một chút, giờ nghe thấy cái giá trên trời này thì đành ngậm ngùi từ bỏ ý định đó.

Có lẽ nhìn ra được tâm tư suy tính của Phương Bình, Ngô Chí Hào bỗng nhiên mỉm cười nói: "Máy đo khí huyết ở bệnh viện là loại máy cỡ lớn chuyên dụng, có thể đo lường chính xác từng dao động biến thiên của khí huyết, cũng như trị số khí huyết lúc đạt đỉnh cao nhất.

Tuy nhiên cậu chắc hẳn là lần đầu tiên đi kiểm tra, thực ra cũng không cần thiết phải đo đạc chi tiết tỉ mỉ đến mức độ như vậy làm gì.

Tối nay cậu không phải qua nhà tớ lấy sổ ghi chép sao?

Nhà tớ có một chiếc máy đo khí huyết mini cỡ nhỏ, chỉ có điều sai số hơi lớn một chút, dao động lên xuống trong khoảng chừng 5 cal, cậu có thể dùng thử xem sao."

"Vãi chưởng, Chí Hào, nhà cậu còn sắm cả cái thứ máy móc này cơ á?"

Lời Ngô Chí Hào vừa dứt, những người khác đều không khỏi trố mắt kinh ngạc thốt lên.

Mặc dù máy đo khí huyết cỡ nhỏ không đắt đỏ bằng máy cỡ lớn ở bệnh viện, sai số càng lớn thì giá thành lại càng rẻ hơn, loại sai số 5 cal này đã được coi là sai số tương đối lớn rồi.

Thế nhưng cho dù có như vậy đi chăng nữa, loại thiết bị đo lường đặc thù này cũng vô cùng đắt đỏ.

Ít nhất trong mắt đám học sinh bọn họ, đó đã là một khoản tiền khổng lồ khiến người ta phải giật mình kinh hãi.

Giống như loại máy móc trong nhà Ngô Chí Hào, loại rẻ nhất trên thị trường cũng phải tốn tới mấy chục vạn tệ.

Ngô Chí Hào nở nụ cười không mấy để tâm đáp: "Đồ cũ mua lại thôi mà, thực ra cũng chẳng đáng bao nhiêu tiền đâu. Cộng thêm việc tớ phải thường xuyên kiểm tra định kỳ, mỗi lần chạy ra bệnh viện vừa tốn kém lại vừa mất thời gian, cho nên bố tớ mới cất công lùng sục mua lại một chiếc máy cũ cho tớ, chủ yếu là để đo đạc áng chừng đại khái thôi."

Đây đúng là lời nói thật lòng, đối với những người như bọn họ, điều cần nhất chính là độ chuẩn xác tuyệt đối.

Sai số lên xuống tận mấy cal như thế này thì quả thực là quá thiếu chính xác.

Đám người đang đứng ở đây nếu thực sự kéo nhau qua nhà Ngô Chí Hào kiểm tra, e rằng số liệu của mọi người rất có thể sẽ hiển thị y hệt như nhau.

Thậm chí quá đáng hơn nữa, kết quả cuối cùng đo ra khéo Dương Kiến còn cao điểm hơn cả Ngô Chí Hào cũng là chuyện hết sức bình thường.

Nếu như thực sự căn cứ vào cái bảng số liệu sai lệch này để lên kế hoạch ôn thi chuẩn bị thì cứ việc nằm đó mà chờ bị đánh rớt đài đi.

Thế nhưng đối với những người khác thì nó vô dụng, còn đối với Phương Bình thì lại có tác dụng vô cùng to lớn!

Phương Bình hiện tại mục đích chủ yếu chính là muốn xem xem, 1.1 điểm khí huyết kia của mình rốt cuộc có thể quy đổi thành bao nhiêu cal trong hiện thực, chỉ cần biết được một khoảng phạm vi đại khái là đã quá đủ rồi.

Nghe Ngô Chí Hào nói như vậy, Phương Bình vội vàng tươi cười hớn hở nói: "Vậy thì làm phiền cậu quá rồi, tớ thật sự chẳng biết phải cảm ơn cậu thế nào cho xiết nữa. Không nói nhiều làm gì, đợi sau này tớ thi đỗ rồi, nhất định sẽ bao cậu một bữa tiệc linh đình hoành tráng!"

"Hahaha..."

Trương Hạo lập tức cười phá lên, trêu chọc: "Phương Bình ơi là Phương Bình, tớ chỉ sợ Ngô Chí Hào đợi đến mốc mồm cũng chẳng đợi nổi bữa đại tiệc này của cậu đâu."

"Lượn sang một bên đi." Phương Bình tràn đầy tự tin khí phách nói: "Tao nhất định sẽ thi đỗ, điểm này căn bản không cần phải nghi ngờ gì hết."

"Hahaha..."

Mọi người lại một lần nữa cười ầm lên, cũng không hẳn là chế giễu cười nhạo gì, chỉ cảm thấy Phương Bình thằng nhóc này quả thực quá mức tự tin tràn trề. Trong số 8 người đang có mặt ở đây, e rằng ngay cả Ngô Chí Hào cũng chẳng dám vỗ ngực khẳng định một trăm phần trăm mình tuyệt đối sẽ thi đỗ.

Cười đùa một hồi, Trương Hạo lại quay sang dặn Ngô Chí Hào: "Chí Hào, tối nay Phương Bình qua nhà cậu kiểm tra, ngày mai nhớ phải báo kết quả cho bọn tớ biết với đấy nhé.

Tuy rằng không chuẩn xác lắm, nhưng đo đi đo lại nhiều lần thì cũng có thể áng chừng ra được kết quả đại khái thôi."

Mọi người đối với trị số khí huyết của Phương Bình vẫn có chút tò mò hiếu kỳ, thuần túy chỉ là tính tò mò thông thường mà thôi, giống như những kỳ thi kiểm tra bình thường, bạn đối với điểm số của các bạn học khác cũng luôn cảm thấy tò mò muốn biết vậy."""
    }
}

def main():
    conn = sqlite3.connect("data/novels.db")
    cur = conn.cursor()
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    total_vi_chars = 0
    total_raw_chars = 0
    
    print("=" * 60)
    print("BẮT ĐẦU CẬP NHẬT PHƯƠNG ÁN B - BATCH 2 (CHƯƠNG 6 - 10)")
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
    print(f"HOÀN TẤT BATCH 2! Tổng raw: {total_raw_chars:,} ký tự | Tổng dịch: {total_vi_chars:,} ký tự")
    print("=" * 60)

if __name__ == "__main__":
    main()
