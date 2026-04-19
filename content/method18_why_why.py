method = {
    "id": 18,
    "title": "Why-Why Analysis - Phân tích Tại sao - Tại sao",
    "short_name": "Why-Why Analysis",
    "icon": "❓",
    "pillar": "Focus Improvement",
    "description": "Hỏi 'TẠI SAO?' liên tục 5 lần để ĐÀO SÂU từ TRIỆU CHỨNG → NGUYÊN NHÂN GỐC RỄ. Đơn giản nhất nhưng mạnh nhất!",
    "meaning": """
<p><strong>Why-Why Analysis (Phân tích Tại sao — còn gọi là 5 Whys)</strong> là phương pháp phân tích ĐƠN GIẢN nhưng CỰC KỲ HIỆU QUẢ, phát triển bởi <strong>Sakichi Toyoda</strong> (người sáng lập Toyota) và là nền tảng của Toyota Production System.</p>
<p><em>Hình dung: Con bạn bị ốm (triệu chứng). Bạn cho uống thuốc hạ sốt → hết sốt → hôm sau SỐT LẠI! → Tại sao? Vì chỉ TRỊ TRIỆU CHỨNG (sốt) mà không trị NGUYÊN NHÂN (viêm họng)! Why-Why = đào sâu đến NGUYÊN NHÂN GỐC → trị GỐC → KHÔNG TÁI PHÁT!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 5 quy tắc VÀNG khi làm Why-Why</div>
    <p><strong>1. Mỗi "Tại sao?" phải dựa trên SỰ THẬT</strong> — không đoán mò! Nếu không chắc → ĐI XÁC NHẬN (Genba!) trước khi tiếp tục!<br>
    <strong>2. Nguyên nhân phải ACTIONABLE</strong> — "Do thời tiết" = KHÔNG actionable! "Do seal bị hở" = ACTIONABLE (sửa được!)<br>
    <strong>3. Hỏi "Tại sao?" hệ thống/quy trình</strong> — KHÔNG đổ lỗi người! "Do anh A cẩu thả" = SAI! "Do SOP không rõ ràng" = ĐÚNG! (Sửa SOP = ngăn TẤT CẢ nhân viên sai!)<br>
    <strong>4. Dừng khi đạt nguyên nhân có thể NGĂN CHẶN</strong> — Nếu hỏi quá sâu: "Tại sao lỗi?" → "Tại sao có nhà máy?" → "Tại sao có loài người?" = VÔ NGHĨA!<br>
    <strong>5. Một vấn đề = NHIỀU nhánh</strong> — 1 Why → có thể 2-3 câu trả lời → CHIA NHÁNH → phân tích TỪNG nhánh!<br><br>
    <em>"5" Whys chỉ là con số THAM KHẢO! Có thể 3 Whys đã đủ, có thể cần 7 Whys!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Tìm NGUYÊN NHÂN GỐC RỄ (root cause) thay vì chỉ xử lý TRIỆU CHỨNG → ngăn vấn đề TÁI PHÁT!</li>
    <li>ĐƠN GIẢN + DỄ HỌC: AI CŨNG LÀM ĐƯỢC! Operator, kỹ thuật viên, manager → tất cả đều dùng 5 Whys!</li>
    <li>Phương pháp NHANH: Họp 15-30 phút → có root cause → có countermeasure! (Không cần Minitab, Excel phức tạp!)</li>
    <li>Thay đổi TƯ DUY tổ chức: Từ "ai sai?" → "TẠI SAO hệ thống cho phép sai?" → văn hóa CẢI TIẾN thay vì ĐỔ LỖI!</li>
    <li>LÀ NỀN TẢNG cho tất cả phương pháp phân tích khác: WWBLA, FMEA, 8D, A3... đều BẮT ĐẦU từ Why-Why!</li>
    <li>Áp dụng MỌI NƠI: Sản xuất, chất lượng, an toàn, logistics, IT, HR, tài chính... bất kỳ vấn đề nào cũng dùng được!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: MÔ TẢ vấn đề CỤ THỂ — "Cái gì? Khi nào? Bao nhiêu?"</div>
        <div class="step-card__desc">Viết RÕ vấn đề bằng SỐ LIỆU: ❌ SAI: "Máy hay hỏng" (mơ hồ! máy nào? bao lâu? ảnh hưởng gì?). ✅ ĐÚNG: "Pellet Mill #3 dừng do bearing cháy ngày 5/3/2025, downtime 8 giờ, mất 40 tấn sản phẩm = 200 triệu VND." Dùng 5W: What (Cái gì xảy ra?), When (Khi nào?), Where (Ở đâu?), Who (Ai phát hiện?), How much (Thiệt hại bao nhiêu?). CHỤP ẢNH hiện trường! Thu thập DỮ LIỆU TRƯỚC KHI phân tích!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Hỏi "TẠI SAO?" liên tục — MỖI bước = SỰ THẬT + BẰNG CHỨNG!</div>
        <div class="step-card__desc">Vấn đề → TẠI SAO? → Nguyên nhân 1 → TẠI SAO? → Nguyên nhân 2 → TẠI SAO?... MỖI câu trả lời PHẢI có BẰNG CHỨNG: "Bearing cháy" → Bằng chứng? → XEM bearing: vết cháy, mảnh sắt → CONFIRMED! "Thiếu dầu" → Bằng chứng? → Kiểm tra grease: khô, cứng, đen → CONFIRMED! NẾU không có bằng chứng → GHI CHÚ "cần xác nhận" → ĐI XÁC NHẬN trước khi tiếp! Nếu 1 bước có NHIỀU câu trả lời → CHIA NHÁNH → phân tích TẤT CẢ nhánh! Ưu tiên nhánh có BẰNG CHỨNG mạnh nhất!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xác định NGUYÊN NHÂN GỐC — 3 tiêu chí kiểm tra!</div>
        <div class="step-card__desc">Nguyên nhân gốc phải thỏa MÃN 3 tiêu chí: ✅ <strong>ACTIONABLE</strong> (có thể hành động): "Seal hở" → sửa/thay seal = actionable! "Do số mệnh" = KHÔNG actionable! ✅ <strong>PREVENTABLE</strong> (có thể ngăn ngừa): Khi sửa root cause → vấn đề SẼKHÔNG tái phát! ✅ <strong>WITHIN CONTROL</strong> (trong tầm kiểm soát): "Giá dầu tăng" = ngoài tầm kiểm soát! "PM schedule quá dài" = trong tầm! NẾU "sửa root cause rồi mà vẫn tái phát" → ROOT CAUSE SAI → tìm lại!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: COUNTERMEASURE + FOLLOW-UP — Sửa + Kiểm tra!</div>
        <div class="step-card__desc">Cho MỖI root cause → đề xuất countermeasure: <strong>Immediate (ngay)</strong>: Sửa lỗi hiện tại → ngăn ảnh hưởng ngay! <strong>Preventive (phòng ngừa)</strong>: Sửa hệ thống/quy trình → ngăn TÁI PHÁT! <strong>Systemic (hệ thống)</strong>: Thay đổi culture/management → HORIZONTAL DEPLOYMENT (áp dụng cho thiết bị/quy trình tương tự!) Follow-up sau 1-3 tháng: Vấn đề có TÁI PHÁT không? Nếu TÁI PHÁT → Root cause CHƯA ĐÚNG → làm lại! Ghi thành OPL (One Point Lesson) → chia sẻ bài học cho TOÀN NHÀ MÁY!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Bearing cháy = SỬA bearing? SAI! 5 Why → Gốc = PM schedule quá dài!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Pellet Mill #3 — Bearing trục chính CHÁY! Downtime 8 giờ, mất 40 tấn = 200 triệu VND. Team sửa: thay bearing mới → XONG? Chưa! 3 tháng sau → CHÁY LẠI! → Why-Why!",
            "analysis": "5 Whys — Bearing cháy Pellet Mill:\n\n• Why 1: Tại sao bearing cháy?\n→ Thiếu mỡ bôi trơn → metal-to-metal contact → nhiệt tăng → cháy!\n📊 Bằng chứng: Xem bearing cũ: vết cháy xanh + mỡ khô cứng đen\n\n• Why 2: Tại sao thiếu mỡ?\n→ Grease lịch bơm mỡ 3 tháng/lần → QUÁ DÀI! Bearing pellet mill = điều kiện KHÓ (nóng, bụi, tải nặng) → mỡ HẾT sau 6 tuần!\n📊 Bằng chứng: Xem lịch PM → bơm mỡ 3 tháng. Xem spec bearing → recommend greasing mỗi 4-6 tuần cho điều kiện nặng!\n\n• Why 3: Tại sao lịch bơm mỡ 3 tháng?\n→ Lịch PM COPY từ máy cũ (máy cũ tải NHẸ hơn!) → không điều chỉnh cho máy mới tải NẶNG hơn!\n\n• Why 4: Tại sao copy mà không điều chỉnh?\n→ KHÔNG CÓ QUY TRÌNH review PM checklist khi đưa thiết bị mới vào!\n\n→ ROOT CAUSE: Không có quy trình review + customize PM checklist cho thiết bị mới!\n(KHÔNG PHẢI \"thay bearing mới\" = countermeasure! Đó chỉ là SỬA TRIỆU CHỨNG!)",
            "result": "Countermeasure 3 tầng:\n\n• Immediate: Bơm mỡ bearing pellet mill NGAY! + Rút lịch bơm mỡ từ 3 tháng → 6 tuần (theo spec manufacturer!)\n• Preventive: SOP mới: Khi đưa thiết bị mới vào → PHẢI review manufacturer recommendation → Customize PM checklist theo điều kiện THỰC TẾ (tải, nhiệt, bụi, tốc độ)\n• Systemic (Horizontal Deployment): Review PM checklist cho TẤT CẢ 5 pellet mills! → Phát hiện: Mill #1 và #5 cũng lịch sai → SỬA LUÔN!\n\nKết quả 12 tháng: Bearing failure 4 lần/năm → 0 lần! Tiết kiệm 800 triệu/năm!\n\n→ Bài học Why-Why: \"Bearing cháy → thay bearing\" = SỬA TRIỆU CHỨNG → sẽ CHÁY LẠI! Why-Why → PМ schedule sai → SỬA SCHEDULE → KHÔNG BAO GIỜ CHÁY NỮA!"
        },
        {
            "title": "Giao hàng trễ 15% — Gốc = nhân viên mới skip barcode scan!",
            "industry": "E-commerce / Logistics",
            "situation": "Tỷ lệ giao hàng trễ tăng 5% → 15% trong 2 tháng. Customer complaint bùng nổ! BGĐ hỏi: \"Bộ phận giao hàng làm gì vậy?\" → Why-Why phân tích!",
            "analysis": "5 Whys — Giao hàng trễ:\n\n• Why 1: Tại sao giao trễ?\n→ Picking chậm → đơn hàng không ra kịp cutoff time → trễ!\n📊 Bằng chứng: Picking time tăng từ 3 phút → 8 phút/đơn\n\n• Why 2: Tại sao picking chậm?\n→ Hàng không đúng vị trí trong kho! Picker đi tìm → mất thời gian!\n📊 Bằng chứng: Location accuracy giảm từ 98% → 82%!\n\n• Why 3: Tại sao hàng không đúng vị trí?\n→ Putaway (nhập kho) sai location → đặt A-01 nhưng scan B-15!\n📊 Bằng chứng: 23% đơn putaway tuần qua có location mismatch!\n\n• Why 4: Tại sao putaway sai?\n→ Nhân viên mới SKIPBARCODE SCAN → đặt hàng ĐẠI → không xác nhận location!\n📊 Bằng chứng: WMS log → 90% sai location = 3 nhân viên mới (Why 5: Tại sao skip scan?\n→ Chưa được TRAINING đầy đủ + WMS CHO PHÉP skip scan (không bắt buộc!) + Buddy system không có!",
            "result": "Countermeasure:\n\n• Immediate: Kiểm tra + sửa location cho 2,000 SKU sai → Location accuracy → 95%\n• Preventive:\nWMS system force scan: KHÔNG cho phép skip barcode! Putaway bắt buộc: Scan hàng → Scan location → Confirm → Nếu sai → BLOCK!\nTraining mandatory 3 ngày: Nhân viên mới PHẢI pass test WMS trước khi vào kho!\nBuddy system: Nhân viên mới → đi kèm senior 2 tuần đầu!\n• Systemic: Onboarding SOP cho TẤT CẢ vị trí kho → training → test → buddy → solo\n\nKết quả: Giao trễ 15% → 4% (tốt hơn cả trước khi tăng nhân viên mới!)\n\n→ Bài học Why-Why: Tưởng \"giao hàng trễ\" = lỗi shipper? Why-Why → lỗi PUTAWAY → lỗi NHÂN VIÊN MỚI SKIP SCAN → lỗi HỆ THỐNG cho phép skip! → SỬA HỆ THỐNG (force scan) → không ai có thể skip → HẾT LỖI!"
        },
        {
            "title": "Motor quá nhiệt 95°C — 5 Why chỉ cần 3 bước = lưới bảo vệ bám bụi!",
            "industry": "Hóa chất",
            "situation": "Motor bơm hóa chất chạy nóng 95°C (tiêu chuẩn < 80°C). Dòng điện BÌNH THƯỜNG! Team tưởng phải thay motor mới (60 triệu!) → Why-Why TRƯỚC KHI thay!",
            "analysis": "3 Whys — Motor quá nhiệt (chỉ cần 3!):\n\n• Why 1: Tại sao motor nóng 95°C?\n→ Quạt làm mát motor thổi YẾU → không tản nhiệt đủ!\n📊 Bằng chứng: SỜ gió từ quạt phía sau motor → yếu hơn bình thường rõ rệt (3 GEN!)\n\n• Why 2: Tại sao quạt thổi yếu?\n→ Lưới bảo vệ quạt bị bám BỤI kín 70%! → gió không qua lưới được!\n📊 Bằng chứng: NHÌN: lưới bẩn bám bụi dày 1cm. SỜ: bụi dính cứng!\n\n• Why 3: Tại sao lưới bám bụi?\n→ PM checklist KHÔNG CÓ mục \"vệ sinh lưới quạt motor\"! → Không ai vệ sinh → bụi tích tụ 2 năm!\n\n→ ROOT CAUSE: PM checklist thiếu mục vệ sinh lưới quạt motor!\n→ Chỉ cần 3 Whys! KHÔNG CẦN 5! (Dừng khi đạt actionable root cause!)",
            "result": "Countermeasure:\n\n• Immediate: Vệ sinh lưới bảo vệ + thay quạt (cánh cũ bị mòn do bụi) → TỔNG: 2 triệu VND! (so với \"thay motor 60 triệu\"!) → Motor temp giảm về 72°C!\n• Preventive: Thêm mục \"Vệ sinh lưới quạt motor\" vào PM checklist HÀNG THÁNG!\n• Horizontal Deployment: Kiểm tra TẤT CẢ 30 motor nhà máy → phát hiện 8 motor CŨNG bị bụi kín lưới → VỆ SINH HẾT!\n\nKết quả: 0 motor quá nhiệt! Tiết kiệm: 8 motor × 60 triệu = 480 triệu (nếu \"thay motor\" thay vì \"vệ sinh 2 triệu\"!)\n\n→ Bài học Why-Why: Tưởng motor hỏng → thay 60 triệu? 3 Whys + 3 GEN = phát hiện lưới bẩn → vệ sinh 2 triệu → XONG! Why-Why = TIẾT KIỆM 58 TRIỆU trong 15 phút!"
        },
        {
            "title": "Turnover 25%/năm — 5 Why: Tưởng lương? Gốc = không career path!",
            "industry": "Sản xuất",
            "situation": "Turnover rate công nhân sản xuất 25%/năm → lúc nào cũng thiếu người → training liên tục → chất lượng biến động! BGĐ nói: \"Tăng lương đi!\" → Nhưng tăng lương RỒI → vẫn nghỉ!",
            "analysis": "5 Whys — Turnover cao (ĐA NHÁNH!):\n\n• Why 1: Tại sao turnover 25%?\n→ Nhân viên KHÔNG HÀI LÒNG → nghỉ việc!\n\n• Why 2: Tại sao không hài lòng? → 3 NHÁNH!\nNhánh A: Lương thấp hơn thị trường 15%\nNhánh B: Không có CAREER PATH (đường thăng tiến)\nNhánh C: Môi trường làm việc nóng bức, bụi\n\n• Why 3: WHY cho từng nhánh:\nNhánh A: Tại sao lương thấp hơn? → Benchmark lương chưa cập nhật 3 năm\nNhánh B: Tại sao không career path? → KHÔNG CÓ skill matrix + job ladder → operator làm 5 năm vẫn = nhân viên mới!\nNhánh C: Tại sao nóng bụi? → Hệ thống thông gió CŨ + không có quạt công nghiệp\n\nKiểm tra: Nhánh nào là ROOT?\n• Công ty NTR gần đó tăng lương 20% → nhân viên vẫn nghỉ 18% → Lương KHÔNG PHẢI root duy nhất!\n• Phỏng vấn 50 nhân viên nghỉ: \"Không thấy tương lai\" (65%) > \"Lương thấp\" (45%) > \"Nóng bụi\" (20%)\n→ ROOT CAUSE CHÍNH: Không có career path + skill matrix! (Lương là yếu tố phụ!)",
            "result": "Countermeasure — Career Ladder System:\n\n• Nhánh B (Career — ROOT!):\nSkill Matrix 5 cấp: Level 1 (Trainee) → Level 2 (Operator) → Level 3 (Senior Operator) → Level 4 (Team Leader) → Level 5 (Supervisor)\nMỗi level: Kỹ năng cần có + thời gian tối thiểu + lương tương ứng\n→ Operator THẤY CON ĐƯỜNG phát triển → MỤC TIÊU rõ ràng → MUỐN Ở LẠI!\n\n• Nhánh A (Lương): Benchmark lại → điều chỉnh competitive → +8%\n• Nhánh C (Môi trường): Lắp quạt công nghiệp + mái thông gió → giảm 5°C\n\nKết quả 12 tháng: Turnover 25% → 10%! Tiết kiệm chi phí tuyển dụng + training: 500 triệu/năm!\n\n→ Bài học Why-Why đa nhánh: BGĐ tưởng \"tăng lương\" = giải quyết! Why-Why phát hiện 3 nhánh → phỏng vấn 50 người → career path mới là ROOT! Nếu chỉ tăng lương → turnover vẫn 18%! Phải sửa career path → turnover 10%!"
        },
        {
            "title": "Rò rỉ khí nén 30% — 5 Why: Gốc = KHÔNG AI chịu trách nhiệm KPI energy!",
            "industry": "Sản xuất",
            "situation": "Hệ thống khí nén mất 30% lưu lượng do rò rỉ! Máy nén chạy thêm 1 ca → tốn 200 triệu/năm! Maintenance nói \"cần mua thêm compressor\" (500 triệu!). Why-Why TRƯỚC KHI MUA!",
            "analysis": "5 Whys — Rò rỉ khí nén:\n\n• Why 1: Tại sao rò rỉ 30%?\n→ 12 điểm rò rỉ trên đường ống + fitting + coupling cũ!\n📊 Bằng chứng: 3 GEN → NGHE xì ở 12 vị trí → đánh dấu sơn đỏ!\n\n• Why 2: Tại sao 12 điểm rò?\n→ Joints và fittings CŨ + hỏng → 3 coupling nứt, 5 quick-connector mòn, 4 gasket hở!\n📊 Bằng chứng: Tháo ra → nứt, mòn, biến dạng!\n\n• Why 3: Tại sao không phát hiện và sửa SỚM?\n→ Không có chương trình leak detection! Không ai đi kiểm tra rò rỉ → rò bao lâu cũng không biết!\n\n• Why 4: Tại sao không có leak detection?\n→ Không ai CHỊU TRÁCH NHIỆM compressed air! Production xài → Maintenance sửa máy nén → KHÔNG AI quản lý ĐƯỜNG ỐNG + RÒ RỈ!\n\n• Why 5: Tại sao không ai chịu trách nhiệm?\n→ KPI energy KHÔNG GẮN với maintenance team! → Rò rỉ = lãng phí ENERGY → nhưng maintenance không có KPI energy → KHÔNG QUAN TÂM!",
            "result": "Countermeasure — Từ KPI đến Leak Survey!:\n\n• Immediate: Sửa 12 điểm rò → áp suất phục hồi 6.8 bar (từ 5.5) → compressor chạy 65% tải (từ 100%) → KHÔNG CẦN MUA MÁY NÉN MỚI! Tiết kiệm 500 triệu CAPEX!\n• Preventive:\nGiao KPI energy cho Maintenance: SEC (Specific Energy Consumption) compressed air → kWh/m³ → nếu tăng → có rò rỉ → PHẢI kiểm tra!\nUltrasonic leak survey HÀNG QUÝ: Dùng máy đo siêu âm → phát hiện rò rỉ NGAY CẢ khi nhỏ (tai người không nghe được!) → sửa ngay!\nTag system: Phát hiện rò → dán tag đỏ → sửa trong 7 ngày → xác nhận → bóc tag\n\nKết quả: Rò rỉ 30% → 8%! Tiết kiệm 200 triệu/năm tiền điện! + 500 triệu không cần mua máy nén!\n\n→ Bài học Why-Why + Management: Tưởng \"mua thêm máy nén\" = giải quyết? Why-Why → Gốc = KHÔNG AI chịu trách nhiệm → KPI energy thiếu → không detect leak → rò rỉ tích tụ → thiếu áp → tưởng thiếu máy! SỬA ROOT (KPI + leak survey) → tiết kiệm 700 triệu!"
        },
        {
            "title": "In offset waste 12% — 5 Why: Heater hỏng 2 tháng → ink viscosity dao động!",
            "industry": "In ấn",
            "situation": "Waste paper rate tăng 5% → 12% trên máy in 4 màu! Tốn thêm 500 triệu/năm giấy! Operator điều chỉnh suốt ngày → VẪN LỆCH MÀU! Why-Why!",
            "analysis": "5 Whys — Waste in cao:\n\n• Why 1: Tại sao waste 12%?\n→ Color mismatch (lệch màu) giữa 4 đơn vị in → phải chỉnh → giấy bỏ!\n📊 Bằng chứng: QC report → 80% waste do lệch màu → color variation > spec!\n\n• Why 2: Tại sao lệch màu?\n→ Ink viscosity KHÔNG ỔN ĐỊNH! Đầu ca viscosity OK → 2 giờ sau viscosity thay đổi → màu lệch!\n📊 Bằng chứng: Đo viscosity mỗi 30 phút → biến động ±15% (spec ±3%)!\n\n• Why 3: Tại sao viscosity không ổn định?\n→ Ink fountain (máng mực) không có TEMPERATURE CONTROL! Nhiệt mực thay đổi theo nhiệt nhà xưởng → viscosity thay đổi theo!\n📊 Bằng chứng: Nhiệt mực sáng 25°C → trưa 35°C → chiều 30°C! (Correlation r=0.92 giữa temp và viscosity!)\n\n• Why 4: Tại sao không temperature control?\n→ Heater/chiller ink fountain HỎNG 2 tháng rồi! Chưa sửa vì spare part chờ nhập!\n\n• Why 5: Tại sao 2 tháng chưa sửa?\n→ Spare part không có trong kho + không có critical spare list!",
            "result": "Countermeasure:\n\n• Immediate: Sửa heater GẤP! (mượn heater từ máy khác trong lúc chờ spare) → nhiệt mực ổn định 28±1°C → viscosity ổn → waste GIẢM NGAY từ 12% → 5%!\n• Preventive:\nCritical spare part list: Liệt kê TẤT CẢ spare part critical → DUY TRÌ stock tối thiểu → heater = critical → phải có 1 cái trong kho LUÔN!\nInk viscosity check SOP: Mỗi 30 phút đo viscosity → nếu OUT → điều chỉnh NGAY → KHÔNG ĐỢI lệch màu mới sửa!\n• Systemic: Review tất cả máy in → lập critical spare list cho từng máy → safety stock → KHÔNG BAO GIỜ thiếu spare critical!\n\nKết quả: Waste 12% → 4%! Tiết kiệm 400 triệu/năm giấy! Ink consumption cũng giảm 8%!\n\n→ Bài học Why-Why: Operator cố gắng chỉnh màu → TRIỆU CHỨNG! Why-Why tìm GỐC: heater hỏng → temp dao động → viscosity dao động → lệch màu! Sửa heater = SỬA GỐC → waste giảm 67%!"
        }
    ]
}
