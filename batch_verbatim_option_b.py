# -*- coding: utf-8 -*-
"""
DỊCH THEO PHƯƠNG ÁN B (VERBATIM 100% NGUYÊN VĂN TỪNG CÂU TỪNG CHỮ)
Tác phẩm: Toàn Cầu Cao Võ (全球高武) - Lão Ưng Cật Tiểu Kê (老鹰吃小鸡)
Lưu toàn văn 100% nguyên bản chữ Hán từ Piaotia vào raw_content.
Bản dịch tiếng Việt văn phong cao võ trau chuốt, đầy đủ từng câu độc thoại và hội thoại.
Batch 1: Chương 1 đến Chương 5.
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
        if l == title or l == f"全球高武 {title}":
            continue
        filtered.append(l)
        
    return title, "\n\n".join(filtered)

# DỮ LIỆU DỊCH FULL VERBATIM CHƯƠNG 1 - 5
CHAPTERS_DATA_VERBATIM = {
    1: {
        "url": "https://www.piaotia.com/html/9/9640/6523755.html",
        "title_vi": "Chương 1: Kịch Bản Không Đúng",
        "content_vi": """Ngày 5 tháng 4 năm 2008.

Thứ Bảy.

Phòng học lớp 12 ban 4, trường Trung học Số 1 Dương Thành.

Phương Bình mất tròn nửa tiếng đồng hồ mới xác định được một chuyện: Đây không phải là nằm mơ, cũng không phải là đang đóng phim — nhảm nhí, đóng phim mà có thể làm cho đám bạn học của mình đồng loạt cải lão hoàn đồng thế này thì đoàn làm phim này có thể bay lên trời luôn rồi!

Sau khi xác định được sự thật mình đã trùng sinh, Phương Bình thoáng có chút thỏ thỏ bất an trong chốc lát, nhưng ngay sau đó liền thản nhiên đón nhận.

Là một thanh niên ngũ độc của thế kỷ mới, ai mà chẳng có chút ít "kinh nghiệm trùng sinh"?

Dù bản thân chưa từng trùng sinh thì trên mạng cũng đầy rẫy tiểu thuyết, chỉ cần đọc lướt qua là biết: Đây chính là pháp bảo chí cao vô thượng để đám lùn xí trai nghèo hèn nghịch tập trở thành cao phú soái!

Huống chi, kiếp trước mình tiền chẳng có, gái cũng không, trùng sinh lại một đời chẳng làm gì cũng có thể sống thêm được bao nhiêu năm, tính kiểu gì cũng thấy lời to chứ không lỗ.

Khó khăn lắm mới chịu đựng được đến khi tiếng chuông tan học vang lên, người thầy giáo mang dáng vẻ vừa quen thuộc lại vừa có chút xa lạ kia cố tình kéo dài tiết học thêm mấy phút nữa mới lưu luyến rời đi.

Còn về câu nói cuối cùng của thầy giáo lúc bước ra khỏi cửa, Phương Bình chỉ coi như lỗ tai mình nghe nhầm:

"Báo danh Võ khoa, tuần sau sẽ bắt đầu, những em nào có ý định thì chuẩn bị cho tốt."

Phương Bình căn bản không để tâm, hắn nghe nhầm thành báo danh "Văn khoa". Thi đại học đều phải báo danh trước, nhưng bình thường đều do nhà trường làm thay, việc gì phải nhắc nhở thêm làm gì.

Mấu chốt của mấu chốt là: Lớp 12 ban 4 là lớp ban tự nhiên (Khối A), thì liên quan cái quái gì đến Văn khoa?

Thế nhưng, vừa mới trải qua chuyện trùng sinh long trời lở đất, Phương Bình làm sao còn hơi sức đâu mà để ý đến chuyện hạt mè hạt vừng này.

Lúc này, điều Phương Bình đang nghĩ trong đầu phải là: Đấm gục Jack Ma, đá văng Mã Hóa Đằng mới đúng chứ!

Mặc dù mốc thời gian năm 2008 này có hơi muộn một chút, nhưng kẻ trùng sinh mà không làm ra được chuyện gì kinh thiên động địa vượt ngoài dự liệu của người đời thì sao có thể xứng danh là người trùng sinh?

Hay là không theo con đường kinh doanh nữa, chuyển sang đi làm chính trị?

Phương Bình âm thầm tính toán trong lòng, cũng chẳng có tâm trí đâu mà tán gẫu với đám bạn học xung quanh.

Đám thanh thiếu niên non choẹt này làm sao có thể tưởng tượng nổi mục tiêu hùng vĩ trong đầu mình. Kể từ ngày hôm nay trở đi, chúng ta đã không còn là người của cùng một thế giới nữa rồi!

Đúng lúc Phương Bình đang mải mê thêm gạch thêm ngói cho bản kế hoạch tương lai huy hoàng của mình, cậu bạn Dương Kiến ngồi bàn phía trước — vóc người vạm vỡ, vai u thịt bắp — đột nhiên quay đầu lại hỏi:

"Phương Bình, Trần Phàm, hai đứa mày có báo danh không?"

Phương Bình ấn tượng với Dương Kiến này vô cùng sâu sắc, không phải vì Dương Kiến đẹp trai ngút trời gì cho cam.

Mấu chốt là ở chỗ: Sau khi tốt nghiệp đại học, trong một buổi họp lớp cấp ba, thằng nhóc Dương Kiến vừa mới tốt nghiệp không biết học đòi ở đâu mà nuôi nguyên một bộ râu quai nón rậm rạp xồm xoàm, suýt chút nữa làm Phương Bình tưởng bố của Dương Kiến cũng đến tham gia họp lớp cùng con trai!

Kể từ lần đó, Phương Bình không bao giờ quên được người bạn râu quai nón này, đặc điểm nhận dạng quá đỗi rõ ràng.

Trong lòng đang mải suy nghĩ chuyện lớn, Phương Bình nhất thời cũng chưa kịp tiếp lời.

Cậu bạn cùng bàn của Phương Bình — một trong hai thành viên của nhóm "Bình Phàm Nhị Nhân Tổ" (Bộ đôi Bình Phàm) do cả lớp gán ghép — Trần Phàm, lúc này lại lắc đầu nói:

"Tao không báo danh đâu, tốn tiền vô ích. Báo danh một cái mất đứt một vạn tệ, chắc chắn là thi không đỗ rồi. Từng ấy tiền, tiền sinh hoạt phí cộng với tiền học phí cả một năm đại học cũng gần như đủ rồi."

Dương Kiến khẽ thở dài có chút tiếc nuối: "Cũng đúng, nhưng trong lòng cứ thấy không cam tâm thế nào ấy. Không thử một lần, chỉ sợ cả đời này sẽ phải hối hận."

Bạn cùng bàn của Dương Kiến cũng là một nam sinh, tên là gì thì trong trí nhớ Phương Bình có hơi mờ nhạt, lúc này cũng quay lại gia nhập cuộc thảo luận, sắc mặt ảm đạm nói:

"Đây là cơ hội duy nhất để chúng ta cá chép hóa rồng, đáng tiếc là chẳng liên quan gì đến chúng ta cả."

Ba người kẻ thì xuýt xoa, người thì tiếc nuối, khiến Phương Bình ngồi bên cạnh nghe mà đầu óc quay cuồng, chẳng hiểu mô tê gì cả.

Báo danh?

Chẳng lẽ là "Văn khoa" mà lúc nãy thầy giáo vừa nói?

Lệ phí báo danh mà mất đứt một vạn tệ?!

Đây là năm 2008 đấy! Nếu nhớ không nhầm thì giá nhà ở khu trung tâm huyện Dương Thành lúc này cũng chỉ tầm 4.000 tệ một mét vuông, thi đại học báo danh cái gì mà cần nhiều tiền đến mức đó?

Mấy tên này không nói nhầm đấy chứ?

Hay là bị bọn lừa đảo nào dắt mũi rồi?

Phương Bình vừa định mở miệng xen vào hỏi cho ra nhẽ, cậu bạn cùng bàn Trần Phàm đã đưa tay đẩy gọng kính cận, sắc mặt kiên nghị nói:

"Cho dù không thi đỗ Võ khoa mà đi thi Văn khoa, thì cũng chưa chắc cả đời này không thể ngẩng đầu làm người! Ngoài xã hội cũng có các lớp bồi dưỡng võ đạo mà, đợi sau này chúng ta tốt nghiệp đại học, kiếm ra tiền rồi, lúc đó đi học nâng cao cũng được. Dù không bằng được đám sinh viên Võ khoa chính quy, nhưng chí ít vẫn còn có hy vọng!"

Lời này vừa thốt ra, bạn cùng bàn của Dương Kiến cũng kích động phụ họa: "Đúng đấy! Thi đỗ vào một trường đại học Văn khoa danh tiếng, sau này tốt nghiệp ra trường lương bổng đãi ngộ cũng đâu có thấp!"

"Tao vẫn muốn thử một lần xem sao..." Dương Kiến có chút do dự. Gia cảnh nhà hắn cũng thuộc diện khá giả, lại thêm thân hình cường tráng vạm vỡ, không thử sức một phen thì thực sự không cam lòng.

Đối với việc Dương Kiến muốn thử sức, hai người Trần Phàm cũng không khuyên can thêm. Mặc dù hy vọng vô cùng mong manh, nhưng cơ hội đang bày ra ngay trước mắt, luôn có những người không cam tâm chịu an phận. 

Dù mọi người đều còn trẻ tuổi bồng bột, nhưng trong lòng ai cũng hiểu: Lúc này mà mở miệng can ngăn Dương Kiến, nếu lỡ làm Dương Kiến bỏ lỡ cơ hội đổi đời thì chẳng khác nào kết thành huyết hải thâm thù.

Ba người bàn luận sôi nổi như lửa cháy, thế nhưng Phương Bình ngồi bên cạnh lúc này lại ngây ngốc toàn tập.

Tình huống gì thế này?

Nuốt nước bọt một cái ực, Phương Bình nhìn chằm chằm ba người một hồi lâu, không hề thấy có chút biểu cảm đùa giỡn nào trên mặt họ. Đến lúc này, Phương Bình rốt cuộc mới nhận ra có điều gì đó sai sai, sai quá sai rồi!

Đang định mở miệng hỏi thì lại bị người khác cướp lời.

Bàn học bên cạnh Phương Bình vốn có hai nam sinh đang thì thào to nhỏ với nhau, lúc này chắc cảm thấy hai người thảo luận không đủ đã. 

Đợi đám Phương Bình bên này vừa yên ắng lại một chút, một nam sinh đầu đinh ở bàn bên liền lộ vẻ mặt kích động, hưng phấn không kìm nén nổi quay sang nói lớn:

"Dương Kiến, Trần Phàm, tối qua hai đứa mày có lên mạng xem tin tức thời sự không đấy?"

Hai người Dương Kiến lắc đầu. Sắp thi đại học đến nơi rồi, ở nhà bố mẹ quản thúc nghiêm ngặt vô cùng, làm gì có thời gian mà lên mạng chơi bời.

Thấy hai người không biết chuyện gì, Phương Bình cùng nam sinh kia cũng ngơ ngác mịt mù, nam sinh đầu đinh lập tức cười ha hả nói:

"Tiếc quá đi mất! Tối qua nổ ra một tin chấn động toàn cầu luôn đấy!

Mấy đứa mày có biết không?

Mã Tông Sư... đột phá Bát Phẩm rồi!

Mã Tông Sư năm nay còn chưa đầy 40 tuổi, đã là cường giả võ đạo đệ nhất của thế hệ thanh niên nước ta!

Hôm qua, Tập đoàn Chim Cánh Cụt (Tencent) đã chính thức gửi chiến thư khiêu chiến tới ngài Thâm — Tổng giám đốc khu vực Châu Á Thái Bình Dương của Google, một cường giả Bát Phẩm lâu năm lão làng!"

"Cái gì?!"

"Thật hay giả đấy?!"

"Mã Tông Sư đột phá Bát Phẩm rồi sao? Không phải mấy năm trước ông ấy mới đột phá Thất Phẩm thôi à?"

"Không thể tin nổi!"

"Trương Hạo, mau nói tiếp đi! Là công khai khiêu chiến hay là giao đấu bí mật?"

"Trận chiến của cường giả Bát Phẩm... Muốn đi xem quá đi mất, đáng tiếc là loại người như chúng ta căn bản không có cửa, không có tư cách đến quan chiến..."

Học sinh lớp 12 sắp thi đại học, giờ tan học lên mạng không nhiều, cho nên tin tức bùng nổ đêm qua tuy đã gây chấn động dữ dội ngoài xã hội, nhưng trong lớp học số người biết chuyện lại không có mấy ai.

Nam sinh đầu đinh — chính là Trương Hạo — giọng nói lúc nãy không hề nhỏ. 

Hắn vừa dứt lời, nhóm Phương Bình còn chưa kịp tiếp lời thì đám bạn học xung quanh nghe thấy đã lập tức phát cuồng lên!

Còn Trương Hạo lúc này vô cùng hưởng thụ cảm giác vạn người chú ý, mặt mày rạng rỡ nói tiếp:

"Là thật một trăm phần trăm! Mã Tông Sư thực sự đã đột phá! Không chỉ có chúng ta, mà toàn bộ thế giới này làm gì có ai dám tin ông ấy lại có thể đột phá Bát Phẩm nhanh đến mức như vậy?

Cho nên chiến thư vừa phát ra, cả thế giới đều chấn động bàng hoàng!

Chỉ cần lần này Mã Tông Sư đánh bại Thâm, Tập đoàn Chim Cánh Cụt có thể gióng trống mở cờ tiến quân vào thị trường các nước Châu Á, trở thành một trong những tập đoàn bá chủ khu vực!

Đợi thêm vài năm nữa, một khi Mã Tông Sư đột phá Cửu Phẩm Tuyệt Đỉnh, thì Tập đoàn Chim Cánh Cụt sẽ chính thức trở thành tập đoàn bá chủ toàn cầu!"

"Trời đất ơi, tốc độ này cũng quá nhanh rồi, Bát Phẩm Tông Sư Cảnh!"

"Bảng xếp hạng Tông Sư cập nhật chưa? Mã Tông Sư phen này chắc chắn lọt vào top 30 rồi!"

"Xời, top 30 cái gì, tao bảo lọt vào top 20 cũng dư sức!"

"Chưa đến mức đấy đâu, Mã Tông Sư dù sao cũng mới vừa đột phá, làm sao leo lên top 20 nhanh thế được, trừ khi đánh bại được Thâm thì mới có hy vọng..."

Lúc này, đám bạn học xung quanh đã bắt đầu chia phe tranh luận rôm rả, trong mắt mỗi một người đều lộ rõ vẻ hưng phấn, sùng bái, kích động và khao khát tột bậc.

Ngay cả đám nữ sinh trong lớp lúc này cũng không ngoại lệ.

Toàn bộ lớp học, kẻ duy nhất lạc lõng ngoại lệ... chính là Phương Bình.

Lúc này, trong đầu Phương Bình như một mớ bột nhão, mặt mày ngơ ngác, cả người chết lặng như hóa đá.

Cái tình huống quái quỷ gì thế này?!

Những lời mọi người vừa nói hắn đều nghe hiểu từng chữ, từng chữ viết ra hắn khẳng định cũng đều nhận biết.

Thế nhưng, tại sao khi xâu chuỗi chúng lại với nhau, hắn lại hoàn toàn không thể nào hiểu nổi?!

Mã Tông Sư là ai?

Tập đoàn Chim Cánh Cụt (Tencent) thì đương nhiên hắn biết thừa, năm 2008 Tập đoàn Chim Cánh Cụt đã là một con quái vật xưng bá ngành IT rồi.

Google thì hắn lại càng biết, không biết mới là lạ.

Ý trong lời nói của Trương Hạo lúc nãy chẳng lẽ là sự cạnh tranh nghiệp vụ giữa Tencent và Google?

Nhưng tại sao... tại sao nó lại quái dị, sai lệch và kỳ cục đến mức độ này?!

Cổ họng Phương Bình giật giật một cái, nuốt nước bọt ừng ực, chỉ cảm thấy bờ môi khô khốc đến lợi hại:

Cái kịch bản này... hình như có chỗ nào đó không đúng lắm rồi!"""
    },
    2: {
        "url": "https://www.piaotia.com/html/9/9640/6523756.html",
        "title_vi": "Chương 2: Nhất Định Phải Thi Võ Khoa!",
        "content_vi": """Trong phòng học.

Phương Bình đầu óc mù mịt, nội tâm thỏ thẻ bất an.

Khó khăn lắm mới đợi đến khi mọi người bàn tán gần xong, Phương Bình khẽ chọc chọc vào sườn cậu bạn cùng bàn Trần Phàm, hạ thấp giọng thì thào:

"Mã... Mã Tông Sư... là Mã Hóa Đằng?"

Sắc mặt Trần Phàm lập tức biến đổi, trong nháy mắt trở nên nghiêm túc dị thường, trịnh trọng nói:

"Phương Bình, gọi thẳng tên húy của Tông Sư, đó là sự bất kính lớn nhất đấy!"

Phương Bình: "..."

Phương Bình lúc này thực sự muốn khóc thành tiếng. Mẹ nó chứ, ngay cả cái tên cũng không được gọi thẳng, uy phong của Tiểu Mã ca ở thế giới này quả thực còn đáng sợ hơn cả Tổng thống!

Tuy nhiên, Phương Bình cũng xác định được một chuyện: Ông chủ của Tập đoàn Chim Cánh Cụt quả nhiên vẫn là Tiểu Mã ca.

Doanh nghiệp đúng, ông chủ cũng đúng, thứ duy nhất sai lệch... chính là cái danh hiệu "Cường giả võ đạo" trong miệng mọi người!

Hắn luôn cảm thấy có một thứ gì đó cực kỳ kỳ quái, đột ngột bị nhét bừa vào giữa thế giới này, khiến hắn cảm thấy nghẹn ứ ở cổ họng, nuốt không trôi nhả không xong.

Đè nén ham muốn phản bác kịch liệt trong lòng, Phương Bình làm bộ như vô tình hỏi:

"Dạo này bận ôn thi đại học quá, tao cũng chẳng xem thời sự tin tức gì cả. Mày kể cho tao nghe chút đi, xem dạo này có chuyện gì thú vị không?"

Trần Phàm không mấy để tâm đáp: "Thì vẫn là mấy chuyện cũ rích trước đây thôi, chỉ có vụ Mã Tông Sư đột phá Bát Phẩm là hơi ngoài dự liệu một chút."

Trần Phàm vốn là người không thích hóng hớt buôn chuyện, thế nhưng Dương Kiến râu quai nón tương lai ngồi bàn trước lại là người khá hoạt ngôn.

Lúc này chuông vào học vẫn chưa reo, Dương Kiến nghe thấy Phương Bình hỏi han, liền quay đầu lại nói nhỏ:

"Tin lớn xác thực thì không nhiều, nhưng mấy hôm trước tao có đọc lướt qua mấy tờ báo lá cải, biết được một chút tin vỉa hè, cũng chẳng biết có chuẩn xác hay không.

Nghe bảo vị Mã đại sư của A Lý (Alibaba - Jack Ma), gần đây có khả năng đã đột phá Thất Phẩm, chính thức bước vào hàng ngũ Tông Sư rồi đấy!

Lý Tông Sư của Bách Độ (Baidu - Robin Li), hình như cũng đang chuẩn bị bế quan để đột phá Bát Phẩm Cảnh. Thời điểm Lý Tông Sư đột phá Thất Phẩm vốn không chênh lệch mấy so với Mã Tông Sư của Chim Cánh Cụt, nhưng mấy năm gần đây tiến cảnh võ đạo của Lý Tông Sư không nhanh bằng Mã Tông Sư, lần này có đột phá được hay không thì khó nói lắm.

À đúng rồi, còn một tin tức nữa, Trương Tổng Đốc của tỉnh Nam Giang chúng ta, rất có khả năng sẽ đột phá Thất Phẩm trong thời gian tới!

Một khi Trương Tổng Đốc đột phá Thất Phẩm thì ghê gớm lắm đấy nhé. Tỉnh Nam Giang chúng ta suy yếu nhiều năm nay, hiện tại chỉ có vài vị lão tiền bối Thất Phẩm Tông Sư trấn thủ một phương. Trương Tổng Đốc tuổi đời còn trẻ, nếu đột phá được thì có hy vọng tiến xa hơn nữa, quét sạch căn bệnh trầm kha võ đạo suy nhược của Nam Giang.

Còn nữa, trước kỳ đại khảo võ khoa năm nay, nghe đâu trường chúng ta có mời một vị học trưởng năm ngoái đỗ vào Nam Giang Võ Khoa Đại Học về trường diễn thuyết cho chúng ta nghe đấy..."

Dương Kiến thao thao bất tuyệt kể hàng tràng tin đồn bát quái, thế nhưng Phương Bình nghe vào tai lại chẳng khác nào đang nghe thiên thư!

Những tin tức lá cải mà Dương Kiến kể, phần lớn đều là tin tức liên quan đến Võ giả!

Người này người nọ có thể sắp đột phá rồi, người kia đang bế quan tu luyện...

Trong số đó, có những cái tên Phương Bình từng nghe qua kiếp trước, không chỉ giới hạn trong giới kinh doanh, mà bao gồm cả giới giải trí, thậm chí cả giới chính trị!

Từ những lời nói vô tình của Dương Kiến, Phương Bình có thể cảm nhận sâu sắc được: Võ giả ở xã hội này có địa vị tôn sùng vô cùng! Cường giả dưới Thất Phẩm thì Dương Kiến đều thêm hậu tố "Đại sư", còn từ Thất Phẩm trở lên thì kính cẩn gọi là "Tông Sư".

Một điểm khác cũng có thể nhận thấy rõ ràng: Phàm là những nhân vật có danh tiếng lẫy lừng trong xã hội, dường như ai nấy đều là cường giả võ đạo!

Hay nói cách khác: Kẻ không phải cường giả võ đạo, thì căn bản không có cửa để nổi danh!

Trong lúc nói chuyện, Phương Bình buột miệng hỏi một câu: "Những người đó mạnh đến mức nào?"

Kết quả là Dương Kiến chẳng thèm khách khí, phán ngay một câu: "Tùy tiện lôi một vị Võ giả ra cũng đủ đấm nát bấy lũ chúng ta thành cái sàng lọc gạo rồi!"

Đợi đến khi tiếng chuông vào học reo lên, nhân lúc thầy giáo còn chưa bước vào lớp, Dương Kiến thoáng thở dài cảm thán:

"Không thi đỗ Võ khoa, không trở thành Võ giả, thì cả đời này coi như xong phim. 

Làm quan không ra khỏi phạm vi thị trấn/huyện thành, làm kinh doanh cũng chỉ loanh quanh một chỗ. Người bình thường muốn ngoi đầu lên... khó lắm thay!"

Lời này vừa thốt ra, Phương Bình lại một lần nữa sững người ngơ ngác.

Còn Trần Phàm vốn nãy giờ ít khi mở miệng, lúc này cũng thoáng vẻ thất vọng, trầm giọng nói nhỏ:

"Võ giả dù sao cũng chỉ là số ít, huống chi đối với loại người như chúng ta, bất kể là theo nghiệp kinh doanh hay chính trị, e rằng cũng chẳng thể đi tới bước đó, việc gì phải bận tâm nhiều làm gì."

Thông qua cuộc đối thoại giữa hai người, Phương Bình lờ mờ cảm nhận được một điều:

Không trở thành Võ giả, theo như cách hiểu của hắn, thì làm quan sẽ không bao giờ leo lên quá cấp Sảnh/Cục (cấp Tỉnh), làm kinh doanh thì buôn bán không thể vượt ra ngoài phạm vi thành phố!

Không biết đây là quy định cứng của pháp luật, hay là quy tắc ngầm mặc định của toàn xã hội.

Thế nhưng bất kể là loại nào, Phương Bình đều cảm nhận được một cỗ ác ý nồng nặc mà xã hội này đang dành cho mình!

Không trở thành Võ giả, không trở thành cường giả, thì cho dù bản thân có là người trùng sinh mang theo tầm nhìn của tương lai đi chăng nữa, e rằng cả đời này cũng chỉ có thể lẹt đẹt lăn lộn ở tầng đáy xã hội!

Mấu chốt là: Lúc này Phương Bình bắt đầu hoài nghi nghiêm trọng, rốt cuộc mình có phải là người trùng sinh hay không?!

Tuy rằng diện mạo bạn học không đổi, tên tuổi không đổi, bao gồm cả những ông trùm lớn, tên các tập đoàn doanh nghiệp đều trùng khớp hoàn toàn.

Thế nhưng đột nhiên lại mọc ra một cái nghề nghiệp cao năng lực như thế này, liệu những thứ khác có thực sự giống như trong ký ức của mình hay không?

Có lòng muốn hỏi thêm vài câu, nhưng lúc này thầy giáo đã bước vào lớp, những người khác đều đã về lại chỗ ngồi ngay ngắn, không ai dám tán gẫu nữa.

Hơn nữa những thứ này trong mắt người khác đều là kiến thức thường thức cơ bản của cuộc sống, Phương Bình cũng không muốn tiếp tục gặng hỏi sâu thêm. Hỏi nhiều quá, khéo đám bạn học này lại tưởng hắn bị mất trí nhớ hay tâm thần phân liệt thì nguy.

Suy nghĩ một lát, nhân lúc thầy giáo quay lưng viết bảng, Phương Bình nghiêng đầu ghé sát tai hỏi nhỏ Trần Phàm:

"Gần trường mình... gần trường còn quán net nào không?"

Trần Phàm dùng ánh mắt kỳ quái liếc nhìn hắn một cái, nhưng vẫn đáp lại một câu: "Đương nhiên là có rồi, chẳng phải trước đây mày hay ra cái quán net Lam Thiên (Trời Xanh) đó sao?"

"Phù..."

Phương Bình thở phào ra một hơi dài, khẽ gật đầu không nói thêm gì nữa. Xem ra vẫn còn có một số thứ giống hệt kiếp trước.

Chẳng hạn như cái quán net có cái tên sến sẩm quê mùa kia vẫn còn tồn tại. Quán net còn ở đó, chứng tỏ có những thứ căn bản không thay đổi, đợi tan học chạy ra quán net tra cứu tài liệu, chắc chắn sẽ tìm được những thông tin mình muốn hiểu rõ!

Thấy Phương Bình thở phào nhẹ nhõm như trút được gánh nặng, Trần Phàm vẫn có lòng tốt nhắc nhở một câu:

"Tuy chúng ta không thi đỗ được Võ khoa, nhưng cũng không thể vì thế mà buông xuôi bỏ cuộc. Thi Văn khoa điểm cao thì vẫn có cơ hội ngẩng đầu làm người, nói không chừng sau này đi làm kiếm được tiền vẫn có cơ hội trở thành Võ giả. Sắp thi đại học đến nơi rồi, quán net thì bớt đi lại thôi..."

Phương Bình mỉm cười gật đầu. Là thành viên của "Bình Phàm Nhị Nhân Tổ", Trần Phàm tuy ít nói nhưng hoàn cảnh hai đứa sàn sàn như nhau, đối với người bạn cùng bàn này vẫn rất mực quan tâm chân thành.

...

Khó khăn lắm mới chịu đựng xong mấy tiết học còn lại của buổi sáng, tiếng chuông tan trường vừa vang lên một cái, Phương Bình đã vội vã lao nhanh ra ngoài cửa lớp.

Lúc này, trong bụng hắn chứa đầy ắp nghi vấn cần được giải đáp ngay tức khắc!

Trần Phàm thấy Phương Bình hấp tấp chạy ra ngoài, vội đuổi theo hỏi với theo sau lưng: "Mày đi ăn cơm hay đi quán net đấy?"

"Quán net!"

"Về sớm đấy nhé, tiết đầu buổi chiều là tiết của thầy chủ nhiệm đấy!"

Phương Bình ậm ừ đáp một tiếng. Bản thân hắn lúc này, vì bố mẹ đều bận đi làm ở xưởng, bữa trưa đều ăn cơm hộp ở quán cơm bình dân gần trường, không cần phải về nhà.

Tranh thủ khoảng thời gian rảnh rỗi giữa trưa, sự tò mò và khát khao hiểu biết mãnh liệt trong lòng khiến hắn hận không thể lập tức bay tới quán net để tìm hiểu những bí mật mà mình chưa từng biết đến!

Rảo bước thật nhanh, Phương Bình đảo mắt nhìn lướt qua khung cảnh xung quanh dọc đường đi.

Y hệt như trong ký ức, trường Trung học Số 1 Dương Thành chẳng có gì khác biệt, bạn bè thầy cô cũng đều rất đỗi bình thường, Phương Bình không hề nhìn thấy ai có khả năng bay lượn phi thiên độn địa hay trèo tường vượt nóc cả.

Nếu muốn nói đến điểm khác biệt, thì đại khái là trong khuôn viên trường học xuất hiện thêm một số khẩu hiệu tuyên truyền và biển hiệu hết sức kỳ quặc:

【Nghênh chiến kỳ thi đại học, Võ khoa ta đến đây!】
【Liều chết một phen, quyết đoạt lấy một suất Võ khoa!】
【Muốn thi Võ khoa, hãy đến Thanh Điểu — Lớp Bồi Dưỡng Võ Đạo Thanh Điểu, sự lựa chọn tối ưu của bạn!】
【Một viên Huyết Khí Hoàn, đảm bảo bạn đỗ thẳng vào Võ khoa!】
...

Nếu không phải những thứ kỳ quái này xuất hiện đường đường chính chính một cách công khai trong sân trường, Phương Bình tuyệt đối có đủ lý do để tin rằng có một lũ thầy cúng bói toán cùng phường bán thuốc dạo lừa đảo đã trà trộn vào trường học!

Thế nhưng nhìn thấy bộ dạng tập quen đến mức coi như lẽ dĩ nhiên của tất cả mọi người xung quanh, Phương Bình hiểu rõ: Đây rốt cuộc đã không còn là cái thế giới đô thị thuần túy trong ký ức của hắn nữa rồi.

Còn về khoảng cách sai lệch rốt cuộc lớn đến mức nào, thì phải đợi chính bản thân hắn đi tìm hiểu rõ ràng thì mới biết được.

...

Mười phút sau, Phương Bình đã có mặt trước cửa quán net Lam Thiên cách trường không xa.

Vẫn là mùi vị quen thuộc của khói thuốc lá lẫn lộn mì tôm, vẫn là tấm biển hiệu quen thuộc ngày nào. 

Cái quán net mà năm xưa trong mắt một học sinh cấp ba nghèo trông vô cùng sang chảnh cao cấp, nay nhìn lại thì thấy tồi tàn rách nát không chịu nổi, bốn chữ "Lam Thiên Võng Ba" trên biển hiệu đã tróc sơn gần như không còn nhìn rõ mặt chữ.

Sải bước bước vào quán net, ngồi sau quầy thu ngân ngay cửa ra vào vẫn là cô bé thu ngân quen thuộc mà có chút xa lạ kia — một cô gái trẻ tuổi hơn hắn vài tuổi.

Nhớ năm xưa, vào cái thời thanh xuân hừng hực hormone bùng nổ, cô bé thu ngân ăn mặc chững chạc hơn học sinh này cũng từng có vài lần lén lút lẻn vào giấc mơ của Phương Bình, cùng hắn làm vài trò mờ ám xấu hổ.

Nay nhìn lại...

Phương Bình tự cảm thấy mắt nhìn người thời thanh xuân của mình chắc chắn có vấn đề, mắt mọc hơi lệch sang một bên rồi.

Cũng phải thôi, nếu thực sự đẹp nghiêng nước nghiêng thành thì việc quái gì phải ngồi đây làm nhân viên thu ngân quán net rách này.

Liếc nhìn cô bé thu ngân một cái, Phương Bình chẳng có tâm trí đâu mà trêu hoa ghẹo nguyệt, cho dù có muốn tán gái thì cái đẳng cấp này cũng chẳng xứng với thân phận cao sang của một người trùng sinh.

Thế nhưng vừa nghĩ đến hai chữ "Mã Tông Sư", cái cảm giác bề trên ngạo nghễ vừa mới nhen nhóm trong lòng lập tức vỡ tan như bong bóng xà phòng!

Người trùng sinh thì đúng là cao sang thật đấy, nhưng mấu chốt là phải trùng sinh đúng chỗ cơ!

Trong lòng tự chế giễu vài câu, Phương Bình cũng không lề mề, đi thẳng vào vấn đề: "Mở một máy, bao nhiêu tiền một tiếng?"

"Ba tệ."

Cô bé thu ngân trả lời dứt khoát, ngay sau đó bồi thêm một câu: "Có thẻ hội viên không? Chưa có thì nạp thẻ hội viên đi, nạp 50 tặng 10 tệ."

Phương Bình bày ra vẻ mặt cao ngạo, chẳng thèm để ý đến cô nàng.

Nạp 50 tệ mà chỉ tặng có 10 tệ, keo kiệt bủn xỉn quá thể đáng!

Huống chi... hai con mắt nào của cô nhìn ra tôi giống người có nổi 50 tệ trong người thế hả?!

Suốt mấy tiết học buổi sáng, Phương Bình đã kiểm kê lại toàn bộ gia tài trên người mình rồi: Tổng tài sản vỏn vẹn đúng 28 tệ chẵn!

Số tiền ít ỏi này bao gồm cả tiền cơm trưa của hắn, có muốn nạp 50 tệ thì cũng phải móc ra được tiền mới nạp được chứ!

Phớt lờ lời mời chào tiếp thị của cô thu ngân, Phương Bình móc từ trong túi quần ra một tờ tiền mệnh giá 5 tệ nhàu nhĩ, đập mạnh lên mặt bàn quầy thu ngân với vẻ mặt đầy kiêu hãnh.

Đương nhiên, cô bé thu ngân cũng chẳng thèm chấp cái loại nghèo kiết xác này, ném xoạch một chiếc thẻ hội viên tạm thời qua mặt bàn rồi chẳng buồn liếc mắt nhìn hắn thêm cái nào nữa.

Phương Bình rất muốn hét to một câu kinh điển: "Đừng khinh thiếu niên nghèo!", nhưng nghĩ lại cấp bậc của cô bé thu ngân này còn quá thấp, câu nói này sau này để dành nói với các đại lão thì hợp hơn. Không thèm so đo với cô nàng nữa, hắn cầm lấy chiếc thẻ tạm thời đi thẳng vào góc tối trong cùng của quán net.

...

Tại một góc quán net.

Màn hình máy tính bật sáng, Phương Bình như kẻ chết khát vớ được dòng suối mát, điên cuồng gõ phím tìm kiếm những thông tin mà mình khao khát muốn biết.

Ánh sáng xanh lét ma mị hắt ra từ màn hình CRT phản chiếu lên gương mặt Phương Bình, khiến thần sắc của hắn lúc này trông có chút u ám rợn người.

Nếu lúc này có ai ngồi gần Phương Bình, chắc chắn sẽ cảm nhận được sự dị thường đến đáng sợ của hắn:

Lúc thì sắc mặt biến đổi khôn lường, lúc thì phẫn uất bất bình, lúc lại nghiến răng nghiến lợi ken két...

Thỉnh thoảng, lại có vài câu chửi thề tục tĩu thốt ra từ miệng Phương Bình, chẳng biết là hắn đang chửi ông trời, hay là đang chửi rủa ai nữa.

Hơn một tiếng đồng hồ sau, máy tính phát ra tiếng bíp rồi tự động khóa màn hình, tiền trong tài khoản đã cháy sạch.

Phương Bình chẳng còn tâm trí đâu mà nạp thêm tiền nữa. Mang theo một bụng mịt mờ xen lẫn chút bàng hoàng đã thấu tỏ sự đời, hắn chậm rãi cất bước bước ra khỏi quán net.

Ngay khoảnh khắc bước chân ra khỏi ngưỡng cửa quán net Lam Thiên, sắc mặt Phương Bình trở nên kiên định dị thường, hai hàm răng nghiến chặt lại thốt ra từng chữ:

"Thi Võ khoa!"

Dường như cảm thấy một câu nói này vẫn chưa đủ để chứng minh cho quyết tâm ngập trời trong lồng ngực mình, Phương Bình lại gằn giọng bồi thêm một câu:

"Nhất định... nhất định phải thi bằng được Võ khoa!"
"""
    },
    3: {
        "url": "https://www.piaotia.com/html/9/9640/6523757.html",
        "title_vi": "Chương 3: Nghèo Văn Giàu Võ",
        "content_vi": """Bên ngoài quán net.

Phương Bình thần sắc kiên định, trong ánh mắt tràn ngập vẻ cố chấp không gì lay chuyển nổi.

Không cố chấp không được!

Thông qua hơn một tiếng đồng hồ lướt web tra cứu thông tin, Phương Bình rốt cuộc cũng đã vỡ lẽ ra được một số chuyện.

Chẳng hạn như: Võ giả rốt cuộc là cái thứ gì?

Võ giả hiện đại so với tiểu thuyết võ hiệp hay phim ảnh kiếm hiệp kiếp trước căn bản không có quá nhiều sự khác biệt, chẳng qua bối cảnh câu chuyện đã được thay thế bằng thời hiện đại mà thôi. Cái nghề nghiệp mang tên Võ giả này, đã đường đường chính chính xuất hiện và tồn tại trong xã hội văn minh thế kỷ 21!

Nếu chỉ đơn thuần là xã hội xuất hiện thêm một nghề nghiệp có năng lực siêu phàm như siêu nhân, thì Phương Bình dù có tò mò thích thú đến mấy, cũng chưa chắc đã nhất quyết phải đâm đầu vào con đường này.

Thế nhưng trong xã hội ngày nay, Võ giả không còn đơn thuần là một nghề nghiệp nắm giữ vũ lực nữa, mà nó đại diện cho QUYỀN LỰC và ĐỊA VỊ tối thượng!

Cá lớn nuốt cá bé, kẻ mạnh ăn thịt kẻ yếu — đó là chân lý ngàn đời bất biến!

Kiếp trước, sự cách biệt giai cấp này kỳ thực thể hiện không quá mức rõ rệt, dù sao mọi người đều chỉ là người phàm bằng xương bằng thịt, một phát súng bắn trúng đầu là ngã gục như nhau.

Thế nhưng trong cái xã hội tràn ngập những cường giả võ đạo có thể tay không xé sắt, đấm vỡ núi non này, khoảng cách giai cấp lại hiển hiện rõ ràng đến mức không thể nào rõ ràng hơn được nữa!

Chẳng hạn như, trước đó Phương Bình nghe Dương Kiến nói câu "Làm quan không ra khỏi phạm vi thị trấn/huyện thành, làm kinh doanh cũng chỉ loanh quanh một chỗ" mà chưa hiểu thấu đáo, thì đến lúc này hắn đã hoàn toàn hiểu rõ ngọn ngành!

Người bình thường chiếm đại đa số trong xã hội này, người bình thường muốn làm bất kỳ ngành nghề nào kỳ thực nhà nước đều không hề cấm đoán.

Thế nhưng theo quy định của pháp luật — đúng vậy, là pháp luật nước Cộng Hòa Nhân Dân Trung Hoa quy định bằng văn bản rõ ràng đàng hoàng!

Một công ty muốn mở rộng quy mô phát triển vượt ra ngoài ranh giới một thành phố, người đại diện theo pháp luật (chủ tịch/pháp nhân) đăng ký trên giấy phép kinh doanh BẮT BUỘC PHẢI LÀ VÕ GIẢ, cấp bậc không giới hạn!

Còn nếu muốn mở rộng kinh doanh vượt ra ngoài phạm vi một tỉnh, người đại diện theo pháp luật bắt buộc phải có cấp bậc võ đạo KHÔNG ĐƯỢC THẤP HƠN TỨ PHẨM!

Theo như tài liệu mà Phương Bình tra cứu được trên mạng internet, võ đạo thời nay được phân chia làm Cửu Phẩm: Nhất Phẩm là thấp nhất, Cửu Phẩm là cao nhất!

Dưới Tứ Phẩm được gọi là Hạ Tam Phẩm (Võ giả sơ cấp); từ Tứ Phẩm đến Lục Phẩm là Trung Tam Phẩm; còn từ Thất Phẩm trở lên bao gồm cả Thất Phẩm, được tôn xưng là Cao Tam Phẩm — những nhân vật này được toàn xã hội cung kính gọi là CƯỜNG GIẢ TÔNG SƯ!

Muốn thành lập một công ty phát triển liên tỉnh, điều kiện tiên quyết đầu tiên: Pháp nhân của công ty phải là một vị cường giả từ Tứ Phẩm trở lên!

Còn muốn trở thành một tập đoàn đa quốc gia vươn tầm thế giới, tuy luật pháp không có văn bản cứng nhắc nào quy định, thế nhưng Phương Bình dạo qua các diễn đàn mạng cũng thừa hiểu: Nếu tập đoàn của anh không có cường giả Thất Phẩm Tông Sư tọa trấn, thì cho dù sản phẩm của anh có tốt đến đâu, người dùng có đông đến mức nào, mạo hiểm nhảy vào thị trường của các quốc gia khác, khu vực khác thì chẳng khác nào đem tiền đi nộp mạng, làm mồi cho cọp!

Cho dù tập đoàn của anh có cường giả Thất Phẩm trở lên, thì anh cũng phải dùng nắm đấm để chứng minh thực lực của mình trước mặt các đối thủ quốc tế!

Chẳng hạn như Tiểu Mã ca (Mã Hóa Đằng) lúc này!

Sản phẩm của Tập đoàn Chim Cánh Cụt ở thế giới này cũng tương tự như kiếp trước, chủ yếu dựa vào phần mềm nhắn tin trực tuyến, và phần mềm QQ cũng y như xưa, là công cụ trò chuyện trên mạng chính yếu của toàn bộ người dân Hoa Hạ.

Thế nhưng... nó cũng CHỈ GIỚI HẠN trong phạm vi lãnh thổ Hoa Hạ mà thôi!

Tập đoàn Chim Cánh Cụt hiện tại thậm chí còn chưa thể vươn vòi bạch tuộc ra toàn bộ Châu Á! Nguyên nhân là bởi trước đây thực lực của Mã Hóa Đằng tuy đã đạt tới Thất Phẩm Tông Sư, thế nhưng với tư cách là một tập đoàn cự đầu thế giới, Google cũng phát triển phần mềm nhắn tin cạnh tranh, và cường giả mà Google phái đến tọa trấn khu vực Châu Á Thái Bình Dương lại là một lão làng Bát Phẩm Tông Sư tên là Thâm!

Mã Hóa Đằng một ngày chưa thể chứng minh được thực lực của mình đủ sức tranh đoạt tài nguyên với Google, thì đừng bao giờ mơ tưởng đến chuyện mở rộng thị trường ra nước ngoài!

Bởi vì một khi bước chân ra khỏi biên giới quốc gia, những nhân viên hay chi nhánh mà anh phái đi mở rộng thị trường rất có thể sẽ bốc hơi biến mất không một dấu vết chỉ sau một đêm!

Chỉ khi nào anh hướng ra thế giới bên ngoài, hướng tới những kẻ cùng ngành chứng minh được rằng bản thân mình sở hữu thực lực ngang ngửa, đủ tư cách ngồi chung một mâm, thì anh mới có thể vững bước mở rộng kinh doanh. Đó cũng chính là lý do vì sao ngay sau khi đột phá Bát Phẩm, Mã Hóa Đằng đã lập tức công khai gửi chiến thư khiêu chiến tới Thâm!

Trận chiến khiêu chiến này, thắng hay bại thực ra không phải là điều quan trọng nhất; điều quan trọng nhất là chứng minh cho toàn thế giới thấy rằng: Mã Hóa Đằng ta nay đã là một tuyệt đỉnh cường giả Bát Phẩm, ta có đủ tư cách để chia phần miếng bánh béo bở này!

Đó là quy tắc của giới thương trường, còn ở các giới khác trong xã hội, thực tế cũng hoàn toàn diễn ra tương tự như vậy.

Chẳng hạn như giới chính trị, so với kiếp trước có đôi chút khác biệt. Quyền lực lớn nhất trong một tỉnh thuộc về vị Tổng Đốc. Một vị Tổng Đốc đầu tỉnh, tiêu chuẩn tối thiểu bắt buộc phải là Tứ Phẩm Võ Giả!

Thế nhưng trên thực tế hiện nay, Tổng Đốc của các tỉnh trên toàn quốc hầu như không có ai dưới Ngũ Phẩm cả! Những tỉnh lớn, tỉnh trọng điểm kinh tế và quân sự, Tổng Đốc đều là các bậc Thất Phẩm Tông Sư cái thế!

Vị Tổng Đốc đương nhiệm của tỉnh Nam Giang chúng ta hiện tại mới chỉ là Lục Phẩm Võ Giả, tuy rằng trong số các Tổng Đốc toàn quốc không phải là kẻ yếu nhất, nhưng cũng chẳng tính là mạnh mẽ gì. Điều này dẫn đến một hệ lụy vô cùng nghiêm trọng: Tỉnh Nam Giang không thể tranh đoạt được nhiều tài nguyên từ nguồn ngân sách quốc gia!

Tài nguyên nhiều hay ít, sẽ quyết định trực tiếp đến mức độ đầu tư và lực lượng bồi dưỡng Võ giả của chính quyền địa phương.

Trước đó trên mạng có tin đồn vỉa hè nói rằng Tổng Đốc Nam Giang sắp sửa đột phá Thất Phẩm, Dương Kiến lúc nãy khi kể lại chuyện này tỏ ra vô cùng hưng phấn, nguyên nhân sâu xa chính là nằm ở chỗ đó! Một vị Tổng Đốc cấp bậc Tông Sư, có thể mang về cho tỉnh nhà vô số tài nguyên tu luyện quý báu!

Chính trị, thương trường, quân đội đều như vậy, cho đến cả giới giải trí và các ngành nghề khác cũng chẳng hề ngoại lệ!

Những Thiên Vương, Thiên Hậu nổi tiếng lẫy lừng trong giới showbiz hiện nay, không chỉ đòi hỏi phải có tài năng ca hát diễn xuất, không chỉ cần nhan sắc nghiêng nước nghiêng thành, mà bắt buộc phải sở hữu thực lực võ đạo không tầm thường chút nào!

Bởi vì nếu anh không có thực lực, anh kiếm được bao nhiêu của cải tiền bạc đi chăng nữa, anh cũng căn bản không có bản lĩnh để giữ được nó!

Trừ phi... sau lưng anh có một người cha là cường giả võ đạo chống lưng!

Đám phú nhị đại, quan nhị đại trong xã hội hiện nay, hầu như đều có một danh xưng chung thống nhất: VÕ NHỊ ĐẠI!

Bởi vì những kẻ có tiền có quyền trong xã hội này, không một ai không phải là những võ giả cường đại!

Người bình thường cũng có một bộ phận cực kỳ ít ỏi có thể leo lên được tầng lớp thượng lưu, nhưng những người này không một ai ngoại lệ, sau lưng họ đều phải có những võ giả cường đại đứng ra bảo kê, hơn nữa bản thân họ cũng phải thể hiện ra giá trị tuyệt đối của mình — một thứ giá trị khắt khe gấp ngàn vạn lần so với tiêu chuẩn dành cho một Võ giả!

Không thể trở thành Võ giả, thì số phận đã định đoạt là vĩnh viễn không có duyên với giới tinh hoa xã hội, vĩnh viễn không có cửa chạm tay vào quyền lực và tiền tài!

Sự chênh lệch giai cấp đến mức tột cùng này, đã tạo nên một làn sóng điên cuồng trong xã hội hiện đại: Tất cả những người bình thường đều khao khát cháy bỏng được một lần trở thành Võ giả!

Dù là một Võ giả yếu ớt nhất, chẳng làm ăn gì cả, chỉ cần treo tên ở một công ty nhỏ ngoài xã hội, thì mỗi năm bổng lộc thu về tối thiểu cũng từ một trăm vạn tệ trở lên!

Trên thực tế, những người thực sự có thể trở thành cường giả võ đạo, không một ai ngoại lệ, đều là tầng lớp tinh anh của xã hội. Những người này trừ phi quy phục dưới trướng những kẻ mạnh hơn, còn không thì rất ít khi chịu đi làm thuê treo tên ăn lương, mà phần lớn đều tự mình đứng ra lập nghiệp kinh doanh. So với người bình thường, ưu thế cạnh tranh của họ quả thực áp đảo toàn diện!

"Không trở thành Võ giả... thì những ý tưởng làm giàu son vàng kiếp trước của mình căn bản chẳng khác nào miếng thịt béo treo trước miệng sói!"

Phương Bình thở dài thườn thượt, chỉ cảm thấy một cảm giác bất lực đắng ngắt trào lên cổ họng. 

Hắn kiếp trước chỉ là một kẻ tầm thường, nếu không trở thành Võ giả, dù có đẻ ra được những ý tưởng kinh doanh thiên tài, thì cũng chỉ là làm bàn đạp dâng trọn cho kẻ khác cướp đoạt mà thôi. 

Vì vậy, thi vào Võ khoa đại học chính là con đường duy nhất, con đường tắt ngắn nhất để một kẻ nghèo hèn xuất thân từ tầng đáy xã hội như hắn bước chân vào giới thượng lưu!

Thế nhưng... thi Võ khoa đâu có dễ dàng như vậy!

Kỳ thi đại học Võ khoa hàng năm ở thế giới này khó khăn gấp trăm lần so với việc thi đỗ vào Thanh Hoa, Bắc Đại ở kiếp trước!

Năm 2007, toàn quốc có 9 triệu thí sinh tham gia kỳ thi đại học, thế nhưng tất cả các trường đại học trên cả nước cộng lại, tổng chỉ tiêu tuyển sinh Võ khoa vỏn vẹn chưa đầy 2 vạn người! Đó là con số tổng hợp của toàn bộ các trường đại học trên cả nước!

Kiếp trước, các trường top đầu như Thanh Hoa, Bắc Đại mỗi năm tuyển vài ngàn người, các trường top 985 cộng lại mỗi năm cũng tuyển cả trăm ngàn sinh viên. 

Còn ở thế giới này, toàn quốc có hơn 100 trường đại học mở khoa võ và học viện chuyên nghiệp võ thuật, hơn 100 trường này chia nhau vỏn vẹn 2 vạn chỉ tiêu, tính bình quân ra mỗi trường quá ít ỏi!

Tỷ lệ chọi xấp xỉ 1/500! Nhìn qua thì có vẻ không quá thấp, nhưng đó là tính ở các đại đô thị; còn ở những huyện thành nhỏ bé nghèo nàn như Dương Thành, tỷ lệ này phải nhân lên gấp mười lần — tức là 1 chọi 5.000!

Đó cũng chính là nguyên nhân chủ yếu khiến những người như Trần Phàm rơi vào tuyệt vọng và cam chịu từ bỏ ngay từ đầu.

Chưa dừng lại ở đó, việc báo danh dự thi Võ khoa còn có vô vàn những ngưỡng cửa khắc nghiệt khác.

Khoản lệ phí báo danh một vạn tệ mà Trần Phàm nói lúc nãy, chỉ là ngưỡng cửa thấp nhất, sơ đẳng nhất mà thôi!

Lúc này những điều kiện khác còn chưa thèm tính đến, chỉ riêng khoản lệ phí báo danh một vạn tệ này thôi cũng đã đủ khiến Phương Bình đau đầu muốn nứt óc!

Mà thời gian tiếp nhận báo danh Võ khoa, tuần sau đã chính thức bắt đầu rồi, thời hạn nộp hồ sơ cũng có giới hạn nghiêm ngặt. Quá thời hạn này, thì dù anh có tiền tấn đi chăng nữa cũng đừng hòng báo danh thi Võ khoa được nữa!

"Một vạn tệ tiền lệ phí báo danh..."

Phương Bình lúc nãy còn đang mang trong mình ngọn lửa dã tâm hùng vĩ ngút trời, lúc này đã ỉu xìu như bánh đa nhúng nước. Mới chỉ là điều kiện khởi đầu thôi mà ngọn lửa trong lòng đã bị tạt cho một gáo nước lạnh buốt tắt ngúm quá nửa.

Đó là còn chưa kể, phía sau còn cả một chuỗi những yêu cầu tốn kém kinh hoàng khác nữa!

"Đau đầu thật chứ lị!"

Phương Bình thở ngắn than dài. Người trùng sinh mà trùng sinh về xã hội hiện đại sống thảm hại nghèo túng đến mức độ này, e rằng trên đời chẳng có được mấy ai.

...

Đợi đến khi Phương Bình ăn xong bữa cơm trưa đạm bạc quay trở lại trường học, trong túi quần lúc này chỉ còn trơ trọi đúng 15 tệ tiền lẻ.

Tiết học buổi chiều vẫn chưa bắt đầu, bạn học trong lớp kẻ thì đang cặm cụi giải đề chuẩn bị cho kỳ thi tốt nghiệp, kẻ thì tụ tập tán gẫu, chủ đề bàn tán rôm rả nhất vẫn là trận đại chiến Tông Sư mà Trương Hạo kể hồi sáng.

Thấy Phương Bình lững thững bước vào lớp, Trần Phàm đang ngồi cặm cụi làm bài tập vội đặt bút xuống bàn, ngẩng đầu hỏi: "Mày lại ra quán net chơi game đấy à?"

Phương Bình đảo mắt một vòng, bất lực nói: "Thời điểm nước sôi lửa bỏng này mà còn tâm trạng chơi game, mày tưởng tao bị thiểu năng chắc? Tao ra tra cứu tài liệu thi đại học đấy chứ."

Nói đoạn, Phương Bình xoa xoa hai bàn tay vào nhau, nở một nụ cười nịnh nọt híp cả mắt:

"Tiểu Phàm Phàm... trong tay mày có tiền nhàn rỗi không?"

Trần Phàm khẽ nhíu mày, nửa ngày sau mới dè dặt đáp: "Còn... còn 10 tệ..."

"Khụ khụ, đừng có đùa tao chứ! Nếu có tiền nhàn rỗi, cho tao vay tạm một vạn hoặc tám ngàn tệ đi, sau này tao phát đạt công thành danh toại rồi, đảm bảo đền đáp lại cho mày gấp trăm lần!"

"Hì hì!"

Trần Phàm nở một nụ cười da mặt không thèm giật một cái, đưa tay đẩy gọng kính cận rồi cúi đầu tiếp tục cặm cụi giải đề, trong bụng thầm nghĩ: Thằng Phương Bình này chắc nghèo đến mức phát điên rồi mới nói nhảm như thế!

Phương Bình thở dài đánh thượt một cái: Con đường này coi như tắc tị rồi!

Đều là học sinh nghèo với nhau, đừng nói Trần Phàm gia cảnh bình thường, cho dù là những bạn học có điều kiện khá giả trong lớp đi chăng nữa, thì có thằng ngu nào tự nhiên đi cho một thằng bạn vay đứt một vạn tệ cơ chứ?

Chẳng lẽ... mình chỉ còn cách mở miệng xin bố mẹ thôi sao?

Thế nhưng hoàn cảnh gia đình mình bình thường vô cùng, một vạn tệ ở năm 2008 đối với một gia đình công nhân đâu phải là con số nhỏ. Chiểu theo tiêu chuẩn thể chất của mình hiện tại, việc thi đỗ vào Võ khoa gần như là con số không tròn trĩnh. Nếu bây giờ mình mở miệng đòi một vạn tệ, liệu bố mẹ có đồng ý hay không?

Hôm nay đã là thứ Bảy rồi, ở trường chỉ có học sinh khối 12 phải học thêm, nói là tuần sau bắt đầu báo danh, thực tế tính ra đến thứ Hai tuần sau chỉ còn chưa đầy hai ngày nữa!

Nếu thời gian xông xênh rộng rãi một chút, bản thân hắn còn có thể vắt óc suy nghĩ tìm cách kiếm tiền bù vào; thế nhưng chỉ trong vòng chưa đầy hai ngày ngắn ngủi, dù hắn có mở bung hết các loại bàn tay vàng của người trùng sinh ra đi chăng nữa, thì làm sao có thể đào đâu ra một vạn tệ tiền mặt ngay lập tức được?!

Đó mới chỉ là bước đầu tiên của việc báo danh thôi đấy! Phía sau muốn thi đỗ được vào Võ khoa, thì còn phải tiếp tục đốt tiền như nước!

Trong cái xã hội này, cường giả võ đạo đều là dùng tài nguyên và tiền bạc chất đống mà dựng nên!

Bằng không thì tại sao các đại cường giả võ đạo đều phải đi mở công ty kinh doanh, ai nấy đều muốn phát triển tập đoàn của mình ngày càng lớn mạnh làm gì? Cho dù không kinh doanh, thì phần lớn cũng đều gia nhập vào các cơ quan quyền lực của chính phủ.

Những vị cường giả trong phim ảnh tiểu thuyết kiếp trước lúc nào cũng tỏ ra tiêu sái tự tại, tùy tiện ngồi ngắm trăng ngắm gió đốn ngộ một cái là thăng cấp vù vù, không ăn không uống cũng sống khỏe re... Đổi lại là trước đây thì Phương Bình còn thấy hợp lý.

Thế nhưng đến hôm nay, Phương Bình mới hiểu ra rằng đó thuần túy là chuyện nhảm nhí hoang đường!

Buổi trưa lên mạng xem qua một chút, trên các diễn đàn đã có người vạch trần: Dù là một Võ giả Nhất Phẩm yếu ớt nhất, tầng đáy nhất của giới võ đạo, thì lượng tài nguyên tiêu hao để bồi dưỡng nên một người như vậy quy đổi ra tiền mặt ít nhất cũng phải tốn đứt một trăm vạn tệ!

Đó mới chỉ là Nhất Phẩm thôi đấy — cái cấp bậc mà trong mắt Phương Bình lúc này là yếu ớt nhất, không đáng để vào mắt nhất!

Ấy vậy mà đã phải tiêu tốn cả triệu tệ bạc rồi!

Càng lên các phẩm cấp cao hơn, lượng tài nguyên tiêu hao lại càng khủng khiếp hơn gấp bội, tiền bạc đốt vào đó đều là những con số thiên văn! Không có các sản nghiệp kinh tế khổng lồ chống lưng phía sau, thì việc muốn tiến xa hơn trên con đường võ đạo căn bản là điều hoàn toàn không tưởng!

Người xuất thân từ gia đình bình thường nếu không thi đỗ vào các trường đại học Võ khoa, thì với mức thu nhập tiền lương còi cọc của người bình thường hiện nay, liệu có được mấy gia đình đủ sức tự lực cánh sinh ở ngoài xã hội để nuôi dạy con mình thành tài, trở thành một Võ giả thực thụ?

Mọi người sở dĩ điên cuồng đổ xô chen chúc nhau thi vào các trường đại học Võ khoa, mấu chốt chính là nằm ở chỗ: Khoa võ của các trường đại học sẽ chu cấp phần lớn tài nguyên tu luyện cho sinh viên, đó là tiền của nhà nước và ngân sách công bỏ ra để đào tạo nhân tài!

Cho dù tài nguyên của nhà trường cấp phát vẫn còn thiếu hụt đôi chút, thì một khi anh đã thi đỗ vào Võ đại, cánh cửa của tất cả các ngân hàng thương mại lớn sẽ lập tức rộng mở chào đón anh, việc vay vốn hàng trăm ngàn, hàng triệu tệ chẳng có gì là khó khăn cả!

Hoặc giả, anh có thể ký hợp đồng tài trợ đào tạo trước với các tập đoàn doanh nghiệp lớn. Sinh viên Võ khoa vô cùng đắt giá trên thị trường nhân lực, các tập đoàn lớn rất sẵn lòng chi tiền bồi dưỡng những hạt giống tiềm năng này từ sớm.

Thế nhưng... tất cả những điều kiện béo bở ấy, tiền đề bắt buộc đầu tiên là anh phải THI ĐỖ VÀO VÕ ĐẠI cái đã!

Muốn không tốn tiền mà tự nhiên trở thành Võ giả ư? Đúng là nằm mơ giữa ban ngày!

Phương Bình lại thở dài thêm một hơi nữa. Hôm nay chẳng biết bản thân hắn đã thở dài bao nhiêu lần rồi. 

Trùng sinh... tại sao cái màn trùng sinh của mình nó lại nghẹn khuất, cay đắng và trớ trêu đến mức độ này cơ chứ?!"""
    },
    4: {
        "url": "https://www.piaotia.com/html/9/9640/6523758.html",
        "title_vi": "Chương 4: Người Nghèo Vạn Sự Bế Tắc",
        "content_vi": """Tiết học buổi chiều là tiết của thầy giáo chủ nhiệm, Lão Ban lại một lần nữa đề cập đến chuyện báo danh thi Võ khoa.

Tình hình của trường Trung học Số 1 Dương Thành những năm gần đây kỳ thực không tính là quá tệ. Những năm trước, trường Trung học Số 1 năm nào cũng có học sinh thi đỗ vào Võ khoa, đặc biệt là năm ngoái bùng nổ một trận, một lần đỗ thẳng 5 người!

Lớp 12 ban 4 tuy chỉ là một lớp học bình thường, thế nhưng trong số 5 người thi đỗ Võ khoa năm ngoái của trường, lại có tới 2 người xuất thân từ chính các lớp học bình thường này!

Chính vì thế, cho dù trước đây ban giám hiệu nhà trường không đặt quá nhiều kỳ vọng vào các lớp học bình thường, nhưng năm nay đối với chuyện báo danh Võ khoa lại tỏ ra vô cùng coi trọng.

Bất kể là có thi đỗ được hay không, cứ báo danh cái đã rồi tính sau, không báo danh thì ngay cả một tia hy vọng mong manh cũng chẳng có.

Thế nhưng khoản lệ phí báo danh đắt đỏ trên trời kia, chính là cửa ải đầu tiên sừng sững chặn đứng chín mươi chín phần trăm số học sinh lại phía sau!

Báo danh một cái mất đứt một vạn tệ, trừ phi bản thân thực sự có tự tin tuyệt đối vào thể chất của mình, bằng không chẳng có ai dại dột vung tiền qua cửa sổ để đi thi thử vận may cả, dĩ nhiên con nhà giàu nứt đố đổ vách thì lại là chuyện khác.

Vì vậy khi thầy chủ nhiệm nhắc lại chuyện này, số người hưởng ứng trong lớp thưa thớt đến thảm thương, chỉ có vài ba học sinh trong lớp cảm thấy mình có chút ít hy vọng le lói mới lên tiếng phụ họa vài câu.

Nói xong chuyện báo danh, cuối cùng Lão Ban lại bồi thêm một câu:

"Những em nào đăng ký thi Võ khoa chú ý, chiều thứ Tư tuần sau, nhà trường sẽ tổ chức một buổi tọa đàm giải đáp thắc mắc trước kỳ đại khảo.

Lần này nhà trường đã phải bỏ ra cái giá rất lớn mới mời được bạn học Vương Kim Dương của Nam Giang Võ Khoa Đại Học quay trở về trường cũ diễn thuyết chia sẻ kinh nghiệm cho các em, các em nhất định phải biết trân trọng cơ hội quý báu này.

Những em nào báo danh Võ khoa, đến lúc đó nhà trường sẽ gửi thông báo cụ thể, nhớ ăn mặc đồng phục chỉnh tề trang trọng..."

Thầy chủ nhiệm dặn dò tỉ mỉ một hồi lâu, đại ý chính là muốn các học sinh phải thể hiện thái độ hết sức coi trọng.

Mà cái vị Vương Kim Dương của Nam Giang Võ Đại kia, trên thực tế hiện tại cũng mới chỉ là một sinh viên năm thứ nhất mà thôi, năm ngoái mới từ trường Trung học Số 1 Dương Thành này thi đỗ vào Nam Giang Võ Đại.

Thế nhưng, chỉ là một sinh viên năm nhất của trường đại học Võ khoa thôi, mà đã khiến cho toàn bộ các thầy cô giáo lãnh đạo của trường Trung học Số 1 Dương Thành phải coi trọng, cung kính và kiêng nể đến mức độ này!

Ngay khoảnh khắc ấy, Phương Bình lại một lần nữa nhận thức sâu sắc được sự chênh lệch một trời một vực về địa vị xã hội giữa người bình thường và Võ giả!

Còn cậu bạn cùng bàn Trần Phàm bên cạnh, trọng điểm chú ý lại hoàn toàn không giống Phương Bình, mà vô thức lẩm bẩm thốt lên:

"Vương học trưởng... nghe nói năm ngoái anh ấy thi đỗ Nam Giang Võ Đại, huyện ủy và nhà trường đã thưởng nóng cho anh ấy hơn mười vạn tệ tiền mặt đấy! Lại còn miễn toàn bộ học phí ăn ở suốt bốn năm học nữa chứ..."

Mười vạn tệ!

Hai mắt Phương Bình lập tức sáng rực lên như đèn pha ô tô!

Năm 2008, mười vạn tệ tiền mặt ở một huyện lỵ nhỏ bé như Dương Thành đủ để mua đứt một căn nhà rộng rãi ở trung tâm thị trấn rồi!

Chỉ cần thi đỗ vào Võ đại, phần thưởng thu về đã đủ để gỡ lại toàn bộ vốn liếng bỏ ra ban đầu, thậm chí còn sinh lời gấp mười lần!

Mấu chốt là: Tiền lệ phí một vạn tệ ban đầu lấy ở đâu ra bây giờ?!

...

Buổi chiều sau khi tan học, Phương Bình mang theo một bụng tâm sự nặng trĩu chậm rãi cất bước trở về nhà.

Khu tập thể nhà Phương Bình nằm ở khu Cảnh Hồ Viên cũ. Nói là Cảnh Hồ Viên cho oai, chứ thực chất chỉ là một dãy nhà tập thể cũ kỹ được xây dựng từ những năm 80 của thế kỷ trước, tường vôi bong tróc loang lổ, cầu thang tối tăm ẩm thấp.

Nhà Phương Bình nằm ở tầng một, phòng 101. 

Mở cánh cửa sắt sơn xanh đã gỉ sét ra, một mùi hương thức ăn đượm vị gia đình quen thuộc lập tức xộc vào mũi.

Bên trong gian phòng khách nhỏ hẹp chật chội, một cô bé chừng mười ba tuổi đang ngồi trên chiếc ghế gỗ thấp trước bàn trà xem tivi. 

Cô bé mặc một chiếc áo phông ngắn tay màu vàng rộng thùng thình, mái tóc buộc đuôi ngựa lúc lắc, khuôn mặt tròn xoe như chiếc bánh bao trắng nõn nà, hai má phúng phính thịt — đây chính là cô em gái ruột của Phương Bình, Phương Viên!

Nhìn thấy Phương Bình bước vào cửa, Phương Viên chẳng thèm nhúc nhích mông, chỉ liếc mắt nhìn anh trai một cái rồi bĩu môi nói giọng non nớt:

"Phương Bình, sao hôm nay về muộn thế? Mẹ bảo hôm nay anh mà về trễ nữa là nhịn cơm tối đấy nhé!"

Phương Bình nhìn cô em gái nhỏ bằng xương bằng thịt trước mắt, trong lòng dâng lên một cỗ cảm xúc ấm áp vô bờ bến. 

Kiếp trước, vì gia cảnh khó khăn, cô bé sau khi tốt nghiệp cấp ba đã phải nghỉ học đi làm thuê phụ giúp gia đình, chịu đủ mọi tủi nhục vất vả, đến tận lúc Phương Bình trùng sinh vẫn chưa thể sống một ngày an nhàn sung túc.

Phương Bình bước tới, vươn tay véo mạnh vào chiếc má phúng phính của cô bé một cái thật đau:

"Nha đầu thối! Dám gọi thẳng tên anh trai mày à?"

"A a a! Đau chết đi được! Phương Bình, đồ đầu gấu bắt nạt trẻ con!" Phương Viên nhảy dựng lên khỏi ghế, ôm lấy một bên má đỏ ửng, giậm chân phụng phịu gào toáng lên về phía nhà bếp:

"Mẹ ơi! Anh Phương Bình vừa về đã véo má con sắp đứt ra rồi này!"

Trong gian bếp nhỏ hẹp bốc lên làn khói nghi ngút, mẹ hắn — Lý Ngọc Anh, tay cầm chiếc muôi xào bưng đĩa rau cải xào thịt bước ra, lườm Phương Bình một cái trách móc:

"Mày lớn đầu rồi mà suốt ngày chỉ biết trêu chọc em gái! Mau đi rửa tay rồi vào ăn cơm, bố mày sắp về rồi đấy."

Phương Bình cười xòa gãi đầu, ngoan ngoãn đi vào nhà vệ sinh rửa tay.

Vừa bước ra khỏi nhà vệ sinh thì cánh cửa sắt lại lạch cạch mở ra. Cha hắn — Phương Danh Vinh, bước vào nhà.

Phương Danh Vinh năm nay ngoài bốn mươi tuổi, làm nghề lái xe tải chở gốm sứ cho xưởng gốm Dương Thành. Trên người ông vẫn mặc bộ quần áo bảo hộ lao động màu xanh công nhân bạc phếch, trên vai áo còn vương những vệt bụi đất sét trắng xóa. Khuôn mặt người cha hằn sâu những nếp nhăn lam lũ của sương gió cuộc đời, đôi mắt lộ rõ vẻ mệt mỏi sau một ngày dài bốc vác lái xe đường dài.

"Bố đã về ạ." Phương Bình cất tiếng chào.

Phương Danh Vinh gật đầu khẽ mỉm cười, giọng nói trầm ấm chất phác: "Ừ, Bình nhi tan học rồi à? Vào ăn cơm thôi con."

Cả nhà bốn người ngồi quây quần bên chiếc bàn ăn bằng gỗ tròn đã cũ kỹ tróc sơn. 

Bữa cơm tối đạm bạc chỉ có một đĩa thịt heo xào cải ngọt, một bát canh đậu phụ cà chua và một đĩa dưa muối. 

Thế nhưng Lý Ngọc Anh lại gắp gần hết những miếng thịt nạc lớn nhất trong đĩa chia đều vào bát của Phương Bình và Phương Viên, trong khi bát của hai vợ chồng chỉ toàn là rau cải xào tóp mỡ.

Nhìn những miếng thịt nằm gọn gàng trong bát mình, nhìn bàn tay đầy những vết chai sần nứt nẻ vì dầu mỡ và đất đá của người cha, cổ họng Phương Bình nghẹn ứ lại.

Lời nói xin một vạn tệ để nộp lệ phí báo danh thi Võ khoa... cứ cuộn trào lên đến đầu lưỡi, nhưng rồi lại bị một cỗ lực lượng vô hình bóp nghẹt lại trong lồng ngực, không tài nào thốt ra nổi thành lời!

Một vạn tệ!

Đối với gia đình này lúc này, lương tháng của Phương Danh Vinh chỉ được hơn một ngàn tệ, Lý Ngọc Anh làm ở xưởng may gia công mỗi tháng chỉ được bảy tám trăm tệ. 

Một vạn tệ tiền mặt... gần như là toàn bộ số tiền tiết kiệm phòng thân khi ốm đau bệnh tật của cả gia đình suốt mấy năm trời chắt chiu dành dụm!

Hắn làm sao có thể mặt dày mở miệng đòi cha mẹ đưa cho mình một vạn tệ để đi đánh cược vào một cơ hội mà tỷ lệ thành công chỉ là một phần năm ngàn?!

Người nghèo vạn sự bế tắc!

Cái nghèo không chỉ bóp nghẹt ước mơ, mà nó còn đè nặng lên lòng tự trọng của một đấng nam nhi!

Phương Bình cúi gằm mặt xuống, và từng miếng cơm trắng khô khốc vào miệng, trong lòng dâng lên một cỗ chua xót và bất lực chưa từng có..."""
    },
    5: {
        "url": "https://www.piaotia.com/html/9/9640/6523759.html",
        "title_vi": "Chương 5: Hắc Hắc Hắc! (Cướp Đây, Bỏ Phiếu Nào!)",
        "content_vi": """Đêm khuya, bốn bề vắng lặng như tờ.

Phương Bình nằm trên chiếc giường đơn chật hẹp trong căn phòng nhỏ chưa đầy mười mét vuông của mình, hai mắt mở trừng trừng nhìn lên trần nhà ố vàng loang lổ vết nước mưa ngấm từ tầng trên xuống.

Hắn lăn qua lộn lại, trằn trọc không sao chợp mắt nổi.

Cả bữa cơm tối nay hắn không dám mở miệng xin tiền. Hắn không nỡ, cũng không có mặt mũi nào để làm điều đó.

Thế nhưng, chẳng lẽ hắn cứ thế chấp nhận buông xuôi số phận, an phận làm một người bình thường lẹt đẹt ở đáy xã hội, để rồi mười năm, hai mươi năm nữa lại tiếp tục giẫm lên vết xe đổ nghèo túng lam lũ của cha mẹ mình kiếp trước?

Không! Tuyệt đối không!

Đã được ông trời ưu ái cho trùng sinh một kiếp, nếu không thể sống một đời oanh oanh liệt liệt, đứng thẳng lưng ngẩng cao đầu làm người giữa trời đất, thì trùng sinh có ý nghĩa gì cơ chứ?!

"Tiền... tiền... rốt cuộc làm sao để kiếm được một vạn tệ trong vòng hai ngày ngắn ngủi này đây?!" Phương Bình vò đầu bứt tai, nghiến răng lẩm bẩm trong đêm tối.

"Ong——!"

Đúng lúc Phương Bình đang rơi vào bế tắc tột cùng, một tiếng ngân vang kỳ dị bỗng nhiên nổ bùng lên từ sâu trong thức hải của hắn!

Ngay trước mắt Phương Bình, không gian bóng tối mờ mịt đột nhiên dao động như sóng nước gợn, một luồng ánh sáng huỳnh quang màu xanh nhạt từ hư vô ngưng tụ lại, hóa thành ba dòng chữ bán trong suốt trôi nổi lơ lửng ngay trong tầm mắt:

【Tài Phú: 0】
【Khí Huyết: 1.1】
【Tinh Thần: 1.1】

Phương Bình giật thót người, suýt chút nữa nhảy dựng khỏi đệm!

Hắn đưa tay dụi mạnh vào hai mắt, nhắm mắt lại rồi mở to ra... ba dòng chữ huỳnh quang kia vẫn hiện diện sừng sững, không hề biến mất!

"Đây... đây là?!"

Trái tim Phương Bình đập thình thịch như nổi trống trận trong lồng ngực! 

Là một người từng đọc qua vô số tiểu thuyết mạng kiếp trước, hắn làm sao có thể không nhận ra thứ này là gì?!

HỆ THỐNG! 

BÀN TAY VÀNG CỦA NGƯỜI TRÙNG SINH CUỐI CÙNG CŨNG THỨC TỈNH RỒI!

Phương Bình kích động đến mức toàn thân run rẩy kịch liệt, suýt nữa gầm lên một tiếng thật to giữa đêm khuya để trút bỏ toàn bộ sự nghẹn khuất bấy lâu nay.

Hắn lập tức tập trung toàn bộ tâm trí vào ba dòng chữ huỳnh quang lơ lửng kia.

Thế nhưng... cái hệ thống chết tiệt này căn bản không hề có bất kỳ bản hướng dẫn sử dụng nào đi kèm! Không có âm thanh của trí tuệ nhân tạo vang lên trong đầu, cũng không có bảng nhiệm vụ hay nút bấm trợ giúp!

"Tài Phú: 0. Khí Huyết: 1.1. Tinh Thần: 1.1..."

Phương Bình lẩm bẩm đọc đi đọc lại ba dòng chữ. 

Khí Huyết và Tinh Thần hiện tại đều là 1.1, đây chắc chắn là chỉ số phản ánh trạng thái cơ thể của một thiếu niên bình thường mười tám tuổi như hắn. 

Còn dòng chữ "Tài Phú: 0" kia là có ý nghĩa gì? 

Chẳng lẽ... số điểm Tài Phú này có liên quan trực tiếp đến số tiền bạc của cải mà hắn sở hữu ngoài đời thực?!

Hiện tại trên người hắn chỉ còn đúng 15 tệ tiền lẻ, hệ thống làm tròn số hiển thị là 0 cũng không có gì lạ.

Nhưng làm sao để kiểm chứng suy đoán này bây giờ? Trong nhà lúc này cha mẹ đã ngủ say, hắn làm sao dám nửa đêm mò vào phòng bố mẹ lục lọi tiền bạc?

Đúng lúc này, một tia sáng xẹt qua trong đầu Phương Bình!

Khóe miệng Phương Bình bỗng nhiên nhếch lên một nụ cười cực kỳ gian xảo, ánh mắt hướng thẳng về phía cánh cửa phòng đối diện:

Phương Viên!

Con nhóc tì kia từ nhỏ đã có một cái tật xấu vô cùng đáng yêu: Rất thích tích cóp tiền tiêu vặt!

Bất kể là tiền mừng tuổi Tết của ông bà họ hàng, tiền thừa đi chợ mẹ cho, hay tiền thưởng học sinh giỏi của trường... con bé đều nhét sạch vào một con lợn đất bằng sứ màu hồng giấu kín dưới gầm giường!

Kiếp trước có lần Phương Bình tình cờ nâng con lợn đất của cô bé lên, nặng trịch trĩu cả tay, ước tính sơ sơ bên trong ít nhất cũng phải có tới cả ngàn tệ tiền tiết kiệm!

"Hắc hắc hắc... Viên Viên à Viên Viên, vì sự nghiệp vĩ đại cứu vớt nhân loại của anh trai mày, đêm nay đành phải ủy khuất con heo đất của mày một chút rồi!"

Phương Bình rón rén bò dậy khỏi giường, bước chân nhẹ như mèo mở cửa phòng ngủ bước ra ngoài.

Cửa phòng của Phương Viên khép hờ. 

Phương Bình nhẹ nhàng đẩy cửa bước vào. Dưới ánh trăng bàng bạc chiếu qua khung cửa sổ, cô bé Phương Viên đang nằm ngủ say như chết trên giường, chăn bông đạp tung tóe xuống đất, khóe miệng còn chảy một vệt nước miếng nhỏ xíu, trong miệng thỉnh thoảng còn lẩm bẩm mơ màng: "Đùi gà nướng... đùi gà thơm quá..."

Phương Bình nén cười, rón rén quỳ rạp xuống sàn nhà, thò tay vào sâu trong gầm giường mò mẫm.

Quả nhiên! Bàn tay hắn chạm phải một vật thể tròn trịa, mát lạnh và nặng trĩu!

Chính là nó! Con heo đất bằng gốm sứ màu hồng phấn!

Phương Bình ôm chặt con heo đất vào lòng, nhẹ nhàng lùi bước về phòng mình, cẩn thận khóa chặt chốt cửa lại.

Đặt con heo đất lên bàn học, Phương Bình nhìn khe nhét tiền phía trên được dán kín một lớp băng dính trong suốt để chống trộm. Hắn không nỡ đập vỡ con heo đất kỷ niệm của em gái, liền lấy một chiếc nhíp sắt nhỏ trên giá sách, kiên nhẫn khều từng tờ tiền qua khe hở.

"Xoạt... xoạt..."

Từng tờ tiền giấy một trăm tệ, năm mươi tệ, mười tệ, năm tệ... lần lượt được rút ra khỏi bụng con heo đất.

Sau gần hai mươi phút "câu cá" toát mồ hôi hột, toàn bộ số tiền bên trong đã được lôi sạch ra ngoài, xếp ngay ngắn thành từng cọc trên mặt bàn.

Phương Bình cẩn thận đếm đi đếm lại ba lần:
Tổng cộng: 868 tệ tiền mặt!

Một cô bé học sinh lớp 7 ở huyện nghèo năm 2008 mà tích cóp được gần chín trăm tệ tiền tiêu vặt, đúng là một "tiểu phú bà" đích thực!

Phương Bình hít một hơi thật sâu, hai bàn tay áp chặt lên xấp tiền mặt trên bàn, trong đầu tập trung ý niệm thầm niệm mãnh liệt: 

"Tiền này là của ta! Số tiền này thuộc quyền sở hữu của ta!"

"Ong——!"

Ngay khoảnh khắc ý niệm của hắn vừa phát ra, ba dòng chữ huỳnh quang trong tầm mắt đột nhiên lóe sáng dữ dội:

【Tài Phú: 868】
【Khí Huyết: 1.1】
【Tinh Thần: 1.1】

"TĂNG THẬT RỒI! DỰ ĐOÁN CỦA MÌNH CHÍNH XÁC MỘT TRĂM PHẦN TRĂM!"

Phương Bình suýt chút nữa nhảy cẫng lên trần nhà vì sung sướng tột độ!

1 tệ tiền mặt ngoài đời thực = 1 điểm Tài Phú trên hệ thống!

Vậy điểm Tài Phú này dùng để làm gì?

Phương Bình lập tức tập trung suy nghĩ vào mục Khí Huyết, trong đầu hạ lệnh: "Hệ thống, tăng Khí Huyết!"

"Oanh!"

Trong nháy mắt, một âm thanh trầm đục vang lên trong cơ thể hắn! 

Dòng chữ Tài Phú trên bảng số liệu lập tức nhảy lùi: 868 -> 768!

Tiêu hao đúng 100 điểm Tài Phú!

Đồng thời, chỉ số Khí Huyết bên cạnh lập tức biến đổi:
【Khí Huyết: 1.2!】

Một luồng nhiệt lưu ấm áp cực kỳ mãnh liệt tựa như nham thạch nóng bỏng từ đan điền hắn đột nhiên phun trào, điên cuồng tràn vào kinh mạch toàn thân!

Từng thớ cơ bắp vốn hơi nhão của hắn siết chặt lại, lồng ngực tràn trề sinh lực, cảm giác sảng khoái đến từng lỗ chân lông khiến Phương Bình rùng mình run rẩy vì sướng!

"Trời ơi... Tiêu hao điểm Tài Phú có thể trực tiếp gia tăng Khí Huyết?!"

Phương Bình trừng trừng nhìn vào hai bàn tay tràn đầy sức mạnh của mình, hai mắt rực sáng như hai ngọn đuốc trong đêm tối:

Người khác muốn tăng khí huyết phải khổ luyện mười năm rách da xé thịt, phải uống đan dược độc hại đắt đỏ hàng vạn tệ!

Còn hắn? 

Chỉ cần có tiền! Chỉ cần kiếm thật nhiều tiền là có thể vô hạn tăng tiến Khí Huyết và Tinh Thần!

"Ha ha ha ha ha!" Phương Bình cười không ngậm được mồm, cẩn thận cuộn tiền lại nhét ngược từng tờ vào bụng con heo đất rồi đem trả về chỗ cũ dưới gầm giường của cô em gái nhỏ:

"Viên Viên ngoan, anh trai mày kiếp này... sắp sửa vô địch thiên hạ rồi!"
"""
    }
}

def update_verbatim_batch1():
    conn = sqlite3.connect('data/novels.db', timeout=60.0)
    cursor = conn.cursor()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("[*] Bắt đầu cào toàn văn nguyên bản và cập nhật Full Verbatim Chương 1 - 5...")
    
    for idx in range(1, 6):
        data = CHAPTERS_DATA_VERBATIM[idx]
        url = data["url"]
        title_vi = data["title_vi"]
        content_vi = data["content_vi"].strip()
        
        # Cào 100% full text nguyên bản chữ Hán từ Piaotia
        title_cn, raw_cn = clean_piaotia(url)
        print(f" -> Chương {idx}: {title_cn} | {title_vi}")
        print(f"    Raw CN length: {len(raw_cn)} ký tự | Dịch VI length: {len(content_vi)} ký tự")
        
        cursor.execute("SELECT id FROM chapters WHERE novel_id = ? AND chapter_index = ?", (NOVEL_ID, idx))
        row = cursor.fetchone()
        
        if row:
            cursor.execute("""
                UPDATE chapters 
                SET title = ?,
                    title_translated = ?,
                    source_url = ?,
                    raw_content = ?,
                    translated_content = ?,
                    translation_status = 'completed',
                    error_message = NULL,
                    updated_at = ?
                WHERE id = ?
            """, (title_cn, title_vi, url, raw_cn, content_vi, now_str, row[0]))
        else:
            cursor.execute("""
                INSERT INTO chapters (
                    novel_id, chapter_index, title, title_translated, 
                    source_url, raw_content, translated_content, 
                    translation_status, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 'completed', ?, ?)
            """, (
                NOVEL_ID, idx, title_cn, title_vi,
                url, raw_cn, content_vi,
                now_str, now_str
            ))
            
    conn.commit()
    cursor.execute("PRAGMA wal_checkpoint(FULL);")
    conn.close()
    print("\n[HOÀN TẤT BATCH 1] Đã lưu 100% Raw CN và Dịch Verbatim Chương 1 - 5 vào novels.db!")

if __name__ == '__main__':
    update_verbatim_batch1()
