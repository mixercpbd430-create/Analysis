method = {
    "id": 41,
    "title": "RCM - Reliability Centered Maintenance",
    "short_name": "RCM",
    "icon": "🔧",
    "pillar": "Planned Maintenance",
    "description": "Xác định chiến lược bảo trì TỐI ƯU cho từng thiết bị — đúng máy, đúng cách, đúng lúc. Không thiếu, không thừa!",
    "meaning": """
<p><strong>RCM (Reliability Centered Maintenance — Bảo trì tập trung vào Độ tin cậy)</strong> là phương pháp xác định chiến lược bảo trì PHÙ HỢP NHẤT cho từng thiết bị, dựa trên phân tích: Chức năng → Cơ chế hỏng → Hậu quả → Biện pháp hiệu quả nhất.</p>
<p><em>Nói đơn giản: RCM trả lời câu hỏi "Nên bảo trì máy này THEO CÁCH NÀO?" — Kiểm tra định kỳ? Giám sát tình trạng? Hay chạy đến khi hỏng rồi thay? → Mỗi máy, mỗi bộ phận CÓ CÂU TRẢ LỜI KHÁC NHAU!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 7 câu hỏi RCM (theo SAE JA1011 — Tiêu chuẩn quốc tế)</div>
    <p><strong>1. Chức năng (Function)</strong>: Thiết bị này LÀM GÌ? Tiêu chuẩn hiệu suất là gì?<br>
    <strong>2. Hỏng chức năng (Functional Failure)</strong>: Máy KHÔNG LÀM ĐƯỢC GÌ khi hỏng?<br>
    <strong>3. Cơ chế hỏng (Failure Mode)</strong>: Hỏng THEO CÁCH NÀO? (bạc đạn mòn? motor cháy? van kẹt?)<br>
    <strong>4. Hậu quả tức thì (Failure Effect)</strong>: KHI HỎNG thì xảy ra gì? (dừng máy? rò rỉ? nguy hiểm?)<br>
    <strong>5. Mức độ nghiêm trọng (Failure Consequence)</strong>: Hậu quả thuộc loại nào? An toàn/Môi trường? Ẩn? Vận hành? Không vận hành?<br>
    <strong>6. Biện pháp chủ động (Proactive Task)</strong>: CÓ THỂ ngăn chặn/phát hiện sớm không?<br>
    <strong>7. Hành động mặc định (Default Action)</strong>: Nếu KHÔNG THỂ ngăn chặn → Chạy đến hỏng (RTF)? Thiết kế lại?<br><br>
    <strong>4 loại chiến lược BT từ RCM</strong>:<br>
    • <strong>CBM (Condition-Based Maintenance)</strong>: Giám sát tình trạng → sửa KHI CẦN (rung? nóng? mòn?) = Thông minh nhất!<br>
    • <strong>TBM (Time-Based Maintenance)</strong>: Thay định kỳ theo thời gian/số giờ chạy = Truyền thống<br>
    • <strong>FF (Failure-Finding)</strong>: Kiểm tra thiết bị an toàn → xem CÒN HOẠT ĐỘNG KHÔNG (van an toàn, báo cháy...)<br>
    • <strong>RTF (Run-To-Failure)</strong>: Chạy đến khi hỏng → thay mới = OK cho thiết bị RẺ, KHÔNG QUAN TRỌNG</p>
</div>
""",
    "purpose": """
<ul>
    <li>Chọn ĐÚNG chiến lược BT cho TỪNG thiết bị: PM, PdM (CBM), RTF — không phải tất cả máy bảo trì giống nhau!</li>
    <li>Loại bỏ PM tasks KHÔNG CẦN THIẾT (over-maintenance — bảo trì QUÁ nhiều cũng lãng phí!)</li>
    <li>Tập trung nguồn lực vào thiết bị CRITICAL (quan trọng nhất)</li>
    <li>Giảm chi phí bảo trì tổng thể 20-40% MÀ reliability TĂNG (ít hơn nhưng ĐÚNG hơn!)</li>
    <li>Đáp ứng yêu cầu an toàn và môi trường — thiết bị an toàn LUÔN được kiểm tra (failure-finding)</li>
    <li>Dựa trên DỮ LIỆU và LOGIC — không phải "cảm tính" hay "kinh nghiệm" hay "OEM nói thế"</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Chọn thiết bị và phân tích CHỨC NĂNG</div>
        <div class="step-card__desc">Chọn thiết bị CRITICAL trước (dùng ABC analysis — method 38). Liệt kê TẤT CẢ chức năng: Chức năng chính (primary — ví dụ: ép viên 40 T/h, PDI > 92%) + Chức năng phụ (secondary — an toàn, môi trường, bảo vệ). Xác định TIÊU CHUẨN hiệu suất (performance standard) cho mỗi chức năng.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: FMEA — Phân tích cơ chế hỏng</div>
        <div class="step-card__desc">Liệt kê functional failures (mất/suy giảm chức năng) — ví dụ: "Máy không ép được viên" hoặc "Máy ép chậm hơn 40 T/h". Xác định failure modes (cơ chế hỏng cụ thể) — bạc đạn mòn? Die nứt? Motor quá nhiệt? Failure effects (hậu quả) — dừng dây chuyền? rò rỉ dầu? nguy hiểm NV? Dùng FMEA worksheet (bảng phân tích).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: RCM Decision Logic — Chọn chiến lược BT</div>
        <div class="step-card__desc">Phân loại hậu quả: <strong>Safety/Environment (an toàn/môi trường → ưu tiên cao nhất!)</strong> → Hidden (ẩn — hỏng mà không ai biết, ví dụ: van an toàn) → Operational (ảnh hưởng SX) → Non-operational (không ảnh hưởng SX). Chọn task theo logic: CBM (nếu có thể giám sát) → TBM (nếu biết tuổi thọ) → FF (nếu là thiết bị an toàn ẩn) → RTF (nếu rẻ và không ảnh hưởng) → Redesign (nếu không giải pháp nào hiệu quả).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Triển khai và duy trì (Living Program)</div>
        <div class="step-card__desc">Cập nhật PM schedule theo recommendations từ RCM (bỏ tasks không cần, thêm CBM, thêm FF). Đào tạo team BT cách tư duy RCM. Theo dõi kết quả: MTBF tăng? Availability tăng? Chi phí giảm? Review RCM khi: Thêm thiết bị mới, thay đổi điều kiện vận hành, failure pattern thay đổi.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "RCM Pellet Mill — Giảm 17 PM tasks, breakdown giảm 58%!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Pellet mill — thiết bị CRITICAL nhất nhà máy TACN. PM hiện tại: 45 tasks nhưng vẫn breakdown 480 giờ/năm! Vừa TỐN tiền PM, vừa KHÔNG hiệu quả!",
            "analysis": "Phân tích RCM 7 câu hỏi cho pellet mill:\n\nChức năng chính: Ép viên 40 T/h, PDI > 92%\n\n35 failure modes phân tích → Chọn chiến lược BT cho từng cơ chế hỏng:\n• Die nứt → CBM: Giám sát rung động (vibration monitoring) → rung tăng = die sắp nứt → THAY TRƯỚC KHI VỠ hoàn toàn!\n• Bạc đạn chính (main bearing) → CBM: Giám sát rung + nhiệt độ → phát hiện sớm 2-4 tuần trước khi hỏng\n• Motor cháy cuộn dây (winding) → CBM: Đo điện trở cách điện (insulation test) hàng quý\n• Gearbox → CBM: Phân tích dầu (oil analysis) → phát hiện mạt kim loại = bánh răng mòn\n• Van hơi (steam valve) → TBM: Thay ron (gasket) mỗi 6 tháng (vật tư mòn — wear part)\n• Trục vít nạp liệu (feeder screw) → RTF: Rẻ, thay nhanh, không ảnh hưởng an toàn → chạy đến hỏng OK!",
            "result": "Trước RCM: 45 PM tasks → tốn 800 triệu/năm → BREAKDOWN vẫn 480 giờ!\n→ Vấn đề: Nhiều task nhưng SAI LOẠI! Quá nhiều TBM (thay định kỳ) cho bộ phận cần CBM. Và thiếu CBM cho bộ phận critical!\n\nSau RCM: 28 tasks (BỎ 17 task không cần thiết!) + THÊM 5 CBM tasks:\n• Chi phí BT: 800 → 600 triệu/năm (giảm 25%)\n• Breakdown: 480 → 200 giờ/năm (giảm 58%!)\n\n→ Bài học RCM: NHIỀU PM hơn ≠ TỐT hơn! PM ĐÚNG TYPE + ĐÚNG CHỖ mới quan trọng!"
        },
        {
            "title": "RCM Boiler — An toàn KHÔNG được phép hỏng!",
            "industry": "Sản xuất chung",
            "situation": "Lò hơi (boiler) 10 tấn/giờ, áp suất 10 bar: Thiết bị CRITICAL + AN TOÀN (áp suất cao → NỔ nếu hỏng thiết bị bảo vệ!). PM theo thời gian tốn kém.",
            "analysis": "RCM phân tích theo hậu quả:\n\nThiết bị AN TOÀN (Safety → Failure-Finding BẮT BUỘC):\n• PSV (Pressure Safety Valve — Van an toàn áp suất) → FF: Test áp suất mở van HÀNG NĂM (bắt buộc theo luật!). Van này \"nằm im\" suốt nhưng PHẢI HOẠT ĐỘNG khi áp suất cao quá → nếu kẹt → NỔ!\n• LWCO (Low Water Cut-Off — Thiết bị ngắt khi thiếu nước) → FF: Test HÀNG THÁNG! Nếu thiếu nước mà boiler vẫn đốt → ống nổ → thảm họa!\n\nThiết bị VẬN HÀNH:\n• Ống lò (tube) → CBM: Đo độ dày (thickness measurement) + kiểm soát chất lượng nước cấp\n• Bạc đạn quạt FD fan → CBM: Giám sát rung\n• Đầu đốt (burner) → TBM: Overhaul hàng năm (điều chỉnh, vệ sinh)\n• Vật liệu chịu lửa (refractory) → TBM: Kiểm tra hàng năm bằng mắt + camera nhiệt",
            "result": "RCM cho boiler:\n• Tasks an toàn (PSV, LWCO): KHÔNG BAO GIỜ BỎ! → Failure-finding bắt buộc theo quy định + lương tâm\n• CBM cho ống lò: Phát hiện mỏng TRƯỚC KHI rò rỉ → tránh dừng khẩn cấp\n• Camera nhiệt kiểm tra refractory: Tìm điểm nóng = chỗ vật liệu bị bong\n• PM tasks giảm 30% (bỏ các task TBM không cần thiết), AN TOÀN cải thiện!\n\n→ Bài học RCM cho thiết bị an toàn: Thiết bị bảo vệ (PSV, cầu dao chống cháy, interlock...) là HIDDEN FAILURE (hỏng ẩn — hỏng mà KHÔNG AI BIẾT cho đến khi cần mà nó không hoạt động!) → PHẢI kiểm tra định kỳ bằng Failure-Finding!"
        },
        {
            "title": "RCM 50 băng tải — Giảm 53% PM tasks!",
            "industry": "Sản xuất chung",
            "situation": "Nhà máy có 50 băng tải. PM routine tốn RẤT NHIỀU thời gian KTV. Nhiều tasks KTV chỉ đi kiểm tra rồi tick ✓ mà không tìm thấy gì (inspection fatigue — mệt mỏi kiểm tra).",
            "analysis": "RCM phân loại 50 băng tải → KHÔNG PHẢI tất cả bang tải đều quan trọng như nhau!\n\nCritical conveyor (5 chiếc): Trên đường sản xuất chính, hỏng = DỪM DÂY CHUYỀN\n→ Full CBM: Đo xích (chain elongation), rung bạc đạn, nhiệt motor\n\nImportant (15 chiếc): Có đường bypass hoặc buffer\n→ Basic PM: Kiểm tra tuần + bôi trơn tháng\n\nNon-critical (30 chiếc): Có dự phòng hoặc ít ảnh hưởng\n→ Giảm PM đáng kể: Nhiều bộ phận chuyển sang RTF!\n• Tấm lót máng (trough liner) → RTF: Rẻ, thay nhanh, không ảnh hưởng an toàn → chờ mòn hết → thay\n• Nắp che xích (chain guard) → FF: Kiểm tra tuần (nhìn bằng mắt) — không cần tháo ra kiểm tra kỹ",
            "result": "Kết quả RCM cho 50 băng tải:\n• Trước: 50 băng tải × 15 tasks/chiếc = 750 PM tasks/tháng! (KTV kiệt sức)\n• Sau RCM: Giảm còn 350 tasks (giảm 53%!)\n- 5 critical: 15 tasks/chiếc (full CBM) = 75\n- 15 important: 8 tasks/chiếc = 120\n- 30 non-critical: 5 tasks/chiếc (chủ yếu inspect) = 150 + 5 bỏ hoàn toàn\n\nTiết kiệm: 200 man-hours/tháng! KTV có thời gian tập trung vào thiết bị critical\n→ Bài học: Không phải MỌI thiết bị đều cần bảo trì giống nhau! 30 băng tải non-critical chạy RTF → hoàn toàn OK!"
        },
        {
            "title": "RCM Máy phát điện dự phòng — Hidden Failure nguy hiểm!",
            "industry": "Sản xuất chung",
            "situation": "Generator dự phòng 1,000 kVA: Chạy chỉ 20 giờ/năm (khi mất điện lưới). Nhưng KHI CẦN → phải chạy NGAY! Liệu có chạy được không?",
            "analysis": "Đây là ví dụ kinh điển về HIDDEN FAILURE (hỏng ẩn)!\n\nMáy phát chỉ chạy khi mất điện. Vấn đề: Nếu máy phát BỊ HỎNG nhưng KHÔNG AI BIẾT (vì nó đang nằm im!) → Đến lúc mất điện → khởi động → KHÔNG CHẠY → nhà máy TỐI ĐEN, thiệt hại hàng tỷ đồng!\n\nRCM chỉ ra: Máy phát dự phòng cần FAILURE-FINDING, không phải TBM!\n• Failure-Finding chính: Khởi động thử HÀNG TUẦN 15 phút → xác nhận máy SẴN SÀNG\n• Ắc-quy (Battery) → TBM: Test hàng tháng + THAY ở 2.5 năm (không chờ hỏng — ắc-quy = NGUYÊN NHÂN #1 máy phát không khởi động!)\n• ATS (Auto Transfer Switch) → FF: Test mô phỏng mất điện HÀNG THÁNG (ATS tự động chuyển nguồn)\n• Nhiên liệu → TBM: Xử lý diesel cũ (stale fuel → đông đặc), xả nước đọng trong bồn",
            "result": "Kết quả sau áp dụng RCM:\n• Test khởi động hàng tuần: 15 phút mỗi tuần → mức tin cậy 99% sẵn sàng!\n• Thay ắc-quy ở 2.5 năm: Trước đó chờ hỏng → 2 lần mất điện mà máy phát không chạy!\n• ATS test monthly: Phát hiện 1 lần ATS bị kẹt relay → sửa trước khi mất điện thật\n\nReliability khi cần: từ 85% lên 99%!\n→ Bài học QUAN TRỌNG: Thiết bị dự phòng + thiết bị an toàn = HIDDEN FAILURE → Nếu không kiểm tra (Failure-Finding) → bạn KHÔNG BIẾT nó đã hỏng → đến lúc cần → thảm họa!"
        },
        {
            "title": "RCM Packaging Machine — Chuyển 60% PM cho Operator!",
            "industry": "Thực phẩm",
            "situation": "Máy đóng gói FFS (Form-Fill-Seal): Hay dừng vặt (minor stops) nhưng hiếm khi hỏng nặng. KTV BT phải đến sửa mỗi khi dừng vặt → MẤT THỜI GI → KTV không còn thời gian cho thiết bị critical!",
            "analysis": "RCM phân tích failure modes máy đóng gói:\n\n• Thanh hàn (Seal bar) — TBM: Thay heater element (thanh nung) mỗi 2,000 giờ (tuổi thọ biết trước)\n• Xi-lanh khí nén (Jaw pneumatic) — CBM: Test áp suất → nếu giảm = seal kém\n• Bộ căng film (Film tensioner) — TBM: Điều chỉnh mỗi 500 giờ\n• Máy in date (Date coder) — RTF: Có sẵn spare → hỏng thì thay nhanh (5 phút)\n• Mắt đọc (Photo eye) — FF: Test hàng tuần → đảm bảo đọc đúng vị trí cắt\n\nInsight quan trọng: Phần lớn minor stops là việc VẬN HÀNH (clean, adjust, inspect) → KHÔNG CẦN kỹ thuật viên!",
            "result": "RCM recommendation:\n• 60% tasks chuyển thành AM (Autonomous Maintenance — BT tự chủ bởi Operator):\n- Operator vệ sinh đầu hàn HÀNG NGÀY → giảm 70% minor stops!\n- Operator kiểm tra film tension, photo eye, air pressure MỖI ĐẦU CA\n- Operator điều chỉnh nhỏ khi cần (có SOP)\n• 40% tasks còn lại cho KTV: Thay heater element (TBM), test pneumatic system (CBM) → HÀNG QUÝ\n\nKết quả: KTV BT được GIẢI PHÓNG cho thiết bị critical! Máy đóng gói: Minor stops giảm 70%.\n→ Bài học RCM: Không phải mọi PM đều cần KTV! Operator CŨNG LÀ người bảo trì!"
        },
        {
            "title": "RCM 200 Motor — Không cần test TẤT CẢ!",
            "industry": "Sản xuất chung",
            "situation": "200 motor trong nhà máy. PM hiện tại: Đo insulation + vibration TẤT CẢ 200 motor mỗi 6 tháng = 400 man-hours (50 ngày công!) → Quá nặng!",
            "analysis": "RCM phân loại 200 motor theo CONSEQUENCE (hậu quả nếu hỏng):\n\nCritical motors — 25 chiếc (>50kW, không dự phòng, hỏng = dừng nhà máy):\n→ Full CBM: Vibration + current + thermal HÀNG QUÝ\n\nImportant — 50 chiếc (15-50kW):\n→ Basic CBM: Vibration 6 tháng/lần\n\nNon-critical — 125 chiếc (:\n→ RTF! Chỉ kiểm tra bằng mắt khi tiện (visual inspect). Hỏng → thay spare motor → sửa motor hỏng từ từ\n\nLý do RTF OK cho non-critical: Motor nhỏ rẻ, có spare sẵn, thay 30 phút, không ảnh hưởng SX (có dự phòng)",
            "result": "Kết quả:\n• Trước: Test 200 motor = 400 man-hours/6 tháng\n• Sau RCM: Full CBM 25 + Basic CBM 50 + RTF 125 = 150 man-hours (giảm 63%!)\n• Tỷ lệ hỏng motor: KHÔNG THAY ĐỔI! → Vì 125 motor non-critical hỏng cũng không ảnh hưởng (có backup)\n\n→ Tiết kiệm 250 man-hours (31 ngày công!) để tập trung vào 25 motor THỰC SỰ QUAN TRỌNG\n→ Bài học RCM: RTF (chạy đến hỏng) KHÔNG PHẢI là xấu! Cho thiết bị rẻ + có backup + không an toàn → RTF là chiến lược THÔNG MINH!"
        },
        {
            "title": "RCM hệ thống PCCC — An toàn KHÔNG THƯƠNG LƯỢNG!",
            "industry": "Sản xuất chung",
            "situation": "Hệ thống PCCC (sprinkler + bơm chữa cháy + báo cháy): Thiết bị an toàn CỰC KỲ QUAN TRỌNG. Bảo hiểm yêu cầu maintenance log. Nhưng nhiều nhà máy \"lắp xong quên\"!",
            "analysis": "RCM phân tích hệ thống PCCC:\n\nPCCC là TOÀN BỘ HIDDEN FAILURE! → Tất cả đều nằm im cho đến khi CÓ CHÁY → nếu hỏng mà không biết → cháy xảy ra → thiệt hại khủng khiếp!\n\n• Bơm chữa cháy (Fire pump) → FF: Khởi động thử HÀNG TUẦN (không tải) + Test full lưu lượng HÀNG NĂM\n• Bơm jockey (bơm bù áp) → FF: Kiểm tra hoạt động HÀNG TUẦN\n• Đầu phun sprinkler → TBM: Kiểm tra bằng mắt hàng năm. Test FPI (Fire Protection Inspector) theo NFPA\n• Tủ báo cháy (Fire alarm panel) → FF: Test detector (đầu dò khói/nhiệt) 6 tháng/lần\n• Van chặn (Valves) → FF: Kiểm tra mở/đóng 3 tháng/lần + test tamper switch (công tắc chống can thiệp)\n• Bình chữa cháy → TBM: Kiểm tra hàng tháng + thử thủy lực 5 năm/lần",
            "result": "Kết quả áp dụng RCM cho PCCC:\n• TẤT CẢ tasks là Failure-Finding (kiểm tra thiết bị an toàn CÒN HOẠT ĐỘNG KHÔNG)\n• Thêm: Giám sát LIÊN TỤC vị trí van bằng IoT (sensor → alert nếu ai đóng van chặn)\n• Thêm: CBM rung cho bơm chữa cháy\n• Bảo hiểm GIẢM PHÍ 10% khi có RCM program có tài liệu chứng minh!\n\n→ Bài học PCCC: Hệ thống PCCC nằm im 99.99% thời gian → HIDDEN FAILURE mặc định! Nếu không test → bạn KHÔNG BIẾT nó có hoạt động không → đến khi cháy → QUÁ MUỘN!"
        },
        {
            "title": "RCM Clean Room HVAC (Dược phẩm) — HEPA filter tiết kiệm $20K/năm!",
            "industry": "Dược phẩm",
            "situation": "HVAC phòng sạch (clean room): CRITICAL cho chất lượng thuốc. AHU (Air Handling Unit) + Chiller + Đường ống. Thay HEPA filter LÀ CHI PHÍ LỚN!",
            "analysis": "RCM phân tích từng bộ phận HVAC phòng sạch:\n\n• HEPA filter (bộ lọc không khí siêu mịn) → CBM!\nHiện tại: Thay theo lịch 6 tháng/lần (TBM) → RẤT TỐN (HEPA đắt!)\nRCM chỉ ra: Dùng differential pressure (chênh áp) → Khi ΔP = 2× giá trị ban đầu → THAY. Nhiều HEPA vẫn TỐT ở 6 tháng → thay sớm = LÃNG PHÍ!\n\n• Quạt AHU (blower) bearing → CBM: Vibration monitoring\n• Dây curoa (belt) → TBM: Thay 6 tháng (rẻ, dễ thay)\n• Damper actuator (cơ cấu điều khiển lá van gió) → FF: Test 3 tháng/lần → nếu kẹt → cân bằng gió phòng sạch bị lệch → sản phẩm contaminated!\n\n• Chiller compressor → CBM: Oil analysis + vibration → phát hiện trước hỏng (hỏng chiller = $100K+ sửa!)",
            "result": "Kết quả RCM:\n• HEPA filter: Từ TBM (6 tháng) → CBM (theo ΔP) → nhiều filter dùng được 9-12 tháng thay vì 6 → Tiết kiệm $20K/năm!\n• Chiller CBM: Ngăn ngừa 1 sự cố hỏng compressor ($100K!)\n• Damper FF: Phát hiện 1 damper kẹt → sửa trước khi ảnh hưởng sản phẩm\n\n→ Bài học: OEM nói thay HEPA 6 tháng → nhưng RCM dùng DATA (ΔP) → chứng minh nhiều filter vẫn tốt → THAY THEO CONDITION, không theo lịch! → Tiết kiệm mà an toàn hơn!"
        },
        {
            "title": "RCM đội xe vận tải — Mỗi xe một chiến lược!",
            "industry": "Logistics",
            "situation": "50 xe tải giao hàng. PM theo ODO (km) — mỗi 10,000 km. Nhưng: Xe chạy nội thành (30 km/h, dừng nhiều) khác xe chạy cao tốc (80 km/h, ít dừng). PM giống nhau → không hợp lý!",
            "analysis": "RCM phân LOẠI xe theo đặc điểm vận hành:\n\nXe nội thành (20 chiếc): Chạy chậm, dừng nhiều → phanh mòn NHANH. Motor chạy tải nặng (start-stop liên tục) → dầu nhớt xuống cấp nhanh\n→ PM interval NGẮN hơn: 8,000 km thay vì 10,000. Phanh: CBM (đo bề dày)\n\nXe cao tốc (30 chiếc): Chạy nhanh, ít dừng → phanh mòn chậm. Motor chạy đều → dầu nhớt ổn định hơn\n→ PM interval CÓ THỂ DÀI hơn: 12,000-15,000 km (kiểm tra bằng oil analysis)\n\nRCM cụ thể:\n• Dầu nhớt → CBM: Oil analysis → xe nào dầu còn tốt → kéo dài thay. Xe nào dầu xấu → thay sớm\n• Phanh → CBM: Đo bề dày → thay khi còn 30% (không theo km!)\n• Lốp → CBM: Đo độ mòn gai HÀNG TUẦN + TPMS (cảm biến áp suất real-time)\n• Ắc-quy → CBM: Load test 6 tháng → thay trước khi chết",
            "result": "Kết quả:\n• Oil change: Theo analysis → xe cao tốc kéo dài 10K → 15K km → tiết kiệm 30% dầu nhớt!\n• Phanh: Đo thay vì lịch → thay ĐÚNG LÚC, không sớm (lãng phí) không muộn (nguy hiểm)\n• Xe nội thành: PM DÀY hơn (8K) nhưng ĐÚNG nhu cầu → ít breakdown trên đường\n\nTổng: Chi phí PM giảm 15%. Breakdown dọc đường giảm 25%.\n→ Bài học: Cùng xe, cùng model — nhưng CÁCH SỬ DỤNG KHÁC → PM phải KHÁC!"
        }
    ]
}
