method = {
    "id": 9,
    "title": "HAZOP - Hazard and Operability Analysis",
    "short_name": "HAZOP",
    "icon": "☢️",
    "pillar": "SHE",
    "description": "Dùng GUIDE WORDS (NO/MORE/LESS/REVERSE...) để tìm mọi ĐỘ LỆCH so với thiết kế → phát hiện NGUY HIỂM ẩn trong quy trình.",
    "meaning": """
<p><strong>HAZOP (Hazard and Operability Study — Nghiên cứu Nguy hiểm và Khả năng vận hành)</strong> là phương pháp phân tích rủi ro CÓ CẤU TRÚC, sử dụng <strong>Guide Words (từ khóa hướng dẫn)</strong> để xác định các <strong>Deviation (độ lệch)</strong> so với thiết kế ban đầu, từ đó tìm ra NGUY HIỂM tiềm ẩn và vấn đề vận hành.</p>
<p><em>Hình dung: HAZOP = "Nếu... thì sao?" — Nếu KHÔNG CÓ dòng chảy → sao? Nếu ÁP SUẤT CAO HƠN → sao? Nếu CHẢY NGƯỢC → sao? → Với MỖI câu hỏi → tìm nguyên nhân, hậu quả, và rào cản bảo vệ!</em></p>
<p>Phát triển từ ngành hóa chất Anh (ICI, 1960s). Yêu cầu bởi: IEC 61882, API 750, OSHA PSM (Process Safety Management), Seveso Directive (EU).</p>
<div class="note-box note-box--warning">
    <div class="note-title">⚡ 7 Guide Words — "Bộ câu hỏi thần kỳ"</div>
    <p><strong>NO / NOT</strong> (Không có): Không có dòng chảy? Không có tín hiệu? → Bơm hỏng? Van đóng?<br>
    <strong>MORE</strong> (Nhiều hơn): Áp suất cao hơn? Nhiệt độ cao hơn? Lưu lượng nhiều hơn? → Quá tải?<br>
    <strong>LESS</strong> (Ít hơn): Áp thấp hơn? Nhiệt thấp hơn? Flow ít hơn? → Phản ứng không đủ?<br>
    <strong>REVERSE</strong> (Ngược lại): Dòng chảy ngược? Tín hiệu ngược? → Hóa chất chảy ngược về bồn?<br>
    <strong>PART OF</strong> (Một phần): Chỉ một phần thành phần? Nồng độ sai? → Sản phẩm off-spec?<br>
    <strong>AS WELL AS</strong> (Ngoài ra): Có thêm tạp chất? Thêm pha khác? → Phản ứng phụ?<br>
    <strong>OTHER THAN</strong> (Khác với): Hóa chất KHÁC lọt vào? Vận hành KHÁC quy trình? → Phản ứng nguy hiểm?<br><br>
    <em>So sánh: FMEA (method 4) hỏi "Hỏng theo cách nào?". HAZOP hỏi "Nếu thông số LỆCH thì sao?" → HAZOP chi tiết hơn cho quy trình hóa chất, năng lượng, dầu khí!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định NGUY HIỂM ẩn trong THIẾT KẾ và VẬN HÀNH mà người thiết kế CÓ THỂ BỎ SÓT</li>
    <li>Kiểm tra TẤT CẢ độ lệch có thể xảy ra — guide words BUỘC phải xét từng thông số × từng từ khóa → KHÔNG BỎ SÓT</li>
    <li>Đánh giá SAFEGUARDS (rào cản bảo vệ) hiện có → ĐỦ chưa? Cần thêm không?</li>
    <li>Đáp ứng YÊU CẦU PHÁP LUẬT: OSHA PSM, Seveso, TCVN về an toàn hóa chất → BẮT BUỘC cho nhà máy có hóa chất nguy hiểm</li>
    <li>Cải thiện THIẾT KẾ trước khi xây dựng → sửa trên giấy (rẻ!) thay vì sửa khi đã xây (đắt!)</li>
    <li>Làm CƠ SỞ cho SIL assessment (Safety Integrity Level — Mức toàn vẹn an toàn) → xác định SIS (Safety Instrumented System) cần lắp đặt</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Chuẩn bị — Thu thập P&ID, thành lập team</div>
        <div class="step-card__desc">Thu thập: <strong>P&ID</strong> (Piping & Instrumentation Diagram — sơ đồ đường ống và thiết bị đo), PFD (Process Flow Diagram — sơ đồ dòng chảy), Operating Manual (tài liệu vận hành), MSDS (Material Safety Data Sheet — bảng an toàn hóa chất). Thành lập team ĐA CHỨC NĂNG: Process Engineer (thiết kế) + Operator (vận hành) + Instrument Engineer (đo lường) + Safety Officer + Maintenance → 5-7 người. Leader = HAZOP Facilitator (người dẫn dắt — phải được TRAINING HAZOP!).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Chia NODE + Áp dụng GUIDE WORDS</div>
        <div class="step-card__desc">Chia hệ thống thành các NODE (đoạn): Mỗi node = 1 đoạn ống/thiết bị có cùng DESIGN INTENT (mục đích thiết kế). Ví dụ: Node 1 = Bồn chứa → Bơm. Node 2 = Bơm → Heat exchanger. Node 3 = Heat exchanger → Reactor. Với MỖI node: Xác định THÔNG SỐ: Flow (lưu lượng), Pressure (áp suất), Temperature (nhiệt độ), Level (mức), Composition (thành phần)... Áp dụng TỪNG guide word cho TỪNG thông số: "NO + Flow = Không có dòng chảy?" → "MORE + Pressure = Áp suất cao hơn?" → "REVERSE + Flow = Chảy ngược?"...</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xác định Nguyên nhân → Hậu quả → Safeguards</div>
        <div class="step-card__desc">Với MỖI deviation (độ lệch) CÓ Ý NGHĨA: <strong>Cause (Nguyên nhân)</strong>: Tại sao deviation này xảy ra? Bơm hỏng? Van kẹt? Operator lỗi? <strong>Consequence (Hậu quả)</strong>: Nếu xảy ra thì SAO? Nổ? Rò rỉ hóa chất? Sản phẩm off-spec? <strong>Safeguards (Rào cản hiện có)</strong>: Đã có gì bảo vệ? PSV (van an toàn)? Alarm? Interlock? SOP? Ghi vào HAZOP worksheet — mỗi dòng = 1 deviation.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Đánh giá rủi ro + RECOMMENDATIONS</div>
        <div class="step-card__desc">Với mỗi deviation: Đánh giá Risk = Severity × Likelihood (sử dụng Risk Matrix 5×5). Nếu risk = INTOLERABLE (không chấp nhận được) → PHẢI có recommendation (khuyến nghị)! Recommendations thường: Thêm SIS (Safety Instrumented System) với SIL phù hợp. Thêm alarm, interlock, hoặc quá trình bypass. Thay đổi thiết kế (thêm van, thay vật liệu, thêm redundancy). Thêm SOP, training, hoặc procedure. Mỗi recommendation → gán NGƯỜI PHỤ TRÁCH + DEADLINE → theo dõi close-out!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "HAZOP lò hơi — 'NO FLOW' nước cấp = CẠN NƯỚC = NỔ!",
            "industry": "Nhà máy chung",
            "situation": "HAZOP cho hệ thống boiler (lò hơi) cấp steam 15 bar cho dây chuyền sản xuất. Lò hơi = thiết bị ÁP LỰC → NỔ = CHẾT NGƯỜI! → HAZOP bắt buộc!",
            "analysis": "Node: Boiler Feed Water (Nước cấp lò hơi) — Design intent: Cấp nước liên tục 5 m³/h, 105°C, áp 18 bar\n\nHAZOP Worksheet:\n\n| Guide Word | Deviation | Cause | Consequence | Safeguard | Recommendation |\n| NO | Không có dòng nước cấp | Bơm hỏng. Van intake đóng sai. Đường ống tắc | Lò CẠN NƯỚC → ống lửa quá nhiệt → NỔ! | LWCO (Low Water Cut-Off) hiện có 1 cái | Thêm REDUNDANT LWCO (2 cái độc lập!) |\n| LESS | Lưu lượng nước ít hơn | Bơm mòn. Filter tắc. Valve partially closed | Mức nước giảm chậm → overheating dần | Low level alarm | Thêm flow switch + alarm |\n| MORE | Áp suất steam cao hơn 15 bar | Burner không tắt. FWC hỏng. Demand giảm đột ngột | Quá áp → NỔ! | Safety valve (PSV) 1 cái | Thêm PSV thứ 2 + SIL 2 high-high pressure trip |\n| MORE | Nhiệt độ cao hơn | Flame impingement (lửa chạm ống). Scale (cặn bám) | Ống lửa quá nhiệt → nứt → rò → NỔ | Manual inspection | Online tube temperature monitoring |\n| REVERSE | Steam chảy ngược vào đường nước cấp | Steam trap hỏng. Check valve kẹt | Bơm bị steam → cavitation → hỏng bơm | Check valve | PM check valve hàng quý |",
            "result": "Tổng: 12 recommendations từ HAZOP, 4 CRITICAL:\n\n1. Redundant LWCO: 2 cái LWCO KHÁC LOẠI (1 probe, 1 float) → 1 hỏng thì còn 1 (FTA method 5: loại bỏ single point of failure!)\n2. SIL 2 pressure trip: Pressure transmitter → SIS (Safety PLC) → trip burner khi > 16 bar → KHÔNG PHỤ THUỘC DCS thường\n3. PSV thứ 2 + test pop 6 tháng/lần (theo ASME)\n4. Flame safeguard SIL 2: UV/IR sensor → phát hiện mất lửa → đóng gas NGAY (Bài học HAZOP: Guide word 'NO' cho nước cấp → CẠN NƯỚC → NỔ! Đây là scenario mà FMEA có thể BỎ QUA (vì FMEA hỏi 'hỏng gì?' — không hỏi 'nếu KHÔNG CÓ thì sao?'). HAZOP guide words BUỘC xét mọi tình huống!"
        },
        {
            "title": "HAZOP hệ thống NH3 lạnh — Rò rỉ ammonia = NGỘ ĐỘC!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "HAZOP cho hệ thống làm lạnh bằng NH₃ (ammonia) trong kho lạnh nhà máy TACN. NH₃ = khí ĐỘC (300 ppm = nguy hiểm, 2500 ppm = tử vong trong 30 phút!). Nhiều nhà máy TACN dùng NH₃ nhưng CHƯA BAO GIỜ làm HAZOP!",
            "analysis": "Node: NH₃ Liquid Line (Đường ống NH₃ lỏng từ receiver → evaporator)\n\n| Guide Word | Deviation | Cause | Consequence | Safeguard | Recommendation |\n| MORE Pressure | Áp suất NH₃ cao hơn design | Condenser fouling (bẩn). Trời nóng 40°C. Quạt condenser hỏng | Relief valve lift → NH₃ xả ra khu vực! | PSV with piping to outdoor | Ventilation upgrade kho máy + NH₃ alarm 25 ppm |\n| NO Flow | Không có dòng NH₃ | Compressor trip. SOV (Solenoid Valve) đóng. Đường ống tắc (ice) | Kho lạnh mất lạnh → hàng hỏng → thiệt hại HÀNG TỶ (thịt, cá đông lạnh) | Low suction alarm | Backup compressor + auto changeover |\n| REVERSE Flow | NH₃ chảy ngược | Compressor trip đột ngột → áp equalize → liquid slugging | Compressor hỏng valve plate → bánh rang → chi phí sửa LỚN | Non-return valve | PM non-return valve + liquid accumulated alarm |\n| AS WELL AS | NH₃ + nước (ẩm) | Moisture ingress khi mở hệ thống | Acid formation → ăn mòn ống đồng → RÒ RỈ NH₃ | Sight glass moisture indicator | Thay filter dryer hàng năm + vacuum test sau mở |\n| OTHER THAN | Nhầm nạp gas KHÁC (R22) | Bình gas không nhãn, nhầm khi nạp | Phản ứng + compressor hỏng + potential release | Color-coded connection | Quy trình nạp gas: 2 người verify + check label |",
            "result": "TOP Recommendations cho an toàn NH₃:\n\n• NH₃ detector: Lắp 4 đầu dò tại kho máy nén — alarm level 1 (25 ppm — alert), level 2 (150 ppm — EVACUATE!) → nối với sirene + đèn xoay\n• Emergency shower + eyewash: Lắp tại lối ra kho máy — NH₃ dính mắt/da → RỬA NGAY trong 15 giây!\n• Ventilation upgrade: Quạt hút cưỡng bức → thay TOÀN BỘ không khí kho máy 30 lần/giờ (theo ASHRAE 15)\n• SOP evacuation: Diễn tập sơ tán NH₃ leak hàng quý → mọi người biết CHẠY HƯỚNG NÀO (chạy NGƯỢC GIÓ!)\n• SCBA (Self-Contained Breathing Apparatus — bình thở): Đặt BÊN NGOÀI kho máy (không phải bên trong!) → mặc trước khi VÀO khu vực rò rỉ\n• Wind sock (cờ gió): Lắp tại cột nhà máy → biết gió thổi hướng nào → sơ tán NGƯỢC GIÓ!\n\n→ Bài học: Nhiều nhà máy TACN/thực phẩm dùng NH₃ mà CHƯA HAZOP → RỦI RO ẨN! HAZOP phát hiện guide word 'AS WELL AS' (NH₃ + ẩm → ăn mòn → rò rỉ) mà ít ai nghĩ đến!"
        },
        {
            "title": "HAZOP reactor dược phẩm — 'MORE TEMP' = phản ứng mất kiểm soát!",
            "industry": "Dược phẩm",
            "situation": "HAZOP cho reactor batch synthesis API (Active Pharmaceutical Ingredient — hoạt chất dược phẩm). Reactor: 2000L, phản ứng TỎA NHIỆT (exothermic — nhiệt tăng tự nhiên!). Nếu mất kiểm soát nhiệt → RUNAWAY REACTION → NỔ!",
            "analysis": "Node: Reactor Vessel — Phản ứng tổng hợp API\nDesign intent: Nhiệt 85°C ±3°C, áp 2 bar, 6 giờ/mẻ\n\n| Guide Word | Deviation | Cause | Consequence | Safeguard |\n| MORE TEMP | Nhiệt > 88°C | Mất cooling (bơm glycol hỏng). Nạp NVL quá nhanh (exotherm quá mạnh) | RUNAWAY REACTION! Nhiệt tăng không kiểm soát → áp tăng → NỔ reactor → HÓA CHẤT PHUN RA → cháy nổ + hít hơi độc! | TIC (Temperature control) + High temp alarm 90°C |\n| AS WELL AS | Tạp chất lẫn vào | Reactor chưa vệ sinh sạch (lô trước → lô sau). NVL có tạp chất | Cross-contamination → Thuốc bị ô nhiễm → NGUY HIỂM cho bệnh nhân! | CIP validation + IPC test |\n| LESS | Khuấy yếu hơn | Motor khuấy hỏng. Belt trượt. VFD lỗi | Phản ứng không đều → HOTSPOT (điểm nóng cục bộ) → runaway cục bộ | Motor current monitoring |\n| OTHER THAN | Nạp SAI hóa chất | Nhầm bình NVL (nhãn giống nhau). Operator mới | Phản ứng bất ngờ → NỔ! Hoặc sản phẩm sai → thuốc sai → ĐE DỌA BỆNH NHÂN! | Manual check label |",
            "result": "Recommendations CRITICAL cho reactor dược phẩm:\n\n• Emergency cooling system: Hệ thống làm lạnh khẩn cấp RIÊNG BIỆT (độc lập với cooling bình thường) → khi nhiệt > 90°C → emergency cooling TỰ ĐỘNG bật → hạ nhiệt NGAY\n• Rupture disc + vent to scrubber: Đĩa nổ (rupture disc) → nếu áp tăng quá → đĩa nổ xả áp → hơi hóa chất đi vào scrubber (tháp rửa khí) → KHÔNG xả ra môi trường\n• Containment: Bồn chứa thứ cấp (secondary containment) chứa được 110% dung tích reactor → nếu rò → hóa chất KHÔNG lan ra\n• Barcode scanning cho NVL: Trước khi nạp → SCAN barcode NVL → hệ thống SO SÁNH với recipe → ĐÚNG mới cho nạp → LOẠI TRỪ nhầm NVL!\n• CIP validation: Sau mỗi lô → CIP (Clean-In-Place) → Swab test → HPLC test → xác nhận SẠCH → mới chạy lô sau\n\n→ Bài học HAZOP dược: Guide word 'AS WELL AS' (tạp chất/lẫn thuốc) + 'OTHER THAN' (nhầm NVL) → đặc biệt NGUY HIỂM cho dược phẩm! Nhầm thuốc = ĐE DỌA TÍNH MẠNG bệnh nhân!"
        },
        {
            "title": "HAZOP nhà máy nước — 'MORE' chlorine = DƯ HÓA CHẤT trong nước sạch!",
            "industry": "Cấp nước",
            "situation": "HAZOP cho nhà máy nước sạch 50,000 m³/ngày TRƯỚC KHI vận hành. Nước cấp cho 200,000 dân → sai = ảnh hưởng HÀNG TRĂM NGÀN NGƯỜI!",
            "analysis": "Node: Chlorination (Khử trùng bằng Chlorine)\nDesign intent: Chlorine dư 0.5 mg/L ±0.2 tại điểm cuối mạng lưới\n\n| Guide Word | Deviation | Cause | Consequence | Safeguard |\n| MORE | Dư chlorine > 1 mg/L | Dosing pump runaway (bơm định lượng chạy quá). Sensor Cl₂ đọc sai (calibrate sai) → hệ thống bơm THÊM | DƯ chlorine → Nước có mùi, vị → DÂN PHÀN NÀN → Nếu > 4 mg/L → ẢNH HƯỞNG SỨC KHỎE! | Manual check 2 lần/ca |\n| NO | Không có chlorine | Tank chlorine RỖ. Dosing pump hỏng. Đường ống tắc | Nước KHÔNG ĐƯỢC KHỬ TRÙNG → vi khuẩn vượt chuẩn → DỊCH BỆNH! (E.coli, Cholera...) | Low level alarm tank |\n| LESS | Chlorine thấp hơn 0.3 mg/L | Nước đầu vào bẩn hơn (mưa) → chlorine demand tăng. Dosing không đủ | Vi khuẩn còn sống → NGUY HIỂM → người dân uống nước có vi khuẩn | Residual chlorine check |\n| OTHER THAN | Hóa chất KHÁC lẫn vào nước | Nhầm bồn hóa chất. Ống nối sai. Cross-connection với nước thải | ĐẦU ĐỘC hàng trăm ngàn người! → THẢM HỌA! | Dedicated piping |",
            "result": "Recommendations từ HAZOP cho nhà máy nước:\n\n• Online chlorine analyzer: Đo Cl₂ dư LIÊN TỤC tại đầu ra → KHÔNG phụ thuộc test thủ công 2 lần/ca → phát hiện lệch NGAY\n• Auto-dose control: Chlorine analyzer → PLC → điều chỉnh dosing pump TỰ ĐỘNG → Cl₂ luôn trong khoảng 0.3-0.7 mg/L\n• Tank level alarm + auto changeover: Tank chlorine sắp hết → ALARM → tự chuyển sang tank dự phòng → KHÔNG BAO GIỜ hết chlorine\n• Backup chlorinator: 2 hệ thống dosing (1 chạy + 1 standby) → 1 hỏng → chuyển ngay → 0 downtime khử trùng\n• Backflow preventer: Van ngăn chảy ngược tại mỗi điểm nối mạng lưới → ngăn nước bẩn chảy ngược vào nước sạch\n• Color-coded piping: Ống nước sạch = XANH. Ống hóa chất = ĐỎ. Ống nước thải = NÂU → KHÔNG THỂ nhầm!\n\n→ Bài học: HAZOP cho nước sạch = BẢO VỆ SỨC KHỎE CỘNG ĐỒNG! Guide word 'OTHER THAN' (nhầm hóa chất) = kịch bản KINH HOÀNG nhưng ÍT AI NGHĨ ĐẾN → HAZOP buộc phải xét!"
        },
        {
            "title": "HAZOP nhà máy bia — 'MORE PRESSURE' tank lên men = BIẾN DẠNG!",
            "industry": "Đồ uống",
            "situation": "HAZOP cho hệ thống lên men bia: 20 tank, mỗi tank 500 hl (50,000 lít), có thu hồi CO₂. Tank thiết kế chỉ chịu 1 bar → quá áp RẤT NGUY HIỂM!",
            "analysis": "Node: Fermentation Tank — Bồn lên men\nDesign intent: Nhiệt 12°C ±1°C, áp MORE Pressure | Áp > 1 bar | Đường CO₂ tắc (hops block). Van xả bị kẹt đóng. CO₂ recovery system hỏng | Tank BIẾN DẠNG! (tank inox mỏng chỉ chịu 1 bar!). Nắp manway bay → CO₂ PHUN → ASPHYXIATION (ngạt thở — CO₂ nặng, chìm xuống → người bất tỉnh)! | PRV (Pressure Relief Valve) 1 cái |\n| LESS Pressure | Áp âm (vacuum) | CIP nước nóng → hơi ngưng tụ → tạo chân không | Tank BỊ BÓP MÉO (collapse — áp âm hút tank lại!) | Vacuum breaker |\n| LESS TEMP | Nhiệt NO | Không CIP | Quên CIP giữa 2 mẻ. CIP valve hỏng | Cross-contamination → vi khuẩn → bia CHUA → cả tank 500 hl phải đổ! | CIP SOP + checklist |",
            "result": "Recommendations từ HAZOP bia:\n\n• PRV trên TỪNG tank: Kiểm tra PRV hàng quý → test pop → xác nhận xả ở 0.9 bar (dưới design pressure 1 bar)\n• Vacuum breaker trên TỪNG tank: Khi áp giảm CO₂ vent alarm: Nếu CO₂ đường xả bị tắc → pressure tăng → ALARM trước khi đạt 0.9 bar\n• CO₂ detector tại tầng thấp (CO₂ nặng hơn không khí → CHÌM XUỐNG): Lắp detectors ở sàn → alarm 0.5% → EVACUATE 1.5% (OSHA TWA = 5000 ppm = 0.5%)\n• Glycol temperature control SIL 1: High-high temp trip → đóng glycol → bảo vệ men bia\n• CIP validation: CIP auto-sequence → KHÔNG THỂ bỏ qua bước nào → hệ thống KHÓA tank nếu CIP chưa hoàn tất\n• Manway interlock: Nắp manway MỞ → interlock NGĂN áp hóa tank (CIP hoặc CO₂)\n\n→ Bài học HAZOP F&B: Tank bia tưởng \"an toàn\" nhưng 50,000 lít × 1 bar = lực RẤT LỚN! + CO₂ = khí NGẠT! HAZOP phát hiện 'MORE PRESSURE' + 'LESS PRESSURE' (2 chiều!) → bảo vệ tank VÀ CON NGƯỜI!"
        },
        {
            "title": "HAZOP kho hóa chất — 'OTHER THAN' = nạp NHẦM = NỔ!",
            "industry": "Hóa chất",
            "situation": "HAZOP cho kho chứa 500 tấn hóa chất: xăng, dung môi (toluene), acid (H₂SO₄), kiềm (NaOH). CÁC HÓA CHẤT KHÔNG TƯƠNG THÍCH → trộn lẫn = PHẢN ỨNG + CHÁY NỔ!",
            "analysis": "Node: Tank Farm — Loading/Unloading (Nạp/xuất hóa chất)\n\n| Guide Word | Deviation | Cause | Consequence | Safeguard |\n| OTHER THAN | Nạp SAI hóa chất vào bồn | Xe bồn nối nhầm ống. Nhãn bồn phai/mất. Operator nhầm | Phản ứng hóa học không kiểm soát! Acid + dung môi → khí độc. NaOH + acid → tỏa nhiệt mãnh liệt → NỔ! | Color-coded pipe + SOP |\n| MORE Level | Mức bồn vượt max | Operator không theo dõi. Level gauge hỏng. Auto shutoff fail | TRÀN! Tràn xăng → bốc hơi → CHÁY NỔ! Tràn acid → ô nhiễm đất → phạt nặng! | Level gauge + high alarm |\n| AS WELL AS | Hơi dung môi + Nguồn lửa | Rò rỉ nhỏ (gasket leak) + tia lửa tĩnh điện / thiết bị điện không phòng nổ | CHÁY NỔ! LEL xăng = 1.4% → chỉ cần rò rất ít + 1 tia lửa = BÙM! | Fire detection |",
            "result": "Recommendations từ HAZOP kho hóa chất:\n\n• Overfill Protection SIL 2: 2 level sensors INDEPENDENT → SIS → auto SHUT OFF nạp khi mức 95% → KHÔNG phụ thuộc operator!\n• Bunding 110% (bờ chắn tràn): Tường bê tông bao quanh TỪNG nhóm bồn → chứa 110% dung tích bồn lớn nhất → TRÀN thì hóa chất NẰM TRONG bờ chắn\n• Chemical compatibility chart (bảng tương thích hóa chất): Dán TẠI kho → NCC + operator PHẢI kiểm tra trước khi nạp\n• Color-coded piping + DISS connection: Mỗi loại hóa chất = ống riêng + đầu nối KHÁC kích thước → VẬT LÝ KHÔNG THỂ NỐI NHẦM! (Poka-Yoke!)\n• Loading SOP: 2 người verify (driver + operator) → check nhãn xe bồn + nhãn bồn chứa + CoA (Certificate of Analysis) → cả 2 KÝ TÊN → mới bắt đầu nạp\n• Ex-rated equipment: TẤT CẢ thiết bị điện trong khu vực kho = ATEX certified (chống cháy nổ)\n• Grounding & bonding: Nối mass xe bồn + bồn chứa → TIÊU TẠN tĩnh điện → không tia lửa\n\n→ Bài học HAZOP: Guide word 'OTHER THAN' (nhầm hóa chất) = kịch bản KINH HOÀNG nhất trong kho hóa chất! Color-coding + DISS connection = Poka-Yoke (KHÔNG THỂ sai!) → AN TOÀN hơn 100 lần SOP!"
        }
    ]
}
