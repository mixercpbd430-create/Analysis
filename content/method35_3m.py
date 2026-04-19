method = {
    "id": 35,
    "title": "Muda-Mura-Muri (3M) Analysis - Phân tích 3 loại lãng phí",
    "short_name": "3M Analysis",
    "icon": "🗑️",
    "pillar": "Focus Improvement",
    "description": "Phân tích 3 loại bất thường trong Lean: Muda (lãng phí), Mura (không đều), Muri (quá tải) — giải quyết GỐC RỄ của lãng phí.",
    "meaning": """
<p><strong>3M</strong> là nền tảng của Lean Manufacturing, giúp nhận diện 3 dạng bất thường cần loại bỏ trong nhà máy:</p>
<ul>
    <li><strong>Muda (無駄 — Lãng phí)</strong>: Hoạt động KHÔNG tạo giá trị — khách hàng KHÔNG trả tiền cho những thứ này! Có 7+1 loại waste (gọi tắt TIMWOODS):
    <br>T = Transport (vận chuyển), I = Inventory (tồn kho), M = Motion (di chuyển thừa), W = Waiting (chờ đợi), O = Overproduction (sản xuất thừa), O = Overprocessing (gia công thừa), D = Defects (phế phẩm), S = Skills unused (lãng phí tài năng)</li>
    <li><strong>Mura (斑 — Không đều / Biến động)</strong>: Sản lượng, chất lượng, nhịp sản xuất dao động — lúc nhiều lúc ít, lúc nhanh lúc chậm. <em>Ví dụ: Đầu tháng làm 100 tấn, cuối tháng dồn 300 tấn → hỗn loạn!</em></li>
    <li><strong>Muri (無理 — Quá tải)</strong>: Máy hoặc người làm việc VƯỢT khả năng → máy hỏng, người kiệt sức, chất lượng giảm. <em>Ví dụ: Pellet mill chạy 110% công suất cuối tháng → die nứt!</em></li>
</ul>
<div class="note-box note-box--info">
    <div class="note-title">📌 Mối quan hệ nhân-quả: Mura → Muri → Muda</div>
    <p><strong>MURA (không đều) là GỐC RỄ!</strong> Khi sản xuất không đều (Mura), sẽ có lúc quá tải (Muri) → máy hỏng, người mệt → sinh ra phế phẩm, chờ đợi, sửa chữa (Muda). Và có lúc nhàn rỗi (Muda) → người chờ, máy không chạy, tồn kho.<br><br>
    <em>Ví dụ thực tế: Đơn hàng dồn cuối tháng (Mura) → nhà máy chạy overtime 12 giờ/ngày (Muri) → máy hỏng + NV mệt + lỗi tăng (Muda). Đầu tháng ít đơn → máy dừng, NV ngồi chơi (Muda). → <strong>Giải quyết Mura (san phẳng sản lượng) trước = tự động giảm Muri + Muda!</strong></em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Nhìn nhận lãng phí TOÀN DIỆN hơn — không chỉ 7 waste (Muda) mà cả Mura và Muri</li>
    <li>Tìm NGUYÊN NHÂN GỐC RỄ của lãng phí — Mura (không đều) thường là thủ phạm chính</li>
    <li>Cân bằng tải giữa con người, thiết bị, và quy trình — tránh lúc quá tải lúc nhàn rỗi</li>
    <li>Giảm biến động (Mura) = ỔN ĐỊNH quá trình = dễ quản lý, dễ dự đoán, ít bất ngờ</li>
    <li>Bảo vệ thiết bị và con người khỏi quá tải (Muri) — kéo dài tuổi thọ máy, giảm tai nạn</li>
    <li>Là NỀN TẢNG cho Lean transformation — hiểu 3M rồi mới thực hiện Lean hiệu quả</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Đi hiện trường (Gemba Walk) với checklist 3M</div>
        <div class="step-card__desc">Đi khắp nhà máy quan sát với 3 câu hỏi: ① MUDA: Ở đâu có hoạt động KHÔNG tạo giá trị? (chờ đợi, di chuyển thừa, tồn kho...) ② MURA: Ở đâu có sự KHÔNG ĐỀU? (sản lượng dao động, chất lượng lúc tốt lúc xấu, nhịp sản xuất lúc nhanh lúc chậm...) ③ MURI: Ở đâu đang QUÁ TẢI? (máy chạy vượt công suất, người OT quá nhiều, dây chuyền chạy tốc độ vượt thiết kế...)</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Phân loại, đo lường và đánh giá</div>
        <div class="step-card__desc">MUDA: Phân loại theo TIMWOODS (8 loại waste), ước tính thời gian/chi phí mỗi loại. MURA: Đo biến động bằng số liệu — CV% (hệ số biến thiên), range (giá trị lớn nhất - nhỏ nhất), pattern (chu kỳ theo ngày/tuần/tháng). MURI: Đánh giá tải so với khả năng — Utilization > 85% = có rủi ro Muri. Overtime > 20 giờ/tháng = Muri con người.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Phân tích mối quan hệ nhân-quả</div>
        <div class="step-card__desc">Vẽ sơ đồ: MURA nào đang GÂY RA Muri và Muda? Ví dụ: Đơn hàng không đều (Mura) → Nhà máy lúc dồn OT (Muri) → Máy hỏng + lỗi tăng (Muda) → ƯU TIÊN giải quyết Mura! Dùng dữ liệu để ĐỊNH LƯỢNG tác động: Mura gây thiệt hại bao nhiêu VND?</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Đối sách — San phẳng và cân bằng</div>
        <div class="step-card__desc">Giảm MURA: Heijunka (san phẳng sản lượng — sản xuất đều mỗi ngày thay vì dồn cuối tháng). Standardized work (công việc chuẩn hóa — mọi người làm như nhau, giảm biến động). Giảm MURI: Capacity planning (lập kế hoạch công suất — cân bằng tải vs khả năng). Tự động hóa, chia sẻ công việc. Giảm MUDA: Kaizen từng loại waste (xem method 34).</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "3M tại line ép viên TACN — Cuối tháng hỗn loạn!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Ca ngày sản xuất 180 tấn, ca đêm chỉ 120 tấn. Cuối tháng OT weekend liên tục. Breakdown tăng đột biến vào cuối tháng. Đầu tháng máy dừng chờ đơn hàng.",
            "analysis": "MURA (không đều — GỐC RỄ!):\n• Đơn hàng cuối tháng gấp 2 lần đầu tháng! Kinh doanh dồn đơn cuối tháng vì KPI theo tháng\n• Ca ngày SX 180T, ca đêm 120T → chênh lệch 50% giữa 2 ca → có ca quá tải, ca thiếu tải\n\nMURI (quá tải — HẬU QUẢ của Mura):\n• Cuối tháng: Pellet mill chạy 110% công suất → die nứt (quá tải cơ khí), motor overload trip\n• NV OT 12 giờ/ngày cuối tháng → mệt mỏi → thao tác sai → lỗi chất lượng tăng 40%\n\nMUDA (lãng phí — HẬU QUẢ của Muri):\n• Đầu tháng: Máy idle 30% (không có đơn) → NV ngồi chơi, NL tồn kho cao\n• Breakdown cuối tháng → dừng máy chờ sửa (waiting waste)\n• Phế phẩm tăng cuối tháng (defect waste)",
            "result": "Giải quyết MURA trước!\n• Heijunka (san phẳng sản lượng): Lập kế hoạch SX theo TUẦN thay vì theo đơn hàng. Chia đều sản lượng mỗi ngày, không dồn cuối tháng\n• Safety stock thành phẩm 3 ngày: SX trước vào kho đệm → khi KD cần → xuất từ kho → không cần dồn SX cuối tháng\n• Takt time planning: Tính nhịp SX theo nhu cầu → tránh chạy quá tải hoặc nhàn rỗi\n\nKết quả: OT giảm 60%, breakdown giảm 40%, sản lượng đều mỗi ngày!"
        },
        {
            "title": "8 Wastes (TIMWOODS) — Phát hiện 8 loại lãng phí nhà máy TACN",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Quản lý nhà máy muốn audit toàn bộ lãng phí. Tổ chức Gemba Walk với checklist TIMWOODS — 8 loại waste.",
            "analysis": "Kết quả audit 8 waste:\n• T — Transport (Vận chuyển): NL di chuyển 500m từ kho → SX (kho xa, không có conveyor)\n• I — Inventory (Tồn kho): WIP (bán thành phẩm chờ) 2 ngày giữa trộn → ép viên → đọng vốn\n• M — Motion (Di chuyển thừa): Operator đi lại lấy bao rỗng 15 lần/giờ vì bao để xa máy đóng bao\n• W — Waiting (Chờ đợi): Chờ QC phát kết quả lab 30 phút/batch → máy dừng chờ!\n• O — Overproduction (SX thừa): SX thêm 5% \"dự phòng\" cho mỗi đơn hàng → tồn kho thừa\n• O — Overprocessing (Gia công thừa): Nghiền quá mịn so với yêu cầu → tốn điện vô ích (screen sai kích thước!)\n• D — Defects (Phế phẩm): 3% reject rate → NL bỏ đi hoặc tái chế tốn năng lượng\n• S — Skills unused (Lãng phí tài năng): Operator giỏi chỉ vận hành máy, không được giao bảo trì cơ bản (AM) → tài năng bị lãng phí",
            "result": "Ưu tiên TOP 3 waste có impact lớn nhất:\n• Waiting (chờ QC): QC inline — kiểm tra ngay trên dây chuyền thay vì gửi lab → giảm 30 phút chờ/batch!\n• Motion (đi lấy bao): Đặt pallet bao rỗng NGAY CẠ machine đóng bao (point-of-use) → 15 lần đi lại → 0 lần\n• Overprocessing (nghiền thừa): Thay screen size từ Ø2.0mm lên Ø3.0mm cho sản phẩm heo → đủ mịn, tiết kiệm 15% điện nghiền\n→ Top 3 waste giảm 60%! Chi phí cải tiến gần bằng 0."
        },
        {
            "title": "3M dây chuyền may — Line balance 65%!",
            "industry": "Dệt may",
            "situation": "Chuyền may áo polo: Line balance (cân bằng chuyền) chỉ 65%. Một số trạm quá tải (NV làm không kịp), một số trạm nhàn rỗi (NV ngồi chờ hàng). Output thấp hơn khả năng 35%.",
            "analysis": "MURA (Không đều):\n• Takt time (nhịp SX yêu cầu): 45 giây/chiếc\n• Nhưng cycle time (thời gian mỗi trạm) dao động từ 30 đến 70 giây!\n• Trạm nhanh nhất: 30 giây (đính nút) → xong trước → chờ 15 giây mỗi chu kỳ\n• Trạm chậm nhất: 70 giây (ráp cổ áo) → bottleneck → toàn chuyền chờ!\n\nMURI (Quá tải):\n• NV trạm cổ áo: Cycle time 70 giây nhưng takt 45 giây → QUAK TẢI 155%! → phải tăng ca, đau cổ tay, stress\n\nMUDA (Lãng phí):\n• NV trạm đính nút: Chờ 15 giây mỗi chu kỳ (waiting waste) = 33% thời gian ngồi chờ!",
            "result": "Giải quyết MURA — Cân bằng lại chuyền (line rebalancing):\n• Chia trạm cổ áo thành 2: 70 giây ÷ 2 = 35 giây/trạm (dưới takt 45 giây → không còn quá tải!)\n• Gộp trạm đính nút (30 giây) với công đoạn nhỏ khác (15 giây) = 45 giây → vừa takt, không còn chờ!\n• Tất cả trạm đều dao động 40-48 giây → gần takt 45 giây\n\nKết quả:\n• Line balance: 65% → 88%!\n• Output tăng 35% VỚI CÙNG số nhân lực!\n• NV trạm cổ áo hết quá tải → giảm chấn thương tay"
        },
        {
            "title": "3M trong bảo trì — KTV lúc rảnh lúc quá bận!",
            "industry": "Sản xuất chung",
            "situation": "Kỹ thuật viên (KTV) bảo trì: Lúc quá bận (breakdown hàng loạt, chạy khắp nơi) → OT 30 giờ/tháng, stress cao. Lúc rảnh rỗi (không có việc). Hiệu quả bảo trì thấp dù OT cao.",
            "analysis": "MURA (Không đều):\n• PM (Planned Maintenance — bảo trì kế hoạch) dồn cuối tháng (vì đầu tháng \"chưa đến hạn\")\n• Breakdown xảy ra ngẫu nhiên → peak workload bất ngờ → lúc 5 máy hỏng cùng lúc, lúc 0 máy hỏng\n\nMURI (Quá tải):\n• 1 KTV phụ trách 50 máy trong reactive mode (chờ hỏng mới sửa) → không kịp xoay xở khi nhiều máy hỏng cùng lúc\n• OT 30 giờ/tháng → mệt mỏi → sai sót khi sửa → hỏng lại → vòng luẩn quẩn!\n\nMUDA (Lãng phí):\n• Chờ phụ tùng: 35% thời gian sửa chữa! → KTV xuống kho, tìm phụ tùng, giấy tờ xuất kho...\n• Di chuyển: KTV chạy 500m mỗi lần từ kho phụ tùng đến máy rồi quay lại (motion waste)",
            "result": "Giải quyết:\n• PM leveling (san phẳng PM): Phân bổ ĐỀU PM theo TUẦN thay vì dồn cuối tháng → KTV có việc đều, không lúc rỗi lúc bận\n• Zone-based maintenance: Mỗi KTV phụ trách 1 KHU VỰC (thay vì \"ai rảnh sửa\") → di chuyển ngắn, quen máy → sửa nhanh hơn\n• Spare parts kanban: Phụ tùng phổ biến để TẠI KHU VỰC (không xuống kho) → giảm 35% thời gian chờ\n• Predictive maintenance: Giám sát rung + nhiệt → phát hiện sắp hỏng → lên lịch sửa → KHÔNG CÒN breakdown bất ngờ\n\nKết quả: OT giảm 70%! Hiệu quả bảo trì tăng vì KTV không còn chạy khắp nơi."
        },
        {
            "title": "3M vận tải — Xe lúc thiếu lúc thừa!",
            "industry": "Logistics",
            "situation": "Đội xe 20 chiếc: Mùa cao điểm không đủ xe → thuê ngoài đắt. Mùa thấp điểm xe đậu bãi 30% → tốn chi phí bảo hiểm, bảo dưỡng. Fuel cost cao vì xe chạy rỗng (empty return trip) 40%.",
            "analysis": "MURA: Nhu cầu vận chuyển mùa peak gấp 2 lần off-peak (theo mùa vụ nông nghiệp). Tuyến đường không tối ưu → nhiều xe chạy cùng khu vực\n\nMURI: Peak: Xe chạy 14 giờ/ngày (quá tải!), tài xế mệt → rủi ro tai nạn. Lốp mòn nhanh hơn 50% vào mùa cao điểm\n\nMUDA: Off-peak: 30% xe nằm bãi (idle waste). Empty return trips (xe chở hàng đi → chạy rỗng về) = 40% quãng đường! → tốn fuel vô ích",
            "result": "Giải quyết:\n• Fleet right-sizing + thuê mùa vụ: Giữ 15 xe (đủ cho off-peak), thuê thêm 5 xe vào peak → không thừa xe off-peak\n• Route optimization (tối ưu tuyến đường): Gộp đơn hàng cùng khu vực vào 1 xe → giảm số lượt chạy\n• Backhaul matching: Xe giao hàng xong → NHẬN hàng trả về (thay vì chạy rỗng). Ví dụ: Giao TACN đi → Chở bắp/đậu nành về → empty trip giảm 60%\n• Driver rotation: Không để 1 tài xế chạy 14 giờ liên tục → chia ca\n\nUtilization tăng 25%, fuel giảm 15%!"
        },
        {
            "title": "3M analysis nhân sự nhà máy — Supervisor burnout!",
            "industry": "Sản xuất chung",
            "situation": "Turnover (tỷ lệ nghỉ việc) 25%/năm — rất cao! OT cao nhưng tinh thần (morale) thấp. Khoảng cách kỹ năng (skills gap) lớn giữa NV mới và NV cũ.",
            "analysis": "MURA (Không đều giữa các bộ phận):\n• Sản xuất: Utilization 150% (quá tải)\n• QC: Utilization 70% (nhàn rỗi)\n• Bảo trì: Reactive mode (lúc rỗi lúc bận)\n→ Có phòng quá bận, có phòng quá rỗi — mất cân bằng!\n\nMURI (Quá tải con người):\n• Supervisor SX: 12 NV trực tiếp + quản lý hành chính + xử lý sự cố + OT = BURNOUT!\n• 45% supervisor nghỉ việc trong năm đầu! → thay supervisor liên tục → NV mất phương hướng\n\nMUDA (Lãng phí nhân lực):\n• Training không follow-up: 50% NV quên kiến thức sau 2 tuần đào tạo! (training waste)\n• Meeting không có agenda → kéo dài → không có action vụ thể",
            "result": "Giải quyết:\n• Span of control (tầm kiểm soát): Tối đa 8 NV trực tiếp cho 1 supervisor (thay vì 12) → giảm quá tải\n• Tự động hóa hành chính: Báo cáo tự động trên dashboard → supervisor không phải ngồi viết Excel\n• Cross-training matrix: Đào tạo chéo NV QC hỗ trợ SX khi peak, NV SX hỗ trợ QC khi rỗi → cân bằng tải\n• OJT có kiểm tra (structured OJT): Đào tạo + kiểm tra định kỳ → đảm bảo NV nhớ và áp dụng\n• Quy tắc họp: Có agenda + người giữ thời gian + biên bản → ngắn gọn, hiệu quả\n\nTurnover supervisor giảm 50%!"
        },
        {
            "title": "3M trong chuỗi cung ứng — Bullwhip Effect!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Hiệu ứng Bullwhip (hiệu ứng roi da — đơn hàng khuếch đại khi truyền ngược lên chuỗi cung ứng): Khách hàng đặt hàng dao động ±20%, nhà máy SX dao động ±30%, nhà cung cấp nhận đơn dao động ±50%! NCC không thể lập kế hoạch → giá cao, giao trễ.",
            "analysis": "MURA: Đơn hàng từ khách dao động ±20%. Nhà máy phóng đại biến động khi đặt NL ±50% (lo sợ thiếu → đặt nhiều, thừa → dừng đặt → NCC loạng choạng!)\n\nMURI: NCC quá tải khi nhận big order → không đảm bảo quality. Logistics (xe tải, kho) bị ép → tăng giá\n\nMUDA: Safety stock (tồn kho an toàn) phóng đại ở MỖI tầng: NL dự trữ 3 THÁNG! → đọng vốn hàng tỷ đồng",
            "result": "Giải quyết Mura — Giảm khuếch đại Bullwhip:\n• Chia sẻ dự báo với NCC (CPFR — Collaborative Planning, Forecasting, and Replenishment): NCC biết trước nhu cầu → không bị bất ngờ → lập kế hoạch SX ổn định\n• Lịch đặt hàng cố định ± 10%: Cam kết với NCC đơn hàng tháng, cho phép thay đổi ±10% — NCC yên tâm lập kế hoạch\n• VMI (Vendor Managed Inventory) cho top 5 NL: NCC tự quản lý tồn kho tại nhà máy → họ giao đúng lúc, đúng lượng\n• Safety stock giảm từ 3 tháng xuống 3 tuần!\n\nBullwhip giảm 60%! NCC giao đúng hẹn, đúng chất lượng."
        },
        {
            "title": "3M văn phòng — Cuối tháng deadline dồn!",
            "industry": "Đa ngành",
            "situation": "Phòng Marketing: Deadline báo cáo dồn cuối tháng. OT cao, chất lượng báo cáo giảm. Nhân viên stress, nghỉ việc nhiều.",
            "analysis": "MURA: 80% báo cáo tập trung cuối tháng (vì deadline cuối tháng!). Lịch họp không đều: Thứ 2 full meetings, thứ 6 trống → Thứ 2 không làm được việc gì!\n\nMURI: NV cuối tháng OT 20 giờ → mệt mỏi → lỗi tăng (sai số liệu, copy-paste nhầm). Multi-tasking quá mức: 1 NV làm 5 báo cáo cùng lúc → không cái nào tốt!\n\nMUDA: Check email 2 giờ/ngày → ngắt quãng liên tục, không tập trung. Nhập dữ liệu vào 3 hệ thống khác nhau (duplicate reporting) → tốn thời gian vô ích",
            "result": "Giải quyết:\n• Weekly reporting thay monthly: Chia deadline từ 1 lần/tháng → 4 lần/tháng → mỗi tuần làm 1 phần nhỏ = không dồn cuối tháng\n• Meeting-free afternoons: Buổi chiều không họp → NV có thời gian tập trung viết báo cáo\n• Dashboard tự động thay Excel: Power BI/Google Data Studio → dữ liệu tự cập nhật → KHÔNG CẦN viết báo cáo thủ công!\n• Single source of truth: 1 hệ thống duy nhất thay vì 3 → giảm duplicate\n\nOT giảm 80%! Chất lượng báo cáo tăng. NV hạnh phúc hơn."
        },
        {
            "title": "3M quy trình bán hàng — Hockey Stick Effect!",
            "industry": "Đa ngành",
            "situation": "Đội Sales: Doanh số cuối quý luôn gấp 2.5 lần đầu quý (\"đường cong hockey stick\" — phẳng 2 tháng đầu, vọt lên tháng cuối). Cuối quý chạy target điên cuồng.",
            "analysis": "MURA: Revenue 50% đến trong tháng cuối quý, chỉ 20% tháng đầu quý (hockey stick pattern). Tại sao? Vì KPI theo quý → 2 tháng đầu thư giãn, tháng cuối chạy dồn!\n\nMURI: Cuối quý: Discount mạnh để chốt đơn (phá giá!), giao hàng gấp → logistics OT → vận chuyển quá tải. Nhập đơn hàng vội → sai thông tin (sai địa chỉ, sai sản phẩm, sai số lượng) → phải sửa → mất thêm thời gian\n\nMUDA: Đầu quý: Sales team nhàn, pipeline (đơn hàng tiềm năng) không đủ. Demo equipment (thiết bị trưng bày) nằm kho không dùng. SX phải tăng gấp đôi cuối quý → OT, lỗi tăng",
            "result": "Giải quyết:\n• Monthly quota thay quarterly: KPI theo THÁNG → buộc doanh số đều mỗi tháng, không dồn cuối quý\n• Pipeline management weekly: Review pipeline hàng tuần → đảm bảo luôn có đủ đơn hàng tiềm năng\n• Incentive cho early-month orders: Thưởng thêm nếu chốt đơn trong 2 tuần đầu tháng → san phẳng doanh số\n\n→ Demand smoothing (nhu cầu đều) → supply chain stability (chuỗi cung ứng ổn định) → SX không dồn, logistics không quá tải!"
        },
        {
            "title": "3M line đóng gói thực phẩm — Minor stops liên tục!",
            "industry": "Thực phẩm",
            "situation": "Line đóng gói thực phẩm: Dừng ngắn (minor stops) liên tục, tốc độ thay đổi liên miên, label sai phải dừng máy thay. OEE thấp.",
            "analysis": "MURA: SKU mix thay đổi mỗi giờ (lô rất nhỏ → changeover liên tục). Film tension (lực kéo cuộn phim bao) dao động → film rách. Trọng lượng sản phẩm biến động → máy overweight/underweight → dừng chỉnh\n\nMURI: Máy chạy tốc độ MAX cho mọi loại bao (kể cả bao nhỏ khó đóng) → kẹt nhiều hơn. Operator phải xử lý quá nhiều việc cùng lúc: thay film + chỉnh label + kiểm tra trọng lượng\n\nMUDA: Minor stops 15% (film rách, label lệch). Changeover 8 lần/ca (mỗi lần 15 phút) = 2 giờ mất/ca!",
            "result": "Giải quyết:\n• SKU sequencing: Xếp lịch SX nhóm cùng SIZE + cùng loại bao liền nhau → giảm changeover (từ 8 lần xuống 4 lần/ca)\n• Speed recipe per SKU: Mỗi loại sản phẩm có TỐC ĐỘ RIÊNG (không chạy max cho tất cả!) → bao nhỏ chạy chậm hơn = ít kẹt\n• Film tension auto-control: Lắp bộ điều khiển lực kéo tự động → film hết rách\n• SMED changeover (xem method 22/34)\n→ Minor stops giảm 70%! OEE tăng 15%."
        },
        {
            "title": "3M trong xây dựng — Trễ 3 tháng, OT cao!",
            "industry": "Xây dựng",
            "situation": "Dự án xây dựng trễ 3 tháng so với kế hoạch. OT cao nhưng năng suất thấp. Vật tư đến không đúng lúc. Thợ hàn mệt mỏi, lỗi hàn tăng.",
            "analysis": "MURA: Vật tư đến KHÔNG ĐÚNG trình tự (sắt đến trước coffa → sắt nằm chờ → rỉ sét!). Lịch thi công thay đổi 3 lần/tuần → không ai biết hôm nay làm gì!\n\nMURI: Thợ hàn làm 12 giờ/ngày, 7 ngày/tuần liên tục → mệt → tỷ lệ X-ray fail (hàn lỗi) tăng từ 3% lên 8%! → phải cắt mối hàn, hàn lại → THÊM TRỄ!\n\nMUDA: Chờ cẩu: 40 phút/lần (1 cẩu phục vụ 3 khu vực). Rework hàn 8% → tốn thêm NVL + nhân công. Đi lại lấy vật tư 500m (kho tạm quá xa)",
            "result": "Giải quyết:\n• Look-ahead planning 3 tuần: Lập kế hoạch chi tiết 3 tuần tới → vật tư đặt ĐÚNG lúc, ĐÚNG trình tự\n• Material delivery aligned to sequence: Sắt + coffa giao CÙNG NGÀY (không trước không sau)\n• Giới hạn 10 giờ/ngày: OT tối đa 10 giờ (không 12 giờ) → thợ tỉnh táo → X-ray fail về 3% → GIẢM REWORK = NHANH HƠN dù làm ít giờ hơn!\n• Crane scheduling board: Bảng lịch cẩu → đặt lịch trước → không phải chờ\n→ Bài học: Làm NHIỀU GIỜ hơn ≠ Nhanh hơn. Làm ĐỀU + không quá tải = Nhanh hơn!"
        }
    ]
}
