method = {
    "id": 3,
    "title": "C-E Analysis - Phân tích Nguyên nhân & Kết quả",
    "short_name": "C-E Analysis",
    "icon": "🐟",
    "pillar": "Focus Improvement",
    "description": "Biểu đồ xương cá Ishikawa — liệt kê MỌI nguyên nhân tiềm ẩn theo 6M, không bỏ sót, không thiên vị.",
    "meaning": """
<p><strong>C-E Analysis (Cause-Effect Analysis — Phân tích Nguyên nhân & Kết quả)</strong> sử dụng biểu đồ <strong>Ishikawa</strong> (biểu đồ xương cá — Fishbone Diagram) để HỆ THỐNG HÓA mọi nguyên nhân tiềm ẩn gây ra vấn đề.</p>
<p><em>Hình dung: Vấn đề là "đầu cá" (bên phải). Các xương lớn là 6 nhóm nguyên nhân (6M). Mỗi xương lớn có nhiều xương nhỏ (nguyên nhân chi tiết). Nhìn tổng thể → thấy TOÀN BỘ nguyên nhân có thể có!</em></p>
<p>Được phát minh bởi <em>Kaoru Ishikawa</em> năm 1968 — là 1 trong 7 công cụ chất lượng cơ bản (7 QC Tools).</p>
<div class="note-box note-box--info">
    <div class="note-title">📌 6M — 6 nhóm nguyên nhân</div>
    <p><strong>Man (Con người)</strong>: Kỹ năng? Kinh nghiệm? Đào tạo? Thái độ? Sức khỏe? Tuân thủ SOP?<br>
    <strong>Machine (Máy móc)</strong>: Mòn? Cũ? Cài đặt sai? Thiếu PM? Không hiệu chuẩn?<br>
    <strong>Material (Nguyên vật liệu)</strong>: NL kém? Sai spec? Lô mới khác lô cũ? NCC thay đổi?<br>
    <strong>Method (Phương pháp)</strong>: SOP sai? Quy trình thiếu bước? Không cập nhật? Recipe lỗi?<br>
    <strong>Measurement (Đo lường)</strong>: Thiết bị đo sai? Không hiệu chuẩn? Đo thiếu? Đo sai cách?<br>
    <strong>Mother Nature (Môi trường)</strong>: Nhiệt độ? Độ ẩm? Bụi? Ánh sáng? Mùa? Thời tiết?<br><br>
    <em>Trong ngành dịch vụ, có thể dùng 5P thay 6M: <strong>People, Process, Place, Product, Policy.</strong></em></p>
</div>
""",
    "purpose": """
<ul>
    <li>HỆ THỐNG HÓA tất cả nguyên nhân tiềm ẩn → tránh bỏ sót (nhất là nguyên nhân ít ai nghĩ đến!)</li>
    <li>BRAINSTORM nhóm có CẤU TRÚC — thay vì ai nấy nói lung tung → phân theo 6M → có trật tự</li>
    <li>Tránh KẾT LUẬN VỘI — không nhảy thẳng vào "giải pháp" mà chưa xem xét đầy đủ nguyên nhân</li>
    <li>TRỰC QUAN HÓA mối quan hệ nhân-quả → mọi người cùng nhìn → cùng hiểu → cùng đồng thuận</li>
    <li>Làm cơ sở để xác định ROOT CAUSE (nguyên nhân gốc) — sau đó dùng Why-Why (method 18) cho root cause</li>
    <li>Tạo TÀI LIỆU kiến thức tổ chức — khi vấn đề tương tự xảy ra → mở fishbone cũ ra xem!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định VẤN ĐỀ (Effect — "Đầu cá")</div>
        <div class="step-card__desc">Viết RÕ RÀNG vấn đề ở đầu cá (bên phải sơ đồ). Phải CỤ THỂ: Không viết "Chất lượng kém" (quá chung) mà viết "PDI viên cám giảm từ 95% xuống 89% kể từ tuần 12". Dùng dữ liệu: Bao nhiêu? Khi nào? Ở đâu? Tần suất?</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Vẽ 6 nhánh chính (6M)</div>
        <div class="step-card__desc">Vẽ xương sống (mũi tên lớn → đầu cá). Trên xương sống vẽ 6 xương lớn = 6M: Man, Machine, Material, Method, Measurement, Mother Nature. Mỗi nhánh là 1 "nhóm nghi phạm" — phải xét tất cả 6 nhóm, KHÔNG ĐƯỢC BỎ QUA nhóm nào!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: BRAINSTORM — liệt kê mọi nguyên nhân</div>
        <div class="step-card__desc">Với MỖI nhánh 6M, hỏi: "Yếu tố nào trong nhóm này có thể GÂY RA vấn đề?" → Viết lên xương nhỏ. Quy tắc brainstorm: KHÔNG PHÊ PHÁN → ghi TẤT CẢ ý tưởng. Mời NHIỀU bộ phận tham gia (SX, BT, QC, NL...) vì mỗi người thấy góc khác. Hỏi thêm: "Có gì THAY ĐỔI gần đây không?" → thay đổi = nghi ngờ số 1!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Đánh giá, chọn TOP nguyên nhân → Kiểm chứng</div>
        <div class="step-card__desc">Từ danh sách nguyên nhân, đánh giá: Có DỮ LIỆU ủng hộ không? Có THAY ĐỔI gần đây không? Có tương quan với vấn đề không? Chấm điểm hoặc bỏ phiếu → Chọn TOP 3-5 nguyên nhân "most likely" (có khả năng cao nhất). KIỂM CHỨNG bằng dữ liệu/thí nghiệm → xác nhận root cause → đề xuất countermeasure.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "PDI viên cám giảm — Xương cá tìm ra die ngược + steam sai!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "PDI (Pellet Durability Index — độ bền viên cám) giảm từ 95% xuống 89% kể từ tuần 12. QC phàn nàn, khách hàng trả hàng. Ai cũng có ý kiến khác nhau nhưng không ai có bằng chứng!",
            "analysis": "Họp brainstorm 6M với SX, BT, QC, mua hàng (5 người, 60 phút):\n\nMan (Con người): ✗ Vận hành không điều chỉnh steam khi NL thay đổi. ✗ Ca B PDI thấp hơn Ca A (kinh nghiệm khác nhau?)\nMachine (Máy): ✗ Die mới thay tuần 11 (1 tuần trước khi PDI giảm!). ✗ Roller gap chưa điều chỉnh sau thay die. ✗ Steam valve có thể bị rò\nMaterial (NL): ✗ Đổi NCC bắp tuần 10 (gần thời điểm vấn đề!). ✗ Độ ẩm NL thấp hơn bình thường\nMethod: ✗ Không có SOP kiểm tra die sau lắp. ✗ Không có tiêu chuẩn steam temperature\nMeasurement: ✗ Thiết bị đo PDI (durability tester) chưa hiệu chuẩn 6 tháng!\nEnvironment: ✗ Mùa khô → NL khô hơn bình thường\n\nĐánh giá TOP 3: (1) Die mới — timing trùng khớp! (2) NCC bắp mới (3) Steam chưa điều chỉnh",
            "result": "Kiểm chứng TOP 3:\n• Die: Kiểm tra → PHÁT HIỆN die lắp NGƯỢC CHIỀU! (Gap 0.8mm thay vì 0.3mm) → ĐÂY LÀ ROOT CAUSE #1!\n• NCC bắp: So sánh lab → độ ẩm thấp hơn 1% → góp phần nhưng KHÔNG phải nguyên nhân chính\n• Steam: Kiểm tra → nhiệt độ conditioning đúng spec → LOẠI TRỪ\n\nAction: Lắp lại die đúng chiều + điều chỉnh gap 0.3mm → PDI tăng ngay 95.5%!\nThêm: Hiệu chuẩn PDI tester + SOP kiểm tra die sau lắp + IQC cho NCC bắp mới\n\n→ Bài học C-E: Nếu KHÔNG vẽ fishbone → chỉ cãi nhau \"do NL!\" vs \"do máy!\" → C-E buộc mọi người XÉT TẤT CẢ 6M một cách công bằng → tìm ra die ngược mà không ai nghĩ đến!"
        },
        {
            "title": "Sản phẩm nhựa bị flash (ba via) 12% — Khuôn + áp suất!",
            "industry": "Nhựa",
            "situation": "Sản phẩm nhựa bị flash (ba via — nhựa tràn ra ngoài mặt phân khuôn) chiếm 12% sản lượng → phải cắt bỏ thủ công hoặc vứt!",
            "analysis": "Fishbone 6M cho vấn đề FLASH:\n\nMachine:\n✗ Lực kẹp khuôn (clamping force) KHÔNG ĐỦ — nhựa ép mở khuôn ra → chảy tràn\n✗ Mặt phân khuôn (parting line) bị mòn — không kín → nhựa lọt qua khe\n✗ Toggle mechanism (cơ cấu khuỷu) mòn → kẹp yếu\n\nMethod:\n✗ Áp suất phun (injection pressure) QUÁ CAO — nhựa bị ép ra ngoài khuôn\n✗ Holding time (thời gian giữ áp) quá dài\n\nMaterial:\n✗ Độ nhớt nhựa batch mới THẤP HƠN (chảy lỏng hơn → dễ tràn hơn)\n\nMan:\n✗ Operator không kiểm tra bề mặt khuôn đầu ca\n✗ Operator tăng áp suất vì sản phẩm short shot (thiếu nhựa) → quá tay → flash!\n\nTOP 3: (1) Mặt phân khuôn mòn (2) Áp suất phun cao (3) Nhựa batch mới",
            "result": "Kiểm chứng:\n• Mặt phân khuôn: Đo bằng filler gauge → khe hở 0.08mm (spec CONFIRMED! Đây là ROOT CAUSE #1\n• Áp suất: Review log → operator đã tăng áp từ 80 → 100 bar (để bù short shot do nhựa batch mới) → ROOT CAUSE #2\n• Nhựa: So sánh MFI (Melt Flow Index — chỉ số chảy) → batch mới MFI cao hơn 15% → nguyên nhân gián tiếp\n\nAction:\n• Sửa (polish) mặt phân khuôn → khe Flash: 12% → 2%!\n→ Bài học: C-E giúp thấy rằng flash KHÔNG CHỈ do 1 nguyên nhân → Machine + Method + Material PHỐI HỢP gây ra!"
        },
        {
            "title": "Giao hàng trễ 25% — GPS + Route planning giải quyết!",
            "industry": "Logistics",
            "situation": "25% đơn hàng giao trễ so với cam kết. Khách hàng phàn nàn, đe dọa chuyển sang đối thủ. Tổng giám đốc yêu cầu phân tích!",
            "analysis": "Fishbone C-E cho \"Giao hàng trễ 25%\":\n\nMan:\n✗ Dispatcher (điều phối) thiếu kinh nghiệm → phân bổ đơn không tối ưu\n✗ Tài xế không quen đường → đi lạc, đi vòng\n\nMethod:\n✗ Route planning (lập kế hoạch tuyến đường) THỦ CÔNG → tốn thời gian, không tối ưu\n✗ Không có tiêu chuẩn thời gian giao cho từng khu vực\n\nMachine:\n✗ Xe tải cũ hay hỏng dọc đường → trễ + mất thời gian sửa\n✗ GPS chưa lắp → không biết xe ở đâu\n\nMeasurement:\n✗ Không tracking real-time → không biết xe trễ cho đến khi khách gọi phàn nàn!\n✗ Không có dữ liệu thời gian giao thực tế → không benchmark\n\nMaterial:\n✗ Hàng đóng gói không chuẩn → phải xếp lại trên xe → mất thời gian\n\nTOP 3: (1) Route planning thủ công (2) Không tracking (3) Xe cũ hay hỏng",
            "result": "Action plan theo Pareto tác động:\n\nPriority 1 — Route + Tracking:\n• Triển khai GPS tracking → biết REAL-TIME xe ở đâu → chủ động xử lý khi trễ\n• Route optimization software → Phần mềm tự tối ưu lộ trình (giảm km, giảm thời gian)\n→ Giao trễ giảm ngay 50% (từ 25% → 12%)\n\nPriority 2 — Xe cũ:\n• PM (bảo trì kế hoạch) cho xe theo mileage → giảm breakdown dọc đường\n→ Giao trễ do xe hỏng: 8% → 2%\n\nTổng: Giao trễ: 25% → 5%! On-time delivery 95%!\n→ Bài học: C-E giúp thấy trễ hàng KHÔNG CHỈ do tài xế (Man) → Method (quy trình điều phối) và Machine (xe) đóng vai trò lớn hơn!"
        },
        {
            "title": "Shelf life sữa giảm từ 12 → 7 ngày — CIP + Seal!",
            "industry": "Thực phẩm",
            "situation": "Sữa tươi thanh trùng: Hạn sử dụng (shelf life) giảm từ 12 ngày xuống 7 ngày → sản phẩm bị chua sớm → khách hàng trả hàng → thiệt hại hàng trăm triệu!",
            "analysis": "Fishbone C-E cho \"Shelf life giảm 12 → 7 ngày\":\n\nMachine:\n✗ Seal (mối hàn) máy chiết rót KHÔNG KÍN → vi khuẩn xâm nhập sau chiết\n✗ Máy chiết rót gasket (gioăng) mòn → rò rỉ nhỏ\n\nMaterial:\n✗ Sữa tươi nhập có TPC (Total Plate Count — tổng vi khuẩn) CAO hơn spec → vi khuẩn nhiều từ đầu\n✗ NCC mới (sữa rẻ hơn nhưng chất lượng kém hơn?)\n\nMethod:\n✗ CIP (Clean-In-Place — vệ sinh tại chỗ) nhiệt độ THẤP HƠN tiêu chuẩn → không diệt đủ vi khuẩn\n✗ Thời gian CIP cắt ngắn (\"để chạy nhanh!\")\n\nEnvironment:\n✗ Kho lạnh nhiệt độ dao động 2-6°C (spec 2-4°C) → vi khuẩn phát triển nhanh hơn\n\nMan:\n✗ Operator không kiểm tra seal integrity (độ kín) hàng ca\n\nTOP 3: (1) CIP nhiệt độ thấp (2) Seal rò rỉ (3) TPC sữa tươi cao",
            "result": "Kiểm chứng:\n• CIP: Review log → nhiệt CIP = 72°C (spec 85°C!) → DO SENSOR NHIỆT SAI! → Nhiệt thực tế thấp hơn hiển thị → ROOT CAUSE #1!\n• Seal: Kiểm tra → gasket mòn → rò rỉ nhỏ → vi khuẩn xâm nhập → ROOT CAUSE #2\n\nAction:\n• Hiệu chuẩn sensor nhiệt CIP + tăng nhiệt đúng 85°C\n• Thay gasket + PM gasket mỗi 3 tháng + Operator kiểm tra seal hàng ca\n• IQC: Kiểm tra TPC sữa tươi nhập → reject nếu > spec\n\nKết quả: Shelf life phục hồi 11 ngày! 0 khiếu nại!\n→ Bài học C-E: Nhánh Measurement (sensor nhiệt sai) mà nhiều người HAY BỎ QUA → C-E buộc phải xét MEASUREMENT → phát hiện sensor gian dối!"
        },
        {
            "title": "Bug rate tăng 3x sau microservices — Integration test thiếu!",
            "industry": "CNTT",
            "situation": "Đội dev chuyển từ monolith (1 khối) sang microservices (nhiều dịch vụ nhỏ). Bug rate (tỷ lệ lỗi) tăng GẤP 3 lần! Sếp hỏi: \"Kiến trúc mới kém hơn à?\"",
            "analysis": "Fishbone C-E cho \"Bug rate tăng 3x\":\n\nMan (Developer):\n✗ Dev chưa quen distributed system (hệ thống phân tán) → viết code như monolith → lỗi race condition, timeout\n✗ Thiếu kinh nghiệm API design → API không idempotent (gọi 2 lần → kết quả khác!)\n\nMethod (Quy trình):\n✗ THIẾU integration test (test tích hợp giữa các service) → mỗi service test riêng OK nhưng kết hợp lại → LỖI!\n✗ Không có contract testing (kiểm tra hợp đồng API giữa service)\n\nMachine (Hạ tầng):\n✗ Staging environment KHÔNG giống production → test OK ở staging → deploy production → LỖI\n✗ Network latency staging thấp hơn production\n\nMeasurement:\n✗ Logging không đủ chi tiết → lỗi xảy ra nhưng KHÔNG TÌM ĐƯỢC nguyên nhân (request đi qua 5 service → log ở service nào?)\n✗ Thiếu distributed tracing\n\nTOP 3: (1) Thiếu integration test (2) Dev chưa quen (3) Staging ≠ production",
            "result": "Action:\n\n• Contract testing: Mỗi service định nghĩa API contract → test tự động khi code change → phát hiện breaking change TRƯỚC deploy\n• Chaos engineering: Cố tình tạo lỗi (kill service, tăng latency) → test hệ thống chịu lỗi → tìm weak point\n• Centralized logging + Distributed tracing: Mỗi request có trace ID → theo dõi từ request → qua tất cả services → response → BÁO lỗi ở service cụ thể\n• Training: Course distributed system patterns (circuit breaker, retry, idempotency) cho team\n\nKết quả: Bug rate giảm 70%!\n→ Bài học: C-E phù hợp cho cả phần mềm! Dùng 4P (People, Process, Platform, Practice) thay 6M cho CNTT."
        },
        {
            "title": "Chi phí bảo trì tăng 35% mà OEE không tăng — Reactive mode!",
            "industry": "Sản xuất chung",
            "situation": "Chi phí BT tăng 35% so với năm trước (từ 5 tỷ → 6.75 tỷ). NHƯNG OEE KHÔNG CẢI THIỆN — vẫn 62%! BGĐ hỏi: \"Tiền đi đâu?\"",
            "analysis": "Fishbone C-E cho \"Chi phí BT tăng 35% mà OEE không tăng\":\n\nMan:\n✗ Thiếu KTV lành nghề → thuê ngoài đắt gấp 3 → chi phí tăng\n✗ 2 KTV kinh nghiệm nghỉ việc → KTV mới sửa lâu hơn (MTTR tăng)\n\nMachine:\n✗ Thiết bị cũ > 15 năm → breakdown TĂNG → sửa nhiều hơn\n✗ Bathtub curve: Đang vào giai đoạn wear-out → hỏng nhiều bộ phận hơn\n\nMethod:\n✗ REACTIVE maintenance (chữa cháy — chờ hỏng mới sửa) → không PM → breakdown nhiều → chi phí cao!\n✗ Không có PM plan → mọi sửa chữa đều khẩn cấp → tốn OT (overtime), tốn phụ tùng gấp\n\nMaterial (Phụ tùng):\n✗ Phụ tùng không chính hãng → rẻ khi mua nhưng TUỔI THỌ NGẮN → thay nhiều lần → tổng chi phí CAO hơn\n✗ Phụ tùng mua gấp (express delivery) vì không dự trữ → giá đắt hơn 50%\n\nTOP 3: (1) Reactive mode (2) Thiết bị cũ (3) Phụ tùng giả",
            "result": "Action:\n\n• Chuyển từ Reactive → Planned Maintenance: Xây dựng PM plan cho TOP 20 thiết bị critical → PM = sửa kế hoạch (rẻ hơn!) thay vì emergency repair (đắt!)\n• Training KTV nội bộ: Giảm thuê ngoài từ 40% → 10% → tiết kiệm 30% chi phí nhân công\n• Phụ tùng chính hãng + Tồn kho critical spare: Mua chính hãng = đắt hơn 20% nhưng tuổi thọ GẤP 3 → tổng chi phí GIẢM!\n\nKết quả sau 1 năm: Chi phí BT giảm 20% (6.75 → 5.4 tỷ). OEE tăng từ 62% → 70%!\n→ Bài học C-E: Fishbone chỉ ra REACTIVE maintenance = ROOT CAUSE khiến chi phí CAO mà kết quả VẪN TỆ → Đầu tư PM trước = tiết kiệm sau!"
        },
        {
            "title": "Tai nạn lao động tăng gấp đôi — Training + Dàn giáo!",
            "industry": "Xây dựng",
            "situation": "Công trường xây dựng lớn: 8 vụ tai nạn trong quý, tăng GẤP ĐÔI so với quý trước. 3 vụ nghiêm trọng (gãy xương). Thanh tra yêu cầu dừng thi công nếu không cải thiện!",
            "analysis": "Fishbone C-E cho \"Tai nạn lao động tăng gấp đôi\" — Đây là VẤN ĐỀ NGHIÊM TRỌNG → cần phân tích kỹ!\n\nMan:\n✗ 50% công nhân MỚI (tuyển gấp cho phase 2) → CHƯA ĐƯỢC TRAINING an toàn!\n✗ Công nhân cũ \"quen rồi\" → bỏ qua dây an toàn, không đội mũ\n\nMethod:\n✗ SOP an toàn LỖI THỜI (từ 2018, chưa cập nhật cho loại dàn giáo mới)\n✗ Không có Safety Talk hàng sáng (toolbox meeting)\n\nMachine:\n✗ Dàn giáo (scaffolding) cũ, mục → gãy → rơi\n✗ Dây an toàn (harness) nhiều cái quá date (hết hạn sử dụng!)\n\nEnvironment:\n✗ Mùa mưa → trời TRƠN → ngã từ cao\n✗ Ánh sáng yếu buổi chiều → nhìn không rõ → vấp\n\nMeasurement:\n✗ KHÔNG AUDIT an toàn định kỳ → vi phạm an toàn không ai biết cho đến khi tai nạn xảy ra\n✗ Không có near-miss reporting (báo cáo suýt tai nạn)\n\nTOP 3: (1) Công nhân mới chưa training (2) Dàn giáo cũ (3) Không audit",
            "result": "Action NGAY LẬP TỨC (không chờ!):\n\n• Man: Safety training BẮT BUỘC 2 ngày cho TẤT CẢ công nhân mới trước khi vào công trường. Old workers: Refresher training 4h\n• Machine: Kiểm tra + THAY tất cả dàn giáo không đạt chuẩn. Kiểm tra harness → thay cái hết date\n• Method: Safety Talk hàng sáng 15 phút → nhắc nhở rủi ro trong ngày\n• Measurement: Safety audit HÀNG TUẦN → vi phạm → dừng thi công tại vị trí đó ngay\n• Near-miss reporting: Thưởng BÁO CÁO suýt tai nạn (không phạt!) → phát hiện rủi ro TRƯỚC khi xảy ra\n\nKết quả: 0 tai nạn 2 quý tiếp theo! Thanh tra hài lòng!\n→ Bài học: C-E cho vấn đề AN TOÀN PHẢI xét TẤT CẢ 6M — vì tổn thương con người KHÔNG THỂ chấp nhận được!"
        }
    ]
}
