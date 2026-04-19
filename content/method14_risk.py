method = {
    "id": 14,
    "title": "Risk Analysis & Management - Phân tích và quản lý rủi ro",
    "short_name": "Risk Analysis",
    "icon": "🎲",
    "pillar": "Overview",
    "description": "Xác định RỦI RO → Đánh giá: XẢY RA bao % × THIỆT HẠI bao nhiêu = MỨC RỦI RO → Ưu tiên: AVOID / MITIGATE / TRANSFER / ACCEPT.",
    "meaning": """
<p><strong>Risk Analysis & Management (Phân tích và Quản lý Rủi ro)</strong> là quy trình có hệ thống để <strong>xác định (Identify)</strong>, <strong>đánh giá (Assess)</strong>, <strong>ưu tiên (Prioritize)</strong> và <strong>quản lý (Manage)</strong> các rủi ro có thể ảnh hưởng đến MỤC TIÊU của tổ chức.</p>
<p><em>Hình dung: Bạn lái xe → Rủi ro: Tai nạn, hỏng xe, kẹt xe, hết xăng. Mỗi rủi ro có XÁC SUẤT khác nhau (tai nạn = thấp, kẹt xe = cao) và HẬU QUẢ khác nhau (tai nạn = nghiêm trọng, kẹt xe = nhẹ). Quản lý: Đeo dây an toàn (mitigate tai nạn), mua bảo hiểm (transfer), đổ đầy xăng (avoid hết xăng), chấp nhận kẹt xe (accept).</em></p>
<div class="note-box note-box--warning">
    <div class="note-title">⚡ Risk = Likelihood × Impact — Ma trận rủi ro 5×5</div>
    <p><strong>Likelihood (Khả năng xảy ra)</strong>:<br>
    1 = Rare (Hiếm khi — 1 lần/10 năm) → 2 = Unlikely (Ít khi — 1/5 năm) → 3 = Possible (Có thể — 1/năm) → 4 = Likely (Thường xuyên — 1/quý) → 5 = Almost Certain (Gần như chắc chắn — 1/tháng)<br><br>
    <strong>Impact (Mức độ ảnh hưởng)</strong>:<br>
    1 = Insignificant (Không đáng kể — < 10 triệu) → 2 = Minor (Nhỏ — < 50 triệu) → 3 = Moderate (Vừa — < 500 triệu) → 4 = Major (Lớn — < 2 tỷ) → 5 = Catastrophic (Thảm họa — > 2 tỷ hoặc CHẾT NGƯỜI)<br><br>
    <strong>Risk Score = L × I</strong>: 1-4 = LOW (xanh — accept). 5-9 = MEDIUM (vàng — monitor). 10-16 = HIGH (cam — mitigate). 20-25 = EXTREME (đỏ — AVOID hoặc immediate action!)<br><br>
    <strong>4 chiến lược đối phó</strong>:<br>
    🔴 <strong>AVOID (Tránh)</strong>: Không làm hoạt động gây rủi ro! (Ví dụ: Không vào thị trường quá rủi ro)<br>
    🟠 <strong>MITIGATE (Giảm thiểu)</strong>: Giảm L hoặc I! (PM giảm breakdown, fire protection giảm thiệt hại cháy)<br>
    🟡 <strong>TRANSFER (Chuyển giao)</strong>: Chuyển rủi ro cho bên khác! (Bảo hiểm, outsource, hợp đồng)<br>
    🟢 <strong>ACCEPT (Chấp nhận)</strong>: Rủi ro thấp → chấp nhận + theo dõi! (Contingency fund — quỹ dự phòng)</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định rủi ro TRƯỚC KHI chúng xảy ra — PHÒNG bệnh hơn CHỮA bệnh! Rủi ro không quản lý = BOM HẸN GIỜ!</li>
    <li>ĐÁNH GIÁ mức độ: Không phải mọi rủi ro đều nghiêm trọng → L×I = ƯU TIÊN đúng rủi ro quan trọng → KHÔNG lãng phí nguồn lực cho rủi ro nhỏ!</li>
    <li>PHÂN BỔ nguồn lực phòng ngừa HỢP LÝ: Extreme risk = đầu tư lớn! Low risk = chấp nhận → HIỆU QUẢ chi phí!</li>
    <li>GIẢM chi phí thiệt hại: 1 VND phòng ngừa = tiết kiệm 10-100 VND khắc phục! (Chữa cháy đắt hơn phòng cháy 100 lần!)</li>
    <li>Đáp ứng YÊU CẦU PHÁP LUẬT và tiêu chuẩn: ISO 31000 (Risk Management), ISO 9001 clause 6.1, OSHA, HACCP</li>
    <li>Concept ALARP: As Low As Reasonably Practicable — đưa rủi ro về mức THẤP NHẤT có thể TRONG KHẢ NĂNG THỰC TẾ</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: XÁC ĐỊNH rủi ro — "Cái gì có thể xảy ra SAI?"</div>
        <div class="step-card__desc">Brainstorm: Mời team đa chức năng (SX, QC, BT, An toàn, Tài chính) → hỏi "Cái gì có thể xảy ra sai?". Checklist theo danh mục: Thiết bị? Con người? NVL? Tài chính? Pháp luật? Thiên tai? IT? Chuỗi cung ứng? Khách hàng? Đối thủ? Historical data: Xem lại sự cố ĐÃ xảy ra → có thể TÁI PHÁT! SWOT: Threats từ SWOT = rủi ro! Ghi TẤT CẢ vào RISK REGISTER (sổ đăng ký rủi ro) — danh sách đầy đủ!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: ĐÁNH GIÁ rủi ro — Risk = Likelihood × Impact</div>
        <div class="step-card__desc">Cho MỖI rủi ro: Đánh giá <strong>Likelihood (L)</strong>: 1-5 (hiếm → gần chắc chắn). Đánh giá <strong>Impact (I)</strong>: 1-5 (không đáng kể → thảm họa). Tính <strong>Risk Score = L × I</strong>. Plot vào RISK MATRIX 5×5: Extreme (đỏ) → High (cam) → Medium (vàng) → Low (xanh). Lưu ý: Impact nên đánh giá theo NHIỀU chiều: Tài chính? An toàn? Uy tín? Pháp lý? Môi trường? Nếu bất kỳ chiều nào = 5 → Impact = 5! Đánh giá bằng TEAM (consensus) — không phải 1 người quyết định!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Lập KẾ HOẠCH ĐỐI PHÓ — Avoid / Mitigate / Transfer / Accept</div>
        <div class="step-card__desc"><strong>EXTREME risk (20-25)</strong>: AVOID (tránh hoàn toàn) hoặc MITIGATE mạnh → Hành động NGAY! <strong>HIGH risk (10-16)</strong>: MITIGATE (giảm L hoặc I) → Action plan cụ thể, deadline, responsible person. <strong>MEDIUM risk (5-9)</strong>: MITIGATE hoặc TRANSFER (bảo hiểm, hợp đồng) → Theo dõi định kỳ. <strong>LOW risk (1-4)</strong>: ACCEPT (chấp nhận) → Contingency plan nếu xảy ra. Với mỗi action: TRƯỚC action → Risk Score = X. SAU action → Risk Score MỚI = Y (phải GIẢM!) → Đó là RESIDUAL RISK (rủi ro tồn dư).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: GIÁM SÁT + REVIEW — Rủi ro THAY ĐỔI theo thời gian!</div>
        <div class="step-card__desc">Risk Register = tài liệu SỐNG → cập nhật LIÊN TỤC! Review ĐỊNH KỲ (monthly/quarterly): Rủi ro nào ĐÃ GIẢM? Đã xảy ra? Đã close? Rủi ro MỚI nào xuất hiện? (Thay đổi thị trường, pháp luật, công nghệ...). Trigger review: Khi có DỰ ÁN MỚI, sản phẩm mới, NCC mới, thiết bị mới → Risk assessment MỚI! KPI rủi ro: Số incident (sự cố xảy ra) vs. near-miss (suýt xảy ra) → near-miss TĂNG = rủi ro ĐANG TĂNG → action TRƯỚC KHI thành incident!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Risk Assessment dự án mở rộng nhà máy 500 tỷ — Top 4 risk!",
            "industry": "Sản xuất",
            "situation": "Dự án xây mới nhà máy 500 tỷ VND, timeline 18 tháng. BGĐ muốn Risk Assessment trước khi phê duyệt → đảm bảo dự án KHÔNG VỠ TIẾN ĐỘ và NGÂN SÁCH.",
            "analysis": "Risk Register — Top risks dự án:\n\n| # | Rủi ro | L (1-5) | I (1-5) | Risk Score | Chiến lược |\n| R1 | Giá thép/vật liệu TĂNG 20%+ | 4 (Likely — giá biến động thường xuyên) | 4 (Major — tăng ngân sách 50-100 tỷ!) | 16 — HIGH! | MITIGATE |\n| R2 | Chậm giấy phép xây dựng (3-6 tháng) | 3 (Possible — thủ tục phức tạp) | 5 (Catastrophic — delay = mất cơ hội thị trường!) | 15 — HIGH! | AVOID |\n| R3 | Thiếu nhà thầu có năng lực | 3 (Possible — thị trường cạnh tranh) | 4 (Major — delay + quality risk) | 12 — HIGH | MITIGATE |\n| R4 | Bão/mưa kéo dài mùa thi công | 4 (Likely — mùa mưa tháng 7-10) | 3 (Moderate — delay 2-4 tuần) | 12 — HIGH | TRANSFER |\n| R5 | Tai nạn lao động nghiêm trọng | 2 (Unlikely) | 5 (Catastrophic — CHẾT NGƯỜI!) | 10 — HIGH | MITIGATE |\n| R6 | Design change sau khi xây | 3 | 3 | 9 — MEDIUM | AVOID |",
            "result": "Risk Response Plan:\n\n• R1 (Giá vật liệu — Score 16): MITIGATE → Lock giá thép bằng HỢP ĐỒNG DÀI HẠN (mua trước 60% tổng thép lúc giá thấp!) + Mua bảo hiểm giá hàng hóa (commodity hedge) → Risk score SAU: L=2, I=3 = 6 (MEDIUM)\n• R2 (Giấy phép — Score 15): AVOID → Nộp hồ sơ xin phép SỚM 6 THÁNG trước khởi công! + Thuê tư vấn pháp lý chuyên xin phép → TRÁNH delay! → Risk score SAU: L=1, I=3 = 3 (LOW)\n• R4 (Bão/mưa — Score 12): TRANSFER → Mua bảo hiểm xây dựng CAR (Contractor's All Risks) → cover thiệt hại do thiên tai. + Lập kế hoạch thi công ưu tiên phần ngoài trời TRƯỚC mùa mưa → Risk score SAU: L=3, I=2 = 6 (MEDIUM)\n• Contingency budget 15%: 500 tỷ × 15% = 75 tỷ dự phòng → cho rủi ro không lường trước\n\nKết quả: BGĐ phê duyệt dự án SAU KHI thấy Risk Assessment → \"Rủi ro ĐÃ ĐƯỢC QUẢN LÝ!\"\n→ Bài học: Risk Assessment = KHÔNG PHẢI để HỦY dự án → mà để dự án THÀNH CÔNG bằng cách QUẢN LÝ rủi ro!"
        },
        {
            "title": "Risk Assessment an toàn thực phẩm — Antibiotic residue = recall THẢM HỌA!",
            "industry": "Thực phẩm",
            "situation": "Nhà máy chế biến thủy sản XUẤT KHẨU sang EU/US. Nếu phát hiện antibiotic residue → RECALL toàn bộ → mất khách hàng + cấm xuất khẩu! Risk Assessment cho food safety.",
            "analysis": "Risk Register — An toàn thực phẩm:\n\n| # | Rủi ro | L | I | Risk | Impact chi tiết |\n| R1 | Dư lượng kháng sinh (antibiotic residue) vượt MRL (Maximum Residue Limit) | 3 | 5 | 15 — EXTREME! | EU phát hiện → RASFF alert → BAN TOÀN BỘ xuất khẩu từ VN → thiệt hại TOÀN NGÀNH! |\n| R2 | Histamine vượt spec (cá ngừ, cá thu) | 4 | 4 | 16 — EXTREME! | Histamine = gây DỊ ỨNG → recall + kiện tụng + mất khách! |\n| R3 | Kim loại nặng (chì, thủy ngân) | 2 | 5 | 10 — HIGH | Tích tụ trong cơ thể → ung thư → kiện tụng HÀNG TRIỆU USD! |\n| R4 | Allergen cross-contact (tôm lẫn vào cá) | 2 | 5 | 10 — HIGH | Người dị ứng → SỐC PHẢN VỆ → TỬ VONG! → kiện tụng + recall + mất thương hiệu! |\n| R5 | Kim loại (metal fragment) lẫn vào SP | 3 | 4 | 12 — HIGH | Nuốt kim loại → thương tích → recall |",
            "result": "Risk Response — Đa lớp bảo vệ!:\n\n• R1 (Kháng sinh — Score 15):\nMITIGATE: Rapid test 100% lô nguyên liệu → ELISA screening 2 giờ → KHÔNG nhập nếu dương tính!\nMITIGATE: NCC traceability → Mỗi lô NL → trace đến ao nuôi → ao nào từng dùng kháng sinh → ĐÁNH DẤU rủi ro cao!\nTRANSFER: Hợp đồng NCC → NCC chịu 100% thiệt hại nếu NL dương tính kháng sinh\n\n• R2 (Histamine — Score 16):\nMITIGATE: Cold chain monitoring LIÊN TỤC → Sensor nhiệt từ thu hoạch → nhà máy →  15°C!)\nMITIGATE: HACCP CCP tại receiving → test nhiệt + histamine rapid test\n\n• R5 (Kim loại — Score 12):\nMITIGATE: Metal detector + X-ray tại cuối line → 100% sản phẩm đi qua → phát hiện mảnh > 1.5mm\n\n→ Bài học Risk thực phẩm: 1 lô sản phẩm có kháng sinh → EU ban xuất khẩu → TOÀN NGÀNH THIỆT HẠI! Risk Score I=5 → PHẢI xử lý DÙ L thấp! \"Impact 5 = KHÔNG ĐƯỢC XẢY RA DÙ CHỈ 1 LẦN!\""
        },
        {
            "title": "Cybersecurity Risk nhà máy — Ransomware = dừng SX HÀNG TUẦN!",
            "industry": "Sản xuất",
            "situation": "Nhà máy sử dụng SCADA/PLC điều khiển sản xuất. Hacker tấn công ransomware → MÃ HÓA toàn bộ hệ thống → dừng SX → đòi tiền chuộc! Chi phí trung bình 1 vụ ransomware nhà máy: 1.85 triệu USD (IBM 2023).",
            "analysis": "Risk Register — OT (Operational Technology) Security:\n\n| # | Rủi ro | L | I | Risk |\n| R1 | Ransomware mã hóa SCADA/DCS | 3 (Possible — tấn công NM tăng 300%!) | 5 (Catastrophic — dừng SX hàng tuần!) | 15 — EXTREME! |\n| R2 | Legacy system chưa patch (Windows XP, 7 trên HMI) | 5 (Almost certain — 80% NM có legacy!) | 3 (Moderate — backdoor cho hacker) | 15 — EXTREME! |\n| R3 | Supply chain attack qua vendor access (vendor remote vào PLC) | 3 | 4 | 12 — HIGH |\n| R4 | Insider threat (nhân viên cố ý/vô tình) | 2 | 4 | 8 — MEDIUM |",
            "result": "Cybersecurity Risk Response — Defense in Depth!:\n\n• R1 (Ransomware — Score 15):\nMITIGATE: Network segmentation IT/OT → tách HOÀN TOÀN mạng văn phòng (IT) với mạng nhà máy (OT) → ransomware từ email KHÔNG lan sang SCADA!\nMITIGATE: Air-gapped backup → backup OFFLINE (USB/tape) → ransomware KHÔNG MÃ HÓA ĐƯỢC backup! → Recovery Cyber insurance → bảo hiểm cyber cover chi phí khôi phục + mất doanh thu\n\n• R2 (Legacy system — Score 15):\nMITIGATE: Virtual patching → Firewall chặn traffic vào HMI Windows XP → chỉ cho phép protocol cần thiết (Modbus, OPC)\nMITIGATE: Whitelist application → HMI chỉ chạy phần mềm SCADA → block TẤT CẢ phần mềm khác (ransomware = KHÔNG chạy được!)\n\n• R3 (Vendor access — Score 12):\nMITIGATE: Jump server → vendor phải qua jump server (máy trung gian) → log + monitor TẤT CẢ hoạt động → vendor HẾT quyền khi xong\n\n→ Bài học: Ransomware nhà máy = ÁC MỘNG! 1 email phishing → mã hóa SCADA → dừng SX → MẤT TỶ TỶ! Risk Assessment + Defense in Depth = PHÒNG THỦ NHIỀU LỚP!"
        },
        {
            "title": "Risk chuỗi cung ứng — Single source dependency = TIME BOMB!",
            "industry": "Điện tử",
            "situation": "Nhà máy lắp ráp điện tử — 80% linh kiện nhập nước ngoài. Chip thiếu hụt toàn cầu (2021-2023) → ĐỨNG DÂY CHUYỀN! Risk Assessment cho supply chain.",
            "analysis": "Risk Register — Supply Chain:\n\n| # | Rủi ro | L | I | Risk | Chi tiết |\n| R1 | Chip shortage (thiếu hụt chip toàn cầu) | 4 | 5 | 20 — EXTREME! | Không có chip = KHÔNG SẢN XUẤT ĐƯỢC! Lead time từ 8 tuần → 52 tuần! |\n| R2 | Single source dependency (phụ thuộc 1 NCC) | 3 | 5 | 15 — EXTREME! | 15 linh kiện chỉ có 1 NCC! NCC ngừng sản xuất → DEAD! |\n| R3 | Port congestion (tắc cảng/logistics) | 3 | 4 | 12 — HIGH | Container tăng giá 10× + delay 2-4 tuần |\n| R4 | Geopolitical tension (căng thẳng địa chính trị) | 3 | 5 | 15 — EXTREME! | Chiến tranh thương mại → cấm xuất khẩu chip → DỪNG! |",
            "result": "Supply Chain Resilience Strategy:\n\n• R1 + R2 (Chip shortage + Single source):\nMITIGATE: Dual sourcing cho TẤT CẢ linh kiện critical → 2 NCC = 1 hỏng thì còn 1!\nMITIGATE: Safety stock 3 tháng cho top 15 linh kiện critical (trước chỉ 2 tuần!)\nMITIGATE: Local supplier development → phát triển NCC nội địa cho 30% linh kiện → GIẢM phụ thuộc import\nAVOID: Thiết kế dùng chip COMMON (nhiều NCC sản xuất) thay chip UNIQUE (chỉ 1 NCC)\n\n• R3 (Port congestion):\nMITIGATE: Multi-modal transport → đường biển + đường hàng không + đường bộ → đa kênh → không bị stuck!\n\n• R4 (Geopolitical):\nMITIGATE: Supply chain visibility platform → Track TẤT CẢ NCC Tier 1, 2, 3 → Biết NCC Tier 3 ở nước nào → nếu geopolitical risk → CHUYỂN sớm!\n\n→ Bài học: Single source = BOM HẸN GIỜ! COVID + chip shortage → 100 nhà máy DỪNG vì 1 linh kiện thiếu! Dual source + safety stock = BẢO HIỂM chuỗi cung ứng!"
        },
        {
            "title": "Risk thiên tai nhà máy vùng ngập — Flood wall + BCP cứu mạng!",
            "industry": "Sản xuất",
            "situation": "Nhà máy nằm trong vùng ngập lụt lịch sử. Năm 2011 lụt Bangkok — thiệt hại 46 tỷ USD cho ngành SX! Risk Assessment cho thiên tai.",
            "analysis": "Risk Register — Natural Disaster:\n\n| # | Rủi ro | L | I | Risk |\n| R1 | Ngập lụt (mùa mưa/bão) | 4 (Likely — vùng trũng!) | 5 (Catastrophic — máy móc CHÌM = MẤT TOÀN BỘ!) | 20 — EXTREME! |\n| R2 | Bão cấp 12+ | 3 | 4 | 12 — HIGH |\n| R3 | Sét đánh | 4 | 2 | 8 — MEDIUM |\n| R4 | Động đất | 1 (Rare — VN ít động đất mạnh) | 5 | 5 — MEDIUM |",
            "result": "Natural Disaster Risk Response:\n\n• R1 (Ngập lụt — Score 20 EXTREME!):\nMITIGATE: Flood wall 2 mét bao quanh nhà máy → ngăn nước tràn vào!\nMITIGATE: Critical equipment raised → Tủ điện, MCC, server → NÂNG LÊN CAO > 1.5m → nếu nước vào = không ngập thiết bị critical!\nMITIGATE: Sump pump + drainage → Bơm nước ra liên tục → giữ nhà máy khô!\nTRANSFER: Bảo hiểm thiên tai → cover thiệt hại máy móc + mất doanh thu\nPREPARE: BCP (Business Continuity Plan) → Nếu lụt quá lớn → chuyển SX sang nhà máy backup → tiếp tục cung cấp cho khách hàng!\n\n• R2 (Bão): Thiết kế nhà xưởng chịu gió cấp 12 (120 km/h) + bảo hiểm + SOP dọn vật dụng ngoài trời trước bão\n\n• R3 (Sét): Hệ thống chống sét tiếp địa ESE + SPD (bộ chống sét lan truyền trên điện)\n\n→ Bài học: Flood wall 2m = đầu tư 2 tỷ → ngăn thiệt hại 200 tỷ (nếu lụt chìm nhà máy)! Risk Assessment = ĐẦU TƯ THÔNG MINH → ROI = 100:1!"
        }
    ]
}
