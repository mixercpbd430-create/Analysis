method = {
    "id": 13,
    "title": "PPA - Process Point Analysis",
    "short_name": "PPA (Process Point)",
    "icon": "🎯",
    "pillar": "Focus Improvement",
    "description": "Xác định ĐIỂM THEN CHỐT trong quy trình: Q-point (ảnh hưởng CHẤT LƯỢNG) + M-point (ảnh hưởng THIẾT BỊ) → Kiểm soát ĐÚNG chỗ!",
    "meaning": """
<p><strong>PPA — Process Point Analysis (Phân tích điểm quy trình)</strong> là phương pháp phân tích CHI TIẾT từng điểm (point) trong quy trình sản xuất để xác định <strong>Q-point (Quality Point — điểm ảnh hưởng chất lượng)</strong> và <strong>M-point (Machine Point — điểm ảnh hưởng thiết bị)</strong>.</p>
<p><em>Hình dung: Quy trình sản xuất = "dây chuyền 100 bước". Nhưng KHÔNG PHẢI 100 bước đều QUAN TRỌNG như nhau! Có 5-10 bước = "ĐIỂM VÀNG" → kiểm soát CHẶT = chất lượng TỐT. Bỏ lơ = chất lượng TỆ! PPA = tìm ra 5-10 "ĐIỂM VÀNG" đó!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Q-point vs M-point — 2 loại điểm then chốt</div>
    <p><strong>Q-point (Quality Point — Điểm chất lượng)</strong>:<br>
    Thông số ảnh hưởng TRỰC TIẾP đến chất lượng sản phẩm<br>
    Ví dụ: Nhiệt conditioning 85°C → ảnh hưởng PDI viên cám! (Sai = viên mềm!)<br>
    → Phải có <strong>Control Chart (SPC)</strong> theo dõi liên tục!<br><br>
    <strong>M-point (Machine/Maintenance Point — Điểm thiết bị)</strong>:<br>
    Thông số phản ánh TÌNH TRẠNG thiết bị<br>
    Ví dụ: Rung bearing < 4.5 mm/s. Nhiệt motor < 80°C. Áp thủy lực 200±5 bar<br>
    → Phải có <strong>Alarm/Trip</strong> khi vượt ngưỡng!<br><br>
    <em>So sánh: Q-point = "huyết áp, đường huyết" (sức khỏe bệnh nhân = chất lượng SP). M-point = "tiếng tim, nhịp thở" (sức khỏe cơ thể = tình trạng máy)</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định ĐÚNG điểm then chốt — không kiểm soát 100 thông số mà tập trung 5-10 thông số QUAN TRỌNG NHẤT!</li>
    <li>Thiết lập TIÊU CHUẨN kiểm soát (control limits) cho Q/M-points → biết ĐÚNG/SAI NGAY LẬP TỨC</li>
    <li>Xây dựng hệ thống GIÁM SÁT quy trình hiệu quả — SPC cho Q-point, alarm cho M-point</li>
    <li>GIẢM BIẾN ĐỘNG chất lượng bằng kiểm soát thông số ĐẦU VÀO (input) → thay vì kiểm tra output rồi LOẠI BỎ!</li>
    <li>Kết nối NGUYÊN NHÂN (process parameters) → KẾT QUẢ (quality) → Khi quality lỗi → biết NGAY check Q-point nào!</li>
    <li>Hỗ trợ TROUBLESHOOTING nhanh: Sản phẩm lỗi → xem Q-point nào OUT → sửa NGAY! (Không cần phân tích từ đầu!)</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: VẼ SƠ ĐỒ quy trình CHI TIẾT — Từ NVL vào → Sản phẩm ra</div>
        <div class="step-card__desc">Vẽ process flow (sơ đồ dòng chảy) từ đầu vào đến đầu ra. Mỗi BƯỚC = 1 ô: NVL nhập → Trộn → Conditioning → Ép → Cắt → Cooling → Đóng gói → Xuất. Tại MỖI bước: Liệt kê TẤT CẢ thông số vận hành: Nhiệt độ? Áp suất? Tốc độ? Lưu lượng? Thời gian? Nồng độ? Đo bằng gì? (Sensor? Manual?) → Đây là \"bản đồ\" quy trình — phải ĐẦY ĐỦ!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Xác định Q-points và M-points — Đâu là THEN CHỐT?</div>
        <div class="step-card__desc">Tại MỖI bước, hỏi: <strong>Q-point</strong>: "Thông số nào nếu SAI → sản phẩm SẼ LỖI?" → Đó là Q-point! Ví dụ: Nhiệt conditioning sai → PDI thấp → sản phẩm lỗi! → Q-point! <strong>M-point</strong>: "Thông số nào nếu vượt ngưỡng → máy SẼ HỎNG?" → Đó là M-point! Ví dụ: Rung bearing > 7 mm/s → bearing sắp cháy! → M-point! Không phải TẤT CẢ thông số đều là Q/M-point! Chỉ chọn thông số CÓ ẢNH HƯỞNG TRỰC TIẾP!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Thiết lập TIÊU CHUẨN + phương pháp kiểm soát</div>
        <div class="step-card__desc">Cho MỖI Q-point và M-point: <strong>Target</strong> (giá trị mục tiêu): Ví dụ: 85°C. <strong>Tolerance</strong> (dung sai cho phép): Ví dụ: ±3°C → OK từ 82-88°C. <strong>Method</strong> (phương pháp đo): Sensor online? Manual check? Lab test? <strong>Frequency</strong> (tần suất đo): Liên tục? Mỗi giờ? Mỗi mẻ? <strong>Responsible</strong> (ai đo?): Operator? QC? KTV? <strong>Reaction plan</strong> (khi OUT → làm gì?): Dừng? Điều chỉnh? Báo cáo? → Viết thành CONTROL PLAN!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Triển khai SPC + Alarm — GIÁM SÁT LIÊN TỤC!</div>
        <div class="step-card__desc"><strong>Q-points → Control Chart (SPC method 26)</strong>: Vẽ biểu đồ X-bar R cho Q-point → phát hiện OUT OF CONTROL ngay → ACTION trước khi sản phẩm lỗi! <strong>M-points → Alarm system</strong>: Set alarm level: Warning (cảnh báo) + Critical (dừng). Ví dụ: Rung > 4.5 mm/s = WARNING (kiểm tra!). Rung > 7 mm/s = TRIP (dừng máy NGAY!). Kết nối vào DCS/SCADA/PLC → hiển thị real-time → Ai cũng thấy! Review ĐỊNH KỲ (monthly): Q/M-point còn ĐÚNG không? Cần thay đổi giá trị? Thêm point mới?</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Pellet Mill — 4 Q-points + 4 M-points kiểm soát PDI!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "PDI (Pellet Durability Index) biến động 88-98% (spec > 95%). Cần PPA để tìm ĐÚNG thông số nào ảnh hưởng PDI → kiểm soát ĐÚNG CHỖ.",
            "analysis": "Process Flow Pellet Mill → xác định Q-points và M-points:\n\nQ-points (ảnh hưởng PDI trực tiếp):\n| # | Bước | Q-point | Target | Tolerance | Đo bằng |\n| Q1 | Conditioning | Steam temperature | 85°C | ±3°C | PT100 sensor (online) |\n| Q2 | Conditioning | Steam pressure | 2.5 bar | ±0.3 bar | Pressure gauge (online) |\n| Q3 | Conditioning | Moisture sau conditioning | 16.5% | ±0.5% | NIR sensor (hoặc oven test mỗi giờ) |\n| Q4 | Die | Die temperature | 80°C | ±5°C | IR thermometer (mỗi 30 phút) |\n\nM-points (ảnh hưởng thiết bị):\n| # | Bước | M-point | Warning | Critical | Đo bằng |\n| M1 | Main motor | Motor amps | > 90% FLA | > 100% FLA (trip!) | Ammeter (online) |\n| M2 | Gearbox | Bearing temp | > 75°C | > 85°C (trip!) | Temp sensor (online) |\n| M3 | Roller | Roller gap | 0.3mm | Die wear (mm) | > 1mm mòn | > 2mm (thay die!) | Đo chiều sâu lỗ die (monthly) |",
            "result": "Kết quả sau triển khai PPA:\n\n• Control Chart cho Q1-Q4: Operator xem biểu đồ real-time trên SCADA → nếu Q1 (steam temp) OUT → điều chỉnh NGAY → KHÔNG ĐỢI đến khi viên bị lỗi!\n• Alarm cho M1-M4: Motor amps > 90% FLA → BIP! → Kiểm tra die (có thể tắc!) → TRÁNH quá tải!\n\nTrước PPA: PDI biến động 88-98% → SAU PPA: PDI ổn định 96-98%! (biến động GIẢM 80%!)\n\nReaction Plan khi Q-point OUT:\n• Q1 (Steam temp  75°C): → Kiểm tra bôi trơn NGAY! Giảm tải\n\n→ Bài học PPA: 4 Q-points + 4 M-points = TỔNG 8 thông số kiểm soát (trong 50+ thông số trên dây chuyền) → TẬP TRUNG vào 8 = ĐỦ để kiểm soát PDI → 96-98%!"
        },
        {
            "title": "Injection Molding — Melt + Mold + Pressure + Time = Zero Defect!",
            "industry": "Nhựa / Y tế",
            "situation": "Sản phẩm y tế bằng nhựa — YÊU CẦU ZERO DEFECT (0 lỗi)! Defect rate hiện tại 0.5% → cần giảm về < 0.05%. PPA để xác định ĐÚNG thông số kiểm soát.",
            "analysis": "Process Flow Injection Molding → Q-points và M-points:\n\nQ-points (ảnh hưởng chất lượng sản phẩm y tế):\n| # | Bước | Q-point | Target | Tolerance | Tại sao quan trọng? |\n| Q1 | Barrel | Melt temperature | 225°C | ±5°C | Quá nóng → degradation (phân hủy nhựa!) → vàng, giòn! |\n| Q2 | Mold | Mold temperature | 60°C | ±2°C | Quá lạnh → short shot (thiếu nhựa!). Quá nóng → flash (tràn!) |\n| Q3 | Injection | Injection pressure | 800 bar | ±50 bar | Quá thấp → void (bóng khí!). Quá cao → flash + stress! |\n| Q4 | Cooling | Cooling time | 18s | ±1s | Quá ngắn → biến dạng khi eject! Quá dài → giảm output! |\n\nM-points (tình trạng máy ép):\n| # | M-point | Warning | Critical |\n| M1 | Clamp force | Screw RPM | Biến động > ±5% → nhựa trộn không đều | > ±10% → DỪNG! |\n| M3 | Hydraulic oil temp | > 50°C → áp suất KHÔNG ỔN ĐỊNH | > 60°C → DỪNG! |",
            "result": "SPC + Alarm triển khai:\n\n• SPC cho Q1-Q4: MỖI mẻ (shot) ghi lại 4 Q-point → Control Chart → phát hiện OUT OF CONTROL trong Cavity pressure monitoring: Lắp pressure sensor TRONG khuôn → đo áp suất thực tế TRONG hốc khuôn (không chỉ áp máy ép) → chính xác hơn → phát hiện void, short shot NGAY SHOT ĐẦU TIÊN!\n• Process data logging: Lưu TẤT CẢ Q/M-point theo từng shot → nếu customer complaint → trace lại shot đó → biết CHÍNH XÁC thông số lúc sản xuất!\n\nKết quả: Defect rate 0.5% → 0.03%! (giảm 94%!) → ĐẠT standard y tế!\nThêm: OEE tăng 12% (ít dừng máy để sửa lỗi hơn!)\n\n→ Bài học PPA nhựa: Injection molding = 4 THÔNG SỐ VÀNG (Melt, Mold, Pressure, Time) → kiểm soát 4 này = kiểm soát 80% chất lượng! PPA = tìm ĐÚng 4 thông số thay vì 30+ thông số!"
        },
        {
            "title": "CIP sữa — 4 Q-points đảm bảo VỆ SINH tuyệt đối!",
            "industry": "Chế biến sữa",
            "situation": "Quy trình CIP (Clean-in-Place — vệ sinh tại chỗ) cho dây chuyền sữa. Nếu CIP KHÔNG ĐẠT → vi khuẩn → RECALL sản phẩm → THẢM HỌA! PPA xác định Q-point CIP.",
            "analysis": "CIP Process → Q-points quan trọng:\n\n| # | Bước CIP | Q-point | Target | Tolerance | Hậu quả nếu SAI |\n| Q1 | Rửa kiềm (NaOH) | NaOH concentration | 1.5% | ±0.2% | Rinse temperature | 78°C | ±3°C | Contact time | 20 phút | ±2 phút | Conductivity (độ dẫn điện) |  50 → CÒN HÓA CHẤT trong đường ống → DƯ NaOH trong sữa! |\n\nM-points thiết bị CIP:\n| # | M-point | Warning | Critical |\n| M1 | CIP pump flow rate | CIP tank level | Valve position | Valve không về đúng vị trí (leak!) | → DỪNG CIP → kiểm tra valve! |",
            "result": "CIP Validation bằng PPA:\n\n• Auto CIP sequence: PLC tự kiểm soát 4 Q-point → NẾU bất kỳ Q-point nào CHƯA ĐẠT → KHÔNG cho phép chạy bước tiếp theo → đảm bảo MỖI bước PHẢI ĐẠT!\n• Q4 Conductivity = \"Gate keeper\": Conductivity > 50 μS/cm → VẪN CÒN hóa chất → hệ thống TỰ rửa lại → cho đến khi ATP swab test: Sau CIP → swab test (lau bề mặt → test vi khuẩn) → CIP report auto-generate: Mỗi lần CIP → hệ thống TỰ ĐỘNG ghi lại 4 Q-point + thời gian → báo cáo → LƯU HỒ SƠ → audit ISO 22000/FSSC 22000 → có bằng chứng!\n\nKết quả: ATP swab test 100% PASS! CIP cycle time giảm 15% (vì ĐÚNG thông số = không cần rửa thêm lần!)\n\n→ Bài học PPA thực phẩm: CIP = quy trình \"vô hình\" (sạch bằng MẮT không thấy!) → PPA + 4 Q-points = CHỨNG MINH bằng SỐ LIỆU rằng đã vệ sinh ĐỦ → BẢO VỆ người tiêu dùng!"
        },
        {
            "title": "Hàn MIG Robot — Current + Voltage + Speed + Gas = 0 defect!",
            "industry": "Ô tô",
            "situation": "Trạm hàn MIG robot body-in-white (khung xe ô tô). Weld defect (spatter, porosity, undercut) = 0.8% → target < 0.1%. PPA để tìm Q-point hàn.",
            "analysis": "Welding Process → Q-points và M-points:\n\nQ-points (ảnh hưởng chất lượng mối hàn):\n| # | Q-point | Target | Tolerance | Sai thì sao? |\n| Q1 | Welding current (dòng hàn) | 180A | ±10A | Quá cao → burn-through (cháy thủng!) + spatter (xỉ bắn). Quá thấp → cold lap (không ngấu!) |\n| Q2 | Voltage (điện áp) | 22V | ±1V | Quá cao → wide bead + undercut. Quá thấp → stubbing (dây chập!) |\n| Q3 | Travel speed (tốc độ di chuyển torch) | 600 mm/min | ±30 mm/min | Quá nhanh → thin bead (mối hàn mỏng!). Quá chậm → excess weld + heat distortion |\n| Q4 | Gas flow rate (lưu lượng khí bảo vệ) | 15 L/min | ±2 L/min | Quá ít → porosity (rỗ khí!) do không khí lọt vào. Quá nhiều → turbulence → cũng rỗ! |\n\nM-points (tình trạng thiết bị hàn):\n| # | M-point | Warning | Critical |\n| M1 | Wire feed rate | Biến động > ±5% → feeding không đều | Stuck → DỪNG! |\n| M2 | Contact tip wear (mòn đầu tip) | Bore > 1.2mm (ban đầu 1.0mm) | > 1.4mm → THAY! (tip mòn → arc không ổn định!) |\n| M3 | Torch angle | Deviation > 3° → bead lệch | > 5° → Kiểm tra robot calibration! |",
            "result": "Real-time weld monitoring triển khai:\n\n• Weld monitor system: Đo Q1-Q4 TRONG suốt quá trình hàn (không chỉ đầu/cuối!) → biểu đồ Current + Voltage theo THỜI GIAN → phát hiện NGAY nếu có spike/dip (đột biến)!\n• Auto torch cleaning station: Sau mỗi 10 mối hàn → robot đưa torch vào cleaning station → làm sạch spatter → đảm bảo gas flow + wire feed ổn định\n• Tip change interval: PPA data → xác định: Tip mòn 0.05mm/1000 mối hàn → thay TIP mỗi 4,000 mối hàn (trước khi bore > 1.2mm!)\n\nKết quả: Weld defect 0.8% → 0.08%! (giảm 90%!) Spatter giảm 60%!\n\n→ Bài học PPA hàn: Hàn robot tưởng \"tự động\" = không cần kiểm soát? SAI! 4 Q-point (Current, Voltage, Speed, Gas) biến động liên tục → PPA + weld monitor = SỐ HÓA mối hàn → BIẾT tất cả!"
        },
        {
            "title": "Rang cà phê Specialty — Bean temp + Development time = cup score 85!",
            "industry": "Thực phẩm",
            "situation": "Rang cà phê specialty arabica — khách hàng PREMIUM đòi cup score > 84 và ĐỒN NHẤT giữa các lô! Hiện tại: Cup score 80-88 (biến động quá lớn!). PPA để tìm Q-point rang.",
            "analysis": "Roasting Process → Q-points:\n\n| # | Bước | Q-point | Target | Tolerance | Tại sao? |\n| Q1 | First Crack | Bean temp tại first crack | 196°C | ±2°C | First crack quá sớm ( 198°C) → overdeveloped → ĐẮNG! |\n| Q2 | Development | Development time ratio (DTR) | 22% | ±2% | DTR = thời gian từ first crack → drop / tổng thời gian rang. DTR thấp → grassy (hăng cỏ!). DTR cao → baked (khô, phẳng!) |\n| Q3 | Drop | End temperature (nhiệt khi xả) | 210°C | ±3°C | Quyết định ROAST LEVEL (light/medium/dark). Sai 3°C = HOÀN TOÀN KHÁC vị! |\n| Q4 | Drop | Roast color (Agtron) | 55 | ±3 | Agtron = đo màu rang bằng quang học. Sai = khách SẼ THẤY màu khác → complaint! |\n\nM-points (thiết bị rang):\n| # | M-point | Warning | Critical |\n| M1 | Drum speed | ±5% → bean không đảo đều → rang KHÔNG đồng nhất | ±10% → DỪNG! |\n| M2 | Airflow damper | Biến động → convection không ổn định | Stuck → DỪNG! (bean cháy!) |\n| M3 | Burner pressure | ±0.1 bar → rate of rise (ROR) sai | ±0.2 bar → profile sai hoàn toàn! |",
            "result": "Profile logging + Agtron inline:\n\n• Roast profile logging: Sensor ghi bean temp MỖI GIÂY → vẽ đường cong rang → so sánh với PROFILE CHUẨN → nếu lệch > 2°C → điều chỉnh burner/airflow NGAY trong mẻ!\n• Agtron inline check: Đo màu rang NGAY SAU KHI XẢ → confirm Agtron 55±3 → nếu OUT → sample riêng để cupping giữ → KHÔNG trộn vào sản phẩm!\n• Green bean temperature log: Q-point \"ẩn\" — nhiệt bean xanh TRƯỚC KHI rang! Bean lạnh (15°C) vs bean nóng (30°C) = profile KHÁC nhau → phải adjust charge temp theo!\n\nKết quả: Cup score 80-88 (biến động 8 điểm) → 85-87 (biến động chỉ 2 điểm!)\n→ Khách hàng specialty cực kỳ hài lòng → giữ được GIÁ PREMIUM!\n\n→ Bài học PPA F&B: Rang cà phê = \"nghệ thuật\"? KHÔNG! PPA biến NGHỆ THUẬT → KHOA HỌC! 4 Q-point (Bean temp, DTR, End temp, Agtron) = 80% cup score → kiểm soát 4 thông số = ĐỒNG NHẤT mỗi mẻ!"
        },
        {
            "title": "Phun nhựa + Sơn tĩnh điện — Q-point CHUỖI quy trình!",
            "industry": "Gia công kim loại",
            "situation": "Sản phẩm kim loại phun sơn tĩnh điện dùng ngoài trời. Vấn đề: Sơn BỊ BỘC sau 6 tháng! → PPA cho TOÀN chuỗi quy trình (pretreatment + coating + curing).",
            "analysis": "Chuỗi Q-points cho sơn tĩnh điện:\n\n| # | Bước | Q-point | Target | Tolerance | Hậu quả nếu SAI |\n| Q1 | Pretreatment (xử lý bề mặt) | pH dung dịch phosphate | 4.8 | ±0.3 | pH sai → lớp phosphate KHÔNG ĐỀU → sơn KHÔNG BÁM → BỘC! |\n| Q2 | Blowoff (thổi khô) | Surface moisture (ẩm bề mặt) | 0% | — | Ẩm còn → sơn bị BLISTERING (phồng rộp!) sau 3 tháng ngoài trời! |\n| Q3 | Powder coating | Powder thickness (dày sơn) | 70μm | ±10μm |  80μm → orange peel (vỏ cam!) |\n| Q4 | Curing (nung) | Oven temperature | 200°C | ±5°C | Cure time at peak | 15 phút | ±1 phút |  16 phút → overcured → giòn + vàng! |\n\nInsight quan trọng: Sơn bộc sau 6 tháng = KHÔNG PHẢI lỗi sơn! Mà do Q1 (pretreatment pH SAI → phosphate kém → adhesion kém → mưa nắng → BỘC!)",
            "result": "Triển khai PPA cho chuỗi quy trình:\n\n• pH online monitoring: Sensor pH trong bể phosphate → đo LIÊN TỤC → auto-dose hóa chất → pH LUÔN 4.5-5.1\n• Inline thickness gauge: Đo dày sơn MỖI sản phẩm bằng eddy current → nếu  80μm → alarm → chỉnh gun ngay!\n• Oven profiling: Gắn thermocouple lên sản phẩm → đo nhiệt THỰC TẾ trên sản phẩm (không chỉ nhiệt lò!) → đảm bảo 200°C × 15 phút AT PRODUCT!\n• Cross-cut adhesion test: Mỗi ca → 1 sản phẩm → cắt ô (cross-hatch) → dán tape → kéo tape → nếu sơn bong > 5% → DỪNG + kiểm tra Q1-Q5!\n\nKết quả: Sơn bộc ngoài trời 6 tháng → 5 NĂM +! Adhesion test 100% PASS!\n\n→ Bài học PPA chuỗi: Sơn bộc → mọi người đổ lỗi SƠN! Nhưng PPA phân tích TOÀN CHUỖI → tìm Q1 (pretreatment) = GỐC vấn đề! PPA chia nhỏ chuỗi thành 5 Q-points → tìm ĐÚNG điểm sai!"
        }
    ]
}
