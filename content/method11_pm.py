method = {
    "id": 11,
    "title": "PM Analysis - Phân tích PM (Hiện tượng - Cơ chế)",
    "short_name": "PM Analysis",
    "icon": "🔬",
    "pillar": "Overview",
    "description": "Phân tích HIỆN TƯỢNG bằng NGUYÊN LÝ VẬT LÝ → tìm MỌI yếu tố 4M → giải quyết lỗi MÃN TÍNH mà Why-Why bó tay!",
    "meaning": """
<p><strong>PM Analysis (Phenomenon-Mechanism Analysis — Phân tích Hiện tượng - Cơ chế)</strong> là phương pháp phân tích CHUYÊN SÂU dành cho các <strong>chronic losses (tổn thất mãn tính)</strong> — lỗi lặp đi lặp lại mà WHY-WHY và C-E Analysis KHÔNG THỂ giải quyết được!</p>
<p><em>Hình dung: Why-Why = "Bác sĩ gia đình" (hỏi "tại sao?" → đoán bệnh). PM Analysis = "Bác sĩ chuyên khoa" (xét nghiệm máu, chụp CT, sinh thiết → hiểu CƠ CHẾ bệnh → điều trị chính xác!). PM Analysis CHẬM HƠN nhưng chính xác hơn 10 lần!</em></p>
<p>Chữ P-M: <strong>P</strong>henomenon (Hiện tượng) → <strong>P</strong>hysical analysis (Phân tích vật lý) → <strong>M</strong>echanism (Cơ chế) → <strong>M</strong>achine, Man, Material, Method (4M conditions)</p>
<div class="note-box note-box--tip">
    <div class="note-title">💡 Khi nào dùng PM Analysis? — Khi WHY-WHY "BÓ TAY"!</div>
    <p>✅ Vấn đề xảy ra LẶP LẠI nhiều lần — đã sửa rồi mà VẪN TÁI PHÁT<br>
    ✅ Why-Why đã làm 3-5 lần nhưng KHÔNG tìm được root cause → "cứ hỏi tại sao mãi không ra gì!"<br>
    ✅ Tổn thất MÃN TÍNH (chronic) 1-5% — không đột ngột, không cao lắm, nhưng CỨ CÓ HOÀI<br>
    ✅ Vấn đề liên quan đến NHIỀU YẾU TỐ đồng thời (Machine + Material + Method đều ảnh hưởng)<br>
    ✅ Cần hiểu NGUYÊN LÝ VẬT LÝ/HÓA HỌC để giải quyết (không chỉ "hỏi tại sao")<br><br>
    ❌ KHÔNG dùng PM Analysis cho: Lỗi đột xuất rõ ràng (dùng Why-Why), lỗi do sai SOP (dùng training), lỗi thiết kế (dùng FMEA)</p>
</div>
""",
    "purpose": """
<ul>
    <li>Giải quyết CHRONIC LOSSES (tổn thất mãn tính) — "kẻ ăn mòn lợi nhuận thầm lặng" mà phương pháp thường KHÔNG hiệu quả</li>
    <li>HIỂU RÕ cơ chế vật lý/hóa học gây ra hiện tượng — KHÔNG đoán, mà CHỨNG MINH bằng khoa học!</li>
    <li>Xác định TẤT CẢ yếu tố ảnh hưởng (4M conditions) — Machine, Man, Material, Method → KHÔNG BỎ SÓT!</li>
    <li>Thiết lập ĐIỀU KIỆN TỐI ƯU cho TỪNG yếu tố → kiểm soát chặt → tiến tới Zero Defect</li>
    <li>Xây dựng KIẾN THỨC KỸ THUẬT SÂU — đội kỹ thuật hiểu BẢN CHẤT máy/vật liệu, không chỉ biết vận hành</li>
    <li>So sánh: Why-Why = hỏi "TẠI SAO?" (logic ngôn ngữ). PM Analysis = hỏi "CƠ CHẾ VẬT LÝ nào?" (logic khoa học) → CHÍNH XÁC hơn!</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: LÀM RÕ HIỆN TƯỢNG (Phenomenon) — Mô tả CHÍNH XÁC!</div>
        <div class="step-card__desc">Mô tả hiện tượng CỤ THỂ nhất có thể: XẢY RA Ở ĐÂU? (Vị trí: trên/dưới/trái/phải? Mặt A hay B?) KHI NÀO? (Ca nào? Mùa nào? Đầu mẻ hay cuối mẻ?) NHƯ THẾ NÀO? (Kích thước? Hình dạng? Hướng? Màu sắc?) TẦN SUẤT? (Liên tục hay ngẫu nhiên? 1% hay 5%?) Ví dụ SAI: "Viên cám bị nứt". Ví dụ ĐÚNG: "Viên nứt DỌC, dài 3-8mm, tại 50% chiều dọc viên, SAU khi qua cooler, tỷ lệ 4-6%, tăng khi ẩm cao".</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Phân tích NGUYÊN LÝ VẬT LÝ (Physical Analysis)</div>
        <div class="step-card__desc">Giải thích hiện tượng bằng NGUYÊN LÝ VẬT LÝ hoặc HÓA HỌC. Viết PHƯƠNG TRÌNH nếu có thể! Ví dụ: "Viên nứt = Ứng suất nhiệt (thermal stress) > Sức bền kéo của viên (tensile strength)". Phương trình: σ_thermal = E × α × ΔT. Khi ΔT (chênh lệch nhiệt lõi-bề mặt) LỚN → σ > σ_tensile → NỨT! → Đây là CƠ CHẾ! QUAN TRỌNG: Bước này cần KIẾN THỨC KỸ THUẬT SÂU — có thể cần tham khảo sách, hỏi chuyên gia, hoặc thí nghiệm!</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xác định 4M CONDITIONS — Mọi yếu tố ảnh hưởng</div>
        <div class="step-card__desc">Từ cơ chế vật lý, liệt kê TẤT CẢ 4M conditions ảnh hưởng: <strong>Machine (Máy)</strong>: Die L/D ratio, roller gap, cooler airflow, gearbox rung... <strong>Man (Người)</strong>: Kỹ năng adjust, thói quen vận hành, kinh nghiệm... <strong>Material (Vật liệu)</strong>: Loại NVL, ẩm NVL, kích thước hạt, chất kết dính... <strong>Method (Phương pháp)</strong>: SOP, recipe, thông số cài đặt, tốc độ... Mỗi condition → kiểm tra: Có TIÊU CHUẨN không? Tiêu chuẩn có ĐÚNG không? Có được TUÂN THỦ không?</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: KHẢO SÁT + KHẮC PHỤC + CHUẨN HÓA — Sửa TẤT CẢ!</div>
        <div class="step-card__desc">ĐO LƯỜNG từng 4M condition: Giá trị THỰC TẾ là bao nhiêu? SO SÁNH với tiêu chuẩn: Đạt hay không? KHẮC PHỤC sai lệch: Adjust, sửa, thay, training. CHUẨN HÓA: Viết vào SOP mới, cập nhật Control Plan, training lại operator. KHÁC Why-Why: Why-Why tìm 1 root cause → sửa 1 chỗ. PM Analysis tìm TẤT CẢ conditions → sửa TẤT CẢ → chronic loss → ZERO!</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Viên thức ăn nứt mãn tính 6% — Thermal stress do ΔT quá lớn!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Viên thức ăn bị NỨT mãn tính 4-6% sau cooler. Đã làm Why-Why 5 lần → sửa nhiều thứ (thay die, chỉnh steam, đổi NVL) → VẪN 4%! BGĐ: \"Đây là lỗi mãn tính KHÔNG THỂ GIẢM?\". → Áp dụng PM Analysis!",
            "analysis": "Bước 1 — Phenomenon (Hiện tượng CHI TIẾT):\n• Viên nứt DỌC (longitudinal crack — dọc theo chiều dài viên)\n• Vết nứt dài 3-8mm, chiếm ~50% chiều dài viên\n• Xảy ra SAU cooler (viên ra khỏi die thì tốt, qua cooler MỚI nứt!)\n• Tỷ lệ: 4-6%, TĂNG khi trời lạnh (mùa đông) và khi sản xuất thức ăn nhiều tinh bột\n\nBước 2 — Physical Analysis (Phân tích vật lý):\n• Viên ra die: Lõi 85°C, bề mặt 80°C → ΔT = 5°C → OK\n• Qua cooler: Quạt thổi khí lạnh → bề mặt nguội NHANH 40°C, lõi vẫn 75°C → ΔT = 35°C!\n• Thermal stress (ứng suất nhiệt): σ = E × α × ΔT\n• Khi ΔT = 35°C → σ_thermal > σ_tensile (sức bền kéo viên) → NỨT!\n• Giống hiện tượng: Đổ nước lạnh vào LY THỦY TINH NÓNG → LY NỨT! (cùng cơ chế!)\n\nBước 3 — 4M Conditions:\n\n| 4M | Condition | Tiêu chuẩn | Thực tế | Sai lệch? |\n| Machine | Cooler airflow (m³/h) | 10,000 đồng đều | 12,000 + không đều (gió mạnh 1 bên!) | SAI! |\n| Machine | Die L/D ratio | 10:1 (giữ nhiệt tốt) | 8:1 (die mòn → thay die ngắn hơn!) | SAI! |\n| Material | Ẩm sau conditioning | 16-17% | 14-15% (thiếu steam!) | SAI! |\n| Material | % tinh bột NVL | SAI! |\n| Method | Tốc độ cooling | Giảm dần | Thổi MAX ngay từ đầu! | SAI! |\n| Man | Operator điều chỉnh steam | Theo SOP | Giảm steam khi thấy viên ẩm (cảm tính!) | SAI! |",
            "result": "Bước 4 — Khắc phục TẤT CẢ 4M conditions:\n\n• Machine (Cooler): Cân chỉnh airflow ĐỀU 2 bên + giảm từ 12,000 → 10,000 m³/h → ΔT giảm từ 35°C → 20°C → stress Machine (Die): Thay die L/D 10:1 → viên giữ nhiệt đồng đều hơn\n• Material: Tăng steam → ẩm conditioning 16-17% → viên đàn hồi hơn → σ_tensile TĂNG\n• Material: Thêm chất kết dính (lignosulfonate 0.5%) cho formula tinh bột cao → tăng sức bền viên\n• Method: SOP cooler mới: Quạt chạy THẤP 5 phút đầu → TĂNG DẦN (counter-flow giảm shock nhiệt)\n• Man: Training operator: KHÔNG tự ý giảm steam! Dùng moisture meter đo → quyết định\n\nKết quả: Viên nứt 6% → 0.8%! (giảm 87%!) → Tiết kiệm 120 triệu VND/tháng (giảm return, rework)\n\n→ Bài học PM Analysis: Why-Why tìm được 1 nguyên nhân → sửa 1 → vẫn 4% (còn 5 yếu tố khác!). PM Analysis tìm TẤT CẢ 6 conditions sai → sửa TẤT CẢ 6 → 0.8%! Đó là sức mạnh của PM Analysis!"
        },
        {
            "title": "Rung motor bơm mãn tính 8 mm/s — ĐÃ thay bearing 3 lần vẫn rung!",
            "industry": "Hóa chất",
            "situation": "Motor-pump assembly rung mãn tính 8 mm/s (chuẩn ISO < 4.5 mm/s). Đã thay bearing 3 LẦN → vẫn 8 mm/s! Why-Why kết luận \"do bearing\" → NHƯNG thay rồi vẫn rung! → PM Analysis!",
            "analysis": "Bước 1 — Phenomenon:\n• Vibration dominant tại 1× RPM (tần số trùng tốc độ quay) — hướng RADIAL (ngang)\n• Rung 8 mm/s tại DE bearing (Drive End — đầu truyền động)\n• Rung THAY ĐỔI theo tải: Tải 100% → 8 mm/s. Tải 50% → 5 mm/s\n\nBước 2 — Physical Analysis:\n• Vibration 1× RPM + radial = 3 khả năng:\n1. Unbalance (mất cân bằng): F = m × e × ω² (lực = khối lượng × lệch tâm × (tốc độ góc)²)\n2. Misalignment (lệch tâm trục): Lực axial + radial tại coupling\n3. Pipe strain (ống kéo bơm): Ống CỨNG → giãn nở nhiệt → KÉO bơm → rung!\n• Bearing KHÔNG phải nguyên nhân! (Bearing hỏng = rung ở BPFO/BPFI tần số cao, KHÔNG phải 1×RPM!)\n→ Thay bearing 3 lần = sửa SAI NGUYÊN NHÂN 3 lần!\n\nBước 3 — 4M Conditions:\n\n| 4M | Condition | Tiêu chuẩn | Thực tế | Sai lệch? |\n| Machine | Dynamic balance | ISO G2.5 (0.05mm eccentricity) | Chưa bao giờ balance! | SAI! |\n| Machine | Alignment (laser) | Angular SAI! |\n| Machine | Foundation stiffness | Natural freq > 3× running speed | Foundation NỨT → giảm stiffness | SAI! |\n| Method | Pipe support | Expansion loop trước bơm | Ống CỨNG nối thẳng → kéo bơm khi nóng! | SAI! |\n| Method | Coupling type | Flexible coupling | Rigid coupling (cứng!) | SAI! |",
            "result": "Khắc phục TẤT CẢ:\n\n• In-situ balancing (cân bằng tại chỗ): Dùng máy đo → gắn counterweight → balance rotor → Unbalance giảm 90%\n• Laser alignment: Angular 0.15 → 0.03mm, Parallel 0.02mm → ĐẠT tiêu chuẩn\n• Pipe expansion loop: Thêm ống hình chữ U trước bơm → ống giãn nở tự do → KHÔNG kéo bơm!\n• Flexible coupling: Thay rigid → Omega coupling (hấp thu misalignment tồn dư)\n• Sửa foundation: Epoxy grout fill crack → tăng stiffness\n\nKết quả: Vibration 8 mm/s → 2.8 mm/s! Bearing KHÔNG BAO GIỜ phải thay nữa (vì rung giảm → bearing không bị quá tải)\n\n→ Bài học PM Analysis: Thay bearing 3 lần = 3 lần SỬA SAI! Why-Why nói 'do bearing' → NHƯNG bearing chỉ là NẠN NHÂN (bị rung phá hủy)! PM Analysis tìm 5 conditions gốc (balance, alignment, pipe, coupling, foundation) → sửa GỐC → bearing sống LÂU!"
        },
        {
            "title": "Vết xước kính ô tô mãn tính 2% — Particle cứng + F = μ×N!",
            "industry": "Ô tô",
            "situation": "Kính chắn gió (windshield) bị micro-scratch (vết xước nhỏ 0.1-0.5mm) mãn tính 2%. Ảnh hưởng chất lượng premium. Đã kiểm tra nhiều lần — không tìm được nguyên nhân rõ ràng.",
            "analysis": "Bước 2 — Physical Analysis:\n• Vết xước = 1 vật CỨNG hơn kính cào trên bề mặt kính\n• Phương trình: F(xước) = μ × N (lực ma sát = hệ số ma sát × lực nén)\n• Kính (Mohs 5.5) → vật có Mohs > 6 MỚI xước được\n• Particle cứng (bụi cát silica Mohs 7, bụi kim loại Mohs 6-7) BỊ KẸP giữa kính và bề mặt tiếp xúc (roller, găng tay, giá đỡ) → khi kính di chuyển → particle CÀO → xước!\n\nBước 3 — 4M Conditions:\n\n| 4M | Condition | Tiêu chuẩn | Thực tế | Sai? |\n| Machine | Roller material (roller vận chuyển kính) | Shore A 40 (mềm → particle chìm vào roller) | Shore A 70 (cứng → particle NỔI LÊN → cào kính!) | SAI! |\n| Machine | Air cleanliness (Class ISO) | ISO 7 ( 100,000 particles!) | SAI! |\n| Man | Handling gloves | Lint-free (không xơ sợi) | Cotton gloves (có xơ + giữ bụi!) | SAI! |\n| Method | Stacking method | Interleaving paper giữa 2 kính | Không có paper → kính chạm kính! | SAI! |",
            "result": "Khắc phục 4M:\n\n• Roller mềm Shore A 40: Particle rơi lên roller → CHÌM vào bề mặt mềm → KHÔNG cào kính! (Thay roller chỉ 5 triệu!)\n• Air shower station: Lắp buồng thổi khí trước khu vực handling → loại bỏ 95% particle khỏi kính\n• Lint-free gloves: Thay găng cotton → găng nitrile (không xơ, không giữ bụi)\n• Interleaving paper: Đặt giấy mỏng giữa 2 kính khi xếp → kính không chạm kính\n\nKết quả: Scratch 2% → 0.1%! → Giảm 95%!\n\n→ Bài học PM Analysis: F = μ × N → hiểu cơ chế vật lý → biết particle cứng là nguyên nhân → tìm TẤT CẢ nơi particle có thể xuất hiện (4M) → sửa TẤT CẢ → ZERO scratch!"
        },
        {
            "title": "Seal mực in loang mãn tính 3% — Surface tension γ_ink > γ_film!",
            "industry": "Bao bì",
            "situation": "In flexo trên film BOPP bị loang mực mãn tính 3%, đặc biệt ở vùng solid (phủ kín 100%). Đã điều chỉnh máy nhiều lần — lúc được lúc không. → PM Analysis!",
            "analysis": "Bước 2 — Physical Analysis:\n• Mực bám trên film = hiện tượng THẤM ƯỚT (wetting)\n• Phương trình: Wetting xảy ra khi γ_film (surface energy film) > γ_ink (surface tension mực)\n• Ngược lại: γ_film Bước 3 — 4M Conditions:\n\n| 4M | Condition | Tiêu chuẩn | Thực tế | Sai? |\n| Material | Film dyne level | > 38 dyne/cm | 32 dyne/cm (film cũ 3 tuần!) | SAI! |\n| Material | Ink viscosity | 18±1 giây Zahn cup #2 | 21 giây (mực ĐẶC → không trải đều!) | SAI! |\n| Machine | Anilox volume | 5 BCM (billion cubic microns) | 3.5 BCM (anilox mòn → ít mực!) | SAI! |\n| Machine | Impression (áp lực in) | 0.1mm (nhẹ) | 0.3mm (nặng → mực bị ĐÙN RA 2 bên!) | SAI! |",
            "result": "Khắc phục 4M:\n\n• Corona treat INLINE: Lắp bộ xử lý corona NGAY tại máy in (trước trạm in) → film luôn có γ_film > 40 dyne/cm → LUÔN thấm ướt tốt! (Không phụ thuộc tuổi film nữa!)\n• Ink viscosity control: Lắp viscosity cup + timer → operator đo MỖI 30 phút → pha dung môi giữ 18±1s\n• Anilox mới 5 BCM: Thay anilox mòn → chuyển đủ mực → phủ đều\n• Impression 0.1mm: Giảm áp lực → mực KHÔNG bị đùn ra → biên sắc nét\n\nKết quả: Loang mực 3% → 0.2%!\n\n→ Bài học PM Analysis: Cơ chế vật lý γ_film vs γ_ink → biết CHÍNH XÁC vấn đề tại surface energy film → corona inline = giải pháp DỨT ĐIỂM! Why-Why sẽ hỏi 'tại sao loang?' → 'do mực?' → thay mực → VẪN LOANG (vì GỐC là film!)."
        },
        {
            "title": "Ăn mòn ống cooling water mãn tính — MIC + galvanic cell!",
            "industry": "Sản xuất chung",
            "situation": "Ống thép carbon hệ thống cooling water bị RỈ thủng mãn tính — phải thay ống mỗi 2 NĂM (thiết kế 15 năm!). Chi phí thay: 200 triệu/lần. Đã xử lý hóa chất nhưng vẫn rỉ!",
            "analysis": "Bước 2 — Physical Analysis (Hóa học!):\n• Ăn mòn kim loại = phản ứng ĐIỆN HÓA:\n• Anodic: Fe → Fe²⁺ + 2e⁻ (sắt TAN vào nước!)\n• Cathodic: O₂ + 2H₂O + 4e⁻ → 4OH⁻ (oxy + nước nhận electron)\n• Tốc độ ăn mòn phụ thuộc: pH, O₂ hòa tan, nhiệt độ, vi khuẩn, cặn bám\n\nBước 3 — 4M Conditions:\n\n| 4M | Condition | Tiêu chuẩn | Thực tế | Sai? |\n| Material | Water pH | 7.5-8.5 (kiềm nhẹ) | 6.8 (ACID nhẹ → ăn mòn nhanh!) | SAI! |\n| Material | Biocide (diệt vi khuẩn) | Chlorine 0.5 ppm | 0.1 ppm (hết biocide!) | SAI! → MIC! (Microbiologically Influenced Corrosion — ăn mòn vi sinh!) |\n| Machine | Velocity (tốc độ nước) | > 1 m/s (đủ nhanh = không cặn bám) | 0.3 m/s (CHẬM → cặn BÁM → under-deposit corrosion!) | SAI! |\n| Method | Corrosion inhibitor | Phosphate 5 ppm | 1 ppm (bơm hóa chất HẾT!) | SAI! |\n| Machine | Galvanic couple | Cùng vật liệu | Ống thép NỐI TRỰC TIẾP với van đồng → galvanic cell → thép bị ĂN MÒN nhanh hơn tại mối nối! | SAI! |",
            "result": "Khắc phục 4M:\n\n• pH control 7.5-8.5: Lắp pH meter online + bơm NaOH tự động → kiềm nhẹ → giảm tốc độ ăn mòn 80%!\n• Biocide program: Chlorine 0.5 ppm liên tục + biocide non-oxidizing hàng tuần → tiêu diệt vi khuẩn MIC → không còn ăn mòn vi sinh!\n• Velocity > 1 m/s: Tăng lưu lượng bơm → nước chảy nhanh → KHÔNG BÁM CẶN → không có under-deposit corrosion!\n• Corrosion inhibitor: Phosphate 5 ppm liên tục → tạo màng bảo vệ trên bề mặt kim loại\n• Dielectric fitting: Lắp vòng cách điện giữa ống thép và van đồng → CẮT galvanic cell → không còn ăn mòn tại mối nối!\n\nKết quả: Ống sử dụng 2 năm → 8 NĂM! (gấp 4 lần!)\nTiết kiệm: 200 triệu × 3 lần/8 năm = 600 triệu!\n\n→ Bài học PM Analysis hóa học: Hiểu phương trình ăn mòn Fe → Fe²⁺ + 2e⁻ → biết TẤT CẢ yếu tố ảnh hưởng (pH, O₂, vi khuẩn, cặn, galvanic) → kiểm soát TẤT CẢ → ống sống GẤP 4 LẦN!"
        },
        {
            "title": "Sai kích thước CNC drift mãn tính — Thermal expansion ΔL = α×L×ΔT!",
            "industry": "Cơ khí chính xác",
            "situation": "Bore diameter trên sản phẩm CNC bị DRIFT (trôi) dần +0.005mm/10 chi tiết. Tolerance ±0.01mm → SPC Cpk = 0.8 (cần > 1.33). Đã thay dao, chỉnh offset → vẫn drift!",
            "analysis": "Bước 2 — Physical Analysis:\n• Kích thước TRÔI DẦN (drift) = KHÔNG ĐỘT NGỘT → loại trừ dao mòn (dao mòn = giảm, không tăng)\n• Thermal expansion (giãn nở nhiệt): ΔL = α × L × ΔT\n• α (thép) = 12 × 10⁻⁶ /°C. L (bore Ø50mm) = 50mm. ΔT = 5°C\n• ΔL = 12 × 10⁻⁶ × 50 × 5 = 0.003mm → SAI LỆCH 0.003mm mỗi khi nhiệt tăng 5°C!\n• Spindle chạy → ma sát → NHIỆT TĂNG 5°C/giờ → kích thước drift 0.003mm/giờ → SAU 2 giờ = 0.006mm → OUT OF SPEC!\n\nBước 3 — 4M Conditions:\n\n| 4M | Condition | Tiêu chuẩn | Thực tế | Sai? |\n| Machine | Spindle warm-up | 30 phút trước khi gia công | KHÔNG warm-up! (Chạy ngay = BAN ĐẦU lạnh → DẦN nóng → drift!) | SAI! |\n| Machine | Coolant temperature | 20±0.5°C | 20-25°C (không có chiller!) | SAI! |\n| Machine | Thermal compensation (CNC) | ON | OFF! (Không biết tính năng này!) | SAI! |\n| Method | Tool life management | Thay dao mỗi 200 chi tiết | Thay khi cùn (cảm tính!) | SAI! |",
            "result": "Khắc phục 4M:\n\n• Spindle warm-up 30 phút: Chạy không tải M3 S3000 G4 P1800 → spindle đạt nhiệt ỔN ĐỊNH → gia công = không drift!\n• Coolant chiller ±0.5°C: Lắp chiller → nước cắt gọt LUÔN 20°C → chi tiết + máy = đồng nhiệt\n• Thermal compensation ON: CNC có tính năng tự bù giãn nở nhiệt → ENABLE! (Trước đây không biết có!)\n• Tool life management: Đặt tool Life = 200 chi tiết → CNC tự ALARM → thay dao → KHÔNG MÒN quá\n\nKết quả: Cpk từ 0.8 → 1.67! (vượt yêu cầu 1.33!)\n\n→ Bài học PM Analysis CNC: ΔL = α × L × ΔT → hiểu NGUYÊN LÝ giãn nở nhiệt → tìm 4 conditions (warm-up, chiller, compensation, tool life) → sửa TẤT CẢ → Cpk tăng GẤP ĐÔI!"
        }
    ]
}
