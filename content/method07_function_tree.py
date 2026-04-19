method = {
    "id": 7,
    "title": "Function Tree Analysis - Phân tích cây chức năng",
    "short_name": "Function Tree Analysis",
    "icon": "🏗️",
    "pillar": "Overview",
    "description": "Phân rã hệ thống thành cây chức năng: Máy này LÀM GÌ? Để làm việc đó cần CHỨC NĂNG CON nào? → Hiểu máy TỪ TỔNG THỂ đến CHI TIẾT.",
    "meaning": """
<p><strong>Function Tree Analysis (Phân tích cây chức năng)</strong> là phương pháp PHÂN RÃ (decomposition) một hệ thống phức tạp thành các chức năng con (sub-functions) theo cấu trúc CÂY PHÂN CẤP — từ tổng thể đến chi tiết.</p>
<p><em>Hình dung: Giống sơ đồ tổ chức công ty — Tổng GĐ (chức năng tổng) → Phó GĐ các mảng → Trưởng phòng → Nhân viên. Tương tự: Máy (chức năng tổng) → Hệ thống con → Cụm chi tiết → Chi tiết.</em></p>
<p>Trả lời 2 câu hỏi then chốt: <em>"Hệ thống này LÀM GÌ?"</em> và <em>"Để thực hiện chức năng X, cần những chức năng CON nào?"</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Nguyên tắc MECE — Không trùng, không sót</div>
    <p><strong>MECE = Mutually Exclusive, Collectively Exhaustive</strong><br>
    (Loại trừ lẫn nhau, Bao phủ đầy đủ)<br><br>
    <strong>Mutually Exclusive (Loại trừ lẫn nhau)</strong>: Các chức năng con KHÔNG TRÙNG LẶP — mỗi chức năng chỉ thuộc về 1 nhánh<br>
    <strong>Collectively Exhaustive (Bao phủ đầy đủ)</strong>: Tổng các chức năng con = ĐẦY ĐỦ chức năng cha — không thiếu, không bỏ sót<br><br>
    <em>Ví dụ SAI (trùng lặp): F1: Ép viên, F2: Quay die → F2 NẰM TRONG F1! Không MECE!</em><br>
    <em>Ví dụ ĐÚNG (MECE): F1: Cấp liệu, F2: Conditioning, F3: Ép, F4: Cắt, F5: Làm mát → Không trùng, đầy đủ!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>HIỂU RÕ cấu trúc máy/hệ thống phức tạp — KTV mới đọc Function Tree = hiểu máy NGAY, không cần vận hành 6 tháng</li>
    <li>Làm CƠ SỞ cho FMEA (method 4), FTA (method 5), RCM (method 41) — phải biết máy CÓ GÌ trước khi phân tích hỏng!</li>
    <li>Xác định chức năng CRITICAL (quan trọng) → PM tập trung vào chức năng critical → hiệu quả hơn PM theo danh sách linh kiện!</li>
    <li>Hỗ trợ THIẾT KẾ hệ thống mới — Function Tree = "bản thiết kế chức năng" trước khi thiết kế cơ khí/điện</li>
    <li>Tạo TÀI LIỆU ĐÀO TẠO có cấu trúc — dạy máy từ tổng thể → chi tiết, dễ hiểu hơn dạy từng bộ phận rời rạc</li>
    <li>Phân công TRÁCH NHIỆM bảo trì rõ ràng: Team A chịu F1-F2, Team B chịu F3-F4 → không bỏ sót, không trùng lặp</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định CHỨC NĂNG TỔNG THỂ (Top-level Function)</div>
        <div class="step-card__desc">Viết câu: "[Hệ thống] LÀM GÌ?" → Đó là chức năng tổng thể (F0). Viết dưới dạng ĐỘNG TỪ + DANH TỪ. Ví dụ: Pellet Mill → F0: "Ép viên thức ăn chăn nuôi ở 40 T/h, PDI > 92%, nhiệt viên < 80°C". Bao gồm TIÊU CHUẨN ĐO LƯỜNG (tốc độ, chất lượng, an toàn) — chức năng phải ĐO ĐƯỢC!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: PHÂN RÃ thành chức năng con — Hỏi "CẦN GÌ?"</div>
        <div class="step-card__desc">Với F0, hỏi: "Để thực hiện F0, cần CHỨC NĂNG CON nào?" → Liệt kê F1, F2, F3... → Viết dưới dạng ĐỘNG TỪ + DANH TỪ. Tiếp tục: Với mỗi F1, hỏi lại: "Để thực hiện F1, cần gì?" → F1.1, F1.2... Thường phân rã 3-4 cấp là đủ chi tiết. Dừng khi đến mức có thể: GÁN PM task, hiểu cơ chế hỏng, hoặc xác định component cần bảo trì. Tuân thủ MECE: Không trùng, không sót!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xác định MỐI QUAN HỆ + Input/Output</div>
        <div class="step-card__desc">Cho mỗi chức năng: Input (đầu vào) là gì? Output (đầu ra) là gì? Phụ thuộc (dependency) vào chức năng nào? Ví dụ: F3: Ép viên → Input: Bột đã conditioning (từ F2). Output: Viên cám nóng (sang F5: Làm mát). Dependency: F2 phải chạy TRƯỚC F3. → Hiểu dòng chảy qua các chức năng!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Phân loại CRITICAL / IMPORTANT / SUPPORT</div>
        <div class="step-card__desc"><strong>Critical (Quan trọng)</strong>: Mất chức năng = MẤT SẢN XUẤT hoặc AN TOÀN bị đe dọa → PM ưu tiên cao nhất! <strong>Important (Quan trọng vừa)</strong>: Mất chức năng = GIẢM sản lượng/chất lượng nhưng CHƯA DỪNG → PM trung bình. <strong>Support (Hỗ trợ)</strong>: Mất chức năng = bất tiện nhưng SX vẫn tiếp tục → PM thấp, sửa khi hỏng cũng OK. → Tập trung 80% nguồn lực PM cho chức năng CRITICAL!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Pellet Mill — 5 chức năng chính, 23 chức năng con, 8 Critical!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Cần xây dựng PM plan (Planned Maintenance) cho Pellet Mill. Nhưng máy phức tạp — bắt đầu từ đâu? → Vẽ Function Tree trước!",
            "analysis": "Cây chức năng Pellet Mill:\n\nF0: Ép viên thức ăn chăn nuôi (40 T/h, PDI > 92%)\n├── F1: Cấp liệu (Feed) → Đưa bột vào buồng ép đều đặn\n│   ├── F1.1: Kiểm soát lưu lượng (Feeder screw + VFD — biến tần)\n│   └── F1.2: Phân phối đều (Spreading — trải đều trên die)\n├── F2: Conditioning (Hấp hơi) → Thêm hơi nước + nhiệt để bột mềm + dính\n│   ├── F2.1: Cấp steam (Steam valve + pressure control)\n│   ├── F2.2: Trộn đều steam (Conditioner mixer paddle)\n│   └── F2.3: Kiểm soát nhiệt độ (Temperature sensor + control)\n├── F3: Ép viên (Compression) ★CRITICAL★\n│   ├── F3.1: Quay die (Main motor + gearbox + shaft)\n│   ├── F3.2: Ép qua lỗ die (Roller + die gap control)\n│   └── F3.3: Bôi trơn (Lubrication — bearings, gears)\n├── F4: Cắt viên (Cut) → Cắt viên đúng chiều dài\n│   └── F4.1: Dao cắt (Knife + adjustment)\n└── F5: Làm mát (Cooling) → Giảm nhiệt viên < 80°C\n├── F5.1: Quạt hút (Cooling fan + duct)\n└── F5.2: Xả viên (Discharge gate + level sensor)",
            "result": "Phân loại Critical/Important/Support:\n\n| Chức năng | Loại | Lý do | PM Level |\n| F3: Ép viên | CRITICAL | Mất = DỪNG SX hoàn toàn! | PM hàng tuần |\n| F2: Conditioning | CRITICAL | Steam sai = PDI giảm → chất lượng! | PM hàng tuần |\n| F1: Cấp liệu | Important | Mất = dừng, nhưng ít hỏng | PM hàng tháng |\n| F5: Làm mát | Important | Viên nóng nhưng vẫn SX được | PM hàng tháng |\n| F4: Cắt viên | Support | Dao cùn = viên dài hơn, chưa dừng | PM khi cần |\n\n→ Tổng: 23 chức năng con, 8 chức năng Critical → PM plan TẬP TRUNG vào 8 chức năng này!\n→ Bài học: Function Tree = BẢN ĐỒ máy! Có bản đồ → đi PM ĐÚNG CHỖ, không lạc đường!"
        },
        {
            "title": "Hệ thống khí nén nhà máy — Compressor Critical, rò rỉ = mất 30%!",
            "industry": "Sản xuất chung",
            "situation": "Hệ thống khí nén 10 bar phục vụ TOÀN nhà máy (pneumatic valve, tool, cylinder). Thường xuyên thiếu khí → máy hoạt động chậm. Cần Function Tree để phân tích và cải tiến.",
            "analysis": "Cây chức năng hệ thống khí nén:\n\nF0: Cung cấp khí nén 10 bar, 100 cfm, sạch & khô cho sản xuất\n├── F1: Nén khí (Compression) ★CRITICAL★\n│   ├── F1.1: Hút khí (Intake filter + inlet valve)\n│   ├── F1.2: Nén (Screw compressor + motor 75kW)\n│   └── F1.3: Làm mát sau nén (Aftercooler → giảm nhiệt khí nén)\n├── F2: Xử lý khí (Air Treatment) ★CRITICAL★\n│   ├── F2.1: Tách nước (Moisture separator)\n│   ├── F2.2: Sấy khô (Refrigerated dryer → dewpoint -20°C)\n│   └── F2.3: Lọc (Particulate filter + Coalescing filter → lọc dầu và bụi)\n├── F3: Lưu trữ (Storage)\n│   └── F3.1: Bình chứa (Air receiver 3000L → đệm áp suất)\n├── F4: Phân phối (Distribution)\n│   ├── F4.1: Ống chính (Header pipe + branch)\n│   ├── F4.2: FRL tại máy (Filter-Regulator-Lubricator)\n│   └── F4.3: Van phân phối (Solenoid valves, cylinders)\n└── F5: Điều khiển & Giám sát\n├── F5.1: Pressure switch (on/off compressor)\n└── F5.2: Áp kế (pressure gauge tại FRL)",
            "result": "Phân tích theo Function Tree phát hiện vấn đề:\n\nF4: Phân phối → RÒ RỈ = LÃNG PHÍ LỚN NHẤT!\n• Kiểm tra ống bằng ultrasonic leak detector (dò rò rỉ siêu âm) → Phát hiện 47 điểm rò rỉ!\n• Tổng rò rỉ = 30% lượng khí nén! = Compressor chạy 30% để... XẢ RA NGOÀI TRỜI!\n• Chi phí: 30% × 75kW × 8,760h × 2,000 VND/kWh = 394 triệu/năm LÃM PHÍ!\n\nAction theo Function Tree:\n• F4 (Phân phối): Sửa 47 điểm rò rỉ → tiết kiệm NGAY 394 triệu/năm!\n• F2 (Xử lý): Thay filter đúng lịch (3 tháng) → khí sạch → giảm hỏng van\n• F1 (Nén): PM compressor → vibration monitoring → tránh breakdown\n\n→ Bài học: Function Tree giúp nhìn TOÀN BỘ hệ thống → phát hiện 30% khí bị RÒ ở F4 — mà trước đây chỉ tập trung PM cho F1 (compressor)!"
        },
        {
            "title": "Hệ thống PCCC — Mỗi chức năng là 1 lớp bảo vệ tính mạng!",
            "industry": "An toàn",
            "situation": "Nhà máy cần kiểm tra toàn bộ hệ thống PCCC (Phòng cháy chữa cháy) để đảm bảo compliance (tuân thủ). Hệ thống phức tạp — cần vẽ Function Tree để KHÔNG BỎ SÓT bất kỳ chức năng nào!",
            "analysis": "Cây chức năng PCCC nhà máy:\n\nF0: Bảo vệ con người và tài sản khỏi HỎA HOẠN\n├── F1: PHÁT HIỆN cháy (Detection) ★CRITICAL★\n│   ├── F1.1: Smoke detector (đầu dò khói) — phát hiện khói sớm\n│   ├── F1.2: Heat detector (đầu dò nhiệt) — phát hiện nhiệt bất thường\n│   ├── F1.3: Manual call point (nút bấm báo cháy thủ công)\n│   └── F1.4: Fire alarm panel (tủ trung tâm báo cháy — thu thập tín hiệu)\n├── F2: BÁO ĐỘNG (Notification) ★CRITICAL★\n│   ├── F2.1: Siren + đèn strobe (báo động tại chỗ)\n│   ├── F2.2: Gọi cứu hỏa 114 (tự động hoặc thủ công)\n│   └── F2.3: Thông báo BMS/SCADA (tín hiệu đến phòng điều khiển)\n├── F3: CHỮA CHÁY (Suppression) ★CRITICAL★\n│   ├── F3.1: Sprinkler tự động + Bơm cứu hỏa + Bể nước\n│   ├── F3.2: Bình chữa cháy xách tay (CO2, bột, foam)\n│   └── F3.3: Họng nước + Vòi rồng (standpipe + hose reel)\n├── F4: THOÁT HIỂM (Evacuation) ★CRITICAL★\n│   ├── F4.1: Đèn EXIT (biển thoát hiểm)\n│   ├── F4.2: Emergency lighting (đèn chiếu sáng khẩn cấp — sáng khi mất điện)\n│   └── F4.3: Lối thoát hiểm (cửa, cầu thang, tập kết)\n└── F5: KIỂM SOÁT KHÓI (Smoke Control)\n├── F5.1: Smoke vent (quạt hút khói)\n└── F5.2: Pressurization (quạt tạo áp cầu thang — giữ cầu thang SẠCH KHÓI cho thoát hiểm)",
            "result": "Chuyển Function Tree thành CHECKLIST kiểm tra hàng tháng:\n\n| Chức năng | Kiểm tra gì? | Tần suất | Ai? |\n| F1.1 Smoke detector | Spray test (phun khói giả) → detector BÁO? | Hàng tháng | BT |\n| F1.4 Panel | Kiểm tra LED, battery backup, communication | Hàng tháng | BT |\n| F2.1 Siren | Bấm test → nghe RÕ tại mọi khu vực? | Hàng quý | BT |\n| F3.1 Sprinkler | Flow test (mở van test → nước chảy đủ áp?) | Hàng quý | BT + PCCC |\n| F3.1 Bơm cứu hỏa | Chạy thử (weekly run test) | Hàng tuần | BT |\n| F4.1 EXIT | Đèn sáng đủ? Battery OK? | Hàng tháng | AN TOÀN |\n| F4.3 Lối thoát | KHÔNG CÓ VẬT CẢN? Cửa mở được? | Hàng tuần | AN TOÀN |\n\n→ Bài học: Nếu chỉ kiểm tra \"hệ thống PCCC\" chung chung → DỄ BỎ SÓT (ai đi kiểm tra đèn EXIT? ai test smoke vent?). Function Tree → CHIA NHỎ → mỗi chức năng có NGƯỜI PHỤ TRÁCH + LỊCH cụ thể → 100% compliance!"
        },
        {
            "title": "Dây chuyền đóng chai PET — Filler & Capper = Bottleneck-critical!",
            "industry": "Đồ uống",
            "situation": "Dây chuyền đóng chai nước ngọt PET 20,000 chai/giờ. Cần Function Tree để xây dựng PM plan cho MỖI máy trong dây chuyền.",
            "analysis": "Cây chức năng dây chuyền đóng chai:\n\nF0: Đóng chai nước ngọt PET 20,000 chai/h, đạt tiêu chuẩn ATTP\n├── F1: Thổi chai (Blow Molding):\n│   ├── F1.1: Nung preform (IR heater → làm mềm nhựa PET)\n│   └── F1.2: Thổi chai (Stretch blow → tạo hình chai từ preform)\n├── F2: Rửa chai (Rinser): Rửa chai mới bằng nước sạch/khí\n├── F3: Chiết rót (Filler) ★CRITICAL — BOTTLENECK★\n│   ├── F3.1: Cấp nước (Product supply valve + tank)\n│   ├── F3.2: Chiết (Fill valve × 60 đầu → rót đồng thời 60 chai!)\n│   └── F3.3: Kiểm soát mức (Level control → đảm bảo đúng ml)\n├── F4: Đóng nắp (Capper) ★CRITICAL★\n│   ├── F4.1: Cấp nắp (Cap feeder + sorter)\n│   └── F4.2: Siết nắp (Capping head + torque control)\n├── F5: Dán nhãn (Labeler)\n│   └── F5.1: Quấn nhãn (Shrink sleeve hoặc self-adhesive)\n└── F6: Đóng thùng (Packer)\n├── F6.1: Xếp chai (Tray packer / Shrink wrapper)\n└── F6.2: Dán mã (Inkjet date/lot code)",
            "result": "Phân loại và xây dựng PM:\n\nCRITICAL: F3 (Filler) + F4 (Capper) → Dừng = DÂY CHUYỀN DỪNG!\n• F3.2 (Fill valve): PM hàng tuần — vệ sinh valve, check seal, test fill volume\n• F4.1 (Cap feeder): PM hàng ca — vệ sinh rail, kiểm tra sorting\n• F4.2 (Capping head): PM hàng tuần — kiểm tra torque (siết quá chặt → nắp nứt, quá lỏng → rò rỉ!)\n\nIMPORTANT: F1 (Blow) + F5 (Label) → Giảm chất lượng nhưng có buffer\n• F1.1 (IR heater): PM hàng tháng — kiểm tra đèn IR (PET nung không đều → chai méo)\n\nSUPPORT: F2 (Rinser) + F6.2 (Inkjet) → PM khi cần\n\nTổng: 12 PM tasks ưu tiên cho 2 máy Critical (Filler + Capper)\n→ Bài học: Function Tree biến \"bảo trì dây chuyền 6 máy\" thành \"tập trung 12 tasks cho 2 máy CRITICAL\" → HIỆU QUẢ GẤP 3!"
        },
        {
            "title": "Hệ thống ERP — F6 Hạ tầng là NỀN TẢNG cho mọi module!",
            "industry": "CNTT",
            "situation": "Hệ thống ERP SAP phục vụ toàn công ty. IT cần Function Tree để xây dựng BCP (Business Continuity Plan — kế hoạch liên tục kinh doanh) và phân tích rủi ro.",
            "analysis": "Cây chức năng ERP:\n\nF0: Quản lý toàn bộ hoạt động doanh nghiệp\n├── F1: Tài chính (FI) — Sổ cái, phải trả, phải thu, báo cáo tài chính\n├── F2: Sản xuất (PP) — MRP (Material Requirements Planning — hoạch định NVL), lịch SX, WO (Work Order)\n├── F3: Mua hàng (MM) — PO (Purchase Order), nhập kho, quản lý NCC\n├── F4: Bán hàng (SD) — SO (Sales Order), giao hàng, xuất hóa đơn\n├── F5: Nhân sự (HR) — Lương, chấm công, tuyển dụng\n└── F6: Hạ tầng IT ★CRITICAL — NỀN TẢNG★\n├── F6.1: Server (application + database)\n├── F6.2: Network (LAN, WAN, firewall)\n├── F6.3: Backup (daily backup, DR site)\n└── F6.4: Security (authentication, encryption)\n\nInsight quan trọng: F6 (Hạ tầng) NẰM DƯỚI tất cả module! F1-F5 đều PHỤ THUỘC F6. Nếu F6 DOWN → TẤT CẢ module DOWN → Công ty TÊ LIỆT!",
            "result": "BCP (Business Continuity Plan) dựa trên Function Tree:\n\nF6 CRITICAL → Redundancy ưu tiên tuyệt đối:\n• F6.1 Server: Active-active cluster (2 server chạy song song) → 1 die thì còn 1\n• F6.2 Network: Dual ISP (2 nhà mạng) → 1 đứt thì còn 1\n• F6.3 Backup: Daily backup + DR site (Disaster Recovery — trung tâm khôi phục) tại thành phố khác\n• F6.4 Security: 2FA + Firewall + Penetration test hàng quý\n\nF1-F5: Phân loại RTO (Recovery Time Objective — thời gian phục hồi):\n• F1 Tài chính: RTO 4h (cuối tháng phải chạy!)\n• F2 Sản xuất: RTO 2h (nhà máy không thể dừng!)\n• F4 Bán hàng: RTO 2h (đơn hàng liên tục!)\n• F3 Mua hàng: RTO 8h (mua sắm có thể chờ)\n• F5 Nhân sự: RTO 24h (lương tính cuối tháng)\n\n→ Bài học IT: Function Tree cho IT giúp thấy: KHÔNG phải module nào cũng cần RTO 1h! Phân loại theo Function Tree → đầu tư DR ĐÚNG MỨC!"
        },
        {
            "title": "Wind Turbine 3MW — Gearbox + Pitch chiếm 60% downtime!",
            "industry": "Năng lượng",
            "situation": "Turbine gió 3MW ngoài khơi — chi phí bảo trì RẤT CAO (phải thuê tàu + cẩu ra biển!). Cần Function Tree để xây dựng O&M strategy (chiến lược vận hành & bảo trì) THÔNG MINH → giảm chi phí.",
            "analysis": "Cây chức năng Wind Turbine:\n\nF0: Phát điện 3MW từ năng lượng gió\n├── F1: Thu năng lượng gió (Rotor system)\n│   ├── F1.1: Cánh quạt (Blade × 3) — bắt gió → quay\n│   ├── F1.2: Pitch system (hệ thống xoay cánh) ★CRITICAL★ — điều chỉnh góc cánh theo tốc độ gió\n│   └── F1.3: Hub (trục nối 3 cánh)\n├── F2: Chuyển đổi cơ → điện\n│   ├── F2.1: Gearbox (hộp số tăng tốc) ★CRITICAL★ — tăng tốc từ 15 rpm → 1,500 rpm để phát điện\n│   └── F2.2: Generator (máy phát điện)\n├── F3: Biến đổi điện\n│   ├── F3.1: Converter (biến đổi tần số → hòa lưới)\n│   └── F3.2: Transformer (biến áp tăng áp → truyền tải)\n├── F4: Điều khiển\n│   ├── F4.1: Yaw system (xoay nacelle hướng theo gió)\n│   └── F4.2: SCADA (giám sát + điều khiển từ xa)\n└── F5: Kết cấu\n├── F5.1: Tower (tháp) + Foundation (móng)\n└── F5.2: Nacelle housing (vỏ nacelle — bảo vệ thiết bị)",
            "result": "Phân tích dữ liệu downtime theo Function Tree:\n\nF2.1 Gearbox: 35% tổng downtime! → Hỏng gearbox = thay = cần CẨU lớn = 1 tỷ VND/lần!\nF1.2 Pitch system: 25% tổng downtime! → Pitch motor, bearing, controller hỏng thường xuyên\n→ 2 chức năng = 60% tổng downtime!\n\nO&M Strategy theo Function Tree:\n• F2.1 Gearbox: CM (Condition Monitoring) liên tục — Vibration + Oil particle counter → phát hiện mòn SỚM → lên lịch thay TRƯỚC khi hỏng (planned vs emergency = tiết kiệm 50% chi phí cẩu!)\n• F1.2 Pitch: PM 6 tháng/lần — Grease bearing + test motor + controller firmware update\n• F3, F4, F5: PM hàng năm — Ít hỏng hơn → PM ít thường xuyên hơn → tiết kiệm chi phí tàu\n\nKết quả: Downtime giảm 30% → Thêm 650 MWh/năm = thêm doanh thu 1.3 tỷ VND/năm/turbine!\n→ Bài học: Function Tree + dữ liệu downtime = biết CHÍNH XÁC chỗ nào tốn tiền NHẤT → tập trung CM/PM → ROI cực cao!"
        }
    ]
}
