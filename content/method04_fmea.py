method = {
    "id": 4,
    "title": "FMEA - Failure Mode & Effect Analysis",
    "short_name": "FMEA",
    "icon": "⚠️",
    "pillar": "Early Management",
    "description": "Phân tích dạng hỏng & tác động — Đánh giá rủi ro TRƯỚC KHI xảy ra, ưu tiên phòng ngừa bằng RPN.",
    "meaning": """
<p><strong>FMEA (Failure Mode and Effect Analysis — Phân tích Dạng hỏng và Tác động)</strong> là phương pháp phân tích có hệ thống nhằm xác định các dạng hỏng TIỀM ẨN (chưa xảy ra!), đánh giá mức độ rủi ro, từ đó PHÒNG NGỪA trước khi vấn đề thực sự xảy ra.</p>
<p><em>Nói đơn giản: FMEA = "Tưởng tượng TẤT CẢ cách mà sản phẩm/quy trình CÓ THỂ hỏng → Đánh giá cái nào NGUY HIỂM NHẤT → Phòng ngừa TRƯỚC!"</em></p>
<div class="note-box note-box--warning">
    <div class="note-title">⚡ Chỉ số RPN — Số ưu tiên rủi ro</div>
    <p><strong>RPN = S × O × D</strong> (Risk Priority Number — Số ưu tiên rủi ro)<br><br>
    <strong>S — Severity (Mức độ NGHIÊM TRỌNG)</strong>: Nếu hỏng thì HẬU QUẢ nặng cỡ nào? (1 = không đáng kể → 10 = tai nạn chết người/thu hồi sản phẩm)<br>
    <strong>O — Occurrence (Tần suất XẢY RA)</strong>: Dạng hỏng này xảy ra THƯỜNG XUYÊN cỡ nào? (1 = gần như không bao giờ → 10 = xảy ra liên tục)<br>
    <strong>D — Detection (Khả năng PHÁT HIỆN)</strong>: Nếu hỏng xảy ra, có PHÁT HIỆN ĐƯỢC không trước khi đến tay khách hàng? (1 = chắc chắn phát hiện → 10 = KHÔNG THỂ phát hiện!)<br><br>
    <strong>RPN > 100 → PHẢI hành động!</strong> RPN càng cao → rủi ro càng lớn → ưu tiên phòng ngừa!<br>
    <em>Lưu ý QUAN TRỌNG: Nếu S ≥ 9 (nghiêm trọng — an toàn/pháp luật) → PHẢI hành động DÙ RPN thấp!</em></p>
</div>
<p><strong>2 loại FMEA</strong>:<br>
• <strong>DFMEA (Design FMEA)</strong>: Phân tích THIẾT KẾ sản phẩm — "Sản phẩm có thể hỏng theo cách nào?"<br>
• <strong>PFMEA (Process FMEA)</strong>: Phân tích QUY TRÌNH sản xuất — "Quy trình có thể gây lỗi theo cách nào?"</p>
""",
    "purpose": """
<ul>
    <li>Xác định SỚM các dạng hỏng TIỀM ẨN — phòng bệnh hơn chữa bệnh! Chi phí sửa ở giai đoạn thiết kế RẺ HƠN 100 lần so với sửa sau khi sản phẩm đến tay khách hàng</li>
    <li>Đánh giá rủi ro bằng RPN → ưu tiên hành động ĐÚNG CHỖ — không phân bổ nguồn lực đều cho mọi rủi ro</li>
    <li>Giảm chi phí warranty (bảo hành), recall (thu hồi), complaint (khiếu nại) bằng cách ngăn chặn lỗi từ gốc</li>
    <li>Yêu cầu BẮT BUỘC trong nhiều ngành: Ô tô (IATF 16949), Y tế (ISO 13485), Hàng không (AS9100)</li>
    <li>LƯU TRỮ kiến thức kỹ thuật có cấu trúc — FMEA là "bộ nhớ" của tổ chức về rủi ro → nhân viên mới đọc FMEA = hiểu ngay rủi ro!</li>
    <li>Cải thiện RELIABILITY (độ tin cậy) sản phẩm và quy trình → ít hỏng hơn, ít lỗi hơn, ít khiếu nại hơn</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định phạm vi — Phân tích CÁI GÌ?</div>
        <div class="step-card__desc">Chọn sản phẩm/quy trình cần phân tích. Liệt kê TẤT CẢ chức năng (functions) và yêu cầu kỹ thuật. Ví dụ: Pellet Mill → Chức năng: Ép viên 40 T/h, PDI > 92%, Nhiệt viên < 80°C. Thành lập nhóm CROSS-FUNCTION: Thiết kế + SX + QC + BT + NCC (mỗi người thấy 1 góc rủi ro khác).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Liệt kê Failure Modes — Hỏng theo CÁCH NÀO?</div>
        <div class="step-card__desc">Với MỖI chức năng, hỏi: "Chức năng này có thể THẤT BẠI theo cách nào?" → Liệt kê failure modes (dạng hỏng). Ví dụ: Pellet Mill → FM: Die nứt, Bạc đạn kẹt, Motor overload, Steam valve rò, Feeder tắc, Roller mòn... Cho mỗi FM: Xác định Failure Effect (hậu quả) và Failure Cause (nguyên nhân). Dùng kinh nghiệm, CMMS data (dữ liệu hỏng cũ), OEM manual, C-E diagram (method 3).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Đánh giá S-O-D → Tính RPN</div>
        <div class="step-card__desc">Cho mỗi failure mode, nhóm CÙNG CHẤM ĐIỂM: <strong>S (Severity 1-10)</strong>: Hậu quả nặng cỡ nào? An toàn = 9-10. Dừng SX = 7-8. Chất lượng giảm = 4-6. <strong>O (Occurrence 1-10)</strong>: Bao lâu xảy ra 1 lần? Hàng ngày = 8-10. Hàng tháng = 5-7. Hàng năm = 2-4. <strong>D (Detection 1-10)</strong>: Phát hiện khó không? Auto detect = 1-3. Manual inspect = 4-6. Khó/không phát hiện = 7-10. RPN = S × O × D → Sắp xếp từ CAO → THẤP.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Hành động phòng ngừa → Tính lại RPN sau cải tiến</div>
        <div class="step-card__desc">RPN > 100 hoặc S ≥ 9 → PHẢI hành động! 3 cách giảm RPN: <strong>Giảm O</strong> (giảm xảy ra): PM, design change, better material. <strong>Giảm D</strong> (tăng phát hiện): Sensor, inspection, test, Poka-Yoke. <strong>Giảm S</strong> (giảm nghiêm trọng): Redesign, backup system, safety device. Sau khi thực hiện → chấm lại S-O-D → tính RPN mới → xác nhận đã giảm đủ! FMEA là LIVING DOCUMENT (tài liệu sống) — cập nhật khi có FM mới, sản phẩm thay đổi, hoặc field failure (hỏng thực tế ngoài dự đoán).</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "PFMEA trộn TACN — Cross-contamination thuốc RPN = 200!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Phân tích PFMEA (Process FMEA) cho quy trình trộn (batching & mixing) thức ăn gia súc. Nhà máy sản xuất cả thức ăn CÓ THUỐC và KHÔNG THUỐC trên cùng dây chuyền.",
            "analysis": "FMEA worksheet — TOP failure modes:\n\n| # | Failure Mode | S | O | D | RPN |\n| 1 | Cross-contamination thuốc (lẫn thuốc giữa các mẻ) | 10 | 4 | 5 | 200! |\n| 2 | Trộn không đều (CV% > 10%) | 7 | 3 | 4 | 84 |\n| 3 | Sai công thức (cân sai liều) | 9 | 3 | 3 | 81 |\n| 4 | NL bị ẩm, vón cục | 5 | 4 | 3 | 60 |\n\nFM #1 đặc biệt nguy hiểm: S = 10 (thuốc kháng sinh lẫn vào thức ăn KHÔNG THUỐC → vi phạm an toàn thực phẩm, có thể bị thu hồi sản phẩm + phạt nặng!). O = 4 (xảy ra vài lần/năm do xả cặn không đủ giữa mẻ). D = 5 (khó test nhanh cross-contamination → phải gửi lab 2-3 ngày!)",
            "result": "Action cho RPN 200 (PHẢI giảm NGAY!):\n\nGiảm O (Occurrence — giảm xảy ra):\n• Sequencing flush (mẻ rửa): Chạy 1 mẻ NL trống giữa mẻ CÓ THUỐC và KHÔNG THUỐC → đẩy hết cặn thuốc ra\n• Dedicated micro-ingredient mixer (máy trộn vi lượng riêng cho thuốc) → không dùng chung\n→ O: 4 → 2\n\nGiảm D (Detection — tăng khả năng phát hiện):\n• Test nhanh (rapid test kit) tại nhà máy → kết quả 30 phút thay vì 2 ngày\n→ D: 5 → 2\n\nRPN mới: 10 × 2 × 2 = 40! (giảm từ 200 → 40)\n→ Bài học: S = 10 (an toàn thực phẩm) → DÙ RPN thấp vẫn phải hành động! Cross-contamination = rủi ro SỐ 1 trong nhà máy TACN!"
        },
        {
            "title": "PFMEA chiết rót sữa — Nhiễm khuẩn S=10, phải UV + online test!",
            "industry": "Thực phẩm",
            "situation": "Dây chuyền chiết rót sữa tươi tiệt trùng MỚI. Trước khi chạy, phải làm PFMEA để xác định rủi ro quy trình.",
            "analysis": "FMEA cho quy trình chiết rót:\n\n| # | Failure Mode | Effect (Hậu quả) | S | O | D | RPN |\n| 1 | Nhiễm khuẩn (bacterial contamination) | Sữa chua sớm → thu hồi → mất uy tín | 10 | 3 | 5 | 150! |\n| 2 | Seal không kín (seal defect) | Rò rỉ → sữa bị hỏng, khách trả hàng | 9 | 4 | 3 | 108 |\n| 3 | Thể tích sai (fill volume error) | Thiếu: vi phạm nhãn. Thừa: lỗ | 5 | 3 | 2 | 30 |\n\nTại sao Detection = 5 cho nhiễm khuẩn?\nVi khuẩn KHÔNG NHÌN THẤY BẰNG MẮT! Sữa nhiễm khuẩn trông/ngửi bình thường lúc mới chiết → phải nuôi cấy 2-3 ngày mới biết → Lúc biết → sữa ĐÃ GIAO cho khách rồi! → D = 5 (khó phát hiện kịp thời!)",
            "result": "Action cho RPN 150:\n\nGiảm O (giảm xảy ra):\n• UV sterilization (khử trùng tia cực tím) tại đầu chiết → diệt vi khuẩn ngay trước khi sữa vào hộp\n• CIP validation (xác nhận quy trình vệ sinh): Swab test bề mặt ống + đo ATP (đo vi sinh nhanh) TRƯỚC khi chạy\n→ O: 3 → 1\n\nGiảm D (tăng phát hiện):\n• Online bacteria test: Máy đo vi khuẩn real-time (impedance method — phương pháp trở kháng) → kết quả 4 giờ thay vì 3 ngày!\n→ D: 5 → 2\n\nRPN mới: 10 × 1 × 2 = 20! (giảm từ 150 → 20)\n→ Bài học FMEA: S = 10 có thể KHÔNG GIẢM ĐƯỢC (nhiễm khuẩn luôn nghiêm trọng!) → Phải giảm O (ngăn xảy ra) VÀ D (phát hiện sớm)!"
        },
        {
            "title": "DFMEA ECU ô tô — Software hang RPN 192, cần watchdog!",
            "industry": "Ô tô",
            "situation": "Thiết kế DFMEA (Design FMEA) cho ECU (Electronic Control Unit — hộp điều khiển điện tử) điều khiển động cơ ô tô. Yêu cầu theo IATF 16949 (tiêu chuẩn chất lượng ô tô quốc tế).",
            "analysis": "DFMEA cho ECU:\n\n| # | Failure Mode | Effect | S | O | D | RPN |\n| 1 | Software hang (phần mềm treo) | Mất điều khiển động cơ → xe dừng đột ngột! | 8 | 4 | 6 | 192! |\n| 2 | Connector corrode (chân kết nối bị ăn mòn) | Tín hiệu gián đoạn → động cơ chạy không ổn | 7 | 5 | 5 | 175 |\n| 3 | PCB short circuit (chập mạch) | ECU chết → xe không khởi động | 9 | 3 | 4 | 108 |\n\nSoftware hang (RPN 192) nguy hiểm nhất!\n• D = 6 (KHÓ phát hiện!): Software treo xảy ra ngẫu nhiên, không dự đoán được lúc nào → không test hết tất cả trường hợp\n• Hậu quả: Xe đang chạy 100 km/h → ECU hang → mất điều khiển ga, nhiên liệu → CỰC KỲ NGUY HIỂM!",
            "result": "Action cho TOP 3 RPN:\n\nFM #1 — Software hang (RPN 192):\n• Watchdog timer (bộ canh gác): Chip giám sát riêng → nếu phần mềm không \"gõ cửa\" mỗi 10ms → watchdog TỰ ĐỘNG RESET ECU → khôi phục trong 32\n\nFM #2 — Connector corrode (RPN 175):\n• Sealed connector (đầu nối kín nước) IP67 + Gold plating (mạ vàng chống ăn mòn)\n→ O: 5 → 2 → RPN: 175 → 56\n\nFM #3 — PCB short (RPN 108):\n• Conformal coating (phủ lớp bảo vệ mạch) → chống ẩm, bụi, muối\n→ O: 3 → 1 → RPN: 108 → 36\n\n→ Bài học DFMEA ô tô: 1 lỗi ECU = TAI NẠN → FMEA là BẮT BUỘC không thương lượng trong ngành ô tô!"
        },
        {
            "title": "PFMEA dược phẩm — Cross-contamination thuốc = hậu quả chết người!",
            "industry": "Dược phẩm",
            "situation": "PFMEA cho quy trình sản xuất thuốc viên nén theo GMP (Good Manufacturing Practice — Thực hành sản xuất tốt). Nhà máy sản xuất nhiều loại thuốc trên cùng thiết bị.",
            "analysis": "FMEA cho quy trình dược:\n\n| # | Failure Mode | Effect | S | O | D | RPN |\n| 1 | Cross-contamination (lẫn thuốc giữa lô) | BN uống thuốc sai → DỊ ỨNG/TỬ VONG! | 10 | 3 | 4 | 120 |\n| 2 | Sai hàm lượng hoạt chất (potency error) | Thuốc không hiệu quả HOẶC quá liều! | 10 | 2 | 3 | 60 |\n| 3 | Độ cứng viên sai (tablet hardness) | Viên vỡ hoặc không tan → không hiệu quả | 4 | 4 | 2 | 32 |\n\nCross-contamination đặc biệt nguy hiểm:\n• Ví dụ kinh hoàng thực tế: Thuốc beta-blocker (tim mạch) lẫn vào thuốc dị ứng → BN dùng → huyết áp tụt → nhập viện!\n• Nguyên nhân thường gặp: Vệ sinh thiết bị giữa các lô KHÔNG ĐỦ, hạt thuốc lô trước còn bám trong máy trộn",
            "result": "Action cho S = 10:\n\nGiảm O (giảm xảy ra):\n• Dedicated equipment (thiết bị chuyên dụng) cho thuốc high-potency (thuốc mạnh): Máy trộn, máy ép riêng → KHÔNG DÙNG CHUNG\n• Line clearance checklist (bảng kiểm tra dọn dẹp dây chuyền): Sau mỗi lô → vệ sinh + kiểm tra bằng mắt + swab test → ký xác nhận → lô mới mới được bắt đầu\n→ O: 3 → 1\n\nGiảm D (tăng phát hiện):\n• Swab test + visual inspection SAU vệ sinh\n• HPLC test cho lô đầu tiên sau changeover\n→ D: 4 → 2\n\nRPN mới: 10 × 1 × 2 = 20!\n→ Bài học dược phẩm: Trong ngành dược, S ≥ 9 → KHÔNG CHỜ RPN > 100 mới hành động! An toàn bệnh nhân = ưu tiên TUYỆT ĐỐI!"
        },
        {
            "title": "DFMEA hệ thống PCCC — Sprinkler không kích hoạt = THẢM HỌA!",
            "industry": "Phòng cháy",
            "situation": "DFMEA cho hệ thống sprinkler tự động trong nhà kho 10,000 m². Kho chứa hàng dễ cháy (nhựa, giấy, vải).",
            "analysis": "FMEA cho hệ thống PCCC:\n\n| # | Failure Mode | Effect | S | O | D | RPN |\n| 1 | Sprinkler không kích hoạt (fails to activate) | Cháy không được dập → lan rộng → THẢM HỌA! | 10 | 2 | 4 | 80 |\n| 2 | Áp lực nước không đủ (low pressure) | Nước phun yếu → không dập được lửa lớn | 9 | 3 | 3 | 81 |\n| 3 | False alarm (báo cháy giả) | Phun nước khi không cháy → ướt hàng → thiệt hại | 3 | 5 | 2 | 30 |\n\nTại sao D = 4 cho \"sprinkler không kích hoạt\"?\nSprinkler nằm YÊN trên trần 100% thời gian → CHỈ hoạt động khi có cháy! → Nếu bị HỎI, ĂN MÒN, TẮC → KHÔNG AI BIẾT! (Hidden failure — hỏng ẩn!) → Khi cháy thật → MỚI biết nó không hoạt động → QUÁ MUỘN!\n\nDù RPN chỉ 80 (",
            "result": "Action cho S = 10 (an toàn sinh mạng — không thương lượng!):\n\nGiảm O:\n• PM: Kiểm tra đầu sprinkler hàng năm (visual + FPI test theo NFPA 25)\n• Bảo vệ ống khỏi ăn mòn → nitrogen fill (bơm nitơ — khí trơ) cho ống khô\n→ O: 2 → 1\n\nGiảm D:\n• Monthly flow test (test dòng chảy hàng tháng): Mở van test → xác nhận nước chảy đủ áp → ÍT NHẤT biết hệ thống CÒN SỐNG!\n• Jockey pump backup (bơm dự phòng): Nếu bơm chính hỏng → bơm dự phòng tự khởi động\n→ D: 4 → 2\n\nRPN mới: 10 × 1 × 2 = 20!\n→ Bài học FMEA cho thiết bị an toàn: Sprinkler, báo cháy, van an toàn, cầu dao... = HIDDEN FAILURE → phải kiểm tra định kỳ (Failure-Finding — xem RCM method 41)!"
        },
        {
            "title": "FMEA Mobile Banking — Data breach S=10, RPN 150!",
            "industry": "Tài chính",
            "situation": "FMEA cho hệ thống Mobile Banking app trước khi launch. Phải đánh giá rủi ro bảo mật theo yêu cầu ngân hàng nhà nước.",
            "analysis": "FMEA cho banking app:\n\n| # | Failure Mode | Effect | S | O | D | RPN |\n| 1 | Data breach (rò rỉ dữ liệu) | Lộ thông tin KH → mất tiền, mất uy tín, phạt pháp lý | 10 | 3 | 5 | 150! |\n| 2 | Transaction failure (giao dịch thất bại) | KH không chuyển được tiền → khiếu nại | 8 | 4 | 3 | 96 |\n| 3 | Session hijack (chiếm phiên đăng nhập) | Hacker dùng session KH → chuyển tiền đi! | 10 | 2 | 4 | 80 |\n\nData breach (RPN 150):\n• D = 5 (KHÓ phát hiện!): Hacker có thể đã lấy dữ liệu HÀNG THÁNG trước khi phát hiện (như trường hợp Equifax, Yahoo)\n• Hậu quả: Lộ số tài khoản, số CMND, password → KH mất tiền → kiện ngân hàng → phạt luật bảo vệ dữ liệu",
            "result": "Action cho banking security:\n\nGiảm O (giảm xảy ra):\n• End-to-end encryption (mã hóa đầu cuối): Dữ liệu MÃ HÓA suốt đường đi → hacker bắt được cũng KHÔNG ĐỌC ĐƯỢC\n• 2FA (Two-Factor Authentication — xác thực 2 bước): Password + OTP/Biometrics → hacker có password vẫn không vào được\n→ O: 3 → 1\n\nGiảm D (tăng phát hiện):\n• Penetration test (test xâm nhập) hàng quý: \"Ethical hackers\" tấn công hệ thống → tìm lỗ hổng TRƯỚC hacker thật\n• Real-time anomaly detection (phát hiện bất thường): AI giám sát traffic → phát hiện tấn công trong PHÚT\n→ D: 5 → 2\n\nRPN mới: 10 × 1 × 2 = 20!\n→ Bài học: FMEA không chỉ cho nhà máy! Banking, healthcare, aviation → bất kỳ hệ thống nào rủi ro CAO đều CẦN FMEA!"
        },
        {
            "title": "DFMEA LED driver ngoài trời — Sét đánh RPN 180, cần SPD!",
            "industry": "Điện-Điện tử",
            "situation": "DFMEA cho LED driver 150W (bộ nguồn đèn LED) dùng cho đèn đường outdoor (ngoài trời). Phải chịu nắng, mưa, sét, bẩn.",
            "analysis": "DFMEA cho LED driver outdoor:\n\n| # | Failure Mode | Effect | S | O | D | RPN |\n| 1 | Sét đánh (lightning surge) | Cháy PCB → đèn tắt → nguy hiểm giao thông! | 10 | 3 | 6 | 180! |\n| 2 | Quá nhiệt (overheating) | Component hỏng → tuổi thọ giảm 50% hoặc cháy | 9 | 4 | 4 | 144 |\n| 3 | Điện áp đầu ra bất thường (output voltage drift) | LED sáng yếu hoặc quá sáng → hỏng LED | 8 | 3 | 3 | 72 |\n\nSét (RPN 180) — D = 6 (rất khó phát hiện!):\n• Surge (xung điện áp do sét) có thể GÂY HẠI mà KHÔNG phá hủy ngay → PCB bị suy yếu dần → hỏng sau vài tuần/tháng\n• Outdoor → trên cột cao → DỄ BỊ SÉT hơn thiết bị trong nhà\n• 150W driver: Giá chỉ 2 triệu VND nhưng thay 1 cái phải cẩu xe, 2 NV, 2 giờ → chi phí thay 5 triệu! Thay 1,000 cái = 5 TỶ!",
            "result": "Action:\n\nFM #1 — Sét (RPN 180):\n• SPD (Surge Protection Device — thiết bị chống sét): Lắp MOV (Metal Oxide Varistor) + GDT (Gas Discharge Tube) → hấp thụ xung sét → bảo vệ PCB\n• Design kV rating phù hợp: 10kV/10kA theo IEC 61000-4-5\n→ O: 3 → 1, D: 6 → 3 → RPN: 180 → 30\n\nFM #2 — Quá nhiệt (RPN 144):\n• Thermal management: Heatsink nhôm + thermal derating (giảm công suất khi nhiệt cao) + fan tự động trên 70°C\n→ O: 4 → 2 → RPN: 144 → 54\n\n→ Bài học DFMEA outdoor: Thiết bị ngoài trời phải chịu SÉT, NÓNG, MƯA, BỤI → Mỗi yếu tố = 1 failure mode → FMEA giúp thiết kế CHỊU ĐƯỢC tất cả!"
        }
    ]
}
