method = {
    "id": 12,
    "title": "PPA - Past Performance Analysis",
    "short_name": "PPA (Past Performance)",
    "icon": "📜",
    "pillar": "Overview",
    "description": "Phân tích DỮ LIỆU QUÁ KHỨ: OEE 36 tháng, breakdown 5 năm, quality trend → tìm PATTERN + bài học → DỰ BÁO tương lai.",
    "meaning": """
<p><strong>PPA — Past Performance Analysis (Phân tích hiệu suất quá khứ)</strong> là phương pháp phân tích DỮ LIỆU LỊCH SỬ (12-60 tháng) để tìm ra <strong>xu hướng (trend)</strong>, <strong>mẫu hình (pattern)</strong>, <strong>bài học kinh nghiệm (lessons learned)</strong>, và <strong>dự báo (forecast)</strong> cho tương lai.</p>
<p><em>Hình dung: Bác sĩ xem HỒ SƠ BỆNH ÁN 5 năm của bệnh nhân → Huyết áp TĂNG DẦN từ 120 → 150 → nếu không can thiệp → 2 năm nữa = CAO HUYẾT ÁP! Tương tự: MTBF GIẢM DẦN từ 6 tháng → 3 tháng → nếu không PM → BREAKDOWN VỠ MẶT!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Dữ liệu cần thu thập</div>
    <p><strong>Tối thiểu 12 tháng</strong> (để thấy seasonal pattern — mùa vụ):<br>
    KPI sản xuất: OEE, output, yield, cycle time theo tháng<br>
    Maintenance: Work orders, breakdown hours, MTBF, MTTR, spare parts cost<br>
    Quality: Defect rate, customer complaint, return rate<br>
    Safety: Incident reports, near-miss, LTIFR (Lost Time Injury Frequency Rate)<br>
    Chi phí: Maintenance cost, energy cost, overtime cost<br><br>
    <em>QUAN TRỌNG: Dữ liệu phải CÓ THỜI GIAN (timestamp) — không có thời gian = KHÔNG THỂ phân tích trend!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>NHẬN DIỆN xu hướng (trend): KPI đang TĂNG? GIẢM? ĐI NGANG? → Biết mình đang ĐI ĐÂU!</li>
    <li>PHÁT HIỆN pattern (mẫu hình): Seasonal (mùa vụ)? Weekly (tuần)? Shift (ca)? → LẬP KẾ HOẠCH đúng!</li>
    <li>RÚT BÀI HỌC từ thành công và thất bại: Cải tiến X đã HIỆU QUẢ? Dự án Y đã THẤT BẠI? Tại sao?</li>
    <li>DỰ BÁO tương lai: Trend giảm → bao giờ đạt TARGET? Hoặc bao giờ HẾT TUỔI THỌ thiết bị?</li>
    <li>ĐÁNH GIÁ hiệu quả cải tiến: Trước cải tiến 62% → sau 80% → CẢI TIẾN CÓ HIỆU QUẢ! Hay sau 63% → KHÔNG HIỆU QUẢ!</li>
    <li>THUYẾT PHỤC BGĐ bằng DỮ LIỆU: "OEE Line 1 giảm 15% trong 3 năm → cần đầu tư 5 tỷ" → có SỐ LIỆU = thuyết phục!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Thu thập DỮ LIỆU LỊCH SỬ — Ít nhất 12-24 tháng!</div>
        <div class="step-card__desc">Xác định KPI cần phân tích: OEE? Breakdown? Quality? Cost? Thu thập dữ liệu từ: CMMS (work orders), ERP (production), QMS (quality), Excel (nếu chưa có hệ thống). Ít nhất 12 tháng (thấy seasonal), tốt nhất 24-36 tháng (thấy trend dài hạn). KIỂM TRA chất lượng dữ liệu: Có tháng nào THIẾU? Có giá trị BẤT THƯỜNG (outlier)? Timestamp có CHÍNH XÁC? Ghi chú SỰ KIỆN: Tháng nào thay máy mới? Đổi NCC? Đào tạo? → Liên kết sự kiện với biến động dữ liệu!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Phân tích TREND + PATTERN — Vẽ biểu đồ!</div>
        <div class="step-card__desc"><strong>Trend chart (biểu đồ xu hướng)</strong>: KPI theo thời gian → đường TĂNG, GIẢM hay ĐI NGANG? Thêm trend line (đường xu hướng) → dự đoán tương lai! <strong>Pareto</strong>: Top nguyên nhân breakdown? Top sản phẩm lỗi? → 80/20! <strong>Seasonal pattern</strong>: Có tháng nào LẶP LẠI mỗi năm? (Tết, mùa mưa, mùa nóng) <strong>Shift pattern</strong>: Ca đêm output thấp hơn? → Xác nhận bằng dữ liệu! <strong>Histogram</strong>: Phân bố MTBF → biết "tuổi thọ trung bình" thiết bị. Dùng công cụ: Excel Pivot Table, Power BI, Minitab!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: XÁC ĐỊNH NGUYÊN NHÂN biến động — Liên kết SỰ KIỆN</div>
        <div class="step-card__desc">Với mỗi biến động LỚN trên biểu đồ, hỏi: "Tháng đó CÓ GÌ ĐẶC BIỆT?" Ví dụ: OEE tăng từ 65% → 80% tháng 6/2024 → Tháng 5 đã lắp vibration monitor → phát hiện bearing sớm → giảm breakdown → OEE TĂNG! Hoặc: OEE giảm từ 80% → 60% tháng 9/2024 → Tháng 8 thay NCC mới → NVL kém → changeover tăng → OEE GIẢM! → LIÊN KẾT dữ liệu + sự kiện = HIỂU TẠI SAO biến động!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: RÚT BÀI HỌC + DỰ BÁO + ACTION PLAN</div>
        <div class="step-card__desc"><strong>Lessons learned (Bài học)</strong>: Cải tiến nào ĐÃ HIỆU QUẢ? → NHÂN RỘNG! Cải tiến nào THẤT BẠI? → TẠI SAO? → TRÁNH lặp lại! <strong>Forecast (Dự báo)</strong>: Trend line → bao giờ đạt target? Bao giờ thiết bị hỏng? Bao giờ vượt ngân sách? <strong>Action plan</strong>: Dựa trên bài học + dự báo → lập kế hoạch: Đầu tư thiết bị khi nào? Training gì? Thay đổi PM strategy nào? Trình bày bằng DỮ LIỆU + BIỂU ĐỒ cho BGĐ → THUYẾT PHỤC hơn 100 lần nói "cần cải tiến"!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "OEE 3 năm — Line 1 suy giảm 78%→62%, Line 3 tăng 65%→82% nhờ TPM!",
            "industry": "Sản xuất",
            "situation": "BGĐ yêu cầu lập kế hoạch ĐẦUTƯ thiết bị cho năm tới. Phân tích OEE 36 tháng cho 5 dây chuyền để xác định đâu cần đầu tư.",
            "analysis": "OEE trend 36 tháng — 5 Lines:\n\n| Line | OEE Y1 | OEE Y2 | OEE Y3 | Trend | Root cause |\n| Line 1 | 78% | 70% | 62% | ↓ GIẢM 16%! | Thiết bị 15 tuổi! Breakdown tăng 3×. Die mòn nhanh (steel soft) |\n| Line 2 | 72% | 73% | 74% | → Đi ngang | PM cơ bản, không cải tiến |\n| Line 3 | 65% | 74% | 82% | ↑ TĂNG 17%! | TPM triển khai Y2! AM + PM + Kaizen → breakdown giảm 60%! |\n| Line 4 | 70% | 68% | 66% | ↓ Giảm nhẹ | Thiết bị 8 tuổi, bắt đầu xuống cấp |\n| Line 5 | 80% | 75% | 85% | ~ Mùa vụ! | Peak T1-T3 (Tết), low T6-T8 → biến động MÙA VỤ, không phải trend! |\n\nPhân tích chi tiết Line 1 vs Line 3:\n• Line 1: MTBF giảm từ 120h → 40h trong 3 năm! Tốc độ xuống cấp = 27h/năm → DỰ BÁO: Năm 4 MTBF = 13h = breakdown HẦU NHƯ LIÊN TỤC!\n• Line 3: Sau TPM tháng 6/Y2: Breakdown giảm 60%, Changeover giảm 40% (SMED), Quality tăng từ 95% → 99%",
            "result": "Bài học + Action Plan:\n\nLessons Learned:\n• ✅ TPM Line 3 = SUCCESS! ROI 300% → NHÂN RỘNG!\n• ❌ Line 1 không đầu tư PM → thiết bị xuống cấp NHANH → bài học: KHÔNG BẢO TRÌ = TIÊU DIỆT thiết bị!\n\nQuyết định đầu tư dựa trên data:\n• Line 1: THAY MỚI! MTBF trend → 13h Y4 = KHÔNG THỂ SẢN XUẤT! Đầu tư 8 tỷ thay mới → ROI 2 năm\n• Line 2 + Line 4: Triển khai TPM (bài học từ Line 3!) → 7 tỷ → dự kiến OEE +10-15% trong 2 năm\n• Line 5: Không cần đầu tư — biến động là MÙA VỤ, không phải suy giảm! Production plan theo seasonal index\n\nTỔNG budget: 15 tỷ VND → Dự kiến tăng output 25% → Thêm doanh thu 30 tỷ/năm!"
        },
        {
            "title": "Breakdown 5 năm xi măng — Top 10 thiết bị = 65% tổng downtime!",
            "industry": "Xi măng",
            "situation": "Chuyển đổi từ reactive maintenance (hỏng đâu sửa đó) → planned maintenance. Cần phân tích 5 năm breakdown data cho 200 thiết bị để biết BẮT ĐẦU TỪ ĐÂU.",
            "analysis": "Pareto breakdown 5 năm — 200 thiết bị:\n\n| Rank | Thiết bị | Breakdown hours | % Tổng | Trend |\n| 1 | Kiln drive gearbox | 1,200h | 15% | MTBF giảm 6M → 3M! |\n| 2 | Clinker cooler fan | 800h | 10% | Seasonal: TĂNG MÙA HÈ (nhiệt 45°C!) |\n| 3 | Raw mill classifier | 600h | 7.5% | Đi ngang — wear part |\n| 4 | Kiln feed bucket elevator | 550h | 7% | TĂNG sau tháng 18 (chain stretch) |\n| 5 | Coal mill motor | 500h | 6% | Đột xuất — winding failure |\n| 6-10 | 5 thiết bị khác | 1,550h | 19.5% | Hỗn hợp |\n| 11-200 | 190 thiết bị | 2,800h | 35% | Low frequency |\n\nInsight từ data:\n• Top 10 thiết bị = 65% tổng breakdown! (80/20 rule — Pareto!)\n• Kiln gearbox: MTBF GIẢM DẦN → dấu hiệu WEAR tiến triển → nếu không action = BREAKDOWN CATASTROPHIC!\n• Cooler fan: Seasonal pattern → MÙA HÈ bearing cháy do nhiệt → PM TRƯỚC mùa hè!",
            "result": "Action Plan từ PPA:\n\n• Kiln gearbox: Lắp VIBRATION + OIL ANALYSIS monitoring NGAY! MTBF giảm = wear tiến triển → nếu vibration tăng trên alarm → LÊN LỊCH thay gearbox (planned, không emergency) → tiết kiệm 50% chi phí + 0 downtime bất ngờ!\n• Cooler fan: \"Summer PM Campaign\" — PM đặc biệt tháng 4 hàng năm (trước mùa hè): Thay bearing + kiểm tra motor cooling + vệ sinh bụi → NGĂN breakdown mùa hè!\n• Top 10 thiết bị: Lập PM plan chi tiết: Weekly inspection + Monthly PM + Condition Monitoring → Dự kiến giảm 40% breakdown\n• 190 thiết bị còn lại: Reactive maintenance OK! (Ít breakdown, chi phí PM > chi phí sửa → Run-to-failure hợp lý!)\n\n→ Bài học PPA: 5 năm data → Pareto → TOP 10 = 65% → TẬP TRUNG PM cho 10 thiết bị = HIỆU QUẢ NHẤT! Không cần PM 200 thiết bị!"
        },
        {
            "title": "Tai nạn 5 năm xây dựng — Thợ < 1 năm KN = 60% incidents!",
            "industry": "Xây dựng",
            "situation": "Safety Manager phân tích 5 năm incident data (250 báo cáo sự cố) để cải thiện safety program.",
            "analysis": "Phân tích 250 incidents theo nhiều chiều:\n\nTheo loại tai nạn (Pareto):\n• Rơi từ trên cao: 35% (87 cases) → #1!\n• Vật rơi trúng: 25% (63 cases)\n• Điện giật: 15% (38 cases)\n• Kẹp/nghiền: 12% (30 cases)\n• Khác: 13% (32 cases)\n\nTheo thời gian (pattern):\n• GIỜ PEAK: 10-11h sáng (trước giải lao) + 14-15h chiều (sau nghỉ trưa, mệt!) → 2 khung giờ nguy hiểm!\n• NGÀY PEAK: Thứ 2 (sau weekend, quên SOP) + Thứ 6 (cuối tuần, vội vã hoàn thành!) → 2 ngày nguy hiểm!\n\nTheo kinh nghiệm (insight quan trọng nhất!):\n• Thợ 60% tổng incidents! (dù chỉ chiếm 30% nhân lực!)\n• Thợ 1-3 năm: 25%\n• Thợ > 3 năm: 15%\n→ Thợ mới = RỦI RO GẤP 4 LẦN!",
            "result": "Safety program cải tiến dựa trên data:\n\n• Focus fall protection (35% incidents!): Harness inspection hàng tuần + scaffold tag system + fall arrest training mandatory → Target: Giảm 50% fall incidents\n• Toolbox talk trước giờ PEAK: 9:45 sáng + 13:45 chiều → nhắc nhở an toàn NGAY TRƯỚC khung giờ nguy hiểm!\n• Monday safety briefing + Friday checklist: Thứ 2 = review SOP → \"nhắc lại sau weekend\". Thứ 6 = kiểm tra an toàn trước khi về → \"không vội vã\"\n• Buddy system cho thợ mới (: MỖI thợ mới = 1 thợ kinh nghiệm đi kèm 3 tháng đầu → thợ mới KHÔNG BAO GIỜ làm 1 mình! (60% incidents = thợ mới!)\n\nKết quả: LTIFR (Lost Time Injury Frequency Rate) giảm 70% trong 2 năm!\n\n→ Bài học PPA an toàn: 250 incidents = KHO VÀNG kinh nghiệm! Phân tích theo NHIỀU CHIỀU (loại, thời gian, kinh nghiệm) → phát hiện pattern → safety program CHÍNH XÁC! Data > cảm tính!"
        },
        {
            "title": "Quality + Supplier correlation 2 năm — Supplier B = 8% OOS!",
            "industry": "Dược phẩm",
            "situation": "Sản phẩm dược bị OOS (Out of Specification — ngoài spec) mãn tính 3-4%. Đã kiểm tra quy trình SX nhiều lần → ổn. Phân tích 2 năm quality data LIÊN KẾT với supplier lots.",
            "analysis": "Phân tích OOS theo supplier — 2 năm (480 lô):\n\n| Supplier | Số lô | OOS | % OOS | API variation (CV%) |\n| Supplier A | 320 | 6 | 1.9% | 1.2% (ổn định) |\n| Supplier B | 160 | 13 | 8.1%! | 3.8% (biến động GẤP 3!) |\n\nInsight:\n• Supplier B: API content (hàm lượng hoạt chất) biến động CV% = 3.8% → GẤP 3 lần Supplier A!\n• Correlation analysis: r = 0.85 giữa API variation NVL và final product OOS → TƯƠNG QUAN RẤT MẠNH!\n• Nghĩa là: NVL biến động → sản phẩm biến động → OOS!\n• Supplier B rẻ hơn 5%/kg → nhưng OOS = rework + reject + recall risk → TỔNG CHI PHÍ CAO HƠN NHIỀU!\n\nTimeline mapping:\n• Tháng 3, 7, 11/Y1 và tháng 2, 5, 8/Y2: OOS spike → kiểm tra → TẤT CẢ lô dùng NVL Supplier B!",
            "result": "Action từ PPA:\n\n• Chuyển 100% volume sang Supplier A: Đắt hơn 5% NVL nhưng: OOS giảm 8% → 2% → tiết kiệm chi phí rework/reject GẤP 10 lần chênh lệch giá NVL!\n• Incoming testing TIGHTENED: TẤT CẢ supplier → test full spec (không chỉ CoA) → bắt lô BIẾN ĐỘNG trước khi nó vào SX!\n• Supplier qualification SOP: Cập nhật SOP đánh giá NCC: Yêu cầu NCC cung cấp Cpk ≥ 1.33 cho API content → NCC biến động = LOẠI!\n• Dual sourcing strategy: Tìm Supplier C để backup → không phụ thuộc 100% Supplier A\n\n→ Bài học PPA + Quality: 2 năm data + correlation analysis → phát hiện 80% OOS do 1 SUPPLIER! Nếu không phân tích data → cứ đổ lỗi \"quy trình SX\" → sửa hoài không được!"
        },
        {
            "title": "Chi phí bảo trì 5 năm — Từ 70% reactive → 70% preventive = tiết kiệm 12.5 tỷ!",
            "industry": "Sản xuất",
            "situation": "BGĐ hỏi: \"TPM triển khai 2 năm rồi, CÓ HIỆU QUẢ KHÔNG?\" → Phân tích chi phí BT 5 năm để CHỨNG MINH ROI bằng dữ liệu!",
            "analysis": "Chi phí bảo trì 5 năm — Year 1-3 (trước TPM) vs Year 4-5 (sau TPM):\n\n| Năm | Tổng BT (tỷ) | % Reactive | % Preventive | Availability | MTBF |\n| Y1 | 12.0 | 75% (hỏng đâu sửa đó!) | 25% | 78% | 80h |\n| Y2 | 11.5 | 70% | 30% | 80% | 90h |\n| Y3 | 11.0 | 68% | 32% | 81% | 95h |\n| --- | TPM bắt đầu tháng 1/Y4 | --- | --- | --- | --- |\n| Y4 | 9.5 | 40% | 60% | 88%! | 150h! |\n| Y5 | 8.0 | 28% | 72% | 93%! | 220h! |\n\nInsight rõ ràng từ data:\n• Chi phí BT: Y1-3 trung bình 11.5 tỷ → Y5 = 8.0 tỷ → GIẢM 3.5 tỷ/năm!\n• Nhưng QUAN TRỌNG HƠN: Availability 78% → 93% = tăng 15% = thêm NHIỀU sản phẩm!\n• MTBF 80h → 220h = tăng 2.75 lần → thiết bị SỐ ĐÁng tin cậy!\n• Reactive 75% → 28% = SẢN XUẤT ỔN ĐỊNH (không bất ngờ breakdown nữa!)",
            "result": "ROI chứng minh cho BGĐ:\n\n💰 Tiết kiệm direct: Chi phí BT giảm 3.5 tỷ × 2 năm = 7 tỷ\n💰 Tiết kiệm indirect: Availability +15% → thêm output → thêm doanh thu ≈ 5.5 tỷ/năm\n💰 Tổng tiết kiệm 2 năm: 12.5 tỷ!\n💰 Chi phí TPM: Training 500 triệu + CMMS 300 triệu + Tools 200 triệu = 1 tỷ\n💰 ROI = (12.5 — 1) / 1 = 1,150%!\n\n→ BGĐ: \"Ok, mở rộng TPM toàn nhà máy!\" 🎉\n\n→ Bài học PPA + Management: Data 5 năm = BẰNG CHỨNG KHÔNG THỂ PHỦ NHẬN! BGĐ hỏi \"có hiệu quả không?\" → CÓ, lãi 12.5 tỷ/2 năm! Data > thuyết trình PowerPoint!"
        },
        {
            "title": "Energy consumption 3 năm — SEC tăng 12% dù output chỉ tăng 5%!",
            "industry": "Sản xuất",
            "situation": "Hóa đơn điện TĂNG 25% trong 3 năm. BGĐ cho rằng \"sản lượng tăng nên điện tăng\". Nhưng sản lượng chỉ tăng 5%! → Phân tích 36 tháng energy data!",
            "analysis": "Phân tích SEC (Specific Energy Consumption — kWh/tấn sản phẩm):\n\n| Năm | Output (tấn) | Electricity (MWh) | SEC (kWh/T) | So Y1 |\n| Y1 | 100,000 | 4,500 | 45.0 | Baseline |\n| Y2 | 103,000 | 4,800 | 46.6 | +3.6% |\n| Y3 | 105,000 | 5,250 | 50.0 | +11.1%! |\n\nSEC TĂNG 11% dù output chỉ tăng 5%! → Nhà máy đang LÃNG PHÍ nhiều hơn!\n\nPhân tích theo thiết bị (sub-metering):\n• Compressor: SEC tăng 18% → Rò rỉ khí nén TĂNG!\n• Cooling system: SEC tăng 15% → Chiller hiệu suất GIẢM (fouling)\n• Production machines: SEC tăng 5% → Tương ứng output → OK\n• Lighting + offices: SEC tăng 8% → Đèn cũ + AC kém\n\nWeekend pattern: Cuối tuần output = 10% nhưng consumption = 40%! → Ai bật máy cuối tuần mà không sản xuất?!",
            "result": "Action từ PPA năng lượng:\n\n• Compressor (SEC +18%): Ultrasonic leak survey → sửa 47 điểm rò → SEC compressor giảm 25%! (Chi phí sửa 50 triệu → tiết kiệm 200 triệu/năm!)\n• Cooling (SEC +15%): Vệ sinh condenser + thay gas chiller → hiệu suất phục hồi 95% → SEC giảm 12%\n• Weekend shutdown: SOP tắt máy cuối tuần → giảm consumption weekend 60% → tiết kiệm 150 triệu/năm\n\nKết quả: SEC từ 50.0 → 42.0 kWh/T (giảm 16%!) → Tiết kiệm 2 tỷ/năm!\n\n→ Bài học PPA năng lượng: Nếu chỉ nhìn TỔNG hóa đơn → \"sản lượng tăng nên điện tăng\" (sai!). PPA + SEC analysis → phát hiện LÃNG PHÍ ẩn (rò rỉ, chiller bẩn, weekend) → tiết kiệm 2 tỷ!"
        }
    ]
}
