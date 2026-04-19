method = {
    "id": 2,
    "title": "Bottleneck Loss Analysis - Phân tích tổn thất nút thắt",
    "short_name": "Bottleneck Loss Analysis",
    "icon": "📉",
    "pillar": "Focus Improvement",
    "description": "Đã tìm ra bottleneck rồi → Giờ PHÂN TÍCH CHI TIẾT: Tổn thất nào lớn nhất? Mất bao nhiêu tấn/giờ/tiền? Cải tiến đâu trước?",
    "meaning": """
<p><strong>Bottleneck Loss Analysis (Phân tích tổn thất tại nút thắt)</strong> là bước TIẾP THEO sau khi đã xác định bottleneck (method 1). Thay vì chỉ biết "máy nào là bottleneck", phương pháp này đi SÂU hơn: <em>Tại sao bottleneck chỉ đạt 52% năng lực? 48% còn lại MẤT Ở ĐÂU?</em></p>
<p><em>Hình dung: Bạn biết cổ chai là chỗ hẹp (bottleneck). Nhưng cổ chai còn bị đầy cặn bẩn (losses) → nước chảy còn CHẬM HƠN NỮA! Phân tích losses = dọn sạch cặn bẩn trong cổ chai!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 6 tổn thất lớn (Six Big Losses) tại Bottleneck</div>
    <p><strong>AVAILABILITY LOSSES (Tổn thất thời gian — máy DỪNG)</strong>:<br>
    ① <strong>Breakdown (Hỏng máy)</strong>: Máy hỏng đột ngột, dừng ngoài kế hoạch<br>
    ② <strong>Setup/Changeover (Chuyển đổi)</strong>: Thời gian đổi sản phẩm, đổi khuôn, đổi die<br><br>
    <strong>PERFORMANCE LOSSES (Tổn thất tốc độ — máy CHẠY CHẬM)</strong>:<br>
    ③ <strong>Minor Stops/Idling (Dừng vặt)</strong>: Dừng < 5 phút (kẹt liệu, gỡ sản phẩm, sensor lỗi...)<br>
    ④ <strong>Speed Loss (Giảm tốc)</strong>: Máy chạy DƯỚI tốc độ thiết kế (vì NL xấu, mòn, cài đặt sai...)<br><br>
    <strong>QUALITY LOSSES (Tổn thất chất lượng — sản phẩm LỖI)</strong>:<br>
    ⑤ <strong>Startup Reject (Phế khởi động)</strong>: Sản phẩm lỗi khi khởi động máy, chỉnh máy đầu ca<br>
    ⑥ <strong>Production Defect (Phế trong SX)</strong>: Sản phẩm lỗi phát sinh trong quá trình sản xuất<br><br>
    <em>→ OEE tại Bottleneck = Availability × Performance × Quality → MỌI cải tiến ở đây đều TĂNG sản lượng TOÀN DÂY CHUYỀN!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Định lượng CHÍNH XÁC từng loại tổn thất tại bottleneck (bao nhiêu giờ? bao nhiêu tấn? bao nhiêu tiền?)</li>
    <li>Xác định tổn thất LỚN NHẤT → ưu tiên cải tiến CHỖ NÀY TRƯỚC (Pareto — 20% nguyên nhân gây 80% tổn thất)</li>
    <li>Tính OEE cục bộ tại bottleneck — đây là OEE QUAN TRỌNG NHẤT vì nó quyết định sản lượng dây chuyền!</li>
    <li>Ước tính LỢI ÍCH TÀI CHÍNH của từng phương án cải tiến → thuyết phục BGĐ bằng số tiền tiết kiệm!</li>
    <li>Thiết lập KPI (chỉ số đo lường) theo dõi hiệu quả cải tiến theo thời gian</li>
    <li>Khác biệt với method 1: Method 1 = BIẾT bottleneck ở đâu. Method 2 = BIẾT CẢI TIẾN bottleneck BẰNG CÁCH NÀO!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định bottleneck (dùng Method 1)</div>
        <div class="step-card__desc">Dùng Bottleneck Analysis (method 1) để xác định máy/công đoạn nghẽn. Nếu đã biết rồi → bắt đầu ngay bước 2. Lưu ý: Chỉ phân tích loss tại BOTTLENECK! Phân tích loss ở máy không phải bottleneck → cải tiến cũng KHÔNG TĂNG sản lượng dây chuyền!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Thu thập dữ liệu tổn thất 2-4 tuần</div>
        <div class="step-card__desc">Ghi nhận CHI TIẾT mọi tổn thất tại bottleneck trong 2-4 tuần (đủ đại diện): Mỗi lần dừng máy: thời gian? nguyên nhân? Tốc độ thực vs thiết kế: chênh bao nhiêu? Phế phẩm: bao nhiêu? loại gì? Dùng log sheet (phiếu ghi), CMMS, hoặc sensor tự động. QUAN TRỌNG: Ghi TRUNG THỰC! Nếu che giấu loss → không cải tiến được!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Phân loại theo 6 Big Losses + Vẽ Pareto</div>
        <div class="step-card__desc">Phân loại mỗi loss vào 6 nhóm: Breakdown, Setup, Minor Stop, Speed Loss, Startup Reject, Production Defect. Quy đổi TẤT CẢ ra CÙNG ĐƠN VỊ: giờ mất hoặc tấn mất hoặc VND mất. Vẽ Pareto chart (method 25): Top 1-3 losses chiếm 70-80% tổng → ĐÂY là mục tiêu cải tiến!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Root cause + Action plan + Theo dõi KPI</div>
        <div class="step-card__desc">Cho TOP losses: Dùng Why-Why (method 18), C-E Analysis (method 3), FMEA (method 4) để tìm nguyên nhân gốc. Đề xuất giải pháp cụ thể + tính ROI (lợi tức đầu tư). Theo dõi OEE bottleneck hàng tuần → trend tăng = cải tiến hiệu quả! Lặp lại: Khi cải tiến xong loss lớn nhất → loss thứ 2 trở thành lớn nhất → tiếp tục Pareto!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Pellet Mill OEE 52% → 68% — Changeover die là loss #1!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Pellet Mill (máy ép viên) đã được xác định là bottleneck (method 1). OEE chỉ 52%! 48% năng lực bị MẤT ở đâu?",
            "analysis": "Thu thập 4 tuần dữ liệu, phân loại 6 Big Losses:\n\n| # | Loại Loss | Giờ mất/tuần | % tổng loss |\n| ① | Breakdown (hỏng máy đột ngột) | 15h | 30% |\n| ② | Changeover die (đổi khuôn ép) | 12h | 24% |\n| ④ | Speed loss (chạy chậm do steam kém) | 8h | 16% |\n| ③ | Minor stops (kẹt liệu, sensor) | 6h | 12% |\n| ⑥ | Production defect (viên bể, bụi) | 5h | 10% |\n| ⑤ | Startup reject (viên lỗi đầu ca) | 4h | 8% |\n\nPareto: Breakdown (30%) + Changeover (24%) = 54% tổng loss! → Chỉ cần giải quyết 2 vấn đề này = giải quyết HƠN NỬA tổn thất!\n\nPhân tích sâu changeover:\n• Thay die: 45 phút/lần × 4 lần/tuần = 3 giờ (internal — máy DỪNG)\n• Thay roller: 30 phút/lần × 3 lần/tuần = 1.5 giờ\n• Chờ die nguội + tháo die nóng: 15 phút/lần → LÃNG PHÍ (có thể làm trước!)",
            "result": "Action plan theo thứ tự Pareto:\n\nPriority 1 — Giảm Breakdown (15h → 8h):\n• PM (Planned Maintenance) định kỳ cho die: Kiểm tra mòn → thay TRƯỚC KHI nứt\n• CBM (Condition-Based Maintenance): Lắp sensor rung → phát hiện bạc đạn sắp hỏng\n\nPriority 2 — Giảm Changeover (12h → 4h):\n• SMED (method 22): Phân tách Internal/External → chuẩn bị die mới + công cụ TRƯỚC KHI dừng máy\n• Quick clamp thay vì bulong → thay die nhanh hơn 50%\n\nKết quả: OEE: 52% → 68% (+16%) = Sản lượng dây chuyền tăng 31%!\n→ Bài học: Phân tích loss TRƯỚC → biết CẢI TIẾN ĐÂU TRƯỚC → không lãng phí effort vào loss nhỏ!"
        },
        {
            "title": "Máy CNC 5 trục — Setup chiếm 22% thời gian, OEE chỉ 50%!",
            "industry": "Cơ khí",
            "situation": "Xưởng gia công: Máy CNC 5 trục là bottleneck (đắt nhất, khó mua thêm). Chạy 24/7 nhưng KHÔNG ĐỦ đơn hàng. OEE chỉ 50%.",
            "analysis": "Loss breakdown tại CNC 5 trục:\n\n| # | Loại Loss | % thời gian |\n| ② | Setup (gá phôi, chỉnh jig, load chương trình) | 22% |\n| ④ | Speed loss (chạy chậm vì tool mòn) | 15% |\n| ③ | Minor stop (tool change tự động lỗi) | 3% |\n| — | Chờ chương trình NC (lập trình viên chưa xong!) | 8% |\n| ⑥ | Scrap (phế phẩm do sai kích thước) | 5% |\n\nInsight quan trọng: \"Chờ chương trình NC 8%\" KHÔNG NẰM trong 6 Big Losses truyền thống → nhưng đây là loss THỰC TẾ rất lớn → Bottleneck ĐANG CHỜ bộ phận khác (lập trình)!\n\nSetup 22% chi tiết:\n• Gá phôi: 12 phút (phải canh chỉnh bằng đồng hồ)\n• Load chương trình + set tool offset: 8 phút\n• Chạy thử + đo kiểm: 10 phút\n→ Tổng 30 phút/job × 8 job/ngày = 240 phút = 4 giờ MẤT mỗi ngày!",
            "result": "Cải tiến theo Pareto:\n\nPriority 1 — Setup 22% → mục tiêu 9%:\n• Tool PRESET ngoài máy: Đo và set tool offset trên máy đo ngoài → Load vào máy = 0 phút setup tool\n• Modular fixture (jig module): Thay vì chỉnh từng chi tiết → snap-in jig → gá 12 phút → 3 phút\n• Chương trình NC verify bằng simulation TRƯỚC → bỏ chạy thử\n\nPriority 2 — Chờ NC 8% → 2%:\n• Lập trình viên làm trước 1 ngày (queue chương trình sẵn sàng) → máy KHÔNG BAO GIỜ CHỜ\n\nKết quả: OEE: 50% → 72%! = Thêm 5 giờ sản xuất/ngày trên máy CNC đắt nhất!\n→ Bài học: Bottleneck loss không chỉ từ MÁY — còn từ bộ phận HỖ TRỢ (lập trình, vật tư, QC)!"
        },
        {
            "title": "Máy đóng chai — Minor stops 15%, cap jam liên tục!",
            "industry": "Đồ uống",
            "situation": "Máy filling (chiết rót) nước giải khát: Tốc độ thiết kế 600 chai/phút, thực tế chỉ 420 chai/phút. Máy CHẠY nhưng hay DỪM VẶT!",
            "analysis": "Loss breakdown:\n\n| # | Loại Loss | % |\n| ③ | Minor stops — Cap jam (kẹt nắp) | 15% |\n| ④ | Speed loss — Filler valve leak → chạy chậm | 12% |\n| ② | Changeover (đổi sản phẩm/kích cỡ chai) | 8% |\n| ⑤ | Startup reject (chai đầu đổ sản phẩm) | 3% |\n\nMinor stops là \"kẻ giết thầm lặng\"!\n• Mỗi lần kẹt nắp: chỉ 10-30 giây → operator gỡ → chạy tiếp\n• Nhưng xảy ra 40-60 lần/ca! → 10-30 giây × 50 lần = 8-25 phút/ca!\n• Vì quá ngắn nên KHÔNG AI GHI → \"invisible loss\" (tổn thất vô hình)\n• NHƯNG tích lũy = 15% tổng thời gian! = 108 phút/ngày = 1.8 giờ MẤT mỗi ngày!",
            "result": "Cải tiến:\n\nPriority 1 — Cap jam 15%:\n• Root cause: Cap feeder (bộ cấp nắp) cũ, rail bị mòn → nắp lật nghiêng → kẹt\n• Action: Thay cap feeder mới + vệ sinh rail hàng ca (AM — Autonomous Maintenance)\n→ Minor stops: 50 lần → 5 lần/ca\n\nPriority 2 — Speed loss 12%:\n• Root cause: Filler valve seal mòn → leak → rót không đủ → máy tự giảm tốc\n• Action: Overhaul filler valve + PM seal định kỳ\n→ Tốc độ: 420 → 540 chai/phút\n\nKết quả: Tốc độ thực: 420 → 540 chai/phút (tăng 29%!)\n→ Bài học: Minor stops nhỏ nhưng TÍCH LŨY rất lớn! Vì quá nhỏ nên không ai ghi → cần ĐO LƯỜNG bằng counter/sensor!"
        },
        {
            "title": "Máy phun nhựa — Cooling time dài + changeover khuôn tốn 18%!",
            "industry": "Nhựa",
            "situation": "Máy phun nhựa 650 tấn: Cycle time thiết kế 25 giây, thực tế 35 giây. OEE chỉ 48%. Sản lượng thấp hơn mục tiêu 40%.",
            "analysis": "Loss breakdown 35 giây thực tế vs 25 giây thiết kế:\n\nPhân tích từng giai đoạn cycle (xem method 39 — Standard Reflection):\n| Giai đoạn | Thiết kế | Thực tế | Gap |\n| Injection (phun) | 3s | 3s | OK |\n| Packing (giữ áp) | 4s | 5s | +1s |\n| Cooling (làm mát) | 12s | 20s | +8s ‼️ |\n| Eject + Mold open/close | 6s | 7s | +1s |\n\nCooling = +8 giây = gap LỚN NHẤT! = 80% tổng speed loss!\n\nThêm losses khác:\n• Changeover khuôn: 18% thời gian (1.5 giờ/lần × 3 lần/ngày = 4.5 giờ/ngày!)\n• Reject flash/short shot: 7%\n• Dừng gỡ sản phẩm dính khuôn (robot lấy sản phẩm lỗi): 5%",
            "result": "Cải tiến theo Pareto:\n\nPriority 1 — Cooling time +8s:\n• Root cause: Kênh nước làm mát trong khuôn BỊ TẮC (cáu cặn) → nước chảy yếu → mát chậm\n• Action: Vệ sinh kênh nước bằng hóa chất tẩy cặn + lắp bộ lọc nước → Cooling: 20s → 13s!\n• Bonus: Packing cũng giảm vì sản phẩm cứng nhanh hơn → 5s → 4s\n\nPriority 2 — Changeover 18%:\n• SMED: Quick clamp thay bulong + magnetic clamping plate → Changeover: 1.5h → 30 phút!\n\nKết quả: Cycle time: 35s → 26s. OEE: 48% → 65%. Sản lượng tăng 35%!\n→ Bài học: Cooling time = \"hidden loss\" rất lớn trong ép nhựa — kiểm tra KÊNH NƯỚC khuôn thường xuyên!"
        },
        {
            "title": "Lab QC Dược phẩm — Bottleneck KHÔNG PHẢI MÁY mà là QUY TRÌNH!",
            "industry": "Dược phẩm",
            "situation": "Lab QC là bottleneck giải phóng lô hàng (batch release). Trung bình 5 ngày để có kết quả → Tồn kho thành phẩm chờ QC release rất lớn → Vốn bị \"chôn\"!",
            "analysis": "Loss breakdown 5 ngày TAT (Turnaround Time):\n\n| # | Loss | Thời gian | % |\n| 1 | Chờ thiết bị HPLC (máy sắc ký) | 1.5 ngày | 30% |\n| 2 | Chuẩn bị mẫu lặp (triplicate — làm 3 lần!) | 1.0 ngày | 20% |\n| 3 | Chờ phê duyệt manager (ký giấy!) | 0.75 ngày | 15% |\n| 4 | Chờ hóa chất/dung môi (hết stock!) | 0.5 ngày | 10% |\n| 5 | Phân tích thực tế (chạy HPLC, đo, tính) | 1.0 ngày | 20% |\n| 6 | Khác (ghi chép, nhập dữ liệu) | 0.25 ngày | 5% |\n\nInsight QUAN TRỌNG: Phân tích thực tế (chạy máy, đo) chỉ chiếm 20%! 80% còn lại là CHỜM ĐỢI! (chờ máy, chờ hóa chất, chờ sếp ký!)",
            "result": "Cải tiến theo Pareto:\n\nPriority 1 — Chờ HPLC 30%:\n• Mua thêm 1 máy HPLC (đầu tư 1.5 tỷ VND) → máy luôn available\n• Scheduling: Sắp xếp lịch chạy HPLC → không xung đột giữa các lô\n\nPriority 2 — Chờ phê duyệt 15%:\n• E-signature (chữ ký điện tử) → manager ký trên điện thoại → không cần chờ sếp về bàn!\n\nPriority 3 — Giảm lặp mẫu 20%:\n• Risk-based testing: Sản phẩm đã validated ổn định → giảm triplicate thành duplicate (từ 3 → 2 lần)\n\nKết quả: TAT: 5 ngày → 2.5 ngày! Tồn kho chờ release GIẢM 50% → giải phóng hàng tỷ VND vốn lưu động\n→ Bài học: Loss analysis áp dụng CHO CẢ quy trình dịch vụ/hành chính — và thường CHỜ ĐỢI chiếm 70-80% tổng thời gian!"
        },
        {
            "title": "Kho e-commerce — Trạm đóng gói nghẽn, 60% chờ đợi!",
            "industry": "Thương mại điện tử",
            "situation": "Kho fulfillment: Trạm đóng gói là bottleneck. Capacity: 500 đơn/ca nhưng nhận 800 đơn/ca. Đơn chậm → khách phàn nàn, rate 1 sao!",
            "analysis": "Loss breakdown tại trạm đóng gói:\n\n| # | Loss | % thời gian | Ghi chú |\n| 1 | Chờ hàng từ picking (lấy hàng) | 25% | Picker chọn sai kệ, đi lòng vòng |\n| 2 | Tìm vật tư đóng gói (hộp, xốp, băng keo) | 10% | Bàn đóng gói BỪA BỘN → tìm mất 2-3 phút |\n| 3 | Thiếu bao bì phù hợp (size không khớp) | 8% | Hộp quá to cho sản phẩm nhỏ → phải tìm hộp khác |\n| 4 | In label lỗi (printer kẹt, mực hết) | 5% | Printer cũ, không có backup |\n| 5 | Đóng gói thực tế | 52% | Thao tác đóng gói, quét barcode, dán label |\n\nInsight: Đóng gói thực tế chỉ chiếm 52% → 48% là LÃNG PHÍ! (chờ hàng, tìm đồ, thiếu vật tư, printer lỗi)",
            "result": "Cải tiến:\n\nPriority 1 — Chờ picking 25%:\n• Zone picking theo wave: Nhóm đơn hàng theo khu vực kho → picker đi 1 vòng lấy NHIỀU đơn → nhanh hơn 40%\n• Đưa hàng đến trạm đóng gói bằng conveyor → packer KHÔNG CẦN CHỜ\n\nPriority 2 — Tìm vật tư 10%:\n• 5S bàn đóng gói: Mỗi loại vật tư có VỊ TRÍ CỐ ĐỊNH (shadow board)\n• Kit vật tư đóng gói: Mỗi loại đơn có kit chuẩn (hộp + xốp + label + tape) chuẩn bị SẴN\n\nPriority 3 — Bao bì 8%:\n• Chuẩn hóa 4 size hộp thay vì 12 size → dễ tìm, dễ trữ\n\nKết quả: Từ 500 → 750 đơn/ca (tăng 50%!)\n→ Bài học: Loss analysis = THẤY được lãng phí ẨN trong mọi quy trình → 48% thời gian packer không đóng gói mà đi TÌM ĐỒ!"
        },
        {
            "title": "Lò hơi — Tube leak gây dừng 10%, mất 800 triệu/năm!",
            "industry": "Tiện ích",
            "situation": "Lò hơi 30 T/h cung cấp steam cho toàn nhà máy — bottleneck utility. Năng lực: 30 T/h nhưng thực tế chỉ 22 T/h ổn định. Thiếu steam → nhiều dây chuyền phải GIẢM TẢI!",
            "analysis": "Loss breakdown:\n\n| # | Loss | % ảnh hưởng | Tác động tiền |\n| 1 | Tube leak (rò ống) — unplanned stop | 10% | 800 triệu/năm |\n| 2 | Burner fouling (đầu đốt bẩn) → giảm hiệu suất | 8% | Tốn thêm nhiên liệu |\n| 3 | CIP blowdown quá thường xuyên | 5% | Mất nước nóng + hóa chất |\n| 4 | Startup sau weekend (nâng nhiệt chậm) | 5% | Mất 5 giờ mỗi thứ 2 |\n\nTube leak = loss #1 và NGUY HIỂM nhất!\n• Mỗi lần rò ống: Dừng lò 24-72 giờ (hạ nhiệt → sửa → nâng nhiệt lại)\n• 3 lần/năm × 48h = 144 giờ dừng = 10% availability\n• Thiếu steam → 5 dây chuyền SX dừng/giảm tải → thiệt hại DÂY CHUYỀN\n• Root cause: Ống 15 năm, nước cấp không xử lý đủ → ăn mòn + tích cáu",
            "result": "Cải tiến theo Pareto:\n\nPriority 1 — Tube leak 10%:\n• PM tube inspection (kiểm tra ống định kỳ): Đo độ dày ống bằng siêu âm (UT) 6 tháng/lần → thay ống MỎNG trước khi rò\n• Water treatment upgrade: Xử lý nước cấp đạt chuẩn → giảm ăn mòn + cáu\n→ Tube leak: 3 lần/năm → 0 lần!\n\nPriority 2 — Burner fouling 8%:\n• Vệ sinh burner 2 tuần/lần (thay vì chờ tắc) → hiệu suất đốt tăng 5%\n\nPriority 3 — Blowdown 5%:\n• Auto blowdown controller: Xả tự động theo TDS (Total Dissolved Solids) → không xả thừa\n\nKết quả: Steam output: 22 → 28 T/h (tăng 27%!) Toàn nhà máy chạy đủ steam!\n→ Bài học: Bottleneck UTILITY (lò hơi, khí nén, điện) ảnh hưởng TOÀN NHÀ MÁY — loss ở đây = mất sản lượng NHIỀU dây chuyền!"
        }
    ]
}
