method = {
    "id": 10,
    "title": "JSA - Job Safety Analysis",
    "short_name": "JSA",
    "icon": "🦺",
    "pillar": "SHE",
    "description": "Chia công việc thành TỪNG BƯỚC → MỖI bước hỏi 'Cái gì có thể GÂY THƯƠNG TÍCH?' → Đề xuất biện pháp kiểm soát.",
    "meaning": """
<p><strong>JSA (Job Safety Analysis — Phân tích an toàn công việc)</strong>, còn gọi là JHA (Job Hazard Analysis), là phương pháp phân tích an toàn bằng cách <strong>CHIA NHỎ</strong> một công việc thành <strong>các bước tuần tự</strong>, rồi xác định <strong>mối nguy (hazard)</strong> và <strong>biện pháp kiểm soát (control)</strong> TẠI MỖI BƯỚC.</p>
<p><em>Hình dung: HAZOP (method 9) = phân tích an toàn cho HỆ THỐNG (boiler, reactor, pipeline). JSA = phân tích an toàn cho CON NGƯỜI làm CÔNG VIỆC cụ thể (thay die, hàn, vào bồn kín, sửa điện). HAZOP bảo vệ NHÀ MÁY. JSA bảo vệ CÔNG NHÂN!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Cấu trúc JSA — 3 cột thần kỳ</div>
    <p>Mỗi JSA là bảng 3 cột:<br>
    <strong>Cột 1: Bước công việc</strong> → Liệt kê từng bước theo thứ tự thực hiện<br>
    <strong>Cột 2: Mối nguy tiềm ẩn</strong> → Tại mỗi bước, CÁI GÌ có thể gây thương tích?<br>
    <strong>Cột 3: Biện pháp kiểm soát</strong> → Làm GÌ để ngăn ngừa thương tích?<br><br>
    <strong>Hierarchy of Controls (Thứ bậc kiểm soát — ưu tiên từ trên xuống)</strong>:<br>
    1. <strong>Elimination (Loại bỏ)</strong>: Bỏ công việc nguy hiểm hoàn toàn → HIỆU QUẢ NHẤT!<br>
    2. <strong>Substitution (Thay thế)</strong>: Thay bằng cách ít nguy hiểm hơn<br>
    3. <strong>Engineering (Kỹ thuật)</strong>: Rào chắn, interlock, thông gió...<br>
    4. <strong>Administrative (Hành chính)</strong>: SOP, training, permit, rotation...<br>
    5. <strong>PPE (Bảo hộ cá nhân)</strong>: Mũ, găng, kính, dây an toàn... → CUỐI CÙNG, kém hiệu quả nhất!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định mối nguy tại TỪNG BƯỚC công việc → không bỏ sót nguy hiểm "ẩn" trong bước ít ai để ý</li>
    <li>Phát triển biện pháp phòng ngừa TRƯỚC KHI bắt đầu công việc — phòng bệnh hơn chữa bệnh!</li>
    <li>ĐÀO TẠO nhân viên MỚI: Đọc JSA = biết bước nào NGUY HIỂM + phải làm gì để AN TOÀN → thay vì chỉ nói "cẩn thận nhé!"</li>
    <li>Tạo SOP AN TOÀN chuẩn → mọi người làm GIỐNG NHAU → giảm sự khác biệt giữa ca A và ca B</li>
    <li>GIẢM tai nạn: Mỗi JSA hoàn thành = 1 công việc được "rà soát an toàn" → làm đủ JSA cho TẤT CẢ công việc → tai nạn LẦN ĐẦU tiến về 0!</li>
    <li>Đáp ứng PHÁP LUẬT: Luật ATVSLĐ yêu cầu đánh giá rủi ro cho công việc nguy hiểm</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: CHỌN công việc — Ưu tiên công việc NGUY HIỂM nhất!</div>
        <div class="step-card__desc">Ưu tiên JSA cho: Công việc có LỊCH SỬ TAI NẠN (đã từng gây thương tích). Công việc MỚI (chưa có kinh nghiệm). Công việc NGUY HIỂM: Làm trên cao (> 2m), Không gian kín (confined space), Hàn cắt (hot work), Điện cao thế, Hóa chất, Nâng hạ tải trọng. Công việc THAY ĐỔI (quy trình mới, thiết bị mới). KHÔNG cần JSA cho: Công việc văn phòng thông thường, công việc đã có SOP an toàn đầy đủ.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: CHIA BƯỚC — Quan sát THỰC TẾ, viết 6-12 bước</div>
        <div class="step-card__desc">ĐI ĐẾN HIỆN TRƯỜNG — KHÔNG ngồi phòng máy lạnh viết JSA! QUAN SÁT người thực hiện công việc → ghi lại TỪNG BƯỚC. Số bước: 6-12 bước là vừa. Quá ít (< 5) → bỏ sót. Quá nhiều (> 15) → quá chi tiết. Viết bước bằng ĐỘNG TỪ: "Tháo cover", "Cẩu die ra", "Vệ sinh", "Lắp die mới"... QUAN TRỌNG: Hỏi NGƯỜI THỰC HIỆN — họ biết RỦI RO thực tế hơn kỹ sư ngồi phòng!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: XÁC ĐỊNH MỐI NGUY tại mỗi bước — "Cái gì có thể gây thương tích?"</div>
        <div class="step-card__desc">Tại MỖI bước, hỏi: "Cái gì có thể gây THƯƠNG TÍCH?" → Kiểm tra 10 loại mối nguy: <strong>Kẹp/Nghiền</strong> (Caught in/between): Tay kẹp vào máy? <strong>Bị đánh/Va đập</strong> (Struck by): Vật rơi trúng? <strong>Rơi/Ngã</strong> (Fall): Ngã từ trên cao? Trượt? <strong>Điện giật</strong> (Electrocution): Chạm dây? Arc flash? <strong>Bỏng</strong> (Burn): Nhiệt? Hóa chất? <strong>Hít</strong> (Inhalation): Khói? Bụi? Khí độc? <strong>Tiếng ồn</strong> (Noise): Quá 85 dB? <strong>Ergonomics</strong>: Nâng nặng? Tư thế sai? <strong>Hóa chất</strong>: Dính da? Mắt? <strong>Khác</strong>: Thiếu oxy? Rung? Phóng xạ?</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: ĐỀ XUẤT BIỆN PHÁP KIỂM SOÁT — Theo Hierarchy of Controls!</div>
        <div class="step-card__desc">Với MỖI mối nguy → đề xuất biện pháp kiểm soát theo THỨ BẬC: (1) Loại bỏ → (2) Thay thế → (3) Engineering → (4) Administrative → (5) PPE. Ưu tiên ELIMINATION + ENGINEERING → hiệu quả nhất! PPE = phương án CUỐI CÙNG (nếu các biện pháp trên không khả thi). Mỗi biện pháp phải CỤ THỂ: Không viết "cẩn thận" → mà viết "Đeo găng chịu nhiệt EN 407 khi tiếp xúc bề mặt > 50°C". JSA = tài liệu SỐNG → cập nhật khi có tai nạn mới, thiết bị thay đổi, hoặc quy trình sửa đổi!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "JSA thay die máy ép viên — Die 500kg, nóng 80°C!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Thay die máy ép viên (pellet mill) — die nặng 500kg, nóng 80°C sau khi chạy. Đây là công việc THƯỜNG XUYÊN (mỗi 2-4 tuần) nhưng RẤT NGUY HIỂM: Nặng + Nóng + Không gian hẹp + Cẩu!",
            "analysis": "JSA — Thay die Pellet Mill:\n\n| # | Bước | Mối nguy | Biện pháp kiểm soát |\n| 1 | LOTO máy (Lock Out / Tag Out) | ❌ Máy bất ngờ KHỞI ĐỘNG khi tay đang ở trong! → KẸP → CHẾT! | ✅ LOTO: Cắt nguồn + khóa + dán tag TÊN người thao tác. MỖI người 1 khóa riêng → chỉ CHÍNH MÌNH mới mở! |\n| 2 | Đợi nguội | ❌ Die nóng 80°C → BỎNG nặng da tay, ngực (tiếp xúc gần) | ✅ Đợi nhiệt  40°C |\n| 3 | Tháo cover (nắp máy) | ❌ Bu lông rỉ → cờ lê trượt → đập tay/mặt. Nắp nặng rơi | ✅ Dùng đúng size socket. Đỡ nắp bằng giá đỡ hoặc 2 người. Găng cơ khí |\n| 4 | Cẩu die cũ ra | ❌ Die 500kg rơi → ĐÈ CHẾT! Cáp cẩu đứt. Móc tuột. Die xoay | ✅ Cẩu CERTIFIED (đã kiểm định), rated > 1 tấn. Cáp/xích kiểm tra trước. Sling angle KHÔNG ĐỨNG DƯỚI TẢI! Signalman (người ra tín hiệu) riêng biệt |\n| 5 | Vệ sinh buồng ép | ❌ Bụi cám bay vào mắt. Mặt buồng ép sắc → cắt tay | ✅ Kính bảo hộ. Găng chống cắt. Dùng xẻng nhựa (không kim loại — tránh tia lửa nếu có dầu) |\n| 6 | Cẩu die mới vào | ❌ Die va vào người khi hạ. Die lắp lệch → kẹp tay giữa die và frame | ✅ Hạ CHẬM. 2 người canh 2 bên. Tay KHÔNG đặt giữa die và frame! Dùng thanh gỗ/nhựa để canh vị trí |\n| 7 | Chỉnh roller gap | ❌ Tay vào giữa roller và die → KẸP. Mắt trúng dầu mỡ | ✅ LOTO vẫn CÒN hiệu lực! Dùng feeler gauge đo gap. Kính bảo hộ |\n| 8 | Test run | ❌ Rung bất thường (lắp sai). Viên bắn ra (gap không đều) | ✅ Đóng cover trước khi chạy. STAND CLEAR (đứng xa). Chạy 5 phút không tải trước |",
            "result": "Tóm tắt JSA thay die:\n\n• Rủi ro #1: Die 500kg rơi → ĐÈ CHẾT → Control: Cẩu certified + KHÔNG ĐỨNG DƯỚI TẢI\n• Rủi ro #2: Máy khởi động khi tay bên trong → KẸP → CHẾT → Control: LOTO BẮT BUỘC\n• Rủi ro #3: Bỏng 80°C → Control: Đợi Yêu cầu: Tối thiểu 2 người. 1 người thao tác + 1 người hỗ trợ/canh chừng. PPE: Mũ cứng + kính + găng + giày bảo hộ mũi thép\n\n→ Bài học JSA: Công việc \"thường ngày\" (thay die mỗi 2 tuần) KHÔNG CÓ NGHĨA LÀ AN TOÀN! 500kg + 80°C + cẩu = NGUY HIỂM! JSA biến \"quen rồi coi thường\" thành \"mỗi lần đều kiểm tra\""
        },
        {
            "title": "JSA vào bồn kín (Confined Space) — KHÔNG KHÍ ĐỦ ĐỂ THỞ KHÔNG?",
            "industry": "Hóa chất",
            "situation": "Vào bể chứa hóa chất 20m³ để vệ sinh — CONFINED SPACE (không gian kín) = 1 trong những công việc NGUY HIỂM NHẤT! Mỗi năm hàng chục người CHẾT trong confined space (cả người cứu hộ!).",
            "analysis": "JSA — Confined Space Entry (Vào không gian kín):\n\n| # | Bước | Mối nguy | Biện pháp kiểm soát |\n| 1 | Isolate bồn (cô lập) | ❌ Hóa chất còn chảy vào bồn khi người đang ở trong! → NGẠT/BỎNG HÓA CHẤT | ✅ Double block & bleed: 2 van đóng + 1 van xả giữa → XÁC NHẬN không còn hóa chất chảy vào! |\n| 2 | Rửa bồn (từ bên ngoài) | ❌ Hơi hóa chất bay ra khi rửa → HÍT PHẢI | ✅ Rửa từ xa (vòi phun). PPE: Mặt nạ phòng độc. Đứng NGƯỢC GIÓ |\n| 3 | Test khí TRƯỚC KHI VÀO! | ❌ Thiếu oxy (O₂  Khí độc (H₂S, CO) → ngộ độc. Khí cháy nổ (LEL > 10%) → NỔ! | ✅ 4-gas detector: Đo O₂ + LEL + CO + H₂S. Kết quả: O₂ > 19.5%, LEL Thông gió cưỡng bức | ❌ Khí độc tích tụ lại khi vào bồn | ✅ Forced ventilation (quạt cưỡng bức): Thổi khí sạch VÀO liên tục. Vị trí quạt: Không hút từ vùng nhiễm! |\n| 5 | Vào bồn + vệ sinh | ❌ Ngã trong bồn (bề mặt trơn). Hít hơi. Kẹt không ra được | ✅ Harness + lifeline (dây an toàn): Buộc người → nếu bất tỉnh → kéo ra NGAY! Standby person (người canh) ở BÊN NGOÀI miệng bồn 100% thời gian → KHÔNG BAO GIỜ để 1 người vào 1 mình! |\n| 6 | Ra bồn | ❌ Kiệt sức không leo ra được. Khí đổi chiều gió → lùa vào bồn | ✅ Standby person giám sát. Rescue tripod (giá đỡ cứu hộ) sẵn sàng → kéo người ra nhanh chóng |",
            "result": "Quy tắc VÀNG cho Confined Space:\n\n• PERMIT TO WORK (Giấy phép làm việc): PHẢI CÓ permit TRƯỚC khi vào! Permit ghi rõ: Ngày/giờ, ai vào, test khí kết quả bao nhiêu, biện pháp kiểm soát, ai canh\n• 4-gas detector LIÊN TỤC: Không chỉ test 1 lần trước khi vào → ĐEO detector liên tục khi bên trong! Môi trường có thể THAY ĐỔI bất kỳ lúc nào!\n• SCBA (bình thở) SẴN SÀNG: Đặt BÊN NGOÀI miệng bồn → nếu alarm → standby person MẶC SCBA → vào cứu\n• KHÔNG BAO GIỜ cứu hộ mà KHÔNG có PPE!: Rất nhiều trường hợp: 1 người bất tỉnh → 2 người nhảy vào cứu KHÔNG PPE → CẢ 3 CHẾT! → Gọi cứu hộ chuyên nghiệp nếu không có trang bị!\n• Exit plan: Trước khi vào → xác định: Lối ra ở đâu? Nếu bất tỉnh → kéo ra bằng cách nào? Bệnh viện gần nhất ở đâu?\n\n→ Bài học: Confined space = KILLER #1 trong công nghiệp! JSA cho confined space PHẢI cực kỳ chi tiết → MỘT BƯỚC BỎ QUA = MỘT MẠNG NGƯỜI!"
        },
        {
            "title": "JSA bảo trì tủ điện 22kV — ARC FLASH có thể cháy quần áo!",
            "industry": "Điện lực",
            "situation": "Bảo trì tủ điện trung thế 22kV — ĐIỆN CAO THẾ = CHẾT NGAY KHI CHẠM! Arc flash (hồ quang điện) = NHIỆT ĐỘ 20,000°C → cháy quần áo, bỏng toàn thân, mù mắt trong TÍCH TẮC!",
            "analysis": "JSA — Bảo trì tủ điện 22kV:\n\n| # | Bước | Mối nguy | Biện pháp kiểm soát |\n| 1 | CẮT NGUỒN (Open breaker) | ❌ Cắt NHẦM tủ → tủ vẫn CÓ ĐIỆN! Còn điện ĐƯA NGƯỢC từ tải | ✅ Xác nhận đúng tủ bằng SƠ ĐỒ + NHÃN. Cắt TẤT CẢ nguồn cấp + nguồn ngược (backfeed). 2 người verify |\n| 2 | TAG + LOCK | ❌ Người KHÁC đóng lại điện khi mình đang thao tác → CHẾT! | ✅ MỖI người 1 ổ khóa riêng + tag TÊN → chỉ chính mình mở. Nhiều người thao tác → NHIỀU khóa trên cùng 1 lockout hasp |\n| 3 | TEST ĐIỆN = 0 | ❌ Vẫn còn ĐIỆN TỒN DƯ (capacitor charge, induced voltage) → ĐIỆN GIẬT CHẾT! | ✅ Dùng voltage detector CÓ CHỨNG NHẬN (rated cho 22kV). Test TẤT CẢ 3 pha + pha-pha + pha-đất. TEST DETECTOR TRƯỚC (trên nguồn sống) → confirm detector hoạt động! |\n| 4 | NỐI ĐẤT (Grounding) | ❌ Điện cảm ứng từ đường dây song song → VẪN CÓ THỂ GIẬT! | ✅ Lắp dây nối đất tạm thời (temporary ground set) → nối 3 pha xuống đất → nếu có điện cảm ứng → chạy xuống đất, KHÔNG chạy qua người! |\n| 5 | MỞ TỦ + thao tác | ❌ ARC FLASH! Nếu có fault khi mở tủ → hồ quang 20,000°C → bỏng, mù, cháy quần áo. Chạm busbar → điện giật | ✅ Arc flash PPE Cat 4: Quần áo chống hồ quang (arc-rated), face shield chống hồ quang, bao tay cách điện 22kV, giày cách điện. STAND TO THE SIDE (đứng BÊN HÔNG tủ, không đứng ĐỐI DIỆN!) → nếu arc flash → hồ quang bắn RA PHÍA TRƯỚC! |\n| 6 | GỠ GROUND + ĐÓNG ĐIỆN | ❌ Quên gỡ ground → đóng điện → SHORT CIRCUIT → NỔ! | ✅ Checklist: Gỡ ground ✓ → Gỡ lock ✓ → Gỡ tag ✓ → Đóng breaker ✓ → Test tải ✓ |",
            "result": "LOTO 5-Step Safety Procedure (Quy trình an toàn điện 5 bước):\n\n1. OPEN (Cắt) → 2. TAG + LOCK (Khóa) → 3. TEST (Kiểm tra = 0) → 4. GROUND (Nối đất) → 5. TEST lần nữa (xác nhận ground tốt)\n\nChỉ QUALIFIED ELECTRICIAN (thợ điện có chứng chỉ) mới được thao tác!\nBUDDY SYSTEM: LUÔN có 2 người — 1 thao tác + 1 canh chừng + biết CPR/AED!\n\nArc Flash boundary: Xác định khoảng cách an toàn (flash protection boundary) — ai bước VÀO phải mặc arc flash PPE!\n\n→ Bài học JSA điện: 22kV = CHẾT NGAY KHI CHẠM! Arc flash = không cần chạm vẫn BỎNG + MÙ! JSA cho điện = MỖI BƯỚC đều là bước SỐNG CHẾT → KHÔNG BAO GIỜ bỏ bước, KHÔNG BAO GIỜ \"quen rồi thôi\"!"
        },
        {
            "title": "JSA hàn cắt nóng (Hot Work) — 30 phút sau hàn VẪN CÓ THỂ CHÁY!",
            "industry": "Bảo trì",
            "situation": "Hàn sửa đường ống trong nhà máy sản xuất — cạnh khu vực có vật liệu dễ cháy (giấy, gỗ, dầu). Hot work (hàn, cắt, mài) = TIA LỬA bay xa đến 11 mét! → Nguy cơ CHÁY NỔ!",
            "analysis": "JSA — Hot Work (Hàn cắt nóng):\n\n| # | Bước | Mối nguy | Biện pháp kiểm soát |\n| 1 | Lấy HOT WORK PERMIT (Giấy phép hàn nóng) | ❌ Hàn mà KHÔNG có permit → không ai kiểm tra khu vực → CHÁY! | ✅ PHẢI có permit TRƯỚC KHI bắt đầu! Permit ký bởi area supervisor → xác nhận khu vực ĐÃ kiểm tra an toàn |\n| 2 | Kiểm tra khu vực 11m | ❌ Vật liệu dễ cháy gần (giấy, gỗ, dầu, dung môi, bụi) → tia lửa rơi → CHÁY! | ✅ Di chuyển TẤT CẢ vật liệu dễ cháy trong bán kính 11m (35 feet). Không di chuyển được → che phủ bằng fire blanket (chăn chống cháy). Nếu có gas/dung môi → KHÔNG HÀN → dùng phương pháp khác! |\n| 3 | Setup thiết bị hàn | ❌ Ống gas bị rò → gas tích tụ → NỔ! Dây hàn hở → điện giật | ✅ Kiểm tra ống gas (xà phòng test). Kiểm tra dây hàn không hở. Flashback arrestor (chống cháy ngược) trên mỏ hàn gas |\n| 4 | HÀN | ❌ Bỏng (tia lửa, kim loại nóng chảy). UV → cháy mắt (welder's eye). Khói hàn → hít bụi kim loại (Mn, Cr, Zn) → suy phổi | ✅ PPE: Mặt nạ hàn auto-darkening + găng da dài + tạp dề da + giày bảo hộ. LEV (Local Exhaust Ventilation — hút khói cục bộ) tại điểm hàn → hút khói đi NGAY |\n| 5 | Kiểm tra SAU hàn | ❌ TIA LỬA NẰM ẨN → ÂM Ỉ → CHÁY SAU 30 PHÚT đến VÀI GIỜ! | ✅ FIRE WATCH 30 PHÚT sau hàn! Người canh chừng với bình chữa cháy → ở lại khu vực 30 phút SAU KHI ngừng hàn → kiểm tra KHÔNG CÓ ÂM Ỉ! |\n| 6 | Thu dọn | ❌ Mẩu kim loại nóng trên sàn → người khác GIẪM PHẢI → bỏng | ✅ Quét sạch mẩu kim loại NGAY. Đánh dấu vùng nóng nếu chưa nguội |",
            "result": "Quy tắc Hot Work:\n\n• HOT WORK PERMIT BẮT BUỘC: Mỗi lần hàn = 1 permit mới. Hết ca = permit hết hiệu lực → hôm sau = cần permit MỚI\n• 11 mét rule: Tia lửa bay xa đến 11m → kiểm tra và dọn sạch trong bán kính 11m\n• FIRE WATCH 30 phút: KHÔNG BAO GIỜ bỏ đi ngay sau khi hàn xong! Nhiều vụ cháy nhà máy xảy ra VÀI GIỜ SAU khi hàn!\n• Thống kê thực tế: Theo NFPA (Hiệp hội Phòng cháy Mỹ): Hot work gây ra 4,500 vụ cháy/năm → thiệt hại 200 triệu USD → PHẦN LỚN do KHÔNG kiểm tra sau hàn!\n\n→ Bài học JSA: Bước 5 (fire watch 30 phút SAU hàn) = bước mà 90% người BỎ QUA! \"Hàn xong → đi luôn\" → 2 giờ sau → CHÁY! JSA buộc phải GHI RÕ bước này → KHÔNG THỂ bỏ!"
        },
        {
            "title": "JSA vận hành xe nâng — Va chạm người đi bộ = rủi ro #1!",
            "industry": "Logistics",
            "situation": "Vận hành xe nâng (forklift) trong kho hàng CÓ NGƯỜI ĐI BỘ. Xe nâng 2.5 tấn × 15 km/h = lực va chạm CỰC LỚN → ĐÈ CHẾT người! Năm 2023: 85 người tử vong do xe nâng tại Mỹ (OSHA).",
            "analysis": "JSA — Vận hành xe nâng trong kho:\n\n| # | Bước | Mối nguy | Biện pháp kiểm soát |\n| 1 | Kiểm tra trước ca | ❌ Phanh hỏng → KHÔNG DỪNG ĐƯỢC! Vô lăng lỏng → MẤT LÁI! Rò dầu thủy lực → fork hạ đột ngột | ✅ Pre-use checklist: Phanh ✓ Vô lăng ✓ Đèn ✓ Còi ✓ Dầu ✓ Fork ✓ Seatbelt ✓. Bất kỳ item FAIL → KHÔNG chạy → BÁO BT ngay! |\n| 2 | Nâng hàng | ❌ Nâng QUÁ TẢI → xe LẬT! Fork không vào đúng pallet → hàng rơi → ĐÈ | ✅ Kiểm tra load chart (bảng tải trọng) → KHÔNG vượt! Fork vào tận SÁT thành pallet → nâng từ từ → kiểm tra ổn định |\n| 3 | Di chuyển | ❌ VA CHẠM NGƯỜI ĐI BỘ! Góc khuất → không thấy người. Hàng cao → che tầm nhìn | ✅ Speed limit 10 km/h (5 km/h ở góc cua!). HORN (bấm còi) tại MỌI giao lộ và góc khuất! Hàng cao → ĐI LÙI (nhìn rõ hơn). Gương cầu lồi tại góc khuất |\n| 4 | Xếp hàng lên rack | ❌ Fork chọc thủng hàng rack trên → hàng RƠI XUỐNG ĐẦU. Xe nâng va rack → rack đổ DOMINO! | ✅ Nâng/hạ CHẬM. KHÔNG AI ĐỨNG DƯỚI tải đang nâng! Rack protector (thanh bảo vệ chân rack). End-of-aisle guard |\n| 5 | Hạ hàng | ❌ Hạ quá nhanh → hàng trượt khỏi fork → rơi chèn chân | ✅ Hạ CHẬM. Fork nghiêng nhẹ ra sau. Bước lùi SAU KHI hạ xong (không đứng ngay trước) |",
            "result": "Biện pháp bổ sung cho an toàn xe nâng:\n\n• Pedestrian lane (làn người đi bộ): Sơn vạch TÁCH BIỆT đường xe nâng và đường người đi bộ → KHÔNG ĐI CHUNG!\n• Blue spot light: Đèn LED chiếu 1 chấm xanh trước xe nâng 5m → người đi bộ THẤY ánh sáng xanh = XE NÂNG ĐANG ĐẾN → TRÁNH!\n• Backup alarm (còi lùi): Xe nâng đi lùi → còi tự động kêu → cảnh báo người phía sau\n• Seatbelt BẮT BUỘC: Xe lật → seatbelt giữ người TRONG cabin → sống! Không seatbelt → người bị NÉM RA → xe ĐÈ lên → CHẾT!\n• Chỉ người có GIẤY PHÉP mới được lái: Training + test + cấp giấy phép nội bộ → không có giấy phép = KHÔNG ĐƯỢC LÁI!\n\n→ Bài học JSA xe nâng: Rủi ro #1 = VA CHẠM người đi bộ! Engineering control (pedestrian lane, blue spot) HIỆU QUẢ HƠN 100 lần so với Admin control (\"đi cẩn thận\")! → Hierarchy of Controls!"
        },
        {
            "title": "JSA làm việc trên cao — Dây an toàn + Toe board cứu mạng!",
            "industry": "Xây dựng",
            "situation": "Sửa chữa mái tôn nhà xưởng ở độ cao 12m. Ngã từ trên cao = NGUYÊN NHÂN TỬ VONG SỐ 1 trong ngành xây dựng! Năm 2023: 395 người chết do ngã từ trên cao tại Mỹ (BLS).",
            "analysis": "JSA — Làm việc trên cao 12m:\n\n| # | Bước | Mối nguy | Biện pháp kiểm soát |\n| 1 | Dựng giàn giáo | ❌ Giàn giáo đổ do đất mềm / lắp sai. Vật rơi khi dựng | ✅ Competent person (người có năng lực) giám sát. Base plate trên nền CỨNG. Kiểm tra TRƯỚC khi sử dụng. Tag GREEN = OK |\n| 2 | Leo lên | ❌ Trượt thang. Giẫm nhầm bậc | ✅ 3-point contact (3 điểm tiếp xúc): 2 tay + 1 chân hoặc 1 tay + 2 chân LUÔN LUÔN tiếp xúc! KHÔNG mang đồ bằng tay khi leo → dùng túi đeo hoặc kéo dây |\n| 3 | Làm việc trên mái | ❌ TRỢ GÃ QUA MÉP! Tôn mỏng → GIẪM THỦNG → RƠI! Gió mạnh → mất thăng bằng | ✅ Harness + lifeline (dây an toàn + dây cứu sinh): Buộc vào anchor point CHỊU 2,268 kg (5,000 lbs). Guardrail (lan can) xung quanh khu vực làm việc. KHÔNG GIẪM lên tôn mỏng → đi trên xà gồ! Toe board (tấm chắn chân) → ngăn dụng cụ trượt rơi xuống |\n| 4 | Tháo/lắp tôn | ❌ Tấm tôn gió thổi → BAY → cắt người bên dưới! Tôn sắc → cắt tay | ✅ Buộc tôn bằng dây. Không làm khi gió > 40 km/h. Găng chống cắt |\n| 5 | Hạ vật liệu, xuống | ❌ Ném đồ xuống → TRÚNG người bên dưới | ✅ KHÔNG NÉM! Hạ bằng dây thừng hoặc ống trượt. Exclusion zone (vùng cấm) bên dưới → rào + biển báo → KHÔNG AI được vào! |",
            "result": "FALL PROTECTION — Quy tắc vàng:\n\n• > 2m = PHẢI có fall protection (theo TCVN / OSHA): Guardrail HOẶC Harness + lifeline HOẶC Net (lưới)\n• Harness 5-point (dây an toàn 5 điểm): ĐÚNG cách mặc → dây qua vai, ngực, hông → nếu rơi → treo THẲNG ĐỨNG → SỐNG!\n• Anchor point: PHẢI chịu 2,268 kg! Không buộc vào ống nước, lan can mỏng, hay dây điện!\n• Catch net (lưới an toàn): Căng lưới bên dưới khu vực làm việc → nếu rơi → rơi vào lưới → SỐNG!\n• Buddy system: LUÔN 2 người → 1 ngã → 1 cứu/gọi cấp cứu\n• Giới hạn thời gian khi trời nóng: > 35°C → nghỉ 15 phút/giờ → tránh sốc nhiệt → MẤT THĂNG BẰNG → NGÃ!\n\n→ Bài học JSA trên cao: Ngã từ 12m = vận tốc chạm đất 55 km/h → TỬ VONG! Harness + lifeline = BẢO HIỂM NHÂN THỌ thực sự! MỘT lần quên đeo = MỘT lần cá cược MẠNG SỐNG!"
        }
    ]
}
