method = {
    "id": 15,
    "title": "Trend Analysis - Phân tích xu hướng",
    "short_name": "Trend Analysis",
    "icon": "📈",
    "pillar": "Planned Maintenance",
    "description": "Theo dõi dữ liệu THEO THỜI GIAN: Rung tăng DẦN? Chiều dày GIẢM DẦN? → DỰ ĐOÁN khi nào HỎNG → BẢO TRÌ ĐÚNG LÚC!",
    "meaning": """
<p><strong>Trend Analysis (Phân tích xu hướng)</strong> là phương pháp theo dõi SỰ THAY ĐỔI của dữ liệu THEO THỜI GIAN để nhận diện <strong>xu hướng (tăng/giảm/ổn định/chu kỳ)</strong> và <strong>DỰ ĐOÁN</strong> tình trạng TƯƠNG LAI.</p>
<p><em>Hình dung: Bác sĩ theo dõi đường huyết bệnh nhân MỖI THÁNG: 100 → 110 → 120 → 130 → 140 → DỰ ĐOÁN: 6 tháng nữa = ĐÁI THÁO ĐƯỜNG nếu không can thiệp! Tương tự: Vibration bearing tăng dần 2.5 → 3.5 → 4.5 → 5.5 mm/s → DỰ ĐOÁN: 3 tháng nữa = CHÁY BEARING nếu không thay!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 4 loại xu hướng — Nhận diện ĐÚNG = Hành động ĐÚNG!</div>
    <p><strong>1. Linear trend (Tuyến tính)</strong>: Tăng/giảm ĐỀU ĐẶN → Mòn cơ khí, ăn mòn, mỏi → LÊN LỊCH thay<br>
    <strong>2. Exponential trend (Lũy thừa)</strong>: Tăng NHANH DẦN (càng ngày càng nhanh!) → Hỏng SẮP xảy ra! → HÀNH ĐỘNG GẤP!<br>
    <strong>3. Cyclic/Seasonal (Chu kỳ)</strong>: Lặp lại theo mùa/tuần/ca → Lập kế hoạch theo PATTERN → PM trước mùa peak!<br>
    <strong>4. Step change (Đột biến)</strong>: Thay đổi ĐỘT NGỘT → Có sự kiện (thay NVL, sửa máy, tai nạn) → TÌM NGUYÊN NHÂN!<br><br>
    <em>Trend Analysis = nền tảng của CBM (Condition-Based Maintenance) và PdM (Predictive Maintenance) → bảo trì THEO TÌNH TRẠNG THỰC TẾ thay vì theo LỊCH cố định!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>DỰ ĐOÁN thời điểm hỏng hóc TRƯỚC KHI xảy ra — P-F Interval (thời gian từ lúc phát hiện P đến lúc hỏng F) → CAN THIỆP trong cửa sổ này!</li>
    <li>LÊN LỊCH bảo trì TỐI ƯU dựa trên TÌNH TRẠNG THỰC TẾ → không quá sớm (lãng phí!) + không quá trễ (breakdown!)</li>
    <li>PHÁT HIỆN SỚM suy giảm hiệu suất: OEE giảm dần? Energy tăng dần? → CAN THIỆP khi còn nhỏ → trước khi thành BIG PROBLEM!</li>
    <li>GIẢM over-maintenance (bảo trì quá mức): Thay bearing 6 tháng/lần → nhưng trend cho thấy bearing CÒN TỐT → kéo dài 9 tháng → tiết kiệm!</li>
    <li>Hỗ trợ quyết định THAY THẾ vs SỬA: MTBF giảm dần → đến lúc nào thì chi phí sửa > chi phí thay MỚI?</li>
    <li>ĐÁNH GIÁ hiệu quả cải tiến: Trước kaizen OEE = 65% → sau kaizen tăng → nhưng có BỀN VỮNG không? → Trend 6 tháng sau cho biết!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định THÔNG SỐ + BASELINE — Đo cái gì? Mức bình thường là bao nhiêu?</div>
        <div class="step-card__desc">Chọn LEADING INDICATORS (chỉ số dẫn trước — thay đổi TRƯỚC KHI hỏng): <strong>Vibration (rung)</strong>: Bearing, motor, pump, fan. <strong>Temperature (nhiệt)</strong>: Motor, bearing, transformer, tủ điện. <strong>Pressure (áp suất)</strong>: Filter ΔP, hydraulic, pneumatic. <strong>Oil analysis (dầu)</strong>: Fe ppm (mạt sắt), water, viscosity. <strong>Thickness (chiều dày)</strong>: Ống, bồn, boiler tube (ăn mòn). <strong>Insulation Resistance (IR)</strong>: Motor, cable. <strong>Process KPI</strong>: OEE, yield, SEC (specific energy consumption). Với mỗi thông số: Xác định BASELINE (giá trị bình thường): Vd. Rung motor lúc mới = 2.0 mm/s → đây là baseline! Xác định ALARM và ACTION limits: Warning = 4.5 mm/s. Action/Trip = 7.1 mm/s.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Thu thập dữ liệu ĐỊNH KỲ — Cùng điều kiện, cùng cách đo!</div>
        <div class="step-card__desc">Tần suất đo phụ thuộc CRITICALITY (mức quan trọng): Critical equipment: Hàng tuần hoặc ONLINE (liên tục). Important: Hàng tháng. General: Hàng quý. Ghi vào CMMS/Excel: Ngày đo + giá trị + điều kiện vận hành (tải, RPM, nhiệt môi trường). QUAN TRỌNG: Đo CÙNG ĐIỀU KIỆN mỗi lần! (Cùng tải, cùng điểm đo, cùng dụng cụ) → Nếu điều kiện khác → KHÔNG SO SÁNH ĐƯỢC → trend vô nghĩa!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: VẼ TREND CHART + Phân tích xu hướng</div>
        <div class="step-card__desc">Vẽ biểu đồ: Trục X = thời gian. Trục Y = giá trị đo được. Thêm các đường: BASELINE (giá trị ban đầu — ngang), ALARM limit (vàng — cẩn thận!), ACTION limit (đỏ — hành động NGAY!), TREND LINE (đường xu hướng — hồi quy linear/polynomial). Phân tích: HÌNH DÁNG xu hướng? Linear? Exponential? Cyclic? Step? TỐC ĐỘ thay đổi? Nhanh hay chậm? Tăng tốc không? Có OUTLIER (điểm bất thường) không? → Kiểm tra: đo sai? hay có sự kiện đặc biệt?</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: DỰ ĐOÁN + LÊN KẾ HOẠCH — Bao giờ đến LIMIT?</div>
        <div class="step-card__desc">EXTRAPOLATE (ngoại suy) trend line → DỰ ĐOÁN: Bao giờ đạt ALARM limit? → BẮT ĐẦU lên kế hoạch PM! Bao giờ đạt ACTION limit? → DEADLINE phải xong PM! Bao giờ HỎNG (failure)? → Deadline TUYỆT ĐỐI! Ví dụ: Vibration trend = +0.5 mm/s/tháng. Hiện tại = 4.0 mm/s. Alarm = 7.0. → (7.0 — 4.0) / 0.5 = 6 tháng → LÊN LỊCH thay bearing THÁNG THỨ 4 (trước alarm 2 tháng = AN TOÀN!). Kết hợp với SHUTDOWN PLAN: Thay trong lúc planned shutdown → KHÔNG ảnh hưởng sản xuất!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Vibration trend bearing — Từ 2.5 → 4.8 mm/s trong 6 tháng → THAY trước 3 tháng!",
            "industry": "Sản xuất",
            "situation": "Motor 200kW quạt ID fan lò hơi — CRITICAL equipment (hỏng = mất hơi = DỪNG nhà máy!). Theo dõi vibration hàng tháng bằng máy đo cầm tay.",
            "analysis": "Trend data vibration — 6 tháng:\n\n| Tháng | Vibration (mm/s) |\n| T1 (baseline) | 2.5 |\n| T2 | 2.8 |\n| T3 | 3.2 |\n| T4 | 3.6 |\n| T5 | 4.0 |\n| T6 | 4.8 ← Tốc độ tăng NHANH HƠN! |\n\nPhân tích xu hướng:\n• Tháng 1-5: Linear trend +0.4 mm/s/tháng\n• Tháng 6: JUMP lên +0.8 mm/s! → Trend CHUYỂN từ linear → EXPONENTIAL! → Bearing bắt đầu hỏng tiến triển!\n• Alarm limit: 7.1 mm/s (ISO 10816 Zone C — motor > 100kW)\n• Action limit: 11.0 mm/s (Zone D — NGUY HIỂM!)\n\nDự đoán (extrapolate):\n• Nếu tăng linear 0.4/tháng → đạt alarm tháng T12 (6 tháng nữa)\n• NHƯNG trend ĐÃ exponential → có thể đạt alarm tháng T9 (3 tháng nữa!)→ PHẢI action SỚM!",
            "result": "Hành động dựa trên trend:\n\n• T6 (hiện tại = 4.8): Tăng tần suất đo từ HÀNG THÁNG → HÀNG TUẦN → theo dõi SÁT hơn!\n• T7: ORDER bearing mới (lead time 2 tuần) → SẴN SÀNG trong kho!\n• T8: LÊN LỊCH thay bearing trong PLANNED SHUTDOWN tháng 9 → trước alarm 1 tháng = AN TOÀN!\n• T9: Thay bearing → vibration TRỞ VỀ 2.2 mm/s → DONE!\n\nChi phí so sánh:\n• Thay bearing THEO KẾ HOẠCH: 50 triệu (bearing + nhân công) + 8 giờ shutdown planned\n• Breakdown KHÔNG KẾ HOẠCH: 50 triệu bearing + 200 triệu mất sản lượng + 3 ngày dừng + CÓ THỂ hỏng motor (thêm 500 triệu!)\n→ Trend Analysis tiết kiệm: 650 triệu!\n\n→ Bài học: Vibration TĂNG DẦN = bearing ĐANG SUY YẾU! Trend Analysis = biết TRƯỚC 3 tháng → chuẩn bị → thay ĐÚng LÚC → ZERO downtime bất ngờ!"
        },
        {
            "title": "Oil analysis trend gearbox — Fe ppm EXPONENTIAL = Gear PITTING!",
            "industry": "Xi măng",
            "situation": "Gearbox ball mill 2,500kW — gearbox giá 3 TỶ! Nếu gãy răng = thay gearbox MỚI! Phân tích dầu hàng quý → theo dõi Fe ppm (mạt sắt trong dầu).",
            "analysis": "Trend data Fe ppm — 5 quý:\n\n| Quý | Fe (ppm) | Tốc độ tăng |\n| Q1 (baseline) | 25 | — |\n| Q2 | 35 | +10 |\n| Q3 | 48 | +13 |\n| Q4 | 72 | +24 ← Tăng GẤP ĐÔI! |\n| Q5 | 105 | +33 ← EXPONENTIAL! |\n\nPhân tích:\n• Normal Fe: GEAR ĐANG BỊ PITTING (rỗ bề mặt)!\n• Water content cũng tăng (120 ppm → 350 ppm!) → Nước trong dầu → ĂN MÒN gear → pitting!\n\nDự đoán:\n• Nếu xu hướng tiếp tục → Fe > 200 ppm trong 2 quý → NGUY CƠ GÃY RĂNG! → Thay gearbox 3 TỶ!",
            "result": "Hành động NGAY:\n\n• Q5 (105 ppm!): TĂNG tần suất phân tích dầu → HÀNG THÁNG (thay vì quý)\n• Thay dầu + flush: Thay toàn bộ dầu mới → loại bỏ mạt sắt + nước → GIẢM tốc độ hư hại\n• Sửa water ingress: Tìm nguồn nước lọt vào dầu → sửa seal + lắp breather desiccant → NGĂN nước!\n• Mở gearbox kiểm tra: Tận dụng shutdown kế hoạch → mở inspection cover → XÁC NHẬN pitting trên pinion → Polish (đánh bóng) vết pitting nhẹ → kéo dài tuổi thọ thêm 2 năm!\n• Không cần thay gearbox!: Sửa sớm = 150 triệu (thay dầu + sửa seal + polish). Thay mới = 3 TỶ!\n\n→ Bài học Oil Analysis Trend: Fe ppm = \"máu\" của gearbox! Fe TĂNG = gear đang \"CHẢY MÁU\" (mòn)! Trend EXPONENTIAL = CẤP CỨU! Action SỚM = cứu gearbox 3 tỷ bằng 150 triệu!"
        },
        {
            "title": "Boiler tube thickness — UT trend linear giảm 0.35mm/năm → Thay khi nào?",
            "industry": "Nhà máy nhiệt điện",
            "situation": "Ống lò hơi (boiler tube) bị ăn mòn/mài mòn từ bên trong. Đo chiều dày bằng UT (Ultrasonic Testing) hàng năm → determine REMAINING LIFE (tuổi thọ còn lại).",
            "analysis": "Trend data chiều dày ống — 5 năm:\n\n| Năm | Thickness (mm) | Wear rate |\n| Y1 (mới) | 6.0 | Baseline |\n| Y2 | 5.7 | -0.3 |\n| Y3 | 5.3 | -0.4 |\n| Y4 | 5.0 | -0.3 |\n| Y5 | 4.6 | -0.4 |\n\nPhân tích:\n• Trend: LINEAR giảm trung bình -0.35mm/năm\n• Min. thickness theo ASME: 3.5mm (dưới mức này → ÁP suất có thể gây NỔ!)\n\nDự đoán:\n• Remaining life = (4.6 — 3.5) / 0.35 = 3.14 năm ≈ 3 năm\n• → PHẢI thay ống trước năm Y8!\n• Lead time đặt ống mới: 6 tháng → ORDER trước Y7.5!\n• Planned overhaul gần nhất: Y7 → THAY TRONG overhaul Y7 = PERFECT TIMING!",
            "result": "Kế hoạch từ Trend Analysis:\n\n• Y5 (hiện tại): Xác nhận remaining life = 3 năm → BÁO CÁO BGĐ + lập budget\n• Y6: Phê duyệt budget + chọn NCC + ORDER ống mới (lead time 6 tháng)\n• Y6.5: Ống mới về kho → SẴN SÀNG\n• Y7 (overhaul): THAY cụm ống trong planned overhaul → 0 downtime thêm!\n• Tăng tần suất UT: Y6-Y7 → đo 6 tháng/lần (thay vì hàng năm) → theo dõi SÁT hơn khi gần limit!\n\nChi phí so sánh:\n• Thay ống THEO KẾ HOẠCH (trong overhaul): 500 triệu (ống + nhân công)\n• Ống NỔ KHÔNG KẾ HOẠCH: 500 triệu ống + 2 tỷ mất sản xuất (emergency shutdown 2 tuần!) + RỦI RO AN TOÀN!\n\n→ Bài học Trend thickness: LINEAR trend = DỰ ĐOÁN CHÍNH XÁC remaining life! 0.35mm/năm × 3 năm = thay lúc overhaul Y7 = PERFECT! Trend Analysis = BẢO TRÌ ĐÚNG LÚC — không sớm (lãng phí) + không trễ (nổ!)!"
        },
        {
            "title": "OEE trend sau Kaizen — Step change → rồi REGRESSION! Tại sao?",
            "industry": "Sản xuất",
            "situation": "Kaizen event 1 tuần trên Line 3 → OEE nhảy từ 62% → 75%! Nhưng 2 tháng sau → OEE quay về 68%! BGĐ hỏi: \"Kaizen THẤT BẠI à?\" → Trend Analysis giải đáp!",
            "analysis": "OEE trend weekly — 12 tuần sau Kaizen:\n\n| Tuần | OEE | Ghi chú |\n| Trước Kaizen (avg.) | 62% | Baseline |\n| W1 (ngay sau KZ) | 75% | ↑ STEP CHANGE! Mọi người hào hứng! |\n| W2 | 74% | Duy trì |\n| W3 | 73% | Đang tốt |\n| W4 | 72% | Bắt đầu giảm nhẹ |\n| W5 | 70% | ↓ Regression bắt đầu! |\n| W6 | 69% | Tiếp tục giảm |\n| W8 | 68% | Ổn định ở 68% — vẫn cao hơn 62% nhưng KHÔNG ĐẠT 75%! |\n| W10 | 67% | Tiếp tục giảm? |\n| W12 | 68% | Ổn định 68% |\n\nPhân tích trend pattern:\n• STEP CHANGE tại W1: +13% (62 → 75) → Kaizen TẠO RA tác dụng THẬT!\n• REGRESSION W4-W8: Từ 75 → 68 → mất 7% → Sustainability issue!\n• Tại sao regression? → 5S quay về cũ! → SOP mới không được tuân thủ! → Quản lý ca không follow-up! → Mọi người \"quên\" → quay về thói quen CŨ!",
            "result": "Action để DUY TRÌ kết quả Kaizen:\n\n• Daily Management System: Họp 10 phút đầu ca → xem OEE hôm qua → nếu Standard Work audit: Trưởng ca đi gemba (hiện trường) → kiểm tra operator CÓ ĐANG LÀM theo SOP mới không → HÀNG NGÀY!\n• Visual Management: Bảng OEE TREO TẠI LINE → MỌI NGƯỜI thấy → áp lực xã hội → DUY TRÌ!\n• Kết quả sau 4 tuần thêm:\nW12 = 68% → W16 = 72% → W20 = 73% → Ổn định 73%!\n\n→ Kaizen KHÔNG thất bại! Kaizen tạo step change 62→75%, regression về 68% (vẫn +6% so với baseline!). Thêm Daily Management → ổn định 73% (+11% so với baseline!)\n\n→ Bài học Trend + Kaizen: Trend Analysis phát hiện REGRESSION (quay lại thói quen cũ) → NẾU không theo dõi trend → tưởng \"kaizen thất bại\" → SỰ THẬT: kaizen tạo step change + cần SUSTAINABILITY SYSTEM để duy trì!"
        },
        {
            "title": "Chiller COP giảm dần — Từ 5.8 → 4.5 trong 12 tháng → Tốn thêm 30% điện!",
            "industry": "HVAC",
            "situation": "Chiller 500 TR (refrigeration ton) làm lạnh nhà máy. COP (Coefficient of Performance) đo hàng tháng. COP giảm = HIỆU SUẤT GIẢM = TIÊU TỐN ĐIỆN HƠN!",
            "analysis": "COP trend — 12 tháng:\n\n| Tháng | COP | So design COP 6.0 |\n| T1 | 5.8 | –3% (gần design) |\n| T3 | 5.5 | –8% |\n| T6 | 5.2 | –13% |\n| T9 | 4.8 | –20% |\n| T12 | 4.5 | –25%! |\n\nPhân tích:\n• COP giảm = CẦN NHIỀU ĐIỆN HƠN để làm cùng lượng lạnh!\n• COP design = 6.0. Hiện tại 4.5 → hiệu suất giảm 25%!\n• Chi phí điện chiller: 800 triệu/năm × 125% = 1 TỶ → tốn thêm 200 triệu/năm!\n• Nguyên nhân COP giảm dần (4 yếu tố): Condenser tube FOULING (bám bẩn → trao đổi nhiệt kém). Refrigerant THIẾU (rò rỉ nhẹ). Evaporator SCALE (cặn canxi). Compressor valve WEAR (mòn van → hiệu suất nén giảm).",
            "result": "PM dựa trên Trend → COP phục hồi!:\n\n• Condenser tube cleaning (vệ sinh ống ngưng tụ): Bẩn nặng → dùng bàn chải cơ khí + hóa chất → trao đổi nhiệt tăng 15% → COP +0.5!\n• Refrigerant charge top-up (nạp thêm gas lạnh): Thiếu 10% → nạp thêm → COP +0.3!\n• Evaporator descaling (tẩy cặn bốc hơi): Cặn canxi → acid wash → COP +0.3!\n\nKết quả: COP từ 4.5 → 5.6! (phục hồi 92% design COP!)\nTiết kiệm: 200 triệu/năm chi phí điện!\nChi phí PM: 50 triệu → ROI = 4:1!\n\nSOP mới: PM chiller HÀNG QUÝ (clean condenser + check gas + check evap) → DUY TRÌ COP > 5.5 → KHÔNG để xuống 4.5 nữa!\n\n→ Bài học Trend COP: COP GIẢM DẦN = \"ăn mòn\" tiền điện! 25% COP loss = 200 triệu/năm LÃNG PHÍ! Trend Analysis phát hiện SỚM → clean quarterly → tiết kiệm TRIỆU VND mỗi năm!"
        },
        {
            "title": "Insulation Resistance trend motor 6.6kV — IR exponential decay = SẮP CHÁY!",
            "industry": "Điện lực",
            "situation": "Motor 6.6kV (trung thế) bơm nước cấp lò hơi — CRITICAL! Đo IR (Insulation Resistance — điện trở cách điện) hàng tháng bằng megger. IR giảm = cách điện SUY YẾU = NGUY CƠ CHÁY cuộn dây!",
            "analysis": "IR trend — 10 tháng (motor 6.6kV):\n\n| Tháng | IR (MΩ) | Trend |\n| T1 (baseline) | 500 | Bình thường |\n| T3 | 200 | Giảm nhanh |\n| T5 | 100 | ↓ |\n| T7 | 50 | ↓ exponential! |\n| T9 | 20 | GẦN LIMIT! |\n| T10 (dự đoán) | ~12 | SẮP ĐẠT min 10 MΩ! |\n\nPhân tích:\n• Min acceptable IR cho motor 6.6kV: 10 MΩ (IEEE 43)\n• Trend: EXPONENTIAL DECAY (giảm cực nhanh!) → IR 500 → 20 trong 9 tháng!\n• Nguyên nhân: Ẩm + nhiệt → phá hủy cách điện cuộn dây DẦN DẦN\n• Nếu IR < 10 MΩ → RÒ ĐIỆN → CHÁY CUỘN DÂY → dừng motor → dừng lò hơi → DỪNG NHÀ MÁY!\n• Cháy motor 6.6kV = REWINDING 2 tuần + 800 triệu!",
            "result": "Action dựa trên trend exponential:\n\n• T9 (IR=20 — gần limit!): QUYẾT ĐỊNH rewinding motor trong planned outage tháng 11!\n• T9 → T10: Giảm tải motor xuống 80% → GIẢM nhiệt → CHẬM tốc độ suy giảm IR → \"mua thêm thời gian\"!\n• T11 (planned outage): Rewinding motor → IR MỚI = 800 MΩ → XẾP HẠNG EXCELLENT!\n\nChi phí so sánh:\n• Rewinding THEO KẾ HOẠCH (T11): 300 triệu + 3 ngày trong planned outage\n• Cháy motor KHÔNG KẾ HOẠCH: 800 triệu (rewinding khẩn cấp đắt gấp 2.5×!) + 2 tuần dừng SX (mất 2 tỷ!) + RỦI RO CHÁY NỔ!\n→ Trend Analysis tiết kiệm: 2.5 TỶ!\n\n→ Bài học IR trend: IR EXPONENTIAL DECAY = cách điện ĐANG CHẾT! Nếu KHÔNG theo dõi trend → motor sẽ CHÁY BẤT NGỜ! Megger test hàng tháng + trend chart = biết TRƯỚC SỐ PHẬN motor = lên kế hoạch rewinding ĐÚNG LÚC!"
        }
    ]
}
