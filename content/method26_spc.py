method = {
    "id": 26,
    "title": "SPC - Statistical Process Control (Kiểm soát quá trình bằng thống kê)",
    "short_name": "SPC",
    "icon": "📉",
    "pillar": "Overview",
    "description": "Sử dụng biểu đồ kiểm soát (control chart) và công cụ thống kê để giám sát, kiểm soát và cải tiến quá trình sản xuất — phát hiện sớm bất thường TRƯỚC KHI tạo phế phẩm.",
    "meaning": """
<p><strong>SPC (Statistical Process Control — Kiểm soát quá trình bằng thống kê)</strong> là phương pháp dùng dữ liệu và biểu đồ thống kê để giám sát quá trình sản xuất, đảm bảo quá trình ổn định và sản phẩm đạt chất lượng.</p>
<p>SPC phân biệt 2 loại biến động:</p>
<ul>
    <li><strong>Biến động ngẫu nhiên (Common cause)</strong>: Dao động nhỏ tự nhiên, luôn tồn tại — ví dụ: trọng lượng bao thức ăn dao động ±0.2kg là bình thường do NL, nhiệt độ, độ ẩm thay đổi nhỏ. <em>Không cần can thiệp ngay</em>, chỉ cải tiến hệ thống.</li>
    <li><strong>Biến động bất thường (Special cause)</strong>: Dao động lớn, có nguyên nhân cụ thể — ví dụ: trọng lượng bao đột ngột giảm 1kg vì cảm biến cân bị trôi. <em>Cần điều tra và xử lý ngay!</em></li>
</ul>
<div class="note-box note-box--info">
    <div class="note-title">📌 Công cụ SPC chính</div>
    <p><strong>Biểu đồ kiểm soát (Control Chart)</strong>: Vẽ giá trị đo theo thời gian, kèm 3 đường:<br>
    • <strong>UCL</strong> (Upper Control Limit — Giới hạn kiểm soát trên) = Trung bình + 3 lần độ lệch chuẩn<br>
    • <strong>CL</strong> (Center Line — Đường trung tâm) = Giá trị trung bình<br>
    • <strong>LCL</strong> (Lower Control Limit — Giới hạn kiểm soát dưới) = Trung bình - 3 lần độ lệch chuẩn<br><br>
    <strong>Cp/Cpk (Chỉ số năng lực quá trình)</strong>: Đánh giá quá trình có đủ khả năng đáp ứng spec không<br>
    • Cpk ≥ 1.33: Tốt — quá trình có đủ năng lực<br>
    • Cpk = 1.0: Vừa đủ — rủi ro cao<br>
    • Cpk < 1.0: Kém — quá trình không đủ năng lực, sẽ có phế phẩm<br><br>
    <em>Nói đơn giản: Control chart giống như máy đo tim trong bệnh viện — nếu nhịp tim nằm trong giới hạn bình thường → OK. Nếu nhảy ra ngoài → BÁO ĐỘNG!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li><strong>Phát hiện sớm</strong> biến động bất thường TRƯỚC KHI sản phẩm bị lỗi — cứu được hàng loạt sản phẩm</li>
    <li>Phân biệt rõ: dao động bình thường hay bất thường → hành động đúng (tránh "sửa quá tay" hoặc "bỏ lọt")</li>
    <li><strong>Đo lường năng lực quá trình</strong> bằng Cp/Cpk — quá trình hiện tại có đủ khả năng đáp ứng yêu cầu không?</li>
    <li>Giảm kiểm tra sản phẩm cuối (inspection) — vì kiểm soát ngay trong quá trình, sản phẩm ra đều tốt</li>
    <li>Cung cấp bằng chứng khoa học cho quyết định cải tiến — dựa trên dữ liệu, không phải cảm tính</li>
    <li>Duy trì quá trình ổn định sau khi cải tiến — biểu đồ kiểm soát "canh gác" không cho quá trình trôi lại</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Chọn đặc tính cần kiểm soát</div>
        <div class="step-card__desc">Chọn đặc tính ảnh hưởng chất lượng nhất (CTQ — Critical to Quality): trọng lượng, kích thước, độ ẩm, nhiệt độ... Xác định tiêu chuẩn (spec): giới hạn trên (USL) và giới hạn dưới (LSL). Xác định cách đo, dụng cụ đo, và tần suất lấy mẫu (mấy mẫu, mấy phút/lần).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Thu thập dữ liệu và chọn loại biểu đồ</div>
        <div class="step-card__desc">Dữ liệu đo được (variable — cân nặng, kích thước): dùng biểu đồ X̄-R (trung bình và biên độ). Dữ liệu đếm (attribute — đạt/không đạt, số lỗi): dùng biểu đồ p (tỷ lệ lỗi) hoặc c (số lỗi). Thu thập ít nhất 25 nhóm mẫu (subgroup) để có đủ dữ liệu tính giới hạn kiểm soát.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Tính giới hạn kiểm soát và vẽ biểu đồ</div>
        <div class="step-card__desc">Tính UCL (giới hạn trên), CL (đường trung tâm), LCL (giới hạn dưới) từ dữ liệu. Vẽ các điểm dữ liệu theo thời gian cùng 3 đường giới hạn. Lưu ý: Giới hạn kiểm soát (UCL/LCL) KHÁC với giới hạn spec (USL/LSL) — control limits tính từ dữ liệu thực tế, spec limits do yêu cầu khách hàng/kỹ thuật.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Đọc biểu đồ, phát hiện bất thường, hành động</div>
        <div class="step-card__desc">Kiểm tra 8 quy tắc phát hiện bất thường: (1) Điểm nào vượt UCL/LCL → BÁO ĐỘNG ngay! (2) 7 điểm liên tiếp cùng phía → quá trình đang trôi (shift). (3) 7 điểm liên tục tăng/giảm → có xu hướng (trend). Khi phát hiện bất thường → DỪNG, điều tra nguyên nhân, sửa ngay. Tính Cp/Cpk để đánh giá năng lực tổng thể.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Trọng lượng bao thức ăn chăn nuôi",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Bao thức ăn 50 kg, dung sai (tolerance) cho phép ±0.5 kg → USL (giới hạn trên) = 50.5 kg, LSL (giới hạn dưới) = 49.5 kg. Khách hàng phàn nàn nhiều bao bị thiếu ký (nhẹ hơn 49.5 kg).",
            "analysis": "Vẽ biểu đồ X̄-R với 30 nhóm mẫu (mỗi nhóm lấy 5 bao cân):\n• Trung bình X̄ = 50.1 kg, biên độ R̄ = 0.8 kg\n• Giới hạn kiểm soát: UCL = 50.56, LCL = 49.64\n• Cpk = 0.67 — rất thấp! (cần ≥1.33)\n• Phát hiện 3 điểm vượt dưới LCL → Báo động! Đây là biến động bất thường (special cause)\n• Điều tra: Cảm biến cân (loadcell) bị trôi giá trị sau 4 giờ chạy liên tục → cân ngày càng thiếu mà không ai biết!",
            "result": "Hành động:\n• Hiệu chuẩn lại loadcell mỗi 4 giờ (trước kia 1 lần/ngày) + thay loadcell cũ bị mỏi (yếu tín hiệu)\n• Kết quả: Cpk tăng từ 0.67 lên 1.45 (đạt yêu cầu). Không còn khiếu nại thiếu ký\n• Bài học: SPC giúp phát hiện vấn đề mà kiểm tra cuối không thấy — loadcell trôi từ từ, nếu chỉ cân kiểm mẫu cuối ca thì không nhận ra xu hướng giảm dần."
        },
        {
            "title": "Độ ẩm viên thức ăn sau ép",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Độ ẩm viên thức ăn sau ép: tiêu chuẩn (spec) 11-13%. Kết quả đo dao động rất lớn 10-14.5% — gây mốc (ẩm cao) hoặc viên giòn dễ vỡ (ẩm thấp).",
            "analysis": "Vẽ biểu đồ X̄-R chart:\n• Trung bình X̄ = 12.2%, biên độ R̄ = 1.8%\n• Cpk = 0.44 — rất kém! Quá trình hoàn toàn không đủ năng lực\n• Phát hiện pattern (dạng mẫu) trên biểu đồ:\n- Độ ẩm tăng cao vào đầu ca (do startup — máy chưa ổn định hơi)\n- Độ ẩm dao động mạnh khi chuyển code sản phẩm (changeover)\n• Nguyên nhân đặc biệt (special cause): Áp suất hơi (steam pressure) lên xuống thất thường do van điều khiển (steam valve) phản hồi chậm",
            "result": "Hành động sửa chữa:\n• Hiệu chỉnh PID (bộ điều khiển tự động) cho van hơi — điều chỉnh tham số P, I, D để van phản hồi nhanh và chính xác hơn\n• SOP khởi động: Xả bỏ 5 phút đầu (sản phẩm đầu ẩm cao, chưa ổn định) — trước kia không có quy định này\n• Lắp cảm biến đo ẩm inline (đo liên tục trên dây chuyền) — phát hiện ngay khi ẩm trôi, không cần chờ QC lấy mẫu\n→ Cpk tăng từ 0.44 lên 1.2. Mục tiêu tiếp theo: đạt 1.33."
        },
        {
            "title": "Độ bền viên PDI thức ăn",
            "industry": "Thức ăn chăn nuôi",
            "situation": "PDI (Pellet Durability Index — chỉ số độ bền viên, đo bằng cách cho viên vào máy lắc quay, tính % viên còn nguyên) yêu cầu ≥92%. Trung bình đạt 94% nhưng thỉnh thoảng rớt xuống 88-90% gây khiếu nại khách hàng.",
            "analysis": "Vẽ biểu đồ I-MR (cá nhân — vì mỗi lần test chỉ 1 mẫu):\n• Trung bình = 93.8%, độ lệch chuẩn σ = 2.1%\n• Phát hiện: Các điểm dưới giới hạn dưới (rớt PDI) đều xảy ra khi die (khuôn ép viên) đã chạy trên 1,200 giờ\n• Vẽ biểu đồ PDI theo tuổi thọ die → thấy trend (xu hướng) giảm rõ ràng: die mòn → lực nén yếu → viên bở\n• Đây là biến động dự đoán được — die mòn là nguyên nhân gốc rễ",
            "result": "Giải pháp dựa trên SPC:\n• Lập biểu đồ theo dõi tuổi thọ die (die life tracking chart) — ghi nhận PDI theo số giờ chạy của từng die\n• Quy định thay die khi PDI trend xuống 93% (dựa trên dữ liệu SPC, không đợi rớt 92%)\n→ Tỷ lệ mẻ bị rớt PDI giảm từ 12% xuống 2%\n→ Bài học: SPC không chỉ phát hiện bất thường hiện tại, mà còn giúp DỰ ĐOÁN vấn đề tương lai dựa trên xu hướng (trend)."
        },
        {
            "title": "Đường kính ống nhựa HDPE",
            "industry": "Nhựa",
            "situation": "Ống HDPE đường kính Ø110 mm ±1 mm. Nhiều cuộn ống bị loại (reject) do sai kích thước — lúc quá to, lúc quá nhỏ. Khách hàng công trình cấp nước yêu cầu chính xác.",
            "analysis": "Vẽ biểu đồ X̄-R (lấy 4 mẫu đo mỗi giờ):\n• Trung bình X̄ = 110.3 mm (hơi lệch về phía lớn), biên độ R̄ = 0.6 mm\n• Phát hiện: 2/3 số điểm nằm trên vùng 2 sigma (2σ) → quá trình đang bị trôi lên (shift)\n• Nguyên nhân: Hiện tượng 'die swell' (nhựa phồng khi ra khỏi đầu đùn) thay đổi — do nhiệt độ barrel zone 3 (vùng nung nóng thứ 3) bị trôi nhiệt kế → nhựa nóng hơn → phồng hơn → ống to hơn",
            "result": "Hành động:\n• Thay điện trở gia nhiệt (heater band) zone 3 bị hỏng 1 thanh + tăng tần suất kiểm tra nhiệt độ mỗi 2 giờ\n→ Cpk tăng từ 0.9 lên 1.5 (đạt yêu cầu)\n→ Reject giảm 80%\n→ Bài học: Không cần đo từng cuộn ống — chỉ cần theo dõi biểu đồ SPC online, khi phát hiện pattern shift → kiểm tra nhiệt barrel ngay."
        },
        {
            "title": "Độ cứng viên thuốc Paracetamol",
            "industry": "Dược phẩm",
            "situation": "Viên nén Paracetamol: độ cứng (hardness) tiêu chuẩn 8-12 kP (kilopond — đơn vị đo lực nén). Biến động lớn giữa các mẻ (batch) — mẻ này cứng mẻ kia mềm. Viên quá mềm vỡ khi vận chuyển, quá cứng không tan khi uống.",
            "analysis": "Vẽ biểu đồ X̄-S chart (lấy 10 viên/mẻ, dùng S chart vì n≥10):\n• Trung bình X̄ = 9.8 kP, S̄ = 1.2 kP\n• Cpk = 0.56 — rất thấp!\n• Phát hiện pattern: Khi thay lô hạt (granule — bột đã tạo hạt) mới → độ cứng dịch chuyển (shift down). Nguyên nhân: Độ ẩm hạt giữa các lô trộn không nhất quán — lô khô hơn → viên mềm hơn. Lô ẩm hơn → viên cứng hơn",
            "result": "Hành động:\n• Kiểm soát độ ẩm hạt TRƯỚC KHI dập viên bằng máy đo NIR inline (Near-Infrared — hồng ngoại gần, đo ẩm không tiếp xúc). Nếu ẩm ngoài khoảng cho phép → chỉnh lại thời gian sấy\n• Lực dập viên tự động điều chỉnh (auto-adjust compression force) theo tín hiệu ẩm\n→ Cpk tăng từ 0.56 lên 1.35. Không mẻ nào bị reject.\n→ Quan trọng trong ngành dược: SPC là bằng chứng GMP cho thanh tra (auditor) thấy quá trình LUÔN kiểm soát được."
        },
        {
            "title": "Tỷ lệ lỗi hàn SMT (bảng mạch điện tử)",
            "industry": "Điện tử",
            "situation": "Tỷ lệ lỗi hàn (defect rate) trên dây chuyền SMT dao động từ 0.1% đến 2.5% — rất không ổn định. Mục tiêu duy trì dưới 0.3%.",
            "analysis": "Vẽ biểu đồ p-chart (tỷ lệ lỗi theo ngày):\n• Tỷ lệ lỗi trung bình p̄ = 0.8%, UCL = 1.6%, LCL = 0.0%\n• Phát hiện: 5 điểm liên tiếp vượt UCL ở tuần thứ 3 → BÁO ĐỘNG! Biến động bất thường\n• Điều tra nguyên nhân đặc biệt (special cause):\n1) Cảm biến nhiệt (thermocouple) zone 3 lò hàn reflow bị trôi → nhiệt độ thực cao hơn hiển thị → kem hàn chảy quá mức\n2) Kem hàn (solder paste) đã quá hạn sử dụng (expired) 10 ngày nhưng không ai kiểm tra vì không có hệ thống FIFO",
            "result": "Hành động:\n• Thay thermocouple + hiệu chuẩn nhiệt tất cả zone lò reflow\n• Áp dụng FIFO (First In First Out — nhập trước xuất trước) cho kem hàn + dán nhãn ghi ngày mở hộp, hạn sử dụng ngay khi mở\n→ Biểu đồ p-chart ổn định tại mức 0.3% sau cải tiến\n→ Bài học: Không ai ngờ 2 vấn đề nhỏ (cảm biến trôi + kem hàn hết hạn) lại xảy ra CÙNG LÚC gây spike defect. SPC phát hiện thời điểm chính xác để điều tra."
        },
        {
            "title": "Thể tích chiết rót nước giải khát",
            "industry": "Đồ uống",
            "situation": "Chai nước 500 ml, dung sai ±5 ml. Chiết nhiều quá (overfill) → tốn chi phí. Chiết ít quá (underfill) → vi phạm pháp luật bảo vệ người tiêu dùng. Cần cân bằng giữa 2 rủi ro.",
            "analysis": "Vẽ biểu đồ X̄-R (lấy 5 chai mỗi 30 phút):\n• Trung bình X̄ = 503 ml → Lệch lên +3 ml! Máy đang chiết thừa\n• Biên độ R̄ = 4 ml, Cpk = 1.0 (vừa đủ nhưng rủi ro)\n• Phân tích: Quá trình lệch tâm (off-center) → mỗi chai thừa 3 ml. Với sản lượng 100,000 chai/ngày × 3 ml = 300 lít nước ngọt bị cho thêm miễn phí/ngày!\n• Quy ra tiền: Lãng phí overfill ≈ 200 triệu VND/năm",
            "result": "Hành động:\n• Chỉnh thời gian chiết (filler timing) — giảm nhẹ để đưa trung bình về 500.5 ml (vẫn hơi dương để an toàn pháp lý)\n• Giảm biến động: hiệu chuẩn đồng hồ đo lưu lượng (flow meter) + bảo trì van chiết (filler valve) — thay seal van bị mòn gây rỉ\n→ X̄ = 500.5 ml (gần target), Cpk tăng lên 1.5\n→ Tiết kiệm 180 triệu VND/năm chỉ bằng việc chỉnh đúng tâm (centering)"
        },
        {
            "title": "Chiều dày lớp sơn Clear Coat ô tô",
            "industry": "Ô tô",
            "situation": "Sơn lớp phủ bóng (clear coat — lớp sơn trong suốt bảo vệ trên cùng) tiêu chuẩn 35-50 μm (micromet). Tỷ lệ sửa lại (rework) cao: quá dày (chảy sơn, da cam), quá mỏng (không bóng, dễ tróc).",
            "analysis": "Vẽ biểu đồ X̄-R chart:\n• X̄ = 44 μm (lệch về phía dày), R̄ = 8 μm (biến động lớn)\n• Cpk = 0.8 — không đạt yêu cầu (cần ≥1.33)\n• Phát hiện pattern đặc biệt:\n- Dao động theo chu kỳ (cyclic) tương quan với thay đổi độ ẩm trong ngày — sáng ẩm cao → sơn khô chậm → phun dày hơn\n- Run of 7 (7 điểm liên tiếp) nằm dưới đường trung tâm vào buổi sáng sớm → buổi sáng sơn mỏng hơn do súng phun chưa ấm",
            "result": "Hành động:\n• Kiểm soát HVAC (hệ thống điều hòa/thông gió) phòng sơn — giữ nhiệt độ và độ ẩm ổn định suốt ngày, không để dao động theo thời tiết\n• Bù lưu lượng sơn (flow rate compensation) tự động theo độ ẩm — khi ẩm cao giảm bớt lượng phun, ẩm thấp tăng\n→ Cpk tăng từ 0.8 lên 1.6. Rework giảm 75%\n→ Bài học: SPC pattern (dao động theo chu kỳ) giúp chỉ ra nguyên nhân là yếu tố MÔI TRƯỜNG (ẩm), không phải MÁY."
        },
        {
            "title": "Số lỗi trên tấm kính float",
            "industry": "Kính",
            "situation": "Kính nổi (float glass): tiêu chuẩn tối đa 3 điểm lỗi/m² (bọt khí, vết sọc, cặn). Thực tế dao động 0-12 lỗi/m² — rất không ổn định.",
            "analysis": "Vẽ biểu đồ c-chart (đếm số lỗi trên mỗi tấm kính):\n• Trung bình c̄ = 4.2 lỗi/m², UCL = 10.3\n• 2 điểm vượt UCL → biến động bất thường\n• Điều tra: Khi tin (thiếc lỏng trong bể tin bath) bị tràn → tạo vết trên bề mặt kính. Và: Số lỗi tăng mỗi lần thay top roller (con lăn trên) → lắp không thẳng hàng gây xước kính",
            "result": "Hành động:\n• Cải thiện kiểm soát mức thiếc lỏng trong bể tin bath — lắp cảm biến mức chính xác\n• Quy trình alignment (chỉnh thẳng hàng) top roller sau mỗi lần thay — dùng laser alignment tool\n→ Trung bình c̄ giảm từ 4.2 xuống 2.1 lỗi/m²\n→ Tiết kiệm hàng tỷ đồng/năm (kính lỗi phải nấu lại hoặc bán hạ cấp)."
        },
        {
            "title": "Momen siết nắp chai (Torque)",
            "industry": "Thực phẩm",
            "situation": "Momen siết nắp chai nước mắm: tiêu chuẩn 15-25 in-lb (đơn vị lực xoắn). Nắp lỏng → rò rỉ nước mắm khi vận chuyển. Nắp quá chặt → khách hàng không mở được.",
            "analysis": "Vẽ biểu đồ X̄-R chart:\n• Trung bình X̄ = 21 in-lb, R̄ = 5 in-lb\n• UCL = 23.9, LCL = 18.1\n• Phát hiện: 4 điểm liên tiếp vượt UCL → nắp ngày càng chặt!\n• Điều tra: Chuck (đầu kẹp nắp trên máy siết) bị mòn → kẹp không chắc → máy tự tăng lực bù → overtorque (siết quá mức)",
            "result": "Hành động:\n• Thay chuck mới + chỉnh lại giá trị momen cài đặt\n• Lắp thiết bị đo momen online (online torque monitoring) — tự động báo động nếu torque vượt giới hạn\n→ Cpk tăng từ 0.8 lên 1.8. Reject giảm 90%\n→ Bài học: 4 điểm liên tiếp tăng trên control chart = cảnh báo sớm chuck mòn, XỬ LÝ TRƯỚC khi giao hàng nắp quá chặt cho khách."
        },
        {
            "title": "pH nước thải — Kiểm soát môi trường",
            "industry": "Hóa chất",
            "situation": "Tiêu chuẩn pH nước thải xả ra 6.5-8.5 (quy định pháp luật). Vi phạm → phạt 500 triệu, đình chỉ sản xuất. Cần giám sát liên tục.",
            "analysis": "Vẽ biểu đồ I-MR (đo pH liên tục bằng sensor online):\n• Trung bình pH = 7.2, biên độ di chuyển MR̄ = 0.4\n• Phát hiện xu hướng (trend): pH giảm dần khi mẻ sản xuất acid chạy — dung dịch acid rò vào bể trung hòa\n• 2 điểm giảm dưới LCL → gần vi phạm pháp luật!\n• Nguyên nhân: Bơm trung hòa (neutralization pump) bị yếu — không bơm đủ kiềm NaOH để trung hòa acid",
            "result": "Hành động:\n• Đại tu bơm trung hòa (thay impeller, seal) — phục hồi lưu lượng\n• Hệ thống điều khiển pH tự động (auto pH control) — đo pH online, tự bơm kiềm khi pH giảm\n• Cài đặt cảnh báo sớm (early warning) tại pH 6.8 — còn 0.3 đơn vị cách giới hạn, cho nhân viên 15 phút xử lý\n→ pH duy trì ổn định 7.0-7.5, không vi phạm suốt 12 tháng."
        },
        {
            "title": "Kích thước hạt bột mì",
            "industry": "Thực phẩm",
            "situation": "Bột mì xay: kích thước hạt D50 (kích thước trung vị — 50% hạt nhỏ hơn, 50% lớn hơn) tiêu chuẩn 60-80 μm. Biến động lớn giữa các ca và mẻ nghiền → bột không đều, khách hàng (nhà làm bánh) phàn nàn.",
            "analysis": "Vẽ biểu đồ X̄-R chart:\n• X̄ = 72 μm, R̄ = 12 μm (biến động rất lớn)\n• Cpk = 0.67 — quá trình không đủ năng lực\n• Phát hiện biến động bất thường: Khi lưới sàng (screen) bị rách mà không phát hiện → hạt quá lớn lọt qua → D50 tăng đột ngột\n• Pattern: Shift (dịch chuyển trung bình) xảy ra chủ yếu ở Ca B → Ca B có vấn đề",
            "result": "Hành động:\n• Bảng kiểm tra lưới sàng (checklist) đầu mỗi ca — nhân viên phải kiểm tra bằng mắt và ghi nhận\n• Lắp máy đo kích thước hạt online (online particle size analyzer) — cảnh báo ngay khi D50 vượt giới hạn\n• Đào tạo bổ sung Ca B — chỉnh thông số nghiền chưa đúng\n→ Cpk tăng từ 0.67 lên 1.3."
        },
        {
            "title": "Định lượng giấy (gram/m²)",
            "industry": "Giấy",
            "situation": "Giấy in A4 tiêu chuẩn 80 gsm (gram/m²) ±3 gsm. Biến động theo chiều ngang tờ giấy (cross-direction) — mép giấy dày hơn giữa. Gây kẹt giấy trong máy in.",
            "analysis": "Vẽ biểu đồ X̄-R theo 8 vị trí đo chiều ngang:\n• Profile trung bình: mép giấy 83 gsm, giữa giấy 78 gsm → chênh 5 gsm!\n• Độ lệch chuẩn chiều ngang σ_cross = 2.5 gsm\n• Cpk = 0.5 — rất kém\n• Nguyên nhân: Hệ thống pha loãng bột (dilution headbox — phun thêm nước trắng vào vùng dày để cân bằng) phân phối không đều → mép giấy nhận ít nước hơn → dày hơn",
            "result": "Hành động:\n• Chỉnh bộ phận pha loãng (dilution profiling) — tăng lưu lượng nước pha loãng ở mép\n• Tinh chỉnh khe phun bột (slice lip) — mở rộng nhẹ ở giữa để bù\n• Dùng máy đo định lượng quét ngang (beta-gauge scanner) phản hồi tự động → hệ thống tự chỉnh khe phun theo đo thực tế\n→ Biến động chiều ngang giảm 60%. Cpk tăng từ 0.5 lên 1.2."
        },
        {
            "title": "Giới hạn chảy thép (Yield Strength)",
            "industry": "Thép",
            "situation": "Thép xây dựng: Giới hạn chảy (Yield Strength — lực kéo khiến thép bắt đầu biến dạng vĩnh viễn) tiêu chuẩn 350-450 MPa. Kết quả thử kéo không ổn định giữa các mẻ nấu.",
            "analysis": "Vẽ biểu đồ X̄-S chart (lấy 5 mẫu/mẻ nấu):\n• Trung bình X̄ = 395 MPa, S̄ = 22 MPa\n• Cpk = 0.83 — chưa đạt\n• Phân tích tương quan (correlation): Giới hạn chảy giảm khi hàm lượng Mangan (Mn) trong thép thấp. Mn là nguyên tố hợp kim quan trọng giúp thép chắc hơn\n• Nguyên nhân đặc biệt: Thời điểm thêm hợp kim (alloy addition timing) không nhất quán — có khi thêm sớm (bị cháy mất), có khi thêm muộn (chưa tan hết)",
            "result": "Hành động:\n• Chuẩn hóa thời điểm thêm hợp kim — quy định thêm Mn tại nhiệt độ chính xác sau khi khử oxy\n• Kiểm soát tốc độ nạp dây hợp kim (wire feeding rate) — tốc độ ổn định giúp Mn phân bố đều\n→ Cpk tăng từ 0.83 lên 1.4. Mọi mẻ thép đều đạt spec."
        },
        {
            "title": "Nhiệt độ hấp tiệt trùng thực phẩm đóng hộp",
            "industry": "Thực phẩm",
            "situation": "Lò hấp tiệt trùng (retort) thực phẩm đóng hộp: nhiệt độ yêu cầu 121°C ±1°C. ĐÂY LÀ THÔNG SỐ AN TOÀN THỰC PHẨM — nếu nhiệt không đủ → vi khuẩn sống → ngộ độc → thu hồi sản phẩm (recall).",
            "analysis": "Vẽ biểu đồ I-MR theo dõi liên tục (real-time):\n• Trung bình = 121.2°C, MR̄ = 0.5°C\n• Phát hiện: 1 điểm tụt xuống 119.5°C — vượt dưới LCL → VI PHẠM quy trình an toàn!\n• Điều tra nguyên nhân: Bẫy hơi (steam trap — thiết bị tự xả nước ngưng) bị hỏng → nước ngưng tụ không thoát → chiếm chỗ hơi nóng → nhiệt độ giảm trong giai đoạn giữ nhiệt (hold time)",
            "result": "Hành động:\n• Bảo trì bẫy hơi (steam trap PM) mỗi 3 tháng — kiểm tra chức năng, thay nếu kẹt\n• Lắp thêm cảm biến nhiệt dự phòng (redundant temperature sensor) — nếu 1 sensor hỏng vẫn có cái thứ 2\n• Cài báo động tự động tại 120.5°C (cách giới hạn 0.5°C) → nhân viên có thời gian xử lý trước khi vi phạm\n→ 12 tháng liên tục không vi phạm nhiệt độ. Đây là ứng dụng SPC quan trọng nhất trong an toàn thực phẩm — 1 điểm ngoài giới hạn có thể ảnh hưởng sức khỏe người tiêu dùng."
        },
        {
            "title": "Tỷ lệ phế phẩm theo ngày — Phát hiện pattern",
            "industry": "Sản xuất chung",
            "situation": "Tỷ lệ phế phẩm (scrap rate) trung bình 4%, nhưng có ngày vọt lên 8-10%. Ban giám đốc: 'Tại sao có ngày lên cao vậy?' — không ai giải thích được vì xảy ra 'ngẫu nhiên'.",
            "analysis": "Vẽ biểu đồ p-chart theo ngày:\n• Trung bình p̄ = 4.2%, UCL = 6.8%\n• 8 điểm vượt UCL — kiểm tra: TẤT CẢ đều rơi vào ngày THỨ HAI hoặc ngày đầu tiên sau kỳ nghỉ lễ!\n• Đây KHÔNG phải ngẫu nhiên — có nguyên nhân rõ ràng\n• Điều tra: Sau nghỉ cuối tuần, máy nguội, dầu bôi trơn đông đặc, tham số máy trôi → sản phẩm đầu ngày Monday chưa đạt (startup loss). Nhân viên vận hành không có quy trình warm-up cụ thể",
            "result": "Hành động:\n• SOP khởi động mở rộng ngày Thứ 2 (extended warm-up Monday SOP): Chạy máy không tải 30 phút trước khi sản xuất. Kiểm tra tham số (nhiệt, áp, tốc độ) đạt ổn định mới chạy\n• Bảng kiểm tra trước sản xuất (pre-production check) bắt buộc sau mỗi kỳ nghỉ\n→ Scrap rate ngày Thứ 2 giảm từ 8% xuống 4.5% (gần bằng ngày bình thường)\n→ Bài học tuyệt vời: Biểu đồ p-chart vạch trần pattern 'thứ Hai lỗi nhiều' mà cảm tính không nhận ra. Data doesn't lie!"
        },
        {
            "title": "Độ nhớt sơn nước",
            "industry": "Sơn",
            "situation": "Sơn nước nội thất: độ nhớt (viscosity — đo mức 'đặc' của sơn) tiêu chuẩn 85-95 KU (Krebs Unit). Biến động giữa các mẻ trộn gây khó thi công — mẻ đặc quá, mẻ loãng quá.",
            "analysis": "Vẽ biểu đồ X̄-R chart (lấy 3 mẫu/mẻ):\n• Trung bình X̄ = 91 KU (hơi lệch lên), R̄ = 5 KU\n• Cpk = 0.8 — chưa đạt\n• Biến động bất thường 1: Khi thêm cellulose (chất tạo đặc — giúp sơn có độ nhớt mong muốn) ở nhiệt độ sai → một số mẻ cellulose không tan hết → vón cục → độ nhớt không đồng nhất\n• Biến động bất thường 2: Run of 7 trên CL khi sử dụng nguyên liệu cellulose từ NCC mới → nguyên liệu NCC mới có đặc tính khác",
            "result": "Hành động:\n• Chuẩn hóa quy trình thêm cellulose: Thêm tại nhiệt độ 40°C + khuấy đều 20 phút trước khi thêm nguyên liệu tiếp theo (trước kia thêm bất kỳ lúc nào)\n• Kiểm tra đầu vào (IQC) cellulose từ NCC mới — đo độ nhớt mẫu thử trước khi chấp nhận lô\n→ Cpk tăng từ 0.8 lên 1.5. Không còn mẻ sơn phải pha lại."
        },
        {
            "title": "Thời gian lắp ráp — Phát hiện chênh lệch tay nghề",
            "industry": "Điện tử",
            "situation": "Thời gian lắp ráp (cycle time) mỗi sản phẩm: mục tiêu 45 giây ±5 giây. Biến động lớn giữa các nhân viên gây mất cân bằng dây chuyền — trạm chậm kéo lùi cả line.",
            "analysis": "Vẽ biểu đồ X̄-R PHÂN NHÓM theo từng nhân viên (operator):\n• Nhân viên A: X̄ = 43 giây (nhanh, ổn định) ✓\n• Nhân viên B: X̄ = 47 giây (chậm hơn 1 chút) △\n• Nhân viên C: X̄ = 52 giây (chậm nhất, vượt giới hạn trên!) ✗\n• Biến động GIỮA nhân viên >> biến động TRONG cùng 1 nhân viên\n→ Nghĩa là: Vấn đề không phải máy hoặc vật liệu, mà là CHÊNH LỆCH TAY NGHỀ",
            "result": "Hành động:\n• Phân tích Nhân viên C: Chưa thành thạo kỹ năng hàn (soldering) → thao tác lóng ngóng, mất thời gian\n• Đào tạo bổ sung (skill gap training) cho NV C — kèm cặp với NV A (người nhanh nhất)\n• Ghi video quy trình chuẩn (standardized work sequence video) để tất cả nhân viên thao tác giống nhau\n• Đặt đồng hồ bấm giờ trực quan (visual timing target) tại mỗi trạm\n→ Tất cả nhân viên đạt 43-47 giây. Cân bằng dây chuyền cải thiện 15%."
        }
    ]
}
