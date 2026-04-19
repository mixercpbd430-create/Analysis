method = {
    "id": 23,
    "title": "OEE Analysis - Phân tích hiệu suất thiết bị tổng thể",
    "short_name": "OEE Analysis",
    "icon": "📈",
    "pillar": "Planned Maintenance",
    "description": "Đo lường và phân tích hiệu suất thiết bị tổng thể (Overall Equipment Effectiveness) qua 3 yếu tố: Availability × Performance × Quality.",
    "meaning": """
<p><strong>OEE (Overall Equipment Effectiveness - Hiệu suất thiết bị tổng thể)</strong> là chỉ số đo lường mức độ hiệu quả thực sự của thiết bị sản xuất. OEE là KPI nền tảng trong TPM, cho biết bao nhiêu phần trăm thời gian sản xuất thực sự tạo ra sản phẩm tốt.</p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Công thức OEE</div>
    <p><strong>OEE = Availability × Performance × Quality</strong><br>
    <strong>A (Khả dụng)</strong> = Thời gian chạy thực / Thời gian kế hoạch × 100% — <em>Máy chạy được bao lâu so với kế hoạch?</em><br>
    <strong>P (Hiệu năng)</strong> = Sản lượng thực / Sản lượng lý thuyết × 100% — <em>Máy chạy có đạt tốc độ thiết kế không?</em><br>
    <strong>Q (Chất lượng)</strong> = Sản phẩm tốt / Tổng sản phẩm × 100% — <em>Bao nhiêu sản phẩm đạt chất lượng?</em><br><br>
    OEE đẳng cấp thế giới (World Class): <strong>85%</strong> (A≥90% × P≥95% × Q≥99%)<br>
    Thực tế hầu hết nhà máy: <strong>60-65%</strong> — nghĩa là mất 35-40% năng lực sản xuất!</p>
</div>
""",
    "purpose": """
<ul>
    <li>Đo lường chính xác hiệu suất thực tế của thiết bị (máy thực sự làm việc hiệu quả bao nhiêu phần trăm)</li>
    <li>Xác định và phân loại các tổn thất: dừng máy, chạy chậm, hay phế phẩm là vấn đề lớn nhất</li>
    <li>So sánh hiệu suất giữa các máy, các ca, các nhà máy để tìm best practice</li>
    <li>Theo dõi hiệu quả cải tiến theo thời gian — OEE tăng nghĩa là cải tiến có hiệu quả</li>
    <li>Là KPI nền tảng cho hoạt động TPM, mọi hoạt động cải tiến đều phản ánh qua OEE</li>
    <li>Hỗ trợ quyết định: cần đầu tư máy mới hay cải tiến máy hiện tại?</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Thu thập dữ liệu vận hành</div>
        <div class="step-card__desc">Ghi nhận hàng ca/ngày: thời gian chạy kế hoạch, thời gian dừng máy (chia rõ: dừng kế hoạch như PM hay dừng đột xuất như hỏng máy), sản lượng thực tế so với thiết kế, số lượng sản phẩm tốt và phế phẩm.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Tính Availability (Tỷ lệ khả dụng)</div>
        <div class="step-card__desc">A = Thời gian chạy thực / Thời gian kế hoạch. Thời gian mất đi do: hỏng máy (breakdown), chuyển đổi sản phẩm (changeover), thiếu nguyên liệu, điều chỉnh máy. Lưu ý: Thời gian bảo trì kế hoạch (PM), nghỉ trưa không tính vào thời gian kế hoạch.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Tính Performance (Tỷ lệ hiệu năng)</div>
        <div class="step-card__desc">P = Sản lượng thực tế / Sản lượng lý thuyết (ở tốc độ thiết kế). Phản ánh tổn thất tốc độ: máy chạy chậm hơn thiết kế, dừng nhỏ ngắn (micro-stops dưới 5 phút, ví dụ kẹt vật liệu rồi tự chạy lại), máy chạy không tải (idling).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Tính Quality (Tỷ lệ chất lượng)</div>
        <div class="step-card__desc">Q = Sản phẩm đạt chất lượng / Tổng sản phẩm. Bao gồm tổn thất: phế phẩm (scrap), sản phẩm cần sửa lại (rework), hao hụt khi khởi động máy (startup loss — khi mới chạy máy, sản phẩm đầu thường chưa đạt).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">5</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 5: Tính OEE và phân tích để cải tiến</div>
        <div class="step-card__desc">OEE = A × P × Q. Nhìn vào yếu tố nào thấp nhất → đó là ưu tiên cải tiến. Ví dụ: nếu A thấp → tập trung giảm dừng máy; nếu P thấp → tìm nguyên nhân chạy chậm; nếu Q thấp → tập trung giảm phế phẩm. Dùng biểu đồ Pareto để xác định nguyên nhân chính.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Máy ép viên (Pellet Mill) nhà máy TACN",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy ép viên chạy 20 giờ/ngày. Tổng thời gian dừng máy 3 giờ, gồm: nứt die (khuôn ép) phải thay mất 1.5 giờ, chuyển đổi code sản phẩm 1 giờ, chờ nguyên liệu 0.5 giờ. Công suất thiết kế 40 tấn/giờ nhưng thực tế chỉ đạt 32 tấn/giờ. Tổng sản lượng 544 tấn, trong đó 15 tấn phế phẩm (viên vỡ, viên bở không đạt PDI).",
            "analysis": "Tính OEE:\n• A (Khả dụng) = 17/20 = 85% — máy dừng mất 3 giờ trong 20 giờ kế hoạch\n• P (Hiệu năng) = 32/40 = 80% — máy chỉ chạy 80% công suất thiết kế, chạy chậm do die mòn\n• Q (Chất lượng) = 529/544 = 97.2% —2.8% sản phẩm bị vỡ/bở không đạt\n• OEE = 85% × 80% × 97.2% = 66.1%\n→ Hiệu năng (P) là yếu tố thấp nhất, cần ưu tiên cải tiến tốc độ chạy máy.",
            "result": "Tập trung cải tiến Performance (hiệu năng):\n• Theo dõi tuổi thọ die — thay die đúng chu kỳ trước khi mòn quá mức làm giảm tốc độ\n• Tối ưu điều kiện steam conditioning (nhiệt độ hơi, áp suất) giúp nguyên liệu dẻo hơn, ép nhanh hơn\n→ P tăng từ 80% lên 90%. OEE mới = 85% × 90% × 97.2% = 74.4% (tăng 8.3%). Quy ra sản lượng: tăng khoảng 50 tấn/ngày."
        },
        {
            "title": "Line đóng bao tự động",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy đóng bao FFS (Form-Fill-Seal - tạo bao, nạp liệu, hàn miệng tự động): kế hoạch chạy 16 giờ/ngày. Dừng máy tổng 2.5 giờ gồm: film (màng bao) bị kẹt 1 giờ, chuyển đổi sản phẩm 0.5 giờ, sealer (thanh hàn miệng bao) bị cháy phải sửa 1 giờ. Tốc độ thực tế 12 bao/phút nhưng thiết kế 15 bao/phút. Tổng đóng được 9720 bao, trong đó 280 bao bị lỗi seal (miệng bao hàn không kín).",
            "analysis": "Tính OEE:\n• A = 13.5/16 = 84.4% — dừng máy 2.5 giờ, chủ yếu do kẹt film và hỏng sealer\n• P = 12/15 = 80% — máy chạy chậm hơn thiết kế 20%, do film căng không đều và dao cắt cùn\n• Q = 9440/9720 = 97.1% — 2.9% bao bị lỗi hàn miệng\n• OEE = 84.4% × 80% × 97.1% = 65.6%\n→ Cả Availability và Performance đều thấp, cần cải tiến đồng thời.",
            "result": "Cải tiến song song A và P:\n• A: Bảo trì định kỳ thanh hàn sealer (thay điện trở, vệ sinh bề mặt) + đào tạo thao tác xử lý kẹt film nhanh cho operator\n• P: Thay dao cắt film đúng chu kỳ + lắp bộ điều khiển lực căng film (tension controller) tự động\n→ A tăng lên 90%, P tăng lên 88%. OEE mới = 76.9%. Tương đương tăng thêm ~2400 bao/ngày."
        },
        {
            "title": "Máy trộn (Mixer) theo mẻ",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy trộn 3 tấn/mẻ, thời gian 1 chu kỳ trộn lý thuyết 4 phút/mẻ. Kế hoạch chạy 480 phút/ca. Thực tế chỉ trộn được 100 mẻ/ca (trong khi lý thuyết phải đạt 120 mẻ). 3 mẻ bị nhầm công thức (formula) phải đổ bỏ trộn lại.",
            "analysis": "Tính OEE:\n• A = (480-35)/480 = 92.7% — dừng 35 phút do chờ nguyên liệu về bin và thời gian vệ sinh máy trộn\n• P = 100/120 = 83.3% — chỉ đạt 83% số mẻ thiết kế, do chờ cân vi lượng và cửa xả chậm\n• Q = 97/100 = 97% — 3 mẻ bị sai công thức phải làm lại\n• OEE = 92.7% × 83.3% × 97% = 74.9%",
            "result": "Cải tiến:\n• P (Hiệu năng): Chuẩn bị cân sẵn nguyên liệu vi lượng (premix, amino acid) trước khi mẻ trước xong + sửa cửa xả bị kẹt cho mở nhanh hơn\n• Q (Chất lượng): Kiểm tra chéo công thức trên màn hình HMI trước khi trộn — hiển thị rõ tên sản phẩm và thành phần\n→ Mục tiêu OEE 82%."
        },
        {
            "title": "Máy nghiền búa (Hammer Mill)",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy nghiền búa nghiền ngô: kế hoạch chạy 20 giờ. Tổng dừng máy 4 giờ gồm: thay lưới sàng mất 1.5 giờ, thay búa nghiền mòn 2 giờ, kẹt nguyên liệu (ngô ướt bị tắc) 0.5 giờ. Công suất thiết kế 35 tấn/giờ nhưng thực tế chỉ đạt 25 tấn/giờ do búa mòn. Chất lượng nghiền: 5% hạt quá cỡ (oversize - không lọt qua lưới, phải nghiền lại).",
            "analysis": "Tính OEE:\n• A = 16/20 = 80% — mất 4 giờ dừng máy, riêng thay búa đã mất 2 giờ\n• P = 25/35 = 71.4% — máy chỉ đạt 71% công suất vì búa mòn, lực nghiền yếu\n• Q = 95% — 5% sản phẩm quá cỡ phải nghiền lại\n• OEE = 80% × 71.4% × 95% = 54.3% — rất thấp!\n→ Performance (71.4%) là vấn đề lớn nhất — búa mòn khiến máy nghiền chậm.",
            "result": "Cải tiến theo thứ tự ưu tiên:\n• P: Quản lý tuổi thọ búa — xoay búa 4 mặt trước khi thay mới, thay đúng chu kỳ trước khi mòn quá mức\n• A: Áp dụng SMED (chuyển đổi nhanh) cho việc thay lưới: chuẩn bị lưới mới sẵn, dùng kẹp nhanh thay vì bu-lông → giảm từ 1.5 giờ xuống 0.5 giờ\n• Q: Kiểm tra lưới sàng có bị rách/thủng không (gây lọt hạt to qua)\n→ Mục tiêu OEE 70%. Tương đương tăng thêm ~80 tấn/ngày sản lượng."
        },
        {
            "title": "Robot hàn khung xe hơi",
            "industry": "Ô tô",
            "situation": "Robot hàn tự động chạy 22 giờ/ngày. Dừng máy tổng 3 giờ: chuyển đổi model xe mất 1.5 giờ (thay jig, nạp chương trình mới), robot báo lỗi phải reset 1 giờ, chờ linh kiện đưa tới 0.5 giờ. Nhịp sản xuất (takt time) lý thuyết 60 giây/xe nhưng thực tế 68 giây. Sản xuất 850 xe, 12 xe phải sửa lại mối hàn (rework).",
            "analysis": "Tính OEE:\n• A = 19/22 = 86.4% — dừng 3 giờ, trong đó chuyển đổi model là nhiều nhất\n• P = 60/68 = 88.2% — mỗi xe mất thêm 8 giây so với thiết kế, do đường di chuyển robot chưa tối ưu\n• Q = 838/850 = 98.6% — 1.4% xe phải rework do mối hàn xấu\n• OEE = 86.4% × 88.2% × 98.6% = 75.1%",
            "result": "Cải tiến:\n• P: Tối ưu đường chạy robot (path optimization) — giảm quãng đường di chuyển giữa các mối hàn → tiết kiệm 5 giây/xe\n• A: Áp dụng SMED cho chuyển đổi model — chuẩn bị jig sẵn + nạp chương trình tự động → giảm 1.5h xuống 0.5h\n• Q: Kiểm tra và mài đầu hàn (tip dress) đúng chu kỳ — đầu hàn mòn gây mối hàn yếu\n→ Mục tiêu OEE 82%."
        },
        {
            "title": "Máy ép nhựa (Injection Molding)",
            "industry": "Nhựa",
            "situation": "Máy ép nhựa 250 tấn chạy 24 giờ/ngày. Tổng dừng máy 5 giờ: thay khuôn (mold) mất 2 giờ, hỏng máy đột xuất 1.5 giờ, thay nhựa (đổi màu/loại nhựa) 1.5 giờ. Chu kỳ ép 30 giây/sản phẩm nhưng thiết kế là 25 giây. Tổng ép 2280 lần (shot), phế phẩm 95 sản phẩm (bị thiếu nhựa, ba-via, lõm bề mặt).",
            "analysis": "Tính OEE:\n• A = 19/24 = 79.2% — mất 5 giờ dừng máy, thay khuôn là lâu nhất\n• P = 25/30 = 83.3% — chu kỳ chậm hơn 5 giây, chủ yếu do thời gian làm nguội quá dài\n• Q = 2185/2280 = 95.8% — 4.2% phế phẩm\n• OEE = 79.2% × 83.3% × 95.8% = 63.2%",
            "result": "Cải tiến:\n• A: Hệ thống thay khuôn nhanh (quick mold change) — dùng kẹp thủy lực + connect nhanh nước, dầu → giảm từ 2 giờ xuống 30 phút\n• P: Tối ưu thời gian làm nguội — kiểm tra kênh nước đóng cặn, vệ sinh lại → giảm cooling từ 15 giây xuống 10 giây\n• Q: Kiểm tra đường thoát khí khuôn (venting) — bị tắc gây sản phẩm thiếu nhựa\n→ Mục tiêu OEE 75%."
        },
        {
            "title": "Dây chuyền chiết rót sữa UHT",
            "industry": "Thực phẩm",
            "situation": "Line chiết rót sữa UHT dạng hộp Tetra Pak: chạy 20 giờ/ngày. CIP (rửa vệ sinh tại chỗ) mất 2 giờ, chuyển đổi sản phẩm 1 giờ, các lần dừng ngắn (kẹt hộp, báo lỗi sensor) tổng 1.5 giờ. Tốc độ thực tế 8000 hộp/giờ, thiết kế 10000 hộp/giờ. Tổng chiết 88000 hộp, loại bỏ 1200 hộp lỗi seal (hàn miệng không kín).",
            "analysis": "Tính OEE:\n• A = 15.5/20 = 77.5% — mất 4.5 giờ, CIP chiếm nhiều nhất\n• P = 8000/10000 = 80% — chạy chậm hơn thiết kế 20%, do bộ nối băng chuyền không đồng bộ\n• Q = 86800/88000 = 98.6% — 1.4% hộp bị lỗi seal phải bỏ\n• OEE = 77.5% × 80% × 98.6% = 61.1% — khá thấp cho line hiện đại.",
            "result": "Cải tiến:\n• A: Tối ưu quy trình CIP — giảm thời gian rửa bằng cách tăng nhiệt độ hóa chất + dừng rửa khi nước hồi đạt chuẩn (không rửa theo thời gian cố định)\n• P: Thay bộ nối cuộn bao (splice unit) + chỉnh alignment băng chuyền → tốc độ ổn định hơn\n• Q: Bảo trì hàm hàn seal (thay điện trở, vệ sinh bề mặt ép) → giảm lỗi hàn\n→ Mục tiêu OEE 72%."
        },
        {
            "title": "Máy CNC phay 5 trục — Linh kiện hàng không",
            "industry": "Hàng không",
            "situation": "Máy CNC 5 trục gia công linh kiện máy bay: kế hoạch chạy 16 giờ/ngày. Thời gian chuẩn bị (setup gá đặt phôi) 3 giờ, thay dụng cụ cắt 1 giờ, chạy thử/kiểm tra chương trình 0.5 giờ. Tốc độ cắt chỉ đạt 70% so với tối ưu (do nhân viên lập trình chưa tối ưu đường chạy dao). 45 chi tiết gia công, 2 phế phẩm.",
            "analysis": "Tính OEE:\n• A = 11.5/16 = 71.9% — mất 4.5 giờ chuẩn bị, chủ yếu do setup phôi quá lâu (gá manual)\n• P = 70% — đường chạy dao chưa tối ưu, máy mất nhiều thời gian chạy không cắt\n• Q = 43/45 = 95.6% — 2 chi tiết bị quá dung sai phải loại bỏ\n• OEE = 71.9% × 70% × 95.6% = 48.1% — rất thấp, hơn nửa năng lực máy bị lãng phí!",
            "result": "Cải tiến:\n• A: Gá đặt phôi offline (chuẩn bị trên bàn gá riêng, khi máy còn đang chạy, xong thì lắp vào) + dùng tool presetter (đo dao sẵn ngoài máy, không mất thời gian đo trên máy)\n• P: Tối ưu chương trình CAM — rút ngắn đường chạy dao, tăng tốc cắt ở vùng an toàn\n• Q: Đo kiểm trong quá trình gia công (in-process measurement) — phát hiện sai số sớm, sửa ngay\n→ Mục tiêu OEE 65%."
        },
        {
            "title": "Máy dệt kim tròn",
            "industry": "Dệt may",
            "situation": "Máy dệt tròn chạy 24 giờ liên tục. Dừng máy tổng 6 giờ: thay kim dệt bị gãy mất 2 giờ (phải tháo nhiều kim xung quanh), sợi đứt phải nối lại mất 2.5 giờ (nhiều lần, mỗi lần 5-10 phút), chuyển đổi kiểu dệt 1.5 giờ. Tốc độ quay 25 vòng/phút nhưng thiết kế 30 vòng/phút. Dệt được 450 kg vải, 20 kg vải lỗi (lỗ kim, sọc ngang do đứt sợi).",
            "analysis": "Tính OEE:\n• A = 18/24 = 75% — dừng tới 6 giờ/ngày, chủ yếu do đứt sợi và gãy kim\n• P = 25/30 = 83.3% — máy chạy chậm hơn thiết kế do quality nhân viên lo lỗi nên giảm tốc\n• Q = 430/450 = 95.6% — 4.4% vải phải cắt bỏ do lỗi\n• OEE = 75% × 83.3% × 95.6% = 59.7%",
            "result": "Cải tiến:\n• A: Bảo trì kim dệt định kỳ (kiểm tra đầu kim mài mòn, thay trước khi gãy) + dùng sợi chất lượng ổn định hơn (ít đứt)\n• P: Tối ưu cam timing (bộ cam điều khiển chuyển động kim) → máy chạy ổn định ở tốc độ cao hơn\n• Q: Lắp hệ thống kiểm tra vải online (camera phát hiện lỗi ngay khi dệt, dừng kịp thời tránh dệt thêm vải lỗi)\n→ Mục tiêu OEE 70%."
        },
        {
            "title": "Máy in offset 4 màu",
            "industry": "In ấn",
            "situation": "Máy in offset 4 màu chạy 16 giờ/ngày, in 10 đơn hàng khác nhau. Mỗi lần chuyển đơn hàng (makeready — thay bản in, chỉnh màu, chỉnh giấy) mất 30 phút × 10 lần = 5 giờ! Tốc độ in 10,000 tờ/giờ nhưng thiết kế 15,000 tờ/giờ (chạy chậm vì sợ lệch màu). Tổng in 100,000 tờ, bỏ 4000 tờ waste (giấy chạy thử + lỗi màu).",
            "analysis": "Tính OEE:\n• A = 11/16 = 68.8% — mất tới 5 giờ cho makeready (31% thời gian!)\n• P = 10000/15000 = 66.7% — chạy rất chậm vì operator không tin tưởng tốc độ cao\n• Q = 96000/100000 = 96% — 4% giấy phải bỏ\n• OEE = 68.8% × 66.7% × 96% = 44% — cực kỳ thấp, hơn nửa năng lực máy lãng phí!\n→ Cả 3 yếu tố đều thấp, nhưng Performance tệ nhất.",
            "result": "Cải tiến:\n• A: Áp dụng SMED cho makeready — chuẩn bị bản in, pha mực sẵn khi máy còn chạy đơn trước → giảm từ 30 xuống 15 phút/lần\n• P: Hệ thống chỉnh màu tự động (CPC - Computer Print Control) + auto register (tự chỉnh chồng màu) → tin tưởng tăng tốc lên 13,000 tờ/giờ\n• Q: Camera kiểm tra chất lượng in inline — phát hiện lỗi ngay, dừng sớm tránh in thêm tờ lỗi\n→ Mục tiêu OEE 60%. Tăng từ 44% lên 60% = tương đương tăng 36% sản lượng."
        },
        {
            "title": "Nồi hơi (Boiler) công nghiệp",
            "industry": "Sản xuất chung",
            "situation": "Nồi hơi 10 tấn hơi/giờ: chạy 720 giờ/tháng. Dừng tổng 48 giờ gồm: bảo trì định kỳ PM 24 giờ, sửa chữa đột xuất 20 giờ, rò ống nước 4 giờ. Công suất hơi thực tế 8.5 tấn/giờ (dưới thiết kế 10T/h). Hiệu suất nhiệt chỉ đạt 82% (tiêu chuẩn 90% — nghĩa là 18% nhiệt lượng bị thất thoát).",
            "analysis": "Tính OEE (áp dụng cho utility):\n• A = 672/720 = 93.3% — khá tốt nhưng sửa chữa đột xuất 20 giờ là vấn đề\n• P = 8.5/10 = 85% — boiler không đạt công suất, do đóng cặn trong ống làm giảm trao đổi nhiệt\n• Q (hiệu suất nhiệt) = 82/90 = 91.1% — nhiệt thất thoát qua ống khói, vỏ boiler\n• OEE = 93.3% × 85% × 91.1% = 72.2%",
            "result": "Cải tiến:\n• P: Xử lý hóa chất nước cấp boiler (ngăn đóng cặn) + vệ sinh ống trao đổi nhiệt → phục hồi công suất\n• Q: Tối ưu tỷ lệ gió/nhiên liệu (air-fuel ratio) bằng phân tích O₂ ống khói → giảm thất thoát nhiệt\n• A: Lắp cảm biến rung (vibration) + camera nhiệt (thermal) để phát hiện sớm sự cố, sửa chữa chủ động thay vì chờ hỏng\n→ Mục tiêu OEE 80%."
        },
        {
            "title": "Máy đóng gói đứng VFFS — Snack",
            "industry": "Thực phẩm",
            "situation": "Máy VFFS (Vertical Form Fill Seal — tạo túi, nạp liệu, hàn bao theo phương đứng) đóng gói snack: chạy 16 giờ. Dừng 3 giờ gồm: film kẹt 1 giờ, chuyển sản phẩm 1 giờ, sửa thanh hàn sealer 1 giờ. Tốc độ 180 bao/phút nhưng thiết kế 250 bao/phút. Tổng 145,800 bao, 3500 bao lỗi hàn (bao bị hở, không kín).",
            "analysis": "Tính OEE:\n• A = 13/16 = 81.3% — dừng 3 giờ, phân bổ đều 3 nguyên nhân\n• P = 180/250 = 72% — chạy rất chậm so với thiết kế, vấn đề nghiêm trọng!\n• Q = 142300/145800 = 97.6% — 2.4% bao lỗi\n• OEE = 81.3% × 72% × 97.6% = 57.1%",
            "result": "Cải tiến:\n• P (ưu tiên #1, vì thấp nhất): Chỉnh bộ căng film (film tension) đúng thông số + chỉnh alignment hàm hàn (jaw alignment) + hiệu chỉnh servo motor → máy chạy nhanh mà ổn định\n• A: Thiết kế ống tạo hình (forming tube) thay nhanh cho từng kích thước bao → giảm thời gian chuyển đổi\n• Q: Lắp máy phát hiện rò rỉ online (leak detector) để loại ngay bao lỗi, không trộn vào hàng tốt\n→ Mục tiêu OEE 70%."
        },
        {
            "title": "Máy đùn ống nhựa HDPE",
            "industry": "Nhựa",
            "situation": "Máy đùn (extruder) ống nhựa HDPE: chạy 24 giờ liên tục. Dừng 4 giờ: thay đầu đùn (die) cho kích thước ống khác mất 2 giờ, xả nhựa cũ khi đổi màu (purge) 1 giờ, sửa chữa 1 giờ. Năng suất 180 kg/giờ nhưng thiết kế 250 kg/giờ. Tổng 3600 kg, phế phẩm 150 kg (ống bị méo, sai kích thước).",
            "analysis": "Tính OEE:\n• A = 20/24 = 83.3% — dừng 4 giờ, thay die lâu nhất\n• P = 180/250 = 72% — máy chạy chậm, do nhiệt độ barrel chưa tối ưu và trục vít (screw) mòn\n• Q = 3450/3600 = 95.8% — 4.2% phế phẩm do ống méo, sai đường kính\n• OEE = 83.3% × 72% × 95.8% = 57.5%",
            "result": "Cải tiến:\n• A: Hệ thống thay die nhanh (quick die change) + xả nhựa tự động (auto purge) → giảm downtime\n• P: Tối ưu thiết kế trục vít + điều chỉnh nhiệt độ từng vùng barrel → tăng năng suất đùn\n• Q: Đo đường kính ống online bằng máy đo laser → phát hiện ngay khi ống lệch kích thước, điều chỉnh kịp thời\n→ Mục tiêu OEE 70%."
        },
        {
            "title": "Máy đùn viên thức ăn thủy sản",
            "industry": "Thức ăn thủy sản",
            "situation": "Máy đùn (extruder) sản xuất viên thức ăn tôm cá nổi: kế hoạch 20 giờ. Dừng tới 5 giờ: chuyển đổi kích cỡ viên 2 giờ (thay die + chỉnh dao cắt), vệ sinh máy 1.5 giờ (thức ăn thủy sản dễ bám dính), sửa die bị tắc 1.5 giờ. Công suất 1.8 tấn/giờ nhưng thiết kế 2.5 tấn/giờ. Tổng 27 tấn, 2 tấn bị loại (viên vỡ, sai kích cỡ).",
            "analysis": "Tính OEE:\n• A = 15/20 = 75% — dừng máy chiếm 25% thời gian, quá nhiều!\n• P = 1.8/2.5 = 72% — máy chạy chậm do trục vít (screw) mòn và bộ tiền xử lý (preconditioner) hoạt động chưa tốt\n• Q = 25/27 = 92.6% — 7.4% phế phẩm, cao hơn bình thường\n• OEE = 75% × 72% × 92.6% = 50% — rất thấp, cả 3 yếu tố đều kém!",
            "result": "Cải tiến toàn diện (cả 3 yếu tố đều cần):\n• A: Áp dụng SMED cho thay die + thiết kế hệ thống CIP vệ sinh tự động → giảm 5 giờ dừng xuống 3 giờ\n• P: Thay trục vít mới (screw bị mòn giảm hiệu suất đùn) + tối ưu preconditioner (nhiệt + ẩm giúp nguyên liệu chín trước khi đùn, máy đùn nhẹ tải hơn)\n• Q: Sàng rung phân loại (vibrating screen) kích cỡ viên ngay sau đùn → loại viên sai size ngay\n→ Mục tiêu OEE 65%."
        },
        {
            "title": "Line lắp ráp bảng mạch SMT",
            "industry": "Điện tử",
            "situation": "Dây chuyền gắn linh kiện bề mặt SMT (Surface Mount Technology): chạy 16 giờ. Dừng 2.5 giờ: chuyển đổi sản phẩm 1.5 giờ (thay stencil, nạp feeder, đổi chương trình), feeder kẹt linh kiện 0.5 giờ, lỗi kem hàn 0.5 giờ. Tốc độ gắn 15,000 linh kiện/giờ nhưng thiết kế 20,000. Tổng 120,000 mối hàn, 180 mối lỗi.",
            "analysis": "Tính OEE:\n• A = 13.5/16 = 84.4% — chuyển đổi sản phẩm chiếm nhiều thời gian nhất\n• P = 15000/20000 = 75% — máy gắn chậm hơn thiết kế 25%, do feeder rung không đều và vòi hút (nozzle) bám bẩn\n• Q = 119820/120000 = 99.85% — chất lượng rất cao (ngành điện tử yêu cầu >99.5%)\n• OEE = 84.4% × 75% × 99.85% = 63.2%",
            "result": "Cải tiến:\n• P (ưu tiên #1): Bảo trì feeder định kỳ (vệ sinh rãnh dẫn linh kiện) + vệ sinh vòi hút nozzle hàng ca + tối ưu thứ tự gắn linh kiện (giảm quãng đường đầu gắn di chuyển)\n• A: Hệ thống trolley exchange (xe chứa feeder chuẩn bị sẵn, khi chuyển sản phẩm chỉ cần đẩy xe vào)\n→ Mục tiêu OEE 75%."
        },
        {
            "title": "Máy cán thép nguội (Cold Rolling Mill)",
            "industry": "Thép",
            "situation": "Máy cán nguội thép tấm chạy 24 giờ. Dừng 5 giờ: thay trục cán (roll) mất 3 giờ (phải tháo, vận chuyển roll nặng hàng tấn), thay cuộn thép (coil change) 1 giờ, sự cố đứt thép 1 giờ. Tốc độ cán 300 m/phút nhưng thiết kế 500 m/phút. Tổng cán 800 tấn, 25 tấn sai dung sai (off-gauge - quá dày/mỏng).",
            "analysis": "Tính OEE:\n• A = 19/24 = 79.2% — thay roll 3 giờ là tổn thất lớn nhất\n• P = 300/500 = 60% — cực kỳ thấp! Máy chỉ chạy 60% tốc độ thiết kế\n• Q = 775/800 = 96.9% — 3.1% thép sai kích thước\n• OEE = 79.2% × 60% × 96.9% = 46.1% — Performance là vấn đề nghiêm trọng nhất!",
            "result": "Cải tiến:\n• P (ưu tiên #1): Tối ưu hình dạng trục cán (roll crown) để tránh rung ở tốc độ cao + cải thiện hệ thống cooling (nước làm mát trục cán) + hiệu chỉnh bộ điều khiển chiều dày tự động (AGC - Automatic Gauge Control)\n• A: Hệ thống thay roll nhanh dạng cassette (cả cặp roll gắn sẵn trên khung, đưa vào-rút ra nhanh)\n• Q: Đo chiều dày liên tục bằng tia X (X-ray gauge) hồi tiếp trực tiếp về AGC → tự chỉnh ngay\n→ Mục tiêu OEE 62%."
        },
        {
            "title": "Máy cắt laser fiber",
            "industry": "Kim loại",
            "situation": "Máy cắt laser fiber 6kW: chạy 16 giờ. Dừng 3 giờ: nạp/dỡ tấm thép (loading/unloading) thủ công 1.5 giờ, thay đầu phun (nozzle) bị cháy 0.5 giờ, lập trình cắt trên máy 1 giờ. Tốc độ cắt chỉ đạt 70% so với tối ưu (do thông số cắt chưa hiệu chỉnh cho từng vật liệu). 480 chi tiết cắt, 10 phế phẩm (cắt sai, ba-via thô).",
            "analysis": "Tính OEE:\n• A = 13/16 = 81.3% — dừng 3 giờ, nạp/dỡ thủ công chiếm 1.5 giờ\n• P = 70% — chạy chậm do chưa tối ưu tốc độ cắt cho từng loại thép (dày/mỏng, inox/carbon steel)\n• Q = 470/480 = 97.9% — 2.1% phế phẩm\n• OEE = 81.3% × 70% × 97.9% = 55.7%",
            "result": "Cải tiến:\n• A: Lắp bàn nạp/dỡ tấm tự động (auto sheet changer) — máy cắt tấm này, hệ thống tự nạp tấm kế + dỡ thành phẩm, gần như không dừng. Lập trình nesting offline (trên máy tính riêng, không chiếm thời gian máy)\n• P: Tối ưu thông số cắt riêng cho từng vật liệu (công suất laser, tốc độ, áp suất khí thổi) dựa trên thử nghiệm và bảng tra\n• Q: Phát hiện lỗi đâm xuyên (pierce detection) tự động — nếu tia laser không xuyên thủng tấm thì dừng, tránh cắt hỏng\n→ Mục tiêu OEE 70%."
        },
        {
            "title": "Xe nâng điện trong kho",
            "industry": "Logistics",
            "situation": "Xe nâng điện hoạt động 16 giờ/ngày trong kho hàng. Thời gian mất: sạc pin 3 giờ, chờ hàng đến (xe đứng không) 2 giờ, sửa chữa nhỏ 0.5 giờ. Di chuyển được 180 pallet/ngày nhưng khả năng tối đa 280 pallet. Hư hại hàng hóa (va đập, rơi) 5 pallet.",
            "analysis": "Tính OEE (áp dụng cho thiết bị logistics):\n• A = 10.5/16 = 65.6% — mất tới 5.5 giờ! Sạc pin và chờ hàng chiếm nhiều nhất\n• P = 180/280 = 64.3% — xe di chuyển không hiệu quả, đi đường xa, chờ xếp/dỡ\n• Q = 175/180 = 97.2% — 5 pallet hư hại do lái ẩu hoặc xếp chồng sai\n• OEE = 65.6% × 64.3% × 97.2% = 41% — cực kỳ thấp, gần 60% năng lực bị lãng phí!",
            "result": "Cải tiến:\n• A: Hệ thống thay pin nhanh (battery swap - thay pin sạc sẵn thay vì đợi sạc tại chỗ) + phần mềm quản lý kho WMS tự phân công việc (giảm thời gian xe chờ không việc)\n• P: Tối ưu tuyến đường di chuyển (route optimization) + sắp xếp hàng theo ABC (hàng bán chạy để gần, ít đi xa)\n• Q: Đào tạo lái xe nâng an toàn + qui định chiều cao xếp chồng\n→ Mục tiêu OEE 60%."
        },
        {
            "title": "Máy đóng lon bia tự động",
            "industry": "Đồ uống",
            "situation": "Dây chuyền đóng lon bia: chạy 20 giờ. Dừng 3 giờ gồm: CIP rửa vệ sinh 1.5 giờ, lon kẹt trên băng chuyền 1 giờ, lỗi CO₂ (áp suất không ổn định) 0.5 giờ. Tốc độ 800 lon/phút nhưng thiết kế 1200 lon/phút. Tổng chiết 624,000 lon, loại bỏ 5000 lon (lỗi seal nắp, lỗi mức chiết).",
            "analysis": "Tính OEE:\n• A = 17/20 = 85% — tương đối ổn\n• P = 800/1200 = 66.7% — rất thấp, máy chạy chậm hơn 33% so với thiết kế!\n• Q = 619000/624000 = 99.2% — chất lượng ở mức chấp nhận\n• OEE = 85% × 66.7% × 99.2% = 56.2%\n→ Performance là vấn đề chính — tại sao máy không chạy nhanh được?",
            "result": "Cải tiến:\n• P (ưu tiên hàng đầu): Bảo trì van chiết (filler valve) — vệ sinh, thay seal → dòng chảy bia ổn định ở tốc độ cao. Cải thiện hệ thống dẫn lon (can handling guides) — lon không bị đổ/kẹt khi di chuyển nhanh\n• A: Tối ưu quy trình CIP (rút ngắn bước rửa cuối) + lắp sensor phát hiện lon kẹt sớm để xử lý nhanh\n• Q: Kiểm tra mí ghép lon (seam inspection) bằng camera → phát hiện lỗi seal ngay\n→ Mục tiêu OEE 72%."
        },
        {
            "title": "Máy ép kính pin mặt trời (Solar Laminator)",
            "industry": "Năng lượng",
            "situation": "Máy ép nhiệt (laminator) tấm pin mặt trời: chạy 20 giờ. Dừng 4 giờ gồm: thay chương trình ép cho sản phẩm khác 1.5 giờ, bơm chân không bị lỗi 1.5 giờ, vệ sinh bề mặt ép 1 giờ. Chu kỳ ép 18 phút/tấm nhưng thiết kế 12 phút. Ép 53 tấm, 2 tấm bị tách lớp (delamination - các lớp vật liệu không dính kết).",
            "analysis": "Tính OEE:\n• A = 16/20 = 80% — bơm chân không lỗi gây dừng đáng kể\n• P = 12/18 = 66.7% — chu kỳ ép lâu hơn 50% so với thiết kế, do profile gia nhiệt (cure profile) chưa tối ưu\n• Q = 51/53 = 96.2% — 2 tấm bị tách lớp phải bỏ, mỗi tấm trị giá vài triệu đồng\n• OEE = 80% × 66.7% × 96.2% = 51.3%",
            "result": "Cải tiến:\n• P: Tối ưu profile gia nhiệt (cure profile) — nghiên cứu nhiệt độ + thời gian ép phù hợp từng loại EVA/backsheet, rút ngắn chu kỳ mà vẫn đảm bảo kết dính. Bảo trì bơm chân không định kỳ (thay gioăng, dầu bơm)\n• A: Lưu sẵn các chương trình ép (recipe) cho từng sản phẩm trên PLC, chuyển đổi chỉ cần chọn trên màn hình. Vệ sinh bề mặt ép tự động bằng hệ thống khí nén\n• Q: Kiểm tra EL (Electroluminescence — chiếu sáng tế bào pin để phát hiện vết nứt) trước khi ép → loại tấm lỗi sớm, tránh ép rồi mới phát hiện\n→ Mục tiêu OEE 65%."
        }
    ]
}
