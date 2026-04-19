method = {
    "id": 1,
    "title": "Bottleneck Analysis - Phân tích nút thắt cổ chai",
    "short_name": "Bottleneck Analysis",
    "icon": "🔍",
    "pillar": "Focus Improvement",
    "description": "Xác định và loại bỏ điểm NGHẼN trong quy trình — nơi năng suất toàn bộ dây chuyền bị giới hạn bởi 1 công đoạn yếu nhất.",
    "meaning": """
<p><strong>Bottleneck Analysis (Phân tích nút thắt cổ chai)</strong> là phương pháp xác định công đoạn hoặc thiết bị có năng lực sản xuất THẤP NHẤT trong dây chuyền — từ đó giới hạn sản lượng TOÀN BỘ hệ thống.</p>
<p><em>Hình dung: Chai nước có cổ hẹp → dù thân chai rất rộng, nước chỉ chảy ra được qua cổ chai hẹp! Tương tự, dù các máy khác rất nhanh, sản lượng dây chuyền chỉ bằng máy CHẬM NHẤT.</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Nguyên lý cốt lõi</div>
    <p><strong>"Một chuỗi chỉ mạnh bằng mắt xích yếu nhất"</strong><br><br>
    <strong>Bottleneck</strong> = Bất kỳ nguồn lực nào mà năng lực ≤ nhu cầu đặt ra → Quyết định throughput (thông lượng — sản lượng đầu ra) của toàn hệ thống.<br><br>
    <strong>Ví dụ đơn giản</strong>: Trộn 60 T/h → Ép viên 40 T/h → Đóng bao 55 T/h<br>
    → Dây chuyền chỉ đạt <strong>40 T/h</strong> (= năng lực máy ép viên — bottleneck!)<br>
    → Máy trộn chạy 60 T/h nhưng 20 T/h dư ra = WIP (Work In Process — bán thành phẩm tồn đọng) → LÃNG PHÍ!<br><br>
    <strong>Quy tắc</strong>: Cải tiến BẤT KỲ máy nào KHÔNG PHẢI bottleneck → sản lượng dây chuyền KHÔNG TĂNG! Chỉ cải tiến BOTTLENECK mới tăng sản lượng!</p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định CHÍNH XÁC công đoạn/thiết bị nào đang GIỚI HẠN sản lượng toàn dây chuyền</li>
    <li>Tối ưu năng lực sản xuất tổng thể — tăng sản lượng MÀ KHÔNG CẦN mua thêm máy cho tất cả công đoạn</li>
    <li>Giảm WIP (Work In Process — bán thành phẩm tồn đọng) → giảm vốn bị "chôn" trong hàng chờ</li>
    <li>Cân bằng tải giữa các trạm — tránh máy chạy quá tải (bottleneck) trong khi máy khác chờ (starving)</li>
    <li>Ưu tiên đầu tư ĐÚNG CHỖ — chỉ nâng cấp bottleneck, không lãng phí tiền nâng cấp máy không phải bottleneck</li>
    <li>Áp dụng TOC (Theory of Constraints — Lý thuyết Ràng buộc) của Eliyahu Goldratt</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Vẽ sơ đồ dòng chảy quy trình (Process Flow)</div>
        <div class="step-card__desc">Liệt kê TẤT CẢ công đoạn từ đầu vào đến đầu ra. Ghi rõ: Tên công đoạn, thiết bị, cycle time (thời gian 1 chu kỳ), năng lực thiết kế (tấn/h hoặc sản phẩm/h). Bao gồm cả thời gian changeover (chuyển đổi sản phẩm), setup, và thời gian chờ giữa các công đoạn.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Đo lường năng lực THỰC TẾ từng công đoạn</div>
        <div class="step-card__desc">Thu thập dữ liệu THỰC TẾ (không dùng năng lực thiết kế — vì thực tế luôn thấp hơn!). Đo: Cycle time thực, uptime (thời gian chạy thực), scrap rate (tỷ lệ phế phẩm), changeover time. Tính năng lực thực = Thời gian có sẵn × Tốc độ thực × (1 - Scrap%). Đo ít nhất 1-2 tuần để có dữ liệu đại diện.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xác định BOTTLENECK</div>
        <div class="step-card__desc">So sánh năng lực thực tế của từng công đoạn → Công đoạn có năng lực THẤP NHẤT = BOTTLENECK! Dấu hiệu nhận biết bottleneck: (1) WIP đọng TRƯỚC công đoạn đó (hàng xếp đầy!). (2) Các công đoạn SAU nó bị "đói" (starving — chờ hàng). (3) Máy chạy 100% thời gian, không bao giờ rảnh. Lưu ý: Bottleneck có thể DI CHUYỂN khi điều kiện thay đổi!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Cải tiến theo TOC 5 bước (Exploit → Subordinate → Elevate)</div>
        <div class="step-card__desc"><strong>Bước TOC 1 — EXPLOIT (khai thác tối đa)</strong>: Bottleneck KHÔNG ĐƯỢC dừng — bảo trì, changeover, nghỉ trưa đều phải tối thiểu! <strong>Bước TOC 2 — SUBORDINATE (phối hợp)</strong>: Các công đoạn khác phối hợp theo nhịp của bottleneck (không chạy nhanh hơn → chỉ tạo WIP thừa!). <strong>Bước TOC 3 — ELEVATE (nâng cấp)</strong>: Nếu vẫn chưa đủ → đầu tư nâng cấp bottleneck (thêm máy, tăng tốc, giảm scrap). <strong>Bước TOC 4 — REPEAT</strong>: Sau khi nâng cấp → bottleneck có thể DI CHUYỂN sang công đoạn khác → lặp lại phân tích!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Dây chuyền TACN — Ép viên là bottleneck, tăng 26% sản lượng!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Dây chuyền 3 công đoạn: Trộn (Mixer) 60 T/h → Ép viên (Pellet Mill) 40 T/h → Đóng bao (Packer) 55 T/h. Sản lượng thực tế chỉ 38 T/h. WIP (bán thành phẩm) tồn đọng đầy giữa trộn và ép viên.",
            "analysis": "Xác định bottleneck:\n• Trộn: 60 T/h → DƯ năng lực (chờ ép viên liên tục)\n• Ép viên: 40 T/h → THẤP NHẤT = BOTTLENECK!\n• Đóng bao: 55 T/h → Cũng dư (chờ ép viên)\n\nThực tế ép viên chỉ đạt 38 T/h (không phải 40 T/h thiết kế) vì:\n• Die (khuôn ép) bị mòn → sản phẩm ép chậm hơn\n• Steam conditioning (hấp hơi) chưa đủ nhiệt → viên cám khó ép → máy phải chạy chậm\n\nDấu hiệu nhận biết: WIP (bột đã trộn) chất đầy bin chờ ÉP. Máy trộn phải dừng chờ vì bin đầy. Máy đóng bao rảnh 30% thời gian chờ viên cám.",
            "result": "Áp dụng TOC:\n• Exploit: Ép viên KHÔNG DỪNG khi nghỉ trưa (nhờ ca trực). Changeover die tối ưu bằng SMED (xem method 22) → giảm 50%\n• Subordinate: Máy trộn chạy THEO NHỊP ép viên (không chạy full 60 T/h nữa → giảm WIP)\n• Elevate: Thay die mới + tối ưu steam conditioning → ép viên tăng 38 → 48 T/h\n\nKết quả: Sản lượng dây chuyền tăng 26%! (38 → 48 T/h)\n→ Bottleneck MỚI: Đóng bao (55 T/h) giờ gần bottleneck → Tiếp tục phân tích!"
        },
        {
            "title": "SMT Line điện tử — Pick & Place gây nghẽn, tăng 60% output!",
            "industry": "Điện tử",
            "situation": "Line SMT (Surface Mount Technology — công nghệ gắn linh kiện bề mặt) có 5 trạm: In keo (Paste) 25s → Gắn linh kiện (Pick & Place) 45s → Hàn (Reflow) 30s → Kiểm tra (AOI Inspect) 25s → Test chức năng 28s. Output chỉ đạt 80 board/giờ thay vì mục tiêu 130.",
            "analysis": "Bottleneck rõ ràng: Pick & Place = 45 giây/board!\nCác trạm khác chỉ 25-30 giây → Tất cả đều CHỜM máy Pick & Place!\n\nPhân tích chi tiết tại sao Pick & Place chậm:\n• 2/8 feeder (bộ cấp linh kiện) thường xuyên bị kẹt → máy dừng chờ operator gỡ kẹt\n• Nozzle (đầu hút) bị mòn → hút linh kiện xịt (miss pick) → retry = tốn thời gian\n• Chưa tối ưu placement sequence (thứ tự đặt linh kiện) → đầu hút di chuyển quá xa giữa các component\n\nTính tác động: Mỗi giờ mất 50 board × giá trị 200K/board = 10 triệu/giờ mất sản lượng!",
            "result": "Cải tiến theo TOC:\n• Exploit: Bảo trì feeder hàng ngày (AM — Autonomous Maintenance) → giảm 90% kẹt. Thay nozzle mòn → miss pick giảm 80%\n• Exploit: Tối ưu placement program (phần mềm sắp xếp thứ tự đặt) → giảm travel distance 30%\n• Elevate: Thêm 1 máy Pick & Place song song (chia 50% linh kiện) → cycle time giảm 45s → 28s\n\nKết quả: Output tăng 60%! (80 → 130 board/giờ)\n→ Bài học: Trước khi mua máy mới (Elevate — tốn tiền), hãy Exploit trước (tối ưu với chi phí 0!)."
        },
        {
            "title": "Xử lý đơn hàng — Kiểm tra tồn kho là bottleneck hành chính!",
            "industry": "Logistics",
            "situation": "Quy trình xử lý đơn hàng: Nhận đơn (2 phút) → Kiểm tra tồn kho (8 phút) → Xuất kho (3 phút) → Đóng gói (4 phút) → Giao hàng (5 phút). Năng suất chỉ 7 đơn/giờ thay vì mục tiêu 25.",
            "analysis": "Bottleneck: Kiểm tra tồn kho = 8 phút/đơn!\nTất cả bước khác chỉ 2-5 phút.\n\nTại sao kiểm tra tồn kho lâu?\n• Phải tra cứu THỦ CÔNG trên 3 hệ thống khác nhau (Excel tồn kho + WMS + ERP)\n• Mỗi lần tra cứu phải mở 3 phần mềm, copy mã hàng, kiểm tra từng kho\n• Có khi tồn kho trên hệ thống KHÔNG KHỚP thực tế → phải gọi kho xác nhận thêm 3-5 phút\n\n→ Bottleneck NÀY KHÔNG PHẢI do NGƯỜI CHẬM mà do HỆ THỐNG CHẬM!",
            "result": "Cải tiến:\n• Exploit: Tạo 1 bảng Excel tổng hợp tồn kho (tạm thời) → giảm từ tra 3 hệ thống xuống 1 → Kiểm tra từ 8 phút xuống 4 phút\n• Elevate: Tích hợp ERP tự động kiểm tra tồn kho real-time → giảm xuống 1 phút!\n\nKết quả: Throughput tăng 3.5 lần! (7 → 25 đơn/giờ)\n→ Bài học: Bottleneck không chỉ trong NHÀ MÁY — các quy trình VĂN PHÒNG (admin, kế toán, mua hàng) cũng có bottleneck! Và thường bottleneck hành chính do HỆ THỐNG, không do con người."
        },
        {
            "title": "Phòng khám — Phòng xét nghiệm là bottleneck, BN chờ 40 phút!",
            "industry": "Y tế",
            "situation": "Lưu trình bệnh nhân: Đăng ký (3 phút) → Khám bác sĩ (15 phút) → Xét nghiệm (25 phút) → Nhận kết quả (10 phút) → Tái khám (10 phút). Bệnh nhân phàn nàn chờ xét nghiệm quá lâu — có lúc 40 phút!",
            "analysis": "Bottleneck: Phòng xét nghiệm = 25 phút/BN!\n\n• Các bước khác chỉ 3-15 phút → phòng xét nghiệm = 25 phút → hàng chờ dài!\n• Giờ cao điểm (8-10h sáng): 40 BN/giờ đến nhưng lab chỉ xử lý 2.4 BN/giờ (25 phút/BN × 1 kỹ thuật viên) → HÀNG DÀI!\n• Thời gian chờ cao điểm: 25 → 40 phút vì queue (hàng chờ) xếp chồng\n\nDấu hiệu bottleneck: Bệnh nhân NGỒI CHỒNG CHẤT trước phòng xét nghiệm. Phòng bác sĩ rảnh 30% thời gian (chờ kết quả XN). Phòng đăng ký xong nhanh nhưng BN vẫn kẹt ở XN.",
            "result": "Cải tiến:\n• Exploit: Sắp xếp xét nghiệm phổ biến (máu, nước tiểu) ra 1 line riêng (fast-track) → giảm cycle time trung bình từ 25 → 15 phút\n• Elevate: Thêm 1 kỹ thuật viên vào giờ cao điểm (8-10h) + máy xét nghiệm tự động (auto analyzer)\n• Subordinate: Bác sĩ gửi order xét nghiệm TRƯỚC KHI BN đến lab (via HIS — Hospital Information System) → lab chuẩn bị sẵn\n\nKết quả: Thời gian chờ xét nghiệm giảm 60%! Hài lòng BN tăng rõ rệt.\n→ Bài học: Bottleneck analysis áp dụng cho MỌI quy trình — không chỉ nhà máy!"
        },
        {
            "title": "Dây chuyền sữa — Máy chiết rót + changeover = bottleneck kép!",
            "industry": "Thực phẩm",
            "situation": "Tiếp nhận sữa tươi → Thanh trùng (Pasteurize) 15,000 hộp/h → Phối trộn 14,000 hộp/h → Chiết rót (Filling) 8,000 hộp/h → Đóng thùng 12,000 hộp/h. Changeover chiết rót: 45 phút/lần đổi sản phẩm, 6 lần/ngày.",
            "analysis": "Bottleneck rõ ràng: Máy chiết rót = 8,000 hộp/h!\nCác khâu khác >12,000 hộp/h → chênh lệch rất lớn!\n\nPhân tích sâu hơn — ĐÂU CHỈ TỐC ĐỘ:\n• Tốc độ máy: 8,000 hộp/h (máy cũ, 1 đầu chiết)\n• Changeover: 45 phút × 6 lần/ngày = 270 phút = 4.5 giờ MẤT/NGÀY!\n• Effective production: 24h - 4.5h changeover - 2h nghỉ/vệ sinh = chỉ 17.5 giờ\n• Output thực: 8,000 × 17.5 = 140,000 hộp/ngày\n→ Mà thanh trùng có thể cung cấp 15,000 × 20h = 300,000 hộp/ngày → DƯ GẤP ĐÔI!",
            "result": "Cải tiến 2 tầng:\n• Exploit — SMED cho changeover (xem method 22): Phân tích 45 phút changeover → 60% là external work (có thể chuẩn bị trong khi máy chạy) → Changeover: 45 → 18 phút → Tiết kiệm 162 phút/ngày!\n• Elevate — Nâng cấp máy chiết: Thay máy 2 đầu chiết → Tốc độ: 8,000 → 15,000 hộp/h\n\nKết quả: Output tăng gần GẤP ĐÔI! (140K → 260K hộp/ngày)\n→ Bài học: Bottleneck thường là TỐC ĐỘ + CHANGEOVER! Đừng chỉ nhìn tốc độ — changeover 4.5h/ngày = \"bottleneck ẩn\"!"
        },
        {
            "title": "Call Center — Thiếu agent, khách chờ 12 phút!",
            "industry": "Dịch vụ",
            "situation": "Tổng đài CSKH: IVR (menu tự động) 1 phút → Queue (xếp hàng chờ) → Agent xử lý 6 phút → Escalation (chuyển cấp cao) nếu cần → Resolution. Giờ peak: 200 cuộc/giờ, 10 agent. Khách chờ trung bình 12 phút!",
            "analysis": "Bottleneck: Số lượng Agent!\n\nTính toán capacity:\n• 10 agent × 60 phút ÷ 6 phút/cuộc = capacity 100 cuộc/giờ\n• Nhu cầu peak: 200 cuộc/giờ\n→ Capacity chỉ = 50% nhu cầu → HÀNG CHỜ DÀI!\n\nTính thời gian chờ (queueing theory):\n• Utilization = 200/100 = 200% → QUÁN TẢI!\n• Kết quả: Khách chờ 12 phút → 30% cúp máy trước khi được phục vụ (abandoned calls)\n→ Mất khách = mất doanh thu + mất uy tín!",
            "result": "Cải tiến 3 tầng:\n• Exploit (giảm thời gian xử lý): Knowledge base cho agent (tìm câu trả lời nhanh hơn) → 6 phút → 4.5 phút/cuộc → Capacity tăng 33%!\n• Subordinate (giảm nhu cầu đến bottleneck): Chatbot AI xử lý 40% câu hỏi đơn giản (tra đơn hàng, đổi mật khẩu...) → 200 cuộc giảm còn 120\n• Elevate: Thêm 5 agent part-time cho peak hours (10-12h, 14-16h)\n\nKết quả: Thời gian chờ: 12 phút → 2 phút! Abandoned calls: 30% → 5%\n→ Bài học TOC: Exploit trước (0 đồng!), rồi Subordinate (giảm tải), cuối cùng mới Elevate (tốn tiền)!"
        },
        {
            "title": "Nhà máy thép — Đúc liên tục nghẽn, changeover ladle 15 phút!",
            "industry": "Luyện kim",
            "situation": "Luyện gang → Luyện thép BOF (Basic Oxygen Furnace) cycle 40 phút → Đúc liên tục (Continuous Casting) cycle 55 phút → Cán nóng → Cán nguội. BOF chờ đúc liên tục → thép nguội trong gàu (ladle) → phải nung lại → lãng phí năng lượng!",
            "analysis": "Bottleneck: Máy đúc liên tục = 55 phút/mẻ!\nBOF chỉ 40 phút → mỗi mẻ phải CHỜM 15 phút → thép nguội → nung lại → tốn gas!\n\nPhân tích chi tiết 55 phút:\n• Đúc thực: 40 phút\n• Changeover ladle (đổi gàu thép): 15 phút! → phải dừng đúc, cẩu gàu cũ ra, đưa gàu mới vào, kết nối, bắt đầu rót\n→ 15 phút changeover = 27% tổng cycle! Đây là LÃNG PHÍ lớn\n\nTác động: Mỗi phút dừng đúc = mất 2 tấn thép × 15 triệu VND/tấn = 30 triệu/phút!",
            "result": "Cải tiến:\n• Elevate — Ladle turret (bệ quay gàu): Thay vì cẩu gàu 1 → lắp bệ quay có 2 vị trí → Trong khi đúc gàu 1, gàu 2 CHUẨN BỊ SẴN → Đổi gàu chỉ cần QUAY BỆ → Changeover: 15 phút → 3 phút!\n• Cycle time đúc: 55 → 43 phút\n\nKết quả: Năng lực đúc tăng 22%! Tiết kiệm gas nung lại + tăng sản lượng = hàng chục tỷ VND/năm.\n→ Bài học: Bottleneck thường do CHANGEOVER, không phải do tốc độ xử lý! SMED (method 22) là tool mạnh nhất cho bottleneck loại này."
        },
        {
            "title": "Quy trình tuyển dụng — Bottleneck = Lịch trống của sếp!",
            "industry": "Nhân sự",
            "situation": "Đăng tin tuyển (1 ngày) → Lọc CV (5 ngày) → Phỏng vấn vòng 1 (3 ngày) → Phỏng vấn vòng 2 (7 ngày) → Offer (2 ngày). Tổng: 18 ngày → ứng viên tốt KHÔNG CHỜ được → nhận offer công ty khác!",
            "analysis": "Bottleneck: Phỏng vấn vòng 2 = 7 NGÀY!\n\nTại sao 7 ngày?\n• Manager cấp cao chỉ RẢN vào thứ 6 cuối tuần → phỏng vấn chỉ được 1 buổi/tuần\n• Nếu ứng viên vòng 1 xong thứ 2 → phải CHỜ đến thứ 6 = 4 ngày chờ!\n• Nếu thứ 6 đã full → chờ thêm tuần sau = 11 ngày!\n\nTác động: Ứng viên giỏi có nhiều offer → chờ 7 ngày = MẤT ứng viên → tuyển lại từ đầu → TỐN THÊM thời gian và chi phí!",
            "result": "Cải tiến:\n• Exploit: Block lịch CỐ ĐỊNH 2 buổi/tuần cho phỏng vấn (không để họp khác lấn) → Giảm chờ từ 7 → 3 ngày\n• Subordinate: Vòng 1 lọc NGHIÊM hơn (chỉ gửi 2-3 ứng viên thay vì 5-6) → manager mất ít thời gian hơn\n• Elevate: Cho phép phỏng vấn ONLINE (Zoom/Teams) → manager phỏng vấn giữa 2 cuộc họp (30 phút) thay vì phải rảnh cả buổi\n\nKết quả: Tổng quy trình: 18 → 10 ngày! Tỷ lệ ứng viên chấp nhận offer tăng 40%.\n→ Bài học: Bottleneck trong quy trình hành chính thường là NGƯỜI (lịch bận) chứ không phải hệ thống!"
        },
        {
            "title": "Nhà máy xi măng — Lò nung clinker, gạch chịu lửa mòn!",
            "industry": "Vật liệu xây dựng",
            "situation": "Nghiền thô 200 T/h → Lò nung clinker 150 T/h → Nghiền tinh 180 T/h → Đóng bao 200 T/h. Dây chuyền chỉ đạt 140 T/h, không đạt mục tiêu 170 T/h.",
            "analysis": "Bottleneck: Lò nung clinker = 150 T/h (thiết kế)\nThực tế chỉ đạt 140 T/h vì:\n• Gạch chịu lửa (refractory) bị mòn tại zone nung (burning zone) → phải GIẢM tốc độ quay lò để gạch không bị bong thêm → chạy chậm 10 T/h\n• Nhiên liệu than nghiền chưa đủ mịn → cháy không hoàn toàn → nhiệt lượng thấp hơn → phải quay lò chậm hơn để clinker chín đủ\n\nLò nung là bottleneck ĐẶC BIỆT vì:\n• RẤT ĐẮT (chiếm 60% tổng đầu tư nhà máy) → không thể \"thêm 1 lò\" dễ dàng!\n• Mỗi T/h thiếu = mất ~150,000 VND/T × 24h = 3.6 triệu/giờ thiệt hại!",
            "result": "Cải tiến:\n• Exploit: Tối ưu nhiên liệu: than nghiền mịn hơn (residue 90μm giảm từ 15% xuống 8%) → cháy tốt hơn → nhiệt cao hơn → quay nhanh hơn\n• Elevate: Thay gạch chịu lửa zone nung (major overhaul) → lò chạy full speed\n• Kết hợp: Lắp camera nhiệt (thermal camera) bên trong lò → giám sát mòn gạch real-time → biết lúc nào cần thay → không chờ đến khi gạch bong!\n\nKết quả: Lò nung: 140 → 190 T/h! Tăng 36% sản lượng.\n→ Bài học: Khi bottleneck là thiết bị ĐẮT (không thể mua thêm) → Exploit là CỰC KỲ QUAN TRỌNG — tối ưu TỪNG PHẦN trăm năng suất!"
        },
        {
            "title": "Data Center — Database là bottleneck, response 900ms!",
            "industry": "CNTT",
            "situation": "Web Server (5ms) → API Gateway (10ms) → Database query (800ms!) → Cache (5ms) → Response. Tổng: 900ms. User experience: CHẬM! Google khuyến nghị < 200ms.",
            "analysis": "Bottleneck: Database query = 800ms (89% tổng thời gian!)\n\nTại sao Database chậm?\n• Query không có INDEX (chỉ mục) → Database phải full table scan (đọc TOÀN BỘ 10 triệu records để tìm 1 record!) → như đọc cả quyển từ điển để tìm 1 từ thay vì tra mục lục!\n• JOIN 5 bảng lớn → mỗi join nhân lên complexity\n• Không có READ REPLICA (bản sao đọc) → 1 database phục vụ cả READ lẫn WRITE → tranh chấp tài nguyên\n\nTác động: 800ms load time → bounce rate (tỷ lệ thoát) tăng 30% → MẤT khách hàng!",
            "result": "Cải tiến 3 tầng:\n• Exploit — Thêm INDEX: Tạo index cho cột WHERE, JOIN → query từ full scan → index lookup → 800ms → 50ms! (Chi phí: 0 đồng, chỉ 1 lệnh SQL!)\n• Exploit — Query optimization: Viết lại query, tránh SELECT *, dùng pagination → giảm thêm 30%\n• Elevate — Read Replica: Tạo 2 bản sao DB chỉ phục vụ READ → DB chính chỉ WRITE → giảm tranh chấp\n\nKết quả: Response time: 900ms → 120ms! Bounce rate giảm 25%.\n→ Bài học IT: 1 dòng INDEX có thể giải quyết bottleneck mà KHÔNG TỐN TIỀN! Exploit trước, Elevate sau!"
        }
    ]
}
