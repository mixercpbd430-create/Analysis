method = {
    "id": 6,
    "title": "Failure Analysis - Phân tích sự cố hỏng hóc",
    "short_name": "Failure Analysis",
    "icon": "🔧",
    "pillar": "Planned Maintenance",
    "description": "ĐIỀU TRA chi tiết SAU KHI sự cố xảy ra: Hỏng theo cơ chế gì? Tại sao? Làm sao KHÔNG tái phát?",
    "meaning": """
<p><strong>Failure Analysis (Phân tích sự cố hỏng hóc)</strong> là quá trình ĐIỀU TRA có hệ thống sau khi thiết bị đã HỎNG, nhằm xác định: <strong>Failure mechanism (cơ chế hỏng)</strong>, <strong>Root cause (nguyên nhân gốc)</strong>, và đề xuất <strong>CAPA (Corrective & Preventive Action — hành động khắc phục & phòng ngừa)</strong> để KHÔNG TÁI PHÁT.</p>
<p><em>So sánh dễ hiểu: FMEA (method 4) = "Bác sĩ DỰ ĐOÁN bệnh gì CỎ THỂ xảy ra" (phòng bệnh). Failure Analysis = "Bác sĩ MỔ TỬ THI xem chết vì đâu" (tìm nguyên nhân thực tế) → rút kinh nghiệm để NGƯỜI KHÁC không chết vì lý do tương tự!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Các cơ chế hỏng chính (Failure Mechanisms)</div>
    <p><strong>Fatigue (mỏi)</strong>: Chịu lực lặp đi lặp lại → vết nứt nhỏ → lan dần → GÃY! (Giống bẻ dây thép: bẻ 1 lần không gãy, bẻ 100 lần → gãy!)<br>
    <strong>Wear (mòn)</strong>: Bề mặt ma sát lặp lại → mòn dần → khe hở tăng → rung → hỏng. (Abrasive = mòn cào, Adhesive = mòn dính, Erosive = mòn xói)<br>
    <strong>Corrosion (ăn mòn)</strong>: Hóa chất/nước tác động → kim loại bị ăn mòn dần. (Uniform = đều, Pitting = rỗ, Galvanic = điện hóa, SCC = nứt do ứng suất + hóa chất)<br>
    <strong>Overload (quá tải)</strong>: Lực tác dụng > sức chịu → gãy/biến dạng NGAY. (Khác fatigue: fatigue = lặp nhiều lần, overload = 1 lần cực mạnh)<br>
    <strong>Creep (rão)</strong>: Chịu nhiệt + tải lâu dài → biến dạng từ từ → hỏng. (Thường ở > 40% nhiệt độ nóng chảy)<br>
    <strong>Electrical (điện)</strong>: Quá áp, quá dòng, sụt cách điện, arc (hồ quang) → cháy cuộn dây, PCB</p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định CHÍNH XÁC cơ chế hỏng (HOW — hỏng bằng cách nào?) và nguyên nhân gốc (WHY — tại sao hỏng?)</li>
    <li>Ngăn ngừa sự cố TƯƠNG TỰ TÁI PHÁT — không chỉ sửa mà phải HIỂU tại sao → phòng ngừa</li>
    <li>Cải thiện PM (Planned Maintenance): Kết quả FA → cập nhật PM checklist, interval, phương pháp kiểm tra</li>
    <li>Xây dựng CƠ SỞ DỮ LIỆU kiến thức hỏng hóc — KTV mới đọc FA cũ = học từ kinh nghiệm thực tế!</li>
    <li>Quy trách nhiệm đúng đắn: Hỏng do NCC (vật liệu sai spec) vs do BT (PM thiếu) vs do SX (vận hành sai)</li>
    <li>So sánh: Why-Why (method 18) = hỏi "tại sao?" bằng LỜI. Failure Analysis = điều tra bằng BẰNG CHỨNG VẬT LÝ (kiểm tra bề mặt gãy, phân tích kim tương, đo cứng...)</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: BẢO TOÀN HIỆN TRƯỜNG — ĐỪNG VỨT bất cứ thứ gì!</div>
        <div class="step-card__desc">SAU KHI hỏng → ĐỪNG VỨT chi tiết hỏng! Đây là "bằng chứng"! Chụp ảnh hiện trường NGAY (trước khi dọn dẹp). Thu thập chi tiết hỏng: Trục gãy, bearing cháy, seal rò, PCB cháy... Ghi lại dữ liệu vận hành TRƯỚC sự cố: Nhiệt độ? Tải? Rung? Tiếng lạ? Ai vận hành? Log data từ PLC/SCADA nếu có. QUAN TRỌNG: Nếu vứt chi tiết hỏng → mất bằng chứng → KHÔNG THỂ phân tích!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Phân tích trực quan + Lab (nếu cần)</div>
        <div class="step-card__desc"><strong>Visual inspection (kiểm tra bằng mắt)</strong>: Bề mặt gãy: Nhẵn (fatigue) hay thô ráp (overload)? Có beach marks (vạch bãi biển — fatigue)? Bề mặt bearing: Biến màu xanh (>300°C — cháy do thiếu bôi trơn)? Vết mòn? Mòn đều (bình thường) hay mòn lệch (lắp sai)? <strong>Lab analysis (nếu sự cố lớn)</strong>: Metallography (kim tương — cắt, đánh bóng, soi kính hiển vi), Hardness test (đo cứng), Chemical analysis (phân tích thành phần vật liệu), SEM (kính hiển vi điện tử — xem chi tiết bề mặt gãy).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xác định CƠ CHẾ HỎNG (Failure Mechanism)</div>
        <div class="step-card__desc">Dựa trên bằng chứng, xác định: Fatigue (mỏi)? Wear (mòn)? Corrosion (ăn mòn)? Overload (quá tải)? Creep (rão)? Electrical (điện)? Mỗi cơ chế có "dấu hiệu" riêng — học cách NHẬN BIẾT: Fatigue = beach marks + vùng khởi đầu nứt (initiation) + vùng gãy cuối (final fracture). Wear = bề mặt nhẵn bóng (abrasive) hoặc chuyển vật liệu (adhesive). Corrosion = rỗ (pitting), lớp oxit, biến màu. Overload = biến dạng dẻo (necking), bề mặt gãy thô ráp kiểu cup-and-cone.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: ROOT CAUSE + CAPA — Sửa GỐC, không sửa NGỌN!</div>
        <div class="step-card__desc">Từ failure mechanism → hỏi WHY: Fatigue → tại sao? Ứng suất tập trung? Vết gia công? Tải cyclic? Thiếu fillet radius? Corrosion → tại sao? Nước xâm nhập? Thiếu coating? Vật liệu sai? Viết <strong>CAPA report</strong>: <strong>Corrective Action (CA — khắc phục)</strong>: Sửa ngay lần này — thay trục mới, sửa seal... <strong>Preventive Action (PA — phòng ngừa)</strong>: Ngăn tái phát — thay đổi PM, cải tiến thiết kế, đào tạo, thay vật liệu... QUAN TRỌNG: Nếu chỉ có CA mà không có PA → sẽ TÁI PHÁT!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Gãy trục Pellet Mill — Fatigue từ keyway vết dao sắc!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Trục chính (main shaft) máy ép viên GÃY ĐỘT NGỘT sau 18 tháng vận hành → dừng sản xuất 5 NGÀY → thiệt hại: Trục mới 180 triệu + mất SX 500 triệu = 680 triệu VND!",
            "analysis": "Bước 1 — Bảo toàn: Thu thập 2 mảnh trục gãy + chụp ảnh vị trí gãy + ghi lại: máy đang chạy full load 40 T/h, không có tiếng bất thường trước khi gãy\n\nBước 2 — Kiểm tra bề mặt gãy:\n• Bề mặt gãy có 2 VÙNG RÕ RÀNG: Vùng NHẴN (chiếm 80%) + Vùng THÔ (chiếm 20%)\n• Vùng nhẵn: Có beach marks (vạch bãi biển — đường vân đồng tâm) → ĐẶC TRƯNG của FATIGUE!\n• Vùng khởi đầu nứt (initiation point): Tại RÃM THEN (keyway) — có VẾT DAO GIA CÔNG SẮC cạnh\n\nBước 3 — Cơ chế hỏng: FATIGUE (mỏi)\n• Chất lượng vật liệu (S45C): Đúng spec ✓\n• Hardness: Đạt HRC 28-32 ✓\n• NHƯNG: Keyway CÓ VẾT DAO SẮC CẠNH (no fillet radius) → tập trung ứng suất (stress concentration factor Kt = 4!) → vết nứt khởi đầu TẠI ĐÂY → lan dần qua 80% tiết diện → gãy đột ngột!",
            "result": "CAPA:\n\nCA (Khắc phục): Thay trục mới\n\nPA (Phòng ngừa — QUAN TRỌNG HƠN!):\n• Yêu cầu R0.5mm fillet radius tại keyway: Bo tròn góc rãnh then → giảm Kt từ 4 → 1.5 → giảm ứng suất 60%!\n• NDT (Non-Destructive Testing — kiểm tra không phá hủy): MPI (Magnetic Particle Inspection — kiểm tra hạt từ) cho trục MỚI trước lắp → phát hiện vết nứt gia công\n• Surface finish spec: Yêu cầu Ra PM mới: Vibration monitoring → phát hiện unbalance/misalignment → giảm tải cyclic\n\n→ Bài học FA: 1 vết dao gia công SẮC (chi phí 0 đồng để bo tròn lúc gia công!) → gãy trục 680 triệu! FA tìm ra root cause = vết gia công → PA = bo fillet chỉ tốn 50K VND → tiết kiệm 680 triệu!"
        },
        {
            "title": "Bearing cháy motor 500kW — Thiếu bôi trơn + interval quá dài!",
            "industry": "Xi măng",
            "situation": "Bearing motor quạt ID fan 500kW (quạt hút khí lò nung) CHÁY → motor dừng → lò nung phải giảm tải 50% × 12 giờ → thiệt hại clinker: 600 tấn × 1.5 triệu/T = 900 triệu VND!",
            "analysis": "Bước 2 — Kiểm tra bearing:\n• Vòng trong (inner race) BIẾN MÀU XANH → Nhiệt độ đã > 300°C! (Thép ở 300°C → biến từ vàng → xanh → xám)\n• Grease (mỡ bôi trơn) ĐÃ CHÁY KHÔ hoàn toàn → chỉ còn cặn carbon đen\n• Bi (rolling elements) bị PITTING (rỗ) + spalling (bong tróc) → tiếp xúc kim loại-kim loại\n• Cage (vòng cách) bị GÃY → bi va vào nhau → phá hủy bearing\n\nBước 3 — Cơ chế hỏng: WEAR + OVERHEATING do thiếu bôi trơn\n• Phân tích: Lượng mỡ bôi trơn KHÔNG ĐỦ → ma sát tăng → nhiệt tăng → mỡ cháy → mất bôi trơn hoàn toàn → kim loại chạm kim loại → CHÁY\n• Tại sao thiếu mỡ? PM schedule: Bôi trơn mỗi 3 THÁNG → QUÁ DÀI cho tốc độ 3000 rpm!\n• OEM (nhà sản xuất) khuyến nghị: Mỗi 2,000 giờ chạy ≈ 2.5 tháng → Nhưng nhà máy để 3 tháng → HẾT MỠ trước khi bôi!",
            "result": "CAPA:\n\nCA: Thay bearing + motor rewind (quấn lại cuộn dây bị ảnh hưởng nhiệt)\n\nPA (Phòng ngừa):\n• Tăng tần suất bôi trơn: 3 tháng → 1 tháng (theo tính toán OEM cho 3000 rpm + tải nặng)\n• Auto-greaser (bơm mỡ tự động): Lắp thiết bị tự bơm mỡ theo lịch → không phụ thuộc người → KHÔNG BAO GIỜ QUÊN!\n• Vibration monitoring online: Sensor rung gắn trực tiếp → phát hiện bearing BẮT ĐẦU mòn (vibration tăng) → THAY TRƯỚC KHI CHÁY\n• Temperature monitoring: Sensor nhiệt tại bearing housing → alarm khi > 80°C → action khi > 90°C\n\n→ Bài học FA: Bearing cháy KHÔNG PHẢI do bearing kém — do INTERVAL BÔI TRƠN SAI! FA tìm ra: Sửa interval bôi trơn (0 đồng!) → tránh 900 triệu thiệt hại!"
        },
        {
            "title": "Motor cháy cuộn dây 3 lần/năm — VFD gây voltage spike!",
            "industry": "Sản xuất chung",
            "situation": "Motor 75kW bơm nước cháy cuộn dây LẦN THỨ 3 TRONG NĂM! Mỗi lần sửa: Quấn lại 35 triệu + dừng SX 2 ngày. BGĐ: \"Tại sao motor cứ cháy hoài?!\"",
            "analysis": "Thu thập dữ liệu dòng thời gian:\n• Lần 1: Tháng 2 — cháy phase U-V\n• Lần 2: Tháng 6 — cháy phase V-W\n• Lần 3: Tháng 10 — cháy phase U-W\n→ Pattern: KHÔNG phải cùng phase → loại trừ dây 1 phase kém → vấn đề TOÀN BỘ cuộn dây!\n\nBước 2 — Kiểm tra sâu:\n• Insulation resistance (điện trở cách điện) đo Megger TRƯỚC lần 3: Chỉ 2MΩ! (Cần > 100MΩ!)\n• Kiểm tra môi trường: Motor lắp tại hầm bơm → ẨM THƯỜNG XUYÊN → ẩm xâm nhập cách điện\n• PHÁT HIỆN QUAN TRỌNG: Motor được điều khiển bởi VFD (Variable Frequency Drive — biến tần)!\n\nBước 3 — Cơ chế hỏng: ELECTRICAL — Voltage spike từ VFD:\n• VFD tạo ra voltage spike (xung điện áp) dạng PWM → peak có thể lên > 1000V (dù motor chỉ 380V!)\n• Voltage spike + Ẩm → PHÂN HỦY cách điện cuộn dây dần dần (Partial Discharge — phóng điện cục bộ)\n• Sau 3-4 tháng → cách điện XUYÊN THỦNG → chập giữa 2 phase → CHÁY!",
            "result": "CAPA:\n\nCA: Quấn lại motor lần 3 với cách điện Class H (chịu nhiệt 180°C, tốt hơn Class F cũ 155°C)\n\nPA (Phòng ngừa — GIẢ QUYẾT GỐC!):\n• dU/dt filter (bộ lọc xung áp): Lắp tại đầu ra VFD → lọc voltage spike → sóng ra mịn → không phá cách điện!\n• Motor inverter-duty (motor chuyên dùng cho biến tần): Cách điện REINFORCED (gia cường) chịu được voltage spike VFD → Tiêu chuẩn NEMA MG1 Part 31\n• Space heater (sưởi chống ẩm): Lắp điện trở sưởi trong motor → khi motor DỪNG → sưởi bật → chống ẩm ngưng tụ\n• Megger test hàng tháng: Đo insulation resistance → trend giảm → CẢNH BÁO trước khi cháy! (IR 0 lần cháy trong 2 năm tiếp theo!\n→ Bài học FA: Motor cháy 3 lần → nếu KHÔNG phân tích FA → cứ quấn lại hoài → cháy hoài! FA phát hiện VFD + ẩm = root cause → giải quyết GỐC!"
        },
        {
            "title": "Ống Heat Exchanger thủng sau 2 năm — SCC do Chloride!",
            "industry": "Hóa chất",
            "situation": "Ống đồng (copper) heat exchanger (bộ trao đổi nhiệt) BỊ THỦNG sau chỉ 2 năm (thiết kế 10 năm!). Rò rỉ dung dịch hóa chất → phải dừng nhà máy 3 ngày để sửa!",
            "analysis": "Bước 2 — Phân tích Lab:\n• Cắt mẫu ống thủng → soi kim tương (metallography)\n• Phát hiện: Pitting corrosion (ăn mòn rỗ) mặt ngoài ống (phía nước cooling) → lỗ xuyên thủng\n• Soi sâu: Có dấu hiệu SCC (Stress Corrosion Cracking — nứt do ứng suất + ăn mòn) → vết nứt nhánh cây từ pit → xuyên thành ống\n\nBước 3 — Cơ chế hỏng: PITTING + SCC do Chloride:\n• Phân tích nước cooling: Chloride (Cl⁻) = 350 ppm! (Chloride là ION cực kỳ hung hãn → ăn mòn đồng!)\n• Tiêu chuẩn cho ống đồng: Cl⁻ < 50 ppm! → Vượt GẤP 7 LẦN!\n• Tại sao Cl⁻ cao? Cooling tower sử dụng nước giếng → nước giếng khu vực có Cl⁻ cao + cô đặc thêm khi tuần hoàn\n• Ứng suất (stress) từ ép ống vào tube sheet + thermal cycling → SCC = stress + corrosion → nứt NHANH hơn corrosion thuần!",
            "result": "CAPA:\n\nCA: Thay toàn bộ ống bị hỏng\n\nPA (Phòng ngừa):\n• Short term: Kiểm soát Cl⁻  trong cooling water: Blowdown (xả nước cô đặc) thường xuyên hơn + Chemical treatment (hóa chất ức chế ăn mòn)\n• Long term: Thay vật liệu ống từ đồng → TITANIUM: Titanium chịu Cl⁻ tốt hơn 100 lần! Đắt gấp 5 nhưng tuổi thọ 20+ năm → TỔNG CHI PHÍ THẤP HƠN đồng (thay mỗi 2 năm!)\n• Monitoring: Đo Cl⁻ hàng tuần + Coupon test (mẫu thử ăn mòn) 3 tháng/lần\n\n→ Bài học FA: FA Lab (kim tương + phân tích nước) phát hiện Cl⁻ 350 ppm → ROOT CAUSE! Nếu chỉ THAY ỐNG MỚI mà không sửa nước → 2 năm sau THỦNG LẠI! FA = sửa GỐC, không sửa NGỌN!"
        },
        {
            "title": "Xích tải đứt — HAZ brittle do hàn sai quy trình!",
            "industry": "Khai thác mỏ",
            "situation": "Xích tải than (chain conveyor) ĐỨT tại mối hàn nối → dừng vận chuyển 16 giờ → mỏ mất 16 giờ sản lượng = 2,400 tấn than = 2.4 tỷ VND!",
            "analysis": "Bước 2 — Kiểm tra mối hàn gãy:\n• Gãy NGAY TẠI MỐI HÀN nối xích (không phải tại mắt xích nguyên bản)\n• Bề mặt gãy kiểu brittle fracture (gãy giòn): Phẳng, sáng → KHÔNG biến dạng trước khi gãy\n• Kiểm tra hardness tại vùng gãy: HRC 55! (Vật liệu ban đầu chỉ HRC 30-35)\n\nBước 3 — Cơ chế hỏng: BRITTLE FRACTURE do HAZ martensitic:\n• HAZ (Heat Affected Zone — vùng ảnh hưởng nhiệt): Khi hàn → nhiệt lan ra vùng xung quanh → thay đổi cấu trúc kim loại\n• Xích = thép carbon trung bình (0.35%C) → khi hàn, HAZ bị nguội NHANH (không pre-heat) → tạo martensite (cấu trúc giòn cực kỳ, cứng HRC 55 nhưng GIÒN!)\n• Martensite → chịu tải va đập → GÃY GIÒN ngay!\n• Root cause: Thợ hàn KHÔNG PRE-HEAT (nung nóng trước khi hàn) → HAZ nguội quá nhanh → martensite!",
            "result": "CAPA:\n\nCA: Thay đoạn xích mới + hàn nối lại ĐÚNG quy trình\n\nPA (Phòng ngừa):\n• WPS (Welding Procedure Specification — quy trình hàn chuẩn): Viết rõ cho xích: Pre-heat 150°C → Hàn với que E7018 (low hydrogen) → PWHT (Post-Weld Heat Treatment — nhiệt luyện sau hàn) 600°C/1h → làm nguội chậm trong cát\n• NDT sau hàn: MPI (kiểm tra hạt từ) 100% mối hàn nối xích → phát hiện nứt ngay\n• Hardness test sau hàn: Đo HAZ  HRC 40 → PWHT lại!\n• Chain tension monitoring: Sensor lực căng → quá tải → alarm → giảm tải trước khi đứt\n\n→ Bài học FA thép hàn: PRE-HEAT chỉ tốn 30 phút nung + 10K gas → KHÔNG pre-heat = 2.4 TỶ thiệt hại! FA tìm ra root cause = MỘT BƯỚC BỎ QUA trong quy trình hàn!"
        },
        {
            "title": "Seal bơm rò sau 3 tháng — Hạt silica trong dung dịch!",
            "industry": "Dầu khí",
            "situation": "Mechanical seal (phớt cơ khí) bơm ly tâm bị rò rỉ chỉ sau 3 tháng thay mới. MTBF bình thường 18 tháng! Lần thứ 2 liên tiếp rò sớm. Chi phí seal: 80 triệu/cái + dừng bơm 8 giờ.",
            "analysis": "Bước 2 — Kiểm tra mặt seal:\n• Mặt carbon (stationary ring): Có VẾT XƯỚC CÀO SÂU đồng tâm → Abrasive wear (mòn cào)!\n• Bình thường seal mòn ĐỀU, mịn → nhưng vết xước SÂU = có HẠT CỨNG xâm nhập giữa 2 mặt seal!\n• Lấy mẫu dung dịch bơm → phân tích: Silica particles (hạt cát silic) 200-500 μm!\n\nBước 3 — Cơ chế hỏng: ABRASIVE WEAR do solid particles:\n• Hạt silica (cứng hơn carbon face!) → lọt VÀO giữa 2 mặt seal → CÀO xước bề mặt → mất kín → RÒ!\n• Tại sao có silica? Giếng khai thác → dung dịch có cát lẫn → bơm hút lên → cát đi qua seal\n• Seal plan hiện tại: Plan 11 (tuần hoàn nội bộ — dung dịch bẩn!) → KHÔNG LỌC → cát ĐI THẲNG qua seal!",
            "result": "CAPA:\n\nCA: Thay seal mới\n\nPA (Phòng ngừa — THAY ĐỔI HỆ THỐNG!):\n• Cyclone separator (bộ tách cát ly tâm) trước bơm: Tách 95% hạt > 50μm → dung dịch vào bơm GẦN NHƯ SẠCH\n• Upgrade seal face: Carbon → SiC-SiC (Silicon Carbide): SiC cứng hơn silica → KHÔNG BỊ CÀO → MTBF tăng 3-5 lần\n• Seal plan 32 (external flush): Thay vì tuần hoàn dung dịch bẩn → bơm nước SẠCH từ ngoài VÀO làm mát + flush seal → không có cát\n• Monitoring: Pressure gauge trên flush line → nếu áp giảm → seal bắt đầu rò → alarm\n\nMTBF seal: 3 tháng → 24 tháng! (tăng 8 lần)\n→ Bài học FA: Thay seal hoài mà vẫn rò = THIẾU FA! FA phát hiện GỐC = hạt cát → thay đổi seal plan + vật liệu → giải quyết VĨNH VIỄN!"
        },
        {
            "title": "Cánh quạt công nghiệp gãy bay ra — Resonance + unbalance!",
            "industry": "HVAC",
            "situation": "Cánh quạt hút bụi GÃY BAY RA NGOÀI vỏ quạt → may mắn KHÔNG AI BỊ THƯƠNG! Nếu trúng người → TỬ VONG! Sự cố AN TOÀN NGHIÊM TRỌNG!",
            "analysis": "Bước 2 — Kiểm tra cánh quạt gãy:\n• Gãy tại ROOT (gốc cánh — nơi cánh gắn vào hub)\n• Bề mặt gãy: Beach marks → FATIGUE!\n• Initiation point: Mặt dưới cánh, chỗ hàn gắn với hub\n\nBước 3 — Cơ chế hỏng: FATIGUE do RESONANCE:\n• Phân tích rung: Tần số tự nhiên (natural frequency) cánh quạt = 48 Hz\n• Tốc độ quay: 1440 rpm = 24 Hz → 2× tốc độ quay = 48 Hz\n• RESONANCE (CỘNG HƯỞNG)!: 2x running speed TRÙNG natural frequency → biên độ rung TĂNG CỰC LỚN → fatigue nhanh!\n• Thêm: Dynamic balance ban đầu KÉM (bụi bám lệch tâm) → lực unbalance + resonance = fatigue cực nhanh!\n\n→ Fatigue do resonance = gãy sau VÀI THÁNG thay vì VÀI NĂM!",
            "result": "CAPA (AN TOÀN — ưu tiên tuyệt đối!):\n\nCA: Thay cánh quạt + Kiểm tra TẤT CẢ quạt cùng loại trong nhà máy!\n\nPA:\n• Redesign cánh: Tăng dày root 30% + fillet radius lớn hơn → tăng chịu fatigue\n• Thay đổi natural frequency: Thay đổi chiều dài/dày cánh → natural frequency = 65 Hz → KHÔNG CÒN trùng 2x (48 Hz) → HẾT resonance!\n• Dynamic balancing: Balance quạt trên máy balance TRƯỚC KHI lắp → ISO G2.5 → giảm unbalance 90%\n• Vibration monitoring ONLINE: Sensor rung → alarm khi rung > 4 mm/s → DỪNG + kiểm tra → KHÔNG CHỜ ĐẾN KHI GÃY!\n• Safety guard (lưới bảo vệ): Lắp lưới thép bao quanh quạt → nếu cánh gãy → KHÔNG bay ra ngoài!\n\n→ Bài học FA an toàn: Resonance = \"kẻ giết thầm lặng\"! FA + modal analysis phát hiện resonance → thay đổi thiết kế → CỨU MẠNG NGƯỜI! Vibration monitoring = \"bảo hiểm nhân thọ\" cho thiết bị quay!"
        }
    ]
}
