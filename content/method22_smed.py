method = {
    "id": 22,
    "title": "IE-Technique (SMED) - Kỹ thuật giảm thời gian chuyển đổi",
    "short_name": "IE-Technique (SMED)",
    "icon": "⏱️",
    "pillar": "Focus Improvement",
    "description": "SMED = Single Minute Exchange of Die: Giảm changeover DƯỚI 10 PHÚT! Bí quyết: Chuyển Internal → External + Quick Clamp!",
    "meaning": """
<p><strong>IE-Technique (SMED — Single Minute Exchange of Die)</strong> là kỹ thuật Industrial Engineering do <strong>Shigeo Shingo</strong> (Toyota) phát triển để giảm thời gian chuyển đổi (changeover/setup) xuống dưới 10 phút (1 chữ số phút = "Single Minute").</p>
<p><em>Hình dung: Đội đua F1 pit-stop. Xe vào pit → 4 người ĐỒNG THỜI thay 4 bánh xe → 2 giây → xe RA! Tại sao nhanh? (1) Chuẩn bị SẴN bánh mới TRƯỚC KHI xe vào (External!) (2) Quick-release nut → 1 vặn = tháo (không 20 bolt!) (3) 4 người SONG SONG → không 1 người 4 bánh! (4) Luyện tập → chuẩn hóa → MỌI LẦN như nhau!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 2 khái niệm CỐT LÕI — Internal vs External!</div>
    <p><strong>🔴 Internal Setup (IED)</strong>: Công việc CHỈ làm được khi máy DỪNG!<br>
    Ví dụ: Tháo khuôn cũ, lắp khuôn mới, siết bolt khuôn → BẮT BUỘC máy dừng!<br><br>
    <strong>🟢 External Setup (OED)</strong>: Công việc CÓ THỂ làm khi máy ĐANG CHẠY!<br>
    Ví dụ: Chuẩn bị khuôn mới, kết nối nước/dầu trước, đặt dụng cụ sẵn → làm TRONG LÚC máy chạy đơn hàng trước!<br><br>
    <strong>BÍ MẬT SMED</strong>: Nhiều nhà máy làm TẤT CẢ công việc khi máy DỪNG (mọi thứ đều Internal!) → máy dừng 3 giờ! → SMED phát hiện 40-60% công việc ĐÓ có thể làm khi máy ĐANG CHẠY! → <strong>Chuyển Internal → External → máy dừng chỉ 30 phút!</strong><br><br>
    <em>Target: < 10 phút (Single Minute!) Tại sao? Vì changeover < 10 phút = có thể chạy LOT SIZE NHỎ → linh hoạt → JIT → ít tồn kho!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>GIẢM thời gian changeover = TĂNG thời gian sản xuất → OEE TĂNG! (Changeover = Planned Downtime = OEE killer!)</li>
    <li>CHO PHÉP chạy LOT SIZE NHỎ mà vẫn hiệu quả: Changeover 3 giờ → lot phải LỚN (để \"đáng\" dừng máy!). Changeover 15 phút → lot NHỎ cũng OK → Sản xuất LINH HOẠT!</li>
    <li>GIẢM TỒN KHO: Lot nhỏ → sản xuất ĐÚNG đơn hàng → không sản xuất DƯ → WIP giảm → finished goods giảm → VỐN giảm!</li>
    <li>ĐÁP ỨNG NHANH: Khách hàng thay đổi đơn đột xuất → changeover nhanh → CHUYỂN NGAY → khách hàng HÀI LÒNG!</li>
    <li>GIẢM STRESS cho operator: Changeover 3 giờ = áp lực → vội → sai → hỏng! Changeover 15 phút = SOP rõ ràng → bình tĩnh → chuẩn!</li>
    <li>Áp dụng MỌI ngành: Ép nhựa, CNC, đóng gói, in ấn, hóa chất, thực phẩm, dệt may, điện tử... BẤT KỲ máy nào cần setup!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: QUAY VIDEO + GHI NHẬN hiện trạng — Không bỏ sót bước nào!</div>
        <div class="step-card__desc">QUAY VIDEO toàn bộ quá trình changeover từ đầu đến cuối! Đo: TỔNG THỜI GIAN = từ sản phẩm TỐT CUỐI CÙNG (đơn cũ) → đến sản phẩm TỐT ĐẦU TIÊN (đơn mới)! Liệt kê TỪNG BƯỚC: Bước 1 - Tháo khuôn cũ - 15 phút. Bước 2 - Đi lấy khuôn mới ở kho - 10 phút (Ơ! Sao phải ĐI LẤY?). Bước 3 - Lắp khuôn - 20 phút. Bước 4 - Tìm dụng cụ - 5 phút (Ơ! Sao phải TÌM?)... GHI CHÚ: Những bước \"lãng phí\" → đánh dấu ĐỎ!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: PHÂN LOẠI Internal vs External — Bước nào CẦN máy dừng?</div>
        <div class="step-card__desc">Xem lại TỪNG bước → hỏi: <strong>\"Bước này BẮT BUỘC phải làm khi máy dừng?\"</strong> ✅ BẮT BUỘC máy dừng (Internal): Tháo khuôn, lắp khuôn, siết bolt... ❌ KHÔNG CẦN máy dừng (nhưng ĐANG LÀM khi dừng!) → Chuyển sang External! Ví dụ: \"Đi lấy khuôn mới\" → Có thể lấy TRƯỚC 30 phút khi dừng! \"Tìm dụng cụ\" → Có thể chuẩn bị SẴN trên xe đẩy! \"Kiểm tra drawing\" → Đọc TRƯỚC khi dừng máy! \"Pre-heat khuôn\" → Có thể gia nhiệt ở LÒ RIÊNG! THỰC TẾ: 40-60% bước \"Internal\" CÓ THỂ chuyển sang External!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: TỐI ƯU Internal còn lại — NHANH HƠN + SONG SONG!</div>
        <div class="step-card__desc">Với những bước BẮT BUỘC Internal → làm cho NHANH hơn: <strong>QUICK CLAMP</strong>: Thay 12 bolt bằng 2 quick-release clamp → 20 phút → 3 phút! <strong>SONG SONG</strong>: 2 người làm đồng thời 2 bên (F1 pit-stop!) → Thời gian /2! <strong>LOẠI BỎ ADJUSTMENT</strong>: Dùng locating pin, gauge block, one-touch → KHÔNG CẦN chỉnh! Cassette/cartridge: Lắp sẵn nhiều component thành 1 unit → RÚT CŨ → ĐẨY MỚI = 2 phút! <strong>STANDARDIZE</strong>: Chuẩn hóa kích thước khuôn/die → cùng kích thước base → lắp lẫn được!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: TỐI ƯU External — Chuẩn bị HOÀN HẢO TRƯỚC KHI dừng!</div>
        <div class="step-card__desc"><strong>XE ĐẨY chuyên dụng (Tool Cart)</strong>: Mỗi changeover = 1 xe đẩy → tất cả dụng cụ + khuôn + template SẴN SÀNG → đẩy đến máy → BẮT ĐẦU! <strong>CHECKLIST chuẩn bị</strong>: 15 phút trước dừng → operator chạy checklist: ☐ Khuôn mới trên xe? ☐ Dụng cụ đủ? ☐ Drawing sẵn? ☐ Recipe trên PLC? → TẤT CẢ ✅ mới dừng! <strong>5S khu vực changeover</strong>: Dụng cụ treo tường theo shadow board → tay cầm ĐÚNG cái cần → không TÌM! <strong>RECIPE DATABASE</strong>: Thông số trên PLC/controller → auto-recall theo mã sản phẩm → KHÔNG nhập thủ công!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">5</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 5: CHUẨN HÓA + LUYỆN TẬP + DUY TRÌ!</div>
        <div class="step-card__desc"><strong>SOP changeover MỚI</strong>: Ghi lại QUY TRÌNH mới với hình ảnh/video → DÁN tại máy! <strong>TRAINING</strong>: Tất cả operator phải luyện tập → TẤT CẢ đều làm giống nhau → không \"ai giỏi ai dở\"! <strong>ĐO LƯỜNG</strong>: Ghi thời gian changeover MỖI LẦN → chart theo dõi → nếu TĂNG lại → phải kiểm tra! <strong>KAIZEN liên tục</strong>: Mỗi tháng → review → \"Còn bước INTERNAL nào chuyển được sang External?\" → cải tiến thêm! TARGET: Single Minute = < 10 phút! One-Touch = < 100 giây! OTED (One-Touch Exchange of Die) = đỉnh cao!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Khuôn ép nhựa 3.5 giờ → 55 phút! Quick Clamp + Pre-heat!",
            "industry": "Nhựa",
            "situation": "Máy ép nhựa 450 tấn — changeover khuôn mất 3.5 GIỜ (210 phút!). Mỗi ngày chuyển 2 lần → 7 giờ/ngày CHỈ ĐỂ SET UP! Chỉ còn 17 giờ chạy/ngày!",
            "analysis": "Video Analysis — Phân tích từng bước:\n\n| # | Bước | Thời gian | Internal/External? |\n| 1 | Tháo 12 bolt khuôn cũ | 20' | 🔴 Internal (nhưng quick clamp → 3'!) |\n| 2 | Cẩu khuôn cũ ra | 10' | 🔴 Internal |\n| 3 | Đi lấy khuôn mới ở KHO (cách 100m!) | 25' | ❌ Đang làm Internal → CÓ THỂ External! |\n| 4 | Cẩu khuôn mới vào | 10' | 🔴 Internal |\n| 5 | Lắp 12 bolt khuôn mới | 20' | 🔴 Internal (→ quick clamp → 3'!) |\n| 6 | Kết nối nước/dầu (5 vòi!) | 20' | ❌ Có thể pre-connect trên khuôn trước! |\n| 7 | Nhập thông số (nhiệt/áp/tốc độ) | 15' | ❌ Recipe PLC auto-recall! |\n| 8 | CHỜ khuôn nóng lên (cold → hot!) | 35' | ❌ Pre-heat khuôn trong lò riêng! |\n| 9 | Điều chỉnh fine-tune | 20' | 🔴 Internal (giảm nếu recipe chính xác) |\n| 10 | Chạy thử 10 shot kiểm tra | 25' | 🔴 Internal (giảm nếu pre-heat đúng) |\n| | TỔNG | 210' | |\n\nPhát hiện: 95 phút (45%) = ĐANG làm khi dừng máy NHƯNG có thể làm External!",
            "result": "SMED Kaizen:\n\n| Thay đổi | Trước | Sau | Tiết kiệm |\n| Đi lấy khuôn → Chuẩn bị TRƯỚC (external!) | 25' | 0' | -25' |\n| 12 bolt → Quick hydraulic clamp (tháo + lắp) | 40' | 6' | -34' |\n| Kết nối nước → Multi-coupler (1 đầu nối = 5 vòi!) | 20' | 3' | -17' |\n| Nhập thông số → Recipe PLC auto-recall | 15' | 1' | -14' |\n| Chờ khuôn nóng → Pre-heat trong lò riêng (external!) | 35' | 0' | -35' |\n| Chạy thử → Giảm nhờ pre-heat đúng + recipe chính xác | 25' | 15' | -10' |\n\nTỔNG: 210 phút → 55 phút! GIẢM 74%!\n• Mỗi ngày THÊM 5 giờ sản xuất! → +20% output!\n• ROI: Quick clamp 50 triệu + Multi-coupler 30 triệu + Pre-heat lò 20 triệu = 100 triệu → Payback 2 tháng!"
        },
        {
            "title": "Pellet mill changeover 45' → 12'! Recipe PLC + Sequencing!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Changeover giữa các code cám trên pellet mill mất 45 phút. 4-5 lần/ca → mất 3-4 GIỜIỜ/ca chỉ để đổi code! = 15-20% thời gian sản xuất!",
            "analysis": "Video Analysis — Changeover pellet mill:\n\n| # | Bước | Thời gian | Loại |\n| 1 | Flush (xả) NVL cũ → cho chạy hết trong máy | 15' | 🔴 Internal |\n| 2 | Điều chỉnh STEAM (áp suất, nhiệt) | 5' | 🔴 Internal (→ recipe auto!) |\n| 3 | Chỉnh GAP roller-die | 10' | 🔴 Internal (→ recipe auto!) |\n| 4 | Thay screen sàng (nếu cần) | 5' | 🔴 Internal |\n| 5 | Chạy THỬ đạt chất lượng (viên đúng size, moisture, PDI) | 10' | 🔴 Internal |\n\nPhát hiện:\n• Flush 15' = LÃNG PHÍ LỚN NHẤT! → Nhưng nếu chạy code GẦN NHAU → flush ÍT!\n• Steam + Gap = mỗi operator điều chỉnh KHÁC NHAU (trial-error!) → tốn 15' thay vì 2'!",
            "result": "SMED Kaizen cho Pellet Mill:\n\n| Thay đổi | Trước | Sau | Tiết kiệm |\n| Recipe Management PLC: Lưu thông số (steam, gap, feed rate) cho TỪNG code cám → auto-recall | 15' (steam+gap) | 2' (nhấn nút!) | -13' |\n| Production Sequencing: Chạy codes GẦN NHAU liên tiếp (cùng formula base) → flush ÍT | 15' | 5' (flush ít) | -10' |\n| Standard screen: 1 loại screen dùng chung cho 80% codes (trừ special) | 5' | 0' (không thay!) | -5' |\n| Chạy thử → PDI check nhanh (lấy 1 mẫu → test crush ngay) | 10' | 5' | -5' |\n\nTỔNG: 45 phút → 12 phút! GIẢM 73%!\n• 4 lần/ca × 33 phút tiết kiệm = 2.2 giờ thêm SẢN XUẤT mỗi ca!\n• Sản lượng thêm: 2.2h × 30 tấn/h = 66 tấn/ca! → Revenue thêm 330 triệu/ca!\n\n→ Bài học SMED feed mill: Recipe PLC = QUICK WIN lớn nhất! Operator KHÔNG CẦN Trial-error → nhấn nút → máy tự set! Sequencing = MIỄN PHÍ → chỉ cần LẬP LỊCH thông minh → flush giảm 67%!"
        },
        {
            "title": "SMT line changeover 2 giờ → 18 phút! Trolley exchange = F1 pit-stop!",
            "industry": "Điện tử",
            "situation": "Chuyển model PCB trên line SMT mất 2 GIỜ! Line có: Stencil printer + 3 máy placement + Reflow oven. Thay feeder = 60% changeover time!",
            "analysis": "Video Analysis — SMT Changeover:\n\n| # | Bước | Thời gian | Loại |\n| 1 | Printer: Thay stencil + solder paste | 15' | 🔴 Internal (→ quick-lock!) |\n| 2 | Place machine 1: Thay feeder (25-40 feeder!) | 30' | ❌ → TROLLEY EXCHANGE! |\n| 3 | Place machine 2: Thay feeder | 25' | ❌ → TROLLEY EXCHANGE! |\n| 4 | Place machine 3: Thay feeder | 25' | ❌ → TROLLEY EXCHANGE! |\n| 5 | Reflow: Đổi temperature profile | 5' | 🔴 Internal (→ recipe auto!) |\n| 6 | Nạp program mới | 5' | ❌ → Auto download! |\n| 7 | First Article Inspection | 15' | 🔴 Internal |\n\nPhát hiện: Thay feeder 80 phút = 67% thời gian! Mỗi feeder tháo 1 cái → lắp 1 cái → 25 cái/máy × 3 máy = 75 thao tác!",
            "result": "SMED Game-changer: TROLLEY EXCHANGE SYSTEM!\n\nConcept F1: Thay vì tháo/lắp TỪNG feeder → Pre-setup TOÀN BỘ feeder trên xe đẩy (trolley) riêng TRONG LÚC máy đang chạy! → Khi changeover: RÚT trolley cũ → ĐẨY trolley mới vào → 2 PHÚT/MÁY!\n\n| Thay đổi | Trước | Sau | Tiết kiệm |\n| Feeder 3 máy → Trolley exchange (rút cũ + đẩy mới!) | 80' | 6' (2'/máy!) | -74'! |\n| Stencil → Quick-lock frame (snap-in!) | 15' | 3' | -12' |\n| Program → Barcode scan auto-download (scan PCB → load program!) | 5' | 0.5' | -4.5' |\n| Profile → Recipe auto-recall | 5' | 0.5' | -4.5' |\n| FAI → AOI auto-check first board | 15' | 5' | -10' |\n\nTỔNG: 120 phút → 18 phút! GIẢM 85%!\nInvestment: Trolley exchange system = 200 triệu/machine × 3 = 600 triệu\nPayback: Thêm 1.7 giờ/changeover × 3 lần/ngày = 5 giờ/ngày sản xuất thêm → Payback 2 tháng!"
        },
        {
            "title": "Máy dập 200T changeover khuôn 2.5 giờ → 25 phút! Cassette die!",
            "industry": "Kim loại",
            "situation": "Máy press 200 tấn — thay khuôn dập mất 2.5 GIỜ (150 phút!). Mỗi ca thay 3-4 khuôn → gần NỬA CA = SETUP! Sản xuất thực < 50%!",
            "analysis": "Video Analysis — Die Change Press 200T:\n\n| # | Bước | Thời gian | Nhận xét |\n| 1 | Dừng máy + an toàn (lock-out) | 5' | 🔴 Internal — giữ nguyên (an toàn!) |\n| 2 | Tháo 8 bolt khuôn + clamp | 15' | 🔴 → Hydraulic clamp: 2'! |\n| 3 | CHỜ CRANE (cẩu bận!) | 20' | ❌ LÃNG PHÍ THUẦN! → Roller cart! |\n| 4 | Cẩu khuôn cũ ra | 10' | 🔴 → Roller cart: 3'! |\n| 5 | Cẩu khuôn mới vào | 10' | 🔴 → Pre-stage trên cart: 3'! |\n| 6 | Lắp 8 bolt + clamp | 15' | 🔴 → Hydraulic clamp: 2'! |\n| 7 | Chỉnh stroke + pressure | 15' | 🔴 → Recipe PLC: 1'! |\n| 8 | ALIGNMENT khuôn | 20' | 🔴 → Cassette + locating pin: 0'! |\n| 9 | Chạy thử 5 shot | 15' | 🔴 → Recipe chính xác → 5'! |\n| 10 | First piece check | 25' | 🔴 → GO/NOGO gauge: 8'! |\n\nPhát hiện: Chờ crane 20' + Alignment 20' + Bolt 30' = 70' (47%) = CÓ THỂ LOẠI BỎ!",
            "result": "SMED Kaizen — Cassette Die System!\n\nConcept: Khuôn pre-mounted trên BASE PLATE CHUẨN → locating pin → ĐẨY VÀO → PIN TỰ KHỚP → KHÔNG CẦN ALIGNMENT!\n\n| Thay đổi | Trước | Sau | Tiết kiệm |\n| Crane → Roller cart pre-stage khuôn bên cạnh máy | 30' (cẩu + chờ!) | 6' (đẩy!) | -24' |\n| 16 bolt → Hydraulic die clamp (1 nút bấm!) | 30' | 4' | -26' |\n| Alignment thủ công → Cassette + locating pin (tự khớp!) | 20' | 0' | -20' |\n| Stroke/pressure thủ công → Recipe PLC auto | 15' | 1' | -14' |\n| Chạy thử dài → First shot + GO/NOGO | 40' | 13' | -27' |\n\nTỔNG: 150 phút → 25 phút! GIẢM 83%!\n• Mỗi ca thêm 6 giờ sản xuất! (Từ 680 triệu\n• Payback: Thêm 6h × 30 ngày × output → Payback 4 tháng!"
        },
        {
            "title": "Đổi màu sơn ô tô 35' → 7'! Pig System = Thu hồi 98% sơn!",
            "industry": "Ô tô",
            "situation": "Line sơn robot: đổi màu 15 LẦN/CA → mỗi lần 35 phút → 8.75 giờ/ca = SETUP! → Máy sơn chỉ SẢN XUẤT < 40% thời gian!",
            "analysis": "Video Analysis — Color Change Paint Line:\n\n| # | Bước | Thời gian | Nhận xét |\n| 1 | FLUSH sơn cũ trong ống (bơm dung môi rửa!) | 12' | 🔴 → PIG SYSTEM: 2'! |\n| 2 | Rửa bình chứa sơn (spray head) | 8' | 🔴 → Auto flush: 3'! |\n| 3 | Nạp sơn mới | 5' | 🔴 → Quick change valve: 1'! |\n| 4 | Chỉnh spray pattern (quạt, áp) | 5' | 🔴 → Recipe auto: 0.5'! |\n| 5 | Test spray trên panel thử | 5' | 🔴 → Skip nếu proven recipe: 0'! |\n\nFLUSH = 35% thời gian + LÃNG PHÍ DUNG MÔI + LÃNG PHÍ SƠN!\nMỗi lần flush = 3 lít dung môi + 0.5 lít sơn mất = 15 lần × 3.5 lít = 52.5 lít/CA!",
            "result": "SMED Game-changer: PIG SYSTEM!\n\nConcept: \"PIG\" (heo) = viên bi cao su → bơm qua ống → ĐẨY SƠN CŨ ra → ống sạch → nạp sơn mới!\n• Pig đẩy = thu hồi 98% sơn cũ (thay vì flush bỏ hết!)\n• KHÔNG CẦN dung môi rửa (tiết kiệm 52 lít/ca!)\n\n| Thay đổi | Trước | Sau | Tiết kiệm |\n| Flush dung môi → Pig system | 12' | 2' | -10' |\n| Rửa bình → Auto quick-flush | 8' | 3' | -5' |\n| Nạp sơn → Quick color change valve (đổi bình tức thì!) | 5' | 1' | -4' |\n| Spray pattern → Robot recipe auto | 5' | 0.5' | -4.5' |\n| Test spray → Skip (proven recipe) | 5' | 0.5' | -4.5' |\n| Scheduling: Sơn nhạt → đậm (WHITE → GRAY → BLACK → RED → ...) → GIẢM flush! | — | — | -30% flush thêm! |\n\nTỔNG: 35 phút → 7 phút! GIẢM 80%!\n• 15 lần × 28 phút tiết kiệm = 7 giờ thêm sản xuất/ca!\n• Dung môi tiết kiệm: 52 lít/ca × 300 ngày = 15,600 lít/năm = 78 triệu VND!\n• Sơn thu hồi: 7.5 lít/ca × 300 = 2,250 lít/năm = 450 triệu VND!"
        }
    ]
}
