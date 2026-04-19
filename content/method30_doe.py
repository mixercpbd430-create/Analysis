method = {
    "id": 30,
    "title": "DOE - Design of Experiments (Thiết kế thí nghiệm)",
    "short_name": "DOE",
    "icon": "🧪",
    "pillar": "Overview",
    "description": "Thiết kế thí nghiệm có hệ thống để tìm tổ hợp thông số tối ưu, xác định yếu tố nào ảnh hưởng lớn nhất và tìm điểm vàng cho quá trình sản xuất.",
    "meaning": """
<p><strong>DOE (Design of Experiments — Thiết kế thí nghiệm)</strong> là phương pháp thống kê cho phép thay đổi ĐỒNG THỜI nhiều yếu tố đầu vào để tìm ra tổ hợp tối ưu nhất.</p>
<p><em>Hãy tưởng tượng bạn nấu phở và muốn tìm công thức ngon nhất. Bạn có 4 yếu tố: lượng xương, thời gian nấu, lượng gia vị, nhiệt độ. Nếu thử từng yếu tố một (thay đổi 1 thứ, giữ 3 thứ còn lại) → cần rất nhiều lần thử. DOE cho phép thay đổi CẢ 4 yếu tố cùng lúc theo một ma trận toán học → ít lần thử hơn, nhưng tìm ra được công thức tối ưu VÀ biết yếu tố nào quan trọng nhất!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Các loại DOE phổ biến</div>
    <p><strong>1. Full Factorial (Thí nghiệm đầy đủ)</strong>: Thử TẤT CẢ tổ hợp — ví dụ: 3 yếu tố, mỗi yếu tố 2 mức (cao/thấp) → 2³ = 8 lần thử<br>
    <strong>2. Fractional Factorial (Thí nghiệm rút gọn)</strong>: Chỉ thử MỘT PHẦN tổ hợp thay vì tất cả → tiết kiệm thời gian, vẫn tìm được yếu tố chính<br>
    <strong>3. RSM - Response Surface (Bề mặt đáp ứng)</strong>: Tìm ĐIỂM TỐI ƯU chính xác — vẽ "bản đồ 3D" mô tả kết quả theo các yếu tố<br>
    <strong>4. Taguchi</strong>: Thiết kế bền vững (robust design) — tìm thông số ít bị ảnh hưởng bởi nhiễu (ví dụ: thời tiết, nguyên liệu thay đổi)<br><br>
    <em>Nói đơn giản: DOE như GPS cho nhà máy — thay vì đi thử từng đường, DOE tính toán và chỉ đường tối ưu ngay!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Tìm tổ hợp thông số TỐI ƯU cho quá trình sản xuất — thay vì thử ngẫu nhiên qua kinh nghiệm</li>
    <li>Xác định yếu tố nào ảnh hưởng LỚN NHẤT đến kết quả — tập trung kiểm soát đúng chỗ, bỏ qua yếu tố không quan trọng</li>
    <li>Phát hiện TƯƠNG TÁC giữa các yếu tố — ví dụ: nhiệt độ cao + ẩm cao cùng lúc thì kết quả khác hoàn toàn so với chỉ tăng 1 yếu tố</li>
    <li>Giảm số lần thí nghiệm cần thiết — DOE 16 lần thử có thể thay thế 100+ lần thử ngẫu nhiên</li>
    <li>Xây dựng công thức dự đoán (mô hình toán học) — nhập thông số vào → dự đoán kết quả ra</li>
    <li>Thiết kế sản phẩm/quá trình BỀN VỮNG — ít bị ảnh hưởng bởi yếu tố không kiểm soát được</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định mục tiêu, yếu tố và mức</div>
        <div class="step-card__desc">Response (Y — kết quả cần tối ưu): Ví dụ: độ bền viên, tỷ lệ lỗi, năng suất... Factors (X — yếu tố đầu vào có thể thay đổi): Ví dụ: nhiệt độ, áp suất, tốc độ, nồng độ... Levels (mức — giá trị cao/thấp của mỗi yếu tố): Ví dụ: nhiệt độ 180°C và 220°C. Nếu có quá nhiều yếu tố (>5), dùng DOE sàng lọc (screening) để thu hẹp trước.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Chọn loại thiết kế và lập kế hoạch</div>
        <div class="step-card__desc">Chọn loại DOE phù hợp (Full Factorial, Fractional, Taguchi, RSM...). Xác định số lần chạy (runs) — dùng phần mềm Minitab/Design Expert để tạo ma trận thí nghiệm. Trộn ngẫu nhiên thứ tự chạy (randomize) — tránh yếu tố thời gian ảnh hưởng. Thêm lần chạy lặp lại (replicate) để đánh giá độ tin cậy.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Thực hiện thí nghiệm</div>
        <div class="step-card__desc">Chạy ĐÚNG theo thứ tự đã randomize (không được tự ý sắp xếp lại!). Ghi nhận kết quả chính xác mỗi run. Cố gắng kiểm soát các yếu tố KHÔNG nằm trong thiết kế (noise factors) — ví dụ: nhiệt độ phòng, độ ẩm môi trường. Không thay đổi bất kỳ điều gì ngoài các yếu tố trong thiết kế.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Phân tích kết quả, tối ưu, và xác nhận</div>
        <div class="step-card__desc">ANOVA (phân tích phương sai) xác định yếu tố nào có ý nghĩa thống kê (p-value < 0.05). Biểu đồ Main Effect (ảnh hưởng chính) + Interaction (tương tác). Xây dựng phương trình hồi quy (regression model) dự đoán kết quả. Tìm tổ hợp tối ưu bằng Optimization. QUAN TRỌNG: Chạy xác nhận (confirmation run) 3-5 lần ở điểm tối ưu để kiểm chứng!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Tối ưu thông số ép viên TACN",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Chỉ số PDI (Pellet Durability Index — độ bền viên) dao động 88-96%, không ổn định. 4 yếu tố nghi ngờ ảnh hưởng: áp suất hơi (steam pressure), tốc độ die (die speed), khoảng cách roller (gap), độ ẩm nguyên liệu (moisture). Câu hỏi: Yếu tố nào THỰC SỰ quan trọng?",
            "analysis": "Thiết kế DOE Full Factorial 2⁴ (4 yếu tố, mỗi yếu tố 2 mức cao/thấp) = 16 lần chạy + 3 lần chạy center point (điểm giữa, kiểm tra có phi tuyến không) = tổng 19 runs.\n\nKết quả ANOVA (phân tích phương sai):\n• Steam pressure: p  (yếu tố #1)\n• Moisture NL: p = 0.003 → QUAN TRỌNG (yếu tố #2)\n• Tương tác Steam × Moisture: p = 0.01 → QUAN TRỌNG! (khi cả 2 cùng cao → PDI tốt nhất; nhưng steam cao + moisture thấp → PDI giảm)\n• Die speed: p = 0.35 → KHÔNG quan trọng (bất ngờ!)\n• Gap roller: p = 0.52 → KHÔNG quan trọng (bất ngờ!)\n→ Chỉ 2 trong 4 yếu tố thực sự ảnh hưởng PDI!",
            "result": "Tối ưu: Steam 2.5 bar + Moisture NL 14.5% → PDI ổn định 95.2%\n• Die speed và gap roller: GIỮ NGUYÊN — không cần chỉnh nữa, tiết kiệm thời gian điều chỉnh\n• Chạy xác nhận (confirm run) 5 lần: PDI = 94.8, 95.3, 95.5, 95.0, 95.4 → ổn định!\n→ Bài học: Trước DOE, nhà máy cứ chỉnh cả 4 yếu tố mỗi khi PDI xuống — tốn thời gian mà không hiệu quả. DOE chỉ ra chỉ cần kiểm soát 2 yếu tố (steam + moisture) là đủ!"
        },
        {
            "title": "Giảm cong vênh (warpage) ép nhựa",
            "industry": "Nhựa",
            "situation": "Vỏ remote TV bằng nhựa ABS (Acrylonitrile Butadiene Styrene) bị cong vênh 0.5 mm, tiêu chuẩn < 0.2 mm. 5 yếu tố nghi ngờ: Nhiệt nhựa (melt temp), nhiệt khuôn (mold temp), áp suất giữ (pack pressure), thời gian giữ (pack time), thời gian làm mát (cool time).",
            "analysis": "Vì 5 yếu tố quá nhiều, dùng 2 giai đoạn:\nGiai đoạn 1 - Sàng lọc (Screening): Fractional Factorial 2⁵⁻¹ = 16 runs (thay vì 32 runs full factorial) → tìm ra 2 yếu tố chính:\n• Nhiệt khuôn (mold temp): Ảnh hưởng mạnh nhất — khuôn lạnh → nhựa co không đều → cong\n• Áp suất giữ (pack pressure): Ảnh hưởng lớn thứ 2 — áp thấp → nhựa co ngót nhiều hơn\n\nGiai đoạn 2 - Tối ưu (RSM): Vẽ bề mặt đáp ứng (response surface) 3D cho 2 yếu tố → tìm 'đỉnh núi' (điểm tối ưu)",
            "result": "Tối ưu: Mold temp = 55°C + Pack pressure = 85 MPa → warpage chỉ 0.08 mm (Bài học: DOE 2 giai đoạn — giai đoạn 1 loại bỏ yếu tố không quan trọng, giai đoạn 2 tối ưu chính xác trên yếu tố chính. Tiết kiệm thời gian và nguyên liệu thử nghiệm."
        },
        {
            "title": "Tối ưu quy trình hàn laser thép ô tô",
            "industry": "Ô tô",
            "situation": "Hàn laser thép tấm 1.2 mm (body panel ô tô): Độ ngấu (penetration — laser xuyên sâu bao nhiêu) không đều, 8% mẫu rớt kiểm tra kéo đứt (tensile strength test fail). Cần tìm thông số hàn tối ưu.",
            "analysis": "DOE Full Factorial 3 yếu tố:\n• Công suất laser (Power): 2.5 / 3.0 / 3.5 kW\n• Tốc độ hàn (Speed): 1.5 / 2.0 / 2.5 m/phút\n• Vị trí tiêu cự (Focus position): -1.0 / -0.5 / 0.0 mm\n= 3³ = 27 lần chạy\n\nKết quả:\n• Response 1 (độ ngấu): Power là yếu tố số 1 (công suất càng cao → ngấu càng sâu)\n• Response 2 (độ bền kéo): Tương tác Power × Speed RẤT MẠNH!\n- Công suất cao + tốc độ chậm → ngấu quá sâu → cháy qua, mối hàn giòn\n- Công suất thấp + tốc độ nhanh → ngấu chưa đủ → mối hàn yếu\n- Phải CÂN BẰNG giữa power và speed",
            "result": "Tối ưu: Power = 3.5 kW + Speed = 2.0 m/phút + Focus = -0.5 mm\n• Penetration = 1.1 mm (ổn định, đủ sâu cho tấm 1.2 mm)\n• Strength test fail giảm từ 8% xuống 0.5%\n• Chạy xác nhận 10 mẫu: 10/10 đạt!\n→ Bài học: Nếu chỉ tăng Power mà không chỉnh Speed (thử từng yếu tố — OFAT) → cháy qua! DOE phát hiện tương tác mà OFAT không thể thấy."
        },
        {
            "title": "Tối ưu lên men bia — Rút ngắn thời gian",
            "industry": "Đồ uống",
            "situation": "Thời gian lên men bia 14 ngày. Muốn giảm xuống 10 ngày MÀ KHÔNG ảnh hưởng hương vị. 4 yếu tố: Nhiệt độ (temperature), mật độ men (yeast pitch rate — lượng tế bào men/mL), oxy hòa tan (dissolved O₂), nồng độ dịch nha (wort concentration).",
            "analysis": "DOE Fractional Factorial:\n• Kết quả: Nhiệt độ và Mật độ men là 2 yếu tố then chốt\n• Nhiệt độ tăng từ 12°C lên 14°C → men hoạt động nhanh hơn → lên men nhanh hơn 2-3 ngày\n• Pilot rate tăng từ 10 triệu tế bào/mL lên 15 triệu → nhiều men hơn → lên men song song nhiều đường hơn cùng lúc\n• Oxy và nồng độ dịch nha: ảnh hưởng không đáng kể trong dải thử nghiệm\n• Kiểm tra hương vị: Panel 8 chuyên gia thử mù (blind tasting) bia 10 ngày vs 14 ngày → 95% cho kết quả PASS (không phân biệt được!)",
            "result": "Tối ưu: Nhiệt lên men 14°C (thay vì 12°C) + Pitch rate 15 triệu tế bào/mL (thay vì 10 triệu)\n• Thời gian lên men giảm từ 14 xuống 10 ngày — tiết kiệm 4 ngày/mẻ\n• Flavor panel pass 95% — hương vị không thay đổi\n→ Tăng 40% năng suất (throughput) tank lên men vì mỗi tank xoay vòng nhanh hơn 4 ngày\n→ Tương đương xây thêm 4 tank lên men mới mà không tốn đồng nào!"
        },
        {
            "title": "Tối ưu CIP rửa tank sữa — Rửa nhanh mà vẫn sạch",
            "industry": "Thực phẩm",
            "situation": "CIP (Clean-In-Place — rửa tại chỗ không tháo thiết bị) rửa tank sữa mất 90 phút mỗi lần. Muốn giảm thời gian rửa mà vẫn đạt tiêu chuẩn vi sinh (ATP test — đo mức vi khuẩn còn lại).",
            "analysis": "DOE Taguchi L9 (thiết kế bền vững — tìm thông số ít bị ảnh hưởng bởi dao động):\n• 4 yếu tố, mỗi yếu tố 3 mức:\n- Nhiệt độ nước rửa: 60 / 70 / 80°C\n- Nồng độ NaOH (xút — chất tẩy rửa): 1% / 2% / 3%\n- Thời gian rửa: 10 / 20 / 30 phút\n- Lưu lượng nước (flow rate): 2 / 3 / 4 m/giây\n• Chỉ cần 9 lần chạy (thay vì 81 lần nếu full factorial!)\n• Phân tích S/N ratio (Signal-to-Noise — tỷ lệ tín hiệu/nhiễu, smaller-is-better cho ATP)",
            "result": "Tối ưu bền vững: 70°C + NaOH 2% + 20 phút + flow 3 m/s\n• Tổng CIP: 55 phút (giảm 39% so với 90 phút)\n• ATP Tại sao chọn 70°C thay vì 80°C? Vì ở 70°C kết quả ít dao động hơn khi nhiệt độ nước thay đổi ±3°C (bền vững — robust). Ở 80°C tuy sạch hơn nhưng nếu nhiệt giảm xuống 77°C → không sạch nữa!"
        },
        {
            "title": "Giảm lỗi mạ chrome — Screening rồi tối ưu",
            "industry": "Kim loại",
            "situation": "Mạ chrome trang trí: 12% sản phẩm bị lỗi (lỗ nhỏ — pit, cháy bề mặt — burn, gồ ghề — roughness). 6 yếu tố nghi ngờ ảnh hưởng. Nếu thử Full Factorial 2⁶ = 64 runs → quá tốn kém!",
            "analysis": "Giai đoạn 1 — Sàng lọc (Screening): Fractional Factorial 2⁶⁻³ = 8 runs (chỉ 8 lần thay vì 64!)\n• Kết quả: Giảm 6 yếu tố xuống còn 3 yếu tố quan trọng:\n① Mật độ dòng điện (current density — A/dm²)\n② Nhiệt độ bể mạ (temperature)\n③ Thời gian mạ (plating time)\n\nGiai đoạn 2 — Tối ưu: Full Factorial 2³ = 8 runs trên 3 yếu tố\n• Phát hiện tương tác: Current density × Temperature → dòng cao + nhiệt cao = CHÁY bề mặt (burn)!\n• Vẽ bản đồ 'vùng an toàn' (process window) — tổ hợp nào cho kết quả tốt, tổ hợp nào gây lỗi",
            "result": "Vùng tối ưu: Current 30 A/dm² + Temp 52°C + Time 8 phút → defect giảm từ 12% xuống 1.5%\n• Xác định ranh giới nguy hiểm: Current > 35 + Temp > 55 → CHÁY, tuyệt đối tránh!\n→ Bài học: DOE 2 giai đoạn (screening → optimization) chỉ cần tổng 16 runs để giải quyết vấn đề 6 yếu tố. Tiết kiệm 75% chi phí thí nghiệm so với thử ngẫu nhiên."
        },
        {
            "title": "Tối ưu công thức bê tông giảm xi măng",
            "industry": "Xây dựng",
            "situation": "Bê tông mác M400: muốn giảm lượng xi măng (đắt + phát thải CO₂) mà vẫn đạt cường độ nén (compressive strength) 28 ngày ≥ 40 MPa.",
            "analysis": "Mixture DOE (thiết kế hỗn hợp — đặc biệt cho bài toán công thức, vì tổng thành phần = 100%):\n• Xi măng: 350-420 kg/m³\n• Cát: 650-750 kg/m³\n• Đá: 1000-1100 kg/m³\n• Nước: 170-200 lít/m³\n• Phụ gia siêu dẻo (superplasticizer): 0-1.5%\n• Response: Cường độ 28 ngày + Độ sụt (slump — đo tính dẻo bê tông) + Chi phí\n\nKết quả: Phụ gia siêu dẻo cho phép giảm nước → giảm xi măng mà giữ nguyên cường độ",
            "result": "Tối ưu: Xi măng 380 kg (vs 410 kg hiện tại — giảm 30 kg!) + phụ gia 0.8% → cùng M400, cùng slump\n• Tiết kiệm chi phí 15% (30 kg xi măng × 2,000 VND/kg × hàng triệu m³/năm = hàng tỷ đồng)\n• Giảm phát thải CO₂ khoảng 8% (sản xuất xi măng phát thải rất nhiều CO₂)\n→ DOE Mixture là dạng đặc biệt cho bài toán tối ưu CÔNG THỨC (recipe) — khi các thành phần liên hệ với nhau (tăng A thì phải giảm B+C)."
        },
        {
            "title": "Tối ưu chiết xuất curcumin từ nghệ",
            "industry": "Dược phẩm",
            "situation": "Chiết xuất curcumin (hoạt chất chống oxy hóa) từ bột nghệ: hiện tại yield (tỷ lệ thu hồi) chỉ 3.5%, mục tiêu 5%. Cần tìm điều kiện chiết tối ưu mà không phá hủy curcumin (nhạy nhiệt).",
            "analysis": "DOE RSM Box-Behnken (thiết kế tối ưu bậc 2 — cho phép tìm đỉnh cong, không chỉ tuyến tính):\n• 4 yếu tố:\n- Tỷ lệ dung môi (solvent ratio): 1:10 đến 1:30\n- Nhiệt độ chiết: 50-80°C\n- Thời gian chiết: 2-6 giờ\n- Kích thước hạt nghệ: 0.5-2.0 mm\n• Response: Yield curcumin + Độ tinh khiết (purity)\n• Mô hình bậc 2 (quadratic model): R² = 0.97 → mô hình rất tốt, dự đoán chính xác 97%",
            "result": "Tối ưu: Ethanol 70% + 65°C + 4 giờ + Hạt Bài học: RSM cho phép tìm 'đỉnh cong' — điểm tối ưu không phải ở biên mà ở GIỮA dải, điều mà Factorial DOE thông thường không làm được."
        },
        {
            "title": "Tối ưu rang cà phê — Nghệ thuật gặp khoa học",
            "industry": "Thực phẩm",
            "situation": "Rang cà phê specialty: muốn tối đa điểm cupping (cảm quan coffee) đồng thời giảm vị đắng (bitterness). 3 yếu tố: Nhiệt độ rang (180-220°C), thời gian rang (10-18 phút), lưu lượng gió (airflow 40-80%).",
            "analysis": "DOE RSM CCD (Central Composite Design — thiết kế tổ hợp trung tâm):\n• 3 yếu tố × 5 mức = 20 runs (bao gồm center points và star points)\n• Response 1: Cupping score (điểm cảm quan, thang 100)\n• Response 2: Bitterness (1-10, càng thấp càng tốt)\n• Response 3: Color Agtron (đo màu rang — 100=nhạt, 0=đậm)\n\n• Tương tác Temperature × Time RẤT MẠNH!\n- Nhiệt cao + thời gian dài = rang quá sẫm (dark roast) → đắng, mất hương hoa quả\n- Nhiệt thấp + thời gian ngắn = rang chưa đủ → vị chua, underdeveloped\n- Phải tìm điểm cân bằng giữa nhiệt và thời gian",
            "result": "Tối ưu: 205°C + 13 phút + Airflow 60%\n• Cupping score: 86/100 (specialty grade!)\n• Bitterness: 3/10 (rất thấp)\n• Agtron: 55 (medium roast)\n• LƯU Ý: \"Sweet spot\" (vùng tối ưu) RẤT HẸP — chỉ ±5°C và ±1 phút → quá trình rang phải kiểm soát RẤT CHẶT\n→ Lắp bộ điều khiển PID nhiệt + timer chính xác + cảm biến Agtron inline\n→ DOE biến nghệ thuật rang (cảm tính của thợ rang) thành KHOA HỌC (công thức chính xác có thể lặp lại)."
        },
        {
            "title": "Tối ưu nhiệt luyện thép dao cắt",
            "industry": "Thép",
            "situation": "Dao cắt công nghiệp bằng thép dụng cụ: Độ cứng (hardness) yêu cầu HRC 58-62. Hiện tại dao động lớn 55-65 HRC — dao quá mềm không cắt được, quá cứng bị vỡ. 4 yếu tố nhiệt luyện cần tối ưu.",
            "analysis": "DOE 2 giai đoạn:\nScreening (Full Factorial 2⁴ = 16 runs):\n• Yếu tố: Nhiệt austenitizing (nung nóng), môi trường tôi (quench media — dầu/nước/polymer), nhiệt ram (tempering), thời gian giữ nhiệt (hold time)\n• Kết quả: Nhiệt nung (austenitizing temp) và nhiệt ram (tempering temp) là 2 yếu tố chính\n\nRSM cho 2 yếu tố → Bề mặt đáp ứng cho thấy:\n• Nhiệt nung quá cao → austenite thô → thép giòn (HRC >63)\n• Nhiệt ram quá cao → thép mềm (HRC <57)\n• Có 1 điểm tối ưu rõ ràng trên bề mặt 3D",
            "result": "Tối ưu: Nung 1060°C + Tôi dầu + Ram 200°C + Giữ 2 giờ → HRC = 60.0 ±0.8\n• Cpk tăng từ 0.5 (không đạt) lên 2.5 (xuất sắc!)\n• Mọi dao đều nằm trong spec 58-62 HRC\n→ DOE giải quyết vấn đề tưởng phức tạp (4 yếu tố) bằng cách chỉ ra thực tế chỉ cần kiểm soát 2 yếu tố."
        },
        {
            "title": "Giảm rỗ khí đúc áp lực nhôm",
            "industry": "Đúc kim loại",
            "situation": "Đúc áp lực nhôm (die casting): Lỗi rỗ khí (porosity — bọt khí bị kẹt trong vật đúc) 6%, tiêu chuẩn < 2%. 5 thông số quy trình nghi ngờ. Giám đốc muốn mua hệ thống hút chân không mới (~2 tỷ VND) để giảm rỗ.",
            "analysis": "DOE Screening (sàng lọc trước khi mua thiết bị!):\n• 5 yếu tố: Nhiệt nhôm (metal temp), nhiệt khuôn (die temp), tốc độ phun (injection speed), áp suất tăng cường (intensification pressure), mức chân không (vacuum level)\n• Fractional Factorial 2⁵⁻² = 8 runs\n\nKết quả xếp hạng ảnh hưởng:\n① Vacuum level: #1 quan trọng nhất — hút khí ra khỏi khuôn trước khi nhôm vào\n② Injection speed: #2 — tốc độ phun PHASE 2 (pha nhanh) nếu quá nhanh → tạo rối → bẫy khí\n③ Die temp: #3 — khuôn lạnh → nhôm đông sớm → bẫy khí bên trong",
            "result": "Tối ưu: Vacuum 80 mbar + Speed phase 2 = 4 m/s + Die temp = 220°C → Porosity giảm từ 6% xuống 1.2%!\n• Kiểm tra X-ray: Không còn rỗ khí lớn\n→ KHÔNG CẦN MUA hệ thống chân không mới! Hệ thống hiện tại đủ tốt nếu đặt đúng mức (80 mbar). Trước đây đặt 200 mbar → chưa hút đủ!\n→ Tiết kiệm 2 tỷ VND bằng cách chỉnh đúng thông số thay vì mua máy mới."
        },
        {
            "title": "Tối ưu model AI phân loại lỗi sản phẩm",
            "industry": "CNTT",
            "situation": "Mô hình Deep Learning CNN (Convolutional Neural Network — mạng thần kinh tích chập) phân loại lỗi sản phẩm qua camera: Accuracy (độ chính xác) 87%, cần đạt > 93%. Cần tối ưu hyperparameters (siêu tham số — thông số cài đặt cho AI).",
            "analysis": "DOE Bayesian (Bayes — tối ưu tuần tự thông minh, mỗi run tiếp theo dựa trên kết quả runs trước):\n• 5 yếu tố (hyperparameters):\n- Learning rate (tốc độ học): 0.0001 → 0.01\n- Batch size (kích thước lô): 16, 32, 64\n- Dropout rate (tỷ lệ tắt neuron để tránh overfitting): 0.1-0.5\n- Number of layers (số tầng): 3-7\n- Filter size (kích thước bộ lọc): 3×3, 5×5, 7×7\n• Learning rate là yếu tố THỐNG TRỊ — ảnh hưởng lớn nhất đến accuracy\n• Tương tác Filter size × Layers: nhiều layer + filter lớn → overfitting (học quá khớp dữ liệu huấn luyện, kém khi gặp dữ liệu mới)",
            "result": "Tối ưu: Learning rate = 0.0003 + Batch 32 + Dropout 0.3 + 5 layers + Filter 3×3\n• Accuracy = 94.5% (đạt mục tiêu!)\n• AUC = 0.98 (diện tích dưới đường ROC — rất tốt)\n→ Bài học: DOE không chỉ cho sản xuất — áp dụng được cả trong AI/Machine Learning! Thay vì chỉnh hyperparameters bằng thử sai (trial and error), DOE tìm tối ưu có hệ thống."
        },
        {
            "title": "Tối ưu chiết xuất espresso — Barista khoa học",
            "industry": "F&B",
            "situation": "Espresso: Chỉ số TDS (Total Dissolved Solids — tổng chất rắn hòa tan, đo nồng độ cà phê) mục tiêu 8-12%. Hiện tại dao động lớn 6-14% giữa các barista. Cần chuẩn hóa công thức.",
            "analysis": "DOE Definitive Screening Design (DSD — thiết kế sàng lọc mới, hiệu quả cho nhiều yếu tố):\n• 5 yếu tố: Kích thước xay (grind size), liều lượng cà phê (dose), nhiệt độ nước (water temp), thời gian chiết (extraction time), lực nén (tamp pressure)\n\nKết quả:\n• 3 yếu tố quan trọng: Grind size + Dose + Time\n• Tamp pressure: KHÔNG QUAN TRỌNG! → Bất ngờ: Lực nén barista (15 kg vs 25 kg) KHÔNG ảnh hưởng đáng kể đến TDS → Barista không cần lo lắng về lực nén!",
            "result": "Công thức tối ưu: Grind 2.5 (setting) + Dose 18g + Nhiệt 93°C + Time 27 giây + Tamp bất kỳ (15 kg)\n• TDS = 10.2% ±0.5% — ổn định và nằm trong target\n• Tamp pressure không quan trọng → giảm lo lắng ergonomics cho barista (không cần nén quá mạnh, giảm đau cổ tay)\n→ Lập thành SOP cho tất cả barista → espresso ổn định ở mọi cửa hàng\n→ DOE biến 'nghệ thuật pha chế' thành 'quy trình tiêu chuẩn' có thể đào tạo và nhân rộng."
        }
    ]
}
