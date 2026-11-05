# -*- coding: utf-8 -*-
"""
DỊCH THEO PHƯƠNG ÁN B (VERBATIM 100% NGUYÊN VĂN TỪNG CÂU TỪNG CHỮ)
Tác phẩm: Toàn Cầu Cao Võ (全球高武) - Lão Ưng Cật Tiểu Kê (老鹰吃小鸡)
Lưu toàn văn 100% nguyên bản chữ Hán từ Piaotia vào raw_content.
Bản dịch tiếng Việt văn phong cao võ trau chuốt, đầy đủ từng câu độc thoại, suy nghĩ và hội thoại.
Batch 3: Chương 11 đến Chương 15.
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
    11: {
        "url": "https://www.piaotia.com/html/9/9640/6523765.html",
        "title_vi": "Chương 11: Đo Kiểm Lần Đầu",
        "content_vi": """Quay trở lại lớp học, Phương Bình đối phó vài câu qua loa với Trần Phàm, kế đó liền bắt đầu lật mở những cuốn sách vừa ôm từ chỗ Lão Ban về ra xem.

Xem lướt qua một hồi, Phương Bình cảm thấy đầu đau như búa bổ.

Kỳ thi chuyên nghiệp của võ khoa liên quan tới quá nhiều kiến thức sâu rộng.

Nội dung trọng yếu nhất chính là sự nhận biết đối với chính cơ thể bản thân mình.

Là một chuẩn võ giả dự bị, nếu như ngay cả cấu tạo thân thể của chính mình còn không nắm rõ ràng, thì làm sao có thể rèn luyện thể phách của mình một cách tốt nhất được?

Cơ thể con người có bao nhiêu đốt xương, bao nhiêu đường mạch lạc chủ chốt, hệ thống tuần hoàn của huyết dịch ra sao……

Những thứ này đều là những kiến thức bắt buộc phải nắm vững trong lòng bàn tay.

Bao gồm cả cách sắp xếp, tên gọi của từng khúc xương cốt, tác dụng của ngũ tạng lục phủ, cũng như giải thích tường tận một số danh từ chuyên môn của võ đạo.

Cùng với một loạt các thường thức cơ bản liên quan đến y học và dược vật học.

Ngoài ra, trong số tài liệu mà Lão Ban đưa cho, còn bao gồm cả những cuốn như《Võ Đạo Lịch Sử Học》,《Cổ Kim Danh Nhân Truyện》,《Cơ Sở Vũ Khí Đại Toàn》,《Khái Yếu Bài Bản Võ Thuật Cơ Sở》……

Đừng nói là đọc kỹ từng câu chữ, chỉ cần tùy tiện rút ra một cuốn, Phương Bình mới lật xem vài trang đã thấy hoa mày chóng mặt.

Mà số sách vở chất đống ngay trước mắt hắn tổng cộng nhiều tới hơn mười cuốn dày cộp.

Muốn đọc hết đống sách này từ đầu đến đuôi thực sự là một công trình vô cùng đồ sộ và gian nan.

Cho dù Phương Bình có đọc chúng như đọc tiểu thuyết giải trí đi chăng nữa, thì e rằng đọc xong xuôi khoảng cách tới kỳ thi đại học cũng chẳng còn lại bao nhiêu ngày.

Mà tiếp theo đây, Phương Bình còn phải dành thời gian ôn thi các môn văn hóa nữa chứ.

Đã bao nhiêu năm không đụng tới sách giáo khoa rồi, tuy rằng nền tảng kiến thức vẫn còn đó, nhưng muốn khôi phục lại phong độ trạng thái đỉnh cao cũng không phải là chuyện ngày một ngày hai có thể làm được.

"Nhức đầu thật đấy chứ!"

Trần Phàm ngồi bên cạnh thấy sắc mặt Phương Bình trắng bệch, tuy có chút bất mãn vì trước khi báo danh Phương Bình không thèm bàn bạc với mình tiếng nào, nhưng lúc này vẫn mở miệng an ủi: "Mưu sự tại nhân thành sự tại thiên, dù sao cũng không thể lãng phí mất đống tiền lệ phí báo danh được, đúng không?"

Phương Bình đảo trắng mắt, hóa ra trong mắt cậu, tớ nỗ lực cắm đầu vào học là chỉ vì tiếc 1 vạn tệ tiền lệ phí báo danh kia thôi sao?

Trần Phàm chẳng buồn để ý tới cái lườm của hắn, an ủi một câu xong liền tiếp tục nói: "Đáng tiếc thật, chúng mình không phải là võ giả.

Nếu như trở thành võ giả, tinh lực dồi dào sung mãn, mấy ngày mấy đêm không ngủ cũng chẳng hề hấn gì.

Nghe nói võ giả cao đoạn, tốc độ xử lý của não bộ chẳng khác gì máy vi tính siêu cấp.

Những vị cường giả đó, bất kể là kinh doanh quản lý doanh nghiệp hay giải quyết công việc chính vụ, một người có thể gánh vác bằng mười người bình thường cộng lại, tinh lực dồi dào tới mức dọa người.

Tớ nghe nói năm xưa lúc Mã Tông Sư khởi nghiệp, nguồn vốn eo hẹp, nhân lực thiếu thốn, thời điểm đỉnh cao nhất ngài ấy đã thức trắng suốt bảy ngày bảy đêm không ngủ không nghỉ, một tuần lễ làm bằng khối lượng công việc của người bình thường làm trong cả một năm trời.

Lúc đó thực lực võ đạo của Mã Tông Sư vẫn còn chưa quá mạnh mẽ, nếu đổi thành bây giờ, nói không chừng cả tháng ngài ấy không ngủ cũng được, nghĩ thôi đã thấy thèm thuồng ngưỡng mộ rồi.

Bọn mình nếu như có được thể phách và tinh lực sung mãn của võ giả, thì thi cử văn hóa đã là cái thá gì, thi đạt điểm tuyệt đối tối đa cũng đâu phải là chuyện không có khả năng."

Trần Phàm thở dài với vẻ mặt tràn đầy tiếc nuối. Trong các kỳ thi đại học ngày nay, hàng năm số thí sinh đạt điểm tuyệt đối quả thực không hề ít.

Một số học sinh lớp 12 ở các thành phố lớn, cho dù chưa chính thức trở thành võ giả thực thụ, nhưng khoảng cách tới võ giả cũng chỉ còn cách một bước chân ngắn ngủi.

Trong tình huống như vậy, những người này tuy phải phân tâm làm nhiều việc cùng lúc, nhưng năng lực lĩnh hội và khả năng ghi nhớ của họ lại đáng sợ tới mức kinh người. Hầu hết các thủ khoa văn khoa của các tỉnh hàng năm gần như đều bị những chuẩn võ giả dự bị này thâu tóm sạch sẽ.

Người nói vô tâm, nhưng người nghe lại hữu ý.

Lông mày Phương Bình khẽ giật giật. Trần Phàm không có điều kiện này, nhưng chưa chắc bản thân hắn lại không có.

Những lợi ích to lớn của việc khí huyết cường đại, Phương Bình đã phần nào được thể nghiệm qua.

Ngày hôm qua sau khi khí huyết tăng lên một chút, Phương Bình quả thực cảm thấy bản thân mình có tinh lực dồi dào hơn trước kia rất nhiều. Nếu đổi thành trước kia, ngủ muộn dậy sớm chắc chắn đầu óc sẽ đờ đẫn buồn ngủ díp cả mắt.

Thế nhưng hiện tại, hắn lại hoàn toàn không có cảm giác mệt mỏi đó.

Đó chính là lợi ích của khí huyết hùng hậu, mang lại cho người bình thường một nguồn tinh lực dồi dào sung mãn hơn hẳn.

Vậy thì cột "Tinh thần" trên bảng số liệu rốt cuộc có tác dụng gì?

Trong lòng Phương Bình đã lờ mờ đoán ra được câu trả lời. Có lẽ, lần tới mình nên thử nghiệm tăng điểm tinh thần xem sao.

Nếu như sự gia tăng của trị số tinh thần thực sự có thể làm cho trí nhớ và khả năng lý giải của bản thân trở nên cường đại hơn, vậy thì những kỳ thi phía sau có lẽ sẽ không còn là chướng ngại khó khăn nữa.

Dẫu cho không thi đỗ thành thủ khoa, chỉ cần đạt chuẩn yêu cầu là Phương Bình đã mãn nguyện lắm rồi.

Những lời nói vô tình của Trần Phàm ngược lại đã khiến cho tảng đá trong lòng Phương Bình nhẹ bớt đi rất nhiều. Xem ra, mình vẫn phải nghĩ mọi cách để kiếm thật nhiều tiền, sau đó tiến hành thử nghiệm một phen mới được.

Bất kể là sự gia tăng của khí huyết, hay sự thăng tiến của tinh thần, tất cả đều không thể tách rời khỏi tiền.

Không có tiền, hết thảy đều là công dã tràng.

……

Các tiết học ban ngày chủ yếu vẫn là tự ôn tập và giải đề thi.

Phương Bình không lãng phí thời gian, phần lớn thời gian hắn đều vùi đầu vào đọc sách, căn bản không buồn cầm bút lên làm bài.

Các thầy cô giáo bộ môn nhìn thấy cũng không nói gì, đến giai đoạn nước rút này rồi, tất cả đều dựa vào tinh thần tự giác của học sinh.

Huống chi mấy vị giáo viên cũng nghe phong phanh chuyện Phương Bình báo danh thi võ khoa, cho nên cho dù Phương Bình có lôi sách ôn thi chuyên nghiệp võ khoa ra đọc ngay trong giờ học thì các thầy cô cũng không hề lên tiếng làm phiền.

Thời gian một ngày trôi qua thật nhanh chóng.

Đợi đến khi tiếng chuông tan học buổi chiều vang lên, lần này Phương Bình không cùng rời lớp với Trần Phàm như mọi khi nữa, mà bước chân đi thẳng về phía chỗ ngồi của Ngô Chí Hào.

Ngô Chí Hào vừa thu dọn cặp sách, vừa mỉm cười hỏi: "Thấy hôm nay cậu cả ngày đều cắm đầu đọc kiến thức thi chuyên nghiệp, cảm thấy thế nào rồi?"

"Cũng tàm tạm, khó thì không hẳn là quá khó, chỉ có điều kiến thức nhiều và tạp nham quá."

"Có một số kiến thức người ta không đưa vào đề thi đâu. Lát nữa đợi cậu photo xong cuốn sổ ghi chép, cứ việc bám sát theo những gì tớ ghi lại trong sổ mà ôn tập là được.

Đến lúc đó nếu có chỗ nào không hiểu, cậu cứ việc hỏi tớ."

"Cảm ơn cậu nhé, làm phiền cậu quá rồi."

Phương Bình lại một lần nữa cất lời cảm ơn chân thành. Vào thời điểm then chốt nước sôi lửa bỏng này, Ngô Chí Hào chịu nói ra những lời như vậy thực sự là vô cùng khó quý.

Có những học sinh giỏi, cứ đến lúc thi cử là chỉ mong sao người khác dốt đặc không biết gì, chỉ một mình mình biết hết mọi thứ mới hả lòng hả dạ.

Đương nhiên, điều này cũng bắt nguồn từ việc kỳ đại khảo võ khoa không hề bó hẹp trong phạm vi một lớp học hay một trường học.

Ngô Chí Hào cũng chưa từng coi Phương Bình là đối thủ tiềm tàng của mình. Đối thủ thực sự của cậu ta là đám học sinh ưu tú bên các lớp chọn, là tất cả những học sinh xuất sắc nhất của toàn thành phố Dương Thành, thậm chí là những học sinh kiệt xuất trên khắp cả nước.

Một người đến cả những kiến thức cơ bản nhất còn chưa nắm rõ như Phương Bình, nhất định không phải là đối tượng mà cậu ta cần phải vượt qua.

Nếu như ngay cả chút phong thái độ lượng này cũng không có, thì lấy tư cách gì để bước lên con đường trở thành võ giả?

Hai người vừa trò chuyện rôm rả, vừa cùng nhau rảo bước đi ra khỏi cổng trường.

……

Nhà của Ngô Chí Hào cách Trường Số 1 không quá xa.

Đi bộ từ trường về mất tầm hơn mười phút, cũng là một khu chung cư, nhưng môi trường cảnh quan bên trong rất đẹp, ở Dương Thành có thể xếp vào hàng ngũ khu dân cư cao cấp.

Tới bên ngoài khu chung cư, Phương Bình đưa mắt nhìn một lượt, trong lòng có chút bất ngờ. Hắn cứ tưởng gia đình Ngô Chí Hào ít nhất cũng phải ở biệt thự riêng biệt cơ chứ.

Đối với người bạn học cũ này, Phương Bình trên thực tế không hiểu biết quá nhiều, ngay cả ở kiếp trước thì hai người cũng không có nhiều cơ hội qua lại tiếp xúc với nhau.

Nhưng nghĩ đi nghĩ lại, dường như thế này cũng là điều bình thường.

Điều kiện gia đình Ngô Chí Hào cho dù có khá giả thì cũng khá giả có giới hạn, nếu không thì cậu ta đã chẳng phải học ở lớp thường. Lớp chọn của trường cấp ba, nếu gia đình chịu chi thêm một khoản tiền lớn thì vẫn có thể chạy chọt xin vào được.

Đương nhiên, cũng không loại trừ trường hợp có những người mang tâm lý "thà làm đầu gà còn hơn làm đuôi phượng", cố tình chọn ở lại lớp thường để đứng đầu.

Khu chung cư cao cấp nên ban quản lý tòa nhà cũng làm việc rất có trách nhiệm, không giống như khu nhà Phương Bình ai muốn ra vào tùy tiện cũng được, ở đây phải quẹt thẻ cư dân mới mở được cổng vào.

Hai người bước vào khuôn viên khu chung cư, Ngô Chí Hào vừa đi vừa nói: "Ngày kia Vương sư huynh về trường, không biết chúng mình có cơ hội nói chuyện riêng vài câu với anh ấy không nữa."

"Nhà trường lần này cuối cùng cũng làm được một việc ra hồn. Vương sư huynh chính là thần tượng của đám học sinh lớp thường chúng mình đấy.

Năm ngoái hai học sinh lớp thường thi đỗ vào võ khoa thì Vương sư huynh chính là một trong số đó."

"Trước kỳ thi đại học, thành tích của Vương sư huynh thực ra cũng chỉ ở mức bình thường làng nhàng, thế mà đến tháng cuối cùng bỗng nhiên bùng nổ kinh hoàng. Vương sư huynh thi đỗ vào Đại học Võ thuật Nam Giang khiến cho bao nhiêu người phải rớt cằm kinh ngạc.

Không biết anh ấy có bí quyết gì đặc biệt không, nếu như chúng mình có thể học lỏm được một chút..."

Ngô Chí Hào lẩm bẩm càu nhàu vài câu với vẻ tiếc nuối, dù cho đối phương thực sự có bí quyết bí truyền thì loại chuyện cơ mật này người ta cũng đâu thể công khai kể ra trước bàn dân thiên hạ.

Phương Bình nghe vậy trong lòng bỗng dấy lên một cảm giác kỳ lạ dị thường. Cái này mẹ nó chứ nghe qua sao thấy na ná giống hoàn cảnh của mình thế này?

Chẳng lẽ gã Vương sư huynh kia cũng là người trùng sinh sao?

Thế nhưng những câu nói tiếp theo của Ngô Chí Hào nghe qua thì lại không giống lắm, có lẽ thực sự chỉ là kết quả bùng nổ nỗ lực của một người bình thường mà thôi.

……

Vừa đi vừa nói chuyện phiếm, hai người đã bước tới trước cửa nhà Ngô Chí Hào.

Khoảnh khắc tra chìa khóa mở cửa, Ngô Chí Hào theo bản năng liếc mắt nhìn trộm Phương Bình một cái. Kết quả chỉ thấy gương mặt Phương Bình vẫn phẳng lặng thản nhiên như nước, điều này lại khiến Ngô Chí Hào cảm thấy có chút kỳ lạ.

Căn nhà của gia đình họ Ngô rất rộng rãi, hơn nữa còn là dạng căn hộ thông tầng (duplex) hai tầng lầu trên dưới, phong cách trang trí nội thất nhìn vào thời điểm hiện tại cũng thuộc hàng vô cùng sang trọng đắt tiền.

Trong tình huống bình thường, những học sinh nghèo có hoàn cảnh khó khăn như Phương Bình khi bước chân vào một căn nhà xa hoa thế này đều sẽ lộ ra vẻ mặt ao ước ghen tị, dẫu cho không ghen tị thì cũng chẳng thể nào giữ được vẻ mặt bình thản không chút dao động như vậy.

Thế nhưng Phương Bình quả thực chẳng có chút gợn sóng nào trong lòng, biểu cảm vô cùng tự nhiên thoải mái.

Nếu như biết được suy nghĩ trong đầu Ngô Chí Hào, Phương Bình nhất định sẽ nhiệt tình thỏa mãn nguyện vọng muốn thấy vẻ trầm trồ của đối phương một phen. Đáng tiếc lúc này Phương Bình thực sự không nghĩ ngợi nhiều tới mấy chuyện vụn vặt đó.

Còn về phần ngưỡng mộ hay kinh ngạc, đó toàn là chuyện nhảm nhí viển vông.

Ở kiếp trước của Phương Bình, sau khi tốt nghiệp đại học, dưới sự hỗ trợ của cha mẹ cộng thêm tiền tích lũy của bản thân, hắn cũng đã tự mua được một căn nhà không hề nhỏ. Trang trí nội thất tuy đơn giản nhưng so với nhà họ Ngô ở thời điểm năm 2008 này thì chẳng hề kém cạnh chút nào.

Huống chi căn nhà đó của Phương Bình còn nằm ở thành phố thủ phủ của tỉnh, nếu tính toán chi li ra thì giá trị khéo còn đắt đỏ hơn cả căn hộ thông tầng này của nhà họ Ngô.

Chưa kể hắn đã đi làm ngoài xã hội suốt mấy năm trời, mắt thấy tai nghe từng trải nhiều, những căn biệt thự đơn lập xa hoa lộng lẫy ở Bắc Kinh hay Thượng Hải hắn cũng từng bước chân vào tham quan mở rộng tầm mắt rồi, làm sao có thể vì một căn hộ thông tầng ở một huyện thành nhỏ bé mà phải kinh ngạc há hốc mồm cho được.

……

Trong nhà Ngô Chí Hào có người, mẹ cậu ta đang ở nhà.

Thấy con trai dẫn bạn cùng lớp về chơi, người phụ nữ cũng không nói gì nhiều, cất lời chào hỏi khách sáo vài câu rồi Ngô Chí Hào liền dẫn Phương Bình đi thẳng lên tầng hai.

Trước tiên cậu ta vào phòng sách tìm tập vở ghi chép của mình mang ra đưa tận tay cho Phương Bình. Rất nhanh sau đó, Ngô Chí Hào dẫn Phương Bình rời khỏi thư phòng, bước về phía một căn phòng nằm ngay bên cạnh.

"Đây là phòng tập thể hình, máy đo khí huyết đặt ở bên này."

Ngô Chí Hào vặn tay nắm mở cửa phòng tập ra. Bên trong căn phòng thực ra bài trí khá đơn giản, máy móc dụng cụ cũng không quá nhiều.

Quả tạ tay, tạ đòn, máy chạy bộ, khung nâng chân xà kép là toàn bộ những thứ có mặt ở đây. Riêng có một cỗ máy khác Phương Bình chưa từng nhìn thấy bao giờ, ngay cả trong các phòng gym hiện đại ở kiếp trước hắn cũng chưa từng thấy qua.

Ngoại hình của nó nhìn qua khá giống với một chiếc ghế massage toàn thân, nhưng bên cạnh lại được nối liền với một chiếc màn hình hiển thị điện tử. Nếu đoán không lầm thì đây chính là máy đo khí huyết rồi.

Sự thật chứng minh con mắt nhìn nhận của Phương Bình quả nhiên không tồi. Ngô Chí Hào dẫn Phương Bình bước tới bên cạnh chiếc "ghế massage", cười ha hả nói: "Đây chính là máy đo khí huyết. Tuy nhiên máy nhà tớ chỉ là phiên bản thô sơ giản lược thôi, không thể nào so sánh được với cỗ máy khổng lồ ở bệnh viện. Máy ở bệnh viện nhìn giống hệt như một khoang tàu vũ trụ không gian vậy, có thể tiến hành kiểm tra đo đạc toàn diện mọi chỉ số.

Còn cỗ máy của nhà tớ chỉ có thể kiểm tra áng chừng đại khái thôi.

Cậu nằm lên trên đi, để tớ giúp cậu gắn các đầu cảm biến vào, lát nữa cậu nhớ dùng sức một chút nhé……"

"Dùng sức một chút?"

Phương Bình lộ vẻ nghi hoặc khó hiểu. Ngô Chí Hào mỉm cười giải thích cặn kẽ: "Khí huyết bình thường trong cơ thể đều ở trạng thái bình hòa êm ả, chỉ khi nào nó sôi sục cuộn trào lên thì mới có thể đạt tới mức đỉnh cao nhất.

Không chỉ có thân thể phải sôi sục, mà cảm xúc tâm trạng cũng phải sôi trào lên theo. Đo kiểm tra khí huyết không đơn thuần chỉ đo lượng máu huyết chảy trong huyết quản, mà nó bao gồm cả luồng 'Khí' vô hình vô tướng nữa, cái này nói thật tớ cũng không thể giải thích rõ ràng ngọn ngành được.

Dù sao thì cả thân thể lẫn cảm xúc của cậu đều phải sôi trào bùng nổ lên thì mới có thể chạm tới giới hạn đỉnh cao thực sự của cậu.

Cậu có thấy hai cái bàn đạp ở phía dưới máy đo khí huyết kia không? Lát nữa cậu dùng hết sức bình sinh mà đạp mạnh vào đó, hai cánh tay thì cố hết sức kéo căng về phía sau, tóm lại là có bao nhiêu sức bú sữa mẹ thì cứ dồn hết ra mà dùng.

Bây giờ chúng mình tự đo kiểm tra riêng tư với nhau thì còn không sao, chứ đến lúc khám thể chất chính thức thì nhất định phải dốc toàn tâm toàn lực……"

Ngô Chí Hào giải thích một hồi dông dài, đợi đến khi thấy Phương Bình gật đầu ra hiệu đã hiểu rõ, bấy giờ mới ra dấu bảo Phương Bình nằm ngả lưng lên ghế.

Đợi Phương Bình đã nằm ngay ngắn lên ghế, Ngô Chí Hào liền cầm lấy mấy sợi dây có đầu cảm biến trông gióng như ống nghe của bác sĩ ở xung quanh chiếc "ghế massage", lần lượt dán chặt vào hai cánh tay, hai bắp chân, vùng ngực trái nơi có trái tim và trên trán của Phương Bình.

"Đến lúc đi khám thể chất thực sự thì quy trình không giống thế này đâu. Đến lúc đó người ta sẽ không dán mấy cái đầu cảm biến này lên người cậu, mà cậu sẽ bước thẳng vào trong khoang khí huyết chuyên dụng, ở bên trong cậu cứ tự do vận động là được.

Khoang khí huyết có thể thông qua một loạt các biện pháp công nghệ cao để đưa ra kết quả phản hồi chi tiết và chuẩn xác nhất, lúc đó mới có thể đo lường được trị số khí huyết thực sự của cậu."

Nói dứt lời, Ngô Chí Hào với tay bật công tắc chiếc màn hình hiển thị bên cạnh lên, vội vàng giục giã: "Có thể bắt đầu rồi đấy! Nhớ kỹ nhé: Vận động kịch liệt vào, tâm trạng cũng phải dâng trào dao động mạnh lên, nếu không được thì cứ tưởng tượng đến mấy bộ phim con heo nóng bỏng đi……"

Phương Bình vốn dĩ đang hít sâu chuẩn bị dồn lực, nghe thấy câu nói bựa này suýt chút nữa thì sặc nghẹn đứt cả hơi! Cái thằng nhóc này, hóa ra bên ngoài nhìn thư sinh đứng đắn thế mà bên trong cũng chẳng phải dạng hiền lành tử tế gì cho cam.

Chẳng thèm chấp nhặt với tên này, Phương Bình hít sâu một hơi thật dài, kế đó hai chân liền điên cuồng dồn sức đạp mạnh vào hai chiếc bàn đạp dưới chân, hai cánh tay cũng dùng hết toàn lực kéo căng mạnh mẽ sang hai bên!

Ngô Chí Hào đứng bên cạnh, hai mắt mở to tò mò dán chặt vào chiếc màn hình hiển thị bên cạnh……"""
    },
    12: {
        "url": "https://www.piaotia.com/html/9/9640/6523766.html",
        "title_vi": "Chương 12: Lời Thề Tàn Nhẫn!",
        "content_vi": """Bên trong phòng tập thể hình.

Các con số trên màn hình hiển thị không ngừng nhảy múa chớp nháy liên hồi.

Cùng với những tiếng thở dốc hồng hộc bắt đầu vang lên từ miệng Phương Bình, dãy số trên màn hình rốt cuộc cũng từ từ đứng yên bất động.

"113 cal!"

Ngô Chí Hào trố tròn hai mắt, cả khuôn mặt ngập tràn vẻ khó tin đến tột cùng!

Đúng vậy, chiếc máy đo khí huyết cỡ nhỏ của gia đình cậu ta có sai số lớn là không sai.

Thế nhưng sai số lên xuống cũng chỉ nằm trong khoảng 5 cal mà thôi!

Nói cách khác, trị số khí huyết thực tế của Phương Bình thấp nhất cũng là 108 cal, còn cao nhất thì lên tới tận 118 cal, làm sao có thể như vậy được chứ!

"Làm sao có thể như thế được!"

Ngô Chí Hào thực sự không hề có ý khinh thường hay xem nhẹ Phương Bình, nhưng điều này hoàn toàn phản khoa học mà?

Nếu như nói là Dương Kiến lần đầu tiên đo khí huyết đạt điểm cao thì cậu ta hoàn toàn công nhận và phục lăn.

Người ta vai u thịt bắp, vóc dáng cao to vạm vỡ như hộ pháp, nhìn qua một cái là biết thân thể tráng kiện khỏe như trâu mộng, khí huyết cao hơn người bình thường một chút là chuyện hết sức bình thường.

Thế nhưng cho dù là Dương Kiến đi chăng nữa, thì sự cường tráng đó cũng được xây dựng dựa trên nền tảng gia cảnh khá giả, mỗi bữa cơm đều được ăn uống tẩm bổ đầy đủ chất dinh dưỡng.

Dẫu cho có như vậy, lần đầu tiên đo kiểm tra của Dương Kiến cũng đâu có cao ngất ngưởng tới mức này?

Còn Phương Bình……

Ban đầu trong mắt Ngô Chí Hào, Phương Bình có tự tin đăng ký báo danh, cho dù có cao hơn người bình thường một chút thì cậu ta vẫn hoàn toàn có thể tiếp nhận được, ví dụ như 102 cal, 103 cal……

Thế nhưng bây giờ thì sao?

Con số hiển thị rành rành ra đó là 113 cal! Cho dù có trừ hao sai số ở mức thấp nhất thì cũng đạt tới 108 cal, trong nháy mắt đã san bằng tiêu chuẩn của những người như Trương Nam, Trương Hạo rồi.

Trong số 8 học sinh cùng lớp đăng ký dự thi đợt này, người có điểm số thấp nhất chỉ đạt có 106 cal. Điều đó có nghĩa là Phương Bình lúc này thế mà lại chẳng phải là kẻ đội sổ lẹt đẹt ở đáy bảng xếp hạng!

Trong lúc Ngô Chí Hào còn đang chết trân đứng hình ngẩn ngơ ra đó, Phương Bình trên ghế vẫn đang cắn răng ra sức đạp mạnh vào hai chiếc bàn đạp.

Chờ mãi một lúc lâu không thấy động tĩnh gì, Phương Bình không nhịn được thở dốc hổn hển hỏi: "Được chưa vậy cậu?"

Ngô Chí Hào bấy giờ mới bừng tỉnh khỏi cơn chấn động, giọng nói có chút ngơ ngác đờ đẫn: "Được……"

Vừa định thốt ra chữ "được rồi", Ngô Chí Hào bỗng nhiên đổi giọng nói: "Vừa rồi có lẽ mấy đầu cảm biến tiếp xúc chưa được tốt lắm, cậu thử lại thêm một lần nữa xem sao."

Phương Bình liếc xéo cậu ta một cái. Tuy rằng cảm thấy lý do tên này đưa ra có chút không đáng tin cậy cho lắm, nhưng dù sao cũng đã nhận ân tình của người ta rồi, thử lại một lần thì thử lại một lần vậy.

Nói đi thì cũng phải nói lại, cái trò đo đạc kiểm tra này đúng là một công việc lao động tay chân nặng nhọc, thực sự là quá mức phiền toái mệt mỏi.

Đợi Ngô Chí Hào giúp hắn chỉnh đốn lại vị trí các đầu cảm biến, Phương Bình lại một lần nữa gồng mình dốc sức vận động điên cuồng, cả người mồ hôi mồ kê vã ra như tắm, mệt đến mức thở không ra hơi.

Đừng thấy chỉ vận động trong một chốc lát ngắn ngủi như vậy, khối lượng vận động dồn dập tiêu hao là cực kỳ khủng khiếp.

Ba phút sau, con số trên màn hình lại một lần nữa dừng lại — 108 cal.

Ngô Chí Hào nhanh chóng làm một phép tính trong đầu: Lần này phạm vi dao động là từ 103 đến 113 cal, kết hợp đối chiếu với kết quả lần đo trước, vậy thì phạm vi khí huyết thực tế của Phương Bình chắc chắn dao động chuẩn xác trong khoảng từ 108 đến 113 cal!

Trị số cao nhất tuy chưa bằng cậu ta, bản thân Ngô Chí Hào đã chạm tới mốc 115 cal.

Thế nhưng cho dù lấy con số thấp nhất là 108 cal đi chăng nữa, thì đối với một người chưa từng qua trường lớp rèn luyện nào như Phương Bình đã là một kết quả cực kỳ ghê gớm chấn động rồi.

Trầm ngâm suy tính một lát, Ngô Chí Hào lại ngập ngừng mở miệng: "Hình như số liệu vẫn chưa được chuẩn xác lắm, hay là chúng mình làm lại thêm một lần nữa nhé?"

Phương Bình: "……"

Phương Bình lúc này làm sao không nhìn ra tâm tư suy nghĩ của tên này cơ chứ, hắn lau mồ hôi nhễ nhại trên trán, dở khóc dở cười nói: "Thôi bỏ đi cậu ơi, bây giờ tớ mệt đến mức đứt cả hơi rồi, thể lực hoàn toàn không còn ở trạng thái đỉnh cao nữa, có đo tiếp cũng chẳng thể nào chuẩn xác được đâu."

Lời này nói ra quả thực hoàn toàn chuẩn xác không có chỗ nào bắt bẻ được. Trong tình trạng cơ thể đã kiệt sức mệt mỏi, nếu cứ tiếp tục đo nữa thì kết quả chỉ có nước tụt dốc ngày càng thấp đi mà thôi.

Thế nhưng con số từ 108 cal trở lên vẫn khiến cho cõi lòng Ngô Chí Hào cuộn trào sóng gió, khó lòng mà bình tĩnh lại được.

Trong sâu thẳm tâm can bất giác dâng lên một cỗ cảm giác ghen tị âm ỉ, Ngô Chí Hào nhịn không được lên tiếng hỏi: "Bình thường cậu có thường xuyên ăn các loại đồ ăn bổ dưỡng bổ khí huyết không? Hay là cậu từng uống qua các loại dược phẩm bồi bổ khí huyết rồi?"

Đồ bồi bổ cũng chia làm hai loại: Một loại là thực bổ (bồi bổ bằng đường ăn uống), một loại là dược bổ (bồi bổ bằng thuốc).

Thực bổ thì mang lại hiệu quả chậm, liệu trình kéo dài, nhưng chi phí tốn kém ít hơn, tính tổng thể lại thì tiết kiệm tiền hơn nhiều so với việc dùng thuốc bồi bổ.

Còn về phần dược bổ, tuy rằng hiệu quả phát huy vô cùng nhanh chóng rõ rệt, nhưng thứ nhất là giá thành vô cùng đắt đỏ trên trời, thứ hai là rất dễ rơi vào tình trạng quá mức chịu đựng của cơ thể dẫn đến tác dụng ngược, rất nhiều khi dược hiệu quý giá bị đào thải lãng phí ra ngoài.

Phương Bình nhìn thấy bộ dạng của cậu ta giống hệt như đang vô cùng lo sợ mình sẽ thốt ra bốn chữ "thiên phú dị bẩm", trong lòng bất giác dâng lên một cỗ đồng cảm sâu sắc, bèn mở miệng an ủi: "Nhà tớ ngày nào cũng bắt tớ ăn toàn dược liệu đại bổ quý hiếm, bố mẹ tớ táng gia bại sản gom tiền mua đồ ngon đồ bổ cho tớ ăn, cả nhà chỉ trông cậy vào mỗi việc tớ thi đỗ võ khoa để gỡ lại vốn liếng thôi đấy……"

Lời nói dối này nghe qua kiểu gì cũng thấy giả trân hết chỗ nói!

Ngô Chí Hào tuy rằng cảm thấy chuyện này có chút khó tin và không mấy khả thi, nhưng nghĩ tới ngày khám thể chất đã cận kề trước mắt, vả lại điểm số của Phương Bình rốt cuộc vẫn chưa vượt qua được cậu ta, cho nên trong lòng cũng miễn cưỡng chấp nhận lời giải thích này.

Đè nén sự ghen tị xuống đáy lòng, Ngô Chí Hào cười khổ nói: "Được rồi, ban đầu tớ cứ ngỡ cùng lắm cậu cũng chỉ đạt tầm khoảng 105 cal là cùng, giờ xem ra là tớ đoán sai bét rồi.

Trị số khí huyết của cậu nằm trong khoảng từ 108 đến 113 cal.

Máy đo khí huyết gia đình rốt cuộc cũng không chuẩn xác tuyệt đối, đo nhiều lần thì có thể tiệm cận con số thực hơn, nhưng trạng thái cơ thể không ở đỉnh cao thì cũng không đáng tin cậy cho lắm.

Nếu như cậu thực sự muốn biết con số cụ thể chính xác tới từng cal, thì tốt nhất nên ra Bệnh viện Nhân dân Số 1 để kiểm tra một chuyến."

Phương Bình cười xòa nói: "Để tớ xem xét tình hình thế nào đã, lần này thật sự cảm ơn cậu rất nhiều."

"Khách sáo làm gì……"

Ngô Chí Hào suy nghĩ một chút, vẻ mặt có chút ngập ngừng muốn nói lại thôi, cuối cùng vẫn quyết định mở lời: "Nếu như cậu thực sự có khí huyết từ 110 cal trở lên, về nhà cậu có thể bảo bố mẹ chuẩn bị cho một ít thuốc bổ khí huyết.

Cậu mới vừa đăng ký dự thi nên có nhiều chuyện cậu chưa nắm rõ đâu.

Thông thường, bọn tớ trước khi bước vào kỳ khám thể chất đều sẽ chuẩn bị sẵn một số loại thuốc để tẩm bổ bộc phát khí huyết.

Những nhà có điều kiện kinh tế không mấy dư dả thì ít nhất cũng sẽ chuẩn bị một viên Bổ Huyết Hoàn.

Nhà nào khá giả hơn một chút thì sẽ chuẩn bị viên Bổ Khí Hoàn……"

"Bổ Huyết Hoàn, Bổ Khí Hoàn?"

Phương Bình bất giác nhớ tới những mẩu quảng cáo dán khắp nơi mà mình từng nhìn thấy ở trường học trước đó, vội vàng hỏi dồn: "Tớ quả thật chưa từng để ý tới mấy thứ này, trước kia cũng đâu có tính chuyện thi võ khoa.

Mấy loại thuốc đó giá cả bao nhiêu tiền vậy cậu?"

"Bổ Huyết Hoàn tầm khoảng 5.000 tệ một viên, Bổ Khí Hoàn thì đắt hơn một chút, chừng khoảng 1 vạn tệ một viên."

"Thế còn Huyết Khí Hoàn thì sao?"

Phương Bình lại hỏi thêm một câu, đây chính là cái tên được nhắc tới nhiều nhất trên các tờ rơi quảng cáo ở trường học.

"Xem cậu mua theo kênh nào đã, thực ra giá cả của những thứ này ở các nơi đều không giống nhau. Ở các hiệu thuốc lớn chính quy của nhà nước thì bán giá 3 vạn tệ một viên, tuy nhiên có một số tiệm thuốc tư nhân không có giấy phép kinh doanh loại thuốc đặc thù này, nếu quen biết thì khéo 2 vạn tệ là có thể mua được một viên rồi.

Thế nhưng rất khó tìm, mà nhiều khi cậu có tìm ra được chỗ bán thì người ta chưa chắc đã dám bán cho cậu."

Ngô Chí Hào giải thích đại khái vài câu, thấy Phương Bình đang trầm ngâm suy nghĩ, lại bồi thêm: "Năm ngoái Đại học Võ thuật Nam Giang lấy tiêu chuẩn tuyển sinh tối thiểu 112 cal, thực chất đó là áp dụng đối với những thí sinh có thành tích ở các hạng mục thi cử khác thuộc hàng xuất sắc vượt trội.

Có những bạn điểm thi văn hóa cực kỳ cao, thi môn chuyên nghiệp cũng làm bài rất tốt, chỉ có khí huyết là hơi yếu một chút, cho nên 112 cal mới có thể lách qua khe cửa hẹp để vào trường.

Nhưng nếu như các môn thi khác điểm số không cao, chỉ vừa vặn chạm vạch điểm sàn, thì yêu cầu về mặt khí huyết sẽ bị đẩy lên rất cao.

Đại học Võ thuật Nam Giang tớ vẫn luôn theo dõi sát sao từ lâu rồi, cũng từng đi hỏi dò các anh chị khóa trên, năm ngoái phần lớn sinh viên trúng tuyển thực chất đều có khí huyết dao động tầm khoảng 115 cal.

Năm nay có thể sẽ còn cao hơn một chút nữa, nếu không thì bản thân tớ cũng chẳng phải lo ngay ngáy chuyện thi trượt làm gì.

Trường hợp của cậu thì……"

Ngô Chí Hào lại ngập ngừng dừng lại một lát, giọng nói không quá chắc chắn: "Hiện tại khí huyết chính xác của cậu là bao nhiêu tớ cũng không dám khẳng định, tớ khuyên cậu tốt nhất nên ra bệnh viện kiểm tra cho rõ ràng. Nếu như thực sự đạt từ 110 cal trở lên, vậy thì cậu bảo bố mẹ cắn răng mua lấy một viên Khí Huyết Đan mà dùng thử xem sao."

"Khí Huyết Đan?"

Ngô Chí Hào gật đầu xác nhận: "Ừm, những thứ này đều là các sản phẩm thuốc bổ được bán ở các hiệu thuốc chính quy. Nghe đồn bên trên còn có những loại thần dược cao cấp hơn nữa, nhưng cái đó chẳng liên quan gì tới chúng mình, chưa trở thành võ giả thực thụ thì có uống vào cũng chỉ tổ phí phạm thuốc mà thôi.

Khí Huyết Đan chính là loại thuốc bổ tốt nhất mà thí sinh như chúng mình có thể tiếp cận được rồi. Nếu như vận may tốt, dược hiệu không bị đào thải hao hụt nhiều, thì đến lúc khám thể chất có khả năng bộc phát tăng thêm được từ ba đến bốn cal là hoàn toàn có thể!

Tuy nhiên Khí Huyết Đan có giá hơi đắt đỏ một chút, tròn 10 vạn tệ một viên……"

Phương Bình trong nháy mắt dập tắt ngay ý niệm vừa nhen nhóm trong đầu!

Đùa cái kiểu gì thế không biết, có 10 vạn tệ tiền mặt trong tay thì hắn đã có thể đổi được hẳn 1 điểm khí huyết nguyên vẹn trên hệ thống rồi, mặc dù chưa biết giai đoạn sau tỷ lệ quy đổi tài phú có thay đổi hay không.

Thế nhưng bất kể nói thế nào đi chăng nữa, có 10 vạn tệ trong tay thì hắn có thể làm được biết bao nhiêu việc đại sự, có điên mới đi ném tiền qua cửa sổ để mua cái viên thuốc quỷ tha ma bắt này.

Khí Huyết Đan là loại thuốc tốt nhất mà hiệu quả mang lại cũng chỉ vỏn vẹn có ngần ấy, vậy thì những loại thuốc cấp thấp khác lại càng chẳng cần phải bàn tới làm gì cho mệt.

Ban đầu Phương Bình còn có chút hứng thú tò mò đối với các loại dược phẩm bồi bổ này, giờ phút này thì đã hoàn toàn dẹp bỏ sạch sành sanh mọi ý nghĩ đó ra khỏi đầu.

Hắn mới chỉ có 1.1 điểm khí huyết trên bảng số liệu thôi mà đã tương đương với khoảng 110 cal rồi, nếu như thăng lên 1.2 điểm, chẳng lẽ lại không đạt tới 120 cal sao?

Hiệu quả mang lại từ 1 vạn tệ của hệ thống còn vượt trội hơn hẳn số thuốc bổ trị giá hàng chục vạn tệ mà đám người kia phải bỏ tiền túi ra mua, đến lúc này Phương Bình mới thấm thía nhận ra mình đã vớ bẫm món hời to lớn đến nhường nào.

Hơn nữa số tiền mặt đó của hắn tiêu hao trên hệ thống xong vẫn còn nguyên vẹn, chứ đâu có bị biến mất!

Việc đo kiểm tra đã xong xuôi, Phương Bình cũng không nán lại lâu làm gì, cùng Ngô Chí Hào rảo bước đi xuống tầng dưới.

Mẹ của Ngô Chí Hào vô cùng nhiệt tình hiếu khách, tha thiết giữ Phương Bình ở lại dùng bữa cơm tối cùng gia đình.

Phương Bình đương nhiên sẽ không vô duyên vô cớ ở lại ăn chực, hắn khéo léo nói lời cảm ơn từ chối vài câu rồi khoác cặp sách lên vai bước ra khỏi cửa.

Hắn vừa đi khỏi, mẹ Ngô Chí Hào liền tò mò cất tiếng hỏi: "Trước đây mẹ chưa từng thấy bạn này của con bao giờ, bạn mới quen à?"

Ngô Chí Hào lắc đầu, giải thích: "Bạn cùng lớp đăng ký thi võ khoa mẹ ạ. Cậu ấy chưa từng đi kiểm tra khí huyết bao giờ nên con dẫn về nhà kiểm tra thử cho cậu ấy."

Vừa nghe thấy câu đó, mẹ Ngô Chí Hào liền hiểu ngay gia cảnh của Phương Bình chắc chắn không mấy dư dả gì.

Nếu không, đã báo danh thi võ khoa rồi mà sao đến một lần đi kiểm tra sức khỏe cũng chưa từng làm.

Bà theo bản năng thuận miệng nhận xét một câu: "Thằng bé nhìn hơi gầy guộc, chắc điểm số không cao đâu nhỉ?"

Ngô Chí Hào gãi gãi đầu, vẻ mặt buồn bực ỉu xìu đáp: "Cao lắm đấy mẹ ạ, thấp nhất cũng phải từ 108 cal trở lên. Mẹ ơi, con ngày nào cũng ăn ngon uống bổ ngập mồm, thế mà lần đầu tiên đo hình như cũng chỉ mới được có 103 cal thôi đúng không mẹ? Có phải hồi nhỏ mẹ ngược đãi bỏ đói con không vậy?"

Mẹ Ngô Chí Hào trừng mắt lườm con trai một cái cháy mặt. Ngược đãi cái con khỉ mốc! Vì để cho cái thằng nhóc nghịch tử này dùi mài kinh sử thi võ khoa mà cái nhà này khéo sắp cạn kiệt đến mức không còn gạo mà nấu cơm rồi đây này.

Hai vợ chồng phấn đấu bôn ba suốt bao nhiêu năm trời, đến bây giờ tích lũy lại cũng chỉ còn trơ trọi lại mỗi căn nhà này mà thôi.

……

Khu dân cư Cảnh Hồ Viên.

Tòa 6 phòng 101.

Hôm nay Phương Bình về nhà hơi muộn một chút, lúc hắn bước chân vào nhà thì cả gia đình đều đã tề tựu đông đủ.

Không đợi bố mẹ kịp lên tiếng tra hỏi, Phương Bình đã mặt mày hớn hở toe toét cười nói: "Bố ơi, hôm nay con nộp xong tiền lệ phí báo danh võ khoa rồi, thầy chủ nhiệm còn tặng riêng cho con một bộ tài liệu ôn thi võ khoa dày cộp nữa đấy.

Chưa hết đâu nhé, lúc tan học con vừa qua nhà một bạn cùng lớp, làm một bài kiểm tra đo khí huyết xong xuôi rồi……"

"Kiểm tra khí huyết?"

Chuyện này Phương Danh Vinh tuy không quá am hiểu sâu sắc, nhưng cũng từng nghe người ta bàn tán xôn xao, bèn ngạc nhiên hỏi: "Ở nhà người ta mà cũng kiểm tra được cơ à?"

"Vâng, máy mini cỡ nhỏ của gia đình thôi ạ, độ chuẩn xác không cao lắm." Phương Bình giải thích một câu, kế đó lập tức cười rạng rỡ nói: "Bố có biết khí huyết của con đo ra được bao nhiêu không?"

Phương Danh Vinh về phương diện này không hiểu biết nhiều, ngược lại con nhóc Phương Viên thì lại nắm được chút ít thông tin, nghe vậy liền cười hì hì trêu chọc: "Chắc được 95 cal chứ gì? Anh chạy bộ có một đoạn ngắn mà đã thở hồng hộc như trâu rồi, sức khỏe chắc chắn yếu xìu. Anh trai một bạn cùng lớp em từng đi bệnh viện kiểm tra rồi, được tận 104 cal, nghe nói điểm đó là đã đủ điều kiện để thi võ khoa rồi đấy nhé!"

Phương Bình bĩu môi khinh bỉ: "104 cal mà cũng đòi le te đi thi võ khoa, bộ tưởng võ khoa là mớ rau ngoài chợ rẻ rúng thế chắc?

Thế mà cũng dám lấy ra khoe khoang làm như tự hào lắm, không thấy xấu hổ à.

Anh trai của em đây này, tùy tiện đo đại một phát cũng trên 110 cal, khéo con số thực tế còn bị chiếc máy đó đo thấp đi ấy chứ!"

Phương Viên chớp chớp hai mắt to tròn, kế đó liền "xì" một tiếng thật dài, quay phắt sang mách với bố: "Bố ơi, Phương Bình lại bắt đầu bốc phét chém gió rồi đấy!

Bạn học của con bảo rồi, thi đỗ võ khoa điểm số cũng chỉ tầm 110 cal đổ lại thôi mà……"

"Đó là chuyện từ đời tám hoánh nào rồi nhóc con ạ! Năm ngoái tiêu chuẩn tối thiểu của Đại học Võ thuật Nam Giang đã là 112 cal rồi, mặt bằng chung toàn dao động quanh mốc 115 cal.

Năm nay chắc chắn sẽ còn nhích lên cao hơn một chút nữa. Thế nhưng anh trai em là bậc kỳ tài thiên phú dị bẩm, cơ thể vẫn đang trong giai đoạn phát triển lớn lên từng ngày, khí huyết tự nhiên cũng sẽ tăng vùn vụt theo.

Đợi đến ngày khám thể chất chính thức, anh chắc chắn sẽ vượt chuẩn dư sức. Năm nay thi võ khoa, anh nắm chắc mười phần trong tay!"

Phương Bình nói những lời hùng hồn này một phần cũng là để làm yên lòng cha mẹ. Dù sao cũng là cả một món tiền 1 vạn tệ mồ hôi nước mắt, nếu không có chút thành tích le lói nào thì bản thân hắn cũng chẳng mặt mũi nào mà ăn nói với gia đình.

Thế nhưng nghe hắn dõng dạc tuyên bố như vậy, cả Phương Danh Vinh lẫn Lý Ngọc Anh đều sững sờ chết lặng tại chỗ.

Con trai mình lại có thể chạm gần tới cánh cửa võ khoa đến như vậy sao?

Hai vợ chồng vừa cảm thấy khó tin đến nghẹn ngào, lại vừa có chút nghi hoặc tự hỏi liệu có phải thằng con trai mình đang bốc phét nói khoác để bố mẹ vui lòng hay không?

Thế nhưng nhìn bản mặt Phương Bình lại vô cùng nghiêm túc, thề thốt chắc nịch như đinh đóng cột, cuối cùng hắn thậm chí còn đưa tay nhéo chặt lấy cái má tròn vo núng nính của Phương Viên, lớn tiếng bảo đảm: "Thật sự có trên 110 cal mà! Nếu như con nói dối, con xin thề từ nay về sau sẽ không bao giờ véo má Phương Viên thêm một lần nào nữa!"

"Mẹ ơi cứu con!"

Phương Viên vẻ mặt tràn đầy oan ức mếu máo kêu to: "Anh ấy thề thốt chuyện của anh ấy, mắc mớ gì lại lôi con ra làm vật thề độc thế này chứ!" """
    },
    13: {
        "url": "https://www.piaotia.com/html/9/9640/6523767.html",
        "title_vi": "Chương 13: Phương Bình Hố Cha",
        "content_vi": """Phương Bình thề thốt chắc nịch như đinh đóng cột, khiến cho vợ chồng Phương Danh Vinh dù có nửa tin nửa ngờ thì lúc này cũng không thể không tin.

Tin vào lời con trai nói rồi, hai vợ chồng trước tiên là dâng lên một nỗi vui mừng khôn xiết, nhưng ngay sau đó trong lòng lại bất giác chùng xuống, thậm chí dâng lên một cỗ cảm giác áy náy và tự trách sâu sắc.

Hiển nhiên, họ hoàn toàn tin vào lời Phương Bình: Con trai mình thực sự là một đứa trẻ có thiên phú dị bẩm trời ban.

Thế nhưng bấy lâu nay, chính sự nghèo khó và thiếu hiểu biết của bậc làm cha làm mẹ như họ đã làm lỡ dở tương lai của con mình.

Cứ nghĩ tới việc nếu như con trai mình được sinh ra trong một gia đình giàu sang phú quý có điều kiện……

Hai vợ chồng căn bản không dám tiếp tục nghĩ tiếp nữa. Trên bàn ăn, nụ cười gượng gạo nở trên môi, nhưng tận sâu trong đáy mắt lại là nỗi thất vọng và dằn vặt khôn nguôi không cách nào che giấu nổi.

……

Ăn cơm xong xuôi, Lý Ngọc Anh thu dọn bát đũa mang vào gian bếp sau nhà để rửa, Phương Danh Vinh cũng lẳng lặng cất bước đi theo vào trong.

Phương Viên xoa xoa cái bụng nhỏ no tròn căng, tâm trạng của cô bé lúc này cũng vô cùng vui vẻ thoải mái. Mấy ngày hôm nay cái tên Phương Bình đáng ghét kia dường như không còn tranh giành đồ ăn ngon với cô bé nữa, ngày nào cô bé cũng được ăn uống no nê thỏa thích.

Thế nhưng Phương Bình không thèm tranh giành với mình nữa thì con nhóc lại cảm thấy có chút hụt hẫng trống vắng trong lòng, cứ cảm giác đồ ăn không còn thơm ngon đậm đà như trước kia nữa.

Tiếp tục chủ đề lúc nãy, vừa thấy bố mẹ đi vào bếp, Phương Viên liền hưng phấn ghé sát lại hỏi: "Phương Bình, anh thật sự có thể thi đỗ võ khoa sao?"

"Dĩ nhiên rồi!"

"Nhưng mà tại sao em cứ có cảm giác anh đang bốc phét chém gió thế nhỉ?"

"Giữa người với người với nhau dành cho nhau chút niềm tin có được không hả cô nương?"

Phương Viên miễn cưỡng gật đầu coi như nể mặt ông anh trai một chút, kế đó lại thò đầu sang thăm dò: "Thế nếu như anh thi trượt, sau này thật sự không véo má em nữa chứ?"

Mặt Phương Bình đen thui như đít nồi, quay sang trừng mắt nhìn cô bé: "Em có bị ngốc không đấy hả? Đợi đến khi anh trai em thi đỗ võ khoa, trở thành võ giả thực thụ rồi thì em muốn cái gì mà chẳng có?

Đến lúc đó, anh dẫn em đi ăn gà rán KFC thỏa thích, dẫn em đi sắm quần áo mới xúng xính, dẫn em đi rạp chiếu phim xem phim bom tấn, tiện thể còn có thể giúp em đấm cho mấy thằng nhóc hay đặt biệt danh trêu chọc em một trận tơi bời hoa lá.

Em nói xem, so với việc bị véo má mấy cái, em chọn cái nào?"

Cô bé trong nháy mắt rơi vào trạng thái giằng xé nội tâm vô cùng kịch liệt!

Những lời Phương Bình nói nghe qua sao mà có lý quá chừng vậy nè!

Phương Bình cũng chẳng rảnh rỗi đâu mà đôi co với con bé, hắn đứng bật dậy chuẩn bị rảo bước đi về phía gian bếp sau nhà.

Phương Viên thấy hắn lén la lén lút như ăn trộm, nhịn không được hỏi với theo: "Anh định làm gì đấy?"

"Bố mẹ chắc chắn đang bàn bạc xem kế tiếp phải bỏ ra bao nhiêu tiền để mua đồ tẩm bổ cho anh, anh ra nghe ngóng xem sao."

Phương Bình đâu có ngu ngốc. Bố mẹ cùng nhau đi vào bếp, thời điểm này thì bàn bạc chuyện gì, hắn dùng đầu ngón chân cũng có thể đoán ra được.

Thế nhưng chuyện này tuyệt đối không thể để cho bố mẹ tự ý quyết định được. Nếu như bố mẹ thực sự cắn răng dốc hết vốn liếng trong nhà, lén lút đi mua mấy thứ thuốc bổ đắt đỏ về cho hắn, ví dụ như viên Khí Huyết Đan giá mười vạn tệ kia, thì Phương Bình chắc tức đến hộc máu mà chết mất.

Mà khả năng này lại cực kỳ dễ xảy ra!

Hơn nữa bố mẹ một khi đã mua thì chắc chắn sẽ âm thầm lén lút đi mua, mua xong xuôi mang về nhà rồi mới báo cho hắn biết, đến lúc đó thì có hối hận cũng đã muộn màng không kịp nữa rồi.

Thay vì ngồi đó chờ chết, chi bằng nghĩ cách "hố" bố mẹ mình một vố trước cho xong.

Vào thời điểm nước sôi lửa bỏng này, Phương Bình cũng đang vô cùng cấp bách cần tiền. Tạm thời hắn vẫn chưa nghĩ ra cách nào để có thể kiếm được một món tiền lớn nhanh chóng trong thời gian ngắn, mà cho dù có nghĩ ra được đi chăng nữa thì trong tay cũng phải có chút vốn liếng giắt lưng mới làm ăn được chứ.

Lúc này nghĩ cách hố bố mẹ một phen, Phương Bình cũng chẳng cảm thấy cắn rứt hay có gánh nặng tâm lý gì quá lớn.

Chỉ cần thi đỗ vào võ khoa rồi thì mọi thứ sẽ được đền đáp gấp bội, tiền bạc mất đi đều có thể lấy lại hết.

Mà dẫu cho có thi trượt đi chăng nữa, thì Phương Bình cũng không cho rằng bản thân mình sẽ biến thành một kẻ phế nhân vô dụng của xã hội.

……

Gian bếp ở sân sau.

Mọi chuyện diễn ra y hệt như những gì Phương Bình đã dự liệu.

Phương Danh Vinh đang rít từng hơi thuốc lá sâu, đôi lông mày nhíu chặt lại thành một đường, hạ thấp giọng hỏi vợ: "Trong nhà mình hiện tại còn bao nhiêu tiền tiết kiệm?"

"Hơn năm vạn tệ một chút anh ạ, mấy năm nay thằng Bình với con Viên đi học tốn kém nhiều quá……"

"Ngày mai tan làm em ra ngân hàng rút hết số tiền đó về đây. Thằng Bình tuyệt đối không thể để chúng mình làm lỡ dở thêm nữa.

Cũng tại anh, trước đây trong phân xưởng đã có con của mấy vị lãnh đạo đi làm kiểm tra khí huyết rồi, lúc đó anh vô tâm quá không nghĩ ngợi sâu xa.

Nếu không phải……

Haizz!"

Phương Danh Vinh thở dài thườn thượt một hơi. Nếu không phải lần này Phương Bình tự mình chủ động kiên quyết đòi đăng ký dự thi, thì ông căn bản cũng chưa từng có ý định để con trai mình thi vào võ khoa.

Thế nhưng ai mà ngờ được thằng con trai mình lại thực sự có thiên phú trời cho như vậy chứ, chuyện này khiến cho lão Phương hối hận đến đứt từng khúc ruột.

Bây giờ kỳ thi đại học đã cận kề ngay trước mắt rồi, chẳng biết liệu có còn kịp thời gian nữa hay không.

Lại thở dài một hơi, Phương Danh Vinh tiếp tục nói: "Anh nghe chủ nhiệm phân xưởng của anh kể lại rồi, con trai ông ấy năm ngoái lúc ôn thi đại học cũng mua rất nhiều thuốc bổ về tẩm bổ, hiệu quả mang lại rất tốt.

Trong hai tháng tới này, chúng mình phải cố gắng mua thật nhiều đồ bổ dưỡng ngon lành về bồi bổ cho thằng Bình.

Để ngày mai anh đi hỏi dò thêm xem có loại dược phẩm nào có thể giúp ích được nữa không, nếu thiếu tiền thì đi vay mượn anh em bạn bè thêm một ít.

Đợi sau khi thằng Bình thi xong đại học, cũng phải đưa con Viên đi bệnh viện kiểm tra một chuyến, nếu như lại để sự nghèo khó của hai vợ chồng mình làm lỡ dở nốt đời con bé thì đúng là hủy hoại cả đời hai đứa nhỏ mất!"

Lý Ngọc Anh im lặng hồi lâu không nói nên lời, mãi một lúc sau bà mới khẽ khàng cất giọng: "Được rồi anh, ngày mai tan ca làm em sẽ ra ngân hàng rút tiền về."

"……"

Hai vợ chồng đang thì thầm to nhỏ bàn bạc với nhau, Phương Bình đứng ngoài nghe ngóng cũng đã nắm bắt được hòm hòm mọi chuyện, bèn từ tốn bước chân vào trong gian bếp.

Vừa thấy bóng dáng con trai bước vào, hai vợ chồng lập tức im bặt, không tiếp tục nhắc tới chủ đề đó nữa.

Phương Bình cũng vờ như mình chẳng hề hay biết chuyện gì, làm ra vẻ mặt khó xử ngập ngừng nói: "Bố mẹ ơi, con có chuyện này muốn thưa với bố mẹ."

Phương Danh Vinh vội vàng dập tắt mẩu thuốc lá đang cháy dở, ngẩng đầu bảo: "Có chuyện gì con cứ nói đi."

"Chuyện là thế này ạ, hôm nay con chẳng phải qua nhà bạn học đo kiểm tra khí huyết sao? Cậu bạn đó của con là người có thành tích học tập xuất sắc nhất lớp, năm nay cậu ấy nắm chắc phần thắng thi đỗ vào trường đại học võ khoa.

Cậu ấy bảo với tình hình hiện tại của con thì xác suất thi đỗ là có, nhưng từ giờ đến lúc thi cần phải chuẩn bị thêm một số thứ."

Phương Danh Vinh sốt sắng hỏi dồn: "Con nói mau xem nào, cần chuẩn bị những gì? Những chuyện khác con không cần phải bận tâm lo lắng, chỉ cần có thể thi đỗ vào võ khoa thì bố nhất định sẽ nghĩ mọi cách lo liệu cho con!"

"Dạ, cậu ấy bảo tốt nhất là con nên mua một ít dược phẩm bồi bổ khí huyết về uống."

Phương Danh Vinh thở phào nhẹ nhõm một hơi, chuyện này dẫu cho con trai không chủ động nói ra thì ông cũng đã chuẩn bị tinh thần đi mua rồi.

Phương Bình lại tiếp tục nói tiếp: "Thế nhưng giá cả lại hơi đắt đỏ một chút ạ. Cậu bạn con bảo với tình trạng của con hiện tại, tốt nhất nên mua lấy một viên Huyết Khí Hoàn về dùng.

Thế nhưng nếu ra ngoài các hiệu thuốc lớn mua thì Huyết Khí Hoàn có giá tận 3 vạn tệ một viên!

Cậu bạn con trước đây cũng từng mua qua rồi, nhưng giá rẻ hơn ở hiệu thuốc rất nhiều. Bố cậu ấy làm kinh doanh buôn bán nên quen biết với một số chủ tiệm thuốc tây, chỉ cần 2 vạn tệ là có thể mua được một viên rồi.

Con đang tính xem liệu có nên nhờ cậu ấy mua hộ cho một viên hay không……"

Phương Danh Vinh hơi nhíu mày lại, không phải vì ông tiếc số tiền này, rốt cuộc con số 2 vạn tệ đã là ít hơn rất nhiều so với những gì ông tưởng tượng trong đầu.

Mấu chốt là chuyện này liệu có đáng tin cậy hay không?

Mấy vạn tệ đối với gia đình họ Phương không phải là một con số nhỏ bé gì, nếu như chẳng may bị người ta lừa gạt mất trắng thì đúng là tai họa khôn lường.

Phương Bình đương nhiên hiểu rõ nỗi lo lắng trăn trở của bố mình, lập tức bồi thêm một liều thuốc an thần: "Nhà cậu ấy giàu có lắm bố ạ, tuyệt đối không có chuyện lừa đảo đâu.

Hơn nữa thành tích của cậu ấy rất xuất sắc, là người chắc chắn sẽ thi vào võ khoa.

Bố nghĩ mà xem, thi võ khoa bắt buộc phải qua khâu thẩm tra chính trị cực kỳ nghiêm ngặt. Nếu như cậu ấy dám lừa tiền của con, con chỉ cần báo cáo việc này lên ban giám hiệu nhà trường là cậu ấy sẽ bị tước bỏ tư cách dự thi ngay lập tức.

Cho nên con nghĩ tới nghĩ lui, chắc chắn cậu ấy không dám lừa con đâu, nếu không thì quá mức ngu xuẩn rồi. Một khi đã thi đỗ vào võ khoa thì đừng nói là 2 vạn tệ, ngay cả 200 vạn tệ đối với người ta cũng chẳng phải là số tiền to tát gì."

Phương Danh Vinh do dự một chút, cuối cùng cắn răng hạ quyết tâm, gật đầu nói: "Được rồi! Vậy ngày mai bố sẽ xin nghỉ làm một buổi để trực tiếp đến tận nhà cậu ấy một chuyến……"

"Bố ơi!"

Phương Bình vội vàng can ngăn: "Người ta bận rộn tối mắt tối mũi ôn thi, có 2 vạn tệ mà bố còn đích thân tìm đến tận cửa, làm như thế khác nào tỏ ý không tin tưởng người ta chứ? Người ta là có lòng tốt muốn giúp đỡ con, chứ đâu phải nghĩa vụ bắt buộc phải giúp.

Cũng là nhờ nhìn thấy kết quả kiểm tra khí huyết hôm nay của con rất tốt nên cậu ấy mới nhiệt tình nhận lời giúp đỡ, chứ bình thường ai rảnh đâu mà đi lo chuyện bao đồng?

Nếu như bố đã đồng ý rồi thì cứ để con tự mình qua nhà nói chuyện với cậu ấy là được rồi. Bố xem như thế có được không ạ?"

Phương Danh Vinh vẫn còn chút ngập ngừng chần chừ, nhưng Lý Ngọc Anh đứng bên cạnh đã gật đầu đồng tình: "Ông nó nói thế là đúng đấy, người ta là nể mặt mũi của thằng Bình nhà mình.

Thấy thằng Bình có hy vọng thi đỗ võ khoa nên người ta mới sẵn lòng ra tay giúp đỡ.

Chứ ông là ai cơ chứ, chỉ là một người công nhân làm thuê quèn, ai thèm nể mặt mà giúp đỡ ông?"

Phương Bình thấy bố vẫn còn im lặng đắn đo, lại bồi thêm một câu: "Cậu bạn đó chính là Ngô Chí Hào ở lớp con đấy, bố có nhớ không?"

"Là thằng bé đó sao?"

Phương Danh Vinh trong nháy mắt nhớ ra ngay!

Ông từng đi họp phụ huynh cho Phương Bình nhiều lần, cũng từng tận mắt nhìn thấy bố của Ngô Chí Hào rồi!

Là học sinh có thành tích xuất sắc nhất lớp, sức ảnh hưởng của cậu ta không chỉ dừng lại ở đám học sinh trong lớp, mà còn lan sang cả các bậc phụ huynh.

Mỗi lần đi họp phụ huynh, thầy chủ nhiệm của Phương Bình tuy không phải là kẻ xu nịnh bợ đỡ gì, nhưng nhìn vào thành tích học tập để đánh giá khen ngợi là chuyện hết sức bình thường ở chốn học đường.

Cứ mỗi lần họp phụ huynh là những câu đại loại như "Em Ngô Chí Hào nhà anh chị học rất giỏi, hy vọng thi đỗ võ khoa là cực kỳ lớn", "Nếu đặt vào thang điểm năm ngoái thì chắc chắn em ấy đã đỗ võ khoa rồi"……

Những lời khen ngợi có cánh như thế Lão Ban đâu phải mới nói một hai lần, Phương Danh Vinh ngồi bên dưới đã được nghe qua không biết bao nhiêu bận.

Hơn nữa bố của Ngô Chí Hào ông cũng từng gặp mặt qua rồi, quả thực phong thái ăn mặc đàng hoàng chỉn chu hơn hẳn những người lao động chân tay như ông. Lúc đi họp phụ huynh người ta còn lái cả một chiếc xe ô tô con bóng loáng tới trường, đâu có giống như ông lạch cạch cưỡi chiếc xe máy điện cũ mèm đi họp.

Đối với một gia đình có con trai cầm chắc tấm vé bước chân vào trường đại học võ khoa như vậy, nếu bảo người ta đi lừa đảo 2 vạn tệ của nhà mình thì đánh chết Phương Danh Vinh cũng không dám tin!

Nếu như là sau kỳ thi đại học, Ngô Chí Hào thi trượt võ khoa thì chuyện này còn khó nói.

Thế nhưng ngay trước thềm kỳ thi đại học quan trọng ngàn năm có một này, đúng như lời Phương Bình vừa phân tích: Một khi sự việc bị xé to chuyện ra, làm ầm ĩ lên thì cho dù Ngô Chí Hào có thi đỗ đi chăng nữa cũng sẽ bị hủy bỏ tư cách trúng tuyển ngay lập tức.

Nghĩ thông suốt điểm này, Phương Danh Vinh lập tức gật đầu dứt khoát: "Được! Chuyện này bố hoàn toàn nhất trí!

Lát nữa bố sẽ bảo mẹ con rút tiền đưa cho con. Nhớ kỹ khi qua nhà bạn phải nói năng cho thật lễ phép khách sáo, hết lời cảm ơn sự giúp đỡ quý báu của người ta đấy nhé.

Bây giờ con chưa thi đỗ võ khoa nên bố mẹ cũng ngại không dám đường đột tới nhà người ta, đợi sau này con thi đỗ rồi, cả nhà chúng mình nhất định phải cùng nhau tới tận nơi cảm ơn, mời gia đình người ta một bữa cơm thịnh soạn!

Mà dẫu cho có thi không đỗ đi chăng nữa thì cái ân tình này con cũng phải khắc cốt ghi tâm……"

Phương Danh Vinh dặn dò tỉ mỉ một hồi lâu. Chuyện này đối với ông mà nói thực sự là một món nợ ân tình vô cùng to lớn.

Tiết kiệm được 1 vạn tệ không phải là một con số nhỏ bé gì đối với một gia đình công nhân.

Tuy nhiên ngày mai đến phân xưởng làm việc, ông vẫn phải lựa lời hỏi dò lại vị chủ nhiệm phân xưởng một lần nữa xem có đúng thực tế như vậy không. Nếu như ngoài hiệu thuốc bán rẻ hơn thì cũng chẳng cần thiết phải đi làm phiền người ta làm gì.

Phương Danh Vinh tuy chỉ là một người công nhân bình thường nhưng cũng không hề ngốc nghếch. Nếu không phải vì tương lai của con trai thì nợ ân tình có thể không vay thì tốt nhất đừng nên vay mượn.

Điều kiện gia đình có hạn, nếu như có thể tiết kiệm được 1 vạn tệ thì số tiền đó có thể dùng để mua thêm nhiều đồ ăn ngon bổ dưỡng về tẩm bổ cho Phương Bình.

Nghĩ tới đây, Phương Danh Vinh lại dặn dò thêm một câu: "Con cứ nói trước với bạn con một tiếng, khi nào người ta lấy được thuốc về thì con mới đưa tiền."

"Vâng ạ, bố cứ yên tâm giao cho con."

Phương Bình vội vàng gật đầu lia lịa, trong lòng thầm nói lời xin lỗi: Lại hố ông già một vố nữa rồi.

Thế nhưng vào lúc này, việc hố cha cũng là chuyện vạn bất đắc dĩ không còn cách nào khác. Nếu hắn không chủ động đứng ra can thiệp thì ông bố nhà mình chắc chắn cũng sẽ điên cuồng chạy vạy mua thuốc bên ngoài, vừa tốn kém tiền của mà hiệu quả mang lại chẳng được bao nhiêu.

Tiền bạc chỉ khi nằm trong tay hắn thì mới có thể phát huy được tác dụng thần kỳ to lớn nhất. Cùng lắm sau khi điểm số tài phú đã được hệ thống ghi nhận xong xuôi, hắn lại tìm cớ mang số tiền đó trả lại cho bố mẹ, chỉ là không biết sau khi trả tiền lại thì điểm tài phú trên hệ thống có bị khấu trừ đi hay không?

Phương Bình cảm thấy khả năng bị khấu trừ là cực kỳ cao, chỉ là không biết nếu như điểm tài phú đó đã được chuyển hóa thành khí huyết rồi thì liệu có bị trừ giật lùi lại hay không mà thôi.

Tóm lại bất kể thế nào đi chăng nữa, hiện tại trong tay hắn càng có nhiều điểm tài phú thì hy vọng thi đỗ võ khoa lại càng tăng thêm một phần chắc chắn.

Chỉ cần thực sự thi đỗ vào võ khoa rồi, thì dẫu cho bố hắn biết rõ mình bị con trai lừa gạt đi chăng nữa e rằng ông cũng sẽ chẳng thèm để bụng đâu, khéo còn mừng rơi nước mắt ấy chứ.

……

Bố mẹ hoàn toàn không mảy may nghi ngờ lời Phương Bình nói. Đợi Phương Bình giải quyết êm xuôi xong chuyện này, lúc quay trở về phòng ngủ thì con nhóc Phương Viên đã sớm đứng khoanh tay chờ sẵn ở đó từ bao giờ, làm ra vẻ mặt như vừa tóm được thóp của hắn mà trừng trừng nhìn Phương Bình.

"Phương Bình kia! Khôn hồn thì thẳng thắn sẽ được khoan hồng, kháng cự là sẽ bị nghiêm trị, mau mau khai thật ra mau!"

Phương Bình đảo trắng mắt, thò tay định véo má cô bé một cái, ai ngờ con nhóc phản ứng cực nhanh, né phắt sang một bên, hừ hừ đắc ý: "Đừng hòng dùng cái chiêu này để đánh trống lảng nhé!

Mau thành thật khai báo cho em, những lời anh vừa nói với bố mẹ ban nãy có phải là sự thật không đấy?"

"Thôi đi cô nương, con nít con nôi bớt lo chuyện bao đồng của người lớn lại đi. Đợi đến khi anh mày thi đỗ vào võ khoa rồi thì em tự khắc sẽ biết là thật hay giả thôi."

Phương Bình cũng lười giải thích dông dài với con bé làm gì, thuận miệng nói bừa một câu cho qua chuyện.

Phương Viên phồng má chu môi, lầm bầm càu nhàu: "Dù sao thì anh cũng không được phép lừa dối bố mẹ đâu đấy, nếu không thì…… nếu không thì…… sau này anh đừng hòng đụng vào má em nữa!"

Phương Bình phì cười thành tiếng, đưa tay xoa xoa mái tóc bù xù của con bé, khẳng định chắc nịch: "Yên tâm đi nhóc con, anh trai em chưa đến mức vì mấy chuyện tào lao mà đi lừa gạt những đồng tiền mồ hôi nước mắt của bố mẹ đâu."

Hiện tại hắn làm tất cả những điều này cũng chỉ vì kỳ thi võ khoa, vì tương lai tươi sáng của cả gia đình. Nếu không phải vì thời gian quá đỗi gấp gáp cấp bách thì hắn cũng chẳng bao giờ đi làm cái trò này."""
    },
    14: {
        "url": "https://www.piaotia.com/html/9/9640/6523768.html",
        "title_vi": "Chương 14: Một Bước Lên Thiên Đường Một Bước Xuống Địa Ngục",
        "content_vi": """Nói hết nước hết cái, Phương Bình rốt cuộc cũng dỗ dành đuổi được con nhóc tì đi về phòng.

Vì chuyện này mà Phương Bình lại phải gánh thêm một đống nợ nần hứa hẹn ngập đầu, đến chính bản thân hắn cũng chẳng thể nhớ nổi rốt cuộc mình đã hứa cho con bé này bao nhiêu bổng lộc lợi ích nữa rồi.

……

Ngày hôm sau, ngày 8 tháng 4.

Phương Bình bỗng nhiên nổi như cồn, ít nhất là nổi đình nổi đám khắp toàn bộ lớp 12 ban 4.

Lúc hắn còn chưa tới lớp thì Ngô Chí Hào đã đến trước một bước.

Ngô Chí Hào vừa đặt chân vào lớp học, hai tên có máu nhiều chuyện buôn dưa lê ngập tràn trong huyết quản là Trương Hạo và Dương Kiến đã vội vã xúm lại hỏi han tình hình tối qua.

Lão Ngô có lẽ trong lòng vẫn chưa nguôi ngoai cảm giác bị chấn động kinh hoàng vào tối ngày hôm qua, thấy hai tên này vừa mở miệng hỏi, Lão Ngô lập tức làm ra vẻ mặt bí hiểm thần bí, ghé sát tai thì thầm: "113 cal!"

Cậu ta không hề nhắc tới con số 108 cal của lần đo thứ hai, trên thực tế lần đo thứ hai do thể lực của Phương Bình đã bị suy giảm nghiêm trọng nên vốn dĩ độ chuẩn xác không thể bằng lần đầu tiên được.

Kết quả là con số "113 cal" vừa thốt ra khỏi miệng, cả lớp học dường như chết lặng trong cơn kinh hãi!

Phương Bình — một trong hai thành viên của tổ hợp "Bình Phàm Nhị Nhân Tổ" — bây giờ không còn bình phàm tầm thường nữa rồi sao?

Mới ngày hôm qua thôi, mọi người ai nấy đều giống hệt như nhau, đều đang điên cuồng vùi đầu phấn đấu vì kỳ thi văn khoa, đến cả thành tích văn hóa của Phương Bình cũng đâu có thuộc hàng xuất sắc nổi trội gì.

Thế mà bây giờ thì sao?

113 cal đấy trời đất ơi!

Những học sinh chỉ thi văn khoa đơn thuần trong lớp có thể không nắm rõ tình hình cụ thể của các thí sinh thi võ khoa khác.

Thế nhưng có một điểm cốt lõi mà ai ai trong lớp cũng đều biết rất rõ:

Năm ngoái Đại học Võ thuật Nam Giang lấy điểm chuẩn khí huyết tối thiểu là 112 cal.

Vậy chẳng phải nói là tiêu chuẩn khí huyết hiện tại của Phương Bình đã thừa sức chạm tới ngưỡng cửa tuyển sinh của Đại học Võ thuật Nam Giang rồi sao?

Tình huống như thế này, làm sao có thể không khiến cả lớp nổ tung cho được?

Gã tương lai râu quai nón Dương Kiến mặt mày xám ngoét tràn đầy tuyệt vọng, lẩm bẩm như kẻ mất hồn: "Không khoa học chút nào cả, tuyệt đối không có chút tính khoa học nào ở đây hết! Nhìn cái thân hình nhỏ thó như que củi của nó, thế quái nào lại có khí huyết cao hơn cả tao được chứ?"

Ngay cả võ giả thì cũng phải tuân theo quy luật khoa học chứ!

Thế nhưng cái thằng Phương Bình này, thực sự là phi khoa học tới mức tột cùng rồi!

Cái tên này, một cú đấm của mình khéo phải đánh bay được tám thằng như nó mới đúng chứ?

Dương Kiến thì ôm đầu gào thét kêu trời kêu đất không khoa học, còn Trương Hạo đứng bên cạnh thì giống như vừa lên cơn động kinh tái phát, cả người run rẩy bần bật kêu gào: "Ông trời không có mắt mà!"

"113 cal cơ đấy!"

"Bố mày đây cày cuốc bấy lâu nay cũng mới chỉ đạt có 108 cal……"

Trương Nam ngồi cách đó không xa nghe thấy vậy liền uể oải buông một câu lạnh tanh: "108 cal là điểm của bà đây, tôi nhớ không lầm thì lần đo trước ông chỉ có 107 cal thôi thì phải……"

Trương Hạo thẹn quá hóa giận gầm lên: "Đó là chuyện của nửa tháng trước rồi! Bây giờ tôi đã vươn lên 108 cal rồi nhé!"

Trương Nam cũng chẳng thèm chấp nhặt, nhàn nhạt nói tiếp: "Được rồi, coi như ông được 108 cal đi, thì Phương Bình người ta cũng vừa mới đo được tận 113 cal mà thôi……"

"Bà……!"

Trương Hạo méo xệch mặt như đưa đám, quay phắt sang trừng mắt nhìn Ngô Chí Hào: "Lão Ngô, cậu mau nói cho tớ biết đi, có phải cậu đang thông đồng nói dối để lừa bọn tớ đúng không?"

Ngô Chí Hào một tay lật mở trang sách, một tay xua xua漫 bất kinh tâm đáp: "Lừa các cậu làm cái quái gì chứ? Dù sao điểm của cậu ta cũng đâu có cao bằng tớ, chẳng ảnh hưởng gì tới hòa bình thế giới của tớ cả."

"Sao cậu lại có thể nói ra những lời vô tâm tàn nhẫn như thế được chứ?" Trương Hạo đau đớn đấm ngực thùm thụp: "Cậu thử nghĩ lại xem, mấy anh em chúng mình sống khổ sở thảm thương đến mức nào cơ chứ.

Vừa phải học văn hóa ở trường, vừa phải cắm đầu đi học thêm ở các lớp phụ đạo võ khoa, ngày nào tan học cũng phải lao đầu đi tập thể lực hùng hục như trâu.

Đồ ăn chiên rán nhiều dầu mỡ không được đụng vào, xiên nướng thơm phức ngoài cổng trường không được bén mảng, nước ngọt có ga một giọt cũng không dám uống, giữa mùa hè nóng nực nung người đến một que kem sữa mát lạnh cũng không có gan mà nếm thử lấy một miếng.

Thế mà cái thằng ranh Phương Bình kia, nó sống vô nhân đạo quá đi mất!

Lão Ngô ơi là Lão Ngô, trong lòng cậu chẳng lẽ không có lấy một chút xíu cảm giác ghen ăn tức ở hay hận thù gì sao?"

Những lời này vừa thốt ra, Ngô Chí Hào cũng không thể nào giữ nổi vẻ bình thản ung dung được nữa.

Học sinh bình thường nhìn vào thì luôn thèm thuồng ngưỡng mộ đám học sinh thi võ khoa như bọn họ, nhưng đâu ai biết rằng trong thâm tâm bọn họ cũng thèm muốn cuộc sống vô lo vô nghĩ của những người bình thường biết bao nhiêu.

Vì để chuẩn bị cho kỳ thi võ khoa, bọn họ đã phải đánh đổi và trả giá bằng biết bao nhiêu mồ hôi nước mắt, thế nhưng sự hy sinh to lớn đó lại chưa chắc đã gặt hái được kết quả như ý nguyện.

Đúng như lời Trương Hạo vừa than vãn: Trong khi người ta được ăn những món ngon lành khoái khẩu thì bọn họ ngày ngày phải nhét vào mồm toàn những thứ thuốc bổ đắng ngắt kinh dị.

Các cậu tưởng thuốc bổ là ngon lành lắm chắc?

Ngày nào cũng phải nuốt, nuốt đến mức muốn nôn mửa ra ngoài, nuốt đến mức mỗi lần đi ngang qua mấy quán thịt xiên nướng ven đường là nước miếng cứ thế ứa ra trào dâng nơi khóe miệng.

Thế nhưng vì để duy trì vóc dáng săn chắc, vì để không xảy ra bất kỳ biến chứng tai nạn nào cho cơ thể, vì kỳ thi võ khoa thiêng liêng, bọn họ chỉ đành nghiến răng nghiến lợi, vừa nuốt nước miếng ừng ực vừa ngậm ngùi đau đớn cất bước quay lưng bước đi.

Bình thường ai nấy đều phải chịu chung số phận cay đắng như vậy thì thôi cũng đành chấp nhận số phận, tất cả là vì tương lai tươi sáng sau này mà thôi.

Thế nhưng cái thằng quỷ Phương Bình kia, dường như chẳng hề kiêng khem bất cứ thứ gì trên đời, ăn uống bừa bãi chẳng màng chay mặn.

Đem người so với người, đúng là làm cho người ta tức đến hộc máu chết đi sống lại mà!

Ngô Chí Hào trong lòng cũng cuộn trào sóng gió, cười khổ nói: "Thì cũng đành chịu chứ biết làm sao bây giờ, ai bảo người ta sinh ra đã có thiên phú dị bẩm trời ban, không phục cũng phải phục thôi."

"Không được!"

Trương Hạo nghiến răng kèn kẹt, hừ hừ đầy vẻ hung hăng: "Cái thằng nhóc này chẳng phải từ trước đến nay chưa từng tập luyện thể thao gì sao?

Chuyện khí huyết trời ban thì không làm gì được, bọn mình đành ngậm bồ hòn làm ngọt vậy.

Thế nhưng tối nay nhất định phải hẹn nó cùng ra nhà thi đấu thể thao của trường để rèn luyện thân thể. Đến lúc đó tìm cớ tỉ thí so tài võ thuật với nó, phải đập cho nó một trận ra bã thì mới có thể xả được cục tức nghẹn ứ ở cổ họng này ra được!"

Trương Hạo bên này đang hoa chân múa tay nghiến răng nghiến lợi nói, thì Ngô Chí Hào ngồi đối diện bỗng nhiên chớp chớp mắt, khóe miệng khẽ giật giật, cười ha hả nói: "Đều là bạn học cùng lớp với nhau cả mà, việc gì phải làm lớn chuyện như thế chứ."

"Không được! Không đập nó một trận thì trong lòng tớ bức bối khó chịu không chịu nổi đâu!"

Ngô Chí Hào làm bộ khuyên can: "Thôi bỏ đi mà, người ta Phương Bình chẳng qua chỉ là khí huyết cao hơn cậu một tí tẹo, thành tích văn hóa tốt hơn cậu một chút xíu, ngoại hình nhìn cũng đẹp trai hơn cậu một chút thôi mà?

Thực sự chẳng có gì đáng để nổi giận lôi đình cả đâu, bạn cùng lớp chúng mình thi đỗ vào võ khoa thì sau này ra đường mặt mũi chúng mình cũng được thơm lây thơm cả họ chứ bộ."

"Lão Ngô! Rốt cuộc cậu đứng về phe nào đấy hả?!" Trương Hạo tức tối quát lên.

Ngô Chí Hào lập tức cúi gằm mặt xuống bàn, mắt dán chặt vào trang sách, đầu cũng không thèm ngẩng lên đáp: "Tớ đang bận ôn bài, tớ chẳng đứng về phe nào cả."

Trương Hạo đang định mở mồm càu nhàu tiếp thì bả vai bỗng nhiên bị một bàn tay vỗ nhẹ một cái, ngay sau đó từ phía sau lưng liền vang lên giọng nói vui vẻ sảng khoái của Phương Bình: "Trương Hạo à, theo tao thấy thì đúng là nên đập cho cái thằng Phương Bình kia một trận tơi bời hoa lá thật đấy, nếu không để cục tức đó nghẹn trong người làm tổn thương thân thể thì không đáng chút nào đâu."

Khóe miệng Trương Hạo giật giật liên hồi, cậu ta cứng đờ người quay đầu lại, cười gượng gạo xua tay lia lịa: "Nói đùa, nói đùa tí thôi mà, làm sao mà có chuyện đó được chứ!

Chúng mình là anh em tốt sống chết có nhau cơ mà, tao nỡ lòng nào làm ra cái trò bạo lực đó chứ hả?"

Miệng thì nói năng ngọt xớt như mía lùi, nhưng trong lòng Trương Hạo lại khóc ròng rã như đưa đám: Xong đời rồi, đừng nói tới chuyện đập người ta, lỡ như sau này cái thằng Phương Bình này thật sự thi đỗ trở thành võ giả thì bản thân mình có bị nó đập cho không còn manh giáp nào không đây trời?

Phương Bình cũng chẳng buồn so đo tính toán làm gì, cười ha ha nói: "Đừng có nghe Ngô Chí Hào chém gió bốc phét, tao làm quái gì đạt được tới 113 cal, cùng lắm thì……"

"Cùng lắm thì cũng chỉ dao động tầm khoảng 115 cal đổ lại chứ gì!"

Trương Hạo đảo trắng mắt một cái, cái thằng ranh con này, rõ ràng là đang cố tình nói móc để xát muối vào vết thương lòng của mình đây mà.

Thở dài một hơi thườn thượt, Trương Hạo lúc này thực sự vô cùng tò mò hỏi nhỏ: "Phương Bình, mày rốt cuộc có bí quyết gì để rèn luyện tăng cường khí huyết nhanh như vậy không, chia sẻ cho anh em tí đi?"

"Nói nhảm, nếu tao mà có cái bí quyết thần thánh đó thì tao đã sớm trở thành võ giả từ tám kiếp trước rồi!" Phương Bình làm sao dám thừa nhận chuyện này, xua tay lia lịa nói: "Nếu trên đời thực sự có bí quyết đó thì ngoài đường võ giả đã chạy đầy đường như nấm sau mưa rồi, đến lượt đám học sinh chúng mình ngồi đây thi thố chắc?"

"Ừ thì cũng đúng." Trương Hạo lại thở dài thườn thượt một lần nữa, giọng điệu ngập tràn oán thán: "Bây giờ trong lớp mình chỉ có Lão Ngô, mày, Dương Kiến, với Lưu Nhược Kỳ là 4 đứa có hy vọng thi đỗ lớn nhất thôi.

Đám chúng tao thì xác suất làm bia đỡ đạn chạy lót đường lên tới chín mươi chín phần trăm rồi!

Trước đây chỉ có ba đứa thôi đã đủ làm bọn tao nghẹt thở rồi, giờ mày lại còn nhảy vào chen chân làm một chân nữa, ông trời ơi ngài mau giáng sét đánh chết con luôn cho rồi đi……"

Ngô Chí Hào nãy giờ giả vờ cắm đầu đọc sách lúc này mới ngẩng đầu lên nói: "Vẫn bấp bênh lắm các cậu ạ. Năm nay mặt bằng chung khí huyết của mọi người đều cao hơn hẳn so với năm ngoái, hiện tại bản thân tớ cũng cảm thấy chẳng có chút nắm chắc nào trong tay cả.

Cứ lấy lớp chúng mình ra làm ví dụ đi, nếu tính thêm cả Phương Bình thì số người đạt từ 110 cal trở lên đã có tới 4 người rồi.

Còn các lớp thường khác, theo như những gì tớ nghe ngóng được, số học sinh đạt trên 110 cal cộng dồn lại với nhau e rằng phải có trên 60 người.

Bên các lớp chọn thì lại càng khủng khiếp hơn nữa, đừng thấy bọn họ ít người mà lầm, số người vượt mốc 110 cal không hề ít đâu, bèo nhất cũng phải tầm 40 người.

Tính sơ sơ ra thì chỉ riêng Trường Số 1 chúng ta thôi, số học sinh có khí huyết vượt qua 110 cal đã ngót nghét 100 người rồi đấy!

Đây mới chỉ là tính riêng trường chúng ta thôi đấy nhé. Các trường cấp ba khác trong thành phố Dương Thành tuy chất lượng không bằng trường mình, nhưng năm nay phong độ của họ cũng rất tốt, cứ cho là gom tất cả các trường khác lại thì số lượng cũng xấp xỉ ngang ngửa với Trường Số 1 chúng mình đi.

Vậy thì tính riêng cả thành phố Dương Thành này thôi, số lượng thí sinh có khí huyết từ 110 cal trở lên đã vượt qua con số 200 người rồi!"

Càng tính toán chi li, sắc mặt Ngô Chí Hào lại càng thêm phần bất đắc dĩ: "Năm ngoái toàn thành phố Dương Thành tổng cộng chỉ thi đỗ có vẻn vẹn 9 sinh viên võ khoa. Năm nay nếu như tỷ lệ trúng tuyển vẫn giữ nguyên như cũ, thì tỷ lệ chọi thấp nhất cũng phải là hai mươi chọi một rồi."

Một bạn học khác trong lớp cũng đăng ký thi võ khoa ngồi ở dãy bàn bên cạnh nghe vậy liền lắc đầu cười khổ: "Chí Hào ơi, cậu đã chạm tới mốc 115 cal rồi, ở các lớp thường bên này hầu như chẳng có mấy ai cao điểm hơn cậu đâu.

Các trường khác cũng tương tự như vậy thôi. Người khác kêu than áp lực lớn thì bọn tớ còn tin, chứ cậu thì lấy đâu ra áp lực cơ chứ."

Ngô Chí Hào tuy rằng chỉ là học sinh của lớp thường, nhưng trị số khí huyết 115 cal của cậu ta quả thực có thể xếp vào hàng ngũ top đầu xuất sắc nhất ở tất cả các lớp thường trong toàn trường.

Nếu như thực sự chiếu theo tỷ lệ của năm ngoái, các lớp thường giành được hai suất thi đỗ thì hy vọng của Ngô Chí Hào là vô cùng rộng mở.

Mọi người vừa trò chuyện rôm rả một hồi, sự chú ý rốt cuộc cũng không còn đổ dồn toàn bộ lên người Phương Bình nữa.

Phương Bình cũng rất lấy làm vui vẻ trước tình thế này, đứng một bên lắng nghe bọn họ bàn tán rôm rả, hắn cũng lượm lặt được không ít tin tức hành lang vô cùng giá trị.

Lứa học sinh lớp 12 năm nay của Dương Thành, số người có khí huyết trên 110 cal đã vượt qua con số 200 người.

Đương nhiên, khí huyết không phải là yếu tố duy nhất quyết định tất cả, kiểu gì cũng sẽ có người bị đánh rớt ở những cửa ải sát hạch phía sau.

Thế nhưng ngay sau khi kỳ khám thể chất kết thúc, các trường đại học võ khoa lớn trên toàn quốc sẽ căn cứ vào số liệu phản hồi thực tế mà công bố công khai một mức điểm sàn khí huyết tối thiểu. Đây không phải là điểm chuẩn tuyển sinh chính thức, mà chỉ là điểm sàn điều kiện để được phép bước chân vào cửa ải thứ ba: Kiểm tra thực tế (Thực trắc) mà thôi.

Các trường đại học làm như vậy cũng là để giúp cho những học sinh không đủ tiêu chuẩn có thể tiết kiệm thời gian, sớm quay trở lại tập trung toàn lực vào việc ôn thi các môn văn hóa, nếu không dây dưa kéo dài về sau chỉ tổ làm lỡ dở thời gian quý báu của các em.

Nói cách khác, những ai có khí huyết không đạt chuẩn thì ngay sau khi cửa ải thứ hai kết thúc là đã bị loại thẳng tay không thương tiếc rồi.

Tiêu chuẩn lọt vào vòng trong của năm nay rất có khả năng sẽ chốt ở mốc 110 cal! Mà đây mới chỉ là điều kiện cần để bước vào cửa ải thứ ba mà thôi đấy nhé, cho dù chỉ có như vậy thì ngay trong lớp 12 ban 4 này cũng đã có một nửa số thí sinh đăng ký thi võ khoa phải ngậm ngùi dừng bước ngoài cuộc chơi.

Trong chốc lát, ngay cả cái tên hay bốc phét mồm loa mép giải như Trương Hạo cũng im bặt không thốt lên lời.

Dùi mài kinh sử khổ luyện ròng rã suốt bao nhiêu năm trời, thế mà ngay cả cửa ải thứ ba cũng không có tư cách bước chân vào, đối với những cô cậu học trò đang tuổi ăn tuổi lớn thì đòn giáng tâm lý này quả thực là quá đỗi nặng nề tàn khốc.

Hàng năm chính vì sự sụp đổ tâm lý thảm hại này mà biết bao nhiêu thí sinh thi võ khoa sau khi bị đánh trượt đã hoàn toàn mất phương hướng, đến mức kỳ thi văn hóa sau đó cũng làm bài tệ hại cùng cực, cuối cùng chỉ có thể ngậm ngùi bước chân vào một trường đại học hạng bét tầm thường, quả đúng là cảnh tượng: Một bước lên thiên đường, một bước rơi xuống địa ngục trần gian.

Bọn họ im lặng ủ rũ, Phương Bình cũng không chen ngang tiếp lời làm gì. Trong lòng hắn âm thầm tính toán: Xem ra cột mốc 110 cal quả thực là không hề an toàn một chút nào cả.

Chỉ tính riêng một góc nhỏ của huyện thành Dương Thành này thôi mà đã có nhiều người vượt chuẩn như vậy rồi, ai mà biết được thông tin của Ngô Chí Hào có chuẩn xác tuyệt đối hay không, ngộ nhỡ con số thực tế còn đông hơn thế nữa, đến cả cửa ải thứ ba mình cũng không lết vào nổi thì đúng là nhục nhã ê chề.

Xem ra, bản thân mình bắt buộc phải nhanh chóng tìm cách nâng cao trị số khí huyết lên mới được.

……

Cùng với việc mọi người dần dần giữ trật tự yên lặng trở lại, các tiết học chính khóa trên lớp cũng bắt đầu diễn ra.

Phương Bình vẫn duy trì thói quen như thường lệ: Lúc thì lôi sách văn hóa ra đọc, lúc thì cắm đầu nghiên cứu tài liệu thi chuyên nghiệp võ khoa, xung quanh cũng chẳng có ai buồn lên tiếng làm phiền hắn, ngoại trừ gã Dương Kiến ở bàn trên và Trương Hạo ở bàn bên thỉnh thoảng lại quay sang lảm nhảm buôn chuyện vài câu.

Còn cậu bạn cùng bàn Trần Phàm có lẽ do phải hứng chịu sự kích thích tâm lý quá lớn nên lúc này lại càng thêm điên cuồng vùi đầu vào giải đề thi. Suốt cả một buổi sáng, ngoại trừ một lần đứng dậy đi vệ sinh ra thì gần như lúc nào cậu ta cũng cắm cúi gập đầu làm bài tập như điên như dại.

Tiết học buổi sáng vừa kết thúc, vốn dĩ Phương Bình đang chuẩn bị rảo bước đi ăn trưa thì lại nhận được thông báo của Ngô Chí Hào bảo hắn cùng lên văn phòng của thầy chủ nhiệm gấp.

Bước ra bên ngoài hành lang lớp học, chỉ có vẻn vẹn 4 người: Ngô Chí Hào, Dương Kiến, cô bạn Lưu Nhược Kỳ ít nói và Phương Bình.

Ngô Chí Hào vừa đi vừa thấp giọng giải thích: "Thầy chủ nhiệm bảo ngày mai Vương học trưởng sẽ về thăm trường chúng ta. Phía nhà trường có bố trí người ra đón tiếp, thầy đang cố gắng hết sức để tranh cho lớp chúng mình một suất đi đón.

Tuy rằng việc đi đón người cũng không đại biểu là sẽ mang lại lợi ích cụ thể gì to tát, thế nhưng tiếp xúc sớm với đàn anh đi trước, vào những lúc ít người qua lại, biết đâu Vương sư huynh lại vui vẻ tiết lộ cho chúng mình vài thông tin hữu ích thì sao.

Các cậu cũng biết đấy, kỳ thi võ khoa của thành phố Dương Thành chúng ta, cửa ải thứ ba thực trắc thông thường đều do mấy trường đại học võ thuật lớn của tỉnh Nam Giang phối hợp cùng Sở Giáo Dục đứng ra đồng tổ chức. Biết đâu Vương sư huynh lại nắm được chút tin tức nội bộ cơ mật nào đó thì sao.

Nội dung thi cử mỗi năm đôi khi lại có sự thay đổi khác biệt……"

Ngô Chí Hào giải thích một hồi dông dài, Phương Bình nghe vậy liền lộ vẻ thắc mắc: "Thế nhưng có đi đón người thì cũng đâu đến lượt mấy đứa lớp thường chúng mình chứ?"

Trường Số 1 có biết bao nhiêu lớp học, lại còn có hẳn hai lớp chọn tập hợp toàn con cưng tinh anh của trường, lớp 12 ban 4 của bọn họ đâu có điểm gì đặc biệt nổi trội hơn người.

Ngô Chí Hào nghe hắn hỏi vậy liền cười ha hả đáp: "Cậu quên mất Lão Ban của chúng mình là ai rồi sao? Thầy chủ nhiệm phòng giáo vụ của trường chính là học trò cưng năm xưa của Lão Ban đấy! Chút chuyện cỏn con này đối với thầy thì có là cái thá gì chứ?"

Nghe cậu ta nhắc tới điểm này, Phương Bình bấy giờ mới bừng tỉnh nhớ lại.

Thầy giáo chủ nhiệm lớp hắn quả thực tuổi tác đã khá cao trong trường. Thầy chủ nhiệm phòng giáo vụ đúng thật là học trò cũ của Lão Ban, nhưng không phải là học trò thời cấp ba, mà là từ hồi Lão Ban còn dạy ở trường cấp hai cơ.

Thầy Lưu An Quốc trước đây từng có nhiều năm công tác giảng dạy ở bậc trung học cơ sở, mãi về sau này mới chuyển công tác lên dạy ở trường cấp ba.

Thế nhưng cũng chính vì lý do đó, tuy rằng thâm niên đứng bục giảng của thầy Lưu rất dài, nhưng xuất phát điểm dạy cấp ba muộn màng khiến cho con đường quan lộ thăng tiến của thầy quả thực không thể nào sánh bằng những giáo viên ngay từ đầu đã cắm rễ dạy ở trường cấp ba được.

Đến cả học trò cũ của thầy bây giờ đều đã leo lên làm chức chủ nhiệm phòng giáo vụ quyền cao chức trọng trong trường rồi, mà thầy Lưu An Quốc đến giờ phút này vẫn chỉ là một giáo viên chủ nhiệm bình thường phụ trách một lớp 12 mà thôi.

Hiểu rõ được ngọn ngành câu chuyện, Phương Bình cũng đã đoán ra được mục đích thầy chủ nhiệm gọi mấy đứa bọn hắn lên văn phòng là để làm gì rồi.

Thế nhưng đưa mắt nhìn quanh mấy người bạn đang đồng hành bên cạnh, trong lòng Phương Bình bất giác dâng lên một cỗ cảm xúc bồi hồi xúc động. Hắn không biết việc mình có tên trong danh sách này là do chuyện tối hôm qua hắn đi đo khí huyết đạt điểm cao đã lọt tới tai Lão Ban, hay là do Lão Ban biết hoàn cảnh gia đình hắn nghèo khó nên cố tình chiếu cố nâng đỡ hắn một tay.

Có lẽ cả hai nguyên nhân đều có, Phương Bình cũng chỉ thầm cảm thán trong lòng một chút mà thôi, ít nhất trong mắt hắn thì người thầy chủ nhiệm già này thực sự là một người thầy vô cùng có tâm và trách nhiệm."""
    },
    15: {
        "url": "https://www.piaotia.com/html/9/9640/6523769.html",
        "title_vi": "Chương 15: Tinh Thần Thăng Tiến",
        "content_vi": """Cái tên Vương Kim Dương này, Phương Bình không phải là lần đầu tiên được nghe nhắc tới.

Vào ngày đầu tiên tỉnh lại ở thế giới này, Dương Kiến đã không ngừng thao thao bất tuyệt kể về anh ta.

Sau đó, Trần Phàm bắt đầu nhắc tới, Ngô Chí Hào bắt đầu nhắc tới, đến cả thầy chủ nhiệm lớp cũng liên tục nhắc tới cái tên này.

Tóm lại, chỉ trong vòng mấy ngày ngắn ngủi, tuy rằng Phương Bình chưa từng một lần được tận mắt nhìn thấy mặt mũi Vương Kim Dương tròn méo ra sao, nhưng nếu nói cái tên này vang dội như sấm bên tai thì tuyệt đối không phải là lời nói ngoa ngoắt phóng đại chút nào.

Một học sinh xuất thân từ lớp thường, thành tích học tập bình thường trên lớp cũng chẳng có gì quá mức xuất chúng nổi trội, thế mà lại có thể đường đường chính chính thi đỗ vào một trường đại học võ khoa danh giá, ở cái huyện thành Dương Thành nhỏ bé này quả thực xứng đáng được xưng tụng là một nhân vật truyền kỳ nổi tiếng.

Danh tiếng lẫy lừng của Vương Kim Dương thậm chí có những thời điểm còn lấn át vượt mặt cả những học sinh ưu tú khác của trường từng thi đỗ vào các trường đại học võ khoa vào năm ngoái.

……

Bước chân ra khỏi văn phòng giáo viên, Phương Bình trong đầu vẫn còn đang suy nghĩ miên man về những lời dặn dò của thầy chủ nhiệm ban nãy.

Lão Ban quả thực đã cố tình dành cho hắn một sự chăm sóc ưu ái đặc biệt ngoại lệ.

Theo như những lời thầy Lưu An Quốc vừa phân tích, những học sinh khác thì không sao, mọi người đều đã trải qua một quãng thời gian dài chuẩn bị ôn thi võ khoa từ trước, những điều gì cần biết thì trong lòng đều đã nắm bắt rõ ràng cả rồi.

Phương Bình thì hoàn toàn khác biệt, quyết định đăng ký dự thi của hắn diễn ra quá mức đường đột và bất ngờ.

Nếu như ngày hôm qua Lưu An Quốc không hề ôm ấp bất kỳ tia hy vọng nào đối với Phương Bình, thì ngày hôm nay, sau khi nghe ngóng được kết quả đo đạc kiểm tra khí huyết vào tối ngày hôm qua, Lưu An Quốc lại cảm thấy thằng nhóc này chưa biết chừng cũng có thể giống như Vương Kim Dương năm xưa, tạo nên một kỳ tích chấn động lòng người.

Trùng hợp thay, hoàn cảnh của Phương Bình và Vương Kim Dương lại có quá nhiều điểm tương đồng đến kỳ lạ.

Bình thường ở trong lớp thành tích đều không thuộc hàng top đầu xuất chúng, gia cảnh đôi bên cũng đều thuộc tầng lớp bình dân lao động nghèo khó. Vương Kim Dương năm xưa báo danh thi võ khoa tuy không quá mức đường đột như Phương Bình, thế nhưng ngay trước thềm kỳ thi đại học diễn ra, căn bản cũng chẳng có một ai dám tin tưởng rằng anh ta lại có thể thi đỗ vào võ khoa cả.

Lưu An Quốc cảm thấy, nếu để Phương Bình đi đón tiếp, nói không chừng giữa hai người sẽ tìm được những tiếng nói chung đồng điệu, biết đâu thằng bé lại có thể gặt hái được những thu hoạch quý báu ngoài dự liệu thì sao.

Chính vì lẽ đó, trong danh sách những người đi đón tiếp đợt này, cái tên Phương Bình đã được đặc cách điền vào.

Bên ngoài hành lang văn phòng, trên gương mặt Ngô Chí Hào ngập tràn niềm vui sướng hớn hở, toe toét cười nói: "Thật không ngờ Lão Ban của chúng mình lại ra tay uy lực dũng mãnh đến thế, lần này thế mà nhà trường lại giao trọn nhiệm vụ đón tiếp cho mỗi lớp chúng mình phụ trách."

Đúng vậy, lần này chỉ có 4 học sinh của lớp 12 ban 4 chịu trách nhiệm đi đón tiếp. Đương nhiên, phía nhà trường cũng chu đáo bố trí riêng một chiếc xe ô tô cùng tài xế đưa đón.

Điều này không phải là do các thầy cô giáo trong trường làm bộ làm tịch giữ kẽ giữ thể diện gì. Trên thực tế, một khi Vương Kim Dương đã bước chân vào đại học võ khoa rồi thì thành tựu và địa vị sau khi tốt nghiệp của anh ta chắc chắn sẽ cao hơn đám giáo viên này gấp bội phần, rất nhiều thầy cô thậm chí còn ước gì được đích thân chạy tới để bắt quàng làm họ làm quen thân thiết nữa kìa.

Thế nhưng trước đó khi Vương Kim Dương trao đổi liên lạc với nhà trường, anh ta đã khéo léo nhắn lại rằng không cần phải làm rùm beng phiền toái quá mức, bản thân anh ta có thể tự mình bắt xe đi thẳng tới trường là được rồi.

Về sau không nỡ từ chối tấm thịnh tình quá đỗi nhiệt tình của ban giám hiệu nhà trường, anh ta bèn dứt khoát bảo chỉ cần cử vài bạn đàn em khóa dưới ra đón là được rồi, không cần thiết phải làm phiền tới quý thầy cô giáo lớn tuổi làm gì.

Mặc dù đây có thể chỉ là những lời nói mang tính chất xã giao khách sáo mà thôi, thế nhưng cuối cùng ban giám hiệu nhà trường vẫn quyết định chỉ bố trí học sinh đi đón tiếp, tránh để xảy ra những tình huống ngượng ngùng khó xử cho cả đôi bên.

Lưu An Quốc lần này cũng là hạ quyết tâm cắn răng dốc hết thể diện của mình ra. Trong lớp có Ngô Chí Hào là người có hy vọng thi đỗ võ khoa cực kỳ lớn, cho nên ban đầu Lưu An Quốc chỉ tính toán tranh cho mỗi Ngô Chí Hào một suất đi tiếp xúc mở rộng tầm mắt mà thôi.

Về sau nghe ngóng được chuyện của Phương Bình, thầy lại nghĩ cách muốn tranh thêm một cơ hội nữa để giúp đỡ Phương Bình một tay.

Nghĩ tới việc cả hai đứa này đều được đi rồi, mà hai đứa còn lại trong lớp là Dương Kiến và Lưu Nhược Kỳ biểu hiện cũng không hề kém cạnh chút nào, chi bằng dứt khoát xin cho cả bọn cùng đi luôn một thể cho xong.

Thế là, sáng sớm tinh mơ Lão Lưu đã hùng hổ kéo tới đứng chặn cứng ngay trước cửa văn phòng của thầy chủ nhiệm phòng giáo vụ, tuyên bố chắc nịch: Nếu không gật đầu đồng ý thì lão già này nhất quyết không chịu rời bước!

Hiện tại hiệu trưởng không có mặt ở trường, rất nhiều công việc đối nội đối ngoại đều do một tay thầy chủ nhiệm phòng giáo vụ đứng ra quán xuyến giải quyết. Bị chính người thầy giáo năm xưa của mình đứng chặn cửa ăn vạ như vậy, trong muôn vàn nỗi bất đắc dĩ, vị chủ nhiệm phòng giáo vụ kia chỉ đành cười khổ gật đầu chấp thuận cho xong chuyện.

Dù sao thì việc này cũng chỉ là đi đón người, coi như một chân chạy vặt phụ việc mà thôi, đám học sinh ưu tú bên các lớp chọn khéo còn lười chẳng buồn đi ấy chứ.

Rốt cuộc xoay đi tính lại, nhiệm vụ đi đón tiếp nhân vật truyền kỳ lại rơi trọn vẹn lên đầu mấy học sinh của lớp 12 ban 4.

Ngô Chí Hào nói xong, lại quay sang dặn dò nhóm người Phương Bình: "Sáng mai các tiết học trên lớp chúng mình được miễn không cần phải học đâu. Tầm trước 9 giờ sáng chúng mình tập trung đông đủ ở cổng trường, sau đó leo lên xe của trường cùng nhau chạy thẳng ra bến xe đón người.

Buổi trưa chuyện ăn uống cơm nước cũng do mấy đứa chúng mình đi cùng hầu hạ Vương sư huynh.

Đến buổi chiều, chúng mình lại cùng tháp tùng Vương sư huynh quay trở lại trường học, như vậy là nhiệm vụ coi như hoàn thành tốt đẹp."

Dương Kiến và Lưu Nhược Kỳ đều gật đầu biểu thị đã rõ, riêng Phương Bình thì lại có chút tò mò cất tiếng hỏi: "Vương sư huynh hiện tại là võ giả mấy phẩm vậy các cậu?"

Câu hỏi bất ngờ này của Phương Bình lập tức khiến Ngô Chí Hào bị hớ nghẹn lời, ngập ngừng hồi lâu mới bất đắc dĩ đáp: "Tớ chịu thôi, các trường đại học võ thuật so với các trường đại học văn khoa bình thường thì bí ẩn hơn rất nhiều, có rất nhiều chuyện cơ mật căn bản không bao giờ truyền ra ngoài cho người ngoài biết đâu.

Vương sư huynh hiện tại là võ giả mấy phẩm bọn mình cũng hoàn toàn mù tịt không rõ.

Thế nhưng Vương sư huynh dù sao cũng mới chỉ là sinh viên năm nhất thôi. Đại học Võ thuật Nam Giang ở trong phạm vi tỉnh Nam Giang chúng mình thì đúng là rất có tiếng tăm, nhưng nếu đem ra so sánh với các trường đại học võ thuật trên toàn quốc thì chỉ có thể xếp vào hàng ngũ bình thường mà thôi.

Cụ thể là mấy phẩm thì tớ đoán chừng chắc cũng chỉ tầm Nhất phẩm hoặc Nhị phẩm đổ lại là cùng thôi."

Cậu ta vừa dứt lời, cô bạn Lưu Nhược Kỳ nãy giờ vẫn im lặng như tượng bỗng nhiên lạnh lùng cất giọng: "Nhất phẩm với Nhị phẩm á? Các cậu chẳng lẽ thật sự ngây thơ nghĩ rằng tất cả sinh viên bước chân vào đại học võ thuật đều là võ giả thực thụ hết chắc?"

Cô nàng chỉ buông lại vẻn vẹn một câu đầy ẩn ý như vậy rồi quay người rảo bước đi thẳng một mạch.

Đợi bóng dáng cô nàng đi khuất, Phương Bình như có điều suy nghĩ lên tiếng: "Nghe khẩu khí của cậu ấy, dường như sinh viên học ở đại học võ thuật chưa chắc ai nấy cũng đều là võ giả sao?"

Ngô Chí Hào cười khổ đáp: "Hình như đúng là thế thật đấy, chi tiết cụ thể ra sao thì tớ cũng không rõ lắm. Hình như tớ từng nghe phong phanh có những sinh viên đại học võ thuật học cho đến tận lúc tốt nghiệp ra trường rồi mà vẫn chưa thể trở thành võ giả thực thụ đâu.

Thế nhưng những chuyện sâu xa đó đối với chúng mình hiện tại còn quá mức xa xôi diệu vợi, tình hình thực hư thế nào chúng mình làm sao nắm rõ được."

Phương Bình khẽ gật đầu đồng tình. Hóa ra cho dù có thi đỗ vào trường đại học võ thuật đi chăng nữa thì cũng chưa chắc một trăm phần trăm sẽ trở thành võ giả thực thụ, thảo nào địa vị của võ giả trong xã hội ngày càng được tôn sùng và kính nể đến như vậy.

Còn về phần Vương Kim Dương rốt cuộc đã là võ giả hay chưa thì lúc này cũng rất khó để đưa ra phán đoán chính xác.

Thế nhưng bất kể thực hư ra sao đi chăng nữa, đây cũng chính là nhân vật đầu tiên thực sự có mối liên hệ mật thiết với giới võ giả mà Phương Bình sắp sửa được tận mắt diện kiến ngoài đời thực.

Bấy lâu nay toàn nghe người ta đồn thổi về những truyền thuyết huyền bí của võ giả, chứ võ giả bằng xương bằng thịt thì trên dưới cả cái Trường Số 1 này cũng chẳng có mấy ai từng được may mắn tiếp xúc qua.

Trong chốc lát, cõi lòng Phương Bình bất giác dâng lên một cỗ cảm giác chờ mong háo hức khôn nguôi.

……

Buổi trưa sau khi ăn xong bữa cơm, cộng thêm việc mang tập vở ghi chép của Ngô Chí Hào đi ra tiệm photo copy lại một bản, loay hoay giải quyết xong xuôi hết những thứ này thì số tiền 50 tệ trong túi Phương Bình lại một lần nữa cạn kiệt sạch sành sanh.

Trong tay không có đồng bạc nào lận lưng nên hắn cũng chẳng dám mở mồm ra mời Ngô Chí Hào đi ăn một bữa cơm ra trò.

Đương nhiên bản thân Ngô Chí Hào cũng chẳng mấy để tâm tới chuyện cỏn con này, thế nhưng món ân tình này thì Phương Bình đã âm thầm khắc ghi sâu sắc vào trong lòng.

Mới trùng sinh quay trở về có vài ngày ngắn ngủi thôi mà nợ ân tình đã gánh trên vai không ít rồi: Nợ của thầy chủ nhiệm, nợ của Ngô Chí Hào.

Có những thời điểm, nợ ân tình khó trả hơn nợ tiền bạc gấp bội phần.

Tạm thời gác lại những suy nghĩ vẩn vơ này sang một bên, buổi chiều Phương Bình lại tiếp tục tự mình vùi đầu vào đọc sách ôn tập bài vở.

……

Buổi tối.

Lúc Phương Bình rảo bước trở về tới nhà thì cô em gái và mẹ đều đã có mặt ở nhà, riêng bố Phương Danh Vinh thì vẫn chưa tan ca về tới.

Theo thói quen thường lệ, mỗi lần bước chân vào cửa mà không đưa tay nhéo nhéo cái má tròn vo của Phương Viên thì Phương Bình cứ cảm thấy bứt rứt không quen tay thế nào ấy.

Kết quả là hai anh em lại bắt đầu lao vào đuổi bắt trêu đùa ầm ĩ cả gian nhà lên. Lý Ngọc Anh đang lúi húi chuẩn bị bữa tối ở trong bếp nhìn thấy cảnh tượng đó chỉ biết dở khóc dở cười lắc đầu ngao ngán: Hai đứa con này cứ hễ ở cạnh nhau là chẳng bao giờ chịu ngồi yên tĩnh lấy một giây một phút nào cả.

Hai anh em đùa nghịch đến mức mệt lử cả người thì Phương Danh Vinh cũng vừa vặn đẩy cửa bước chân vào nhà.

Vừa bước qua ngưỡng cửa, Phương Danh Vinh liền cất tiếng hỏi ngay: "Bà nó đã ra ngân hàng rút tiền về chưa đấy?"

Lý Ngọc Anh gật đầu xác nhận. Phương Danh Vinh lập tức quay sang nhìn Phương Bình, trầm giọng dặn dò: "Lát nữa bảo mẹ con đưa cho con 2 vạn tệ tiền mặt. Nhớ kỹ khi nhận thuốc phải hết lời cảm ơn cậu bạn học đó, và gửi lời cảm ơn chân thành tới cả phụ huynh của người ta nữa đấy nhé.

Lần này bố bận việc nên không tiện trực tiếp tới nhà người ta, đợi sau khi kỳ thi đại học kết thúc, cả nhà chúng mình nhất định phải mời gia đình người ta một bữa cơm thịnh soạn mới được."

Hôm nay Phương Danh Vinh tới phân xưởng làm việc cũng đã tranh thủ lựa lời hỏi dò vị chủ nhiệm phân xưởng một phen.

Huyết Khí Hoàn quả thực ngoài các hiệu thuốc lớn đều niêm yết giá chuẩn 3 vạn tệ một viên, hơn nữa hiệu thuốc kiên quyết không bớt lấy một xu cắc nào.

Đợi đến khi Phương Danh Vinh ngập ngừng hỏi xem liệu có thể tìm cách mua với giá 2 vạn tệ được hay không, thì suýt chút nữa đã bị nước bọt của ông chủ nhiệm phân xưởng phun cho ướt sũng cả mặt.

Mua thì đúng là có thể mua được thật, chuyện này trong giới cũng chẳng phải là bí mật gì to tát, thế nhưng cái thân phận của một người công nhân quèn như Phương Danh Vinh thì tính là cái thá gì chứ?

Đến ngay cả bản thân vị chủ nhiệm phân xưởng này năm ngoái lúc lo thuốc thang cho con trai ôn thi đại học, muốn tìm mối mua thuốc giá rẻ mà còn đỏ mắt tìm không ra cửa nẻo quan hệ, huống chi là một gã công nhân quèn như Phương Danh Vinh.

Lần này thì Phương Danh Vinh đã hoàn toàn dập tắt sạch sành sanh mọi ý định không muốn nợ ân tình người khác rồi.

Vào thời điểm hiện tại, kinh tế gia đình quả thực không mấy dư dả gì. Phương Bình cho dù sau này có may mắn thi đỗ trở thành võ giả đi chăng nữa thì tương lai cũng sẽ phải tiêu tốn một lượng tiền bạc khổng lồ, mà nếu như thi trượt thì lại càng phải thắt lưng buộc bụng tiết kiệm từng đồng từng cắc hơn.

1 vạn tệ đối với gia đình này không phải là một con số nhỏ bé, có thể tiết kiệm được đồng nào thì hay đồng nấy, món nợ ân tình này thôi thì đành cắn răng mà nợ vậy.

Thấy ông bố đã gật đầu đồng ý dứt khoát, tảng đá đè nặng trong lòng Phương Bình rốt cuộc cũng được trút bỏ, nhẹ nhõm đi rất nhiều.

Có tiền trong tay rồi thì có rất nhiều việc đại sự sẽ dễ dàng xoay xở giải quyết hơn gấp bội phần.

Mấy ngày nay hắn cũng bận rộn tối mắt tối mũi với bài vở và thông tin thi cử, dẫu cho trong đầu có nảy ra ý tưởng muốn kiếm tiền đi chăng nữa thì cũng hoàn toàn không có đủ thời gian và sức lực để mà triển khai thực hiện.

Vì để đảm bảo chắc chắn có thể thi đỗ vào võ khoa, tạm thời nghĩ cách xoay xở một ít tiền từ chỗ bố mẹ cũng là một hạ sách vạn bất đắc dĩ mà thôi.

Cả gia đình quây quần ăn xong bữa cơm tối, Lý Ngọc Anh liền bước vào phòng ngủ lấy tiền mang ra cho Phương Bình.

Khoảnh khắc cọc tiền 2 vạn tệ dày cộp được đặt gọn gàng vào trong lòng bàn tay Phương Bình, trước mắt hắn bỗng nhiên hoa lên một cái, bảng số liệu quen thuộc lại một lần nữa hiện rõ mồn một trong tầm mắt:

Tài phú: 20000

Khí huyết: 1.1

Tinh thần: 1

Phương Bình thở phào ra một hơi thật dài. Quả nhiên những suy đoán trước đó của hắn hoàn toàn chính xác: Chỉ có những đồng tiền do bố mẹ cho hắn toàn quyền sở hữu, hoặc tiền do chính bản thân hắn làm chủ thì mới có thể được hệ thống chuyển hóa thành điểm số tài phú.

Ngoài ra Phương Bình cũng không nhịn được mà tự giễu cười thầm trong bụng: Bản thân mình bây giờ dường như còn lợi hại và chuẩn xác hơn cả chiếc máy soi tiền giả chuyên dụng nữa kìa.

Tiền bị thiếu hụt đồng nào, hay lẫn lộn tờ tiền giả nào vào trong cọc tiền, hắn chỉ cần liếc mắt nhìn qua bảng số liệu một cái là biết ngay lập tức, căn bản không cần phải tốn công ngồi đếm từng tờ một làm gì cho mệt.

Nếu như cái khả năng này không chỉ giới hạn ở tiền của chính mình, thì sau này lỡ như có thi trượt võ khoa, không thể trở thành võ giả được thì chạy đi xin làm nhân viên giao dịch đếm tiền ở ngân hàng khéo cũng giật giải quán quân toàn quốc ấy chứ chẳng đùa.

Gạt phăng mớ suy nghĩ lung tung rối rắm này sang một bên, Phương Bình cất tiếng chào bố mẹ một câu rồi tự nhốt mình vào trong căn phòng nhỏ riêng tư của mình.

……

Bên trong phòng ngủ.

Chăm chú nhìn vào bảng điều khiển trong tầm mắt, Phương Bình hơi có chút do dự đắn đo: Rốt cuộc nên ưu tiên nâng cấp khí huyết trước hay là nâng cấp tinh thần trước đây?

Tác dụng to lớn của khí huyết thì hiện tại hắn đã được thể nghiệm rõ ràng rồi.

Thế nhưng việc nâng cao lực lượng tinh thần rốt cuộc sẽ mang lại những chuyển biến kỳ diệu gì?

Liệu nó có thực sự giống như những gì hắn hằng suy đoán: Có thể giúp gia tăng vượt bậc trí nhớ và khả năng lý giải tiếp thu kiến thức hay không?

Tuy rằng trong lòng chưa dám khẳng định chắc chắn một trăm phần trăm, nhưng rất nhanh sau đó Phương Bình đã hạ quyết tâm: Cứ thử nâng cấp tinh thần một lần xem sao đã!

Dù sao hiện tại trong tay hắn cũng đang có sẵn tới 20.000 điểm tài phú. Nếu như việc tăng điểm tinh thần không mang lại hiệu quả như ý muốn, thì 10.000 điểm tài phú còn lại hắn vẫn hoàn toàn có thể dùng để đập vào nâng cấp khí huyết như thường.

Trị số khí huyết hiện tại thực ra cũng không cần thiết phải đẩy lên quá cao làm gì. Hiện giờ người mạnh nhất của toàn bộ Trường Số 1 cũng mới chỉ nhỉnh hơn 120 cal một chút thôi, nếu như một kẻ xuất thân từ lớp thường như Phương Bình bỗng nhiên vọt thẳng lên trên 130 cal thì chưa chắc đã là một chuyện tốt lành, khéo lại rước họa vào thân vì bị người ta nghi ngờ soi mói.

Sau khi đã thông suốt mọi chuyện trong đầu, Phương Bình liền căn cứ theo kinh nghiệm thành công của lần trước, khẽ lẩm bẩm trong miệng: "Cộng thêm chút tinh thần đi, không cộng tao đánh chết mày bây giờ!"

"……"

Dãy số liệu trên bảng điều khiển vẫn trơ trơ bất động như tượng đá, trong chốc lát khiến cho Phương Bình cảm thấy vô cùng ngượng ngùng và lúng túng.

Cái thứ quỷ này rốt cuộc có linh nghiệm hay không vậy trời, lần trước chẳng phải đe dọa như thế là được rồi sao?

Thử đi thử lại hết lần này đến lần khác, cuối cùng Phương Bình mới vỡ lẽ hiểu ra: Việc tăng điểm căn bản chẳng liên quan quái gì tới mấy câu thần chú xàm xí khẩu xà tâm phật của hắn cả! Chỉ cần bản thân hắn tập trung cao độ tinh thần, trong đầu toàn tâm toàn ý nghĩ về việc tăng điểm thì con số trên hệ thống sẽ tự khắc chuyển biến theo ý niệm của hắn.

Lãng phí mất không ít thời gian mày mò, Phương Bình rốt cuộc cũng thực hiện xong việc thăng cấp cho lực lượng tinh thần của mình.

Rất nhanh sau đó, dãy số liệu hiển thị trước mắt hắn đột ngột xuất hiện sự biến đổi rõ rệt:

Tài phú: 10000

Khí huyết: 1.1

Tinh thần: 1.1

……

Ngay tại khoảnh khắc lực lượng tinh thần được thăng cấp, Phương Bình bỗng nhiên cảm nhận được sâu trong não bộ truyền đến một luồng khí tức mát lạnh sảng khoái đến tột cùng!

Cảm giác đó giống hệt như có một bàn tay mềm mại thon thả của một thiếu nữ đang dịu dàng xoa bóp vuốt ve từng nếp nhăn trên vỏ não của hắn vậy, thoải mái và sung sướng đến mức khó tả bằng lời.

"Phù……"

Một hồi lâu sau, Phương Bình mới từ từ bừng tỉnh mở mắt ra, thở hắt ra một ngụm trọc khí dài thườn thượt. Hắn chỉ cảm thấy đầu óc tỉnh táo minh mẫn lạ thường, mọi nỗi mệt mỏi căng thẳng tích tụ suốt cả một ngày dài học tập dường như đã tan biến sạch sành sanh không còn sót lại một chút dấu vết nào.

Hắn không vội vàng nâng cấp nốt số điểm khí huyết còn lại, mà vội vã chộp lấy cuốn sách giáo khoa trên bàn, bắt đầu lật từng trang ra đọc ngấu nghiến.

……

Hơn mười phút sau, Phương Bình khép cuốn sách giáo khoa lại, nhắm mắt hồi tưởng lại toàn bộ những nội dung kiến thức mình vừa mới đọc qua, kế đó hai hàng lông mày lại hơi nhíu chặt lại.

Không hề xuất hiện năng lực "quá mục bất vong" (đọc qua một lần là nhớ mãi không quên) thần thánh như trong các cuốn tiểu thuyết mạng thường hay miêu tả. Thế nhưng hiệu quả tích cực mang lại quả thực là có: Trí nhớ của hắn dường như quả thật đã mạnh mẽ và chuẩn xác hơn so với trước kia một chút, chỉ có điều hiệu quả chuyển biến chưa đến mức quá mức rõ rệt kinh thiên động địa mà thôi.

Phương Bình không rõ đây là do bản thân mình đang tự huyễn hoặc an ủi tâm lý, hay sự thật quả đúng là như vậy.

Thế nhưng hắn phỏng đoán, nguyên nhân rất có thể là do mức độ thăng tiến của lực lượng tinh thần lần này vẫn còn quá ít ỏi.

Nó cũng giống hệt như sự thăng tiến của khí huyết vậy: Khí huyết của hắn tuy rằng đã chạm tới mốc 110 cal, thế nhưng Phương Bình đâu có lập tức biến thành siêu nhân mình đồng da sắt, thậm chí nếu bây giờ bảo hắn một mình solo tay đôi với gã Dương Kiến hộ pháp kia thì một trăm phần trăm hắn sẽ bị đối phương đấm cho tơi bời hoa lá không tìm thấy đường về nhà.

Khí huyết và tinh thần thực chất chỉ là một dạng cải tạo và nâng cấp nền tảng thể chất cho cơ thể mà thôi, muốn biến nó thành sức chiến đấu thực thụ thì vẫn cần phải trải qua quá trình rèn luyện, vận dụng và thích nghi của chính bản thân mình.

Đại khái nghĩ thông suốt được những tầng đạo lý này rồi, Phương Bình ngược lại không còn cảm thấy nôn nóng hay sốt ruột nữa.

Chỉ cần thứ này có tác dụng thực tế là tốt rồi. Kế tiếp cứ việc nghĩ cách kiếm thật nhiều tiền, đẩy hai chỉ số quan trọng này lên thật cao. Tăng thêm 0.1 điểm hiệu quả chưa rõ rệt, vậy nếu như tăng gấp đôi, gấp ba lên thì sao?

Nghĩ tới việc sáng sớm ngày mai còn phải đi làm nhiệm vụ đón tiếp đàn anh Vương Kim Dương, Phương Bình không dám thức khuya thêm nữa. Hắn bước chân ra ngoài rửa mặt đánh răng sạch sẽ, rồi nhanh chóng trèo lên giường đánh một giấc ngủ say sưa ngon lành."""
    }
}

def main():
    conn = sqlite3.connect("data/novels.db")
    cur = conn.cursor()
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    total_vi_chars = 0
    total_raw_chars = 0
    
    print("=" * 60)
    print("BẮT ĐẦU CẬP NHẬT PHƯƠNG ÁN B - BATCH 3 (CHƯƠNG 11 - 15)")
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
    print(f"HOÀN TẤT BATCH 3! Tổng raw: {total_raw_chars:,} ký tự | Tổng dịch: {total_vi_chars:,} ký tự")
    print("=" * 60)

if __name__ == "__main__":
    main()
