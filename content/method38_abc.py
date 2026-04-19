method = {
    "id": 38,
    "title": "ABC Analysis - Phân tích phân loại ABC",
    "short_name": "ABC Analysis",
    "icon": "🔤",
    "pillar": "Overview",
    "description": "Phân loại hạng mục thành 3 nhóm A-B-C theo giá trị/tầm quan trọng — tập trung nguồn lực vào nhóm A, đơn giản hóa nhóm C.",
    "meaning": """
<p><strong>ABC Analysis (Phân tích ABC)</strong> dựa trên nguyên tắc Pareto (80/20), phân loại các hạng mục thành 3 nhóm theo GIÁ TRỊ / TẦM QUAN TRỌNG:</p>
<ul>
    <li><strong>Nhóm A — "Ngôi sao" (Quan trọng nhất!)</strong>: Chiếm 10-20% số lượng nhưng chiếm 70-80% GIÁ TRỊ. → Quản lý CHẶT CHẼ NHẤT, theo dõi hàng ngày/tuần</li>
    <li><strong>Nhóm B — "Trung bình"</strong>: Chiếm 20-30% số lượng, 15-25% giá trị. → Quản lý VỪA PHẢI, theo dõi hàng tuần/tháng</li>
    <li><strong>Nhóm C — "Nhiều nhưng nhỏ"</strong>: Chiếm 50-70% số lượng nhưng chỉ 5-10% giá trị. → Quản lý ĐƠN GIẢN, mua theo lô lớn, ít theo dõi</li>
</ul>
<div class="note-box note-box--info">
    <div class="note-title">📌 ABC áp dụng cho MỌI THỨ!</div>
    <p><em>Bất kỳ danh sách nào cần ƯU TIÊN đều dùng abc được!</em><br><br>
    • <strong>Tồn kho NL</strong>: NL nào chiếm nhiều tiền nhất? → Quản lý chặt NL đó<br>
    • <strong>Phụ tùng</strong>: Phụ tùng nào đắt nhất / quan trọng nhất?<br>
    • <strong>Khách hàng</strong>: KH nào mang lại 80% doanh số? → Chăm sóc VIP<br>
    • <strong>Sản phẩm</strong>: Sản phẩm nào mang 80% lợi nhuận?<br>
    • <strong>Lỗi chất lượng</strong>: Lỗi nào gây 80% chi phí chất lượng?<br>
    • <strong>Thiết bị</strong>: Thiết bị nào chiếm 80% chi phí bảo trì?<br>
    → Luôn TẬP TRUNG vào nhóm A trước!</p>
</div>
""",
    "purpose": """
<ul>
    <li>Tập trung NGUỒN LỰC (thời gian, tiền, người) vào hạng mục QUAN TRỌNG NHẤT (nhóm A)</li>
    <li>Tối ưu hóa chính sách quản lý THEO MỨC ĐỘ quan trọng — không quản lý tất cả giống nhau!</li>
    <li>Giảm chi phí quản lý cho nhóm C — ĐỪNG tốn thời gian quản lý chặt những thứ ít giá trị</li>
    <li>Đơn giản hóa quyết định khi số lượng hạng mục LỚN — 200 NL, 500 KH, 800 phụ tùng → chia 3 nhóm → dễ quản lý!</li>
    <li>Kết hợp với nhiều phương pháp khác: Pareto (method 25), Inventory, PM, CBA (method 37)</li>
    <li>Áp dụng phổ quát — MỌI ngành, MỌI phòng ban, MỌI cấp bậc đều dùng được</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Thu thập dữ liệu và tính giá trị</div>
        <div class="step-card__desc">Liệt kê TẤT CẢ items (NL, phụ tùng, khách hàng, sản phẩm...). Tính giá trị mỗi item: Tồn kho = Số lượng × Đơn giá. KH = Doanh số/năm. Lỗi = Tần suất × Chi phí/lần. Sắp xếp giảm dần theo giá trị (cao nhất ở trên).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Tính % tích lũy và phân loại A-B-C</div>
        <div class="step-card__desc">Tính % giá trị của từng item so với tổng. Tính % tích lũy (cumulative %) — cộng dồn từ trên xuống. Phân loại: A = từ 0 đến ~80% tích lũy (những item đầu tiên cộng lại = 80%). B = từ ~80% đến ~95%. C = từ ~95% đến 100%. Vẽ đường cong ABC (trục X = % số lượng items, trục Y = % giá trị tích lũy).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xây dựng CHÍNH SÁCH quản lý KHÁC NHAU cho A, B, C</div>
        <div class="step-card__desc"><strong>Nhóm A</strong>: Kiểm soát CHẶT — review hàng tuần, dự báo chi tiết, safety stock tính chính xác, nhà cung cấp chất lượng nhất. <strong>Nhóm B</strong>: Kiểm soát VỪA — review hàng tháng, reorder point tự động, safety stock vừa phải. <strong>Nhóm C</strong>: Kiểm soát ĐƠN GIẢN — mua theo lô lớn 1-2 lần/năm, hệ thống 2-bin (hết thùng 1 → đặt hàng), không cần dự báo chi tiết.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Review và cập nhật định kỳ</div>
        <div class="step-card__desc">ABC KHÔNG CỐ ĐỊNH — review 6-12 tháng/lần vì giá cả, nhu cầu thay đổi. Items có thể di chuyển giữa nhóm: Sản phẩm B bán chạy bất ngờ → chuyển lên A. NL giá giảm → chuyển từ A xuống B. Xem xét kết hợp ABC-XYZ: X = nhu cầu ổn định, Y = dao động, Z = không dự đoán được → Matrix ABC-XYZ cho chính sách chi tiết hơn.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "ABC tồn kho NL nhà máy TACN — Giải phóng 11 tỷ vốn!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Nhà máy có 200 loại NL, tổng tồn kho 50 tỷ VND. Muốn giảm 20% tồn kho = giải phóng 10 tỷ VND vốn lưu động mà KHÔNG được để thiếu NL dừng máy.",
            "analysis": "Phân loại 200 nguyên liệu:\n\nNhóm A — 15 NL (8% số lượng) = 37.5 tỷ (75% giá trị):\n• Bắp (ngô), Khô đậu nành, Cám gạo, Bột cá (fishmeal), Bột thịt xương...\n• Đặc điểm: Lượng dùng LỚN, giá CAO, biến động giá mạnh → ảnh hưởng 75% chi phí NL!\n\nNhóm B — 35 NL (18%) = 7.5 tỷ (15%):\n• Premix (hỗn hợp vitamin-khoáng), Amino acid (lysine, methionine), Đá vôi (limestone), Dầu cọ...\n\nNhóm C — 150 NL (75% số lượng) = chỉ 5 tỷ (10% giá trị):\n• Phụ gia nhỏ: Vitamin đơn lẻ, chất tạo mùi (flavoring), chất chống mốc, enzyme, màu...\n• 150 loại nhưng tổng giá trị chỉ = 1/7 nhóm A!",
            "result": "Chính sách KHÁC NHAU cho A, B, C:\n\n• Nhóm A: Review HÀNG TUẦN! MRP (tính nhu cầu chính xác theo kế hoạch SX). Safety stock = 7 ngày (tính kỹ dựa trên lead time NCC). Dự báo giá → mua trước khi tăng giá\n• Nhóm B: Review 2 tuần/lần. Reorder point (điểm đặt hàng tự động). Safety stock = 14 ngày\n• Nhóm C: Review tháng/lần. Hệ thống 2-bin (hết thùng 1 → đặt hàng). Safety stock = 30 ngày (mua 1 lần cho 1 tháng)\n\nKết quả: Tồn kho giảm 22% = giải phóng 11 tỷ VND vốn lưu động! Mà KHÔNG thiếu NL lần nào."
        },
        {
            "title": "ABC phụ tùng bảo trì — Hết phụ tùng quan trọng, tồn phụ tùng không ai dùng!",
            "industry": "Sản xuất chung",
            "situation": "800 loại phụ tùng, tồn kho 3 tỷ VND. Vấn đề: Bearing quan trọng → HẾT → máy dừng chờ 3 ngày đặt hàng! Trong khi 300 loại phụ tùng 5 NĂM chưa ai dùng → đọng vốn!",
            "analysis": "Phân loại 800 phụ tùng:\n\nNhóm A — 48 loại (6%) = 2.1 tỷ (70%):\n• Bearing, Motor, Die (khuôn ép viên), Roller (trục lăn), Belt drive (dây curoa lớn)\n• Đặc điểm: Đắt, nếu hết → máy DỪNG, lead time đặt hàng dài (2-4 tuần)\n\nNhóm B — 152 loại (19%) = 600 triệu (20%):\n• Seal, Gasket (ron làm kín), Relay, Sensor, Bơm phụ...\n\nNhóm C — 600 loại (75%) = 300 triệu (10%):\n• Bulong, đai ốc, vòng đệm (washer), dây thít (cable tie), O-ring nhỏ...\n• 600 loại! Tốn rất nhiều thời gian quản lý nhưng tổng giá trị chỉ 300 triệu",
            "result": "Chính sách:\n• Nhóm A (critical spare): Min-Max system — luôn có ÍT NHẤT 2 chiếc dự phòng cho mỗi loại. Review hàng tháng. Đặt hàng TRƯỚC KHI hết (không chờ hết mới đặt!).\n• Nhóm B: Reorder point tự động trong hệ thống — khi còn thấp hơn mức reorder → tự tạo đơn đặt hàng\n• Nhóm C: 2-bin kanban — 2 hộp: hết hộp 1 → đặt hàng 1 lô lớn. Mua theo năm (annual bulk order) → giá rẻ hơn mua lẻ\n• Xử lý tồn cũ: 300 loại > 3 năm không dùng → thanh lý/bán = thu hồi 150 triệu\n\nKết quả: Phụ tùng A KHÔNG BAO GIỜ hết! Giảm 150 triệu vốn đọng trong C!"
        },
        {
            "title": "ABC khách hàng — Chăm sóc đúng người, đúng cách!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "500 khách hàng. Doanh số 1,000 tỷ/năm. Đội kinh doanh 20 người phải phục vụ TẤT CẢ 500 KH → không đủ thời gian chăm sóc KH lớn!",
            "analysis": "Phân loại 500 khách hàng theo doanh số:\n\nNhóm A — 35 KH (7%) = 750 tỷ (75% doanh số!):\n• Đại lý cấp 1, trang trại lớn (>5,000 đầu heo, >50,000 gà)\n• Mỗi KH nhóm A = trung bình 21 tỷ/năm → MẤT 1 KH nhóm A = MẤT 21 tỷ doanh số!\n\nNhóm B — 115 KH (23%) = 200 tỷ (20%):\n• Đại lý cấp 2, trang trại vừa\n\nNhóm C — 350 KH (70%) = chỉ 50 tỷ (5%):\n• Trang trại nhỏ, khách lẻ\n• 350 KH nhưng doanh số trung bình chỉ 143 triệu/KH/năm!\n→ Hiện tại đội sales phải thăm CẢ 350 KH nhỏ → không có thời gian chăm KH lớn!",
            "result": "Chiến lược chăm sóc KHÁC NHAU cho A, B, C:\n\n• Nhóm A: Mỗi KH có account manager RIÊNG. Thăm HÀNG TUẦN. Credit 45 ngày. Ưu tiên giao hàng. Hỗ trợ kỹ thuật trang trại. Ăn trưa/dinner quan hệ\n• Nhóm B: Sales rep chia sẻ (1 người phụ trách 15-20 KH). Thăm 2 tuần/lần. Credit 30 ngày\n• Nhóm C: Telesales (bán qua điện thoại) + đặt hàng online. Credit COD (trả tiền khi giao) hoặc 7 ngày. Không cần sales visit thường xuyên\n\nKết quả: Chi phí bán hàng giảm 20%. KH nhóm A hài lòng hơn (được chăm sóc tốt hơn). Không mất KH lớn."
        },
        {
            "title": "ABC sản phẩm — Loại bỏ sản phẩm LỖ, tăng lợi nhuận 15%!",
            "industry": "Sản xuất chung",
            "situation": "120 SKU (mã sản phẩm). Ban Giám đốc muốn tối ưu danh mục: Giữ sản phẩm nào? Phát triển sản phẩm nào? Loại bỏ sản phẩm nào?",
            "analysis": "Phân loại 120 SKU theo LỢI NHUẬN (không phải doanh số!):\n\nNhóm A — 15 SKU (12.5%) = 80% tổng lợi nhuận:\n• Sản phẩm core (chủ lực) — sản lượng lớn, margin tốt. Đây là \"gà đẻ trứng vàng\" của công ty!\n\nNhóm B — 30 SKU (25%) = 15% lợi nhuận:\n• Ổn định nhưng tăng trưởng thấp\n\nNhóm C — 75 SKU (62.5%) = chỉ 5% lợi nhuận!:\n• Khám phá SỐC: Nhiều sản phẩm nhóm C có MARGIN ÂM (bán ra LỖ!) khi tính đủ chi phí overhead (SX batch nhỏ → changeover tốn thời gian, chi phí đóng gói riêng, quản lý tồn kho phức tạp...)\n• 75 SKU nhưng gây phức tạp cho SX: Changeover nhiều, tồn kho bao bì đa dạng, lập kế hoạch phức tạp",
            "result": "Quyết định cho từng nhóm:\n• Nhóm A — INVEST (đầu tư): Tăng marketing, mở rộng công suất, cải tiến chất lượng. Bảo vệ bằng mọi giá!\n• Nhóm B — MAINTAIN (duy trì): SX hiệu quả, tối ưu chi phí, tìm cách chuyển lên A\n• Nhóm C — REVIEW:\n- 30 SKU margin âm → LOẠI BỎ (sunset): Thông báo KH 3 tháng → chuyển sang SP thay thế\n- 20 SKU margin thấp → TĂNG GIÁ: \"Giá tăng 10% hoặc ngừng SX\" → KH chấp nhận vì không có nhà cung cấp khác\n- 25 SKU giữ lại vì giữ chân KH (customer retention)\n\nKết quả: Lợi nhuận tổng tăng 15%! Giảm 30 SKU → SX đơn giản hơn, ít changeover, ít tồn kho."
        },
        {
            "title": "ABC chi phí bảo trì — Tập trung vào 12 máy chiếm 76% chi phí!",
            "industry": "Sản xuất chung",
            "situation": "120 thiết bị, tổng chi phí bảo trì 5 tỷ/năm. Budget phân bổ ĐỒNG ĐỀU cho tất cả máy → không hiệu quả!",
            "analysis": "Phân loại 120 thiết bị theo chi phí bảo trì:\n\nNhóm A — 12 thiết bị (10%) = 3.8 tỷ (76%!):\n• Pellet Mill #1, #2; Hammer Mill #1; Boiler; Máy đùn (Extruder); Compressor chính\n• Đặc điểm: Máy lớn, chạy liên tục, hỏng → DỪM NHÀ MÁY, sửa rất tốn\n\nNhóm B — 25 thiết bị (21%) = 800 triệu (16%)\n\nNhóm C — 83 thiết bị (69%) = chỉ 400 triệu (8%):\n• Băng tải nhỏ, quạt phụ, bơm dự phòng, van tay...\n→ Hiện tại: PM (bảo trì kế hoạch) giống nhau cho TẤT CẢ 120 máy → lãng phí thời gian KTV cho máy nhóm C ít quan trọng!",
            "result": "Chính sách BT khác nhau:\n• Nhóm A: Phân tích RCM (Reliability Centered Maintenance — xem method 41). CBM (Condition Based Monitoring — giám sát rung, nhiệt). PM plan CHI TIẾT riêng từng máy. Root cause analysis cho MỖI LẦN breakdown\n• Nhóm B: Time-based PM (bảo trì theo chu kỳ thời gian) — đủ tốt\n• Nhóm C: Run-to-failure (chạy đến khi hỏng → thay mới) — chấp nhận được vì máy rẻ, không critical\n\nKết quả: Chi phí BT giảm 25%! Tập trung 80% nỗ lực KTV vào 12 máy nhóm A → reliability tăng, breakdown giảm."
        },
        {
            "title": "ABC lỗi chất lượng — Tập trung 3 lỗi lớn nhất!",
            "industry": "Điện tử",
            "situation": "20 loại defect (lỗi) trên bảng mạch. Tổng chi phí chất lượng (quality cost): 2 tỷ VND/năm. Cần tập trung cải tiến ở đâu?",
            "analysis": "Phân loại 20 loại lỗi theo CHI PHÍ TÁC ĐỘNG:\n\nNhóm A — 3 lỗi (15%) = 1.3 tỷ (65%!):\n• Solder bridge (cầu hàn — 2 chân IC hàn dính nhau): 600 triệu (30%) — tốn nhất vì phải rework tay dưới kính hiển vi!\n• BGA void (lỗ rỗng trong mối hàn BGA): 400 triệu (20%) — phải X-ray kiểm tra + reball lại\n• Tombstone (linh kiện đứng dậy 1 đầu): 300 triệu (15%) — phải gắp lại + hàn lại\n\nNhóm B — 5 lỗi (25%) = 450 triệu (22.5%): Cold solder, Missing component, Misalignment...\n\nNhóm C — 12 lỗi (60%) = 250 triệu (12.5%): Các lỗi nhỏ, ít xuất hiện",
            "result": "Tập trung cải tiến nhóm A:\n• Solder bridge → Stencil redesign: Thiết kế lại tấm stencil (lưới in kem hàn) — aperture ratio (tỷ lệ lỗ mở) phù hợp hơn → kem hàn không tràn giữa các chân IC\n• BGA void → Reflow profile optimization: Tối ưu đường cong nhiệt độ lò hàn → khí thoát ra hết trước khi hàn đóng rắn\n• Tombstone → Pad design modification: Cân bằng diện tích pad 2 đầu linh kiện → lực kéo đều → không bị \"đứng dậy\"\n\nKết quả: Chi phí lỗi nhóm A giảm 50% = tiết kiệm 650 triệu/năm!\n→ Chỉ cải tiến 3 lỗi mà giảm được 1/3 tổng cost of quality!"
        },
        {
            "title": "ABC-XYZ Matrix — Ma trận 2 chiều để quản lý tồn kho THÔNG MINH!",
            "industry": "Sản xuất chung",
            "situation": "ABC phân loại theo GIÁ TRỊ nhưng chưa xét ĐỘ BIẾN ĐỘNG nhu cầu. Cần kết hợp ABC + XYZ để có chính sách chi tiết hơn.",
            "analysis": "Thêm XYZ Analysis (phân loại theo độ biến động nhu cầu):\n• X = Ổn định (demand gần như giống nhau mỗi tháng, CV% Y = Dao động (demand thay đổi theo mùa/xu hướng, CV% 20-50%) — dự báo vừa\n• Z = Không dự đoán được (demand bất thường, CV% > 50%) — rất khó dự báo\n\nMa trận ABC-XYZ:\n• AX (giá trị cao + ổn định): Dự báo chính xác → MRP/JIT (mua đúng lúc đúng lượng)\n• AZ (giá trị cao + bất thường): RỦI RO CAO NHẤT! → Demand sensing + VMI với NCC\n• CX (giá trị thấp + ổn định): DỄ NHẤT → Tự động hóa đặt hàng (2-bin system)\n• CZ (giá trị thấp + bất thường): Mua theo đơn hàng (make-to-order)",
            "result": "Ứng dụng thực tế:\n• AX (bắp, đậu nành — dùng nhiều, đều mỗi tháng): MRP + JIT → Safety stock nhỏ (1 tuần), dự báo chính xác\n• AZ (bột cá nhập khẩu — đắt, lượng biến động theo mùa đánh bắt): Ưu tiên CAO NHẤT! → Demand sensing (theo dõi tín hiệu thị trường), ký hợp đồng dài hạn với NCC, tồn 2-3 tuần\n• CX (bulong, dây thít — rẻ, dùng đều): Set-and-forget! Kanban 2-bin, mua 1 lần/quý\n• CZ (phụ gia đặc biệt — rẻ, hiếm khi dùng): Mua khi cần, không tồn → tránh hết hạn\n\n→ Ma trận ABC-XYZ giúp 'cá nhân hóa' chính sách cho từng loại NL!"
        },
        {
            "title": "ABC thời gian của Supervisor — 40% thời gian lãng phí!",
            "industry": "Sản xuất chung",
            "situation": "Supervisor (quản lý ca) than phiền quá bận, OT 3 giờ/ngày. Nhưng khi phân tích thời gian → phát hiện 40% thời gian dùng cho việc KHÔNG TẠO GIÁ TRỊ!",
            "analysis": "Phân loại THỜI GIAN của Supervisor theo giá trị tạo ra:\n\nNhóm A — 30% thời gian (TẠO GIÁ TRỊ CAO!):\n• Lập kế hoạch SX, phân công ca, huấn luyện nhân viên, giải quyết vấn đề sản xuất, cải tiến quy trình\n→ Đây là những việc supervisor ĐƯỢC TRẢI TIỀN ĐỂ LÀM!\n\nNhóm B — 30% thời gian (Cần thiết nhưng không tối ưu):\n• Viết báo cáo, họp, giao tiếp email, điều phối\n\nNhóm C — 40% thời gian (LÃNG PHÍ!):\n• Nhập liệu vào Excel thủ công (admin), tìm thông tin (searching info), đọc lại email cũ, xử lý bàn giao ca bị sai, giải quyết vấn đề mà NV có thể tự giải quyết\n→ 40% thời gian = 3.2 giờ/ngày → đây là lý do OT 3 giờ!",
            "result": "Giải quyết:\n• Loại bỏ / Tự động hóa nhóm C:\n- Digital reporting: Báo cáo tự động từ hệ thống MES → không cần nhập Excel (giảm 60% admin)\n- Template bàn giao ca trên tablet → không sai sót → không phải xử lý lại\n- FAQ/SOP cho NV → NV tự giải quyết vấn đề nhỏ → không cần gọi supervisor\n• Delegate (ủy quyền) nhóm B: Team leader hỗ trợ báo cáo và điều phối\n\nKết quả: Thu hồi 2 giờ/ngày cho hoạt động nhóm A (tạo giá trị!) → Supervisor hiệu quả tăng 50%. OT = 0!"
        },
        {
            "title": "ABC vật tư y tế bệnh viện — Tiết kiệm 7.5 tỷ!",
            "industry": "Y tế",
            "situation": "Bệnh viện: 2,000 loại vật tư y tế, chi 50 tỷ/năm. Áp lực cắt giảm ngân sách nhưng KHÔNG ĐƯỢC ảnh hưởng chất lượng điều trị!",
            "analysis": "Phân loại 2,000 vật tư theo chi phí:\n\nNhóm A — 100 loại (5%) = 37.5 tỷ (75%):\n• Implant (vật cấy ghép phẫu thuật), thuốc đặc trị đắt tiền, thiết bị phẫu thuật dùng 1 lần\n• Giá mỗi item A: Từ vài triệu đến vài chục triệu → CHI PHÍ LỚN!\n\nNhóm C — 1,500 loại (75%) = chỉ 2.5 tỷ (5%):\n• Kim tiêm, găng tay, gạc, băng keo, bông tẩm cồn...\n• Giá: Vài nghìn đồng/chiếc → Nhưng 1,500 LOẠI → tốn rất nhiều thời gian quản lý!",
            "result": "Chính sách:\n• Nhóm A: Đấu thầu cạnh tranh (competitive bidding) mỗi năm. Hợp đồng ký gửi (consignment) cho implant — bệnh viện chỉ trả khi SỬ DỤNG, không tồn kho. Tham gia GPO (Group Purchasing Organization — mua chung với bệnh viện khác) → giá rẻ hơn 15%\n• Nhóm B: Đấu thầu hàng năm, hợp đồng dài hạn\n• Nhóm C: Standing order (đặt hàng cố định) + tự động bổ sung khi hết (auto-replenishment). Không tốn thời gian đặt hàng từng lần!\n\nTiết kiệm dự kiến: 15% = 7.5 tỷ/năm! Mà chất lượng vật tư KHÔNG thay đổi."
        },
        {
            "title": "ABC quản lý PM tasks — 40% task không cần thiết!",
            "industry": "Sản xuất chung",
            "situation": "500 task PM (Planned Maintenance — bảo trì kế hoạch) mỗi tháng. Đội bảo trì 10 người QUÁ TẢI. Nhưng liệu tất cả 500 task đều CẦN THIẾT?",
            "analysis": "Phân loại 500 PM tasks theo TÁC ĐỘNG đến độ tin cậy (reliability):\n\nNhóm A — 50 tasks (10%) ảnh hưởng 80% reliability:\n• PM cho thiết bị critical (pellet mill, boiler, compressor...). Nếu BỎ TASK NÀY → máy HỎ → dừng nhà máy!\n\nNhóm B — 100 tasks (20%) = 15% impact\n\nNhóm C — 350 tasks (70%) = chỉ 5% impact!:\n• Nhiều task C là \"kiểm tra bằng mắt\" → NV nhìn qua rồi tick ✓ mà KHÔNG thực sự hành động\n• Một số task C tần suất quá DÀY: Kiểm tra hàng tuần nhưng không bao giờ phát hiện vấn đề → có thể kiểm tra hàng tháng đủ rồi!\n• Một số task C cho máy KHÔNG QUAN TRỌNG (run-to-failure OK)",
            "result": "Tối ưu hóa danh sách PM:\n• Nhóm A: KHÔNG BAO GIỜ bỏ! Thêm CBM capability (giám sát tình trạng) cho 10 task A quan trọng nhất\n• Nhóm B: Tối ưu tần suất — ví dụ: từ hàng tuần → 2 tuần/lần (nếu dữ liệu cho thấy không cần thiết hàng tuần)\n• Nhóm C: Loại bỏ 200 tasks không cần thiết + Kéo dài chu kỳ 100 tasks (hàng tuần → hàng tháng)\n\nKết quả: PM tasks giảm 40% (500 → 300/tháng). Đội bảo trì HẾT QUÁ TẢI. Reliability KHÔNG GIẢM (vì chỉ bỏ task C ít impact).\n→ Bài học: Nhiều PM hơn ≠ Tốt hơn! PM ĐÚNG CHỖ mới quan trọng!"
        }
    ]
}
