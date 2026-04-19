method = {
    "id": 5,
    "title": "FTA - Fault Tree Analysis - Phân tích cây sự cố",
    "short_name": "FTA",
    "icon": "🌳",
    "pillar": "Early Management",
    "description": "Từ sự cố ĐỈNH đi NGƯỢC xuống tìm TẤT CẢ tổ hợp nguyên nhân bằng logic AND/OR — tính xác suất, thiết kế an toàn.",
    "meaning": """
<p><strong>FTA (Fault Tree Analysis — Phân tích Cây sự cố)</strong> là phương pháp phân tích <strong>TOP-DOWN (từ trên xuống)</strong>: Bắt đầu từ 1 sự cố nghiêm trọng (Top Event) → đi ngược xuống tìm TẤT CẢ tổ hợp nguyên nhân có thể gây ra sự cố đó, sử dụng <strong>cổng logic AND/OR</strong>.</p>
<p><em>Hình dung: Giống cây úp ngược — gốc cây (top event) ở trên, rễ cây (nguyên nhân gốc) ở dưới. Mỗi nhánh rễ = 1 đường dẫn đến sự cố!</em></p>
<p>Phát triển bởi Bell Labs năm 1962 cho dự án tên lửa Minuteman của quân đội Mỹ. Được dùng rộng rãi trong hàng không (Boeing), năng lượng hạt nhân, hóa chất, y tế.</p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Cổng Logic AND/OR — "Linh hồn" của FTA</div>
    <p><strong>OR Gate (HOẶC)</strong> ⊞: Top event xảy ra nếu BẤT KỲ nguyên nhân con nào xảy ra.<br>
    → Ví dụ: "Mất điện" = Lưới cắt HOẶC máy phát hỏng HOẶC dây đứt → Chỉ cần 1 cái → mất điện!<br>
    → OR = HỆ THỐNG YẾU (1 lỗi = sự cố!) → Cần GIẢM xác suất mỗi nguyên nhân<br><br>
    <strong>AND Gate (VÀ)</strong> ⊓: Top event chỉ xảy ra khi TẤT CẢ nguyên nhân con CÙNG xảy ra.<br>
    → Ví dụ: "Nổ lò hơi" = Quá áp VÀ van an toàn hỏng VÀ alarm hỏng → Cần cả 3 cùng lúc!<br>
    → AND = HỆ THỐNG MẠNH (nhiều lớp bảo vệ!) → Thêm rào cản = an toàn hơn!<br><br>
    <strong>Minimal Cut Set (Tổ hợp cắt tối thiểu)</strong>: Tập hợp NHỎ NHẤT các basic events mà nếu TẤT CẢ xảy ra → top event xảy ra.<br>
    → Cut set chỉ có 1 event = SINGLE POINT OF FAILURE (điểm yếu chết người!) → <strong>PHẢI loại bỏ!</strong></em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Phân tích nguyên nhân sự cố MỘT CÁCH LOGIC từ trên xuống — không bỏ sót tổ hợp nguyên nhân</li>
    <li>Xác định MINIMAL CUT SETS (tổ hợp cắt tối thiểu) — biết chính xác tổ hợp nào NGUY HIỂM NHẤT</li>
    <li>Tính toán XÁC SUẤT xảy ra sự cố đỉnh (quantitative FTA) — từ xác suất mỗi sự kiện cơ bản</li>
    <li>Thiết kế hệ thống AN TOÀN với REDUNDANCY (dự phòng) — thêm AND gate = thêm lớp bảo vệ</li>
    <li>Phát hiện SINGLE POINT OF FAILURE — chỗ chỉ cần 1 lỗi = sự cố → NGUY HIỂM nhất!</li>
    <li>Phân tích COMMON CAUSE FAILURE (nguyên nhân chung) — 1 nguyên nhân đánh sập NHIỀU lớp bảo vệ cùng lúc</li>
    <li>So sánh với C-E (method 3): C-E = brainstorm RỘNG (6M). FTA = phân tích LOGIC SÂU (AND/OR + xác suất)</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định TOP EVENT — Sự cố gì?</div>
        <div class="step-card__desc">Định nghĩa RÕ RÀNG sự cố đỉnh cần phân tích. Phải CỤ THỂ: Không viết "Máy hỏng" (quá chung) → mà viết "Pellet Mill dừng hoàn toàn — mất sản xuất" hoặc "Nổ lò hơi — thiệt hại khôn lường". Vẽ hình chữ nhật ở đỉnh cây = TOP EVENT.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Xây dựng CÂY SỰ CỐ — AND/OR</div>
        <div class="step-card__desc">Hỏi: "Những gì CÓ THỂ gây ra sự cố này?" → Liệt kê nguyên nhân. MỖI nguyên nhân: Xác định quan hệ logic OR (bất kỳ) hay AND (tất cả) → đặt cổng logic tương ứng. Tiếp tục phân tích sâu: Mỗi nguyên nhân trung gian → hỏi lại "Nguyên nhân nào gây ra NÓ?" → Cho đến khi đến BASIC EVENT (sự kiện cơ bản — không phân tích sâu hơn: sai lầm con người, hỏng phần cứng, điều kiện bên ngoài).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Tìm MINIMAL CUT SETS — Tổ hợp nguy hiểm nhất</div>
        <div class="step-card__desc">Boolean algebra (đại số logic) để tìm minimal cut sets: Tập hợp NHỎ NHẤT basic events → top event xảy ra. Cut set 1 event (single point of failure) → NGUY HIỂM NHẤT → phải loại bỏ hoặc thêm rào cản! Cut set 2 events → cần 2 lỗi đồng thời → ít nguy hiểm hơn. Cut set 3+ events → cần nhiều lỗi → tương đối an toàn.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Tính xác suất + Cải tiến</div>
        <div class="step-card__desc">Gán xác suất cho mỗi basic event (từ dữ liệu hỏng, reliability database). Tính: OR gate: P = 1 - (1-P₁)(1-P₂)... ≈ P₁ + P₂ (khi xác suất nhỏ). AND gate: P = P₁ × P₂ × ... (tích xác suất). → Xác suất top event. Cải tiến: Giảm xác suất basic event ở cut set NGẮN NHẤT → hiệu quả nhất! Hoặc: Biến OR gate thành AND gate (thêm lớp bảo vệ) → giảm xác suất TOÀN BỘ.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Mất điện nhà máy — Cut set {Lưới mất, UPS hỏng} gây dừng 8h!",
            "industry": "Sản xuất chung",
            "situation": "Nhà máy bị MẤT ĐIỆN HOÀN TOÀN → dừng sản xuất 8 giờ → thiệt hại 2 tỷ VND. BGĐ yêu cầu phân tích: \"Tại sao hệ thống dự phòng KHÔNG hoạt động?\"",
            "analysis": "Cây sự cố FTA:\n\nTOP EVENT: Mất điện hoàn toàn nhà máy\n├── OR: Đường dẫn 1 HOẶC Đường dẫn 2\n│   ├── Đường dẫn 1: AND (Lưới điện mất VÀ UPS hỏng)\n│   │   ├── Basic: Lưới EVN mất (P = 0.05/năm)\n│   │   └── Basic: UPS battery hết (P = 0.1/năm — vì không PM!)\n│   └── Đường dẫn 2: AND (Lưới mất VÀ Máy phát không khởi động VÀ UPS hết pin)\n│       ├── Basic: Máy phát hỏng (P = 0.08/năm)\n│       └── Basic: UPS hết pin trước khi máy phát lên (P = 0.05/năm)\n\nMinimal Cut Sets:\n• Cut set 1: {Lưới mất, UPS hỏng} → CHỈ CẦN 2 LỖI! → Nguy hiểm!\n• Cut set 2: {Lưới mất, Máy phát hỏng, UPS hết pin} → cần 3 lỗi → ít nguy hiểm hơn\n\nP(top event) ≈ 0.05 × 0.1 + 0.05 × 0.08 × 0.05 = 0.005 + 0.0002 = 0.52%/năm\n→ Cut set 1 chiếm 96% xác suất sự cố! → UPS KHÔNG PM = ĐIỂM YẾU!",
            "result": "Cải tiến dựa trên FTA:\n\nCut set 1 {Lưới, UPS} — chiếm 96% rủi ro:\n• PM UPS hàng tháng: Test battery + thay battery 3 năm/lần → P(UPS hỏng): 0.1 → 0.01\n• ATS (Automatic Transfer Switch — chuyển nguồn tự động): Lưới mất → ATS tự chuyển → máy phát khởi động trong 10 giây → UPS chỉ cần cấp 10 giây (thay vì hàng giờ!)\n→ P(top event) mới: 0.05 × 0.01 + ... = 0.05%/năm (giảm 10 lần!)\n\nTest máy phát HÀNG TUẦN: Chạy thử 15 phút/tuần → xác nhận máy phát SẴN SÀNG\n\n→ Bài học FTA: FTA chỉ ra cut set NGẮN NHẤT = chỗ yếu nhất! Chỉ cần fix 1 cut set ngắn (UPS PM) → giảm 96% rủi ro!"
        },
        {
            "title": "Nổ lò hơi — AND gate 3 lớp bảo vệ, nhưng Common Cause Failure!",
            "industry": "Tiện ích",
            "situation": "Phân tích FTA để đảm bảo an toàn lò hơi 30 T/h, áp suất 15 bar. Yêu cầu tính xác suất nổ và xác nhận đủ lớp bảo vệ.",
            "analysis": "FTA cho NỔ LÒ HƠI DO QUÁ ÁP:\n\nTOP EVENT: Nổ lò hơi do quá áp\n├── AND: Quá áp VÀ KHÔNG có bảo vệ nào hoạt động!\n│   ├── Nguyên nhân: Áp lực tăng vượt giới hạn 15 bar\n│   │   └── OR: Burner không tắt HOẶC FWC (feedwater control) hỏng\n│   ├── Rào cản 1: Van an toàn (safety valve) HỎNG — không xả áp\n│   ├── Rào cản 2: Pressure switch high-high HỎNG — không trip burner\n│   └── Rào cản 3: Operator KHÔNG phản ứng — không manual shutdown\n\nCut set: {Quá áp, Van an toàn hỏng, Pressure switch hỏng, Operator miss}\n→ Cần 4 LỖI ĐỒNG THỜI! → Xác suất NỔ rất thấp... NHƯNG!\n\n⚠️ COMMON CAUSE FAILURE (nguyên nhân chung):\nNếu KHÔNG BẢO TRÌ (không PM) → Van an toàn kẹt + Pressure switch không hiệu chuẩn + Operator không training → 1 nguyên nhân (thiếu PM) phá VỠ TẤT CẢ 3 rào cản!",
            "result": "Ngăn Common Cause Failure:\n\n• Van an toàn: Test pop 6 tháng/lần (bắt buộc theo TCVN/ASME) → xác nhận xả ở 15.5 bar\n• Pressure switch: Hiệu chuẩn hàng năm + INDEPENDENT (độc lập) với hệ thống điều khiển chính\n• Operator: Drill (diễn tập) khẩn cấp hàng quý + kiểm tra kỹ năng\n• Redundant safety valve: Lắp 2 van an toàn KHÁC LOẠI (khác nhà sản xuất) → 1 kẹt thì còn 1!\n• Diversity (đa dạng hóa): Van an toàn (cơ khí) + Pressure switch (điện tử) + Operator (con người) = 3 LOẠI HOÀN TOÀN KHÁC → không có common cause!\n\n→ Bài học FTA: AND gate = AN TOÀN... nhưng Common Cause có thể phá vỡ TẤT CẢ lớp AND! → FTA buộc phải suy nghĩ: \"Có gì có thể làm NHIỀU rào cản hỏng CÙNG LÚC không?\""
        },
        {
            "title": "Tai nạn kẹp tay máy dập — Light curtain + Two-hand = AND gate!",
            "industry": "Gia công kim loại",
            "situation": "Phân tích FTA rủi ro tai nạn kẹp tay trên máy dập 200 tấn. Yêu cầu đạt xác suất tai nạn < 10⁻⁶/năm (1 phần triệu).",
            "analysis": "FTA cho KẸP TAY MÁY DẬP:\n\nTOP EVENT: Kẹp tay\n├── AND: Tay trong vùng nguy hiểm VÀ Máy cycle (ép xuống)\n│   ├── Tay trong vùng nguy hiểm:\n│   │   └── AND: Light curtain (rèm quang) bị vượt qua VÀ Two-hand control bypass\n│   │       ├── Light curtain hỏng (P = 10⁻³/năm)\n│   │       └── OR: Two-hand bị bypass HOẶC relay lỗi\n│   │           ├── Operator bypass (bọc dây) (P = 10⁻²/năm)\n│   │           └── Safety relay lỗi (P = 10⁻⁴/năm)\n│   └── Máy cycle khi không nên:\n│       └── OR: Nút bấm nhầm HOẶC PLC lỗi\n\nMinimal Cut Set nguy hiểm nhất:\n{Light curtain hỏng, Operator bypass two-hand, Nút bấm nhầm}\nP ≈ 10⁻³ × 10⁻² × 10⁻¹ = 10⁻⁶ → VỪA ĐẠT ngưỡng!\n→ Nhưng nếu operator bypass (bọc dây) → single point of failure!",
            "result": "Cải tiến để đạt Anti-bypass monitoring (chống bọc dây): Hệ thống giám sát → nếu 2 nút bấm được nhấn cùng lúc liên tục (bọc dây!) → MÁY TỰ DỪNG + BÁO ĐỘNG\n→ P(bypass): 10⁻² → 10⁻⁴\n• Light curtain SIL 3 (Safety Integrity Level 3): Nâng cấp từ SIL 1 → SIL 3\n→ P(light curtain hỏng): 10⁻³ → 10⁻⁵\n• Safety PLC (PLC an toàn riêng biệt): Không dùng PLC thường cho chức năng safety\n\nP(top event) mới: 10⁻⁵ × 10⁻⁴ × 10⁻¹ = 10⁻¹⁰ → AN TOÀN cực kỳ!\n\n→ Bài học FTA cho an toàn: 1. Bypass là kẻ thù #1 của safety! 2. Thêm AND gate (thêm rào cản) = giảm xác suất CÀ MÁ! 3. SIL level phải PHÙ HỢP với mức rủi ro!"
        },
        {
            "title": "Sập server ngân hàng — Active-active cluster, đạt 99.995%!",
            "industry": "Tài chính",
            "situation": "Hệ thống core banking yêu cầu availability 99.99% (downtime < 52 phút/năm!). FTA để thiết kế kiến trúc đạt mục tiêu.",
            "analysis": "FTA cho SERVICE DOWN:\n\nTOP EVENT: Core banking service down\n├── AND: Primary server down VÀ Secondary server down (active-active cluster)\n│   ├── Primary down:\n│   │   └── OR: Hardware fail (P=0.02) HOẶC Software crash (P=0.05) HOẶC Network fail (P=0.03) HOẶC Power fail (P=0.01)\n│   │   → P(primary down) ≈ 0.11/năm\n│   └── Secondary down:\n│   │   → P(secondary down) ≈ 0.11/năm (giống primary)\n\nVới active-active AND gate:\nP(cả 2 down cùng lúc) = 0.11 × 0.11 = 0.012/năm\nAvailability = 1 - (0.012 × MTTR/8760) ≈ 99.99% ✓ Vừa đạt!\n\nNHƯNG! Common Cause: Nếu cả 2 server cùng DC (data center) → DC bị cháy/mất điện → CẢ 2 DOWN!\n→ Common cause phá vỡ AND gate!",
            "result": "Cải tiến theo FTA:\n\n• Geo-redundancy (dự phòng địa lý): Primary ở DC Hà Nội, Secondary ở DC HCM → Cháy 1 DC → DC kia VẪN CHẠY!\n→ Loại bỏ common cause \"cùng DC\"\n\n• Auto-failover : Khi primary down → DNS tự chuyển traffic → secondary trong Thêm AND gate (thêm 1 layer): Database replication + Read replica → ngay cả khi cả 2 app server down → database VẪN AN TOÀN\n\nP(top event) mới: 0.11 × 0.11 × 0.001 (common cause eliminated) = 1.2 × 10⁻⁵\n→ Availability: 99.995%! Vượt mục tiêu!\n\n→ Bài học FTA cho IT: Redundancy chỉ hiệu quả khi LOẠI BỎ common cause (khác DC, khác cloud provider, khác network)!"
        },
        {
            "title": "Rò rỉ Chlorine nhà máy nước — Double block & bleed valve!",
            "industry": "Hóa chất",
            "situation": "Phân tích FTA rủi ro rò rỉ khí Chlorine (Cl₂ — khí độc!) tại nhà máy xử lý nước. Cl₂ rò rỉ → công nhân HÍT PHẢI → ngộ độc → có thể TỬ VONG!",
            "analysis": "FTA cho RÒ RỈ CHLORINE:\n\nTOP EVENT: Rò rỉ Cl₂ ra môi trường làm việc\n├── OR: Nguồn rò rỉ (bất kỳ cái nào!)\n│   ├── Valve chính hỏng (P = 0.01/năm)\n│   ├── Đường ống bị ăn mòn (corrosion) thủng (P = 0.005/năm)\n│   ├── AND: Gasket rò VÀ Gas detector hỏng (P = 0.02 × 0.05 = 0.001)\n│   └── AND: Operator mở sai van VÀ Interlock bypass (P = 0.03 × 0.01 = 0.0003)\n\nMinimal Cut Sets:\n• {Valve hỏng} → SINGLE POINT OF FAILURE! Cut set = 1 event!\n• {Pipe corrode} → SINGLE POINT OF FAILURE!\n• {Gasket rò, Detector hỏng} → Cut set 2 → ít nguy hiểm hơn\n\nP(top event) ≈ 0.01 + 0.005 + 0.001 + 0.0003 = 1.63%/năm → QUÁ CAO cho khí độc!",
            "result": "Loại bỏ SINGLE POINT OF FAILURE:\n\n• Valve: Double block & bleed (van kép): 2 van nối tiếp + 1 van xả giữa → rò van 1 → van 2 VẪN GIỮ → biến OR thành AND!\n→ P(valve rò) = 0.01 × 0.01 = 0.0001\n\n• Pipe: Kiểm tra ăn mòn: UT (siêu âm đo độ dày) hàng năm + thay ống khi mỏng Gas detector REDUNDANT (dự phòng): 2 detector KHÁC LOẠI (electrochemical + IR) → 1 hỏng thì còn 1\n\n• Interlock NON-BYPASSABLE: Interlock KHÔNG THỂ tắt bằng key → operator không bypass được\n\nP(top event) mới: 0.06%/năm → giảm 27 lần! Đạt ALARP (As Low As Reasonably Practicable — thấp nhất có thể thực hiện được)\n\n→ Bài học FTA: CUT SET 1 EVENT = SINGLE POINT OF FAILURE → phải biến thành cut set 2-3 events bằng cách THÊM rào cản (AND gate)!"
        },
        {
            "title": "Quá liều thuốc bệnh viện — 3 rào cản bảo vệ bệnh nhân!",
            "industry": "Y tế",
            "situation": "Phân tích FTA rủi ro bệnh nhân nhận QUÁ LIỀU thuốc. Sai liều = ĐE DỌA TÍNH MẠNG! Cần thiết kế hệ thống có nhiều lớp bảo vệ.",
            "analysis": "FTA cho QUÁ LIỀU THUỐC:\n\nTOP EVENT: Bệnh nhân nhận quá liều\n├── OR: (Bất kỳ đường dẫn nào → quá liều!)\n│   ├── Đường dẫn 1: AND: BS kê sai VÀ Dược sĩ không phát hiện\n│   │   ├── BS kê sai liều (P = 0.02) — viết gấp, mệt, nhầm đơn vị\n│   │   └── Dược sĩ miss (P = 0.1) — quá tải, không để ý\n│   ├── Đường dẫn 2: AND: Điều dưỡng cho sai liều VÀ Barcode scan bypass\n│   │   ├── ĐD cho sai liều (P = 0.01) — nhầm bệnh nhân, nhầm thuốc\n│   │   └── Bypass barcode (P = 0.05) — scanner hỏng, vội nên không scan\n│   └── Đường dẫn 3: Infusion pump cài sai (P = 0.005)\n\nMinimal Cut Sets:\n• {BS sai, Dược sĩ miss}: P = 0.02 × 0.1 = 0.002 → 2/1000!\n• {ĐD sai, Bypass scan}: P = 0.01 × 0.05 = 0.0005\n• {Pump sai}: SINGLE POINT OF FAILURE! P = 0.005",
            "result": "Cải tiến bằng thêm rào cản (AND gate):\n\nĐường dẫn 1 — BS kê sai:\n• CPOE (Computerized Physician Order Entry — kê đơn điện tử): Hệ thống TỰ ĐỘNG cảnh báo khi liều NGOÀI KHOẢNG an toàn → BS phải confirm → thêm 1 AND gate!\n→ P(BS sai MÀ CPOE không bắt) = 0.02 × 0.01 = 0.0002\n\nĐường dẫn 2 — ĐD cho sai:\n• Barcode verification BẮT BUỘC: Hệ thống KHÔNG CHO phát thuốc nếu chưa scan → LOẠI BỎ bypass!\n→ P(bypass) = 0.05 → 0.001\n\nĐường dẫn 3 — Pump sai (single point):\n• Smart pump với dose limits: Pump TỰ ĐỘNG từ chối liều ngoài khoảng an toàn → thêm AND gate!\n→ P = 0.005 × 0.001 = 0.000005\n\n→ Bài học FTA y tế: Hệ thống y tế CẦN nhiều AND gate! Mỗi AND gate = 1 rào cản → BS sai → CPOE bắt. CPOE miss → Dược sĩ bắt. Dược sĩ miss → Barcode bắt. = \"SWISS CHEESE MODEL\" (mô hình lỗ phô mai xếp chồng)!"
        }
    ]
}
