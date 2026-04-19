method = {
    "id": 21,
    "title": "EPMD Analysis - Phân tích nút thắt cổ chai theo EPMD",
    "short_name": "EPMD",
    "icon": "⚙️",
    "pillar": "Focus Improvement",
    "description": "Bottleneck ở ĐÂU? Do THIẾT BỊ (E), QUY TRÌNH (P), CON NGƯỜI (M), hay THIẾT KẾ (D)? EPMD chỉ ra ĐÚNG HƯỚNG đầu tư!",
    "meaning": """
<p><strong>EPMD Analysis (Phân tích nút thắt theo E-P-M-D)</strong> là phương pháp phân tích CÓ CẤU TRÚC để tìm và GIẢI QUYẾT nút thắt cổ chai (bottleneck) bằng cách phân loại nguyên nhân gây nghẽn theo 4 yếu tố.</p>
<p><em>Hình dung: Đường cao tốc bị KẸT XE. Tại sao kẹt? <strong>E (Equipment)</strong> = Đường hỏng, hố gà? <strong>P (Process)</strong> = Đèn tín hiệu chu kỳ dài? Làn merge không hợp lý? <strong>M (Man)</strong> = Tài xế không biết nhường? Xe chết máy? <strong>D (Design)</strong> = Đường thiết kế chỉ 2 làn nhưng lưu lượng cần 4 làn? → Sửa ĐƯỜNG (E) hay sửa ĐÈN (P) hay đào tạo NGƯỜI (M) hay MỞ RỘNG (D) → MỖI HƯỚNG khác nhau!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 4 yếu tố EPMD — "Kim la bàn" chỉ đúng hướng!</div>
    <p><strong>⚙️ E - EQUIPMENT (Thiết bị)</strong>: Máy HỎNG, máy CHẬM, OEE thấp, breakdown nhiều, tốc độ giảm, changeover lâu.<br>
    <strong>🔄 P - PROCESS (Quy trình)</strong>: Layout kém, WIP tồn đọng, flow NGẮT, batch size sai, scheduling không tối ưu, thiếu parallel.<br>
    <strong>👷 M - MAN (Con người)</strong>: Thiếu người, thiếu KỸ NĂNG, thao tác sai, không có SOP, training kém, idle chờ quyết định.<br>
    <strong>📐 D - DESIGN (Thiết kế)</strong>: SP thiết kế KHÓ sản xuất, dung sai quá chặt, vật liệu khó xử lý, DFM kém, thiết bị design sai.<br><br>
    <em>So với Bottleneck Analysis (method 1): Bottleneck chỉ TÌM "chỗ nào nghẽn?" → EPMD đi SÂU HƠN: "TẠI SAO nghẽn?" → Phân loại theo E-P-M-D → <strong>GIẢI PHÁP chính xác!</strong><br>
    Tránh đầu tư SAI: Tưởng máy chậm (E) → MUA MÁY MỚI! Thực ra do quy trình (P) → mua máy mới VẪN NGHẼN! EPMD tránh sai lầm này!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>XÁC ĐỊNH bottleneck + PHÂN LOẠI nguyên nhân → biết phải ĐẦU TƯ vào đâu: Máy? Quy trình? Người? Thiết kế?</li>
    <li>TRÁNH ĐẦU TƯ SAI: Mua máy mới 5 tỷ khi vấn đề chỉ là scheduling (P) → lãng phí! EPMD phát hiện ĐÚNG yếu tố!</li>
    <li>ƯU TIÊN HÓA hành động: D (thiết kế) thường lâu nhất + đắt nhất → M (training) thường nhanh + rẻ → Làm M trước!</li>
    <li>TĂNG OEE + Throughput TỔNG THỂ: Giải phóng bottleneck = TOÀN BỘ dây chuyền TĂNG sản lượng!</li>
    <li>FRAMEWORK CÓ HỆ THỐNG cho Focused Improvement (FI): Team không brainstorm tự do → dùng EPMD checklist → TOÀN DIỆN!</li>
    <li>Áp dụng MỌI NGÀNH: Sản xuất, logistics, dịch vụ, lab, IT, bệnh viện... BẤT KỲ quy trình nào có bottleneck!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: TÌM BOTTLENECK — Đo cycle time + throughput TỪNG công đoạn!</div>
        <div class="step-card__desc">Vẽ SƠ ĐỒ DÒNG CHẢY (process flow) → Ghi cycle time (thời gian chu kỳ) từng công đoạn → Tìm công đoạn CÓ CYCLE TIME CAO NHẤT = BOTTLENECK! Hoặc: Tìm công đoạn có WIP (hàng chờ) TỒN ĐỌNG CAO NHẤT → hàng đang "xếp hàng" chờ = BOTTLENECK! Ví dụ: Trộn 5 phút → Ép viên 8 phút → Sàng 3 phút → Bao gói 4 phút → ÉP VIÊN = BOTTLENECK (8 phút > tất cả!)</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: PHÂN TÍCH E-P-M-D cho bottleneck — Checklist 4 yếu tố!</div>
        <div class="step-card__desc"><strong>E checklist</strong>: OEE? Breakdown? Speed loss? Changeover time? Thiết bị cũ/mới? Năng lực thiết kế vs thực tế? PM có tốt? <strong>P checklist</strong>: Layout hợp lý? WIP tồn? Flow liên tục? Batch size? Scheduling? Parallel được không? <strong>M checklist</strong>: Đủ người? Skill matrix? Có SOP? Training đủ? Thao tác chuẩn? Idle do chờ? <strong>D checklist</strong>: Thiết kế SP khó SX? Dung sai quá chặt? Có thể redesign? DFM? Thiết bị/jig thiết kế SAI? → Mỗi yếu tố: GHI → ĐÁNH GIÁ impact (H/M/L) → ƯU TIÊN!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: XẾP HẠNG ưu tiên — Impact × Khả thi × Chi phí!</div>
        <div class="step-card__desc">Với MỖI yếu tố E-P-M-D đã tìm → Đánh giá: <strong>IMPACT</strong>: Nếu sửa → sẽ TĂNG bao nhiêu throughput? <strong>KHẢ THI</strong>: Sửa NHANH không? Cần mua gì? Cần ai? <strong>CHI PHÍ</strong>: Bao nhiêu? So với lợi ích? → Ma trận: Impact cao + Khả thi dễ + Chi phí thấp → LÀM TRƯỚC! (Quick win!) → Impact cao + Khả thi khó + Chi phí cao → LÀM SAU BUT PLAN NOW! (Dự án!) → Impact thấp → KHÔNG LÀM! (Waste effort!)</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: ACTION PLAN + THỰC HIỆN + ĐO LƯỜNG!</div>
        <div class="step-card__desc">Lập ACTION PLAN: Mỗi action → Ai làm? Khi nào xong? Đo gì? Target? ĐO LƯỜNG trước/sau: Throughput trước EPMD vs sau EPMD → TĂNG bao nhiêu %? Cycle time trước vs sau → GIẢM bao nhiêu? LƯU Ý: Sau khi giải BOTTLENECK #1 → bottleneck SẼ DỊCH SANG công đoạn khác! → Lặp lại EPMD cho bottleneck MỚI! Continuous improvement = EPMD liên tục!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Pellet mill 65% năng lực — EPMD phát hiện 4 yếu tố CÙNG gây nghẽn!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Dây chuyền ép viên năng suất chỉ 26 tấn/h (thiết kế 40 tấn/h = 65%!). BGĐ: \"Mua pellet mill MỚI 3 tỷ?\" → Trước khi mua → EPMD phân tích ĐÃ!",
            "analysis": "EPMD Analysis — Pellet Mill Bottleneck:\n\n| Yếu tố | Phát hiện | Impact | Ưu tiên |\n| E (Equipment) | Die MÒN 40% → throughput giảm 15% + Steam valve KHÔNG ỔN ĐỊNH → conditioning kém | HIGH | 🔴 Thay die NGAY! |\n| P (Process) | Changeover giữa codes mất 45 phút (quá lâu!) → 4 lần/ca = 3 giờ DỪNG! | HIGH | 🔴 SMED! |\n| M (Man) | Ca ĐÊM chạy chậm hơn ca ngày 15% → operator ca đêm ít kinh nghiệm! | MEDIUM | 🟡 Training! |\n| D (Design) | 3 code cám MỚI formula high-fiber → die design chưa phù hợp (hole ratio sai!) | HIGH | 🔴 Redesign die! |\n\nInsight EPMD:\n• KHÔNG CHỈ 1 yếu tố! CẢ 4 yếu tố đều gây nghẽn!\n• Nếu CHỈ mua máy MỚỊ (E) → P vẫn 45 phút changeover + M vẫn ca đêm chậm + D vẫn die sai → MÁY MỚI VẪN CHỈ 75%!",
            "result": "Action Plan theo EPMD:\n\n| Yếu tố | Action | Chi phí | Throughput tăng |\n| E | Thay die mới + sửa steam valve | 50 triệu | +15% (26 → 30 tấn/h) |\n| P | SMED: Recipe PLC auto-recall + sequencing code gần nhau | 10 triệu | Changeover 45' → 15' → thêm 2h chạy/ca! |\n| M | Training ca đêm: senior operator mentor + SOP visual | 5 triệu | Ca đêm +15% (= ca ngày!) |\n| D | Redesign die hole ratio cho high-fiber codes | 30 triệu | +10% throughput cho 3 codes mới |\n\nTổng: 95 triệu → 35 tấn/h (87.5% thiết kế!)\nSo sánh: Mua pellet mill MỚI = 3 TỶ → chỉ tăng thêm 15% (vì P, M, D vẫn nghẽn!)\n\n→ Bài học EPMD: Tưởng \"máy yếu → mua máy mới 3 tỷ\"? EPMD phân tích: 4 yếu tố cùng gây nghẽn → sửa cả 4 chỉ 95 triệu → đạt 87.5%! MUA MÁY MỚI chưa chắc đạt được nếu P-M-D vẫn nghẽn!"
        },
        {
            "title": "Lab QC lead time 5 ngày — EPMD: Machine (E) + Process (P) + Man (M)!",
            "industry": "Dược phẩm",
            "situation": "Phòng lab QC mất 5 NGÀY kiểm nghiệm thành phẩm → release hàng CHẬM → khách hàng complaint! BGĐ: \"Mua thêm máy HPLC!\" (800 triệu!) → EPMD trước!",
            "analysis": "EPMD Analysis — Lab QC Bottleneck:\n\n| Yếu tố | Phát hiện | Impact |\n| E (Equipment) | 2 máy HPLC CŨ → run time 45 phút/mẫu (máy mới = 20 phút!). Detector hay drift → phải re-calibrate → mất 2h/lần! | HIGH |\n| P (Process) | Mẫu vào lab = xử lý FIFO → đơn hàng GẤP cũng phải CHỜ THEO THỨ TỰ! + Kết quả ghi trên GIẤY → transcribe vào LIMS mất 30 phút/batch! | HIGH |\n| M (Man) | Chỉ 3/6 analyst biết dùng HPLC! 3 người còn lại chỉ làm titration/physical test → HPLC luôn quá tải! | HIGH |\n| D (Design) | Method validation dùng mobile phase CŨ → runtime 45 phút. Revalidate với mobile phase mới → runtime 20 phút! | MEDIUM |\n\nInsight EPMD:\n• Mua thêm HPLC (E) → runtime vẫn 45 phút/mẫu (D chưa sửa!) + scheduling vẫn FIFO (P!) + vẫn 3 người (M!) → lead time giảm ÍT!\n• P (scheduling) + M (training) = CHI PHÍ THẤP nhưng IMPACT CAO!",
            "result": "Action Plan EPMD:\n\n| Yếu tố | Action | Chi phí | Impact |\n| P (Quick win!) | Priority scheduling: Đơn gấp → TEST TRƯỚC! Digitalize: LIMS barcode scan thay ghi giấy | 15 triệu | Lead time đơn gấp: 5 ngày → 2 ngày! |\n| M (Quick win!) | Training HPLC cho 3 analyst còn lại → HPLC capacity TĂNG GẤP ĐÔI! | 10 triệu | Xử lý 2× mẫu/ngày! |\n| D (Medium-term) | Revalidate method với mobile phase mới → runtime 45' → 20'/mẫu | 20 triệu | Throughput +56%! |\n| E (Last resort) | Nếu vẫn thiếu → MUA 1 HPLC mới | 800 triệu | +50% capacity |\n\nKết quả SAU P + M + D (CHƯA MUA MÁY!): Lead time 5 ngày → 2 ngày! Chi phi: 45 triệu!\n→ KHÔNG CẦN MUA HPLC 800 triệu! (Có thể cân nhắc sau nếu demand tăng thêm)\n\n→ Bài học EPMD dược phẩm: Tưởng \"thiếu máy → mua máy 800 triệu\"? EPMD: P (scheduling) + M (training) + D (method) → 45 triệu → lead time GIẢM 60%! Máy HPLC cũ vẫn dùng tốt nếu P-M-D được sửa!"
        },
        {
            "title": "Line nhãn chai 350/phút (target 500) — D: Nhãn wrap khó dán ở tốc độ cao!",
            "industry": "Đồ uống",
            "situation": "Line PET bottle: Filling 500 chai/phút → nhưng labeling CHỈ 350 chai/phút → BOTTLENECK! BGĐ: \"Mua máy dán nhãn MỚI!\" (2 tỷ!) → EPMD kiểm tra!",
            "analysis": "EPMD Analysis — Labeling Bottleneck:\n\n| Yếu tố | Phát hiện | Impact |\n| E (Equipment) | Máy dán nhãn CŨ nhưng tốc độ MAX = 400 chai/phút → vẫn DƯ so với 350 hiện tại! Bị STOP do kẹt nhãn → OEE machine chỉ 70%! | HIGH |\n| P (Process) | Nhãn cuộn NGẮN → phải thay MỖI 30 PHÚT → mất 5 phút/lần → 10% thời gian là THAY CUỘN! | MEDIUM |\n| M (Man) | Operator phản ứng CHẬM khi nhãn kẹt: trung bình 3 phút mới xử lý! → micro-stop tích tụ! | MEDIUM |\n| D (Design) | Nhãn WRAP-AROUND (quấn quanh) khó dán ở tốc độ cao + chai OVAL khó hơn chai TRÒN! → Thiết kế nhãn LÀ GỐC tốc độ thấp! | HIGH — ROOT! |\n\nInsight EPMD:\n• MUA MÁY MỚI (E) → nhưng nhãn wrap-around vẫn khó dán (D!) + cuộn nhãn vẫn ngắn (P!) → tốc độ vẫn bị giới hạn!\n• D (thiết kế nhãn) = ROOT CAUSE tốc độ thấp! Wrap-around + chai oval = COMBO khó ở tốc độ cao!",
            "result": "Action Plan EPMD — Sửa D trước!:\n\n| Yếu tố | Action | Chi phí | Impact |\n| D (Game-changer!) | Chuyển từ wrap-around → SHRINK SLEEVE label! | 100 triệu (mua shrink tunnel) | Tốc độ MAX →600 chai/phút! Chai oval cũng dán DỄDÀNG! |\n| E (Overhaul) | Overhaul máy dán nhãn hiện tại + thay sensor mới | 30 triệu | OEE 70% → 90%! |\n| P | Dùng cuộn nhãn LỚN HƠN (từ 1,000m → 2,500m) | 5 triệu (thay trục cuộn) | Giảm thay cuộn: 30' → 75' → ít stop hơn! |\n| M | SOP xử lý kẹt nhãn nhanh + visual guide | 2 triệu | Phản ứng 3' → 1' |\n\nTổng: 137 triệu → 480 chai/phút! (Gần target 500!)\nSo sánh: Mua máy mới = 2 TỶ → nhưng nếu VẪN dùng nhãn wrap (D) → tốc độ vẫn bị giới hạn!\n\n→ Bài học EPMD đồ uống: EPMD phát hiện D (thiết kế nhãn) là ROOT → đổi từ wrap → shrink sleeve → GAME-CHANGER! Không cần mua máy 2 tỷ, chỉ cần mua shrink tunnel 100 triệu + overhaul 30 triệu = 130 triệu → gần đạt target!"
        },
        {
            "title": "Robot hàn 85s/panel (takt 60s) — M: Path chưa optimal + D: 8 mối hàn thừa!",
            "industry": "Ô tô",
            "situation": "Trạm hàn side panel mất 85s/xe (TAKT TIME = 60s!) → TOÀN line dây chuyền bị bottleneck tại đây! → \"Mua robot mới đời 2024?\" (5 tỷ!) → EPMD trước!",
            "analysis": "EPMD Analysis — Robot Welding Bottleneck:\n\n| Yếu tố | Phát hiện | Impact | Action |\n| E (Equipment) | Robot đời 2012 → tốc độ di chuyển CHẬM hơn 30% so với model mới | -5s nếu nâng cấp servo | 🟡 Medium-term |\n| P (Process) | 45 mối hàn → robot phải quay 3 bên panel → path di chuyển DÀI! | Nhiều air move (di chuyển không hàn) | 🟡 Optimize path |\n| M (Man) | Kỹ sư program robot CHƯA TỐI ƯU path → nhiều air move THỪA → robot bay đi bay lại vô ích! | -10s! | 🔴 Quick win! |\n| D (Design) | 45 mối hàn nhưng PHÂN TÍCH → 8 mối hàn có thể thay bằng adhesive bonding! (Keo kết cấu!) | -15s! | 🔴 Game-changer! |\n\nInsight EPMD:\n• M (optimize path) = Quick win! MIỄN PHÍ! → -10s NGAY!\n• D (adhesive thay 8 mối) = -15s → lớn nhất! Nhưng cần R&D + test 3 tháng\n• E (nâng cấp servo) = -5s → chi phí vừa phải\n• Tổng 3 actions: -30s → 85s → 55s < 60s takt time!",
            "result": "Action Plan — M trước, D sau, E cuối!:\n\n| Thứ tự | Action | Chi phí | Giảm | Cycle time |\n| 1. M (NGAY!) | Optimize robot path: giảm air move, resequence weld order | 0 VND! | -10s | 85 → 75s |\n| 2. D (3 tháng) | Chuyển 8 mối hàn → adhesive bonding (keo kết cấu) | 200 triệu (R&D + test + dispensing robot) | -15s | 75 → 60s |\n| 3. E (nếu cần) | Nâng cấp servo motor robot tốc độ cao | 300 triệu | -5s | 60 → 55s (margin!) |\n\nKết quả: 85s → 55s! Tổng chi phí: 500 triệu (vs mua robot MỚI 5 TỶ!)\nBonus: Adhesive bonding = NHẸ hơn spot weld → xe NHẸ hơn 2kg → fuel efficiency TĂNG!\n\n→ Bài học EPMD ô tô: M (optimize path) = 0 VND → giảm 10s NGAY! D (adhesive) = thay đổi LỚN NHẤT → giảm 15s! E (robot mới 5 tỷ) chỉ giảm 5s → ROI tệ nhất! EPMD giúp ưu tiên M→D→E thay vì mua sắm E trước!"
        },
        {
            "title": "Kho e-commerce 3000 đơn/ngày (target 5000) — P: Route + D: Layout cũ!",
            "industry": "E-commerce",
            "situation": "Kho fulfillment cần 5,000 đơn/ngày mùa sale nhưng chỉ xử lý 3,000! Thiếu 40%! CEO: \"Thuê thêm người!\" (M) → EPMD kiểm tra: Có ĐÚNG thiếu người không?",
            "analysis": "EPMD Analysis — Warehouse Picking Bottleneck:\n\n| Yếu tố | Phát hiện | Impact |\n| E (Equipment) | Xe nâng CŨ → battery chỉ 6 giờ → sạc 4 giờ → downtime 40% thời gian! | HIGH |\n| P (Process) | Picking route KHÔNG TỐI ƯU → nhân viên đi LÒNG VÒNG 60% thời gian! Picking kiểu single-order (1 lần đi = 1 đơn) → rất lãng phí! | ROOT! |\n| M (Man) | Nhân viên thời vụ mùa sale KHÔNG THUỘC layout → picking sai location 8%! Nhưng nhân viên CŨ hoàn toàn ĐỦ nếu process tốt! | MEDIUM |\n| D (Design) | SKU layout theo ABC analysis từ 2 NĂM TRƯỚC! Sản phẩm bán CHẠY NHẤT giờ nằm ở cuối kho → đi xa nhất! | HIGH! |\n\nInsight EPMD:\n• GỐC = P (route lòng vòng) + D (layout cũ 2 năm!) → nhân viên ĐI NHIỀU, PICK ÍT!\n• Thuê thêm người (M) → nhưng route vẫn lòng vòng + layout vẫn cũ → mỗi người VẪN ĐI 60% → cần NHIỀU người hơn nữa!",
            "result": "Action Plan EPMD:\n\n| Yếu tố | Action | Chi phí | Impact |\n| D (Re-slotting!) | Re-slotting SKU theo data bán hàng 3 tháng gần nhất → SP bán chạy → GẦNNHẤT cửa ra! | 5 triệu (nhân công di chuyển) | ĐI ngắn hơn 40%! |\n| P (Wave picking!) | Từ single-order → WAVE PICKING + ZONE PICKING → 1 lần đi = gom 10-20 đơn! | 20 triệu (WMS update) | Picking speed +80%! |\n| E | Mua battery SWAP (thay pin nóng) + 5 xe nâng mới lithium (sạc nhanh 1h) | 200 triệu | Uptime 40% → 90%! |\n| M | Training nhân viên thời vụ + buddy system | 10 triệu | Sai location 8% → 1%! |\n\nKết quả: 3,000 → 4,800 đơn/ngày! Tổng chi phí: 235 triệu!\nSo sánh: Thuê 20 người thêm × 8 triệu/tháng = 160 triệu/tháng! → 1.5 tháng = BẰNG chi phí EPMD nhưng mỗi tháng vẫn phải trả!\n\n→ Bài học EPMD logistics: Thuê thêm người (M) = GIẢI PHÁP ngắn hạn đắt đỏ! EPMD: D (re-slot) + P (wave pick) = giải pháp VĨNGViễn → throughput tăng 60% mà KHÔNG THÊM NGƯỜI!"
        }
    ]
}
