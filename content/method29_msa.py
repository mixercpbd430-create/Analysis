method = {
    "id": 29,
    "title": "MSA - Measurement System Analysis (Phân tích hệ thống đo)",
    "short_name": "MSA",
    "icon": "🔬",
    "pillar": "Overview",
    "description": "Đánh giá độ tin cậy của hệ thống đo lường (con người + thiết bị + phương pháp) — nếu đo sai thì mọi quyết định dựa trên dữ liệu đều sai!",
    "meaning": """
<p><strong>MSA (Measurement System Analysis — Phân tích hệ thống đo)</strong> đánh giá xem hệ thống đo lường có đủ tin cậy không, trước khi dùng dữ liệu đo để ra quyết định.</p>
<p><em>Nói đơn giản: Nếu cái CÂN bạn dùng bị sai, thì việc cân 1,000 sản phẩm đều vô nghĩa — pass hàng lỗi hoặc loại hàng tốt! MSA kiểm tra CÂN có đáng tin không trước khi bắt đầu cân.</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 5 đặc tính đánh giá hệ thống đo</div>
    <p><strong>1. Bias (Sai lệch / Độ chính xác)</strong>: Giá trị đo có đúng so với giá trị thực không? Ví dụ: cân chuẩn 50.00 kg nhưng cân cho 50.30 kg → bias = +0.30 kg<br>
    <strong>2. Linearity (Độ tuyến tính)</strong>: Bias có thay đổi theo dải đo? Ví dụ: ở 10 kg sai 0.1 kg nhưng ở 100 kg sai 1 kg → linearity kém<br>
    <strong>3. Stability (Độ ổn định)</strong>: Đo cùng vật ở thời điểm khác nhau có cho kết quả giống nhau? Ví dụ: sáng đo 50.0 kg, chiều đo 50.5 kg → stability kém<br>
    <strong>4. Repeatability (Độ lặp lại)</strong>: Cùng 1 NGƯỜI đo cùng 1 vật nhiều lần → kết quả có giống nhau không?<br>
    <strong>5. Reproducibility (Độ tái lập)</strong>: KHÁC NGƯỜI đo cùng 1 vật → kết quả có giống nhau không?<br><br>
    <strong>GR&R (Gage Repeatability & Reproducibility)</strong>: Tổng hợp biến động do hệ thống đo<br>
    • GR&R < 10%: ĐẠT — hệ thống đo tốt<br>
    • GR&R 10-30%: Tạm chấp nhận, cần cải tiến<br>
    • GR&R > 30%: KHÔNG ĐẠT — hệ thống đo quá tệ, dữ liệu không đáng tin!</p>
</div>
""",
    "purpose": """
<ul>
    <li>Đảm bảo hệ thống đo đủ tin cậy TRƯỚC KHI thu thập dữ liệu cho SPC — nếu đo sai thì biểu đồ SPC vô nghĩa</li>
    <li>Phân biệt: Sản phẩm thực sự biến động, hay chỉ vì HỆ THỐNG ĐO bị lỗi nên nhìn thấy biến động?</li>
    <li>Đáp ứng yêu cầu tiêu chuẩn quốc tế: IATF 16949 (ô tô), ISO 9001... bắt buộc phải có MSA</li>
    <li>Xác định nguồn gốc biến động: do thiết bị đo? do NGƯỜI đo? hay do phương pháp đo?</li>
    <li>Giảm chi phí do loại nhầm hàng tốt (reject sản phẩm đạt vì đo sai) hoặc bỏ lọt hàng xấu (accept hàng lỗi vì đo sai)</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Chuẩn bị nghiên cứu GR&R</div>
        <div class="step-card__desc">Chọn 10 mẫu sản phẩm đại diện (bao phủ dải từ sản phẩm nhỏ nhất đến lớn nhất). Chọn 3 người đo (operator/appraiser). Mỗi người đo mỗi mẫu 3 lần → tổng 90 phép đo. Người đo KHÔNG biết đang đo mẫu nào (đánh số ngẫu nhiên — để không bị thiên kiến).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Thực hiện đo và ghi nhận</div>
        <div class="step-card__desc">Trộn ngẫu nhiên (randomize) thứ tự đo — tránh đo lần lượt 1→10, dễ bị nhớ kết quả lần trước. Mỗi người đo ĐỘC LẬP — không cho biết kết quả của nhau. Ghi kết quả vào phiếu dữ liệu riêng.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Tính toán GR&R</div>
        <div class="step-card__desc">Repeatability (EV — Equipment Variation): Biến động khi CÙNG 1 người đo lặp lại → phản ánh thiết bị đo. Reproducibility (AV — Appraiser Variation): Biến động GIỮA các người đo → phản ánh con người/phương pháp. GR&R = √(EV² + AV²). %GR&R = GR&R / Tổng biến động × 100%. Dùng Minitab hoặc Excel để tính.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Đánh giá kết quả và hành động</div>
        <div class="step-card__desc">%GR&R < 10%: Tuyệt vời, chấp nhận. 10-30%: Tạm chấp nhận, nên cải tiến. > 30%: Không dùng được! Cần sửa ngay. Nếu Repeatability cao → vấn đề THIẾT BỊ (cần sửa/thay dụng cụ đo). Nếu Reproducibility cao → vấn đề CON NGƯỜI (cần đào tạo + chuẩn hóa SOP đo). Kiểm tra thêm ndc ≥ 5 (number of distinct categories — số mức phân biệt được).</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Cân trọng lượng bao TACN — 3 QC cân khác nhau!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Bao TACN 50 kg ±0.5 kg. 3 nhân viên QC (người A, B, C) cân cùng 10 bao, mỗi bao cân 3 lần. Kết quả: cùng 1 bao mà 3 QC cho kết quả chênh tới 0.8 kg! Ai đúng?",
            "analysis": "Kết quả GR&R:\n• %GR&R = 42% → KHÔNG ĐẠT! (cần Reproducibility = 38% → RẤT CAO! → Vấn đề nằm ở CON NGƯỜI, không phải cân\n• Phân tích sâu: QC-A đặt bao lệch sang 1 bên cân → đọc sai. QC-B chưa chờ số ổn định đã đọc. QC-C đọc đúng cách → kết quả lặp lại tốt nhất",
            "result": "Hành động (sửa CON NGƯỜI vì Reproducibility cao):\n• Viết SOP cân chuẩn: Đặt bao GIỮA mặt cân + chờ số ổn định 3 giây + đọc kết quả\n• Đào tạo cả 3 QC bằng video hướng dẫn (quay QC-C làm mẫu)\n• Kiểm tra lại (re-study) sau đào tạo → GR&R giảm từ 42% xuống 8.5%! ĐẠT!\n→ Bài học: Cân không sai — NGƯỜI cân sai! Chỉ cần đào tạo và SOP là đủ, không cần mua cân mới."
        },
        {
            "title": "Đo độ ẩm bằng NIR vs lò sấy — Cái nào đúng?",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy đo ẩm nhanh NIR (Near-Infrared — hồng ngoại gần, đo trong 30 giây) và phương pháp sấy lò (oven method — sấy 2 giờ, kết quả chính xác nhất) cho kết quả chênh 1-2%. Spec 11-13%. Câu hỏi: Tin NIR hay tin lò sấy?",
            "analysis": "Nghiên cứu Bias (sai lệch hệ thống):\n• NIR đo THẤP HƠN lò sấy trung bình 0.8% → bias = -0.8%. Nghĩa là NIR hiển thị 12% thì thực tế là 12.8%\n• Linearity: Bias tăng lên khi ẩm > 13% — ở vùng ẩm thấp sai ít, vùng ẩm cao sai nhiều hơn\n• Stability: NIR trôi 0.3%/tháng nếu không hiệu chuẩn — do bụi bám trên cửa sổ đo, mẫu chuẩn bên trong máy bị biến đổi",
            "result": "Hành động:\n• Hiệu chuẩn NIR với lò sấy mỗi tuần: Lấy 5 mẫu, đo NIR trước rồi sấy lò. Nếu chênh > 0.3% → chỉnh lại hệ số hiệu chuẩn\n• Cập nhật calibration model (mô hình toán học trong NIR) khi thay đổi nguyên liệu hoặc nhà cung cấp NL mới\n→ Bias giảm từ 0.8% xuống 0.2%. Stability ±0.1%/tháng.\n→ Bài học: NIR nhanh nhưng cần \"chỉnh\" thường xuyên bằng phương pháp chuẩn (lò sấy). Không hiệu chuẩn = đo bừa!"
        },
        {
            "title": "Thước kẹp vs Micrometer — Chọn đúng dụng cụ",
            "industry": "Cơ khí",
            "situation": "Đo đường kính trục Ø25.00 ±0.02 mm (dung sai rất chặt!). Dùng thước kẹp số (digital caliper, phân giải 0.01 mm). GR&R = 45% — KHÔNG ĐẠT! Biến động đo quá lớn so với dung sai 0.04 mm.",
            "analysis": "Phân tích chi tiết:\n• Repeatability = 35%: Cùng 1 người đo lại → kết quả khác! Nguyên nhân: Lực bấm thước kẹp (clamping force) khác nhau mỗi lần → má đo ép vào trục với lực khác → kết quả khác\n• Reproducibility = 28%: 2/3 người đo bấm xéo (không vuông góc) → đọc sai\n• ndc = 2 (chỉ phân biệt được 2 mức: to hoặc nhỏ) — trong khi cần ndc ≥ 5 để kiểm soát quá trình\n→ Kết luận: Thước kẹp KHÔNG PHÙ HỢP cho dung sai ±0.02 mm!",
            "result": "Hành động:\n• Chuyển sang micrometer (panme): Phân giải 0.001 mm (gấp 10 lần thước kẹp), có cơ cấu tay vặn (ratchet stop) đảm bảo lực đo cố định\n• GR&R mới = 6.2% → ĐẠT! ndc = 8 → phân biệt tốt\n• Quy định: Thước kẹp chỉ dùng cho dung sai ≥ 0.1 mm. Dung sai chặt hơn → dùng micrometer\n→ Bài học: Chọn dụng cụ đo phải phù hợp dung sai. Phân giải dụng cụ đo nên nhỏ hơn 1/10 dung sai."
        },
        {
            "title": "Đo độ cứng viên thuốc — Đặt viên đúng cách!",
            "industry": "Dược phẩm",
            "situation": "Viên nén: Spec độ cứng 8-12 kP (kilopond). 3 nhân viên phân tích (analyst) đo cùng 10 viên thuốc → kết quả chênh nhau tới 2 kP! Một analyst bảo đạt, analyst khác bảo không đạt cùng 1 viên.",
            "analysis": "GR&R = 35% → KHÔNG ĐẠT!\n• Repeatability = 12% (cùng 1 analyst đo lại → OK, khá ổn)\n• Reproducibility = 33% → RẤT CAO! → Vấn đề là CON NGƯỜI\n• Nguyên nhân gốc rễ: 2 analyst đặt viên KHÁC HƯỚNG khi đo! Analyst A đặt viên NẰM NGANG (mặt phẳng hướng lên), Analyst B đặt ĐỨNG (cạnh viên chịu lực). Viên thuốc chịu lực khác nhau ở các hướng khác nhau → kết quả khác!",
            "result": "Hành động:\n• SOP chuẩn: Viên luôn đặt NẰM NGANG, mặt phẳng (có chữ in) hướng lên. Ghi rõ kèm hình ảnh minh họa\n• Đồ gá giữ viên (fixture) — thiết bị nhỏ giữ viên đúng vị trí, analyst không cần cầm tay\n• Đào tạo lại + kiểm tra thực hành\n→ GR&R giảm từ 35% xuống 9% → ĐẠT!\n→ Bài học: 1 chi tiết nhỏ (đặt viên ngang hay đứng) tạo ra sai lệch 2 kP — đủ gây accept/reject sai!"
        },
        {
            "title": "Kiểm tra ngoại quan PCB — 3 người, 3 kết quả!",
            "industry": "Điện tử",
            "situation": "3 nhân viên kiểm tra ngoại quan (visual inspection) bảng mạch PCB. Inspector A accept 85% sản phẩm, B chỉ accept 70%, C accept 88%. Chênh 15%! Cùng 1 lô hàng mà người này đạt, người kia loại.",
            "analysis": "Dùng phương pháp MSA thuộc tính (Attribute MSA — cho kiểm tra đạt/không đạt):\n• Hệ số đồng thuận Kappa = 0.45 → MỨC THẤP (cần > 0.75)\n• Nguyên nhân: Tiêu chuẩn loại bỏ (reject criteria) không rõ ràng cho các lỗi ở RANH GIỚI (borderline defects) — ví dụ: vết xước nhẹ, mối hàn hơi xám, PCB hơi cong → người này cho đạt, người kia cho loại\n• Inspector A và C: dễ dãi (accept nhiều). Inspector B: khắt khe (reject nhiều) → cùng 1 tiêu chuẩn mà hiểu khác nhau!",
            "result": "Hành động:\n• Bộ mẫu giới hạn (limit sample set): Tạo bộ 30 mẫu thật gồm: 10 mẫu OK rõ ràng + 10 mẫu NG rõ ràng + 10 mẫu RANH GIỚI (có quyết định đạt/không đạt ghi sẵn từ QA Manager)\n• Đào tạo 3 inspector bằng bộ mẫu — so sánh quyết định của họ với đáp án chuẩn\n• Dán ảnh chụp mẫu ranh giới tại trạm kiểm tra để tham khảo\n→ Kappa tăng từ 0.45 lên 0.82 (tốt!). Pass rate ổn định 78±3% giữa 3 inspector."
        },
        {
            "title": "Máy đo CMM — Đồ gá quyết định tất cả",
            "industry": "Ô tô",
            "situation": "Máy đo tọa độ CMM (Coordinate Measuring Machine — máy đo 3D chính xác đến 0.001 mm) đo 15 điểm trên tấm vỏ ô tô. GR&R = 22% — tạm chấp nhận nhưng IATF 16949 yêu cầu < 10%.",
            "analysis": "Phân tích chi tiết:\n• Repeatability = 8%: Bản thân máy CMM rất ổn định → thiết bị OK\n• Reproducibility = 20% → CAO! → Vấn đề là CON NGƯỜI khi gá chi tiết\n• Kiểm tra tương tác (interaction plot): Operator B luôn đo CAO HƠN A và C → tại sao?\n• Nguyên nhân: Lực kẹp đồ gá (clamping force) khi gá tấm vỏ lên bàn đo khác nhau giữa 3 operator — B kẹp chặt hơn → tấm vỏ bị uốn nhẹ → tọa độ dịch chuyển → đo cao hơn!",
            "result": "Hành động:\n• Đồ gá kẹp tự động bằng khí nén (auto-clamping pneumatic fixture): Lực kẹp cố định mọi lần, mọi người → loại bỏ biến số con người\n• Quét mã vạch (barcode) chi tiết → tự động nạp chương trình đo tương ứng (không cần operator chọn thủ công)\n→ GR&R giảm từ 22% xuống 5.8% → ĐẠT yêu cầu IATF!\n→ Bài học: Máy CMM đắt tiền nhưng GR&R sai vì đồ gá rẻ tiền! Đầu tư đồ gá tốt quan trọng hơn mua máy đắt."
        },
        {
            "title": "Đo độ dày lớp mạ kẽm — Vị trí đo là then chốt",
            "industry": "Kim loại",
            "situation": "Mạ kẽm spec 15-25 μm (micromet). Dùng máy đo XRF gauge (máy đo chiều dày lớp phủ bằng tia X). Cùng 1 mẫu mà các lần đo chênh nhau tới 5 μm!",
            "analysis": "GR&R = 55% → KHÔNG ĐẠT!\n• Repeatability = 50% → RẤT CAO! → Vấn đề THIẾT BỊ/PHƯƠNG PHÁP (cùng 1 người đo lại vẫn khác!)\n• Nguyên nhân: Mỗi lần đo, đặt máy XRF vào VỊ TRÍ KHÁC trên mẫu → bề mặt mạ không đều → đo điểm dày được 25 μm, đo điểm mỏng được 15 μm\n• Bề mặt gồ ghề (surface roughness) ảnh hưởng đo XRF — diện tích điểm đo (spot size) chỉ 2 mm trên bề mặt không phẳng",
            "result": "Hành động (sửa PHƯƠNG PHÁP vì Repeatability cao):\n• Đồ gá cố định vị trí đo (jig): 5 điểm đo CỐ ĐỊNH trên mỗi mẫu (đánh dấu bằng marker) → mỗi lần đo đúng vị trí đó\n• Đo 5 điểm, lấy TRUNG BÌNH → giảm ảnh hưởng của bề mặt gồ ghề\n• Mài nhẹ (polish) điểm đo cho phẳng trước khi đo → XRF đọc chính xác hơn\n→ GR&R giảm từ 55% xuống 12% → Tạm chấp nhận cho mục đích này."
        },
        {
            "title": "3 cảm biến nhiệt cho 3 kết quả — Tin cái nào?",
            "industry": "Sản xuất chung",
            "situation": "Lò nung: 3 cảm biến nhiệt (thermocouple — TC, loại K) lắp cùng vị trí cho kết quả chênh nhau 15°C! TC-1 hiển thị 585°C, TC-2 hiển thị 603°C, TC-3 hiển thị 598°C. Tin cái nào?",
            "analysis": "Nghiên cứu Bias (sai lệch so với chuẩn):\n• TC-1: Thấp hơn giá trị chuẩn 8°C → bias = -8°C. Nguyên nhân: đầu TC bị oxy hóa (oxide) — dùng lâu trong môi trường nóng, kim loại bị biến chất → tín hiệu yếu hơn → đọc thấp\n• TC-2: Cao hơn chuẩn 3°C → bias = +3°C. Nguyên nhân: dây nối (extension wire) bị chập 1 đoạn → tín hiệu nhiễu\n• TC-3: OK (sai lệch < 1°C) — vì mới thay gần đây\n• Stability: TC-1 trôi 5°C/6 tháng — nếu không hiệu chuẩn, ngày càng sai thêm",
            "result": "Hành động:\n• Thay TC-1 (bị oxy hóa không phục hồi được)\n• Sửa dây nối TC-2 (thay đoạn bị chập)\n• Hiệu chuẩn tất cả TC mỗi 6 tháng bằng lò hiệu chuẩn chuẩn (furnace calibrator)\n• Kết quả: 3 TC cho kết quả đồng nhất ±2°C\n• Lắp thêm TC dự phòng (redundant) cho quá trình quan trọng — nếu 1 TC hỏng vẫn có cái khác kiểm tra chéo."
        },
        {
            "title": "pH sensor online vs lab — Đo khác nhau!",
            "industry": "Hóa chất",
            "situation": "Cảm biến pH gắn trên đường ống (inline sensor) cho kết quả chênh 0.5-1.0 pH so với pH meter phòng lab. Hậu quả: hệ thống tự động bơm THỪA hóa chất (over-dosing) vì sensor đọc sai → tốn hóa chất + ảnh hưởng chất lượng.",
            "analysis": "Nghiên cứu chi tiết:\n• Bias: Sensor inline đọc THẤP HƠN lab 0.7 pH trung bình. Hệ thống thấy pH thấp → bơm thêm kiềm → thực tế pH đã đủ rồi!\n• Stability: Sensor trôi 0.3 pH/tháng — do cặn bám trên điện cực (fouling), lâu ngày che mất bề mặt đo\n• Linearity: Bias tăng khi pH > 9 — điện cực cũ (aging) phản hồi chậm ở vùng kiềm cao, không theo kịp thay đổi pH\n• Thời gian phản hồi: Sensor inline cần 30 giây để ổn định, lab meter gần như ngay lập tức",
            "result": "Hành động:\n• Tự rửa tự động (auto cleaning): Phun nước áp lực (water jet) rửa đầu sensor mỗi 4 giờ → giảm cặn bám → bias ổn định\n• Hiệu chuẩn hàng tuần: Dùng 2 dung dịch chuẩn pH 7 và pH 10 (2-point calibration)\n• Thay điện cực (electrode) mỗi 6 tháng — điện cực cũ mất khả năng phản hồi\n→ Bias giảm từ 0.7 xuống 0.1 pH. Tiết kiệm 30% hóa chất do không còn over-dosing."
        },
        {
            "title": "Đo kích thước hạt bột thuốc — Pha mẫu sai, kết quả sai!",
            "industry": "Dược phẩm",
            "situation": "Kích thước hạt D50 (kích thước trung vị — 50% hạt nhỏ hơn giá trị này) dùng máy laser diffraction: spec 50-80 μm. 2 nhân viên phân tích cùng mẫu bột cho kết quả chênh 15 μm! Một người đo 55 μm, người kia đo 70 μm.",
            "analysis": "GR&R = 38% → KHÔNG ĐẠT!\n• Repeatability = 25%: Cùng 1 analyst đo lại vẫn khác — do cách pha mẫu (sample preparation) mỗi lần khác nhau\n• Reproducibility = 28%: 2 analyst khác nhau vì thời gian siêu âm (ultrasonication — rung siêu âm để phân tán bột trong nước) khác nhau. Analyst A siêu âm 30 giây, Analyst B siêu âm 90 giây → bột phân tán khác nhau → đo khác nhau!\n• Nguyên nhân gốc: Lượng chất phân tán (dispersant), thời gian siêu âm, lượng mẫu — KHÔNG AI quy định cụ thể! Mỗi người làm theo kinh nghiệm cá nhân",
            "result": "Hành động:\n• SOP chi tiết: Chất phân tán: 0.1% Tween 80 (dung dịch hoạt động bề mặt). Siêu âm: chính xác 60 giây ở 50% công suất. Lượng mẫu: chính xác 0.5g. Nhiệt độ nước: 25°C\n• Mỗi bước đều quy định CON SỐ CỤ THỂ — không để \"tùy analyst\"\n→ GR&R giảm từ 38% xuống 7% → Xuất sắc!\n→ Bài học: Trong phân tích lab, SỰ KHÁC BIỆT TRONG CÁCH PHA MẪU thường gây lỗi lớn hơn thiết bị đo!"
        },
        {
            "title": "Siết bulon bánh xe ô tô — Lực siết = An toàn!",
            "industry": "Ô tô",
            "situation": "Bulon bánh xe: spec 110 ±10 Nm (Newton-mét — đơn vị đo momen xoắn). 3 kỹ thuật viên dùng cờ lê lực (torque wrench) cho kết quả chênh nhau trên 20 Nm! Đây là vấn đề AN TOÀN — bulon lỏng xe mất bánh!",
            "analysis": "GR&R = 48% → KHÔNG ĐẠT!\n• Repeatability = 30%: Cùng 1 KTV siết lại → lực khác! Nguyên nhân: Kỹ thuật kéo tay cầm khác nhau (tay phải vs trái, góc kéo 45° vs 90°, kéo nhanh vs chậm)\n• Reproducibility = 35%: 3 cờ lê lực chưa hiệu chuẩn đồng bộ — cờ lê A chặt hơn B 5 Nm, cờ lê C lỏng hơn B 8 Nm",
            "result": "Hành động (vấn đề an toàn → ưu tiên sửa ngay!):\n• Hiệu chuẩn đồng bộ 3 cờ lê lực bằng thiết bị chuẩn (torque analyzer) → cả 3 cho kết quả giống nhau\n• Đào tạo kỹ thuật siết đúng: Kéo smooth ở góc 90° (vuông góc với cờ lê), 1 chuyển động liên tục, không giật\n→ GR&R giảm từ 48% xuống 11% → Tạm chấp nhận.\n→ Dài hạn: Chuyển sang cờ lê lực điện tử (electronic torque wrench) — tự đo và ghi nhận chính xác, không phụ thuộc kỹ thuật tay."
        },
        {
            "title": "Đo gloss sơn — Tranh cãi với khách hàng!",
            "industry": "Sơn",
            "situation": "Độ bóng sơn (Gloss 60°): spec 80-90 GU (Gloss Unit). QC nhà máy đo 85 GU — giao hàng. Khách hàng đo được 77 GU — TỪ CHỐI nhận hàng! Chênh 8 GU → tranh cãi ai đo đúng?",
            "analysis": "So sánh giữa 2 phòng lab (inter-lab comparison):\n• Bias: Máy đo của nhà máy (spectrophotometer — máy đo quang phổ) và máy đo của khách hàng chênh 5 GU! Do tấm hiệu chuẩn (calibration tile) khác nguồn gốc → mỗi máy hiệu chuẩn theo tấm khác → kết quả khác\n• Góc đo (geometry): Nhà máy setup 45°/0°, khách hàng setup d/8° → khác hệ thống quang học\n• Nhiệt độ mẫu: Mẫu nóng (vừa sấy xong kiểm tra) vs mẫu nguội chênh 3 GU\n→ Không ai sai — HỆ THỐNG ĐO khác nhau!",
            "result": "Hành động giải quyết tranh cãi:\n• Đồng bộ tấm hiệu chuẩn: Cả 2 bên dùng tấm calibration tile cùng nguồn (NIST traceable — truy nguyên được từ viện tiêu chuẩn Mỹ)\n• Thống nhất góc đo: Cả 2 bên dùng geometry d/8°\n• Đo mẫu ở 23±2°C (nhiệt độ phòng chuẩn)\n• Khách hàng nâng cấp máy đo (đang dùng máy cũ, sensor yếu)\n→ Chênh lệch giảm từ 8 GU xuống 1.5 GU. Dispute giải quyết — giao nhận bình thường!"
        },
        {
            "title": "Cân phân tích phòng lab — Hơi ấm bàn tay cũng ảnh hưởng!",
            "industry": "Hóa chất",
            "situation": "Cân phân tích phòng lab (độ chính xác 0.1 mg). 3 analyst cân cùng 1 mẫu ~1,000 mg → kết quả chênh nhau tới 5 mg (sai lệch 0.5%!). Trong hóa chất, sai 0.5% có thể ảnh hưởng công thức.",
            "analysis": "GR&R = 28% → Tạm chấp nhận nhưng cần cải tiến\n• Repeatability = 10% (cân OK)\n• Reproducibility = 25% → Vấn đề CON NGƯỜI\n• Nguyên nhân:\n- Analyst C không trừ bì (tare) đúng cách — cân cốc rồi đổ mẫu vào nhưng quên nhấn tare trước\n- Analyst A cầm cốc cân bằng tay trần! Hơi ấm bàn tay truyền vào cốc cân → tạo dòng đối lưu không khí bên trong buồng cân → cân dao động → đọc sai!",
            "result": "Hành động:\n• SOP cân phân tích: Dùng kẹp gắp (forceps) hoặc găng tay cách nhiệt — KHÔNG cầm tay trần cốc cân\n• Nhấn Tare → chờ hiển thị 0.0000 → rồi mới đổ mẫu vào\n• Đóng cửa kính buồng cân khi đọc kết quả — tránh gió, đối lưu\n• Zero cân trước mỗi loạt phép cân\n→ GR&R giảm từ 28% xuống 4.5% → Xuất sắc!"
        },
        {
            "title": "Kiểm tra đạt/không đạt bằng gauge — Lực đẩy quyết định!",
            "industry": "Cơ khí",
            "situation": "Kiểm tra lỗ Ø10 H7 (dung sai 10.000-10.015 mm) bằng gauge Go-NoGo (trục kiểm — nếu trục Go lọt vào = đạt, trục NoGo lọt vào = không đạt). 3 QC cho kết quả pass/fail khác nhau 20%! Cùng 1 chi tiết mà QC này pass, QC kia fail.",
            "analysis": "Phân tích MSA thuộc tính (Attribute Agreement Analysis):\n• QC-B pass 90%, QC-A pass 72%, QC-C pass 68%\n• Kappa = 0.52 → MỨC THẤP\n• Nguyên nhân: QC-B dùng sức ĐẨY gauge vào lỗ! (force fit) → gauge vào bằng lực → cho là pass. Thực tế: gauge phải VÀO BẰNG TRỌNG LƯỢNG RIÊNG (tự rơi vào) → nếu phải đẩy = không đạt!",
            "result": "Hành động:\n• Đào tạo đúng cách dùng gauge: Giữ chi tiết đứng, đặt gauge lên miệng lỗ → gauge phải tự rơi vào bằng trọng lượng riêng = PASS. Nếu phải nhấn = FAIL. Không dùng lực!\n• Tiêu chuẩn hóa: Dựng chi tiết đứng, gauge Go rơi vào = ok, gauge NoGo KHÔNG rơi vào = ok\n→ Kappa tăng từ 0.52 lên 0.88 → Tốt!"
        },
        {
            "title": "Đo độ cứng cao su — Đọc sau bao lâu?",
            "industry": "Cao su",
            "situation": "Độ cứng cao su: spec 60 ±5 Shore A (đơn vị đo độ cứng bề mặt bằng cách nhấn đầu kim vào). 3 QC đo cùng mẫu cao su chênh nhau 8 Shore A!",
            "analysis": "GR&R = 52% → KHÔNG ĐẠT!\n• Repeatability = 20% (OK)\n• Reproducibility = 48% → CỰC CAO!\n• Nguyên nhân gây sốc: Mỗi QC đọc kết quả ở thời điểm KHÁC nhau!\n- QC-A: Đọc NGAY khi kim chạm bề mặt (instantaneous) → số cao (ví dụ: 65)\n- QC-B: Đọc sau 3 giây → số giảm (ví dụ: 62)\n- QC-C: Đọc sau 10 giây → số giảm nhiều (ví dụ: 57)\n• Cao su có tính chất 'creep' (biến dạng từ từ) — kim nhấn vào, cao su lún dần → số đọc GIẢM theo thời gian bấm!",
            "result": "Hành động:\n• SOP theo tiêu chuẩn ASTM D2240: Đặt máy đo, nhấn xuống → đọc chính xác sau 1 GIÂY tiếp xúc. Không sớm hơn, không muộn hơn\n• Đồ gá giữ mẫu (fixture) — tránh tay đè lên mẫu (lực tay thêm → số đọc sai)\n• Mẫu phải dày tối thiểu 6 mm (mỏng hơn → nền cứng phía dưới ảnh hưởng kết quả)\n• Đo 3 điểm khác nhau, lấy trung bình\n→ GR&R giảm từ 52% xuống 9% → ĐẠT!"
        }
    ]
}
