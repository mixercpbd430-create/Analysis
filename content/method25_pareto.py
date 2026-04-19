method = {
    "id": 25,
    "title": "Pareto Analysis - Phân tích Pareto (80/20)",
    "short_name": "Pareto Analysis",
    "icon": "📊",
    "pillar": "Focus Improvement",
    "description": "Áp dụng nguyên tắc 80/20 để xác định 20% nguyên nhân gây ra 80% vấn đề, giúp ưu tiên hóa hành động cải tiến hiệu quả nhất.",
    "meaning": """
<p><strong>Pareto Analysis (Phân tích Pareto)</strong> dựa trên nguyên tắc 80/20 của Vilfredo Pareto: <em>"80% kết quả đến từ 20% nguyên nhân"</em>. Trong sản xuất, điều này nghĩa là:</p>
<ul>
    <li>80% thời gian dừng máy thường do 20% loại hỏng hóc gây ra</li>
    <li>80% phế phẩm thường do 20% loại lỗi gây ra</li>
    <li>80% chi phí bảo trì thường nằm ở 20% thiết bị</li>
</ul>
<p><strong>Biểu đồ Pareto</strong> kết hợp biểu đồ cột (thể hiện tần suất/giá trị từng loại) và đường cong tích lũy (%) để nhìn thấy ngay đâu là vấn đề lớn nhất.</p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Nguyên tắc "Số ít quan trọng"</div>
    <p><strong>Vital Few - Số ít quan trọng:</strong> 3-5 nguyên nhân hàng đầu thường chiếm 70-80% tổng tổn thất → Tập trung nguồn lực vào đây!<br>
    <strong>Trivial Many - Số nhiều không đáng kể:</strong> Hàng chục nguyên nhân còn lại chỉ chiếm 20-30% → Không cần dàn trải nguồn lực<br><br>
    <em>Nói đơn giản: Thay vì cố sửa 20 vấn đề cùng lúc, hãy tập trung sửa 3 vấn đề lớn nhất — sẽ giải quyết được 80% tổng tổn thất!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định nhanh chóng các vấn đề/nguyên nhân QUAN TRỌNG NHẤT cần giải quyết trước</li>
    <li>Ưu tiên hóa nguồn lực — đầu tư thời gian và tiền vào đúng chỗ mang lại hiệu quả cao nhất</li>
    <li>Trực quan hóa dữ liệu — biểu đồ Pareto dễ hiểu, thuyết phục ban giám đốc để xin ngân sách</li>
    <li>So sánh trước/sau cải tiến — vẽ Pareto trước và sau để chứng minh hiệu quả</li>
    <li>Kết hợp được với hầu hết mọi công cụ phân tích khác (Why-Why, FMEA, Loss Tree...)</li>
    <li>Đơn giản, ai cũng hiểu, áp dụng rộng rãi ở mọi lĩnh vực — không chỉ sản xuất</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Thu thập và phân loại dữ liệu</div>
        <div class="step-card__desc">Xác định vấn đề cần phân tích (dừng máy, phế phẩm, khiếu nại khách hàng, chi phí...). Thu thập dữ liệu trong khoảng thời gian đủ dài (ít nhất 1-3 tháng). Phân loại dữ liệu theo nguyên nhân, loại lỗi, máy, ca sản xuất... tùy mục đích phân tích.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Sắp xếp và tính phần trăm tích lũy</div>
        <div class="step-card__desc">Sắp xếp các loại nguyên nhân từ LỚN nhất → NHỎ nhất. Tính phần trăm (%) từng loại so với tổng. Tính phần trăm tích lũy (cộng dồn từ trên xuống). Xác định điểm 80% tích lũy — các nguyên nhân nằm trước điểm này chính là "số ít quan trọng".</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Vẽ biểu đồ Pareto</div>
        <div class="step-card__desc">Trục ngang (X): tên các loại nguyên nhân (đã sắp giảm dần). Trục dọc trái (Y1): giá trị/tần suất (số lần, số giờ, số tiền...). Trục dọc phải (Y2): phần trăm tích lũy (0-100%). Vẽ CỘT cho giá trị + ĐƯỜNG CONG cho % tích lũy. Kẻ đường ngang ở mức 80% để dễ nhận biết.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Phân tích sâu và lập kế hoạch hành động</div>
        <div class="step-card__desc">Tập trung vào nhóm A (trước điểm 80% tích lũy). Có thể vẽ Pareto cấp 2 cho từng top item — ví dụ: "Hỏng máy" → Pareto theo bộ phận hỏng. Dùng Why-Why hoặc biểu đồ nhân quả (CE) để đào sâu tìm nguyên nhân gốc rễ. Lập kế hoạch hành động cụ thể cho top 3-5 nguyên nhân.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Hỏng máy ép viên (Pellet Mill) theo nguyên nhân",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy ép viên PM-01 dừng máy đột xuất (breakdown) tổng 480 giờ/năm. Bộ phận bảo trì muốn biết nguyên nhân nào gây dừng nhiều nhất để tập trung phòng ngừa.",
            "analysis": "Vẽ biểu đồ Pareto theo giờ dừng:\n① Nứt/mòn die (khuôn ép): 200 giờ — chiếm 41.7%\n② Hỏng bạc đạn (bearing): 120 giờ — 25%, tích lũy 66.7%\n③ Motor quá tải (trip): 80 giờ — 16.7%, tích lũy 83.3%\n④ Van hơi (steam valve): 40 giờ\n⑤ Kẹt nguyên liệu (feeder jam): 25 giờ\n⑥ Khác: 15 giờ\n→ Top 3 nguyên nhân đầu chiếm 83.3% tổng thời gian dừng! Chỉ cần giải quyết 3 vấn đề này là giảm được phần lớn breakdown.",
            "result": "Lập kế hoạch hành động cho top 3:\n• Die nứt/mòn (200h): Chương trình quản lý tuổi thọ die — theo dõi số giờ chạy, thay die đúng chu kỳ 1,500 giờ trước khi nứt. Ghi chép lịch sử die trên bảng theo dõi\n• Hỏng bạc đạn (120h): Lắp cảm biến đo rung (vibration monitor) để phát hiện sớm bạc đạn hư — sửa chủ động thay vì chờ gãy\n• Motor quá tải (80h): Kiểm tra cách điện (insulation test) định kỳ hàng tháng + vệ sinh quạt làm mát motor\n→ Kết quả: Breakdown giảm 55% năm sau (từ 480h xuống 216h)."
        },
        {
            "title": "Phế phẩm đóng bao theo loại lỗi",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Tỷ lệ lỗi đóng bao 3.2%, tương đương 15,000 bao bị loại mỗi tháng. Mỗi bao lỗi phải mở ra, đổ lại, đóng bao mới → tốn nhân công + lãng phí bao bì. Cần giảm xuống dưới 1%.",
            "analysis": "Vẽ Pareto theo số lượng bao lỗi:\n① Lỗi hàn miệng bao (seal kém — bao hở, bao nhăn): 5,500 bao — 36.7%\n② Sai trọng lượng (nặng hơn/nhẹ hơn quy cách): 4,200 bao — 28%, tích lũy 64.7%\n③ Bao bị rách (rách do va đập trên băng chuyền): 2,800 bao — 18.7%, tích lũy 83.3%\n④ In date sai/mờ: 1,500 bao\n⑤ Bao bẩn (dính bụi, dầu): 700 bao\n⑥ Khác: 300 bao\n→ Top 3 (seal + trọng lượng + rách) = 83.3% tổng lỗi.",
            "result": "Hành động cụ thể cho từng top lỗi:\n• Lỗi seal 5,500 bao: Bảo trì thanh hàn (sealer) định kỳ — thay điện trở đúng chu kỳ + vệ sinh bề mặt ép. Kiểm tra nhiệt độ hàn đầu mỗi ca (dùng giấy thử nhiệt)\n• Sai trọng lượng 4,200 bao: Hiệu chuẩn cảm biến cân (loadcell) hàng tuần bằng quả cân chuẩn. Kiểm tra 5 bao đầu ca trước khi chạy\n• Bao rách 2,800 bao: Kiểm tra chất lượng bao PE từ nhà cung cấp — yêu cầu test độ bền kéo, độ dày đúng spec\n→ Kết quả: Tỷ lệ lỗi giảm từ 3.2% xuống 1.1% (saves ~10,000 bao/tháng)."
        },
        {
            "title": "Khiếu nại khách hàng theo loại",
            "industry": "Thực phẩm",
            "situation": "Công ty nhận 120 khiếu nại khách hàng trong 6 tháng. Ban giám đốc yêu cầu phân tích để giảm khiếu nại và giữ uy tín thương hiệu.",
            "analysis": "Vẽ Pareto theo số lượng khiếu nại:\n① Hạn sử dụng in sai/mờ/không đọc được: 28 vụ — 23.3%\n② Bao bì rách/hở (sản phẩm bị ẩm mốc): 25 vụ — 20.8%, tích lũy 44.2%\n③ Sai quy cách (nhãn ghi 25kg nhưng chỉ 24.5kg): 22 vụ — 18.3%, tích lũy 62.5%\n④ Dị vật (tóc, sợi bao, mảnh kim loại): 18 vụ — 15%, tích lũy 77.5%\n⑤ Mùi lạ (ẩm mốc, hóa chất): 12 vụ — 10%, tích lũy 87.5%\n⑥ Khác: 15 vụ\n→ Top 4 chiếm 77.5% tổng khiếu nại.",
            "result": "Hành động cho từng loại khiếu nại:\n• Hạn sử dụng (28 vụ): Kiểm tra máy in phun (inkjet printer) đầu/cuối mỗi ca — mực đủ, đầu phun sạch, kiểm tra mẫu in rõ nét\n• Bao bì rách/hở (25 vụ): Kiểm tra độ kín seal (seal integrity test) — bơm khí vào bao kiểm tra ngẫu nhiên + lắp metal detector kiểm tra seal\n• Sai quy cách (22 vụ): Bảng checklist đóng gói — operator ký xác nhận trọng lượng 5 bao đầu/giữa/cuối ca\n• Dị vật (18 vụ): Lắp máy dò kim loại (metal detector) trên băng chuyền + máy chiếu X-ray cho sản phẩm xuất khẩu\n→ Mục tiêu giảm 60% khiếu nại trong 6 tháng."
        },
        {
            "title": "Chi phí bảo trì theo thiết bị",
            "industry": "Sản xuất chung",
            "situation": "Tổng chi phí bảo trì nhà máy 5 tỷ VND/năm cho 120 thiết bị. Ban giám đốc muốn biết tiền bảo trì chủ yếu đổ vào máy nào để có chiến lược đúng.",
            "analysis": "Vẽ Pareto chi phí bảo trì theo thiết bị:\n① Máy ép viên (Pellet Mill): 1.2 tỷ — 24%\n② Nồi hơi (Boiler): 800 triệu — 16%, tích lũy 40%\n③ Máy nghiền (Hammer Mill): 600 triệu — 12%, tích lũy 52%\n④ Máy đùn (Extruder): 500 triệu — 10%, tích lũy 62%\n⑤ Máy đóng bao (Packing): 400 triệu — 8%, tích lũy 70%\n... 115 thiết bị còn lại: 1.5 tỷ — 30%\n→ 5 thiết bị (4.2% tổng số) chiếm 70% chi phí bảo trì! Đây chính là nguyên tắc Pareto.",
            "result": "Chiến lược theo Pareto:\n• 5 thiết bị nhóm A (70% chi phí): Phân tích RCM (Reliability Centered Maintenance — bảo trì tập trung vào độ tin cậy) chi tiết + lắp hệ thống CBM (Condition Based Maintenance — bảo trì theo tình trạng: đo rung, đo nhiệt, phân tích dầu). Xây dựng kế hoạch PM riêng, review hàng tháng\n• 25 thiết bị nhóm B (20% chi phí): Bảo trì theo lịch (time-based PM) tiêu chuẩn\n• 90 thiết bị nhóm C (10% chi phí): Chạy đến khi hỏng mới sửa (run-to-failure) cho thiết bị không critical, có dự phòng\n→ Mục tiêu giảm 25% tổng chi phí bảo trì = tiết kiệm 1.25 tỷ/năm."
        },
        {
            "title": "Lỗi lắp ráp bảng mạch PCB theo loại",
            "industry": "Điện tử",
            "situation": "Tỷ lệ lỗi lắp ráp bảng mạch PCB (Printed Circuit Board) là 2.5% — tương đương 1,250 lỗi trên 50,000 sản phẩm. Mục tiêu giảm xuống dưới 0.5%.",
            "analysis": "Vẽ Pareto theo số lượng lỗi:\n① Nối hàn (solder bridge — 2 mối hàn dính nhau gây đoản mạch): 450 lỗi — 36%\n② Mất linh kiện (missing component — máy gắn bỏ sót linh kiện): 280 — 22.4%, tích lũy 58.4%\n③ Linh kiện đứng (tombstone — linh kiện dựng đứng 1 đầu thay vì nằm phẳng): 200 — 16%, tích lũy 74.4%\n④ Mối hàn nguội (cold solder — hàn không chảy hoàn toàn, tiếp xúc kém): 150 — 12%, tích lũy 86.4%\n⑤ Sai phân cực (wrong polarity): 80\n⑥ Khác: 90\n→ Top 3 chiếm 74.4% tổng lỗi.",
            "result": "Hành động cho top 3:\n• Nối hàn (solder bridge) 450 lỗi: Thiết kế lại khuôn in kem hàn (stencil) — giảm kích thước lỗ để lượng kem hàn ít hơn, tránh tràn sang pad bên cạnh. Kiểm tra lượng kem hàn bằng máy SPI (Solder Paste Inspection)\n• Mất linh kiện (missing) 280 lỗi: Bảo trì băng cấp linh kiện (feeder) định kỳ — vệ sinh, thay phần mòn. Kiểm tra vòi hút chân không (vacuum nozzle) — bị tắc sẽ không hút được linh kiện\n• Linh kiện đứng (tombstone) 200 lỗi: Tối ưu thiết kế pad thư giãn cân bằng + Điều chỉnh profile lò hàn reflow (nhiệt độ/thời gian) để kem hàn chảy đều 2 bên\n→ Mục tiêu: tỷ lệ lỗi giảm từ 2.5% xuống 0.8%."
        },
        {
            "title": "Thời gian dừng máy phân tích theo ca sản xuất",
            "industry": "Sản xuất chung",
            "situation": "Nhà máy chạy 3 ca (sáng/chiều/đêm). Tổng thời gian dừng máy 107 giờ/tháng nhưng phân bổ không đều giữa các ca. Câu hỏi: Ca nào có vấn đề nhất và vấn đề gì?",
            "analysis": "Pareto cấp 1 — theo ca:\n① Ca A (sáng): 45 giờ/tháng — 42% → Nhiều nhất!\n② Ca B (chiều): 35 giờ — 32.7%, tích lũy 74.7%\n③ Ca C (đêm): 27 giờ — 25.2%\n\nDrill down Pareto cấp 2 cho Ca A (45 giờ):\n① Chờ nguyên liệu: 15 giờ — 33%\n② Hỏng máy đột xuất: 12 giờ — 27%\n③ Chuyển đổi sản phẩm chậm: 10 giờ — 22%\n④ Khác: 8 giờ",
            "result": "Ca A chiếm 42% tổng dừng máy — cần tìm hiểu cụ thể:\n• Chờ NL 15 giờ (33% của Ca A): Ca sáng bắt đầu 6h nhưng xe nguyên liệu thường đến 7h30 → máy chạy không có NL 1.5h/ngày. Giải pháp: Điều chỉnh lịch giao NL trước 5h30, hoặc chuẩn bị NL tồn bin từ ca đêm\n• Hỏng máy 12 giờ (27%): Ca A có KTV bảo trì mới (kinh nghiệm ít) → xử lý sự cố chậm hơn Ca B,C. Giải pháp: Mentor (kèm cặp) KTV mới với KTV kinh nghiệm trong 3 tháng\n• Chuyển đổi chậm 10 giờ (22%): Ca A không tuân thủ SOP chuyển đổi nhanh — bỏ bước chuẩn bị trước. Giải pháp: Coaching tổ trưởng Ca A về quy trình SMED."
        },
        {
            "title": "Năng lượng tiêu thụ theo khu vực nhà máy",
            "industry": "Sản xuất chung",
            "situation": "Nhà máy TACN tiêu thụ 12 triệu kWh điện/năm, chi phí 24 tỷ VND. Ban giám đốc yêu cầu giảm 15% năng lượng. Câu hỏi: Khu vực nào tiêu thụ nhiều nhất?",
            "analysis": "Vẽ Pareto tiêu thụ điện theo khu vực:\n① Khu nghiền (Hammer Mill + máy phụ trợ): 3.6 triệu kWh — 30%\n② Khu ép viên (Pellet Mill + conditioner + cooler): 2.4 triệu kWh — 20%, tích lũy 50%\n③ Hệ thống khí nén (Compressor + dryer): 1.8 triệu kWh — 15%, tích lũy 65%\n④ Chiếu sáng + Điều hòa văn phòng: 1.2 triệu kWh — 10%, tích lũy 75%\n⑤ Đóng bao: 840 nghìn kWh — 7%, tích lũy 82%\n... 10 khu vực còn lại: 2.16 triệu kWh — 18%",
            "result": "Nghiền + Ép viên + Khí nén = 65% tổng tiêu thụ — tập trung tiết kiệm ở 3 khu này:\n• Nghiền (30%): Lắp biến tần VFD (Variable Frequency Drive — điều chỉnh tốc độ motor theo tải thay vì chạy tốc độ cố định) → tiết kiệm 20-30%. Tối ưu kích thước lỗ lưới sàng — lưới quá nhỏ tốn nhiều năng lượng hơn cần thiết\n• Ép viên (20%): Quản lý die — die mòn cần nhiều lực ép hơn → tốn điện hơn. Thay die đúng hạn\n• Khí nén (15%): Khảo sát rò rỉ khí nén — ước tính nhà máy mất 25% khí nén do rò rỉ tại các mối nối, van, ống! Sửa chữa rò rỉ = tiết kiệm ngay lập tức\n→ Mục tiêu tiết kiệm 2 triệu kWh/năm = 4 tỷ VND."
        },
        {
            "title": "Tai nạn lao động theo loại — Ngành xây dựng",
            "industry": "Xây dựng",
            "situation": "Công ty xây dựng ghi nhận 52 tai nạn lao động trong năm. Cần phân tích Pareto để xác định loại tai nạn phổ biến nhất và có biện pháp phòng ngừa trọng điểm.",
            "analysis": "Vẽ Pareto theo số vụ tai nạn:\n① Trượt/ngã (trượt trên sàn ướt, ngã từ giàn giáo): 18 vụ — 34.6%\n② Vật rơi đè (dụng cụ, vật liệu rơi từ trên cao): 12 vụ — 23.1%, tích lũy 57.7%\n③ Kẹt tay/chân vào máy (máy trộn, máy cắt): 8 vụ — 15.4%, tích lũy 73.1%\n④ Cắt/đâm (kim loại sắc, đinh): 6 vụ — 11.5%, tích lũy 84.6%\n⑤ Điện giật: 4 vụ\n⑥ Khác: 4 vụ\n→ Top 3: Trượt ngã + Vật rơi + Kẹt = 73.1% tổng tai nạn.",
            "result": "Hành động phòng ngừa cho top 3 loại tai nạn:\n• Trượt/ngã 18 vụ: Chương trình 5S công trường — dọn sạch mặt bằng hàng ngày, lắp thảm chống trượt (anti-slip mat) tại lối đi ướt, lan can bảo vệ giàn giáo\n• Vật rơi 12 vụ: Lưới an toàn (safety net) bên dưới khu vực thi công trên cao + dây buộc dụng cụ (tool lanyard) cho dụng cụ cầm tay khi làm việc trên cao\n• Kẹt tay/chân 8 vụ: Lắp rào chắn bảo vệ (machine guarding) cho tất cả bộ phận quay/chuyển động. Nút dừng khẩn cấp (emergency stop) trong tầm với\n→ Mục tiêu giảm 50% tai nạn."
        },
        {
            "title": "Nguyên liệu bị loại (reject) theo nhà cung cấp",
            "industry": "Thức ăn chăn nuôi",
            "situation": "15% lô nguyên liệu nhập về bị loại khi kiểm tra đầu vào (IQC — Incoming Quality Control). Ảnh hưởng nghiêm trọng đến kế hoạch sản xuất — máy phải chờ NL thay thế.",
            "analysis": "Vẽ Pareto số lô bị loại theo nhà cung cấp (NCC):\n① NCC-A (bắp): 35 lô bị loại — 38%\n② NCC-C (khô đậu nành): 22 lô — 23.9%, tích lũy 61.9%\n③ NCC-E (fishmeal): 15 lô — 16.3%, tích lũy 78.3%\n④ Các NCC khác: 20 lô — 21.7%\n\nDrill down Pareto cấp 2 cho NCC-A (35 lô bị loại):\n① Độ ẩm vượt tiêu chuẩn: 20 lô — 58%\n② Protein thấp hơn spec: 9 lô — 25%\n③ Tạp chất cao (cát, sỏi, mối mọt): 6 lô — 17%",
            "result": "3 NCC chiếm 78% số lô bị loại → hành động trọng điểm:\n• NCC-A (38%): Đánh giá tại chỗ (supplier audit) — kiểm tra quy trình sấy, lưu trữ. Thảo thuận lại tiêu chuẩn chất lượng cụ thể (spec) có chế tài phạt nếu vi phạm\n• NCC-C (24%): Tìm NCC thay thế/bổ sung — không phụ thuộc 1 nguồn. Dual-sourcing (mua từ 2 nguồn) để giảm rủi ro\n• NCC-E (16%): Tăng số mẫu kiểm tra khi nhập hàng (sample size) từ 3 mẫu/lô lên 10 mẫu/lô vì NCC này hay gian lận\n→ Tỷ lệ reject giảm từ 15% xuống 5%."
        },
        {
            "title": "Lỗi phần mềm ERP theo module",
            "industry": "CNTT",
            "situation": "Hệ thống ERP (phần mềm quản trị doanh nghiệp) phát hiện 250 lỗi (bugs) trong quý 1. Đội QA (Quality Assurance — kiểm thử) cần xác định module nào nhiều lỗi nhất để ưu tiên sửa.",
            "analysis": "Vẽ Pareto số lỗi theo module:\n① Module Kho (Inventory): 75 lỗi — 30%\n② Module Sản xuất (Production): 55 lỗi — 22%, tích lũy 52%\n③ Module Mua hàng (Purchasing): 40 lỗi — 16%, tích lũy 68%\n④ Module Tài chính (Finance): 35 lỗi — 14%, tích lũy 82%\n⑤ Module Nhân sự (HR): 25 lỗi — 10%\n⑥ Khác: 20 lỗi — 8%",
            "result": "Module Kho + Sản xuất = 52% tổng lỗi:\n• Phân tích sâu: cả 2 module này dùng chung bảng dữ liệu (shared database table) → khi thay đổi 1 bên, bên kia bị ảnh hưởng (conflict)\n• Giải pháp gốc rễ: Thiết kế lại cấu trúc database — tách riêng bảng dữ liệu và đồng bộ qua API (giao tiếp ứng dụng) thay vì dùng chung\n→ Số lỗi giảm 60% trong quý 2. Bài học: Pareto giúp tìm ra 2 module đáng ngờ, sau đó phân tích sâu mới thấy nguyên nhân gốc rễ là thiết kế database."
        },
        {
            "title": "Chờ đợi trong bệnh viện — Trải nghiệm bệnh nhân",
            "industry": "Y tế",
            "situation": "Bệnh nhân khám ngoại trú phải chờ trung bình 90 phút từ khi đến đến khi xong. Mục tiêu giảm xuống 30 phút. Câu hỏi: Thời gian chờ nằm ở khâu nào nhiều nhất?",
            "analysis": "Phân tích Pareto thời gian chờ:\n① Chờ được bác sĩ khám: 35 phút — 38.9%\n② Chờ kết quả xét nghiệm (máu, X-ray): 25 phút — 27.8%, tích lũy 66.7%\n③ Chờ lấy thuốc tại quầy: 15 phút — 16.7%, tích lũy 83.3%\n④ Đăng ký/tiếp nhận ban đầu: 10 phút\n⑤ Khác (di chuyển, chờ thanh toán): 5 phút\n→ Chờ bác sĩ + chờ xét nghiệm = 66.7% tổng thời gian chờ.",
            "result": "Hành động cho top 2 khâu chờ:\n• Chờ bác sĩ (35 phút): Hệ thống hẹn giờ khám (appointment) để phân bổ bệnh nhân đều trong ngày thay vì dồn vào giờ cao điểm. Y tá phân loại (triage nurse) kiểm tra sơ bộ trước khi bác sĩ khám → bác sĩ khám nhanh hơn\n• Chờ xét nghiệm (25 phút): Bổ sung kỹ thuật viên xét nghiệm giờ cao điểm + Làn nhanh (fast track) cho xét nghiệm đơn giản (đường huyết, huyết áp)\n→ Mục tiêu: Giảm thời gian chờ từ 90 phút xuống 40 phút."
        },
        {
            "title": "Hàng bị trả lại theo lý do — Thương mại điện tử",
            "industry": "Thương mại điện tử",
            "situation": "Tỷ lệ trả hàng (return rate) 12%, tương đương 6,000 đơn/tháng, chi phí xử lý 600 triệu VND/tháng (giao nhận lại + kiểm tra + hoàn tiền + mất hàng). Cần giảm return.",
            "analysis": "Vẽ Pareto theo lý do trả hàng:\n① Sai size/sai màu so với đặt: 2,400 đơn — 40%\n② Không đúng mô tả (hình web khác thực tế): 1,200 đơn — 20%, tích lũy 60%\n③ Hư hỏng trong vận chuyển (vỡ, méo, ướt): 900 đơn — 15%, tích lũy 75%\n④ Khách đổi ý (không muốn nữa): 780 đơn — 13%, tích lũy 88%\n⑤ Khác: 720 đơn — 12%",
            "result": "Sai size/màu + Mô tả không đúng = 60% tổng trả hàng:\n• Sai size/màu (40%): Bảng size chi tiết kèm hướng dẫn đo (video). Thử nghiệm công nghệ thử đồ ảo AR (Augmented Reality — chiếu hình sản phẩm lên người qua camera điện thoại)\n• Mô tả không đúng (20%): Quay video sản phẩm 360° (thay vì chỉ ảnh). Ghi rõ kích thước chi tiết, chất liệu thực tế\n• Hư hỏng vận chuyển (15%): Cải tiến đóng gói — thêm lớp đệm, hộp cứng cho hàng dễ vỡ. Kiểm tra chất lượng trước khi xuất kho\n→ Mục tiêu giảm return rate từ 12% xuống 7%."
        },
        {
            "title": "Tiêu thụ nước theo khu vực — Nhà máy dệt nhuộm",
            "industry": "Dệt nhuộm",
            "situation": "Nhà máy dệt nhuộm tiêu thụ 5,000 m³ nước/ngày. Chi phí nước + xử lý nước thải rất lớn (hàng tỷ VND/năm). Cần xác định khu vực dùng nhiều nước nhất.",
            "analysis": "Vẽ Pareto theo khu vực:\n① Nhuộm (dyeing): 2,000 m³/ngày — 40%\n② Giặt/rửa (washing) sau nhuộm: 1,250 m³ — 25%, tích lũy 65%\n③ In hoa (printing): 500 m³ — 10%, tích lũy 75%\n④ Nồi hơi + làm mát: 500 m³ — 10%, tích lũy 85%\n⑤ Hoàn tất (finishing): 400 m³\n⑥ Khác: 350 m³",
            "result": "Nhuộm + Giặt = 65% tổng nước — tập trung tiết kiệm tại đây:\n• Nhuộm (40%): Giảm tỷ lệ nước/vải (liquor ratio) từ 1:8 xuống 1:5. Nghĩa là hiện tại dùng 8 lít nước cho 1 kg vải, giảm xuống 5 lít bằng máy nhuộm mới (Airflow — nhuộm bằng dòng khí, ít nước hơn)\n• Giặt (25%): Giặt ngược dòng (counter-current washing) — nước sạch đi ngược chiều vải, nước giặt đầu (bẩn nhất) dùng lại cho mẻ nhuộm tiếp theo\n• Tái sử dụng nước giặt cuối (tương đối sạch) cho các khâu không yêu cầu chất lượng cao\n→ Mục tiêu giảm 30% = tiết kiệm 1,500 m³/ngày."
        },
        {
            "title": "Lỗi vận hành nhà máy hóa chất",
            "industry": "Hóa chất",
            "situation": "Nhà máy hóa chất ghi nhận 45 sự cố do lỗi con người (human error) trong năm. Đây là rủi ro an toàn nghiêm trọng — sai lầm nhỏ có thể gây hậu quả lớn.",
            "analysis": "Vẽ Pareto theo loại sai sót:\n① Thao tác sai van (mở nhầm van, đóng thiếu van): 15 vụ — 33.3%\n② Sai công thức/liều lượng (dosing — bơm sai lượng hóa chất): 10 vụ — 22.2%, tích lũy 55.6%\n③ Bỏ sót bước trong quy trình (SOP — Standard Operating Procedure): 8 vụ — 17.8%, tích lũy 73.3%\n④ Thông tin truyền đạt sai/thiếu giữa các ca: 6 vụ — 13.3%, tích lũy 86.7%\n⑤ Khác: 6 vụ",
            "result": "Thao tác van + Sai liều lượng + Bỏ sót SOP = 73.3%:\n• Sai van (15 vụ): Sơn màu phân biệt đường ống theo chất (đỏ = acid, xanh = nước, vàng = dung môi) + Hệ thống khóa van (lock system) — chỉ mở được khi đúng trình tự\n• Sai liều lượng (10 vụ): Cân tự động (auto weighing) kết hợp quét mã vạch (barcode) thùng hóa chất — hệ thống so sánh mã hóa chất với công thức, báo lỗi nếu sai\n• Bỏ sót SOP (8 vụ): SOP điện tử trên tablet — mỗi bước phải tích xác nhận (checklist confirmation), camera chụp bằng chứng. Không thể nhảy bước\n→ Mục tiêu giảm 70% lỗi con người."
        },
        {
            "title": "Chi phí bảo hành ô tô theo loại lỗi",
            "industry": "Ô tô",
            "situation": "Chi phí bảo hành (warranty claim) 2 tỷ VND/quý. Nhà máy sản xuất cần biết loại lỗi nào gây tốn kém nhất để cải thiện chất lượng từ gốc.",
            "analysis": "Vẽ Pareto chi phí bảo hành theo loại lỗi:\n① Lỗi bó dây điện (electrical harness — đứt, chập, tiếp xúc kém): 500 triệu — 25%\n② Lỗi sơn (paint defect — bong, phồng, đổi màu): 400 triệu — 20%, tích lũy 45%\n③ Tiếng ồn hệ thống treo (suspension noise — kêu cọc cạch): 300 triệu — 15%, tích lũy 60%\n④ Hỏng điều hòa (AC failure): 250 triệu — 12.5%, tích lũy 72.5%\n⑤ Ron cửa hở (door seal — nước vào cabin): 200 triệu — 10%, tích lũy 82.5%\n⑥ Khác: 350 triệu",
            "result": "Bó dây + Sơn + Treo = 60% chi phí bảo hành:\n• Bó dây điện (25%): Cải thiện chất lượng connector (đầu nối) + Kiểm tra lại đường đi dây (routing) — dây chạm cạnh sắc bị mài mòn → đoản mạch\n• Lỗi sơn (20%): Kiểm soát độ sạch phòng sơn (booth cleanliness) — bụi gây bong sơn. Bảo trì súng phun sơn đúng lịch\n• Tiếng ồn treo (15%): Kiểm tra lại momen siết bu-lông (torque verification) trên dây chuyền lắp ráp — bu-lông lỏng gây tiếng ồn\n→ Mục tiêu giảm 40% chi phí bảo hành = tiết kiệm 800 triệu/quý."
        },
        {
            "title": "Giao hàng trễ phân tích theo nguyên nhân",
            "industry": "Logistics",
            "situation": "Tỷ lệ giao hàng đúng hạn (On-Time Delivery - OTD) chỉ đạt 78%, mục tiêu 95%. Trong tháng có 220 lô hàng bị giao trễ. Khách hàng phàn nàn, có nguy cơ mất đơn hàng.",
            "analysis": "Vẽ Pareto theo nguyên nhân giao trễ:\n① Sản xuất trễ tiến độ (production delay): 88 lô — 40%\n② Thiếu nguyên vật liệu (material shortage — NCC giao trễ): 48 lô — 21.8%, tích lũy 61.8%\n③ Không có xe vận chuyển (truck not available): 35 lô — 15.9%, tích lũy 77.7%\n④ Lỗi chứng từ/giấy tờ (document error — hóa đơn sai, phiếu giao thiếu): 25 lô — 11.4%, tích lũy 89.1%\n⑤ Thời tiết xấu: 15 lô\n⑥ Khác: 9 lô",
            "result": "Sản xuất trễ + Thiếu NL + Không có xe = 77.7%:\n• Sản xuất trễ (40%): Đóng băng lịch sản xuất (frozen schedule) 3 ngày trước ngày giao — không thay đổi lịch trong 3 ngày cuối, ưu tiên sản xuất đúng đơn hàng gấp\n• Thiếu NL (22%): Cải thiện MRP (Material Requirement Planning — hoạch định nhu cầu vật tư) chính xác hơn + Tồn kho an toàn (safety stock) cho NL critical\n• Không có xe (16%): Hệ thống quản lý xe (fleet management) + Hợp đồng với nhà vận tải dự phòng (backup carrier) cho cao điểm\n→ Mục tiêu OTD tăng từ 78% lên 92%."
        },
        {
            "title": "Sai sót đơn hàng kho phân phối",
            "industry": "Phân phối",
            "situation": "3% đơn hàng xuất kho bị sai sót (sai hàng, sai số lượng, gửi nhầm địa chỉ). Tổng 450 sai sót/tháng. Mỗi sai sót phải thu hồi + giao lại → chi phí trung bình 500,000đ/vụ = 225 triệu/tháng.",
            "analysis": "Vẽ Pareto theo loại sai sót:\n① Sai số lượng (giao thừa/thiếu): 180 vụ — 40%\n② Sai mã hàng (giao nhầm sản phẩm): 120 vụ — 26.7%, tích lũy 66.7%\n③ Sai địa chỉ giao: 70 vụ — 15.6%, tích lũy 82.2%\n④ Thiếu hàng trong thùng (đếm thiếu khi đóng thùng): 45 vụ — 10%\n⑤ Khác: 35 vụ",
            "result": "Sai số lượng + sai mã = 66.7% tổng sai sót:\n• Sai số lượng (40%): Quét mã vạch (barcode scan) 100% khi lấy hàng (picking) — hệ thống báo nếu số lượng quét không khớp đơn hàng. Cân trọng lượng thùng trước khi seal (weight verification) — nếu nhẹ/nặng hơn bình thường → kiểm tra lại\n• Sai mã hàng (26.7%): Mã vạch trên sản phẩm phải match với mã vạch trên phiếu xuất — quét so sánh tự động, báo lỗi nếu sai\n• Sai địa chỉ (15.6%): Tự động lấy địa chỉ từ hệ thống CRM (quản lý khách hàng), không nhập tay. In nhãn địa chỉ barcode để shipper quét xác nhận\n→ Mục tiêu giảm sai sót từ 3% xuống dưới 0.5%."
        }
    ]
}
