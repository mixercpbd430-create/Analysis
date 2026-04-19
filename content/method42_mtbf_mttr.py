method = {
    "id": 42,
    "title": "MTBF/MTTR Analysis - Phân tích độ tin cậy thiết bị",
    "short_name": "MTBF/MTTR",
    "icon": "⏱️",
    "pillar": "Planned Maintenance",
    "description": "Đo lường Thời gian trung bình giữa các lần hỏng (MTBF) và Thời gian sửa chữa trung bình (MTTR) — 2 chỉ số NỀN TẢNG của bảo trì.",
    "meaning": """
<p><strong>MTBF</strong> và <strong>MTTR</strong> là 2 chỉ số NỀN TẢNG đo lường sức khỏe thiết bị:</p>
<ul>
    <li><strong>MTBF (Mean Time Between Failures — Thời gian trung bình giữa các lần hỏng)</strong>: Máy chạy được BAO LÂU trước khi hỏng? → MTBF CAO = Máy TIN CẬY!</li>
    <li><strong>MTTR (Mean Time To Repair — Thời gian trung bình để sửa chữa)</strong>: Khi hỏng, sửa MẤT BAO LÂU? → MTTR THẤP = Bảo trì HIỆU QUẢ!</li>
</ul>
<div class="note-box note-box--info">
    <div class="note-title">📌 Công thức và ý nghĩa</div>
    <p><strong>MTBF = Tổng thời gian vận hành ÷ Số lần hỏng</strong><br>
    → Ví dụ: Máy chạy 7,200 giờ/năm, hỏng 24 lần → MTBF = 300 giờ (mỗi 12.5 ngày hỏng 1 lần!)<br><br>
    <strong>MTTR = Tổng thời gian sửa chữa ÷ Số lần hỏng</strong><br>
    → Ví dụ: Tổng sửa 480 giờ, hỏng 24 lần → MTTR = 20 giờ/lần (mỗi lần sửa GẦN 1 NGÀY!)<br><br>
    <strong>Availability (Khả dụng) = MTBF ÷ (MTBF + MTTR) × 100%</strong><br>
    → Ví dụ: 300 ÷ (300 + 20) = 93.8% → MỤC TIÊU > 95%!<br><br>
    <strong>Failure Rate (Tỷ lệ hỏng) λ = 1 ÷ MTBF</strong><br>
    → Ví dụ: 1/300 = 0.0033/giờ → Cứ mỗi giờ chạy có 0.33% xác suất hỏng<br><br>
    <em>MỤC TIÊU BT: TĂNG MTBF (máy chạy lâu hơn trước khi hỏng) + GIẢM MTTR (khi hỏng thì sửa nhanh hơn) → Availability TĂNG!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Đo lường RELIABILITY (độ tin cậy) thiết bị bằng MTBF — máy nào hỏng nhiều nhất? máy nào tin cậy nhất?</li>
    <li>Đo lường MAINTAINABILITY (hiệu quả bảo trì) bằng MTTR — sửa máy nào tốn thời gian nhất? tại sao?</li>
    <li>Tính chính xác AVAILABILITY (khả dụng) — máy sẵn sàng bao nhiêu % thời gian?</li>
    <li>So sánh PERFORMANCE giữa các máy, giữa các dây chuyền, giữa các nhà máy — ai tốt hơn ai?</li>
    <li>Theo dõi TREND cải tiến theo thời gian — MTBF tăng = cải tiến hiệu quả! MTBF giảm = đang xấu đi!</li>
    <li>Hỗ trợ lập kế hoạch: PM interval, số lượng phụ tùng tồn kho, nhân lực BT</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Thu thập dữ liệu hỏng hóc (CHÍNH XÁC!)</div>
        <div class="step-card__desc">Ghi nhận MỖI LẦN breakdown: Thời gian bắt đầu hỏng + Thời gian sửa xong + Nguyên nhân + Bộ phận hỏng + Ai sửa. Cần TỐI THIỂU 6-12 tháng dữ liệu (càng nhiều càng chính xác). QUAN TRỌNG: Phân biệt breakdown (hỏng ngoài KH — unplanned) vs PM (bảo trì KH — planned). Chỉ tính breakdown vào MTBF/MTTR!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Tính MTBF và MTTR — theo MÁY, BỘ PHẬN, LOẠI HỎNG</div>
        <div class="step-card__desc">MTBF = Tổng giờ vận hành ÷ Số lần hỏng. MTTR = Tổng giờ sửa ÷ Số lần hỏng. Tính theo NHIỀU CẤP ĐỘ: Theo từng máy (Pellet Mill #1, #2...), theo bộ phận (bạc đạn, motor, die...), theo loại hỏng (điện, cơ, khí nén...). → Bộ phận nào có MTBF THẤP NHẤT = NƠI CẦN CẢI TIẾN!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Phân tích xu hướng và benchmark</div>
        <div class="step-card__desc">Vẽ trend MTBF/MTTR theo tháng: MTBF TĂNG = reliability CẢI THIỆN. MTBF GIẢM 3 tháng liên tiếp = CẢNH BÁO! Hành động NGAY! MTTR GIẢM = bảo trì hiệu quả hơn. So sánh: Máy cùng loại, với spec OEM (nhà sản xuất), với benchmark ngành. Dùng Bathtub Curve (đường cong bồn tắm) để biết máy đang ở giai đoạn nào: Infant mortality (mới) → Useful life (ổn định) → Wear-out (mòn).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Cải tiến TĂNG MTBF + GIẢM MTTR</div>
        <div class="step-card__desc"><strong>TĂNG MTBF (máy chạy lâu hơn)</strong>: Root cause analysis cho top failures → Cải tiến PM, Design change (nâng cấp vật liệu), điều kiện vận hành tốt hơn (AM — vệ sinh, bôi trơn, siết ốc). <strong>GIẢM MTTR (sửa nhanh hơn)</strong>: Phụ tùng sẵn sàng (critical spare tại máy), đào tạo KTV (skill up), SOP sửa chữa chuẩn (standard repair procedure), công cụ chẩn đoán (diagnostic tools, tablet troubleshooting guide).</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "MTBF/MTTR Pellet Mill — Breakdown mỗi 12 ngày, sửa gần 1 ngày!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Pellet Mill #1: 7,200 giờ vận hành/năm (3 ca × 365 ngày × không kể ngày dừng). 24 lần breakdown, tổng 480 giờ sửa chữa. Ban Giám đốc hỏi: \"Máy hỏng bao nhiêu lần? Sửa bao lâu? Cải thiện thế nào?\"",
            "analysis": "Tính toán:\n• MTBF = 7,200 ÷ 24 = 300 giờ → Cứ mỗi 300 giờ chạy (= 12.5 ngày) lại hỏng 1 lần → QUÁ THẤP!\n• MTTR = 480 ÷ 24 = 20 giờ/lần → Mỗi lần sửa gần 1 ngày → QUÁ LÂU!\n• Availability = 300 ÷ (300+20) = 93.8% → Mục tiêu > 97%!\n\nPhân tích chi tiết TOP failures:\n• Die nứt: 8 lần/năm, MTTR = 30 giờ/lần (phải tháo die nặng, thay, căn chỉnh gap)\n• Bạc đạn chính: 6 lần, MTTR = 24 giờ/lần (tháo lắp phức tạp, chờ phụ tùng)\n• Motor trip: 5 lần, MTTR = 8 giờ/lần (overload, overheating)\n• Feeder screw: 5 lần, MTTR = 4 giờ/lần (mòn, thay nhanh)",
            "result": "Kế hoạch cải tiến:\n\nTĂNG MTBF (từ 300 → mục tiêu 600 giờ):\n• Die: Theo dõi tuổi thọ die + CBM rung → thay TRƯỚC KHI nứt → MTBF die tăng 250 → 500 giờ\n• Bạc đạn: CBM (rung + nhiệt) → phát hiện sớm 2 tuần trước hỏng\n• Motor: Đo insulation test hàng quý → phát hiện suy giảm cách điện\n\nGIẢM MTTR (từ 20 → mục tiêu 12 giờ):\n• Bạc đạn: Phát hiện bằng CBM → chuẩn bị phụ tùng + kế hoạch trước → MTTR: 24 → 12 giờ\n• Die: SOP thay die có hình ảnh → KTV mới cũng làm nhanh\n\nTarget: Availability = 600 ÷ (600+12) = 98%!"
        },
        {
            "title": "MTBF trend Boiler giảm 3 năm liên tục — Bathtub Curve!",
            "industry": "Sản xuất chung",
            "situation": "Boiler MTBF 3 năm: 2022 = 720h, 2023 = 480h, 2024 = 350h. DECLINING (giảm liên tục)! Tại sao?",
            "analysis": "MTBF giảm liên tục = RELIABILITY ĐANG XẤU ĐI!\n\nPhân tích theo Bathtub Curve (đường cong bồn tắm — mô hình tuổi thọ thiết bị):\n• Giai đoạn 1 — Infant mortality (mới): MTBF thấp (hỏng vặt do lắp đặt, chạy thử) → MTBF tăng dần\n• Giai đoạn 2 — Useful life (ổn định): MTBF ổn định, hỏng ngẫu nhiên → Giai đoạn tốt nhất!\n• Giai đoạn 3 — Wear-out (mòn): MTBF GIẢM DẦN → các bộ phận MÒN, cũ, hết tuổi thọ\n\nBoiler 15 năm tuổi → ĐANG VÀO GIAI ĐOẠN WEAR-OUT!\nTop failures thay đổi: 2022 (bảng điều khiển) → 2023 (rò ống + bảng ĐK) → 2024 (RÒ ỐNG CHIẾM ĐA SỐ + vật liệu chịu lửa bong) → Xu hướng: Bộ phận cơ khí/áp lực đang mòn!",
            "result": "Hành động cho giai đoạn WEAR-OUT:\n• Đo độ dày ống lò (tube thickness monitoring): Xác định remaining life (tuổi thọ còn lại) → ống nào mỏng → thay trước\n• Kế hoạch sửa chữa lớn (major overhaul): Budget 2025 cho relining refractory (thay lại vật liệu chịu lửa)\n• CBA (method 37): Nếu MTBF tiếp tục giảm xuống Bài học: MTBF trend cho biết máy đang ở ĐÂU trên Bathtub Curve → nếu ở wear-out → chuẩn bị budget overhaul hoặc thay mới!"
        },
        {
            "title": "Phân tích MTTR chi tiết — 27% thời gian sửa = CHỜ PHỤ TÙNG!",
            "industry": "Sản xuất chung",
            "situation": "MTTR trung bình = 4 giờ/lần. Ban giám đốc nói: \"Giảm MTTR xuống 2 giờ!\". Nhưng giảm BƯỚC NÀO? Cần phân tích chi tiết!",
            "analysis": "Phân tích thành phần MTTR (breakdown MTTR thành từng bước):\n\n| Bước | Thời gian | % |\n| Detection (phát hiện hỏng) | 15 phút | 7% |\n| Notification (thông báo BT) | 10 phút | 5% |\n| Response (KTV đến nơi) | 30 phút | 14% |\n| Diagnosis (chẩn đoán nguyên nhân) | 45 phút | 20% |\n| Wait for parts (CHỜ PHỤ TÙNG) | 60 phút | 27%! |\n| Actual repair (sửa chữa thực tế) | 45 phút | 20% |\n| Test & restart (kiểm tra + khởi động) | 15 phút | 7% |\n→ Tổng: 220 phút = 3.7 giờ\n\n→ Chờ phụ tùng = 27% tổng MTTR! Đây là gap LỚN NHẤT — không phải do KTV sửa chậm!",
            "result": "Giảm MTTR từ 4 giờ xuống 2 giờ:\n\n• Chờ phụ tùng 60' → 10': Đặt critical spare ngay TẠI MÁY (kanban box) → KTV không cần chạy về kho → tiết kiệm 50 phút!\n• Response 30' → 15': Phân vùng KTV (zone-based) → KTV chịu trách nhiệm MÁY GẦN mình → không cần chạy xa\n• Diagnosis 45' → 25': Troubleshooting guide trên TABLET → KTV mới cũng chẩn đoán nhanh bằng KTV giỏi\n\nKết quả: MTTR: 4 giờ → 2 giờ!\n→ Bài học: MTTR không chỉ là \"KTV sửa nhanh hay chậm\" — phần lớn MTTR là CHỜM ĐỢI (chờ phụ tùng, chờ KTV, chờ chẩn đoán)! Cải tiến logistics BT = giảm MTTR nhiều nhất!"
        },
        {
            "title": "MTBF theo bộ phận — Tìm 'mắt xích yếu nhất'!",
            "industry": "Sản xuất chung",
            "situation": "Dây chuyền 5 máy nối tiếp (series). MTBF mỗi máy: A=500h, B=800h, C=300h, D=1000h, E=600h. MTBF dây chuyền là bao nhiêu?",
            "analysis": "Hệ thống NỐI TIẾP (Series): 1 máy hỏng = TOÀN BỘ dây chuyền dừng!\n\nMTBF hệ thống = 1 ÷ (1/500 + 1/800 + 1/300 + 1/1000 + 1/600)\n= 1 ÷ (0.002 + 0.00125 + 0.00333 + 0.001 + 0.00167)\n= 1 ÷ 0.00825 = 121 giờ!\n\n→ Mặc dù mỗi máy riêng lẻ MTBF 300-1000h, nhưng DÂY CHUYỀN chỉ 121h! Vì bất kỳ máy nào hỏng → cả dây chuyền dừng!\n\n→ Máy C (MTBF = 300h) là MẮT XÍCH YẾU NHẤT! Chiếm tỷ lệ hỏng cao nhất (0.00333 ÷ 0.00825 = 40% tổng hỏng dây chuyền!)",
            "result": "Chiến lược cải tiến:\n• Tập trung vào Máy C: Root cause analysis → PM improvement → Mục tiêu: MTBF từ 300 → 600h\n• Nếu C đạt 600h → MTBF hệ thống = 1/(1/500+1/800+1/600+1/1000+1/600) = 151h (+25%!)\n• Lắp buffer (bộ đệm) giữa C và D: Khi C dừng → D vẫn chạy từ buffer → decouple (tách rời) sự phụ thuộc\n\nMục tiêu: System MTBF > 200h\n\n→ Bài học: Cải tiến MTBF máy YẾU NHẤT = cải tiến dây chuyền NHIỀU NHẤT! (Không cần cải tiến máy đã tốt!)"
        },
        {
            "title": "KTV giỏi sửa 1.5 giờ, KTV mới sửa 6 giờ — Chuẩn hóa MTTR!",
            "industry": "Sản xuất chung",
            "situation": "MTTR cùng loại sửa chữa nhưng CHÊNH LỆCH LỚN: KTV kinh nghiệm = 1.5 giờ, KTV trung bình = 3 giờ, KTV mới = 6 giờ. Tại sao?",
            "analysis": "Phân tích nguyên nhân chênh lệch MTTR giữa các KTV:\n\n• Không có SOP sửa chữa chuẩn (Standard Repair Procedure): KTV giỏi biết nhờ KINH NGHIỆM, không nhờ tài liệu → KTV mới phải tự tìm cách\n• Thời gian chẩn đoán (Diagnosis) khác nhau nhất!: KTV giỏi nghe tiếng + nhìn → biết nguyên nhân trong 5 phút. KTV mới → 45 phút thử sai (trial and error)\n• KTV giỏi BIẾT phụ tùng ở đâu: Đi thẳng kệ đúng → lấy → KTV mới lòng vòng tìm 20 phút\n• KTV giỏi có 'trick' sửa nhanh: Mẹo tháo lắp → không truyền lại cho ai!",
            "result": "Chuẩn hóa MTTR bằng Knowledge Management (quản lý kiến thức):\n\n• Video repair guide (hướng dẫn sửa bằng video): Quay lại KTV GIỎI sửa 20 failure modes phổ biến nhất → KTV mới xem video trên tablet → làm theo từng bước\n• Diagnosis flowchart (sơ đồ chẩn đoán): Máy dừng → Nghe tiếng gì? → Check áp suất? → Kết luận A hoặc B → KTV mới cũng chẩn đoán NHANH\n• Parts kit (bộ phụ tùng): Nhóm sẵn phụ tùng cho từng loại sửa → lấy 1 kit = đủ → không tìm kiếm\n• Skill matrix + đào tạo: Đánh giá kỹ năng từng KTV → đào tạo chỗ yếu\n\nKết quả: MTTR: Chênh lệch 1.5-6h → thu hẹp còn 1.5-3h. Average MTTR: 4h → 2.5h"
        },
        {
            "title": "Dùng MTBF để tính tồn kho phụ tùng — Không thừa, không thiếu!",
            "industry": "Sản xuất chung",
            "situation": "Bao nhiêu bearing cần tồn kho? Hiện tại in KHO: 80 chiếc (ai đặt không rõ lý do!). Nhà máy có 50 bearing đang lắp trên máy. MTBF bearing = 2,000 giờ.",
            "analysis": "Dùng MTBF để TÍNH CHÍNH XÁC nhu cầu phụ tùng:\n\nSố lần hỏng dự kiến/năm = 50 bearings × (8,760 giờ/năm ÷ 2,000 giờ MTBF) = 219 lần/năm = 18 chiếc/tháng\n\nDùng phân phối Poisson (thống kê) để tính safety stock:\n• Ở mức phục vụ 95%: Cần 23 bearing/tháng (dự phòng cho biến động)\n• Lead time NCC: 2 tuần → Safety stock = 12 bearing\n\nKết luận: Cần tồn kho = 23 (nhu cầu tháng) + 12 (safety stock) = 35 bearing\n→ Hiện tại đang tồn KHO 80 chiếc → DƯ 45 chiếc! = Đọng vốn 45 × 500K = 22.5 triệu VND",
            "result": "Hành động:\n• Giảm tồn kho: 80 → 35 bearing → Giải phóng 22.5 triệu VND vốn lưu động\n• Lập reorder point tự động: Khi tồn còn 12 chiếc → đặt hàng 23 chiếc → không bao giờ thiếu\n\nÁp dụng cho TẤT CẢ phụ tùng:\n• MTBF-based stocking → giảm overstock 30-40%\n• Đồng thời bổ sung phụ tùng THIẾU (trước đây hết → chờ → MTTR cao!)\n\n→ Bài học: Tồn kho phụ tùng nên tính bằng MTBF + thống kê — KHÔNG PHẢI \"cảm giác\" hay \"mua dư cho chắc\"!"
        },
        {
            "title": "MTBF Lifecycle — Khi nào nên THAY máy mới?",
            "industry": "Sản xuất chung",
            "situation": "Máy 20 năm tuổi: Chi phí BT tăng mỗi năm. BGĐ hỏi: \"Khi nào nên thay mới thay vì tiếp tục sửa?\"",
            "analysis": "Phân tích MTBF lifecycle 20 năm:\n\n| Giai đoạn | Năm | MTBF | Tình trạng |\n| Infant mortality | 1-2 | 200h | Hỏng vặt, lắp đặt, chạy thử |\n| Useful life | 3-8 | 800h | Ổn định, tốt nhất! |\n| Early wear-out | 9-12 | 600h | Bắt đầu mòn |\n| Wear-out accel | 13-16 | 400h | Mòn nhanh! |\n| End of life | 17-20 | 200h | Hỏng liên tục! |\n\nChi phí BT tăng theo tuổi:\n• Năm 3-8: 300 triệu/năm (ổn định)\n• Năm 13-16: 1.2 tỷ/năm (gấp 4!)\n• Năm 17-20: 2.4 tỷ/năm! (gấp 8!) + breakdown tăng → mất sản lượng thêm",
            "result": "Quy tắc quyết định thay máy:\nKhi MTBF  60% khấu hao máy mới → THAY!\n\nHiện tại:\n• MTBF = 200h (dưới 300h ✓)\n• Chi phí BT = 2.4 tỷ/năm\n• Máy mới: 10 tỷ → khấu hao 1 tỷ/năm\n• 2.4 tỷ > 60% × 1 tỷ = 0.6 tỷ → GẤP 4 LẦN ngưỡng!\n\n→ Quyết định: THAY MÁY MỚI! ROI: 2 năm payback\n→ Bài học: MTBF lifecycle analysis cho biết ĐÚNG THỜI ĐIỂM thay máy — không quá sớm (lãng phí), không quá muộn (tốn BT + mất SX)!"
        },
        {
            "title": "5S Workshop BT — Giảm 20% MTTR chỉ bằng DỌN DẸP!",
            "industry": "Sản xuất chung",
            "situation": "Xưởng bảo trì BỪA BỘN: Dụng cụ rải khắp nơi, phụ tùng lẫn cũ/mới, bản vẽ giấy nhàu nát trong tủ. MTTR có phần cao vì KTV MẤT THỜI GIAN TÌM ĐỒ!",
            "analysis": "Phân tích MTTR: 25% thời gian sửa chữa = TÌM KIẾM!\n\n• Tìm dụng cụ (tool): KTV mượn nhau → không trả → tìm khắp workshop\n• Tìm phụ tùng: Kệ lộn xộn, part cũ/mới lẫn, nhiều part sai label\n• Tìm thông tin: Bản vẽ điện (circuit diagram) ở đâu? Manual máy cất chỗ nào? Lịch sử sửa chữa?\n\n25% MTTR = KTV ĐI TÌM ĐỒ thay vì SỬA MÁY!",
            "result": "5S cho xưởng BT:\n• Tool shadow board (bảng treo dụng cụ có hình bóng): Mỗi dụng cụ có VỊ TRÍ CỐ ĐỊNH → 30 giây tìm bất kỳ tool nào! Thiếu tool → thấy NGAY (bóng trống)\n• Phụ tùng organized by machine: Kệ chia theo máy, mỗi ngăn có label rõ ràng, part mới có tag xanh, cũ có tag đỏ\n• Digital manuals trên tablet: Scan tất cả manual + circuit diagram → search trên tablet ra ngay. Lịch sử sửa chữa của từng máy → mở xem 5 giây\n\nKết quả: MTTR 'search time': 25% → 5%. MTTR tổng giảm 20%!\n→ Bài học: 5S KHÔNG CHỈ cho xưởng SX — 5S workshop BT có tác động TRỰC TIẾP lên MTTR!"
        },
        {
            "title": "MTBF cải tiến qua AM — Operator phát hiện 30% breakdown!",
            "industry": "Sản xuất chung",
            "situation": "MTBF = 300 giờ. Đội BT đã làm hết sức nhưng không thể tăng thêm. Có cách nào khác?",
            "analysis": "Autonomous Maintenance (AM — Bảo trì tự chủ) — Operator CŨNG LÀ người bảo trì!\n\nTrước AM: Operator chỉ vận hành. Không kiểm tra, không vệ sinh, không quan tâm → máy xuống cấp dần → KTV phải SỬA\n\nSau AM (Step 1-3): Operator thực hiện hàng ngày:\n• Vệ sinh máy → phát hiện rò rỉ, ốc lỏng, bạc đạn nóng\n• Kiểm tra máy → phát hiện TIẾNG LẠ (15%), RUNG LẠ (10%), RÒ RỈ (20%), ỐC LỎNG (15%), BÁM BẨN (10%)\n• Bôi trơn đúng → giảm ma sát → linh kiện sống lâu hơn\n\n→ Operator phát hiện SỚM 30% lỗi → BÁO BT → BT sửa theo KẾ HOẠCH (planned) thay vì KHẨN CẤP (breakdown)!",
            "result": "Tác động lên MTBF:\n• 30% breakdown được phát hiện sớm bởi operator → chuyển từ unplanned → planned repair\n• MTBF tăng từ 300 → 430 giờ (+43%!)\n• MTTR cũng giảm: Sửa theo kế hoạch (chuẩn bị phụ tùng, dụng cụ trước) → nhanh hơn sửa khẩn cấp\n\n→ AM là cải tiến reliability HIỆU QUẢ NHẤT, CHI PHÍ THẤP NHẤT! Không tốn tiền mua sensor đắt tiền — chỉ cần đào tạo operator VỆ SINH + KIỂM TRA + BÁO CÁO!"
        },
        {
            "title": "MTBF/MTTR Dashboard — Nhìn thấy vấn đề NGAY, không chờ cuối tháng!",
            "industry": "Sản xuất chung",
            "situation": "Trước đây: MTBF/MTTR tính thủ công trên Excel hàng QUÝ → quá muộn để hành động! Khi báo cáo xong → vấn đề đã xảy ra 3 tháng rồi!",
            "analysis": "Vấn đề khi không có dashboard real-time:\n• MTBF giảm liên tục 3 tháng nhưng KHÔNG AI BIẾT cho đến cuối quý → mất 3 tháng phản ứng!\n• Máy breakdown nhiều nhất → không thấy ngay → không focus resources\n• MTTR dài bất thường (1 lần sửa 48h) → không alert → không điều tra\n• Xu hướng (trend) không visible → không dự đoán được → luôn BỊ ĐỘNG",
            "result": "Lắp CMMS (Computerized Maintenance Management System — Hệ thống quản lý bảo trì bằng máy tính):\n\n• Real-time dashboard trên màn hình TV tại phòng BT:\n- MTBF trend (rolling 3 tháng) → nhìn thấy xu hướng NGAY\n- MTTR trend → cải thiện hay xấu đi?\n- Availability trend → đang đạt target?\n• Top 10 worst MTBF machines → biết máy nào CẨN CHÚ Ý nhất!\n• Alert tự động: MTBF giảm 3 tháng liên tiếp → ĐÈN ĐỎ → hành động ngay!\n• Daily auto-calculated: Sáng hôm sau → biết ngay MTBF/MTTR hôm qua\n\nKết quả năm đầu: MTBF tăng 25%, MTTR giảm 20% → Chỉ nhờ NHÌN THẤY số liệu mỗi ngày mà team BT tự cải tiến!"
        }
    ]
}
