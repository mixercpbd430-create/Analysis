method = {
    "id": 17,
    "title": "WWBLA - Why-Why Because Logical Analysis",
    "short_name": "WWBLA",
    "icon": "🧠",
    "pillar": "Focus Improvement",
    "description": "Why-Why nâng cấp: Hỏi 'TẠI SAO?' đi XUỐNG tìm root cause → Đọc NGƯỢC LÊN 'BỞI VÌ...' xác nhận LOGIC ĐÚNG 2 CHIỀU!",
    "meaning": """
<p><strong>WWBLA (Why-Why Because Logical Analysis — Phân tích logic Tại sao - Bởi vì)</strong> là phương pháp phân tích NÂNG CAO, kết hợp 2 hướng suy luận để xác nhận nguyên nhân gốc với ĐỘ TIN CẬY CAO:</p>
<p><em>Hình dung: Why-Why thường (method 18) = đi XUỐNG cầu thang (hỏi tại sao? tại sao?) → đến tầng trệt → TƯỞNG đúng! WWBLA = đi XUỐNG + rồi đi NGƯỢC LÊN (bởi vì A → nên B → nên C) → NẾU đi ngược lên MÀ LOGIC → XÁC NHẬN nguyên nhân ĐÚNG! Nếu đi ngược mà VÔ LÝ → nguyên nhân SAI → tìm lại!</em></p>
<div class="note-box note-box--tip">
    <div class="note-title">💡 2 chiều kiểm tra logic — "Chìa khóa vàng" của WWBLA</div>
    <p><strong>Hướng XUỐNG (Why — Top-Down)</strong>:<br>
    Vấn đề: "Máy dừng" → <strong>TẠI SAO?</strong> → "Motor quá tải" → <strong>TẠI SAO?</strong> → "Die tắc" → <strong>TẠI SAO?</strong> → "NVL cứng" → <strong>TẠI SAO?</strong> → "Bắp tăng 30%→50%"<br><br>
    <strong>Hướng LÊN (Because — Bottom-Up) — KIỂM TRA!</strong>:<br>
    "<strong>BỞI VÌ</strong> bắp tăng 50% → <strong>NÊN</strong> NVL cứng hơn" ✅ Logic!<br>
    "<strong>BỞI VÌ</strong> NVL cứng → <strong>NÊN</strong> die tắc" ❌ LOGIC SAI! (NVL cứng → tải CAO, nhưng không TRỰC TIẾP gây TẮC!)<br>
    → Phát hiện BUG! → Sửa: "BỞI VÌ NVL cứng + ẩm thấp → NÊN viên không kết dính → NÊN die tắc" ✅ LOGIC đúng!<br><br>
    <em>WWBLA tốt hơn Why-Why thường: Why-Why có thể đi SAI HƯỚNG mà KHÔNG BIẾT! WWBLA kiểm tra LOGIC NGƯỢC → phát hiện SAI ngay!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định root cause với ĐỘ TIN CẬY CAO HƠN Why-Why thông thường — vì kiểm tra logic 2 chiều!</li>
    <li>LOẠI BỎ false cause (nguyên nhân sai): Nhiều team làm Why-Why đi sai hướng → countermeasure KHÔNG HIỆU QUẢ → vấn đề TÁI PHÁT! WWBLA phát hiện false cause TRƯỚC KHI action!</li>
    <li>ĐÀO TẠO tư duy phân tích LOGIC: Team PHẢI suy nghĩ "Bởi vì A nên B — CÓ ĐÚNG KHÔNG?" → rèn tư duy chặt chẽ!</li>
    <li>Giải quyết vấn đề PHỨC TẠP có nhiều nhánh: Mỗi nhánh why-why → kiểm tra because → giữ nhánh ĐÚNG + loại nhánh SAI!</li>
    <li>Tạo tài liệu phân tích CÓ CẤU TRÚC + dễ review: Manager đọc Because từ dưới lên → verify logic NHANH!</li>
    <li>Kết hợp với DỮ LIỆU thực tế: Mỗi bước Because → yêu cầu BẰNG CHỨNG → không đoán mò!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: ĐỊNH NGHĨA vấn đề RÕ RÀNG — 5W!</div>
        <div class="step-card__desc">Mô tả vấn đề CỤ THỂ: <strong>What</strong> (Cái gì?): Máy ép viên dừng. <strong>When</strong> (Khi nào?): Ca 2, sau 3 giờ chạy. <strong>Where</strong> (Ở đâu?): Pellet Mill #3. <strong>How much</strong> (Bao nhiêu?): 3 lần/tuần, mỗi lần 45 phút. <strong>Impact</strong> (Thiệt hại?): Mất 15 tấn/tuần = 75 triệu VND/tuần. KHÔNG viết mơ hồ: "Máy hay dừng" → SAI! Viết cụ thể với SỐ LIỆU!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: WHY-WHY (Top-Down) — Hỏi TẠI SAO 5-7 lần + BẰNG CHỨNG!</div>
        <div class="step-card__desc">Hỏi "TẠI SAO?" liên tục → tạo CÂY NGUYÊN NHÂN từ trên xuống: Tại mỗi bước: (1) Hỏi "Tại sao?" (2) Trả lời (3) <strong>CÓ BẰNG CHỨNG KHÔNG?</strong> Bằng chứng: Dữ liệu đo được? Data log? Ảnh chụp? Witness? QUY TẮC: Mỗi "Tại sao" phải dựa trên SỰ THẬT, không phỏng đoán! Nếu 1 bước có NHIỀU nguyên nhân → CHIA NHÁNH → mỗi nhánh = 1 chuỗi Why-Why riêng! Dừng khi đạt nguyên nhân ACTIONABLE (có thể hành động) + PREVENTABLE (có thể ngăn ngừa) + WITHIN CONTROL (trong tầm kiểm soát)!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: BECAUSE (Bottom-Up) — Đọc NGƯỢC LÊN kiểm tra logic!</div>
        <div class="step-card__desc">Từ nguyên nhân GỐC → đọc NGƯỢC LÊN: "<strong>BỞI VÌ</strong> [nguyên nhân gốc] → <strong>NÊN</strong> [bước trên] → <strong>NÊN</strong> [bước trên nữa] → <strong>NÊN</strong> [vấn đề]". Tại MỖI bước ngược, hỏi: "Bởi vì A thì CÓ THẬT NÊN B không?" <strong>✅ Logic ĐÚNG</strong> → Giữ! <strong>❌ Logic SAI</strong> → Nguyên nhân SAI! → quay lại bước 2 → tìm lại! <strong>⚠️ Logic CÓ THỂ nhưng THIẾU</strong> → cần thêm điều kiện → bổ sung! Ví dụ LOGIC SAI: "Bởi vì NVL cứng → nên MÁY NỔ!" → Vô lý! NVL cứng → tải cao → motor quá tải → dừng. KHÔNG NỔ! → Sửa lại!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: XÁC NHẬN bằng DỮ LIỆU + COUNTERMEASURE</div>
        <div class="step-card__desc">Sau khi Because verify LOGIC ĐÚNG → Thu thập dữ liệu XÁC NHẬN nguyên nhân gốc: Đo → So sánh → Chứng minh! Đề xuất COUNTERMEASURE cho nguyên nhân đã verify: Mỗi root cause → 1-2 countermeasure cụ thể. Phân loại: Temporary (tạm thời): Sửa ngay → ngăn tái phát NGẮN HẠN. Permanent (vĩnh viễn): Sửa tận gốc → ngăn tái phát VĨNH VIỄN (SOP, thiết kế, Poka-Yoke). Follow-up: KIỂM TRA sau 1-3 tháng → vấn đề CÓ TÁI PHÁT không? Nếu TÁI PHÁT → root cause CHƯA ĐÚNG → làm lại!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Máy ép viên dừng 3 lần/tuần — Because phát hiện THIẾU LOGIC ở bước 3!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy ép viên dừng do overload (quá tải) 3 lần/tuần, mỗi lần 45 phút. Thiệt hại 75 triệu/tuần. Team đã làm Why-Why thường → kết luận \"do NVL\" → đổi NVL → VẪN DỪNG!",
            "analysis": "WHY-WHY (Top-Down):\n• Vấn đề: Máy ép viên dừng do overload 3 lần/tuần\n• Why 1: Tại sao dừng? → Motor amps vượt 120% FLA → trip overload relay\n📊 Bằng chứng: Log amps PLC — 3 lần trip đều ở 125 A (FLA = 100A)\n• Why 2: Tại sao motor amps cao? → Tải trên die quá lớn\n📊 Bằng chứng: Pressure die > 50 bar (bình thường 35 bar)\n• Why 3: Tại sao tải die lớn? → NVL cứng hơn bình thường\n📊 Bằng chứng: Hardness test NVL — 25 HB (bình thường 18 HB)\n• Why 4: Tại sao NVL cứng? → Tỷ lệ bắp tăng từ 30% → 50% (formula mới)\n📊 Bằng chứng: Recipe sheet — đã thay đổi tháng 3\n• Why 5: Tại sao bắp tăng? → Phòng formula thay đổi để GIẢM GIÁ THÀNH\n\nBECAUSE (Bottom-Up) — KIỂM TRA LOGIC:\n• BỞI VÌ phòng formula tăng bắp 50% → NÊN NVL cứng hơn ✅ Logic đúng!\n• BỞI VÌ NVL cứng → NÊN tải die cao ⚠️ THIẾU LOGIC! NVL cứng KHÔNG TRỰC TIẾP gây tải cao → CẦN thêm: NVL cứng + ẨM conditioning THẤP → viên khó ép → tải die CAO! → Kiểm tra: Ẩm conditioning = 13% (spec 16-17%!) → THIẾU STEAM!\n• BỞI VÌ tải die cao → NÊN motor amps vượt → NÊN trip ✅ Logic đúng!\n\n→ Because phát hiện THIẾU 1 ROOT CAUSE: Ẩm conditioning thấp! Why-Why thường chỉ tìm \"bắp tăng\" → NHƯNG thực tế CẦN THÊM \"conditioning kém\" mới gây die quá tải!",
            "result": "2 Root Causes (nhờ WWBLA!) vs 1 Root Cause (Why-Why thường):\n\n• RC1: Bắp tăng 50% → Action: Phối hợp phòng formula → NẾU bắp > 35% → PHẢI nghiền mịn hơn + thêm chất kết dính (lignosulfonate 0.5%)\n• RC2: Ẩm conditioning thấp 13% (Because phát hiện!): → Action: Tăng steam pressure 2.0 → 2.5 bar + kiểm tra steam trap (1 trap bị kẹt đóng → steam KHÔNG ĐỦ!) → Sửa steam trap → ẩm tăng lên 16.5%\n\nKết quả: Overload dừng 3 lần/tuần → 0 lần! Tiết kiệm 75 triệu/tuần = 300 triệu/tháng!\n\n→ Bài học WWBLA: Why-Why thường tìm 1 RC (bắp tăng) → đổi bắp → VẪN DỪNG (vì conditioning kém!). WWBLA Because phát hiện \"NVL cứng → tải cao\" THIẾU LOGIC → cần thêm \"conditioning kém\" → tìm ĐỦ 2 RC → SỬA ĐỦ 2 → HẾT DỪNG!"
        },
        {
            "title": "Chi phí bảo trì tăng 40% — Because chỉ ra PM CHECKLIST LÀ GỐC!",
            "industry": "Sản xuất",
            "situation": "Chi phí bảo trì tăng 40% YoY nhưng thiết bị VẪN hỏng nhiều! BGĐ hỏi: \"Tăng tiền mà sao vẫn hỏng?\" → WWBLA tìm root cause THỰC SỰ.",
            "analysis": "WHY-WHY (Top-Down):\n• Why 1: Tại sao chi phí BT tăng 40%? → Reactive repair (sửa chữa khẩn cấp) CHIẾM 70% tổng chi phí! Reactive đắt 3× planned!\n• Why 2: Tại sao reactive nhiều? → PM (bảo trì phòng ngừa) KHÔNG HIỆU QUẢ → không bắt được failure mode sớm→ thiết bị vẫn hỏng bất ngờ!\n• Why 3: Tại sao PM không hiệu quả? → PM checklist KHÔNG cập nhật — vẫn dùng checklist 5 năm trước!\n• Why 4: Tại sao checklist không cập nhật? → KHÔNG CÓ feedback loop từ breakdown analysis → PM team KHÔNG BIẾT failure mode mới!\n• Why 5: Tại sao không có feedback loop? → Breakdown report chỉ ghi \"hỏng gì + sửa gì\" → KHÔNG phân tích root cause → KHÔNG cập nhật PM!\n\nBECAUSE (Bottom-Up):\n• BỞI VÌ breakdown report KHÔNG phân tích root cause → NÊN không có failure mode mới ✅\n• BỞI VÌ không có failure mode mới → NÊN PM checklist cũ ✅\n• BỞI VÌ PM checklist cũ → NÊN PM không bắt được failure mode mới ✅\n• BỞI VÌ PM không bắt failure mode → NÊN thiết bị hỏng bất ngờ ✅\n• BỞI VÌ hỏng bất ngờ → NÊN reactive repair nhiều → chi phí tăng 40% ✅\n→ Logic ĐÚNG TỪ DƯỚI LÊN! Root cause confirmed!",
            "result": "Countermeasure — Feedback Loop!:\n\n• Temporary: Review 36 tháng breakdown data → cập nhật PM checklist NGAY → thêm 25 item mới!\n• Permanent — Feedback Loop:\nMỗi breakdown → Breakdown Analysis Report (BAR) → Root Cause → THÊM checkpoints vào PM!\nMonthly review: PM team + Production → cập nhật checklist\nKPI: \"PM effectiveness\" = % breakdown mà PM đã CHECK nhưng không phát hiện → PHẢI = 0%!\n\nKết quả 6 tháng: Chi phí BT giảm 25%! Reactive 70% → 35%! Availability tăng 12%!\n\n→ Bài học WWBLA: Because từ dưới lên = \"câu chuyện hoàn chỉnh\" ai đọc cũng hiểu! Manager đọc: \"À, hóa ra gốc là breakdown report không phân tích root cause → PM checklist cũ → hỏng bất ngờ → chi phí tăng!\" → THUYẾT PHỤC hơn Why-Why thường!"
        },
        {
            "title": "Sản phẩm bị ẩm mốc sau 2 tháng — Because phát hiện 2 nhánh ĐỒNG THỜI!",
            "industry": "Thực phẩm",
            "situation": "Bột dinh dưỡng đóng gói bị ẩm mốc trong bao bì sau 2 tháng. Khách hàng complaint tăng 5× → NGUY CƠ THU HỒI! WWBLA phân tích gấp.",
            "analysis": "WHY-WHY (Top-Down) — 2 NHÁNH!:\n\nNhánh 1 — Seal:\n• Why 1: Tại sao mốc? → Moisture (ẩm) tăng trong bao bì → vi sinh phát triển\n• Why 2: Tại sao ẩm tăng? → Seal bao bì KHÔNG KÍN → hơi ẩm lọt vào\n• Why 3: Tại sao seal không kín? → Seal jaw (thanh hàn nhiệt) bị MÒN → không ép đều\n• Why 4: Tại sao jaw mòn? → PM seal jaw lịch 6 tháng/lần → QUÁ DÀI cho production volume hiện tại (tăng 2× so với lúc đặt lịch PM!)\n\nNhánh 2 — Film:\n• Why 2b: Tại sao ẩm tăng? → Film bao bì THẤM ẨM → MVTR (Moisture Vapor Transmission Rate) quá cao!\n• Why 3b: Tại sao MVTR cao? → NCC thay đổi cấu trúc film (từ 3 lớp → 2 lớp!) mà KHÔNG THÔNG BÁO!\n\nBECAUSE (Bottom-Up) — Kiểm tra CẢ 2 nhánh:\n• Nhánh 1: BỞI VÌ PM 6 tháng quá dài → jaw mòn → seal kém → ẩm vào → mốc ✅ ĐÚNG!\n• Nhánh 2: BỞI VÌ NCC giảm lớp film → MVTR tăng → ẩm thấm → mốc ✅ ĐÚNG!\n→ CẢ 2 NHÁNH đều ĐÚNG LOGIC! → 2 root causes ĐỘC LẬP nhưng ĐỒNG THỜI gây mốc!",
            "result": "Countermeasure cho CẢ 2 nhánh:\n\n• Nhánh 1 (Seal jaw mòn): Rút PM từ 6 tháng → 2 tháng! + Seal strength test HÀNG NGÀY (mỗi ca lấy 5 mẫu → test kéo → ≥ 2 kg/15mm) + Moisture sensor trong gói (indicator card)\n• Nhánh 2 (Film MVTR cao): Yêu cầu NCC quay lại film 3 lớp + Incoming test MVTR cho TỪNG lô film → Spec: MVTR 5× → 0!\n\n→ Bài học WWBLA đa nhánh: Why-Why thường → có thể tìm 1 nhánh (seal jaw) → sửa → MỐC VẪN CÒN (vì film cũng thấm ẩm!). WWBLA Because kiểm tra 2 nhánh → XÁC NHẬN cả 2 → sửa CẢ 2 → 100% hết mốc!"
        },
        {
            "title": "Server API response 2000ms — Because xác nhận migration script drop index!",
            "industry": "CNTT",
            "situation": "API response time tăng từ 200ms → 2000ms (chậm 10×!) trong 3 tuần. User complaint tăng mạnh. DevOps team check server resources → CPU/RAM bình thường!",
            "analysis": "WHY-WHY (Top-Down):\n• Why 1: Tại sao API chậm? → Database query slow (Why 2: Tại sao DB query slow? → Full table scan (quét TOÀN BỘ bảng)\n📊 Bằng chứng: EXPLAIN PLAN → Seq Scan thay vì Index Scan!\n• Why 3: Tại sao full table scan? → Index bị DROP (xóa)!\n📊 Bằng chứng: pg_indexes → index user_email_idx KHÔNG CÒN!\n• Why 4: Tại sao index bị drop? → DB migration script (version 3.2.0) có lệnh DROP INDEX!\n📊 Bằng chứng: Git log → commit abc123 → migration file → DROP INDEX user_email_idx\n• Why 5: Tại sao migration drop mà không recreate? → Developer rebuild table → DROP + CREATE TABLE → QUÊN create index! + CI/CD pipeline KHÔNG CÓ index validation!\n\nBECAUSE (Bottom-Up):\n• BỞI VÌ CI/CD không validate index → NÊN migration drop index mà không ai biết ✅\n• BỞI VÌ index bị drop → NÊN DB full table scan ✅\n• BỞI VÌ full table scan → NÊN query slow 1800ms ✅\n• BỞI VÌ query slow → NÊN API response 2000ms ✅\n→ Logic HOÀN HẢO từ dưới lên! Confirmed by EXPLAIN PLAN!",
            "result": "Countermeasure:\n\n• Immediate (tạm thời): RECREATE index ngay! → API response phục hồi Permanent:\nCI/CD pipeline thêm index validation: Sau mỗi migration → tự động check: Số index TRƯỚC migration vs SAU migration → nếu GIẢM → WARNING + block deploy!\nCode review cho migration scripts: Rule: MỌI migration có DROP → PHẢI có CREATE tương ứng!\nDatabase smoke test: Sau deploy → auto-run top 10 critical queries → nếu > 500ms → ROLLBACK!\n\n→ Bài học WWBLA IT: Because từ dưới lên = \"câu chuyện debugging\" hoàn hảo: Migration drop index → full scan → slow → API chậm. Ai đọc cũng hiểu! + CI/CD validation = Poka-Yoke cho developer → KHÔNG THỂ drop index mà quên create lại!"
        },
        {
            "title": "Bê tông nứt sớm — Because phát hiện W/C ratio là GỐC, không phải mix!",
            "industry": "Xây dựng",
            "situation": "Sàn bê tông nhà xưởng NỨT SAU 6 THÁNG! Phải sửa chữa 500 triệu! Nhà thầu đổ lỗi thời tiết. Chủ đầu tư thuê tư vấn → WWBLA phân tích.",
            "analysis": "WHY-WHY (Top-Down):\n• Why 1: Tại sao sàn nứt? → Co ngót (drying shrinkage) QUÁ LỚN\n• Why 2: Tại sao co ngót lớn? → W/C ratio (tỷ lệ nước/xi măng) CAO = 0.55 (spec max 0.45!)\n📊 Bằng chứng: Không ghi nhận W/C tại site → nhưng concrete core test: cường độ 25 MPa (spec 35 MPa!) → W/C chắc chắn quá cao!\n• Why 3: Tại sao W/C cao? → Công nhân THÊM NƯỚC tại công trường!\n📊 Bằng chứng: Phỏng vấn workers → \"Bê tông bị đặc quá, phải cho thêm nước để đổ được\"\n• Why 4: Tại sao bê tông đặc? → Thời gian vận chuyển từ trạm trộn = 90 PHÚT (spec max 45 phút!) → bê tông bắt đầu đông → đặc!\n• Why 5: Tại sao vận chuyển lâu? → Trạm trộn XA 40km + kẹt xe → 90 phút!\n\nBECAUSE (Bottom-Up):\n• BỞI VÌ trạm trộn xa 40km + kẹt xe → NÊN vận chuyển 90 phút ✅\n• BỞI VÌ 90 phút → NÊN bê tông bắt đầu đông → đặc ✅\n• BỞI VÌ đặc → NÊN workers thêm nước → W/C cao ✅\n• BỞI VÌ W/C cao → NÊN co ngót lớn → NỨT ✅\n→ Logic hoàn hảo! Nhà thầu nói \"do thời tiết\" → WWBLA Because chứng minh: DO THÊM NƯỚC → DO VẬN CHUYỂN XA!",
            "result": "Countermeasure cho dự án tiếp theo:\n\n• Chọn trạm trộn GẦNNHẤT (Dùng phụ gia chậm đông (retarder) nếu vận chuyển > 30 phút → kéo dài workability\n• GIÁM SÁT W/C tại site: Kỹ sư QA kiểm tra slump (độ sụt) tại site → nếu slump > 12cm → BỔ SUNG phụ gia, KHÔNG THÊM NƯỚC!\n• Sàn hiện tại: Đục bỏ vùng nứt + đổ lại bê tông M400 + bảo dưỡng đúng → 500 triệu\n• Bồi thường: WWBLA report = BẰNG CHỨNG → nhà thầu phải chịu chi phí sửa (lỗi do vận chuyển xa + cho thêm nước!)\n\n→ Bài học WWBLA xây dựng: Nhà thầu nói 'do thời tiết' → WWBLA Because chứng minh LOGIC: Trạm xa → vận chuyển lâu → đặc → thêm nước → W/C cao → nứt! Logic KHÔNG CÓ 'thời tiết' ở đâu cả! → Nhà thầu phải chịu trách nhiệm!"
        }
    ]
}
