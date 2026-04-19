method = {
    "id": 28,
    "title": "Material Balance Analysis - Phân tích cân bằng vật chất",
    "short_name": "Material Balance",
    "icon": "⚖️",
    "pillar": "Focus Improvement",
    "description": "Phân tích cân bằng đầu vào - đầu ra nguyên vật liệu trong quy trình sản xuất để tìm ra nguyên vật liệu thất thoát ở đâu và giảm thiểu hao hụt.",
    "meaning": """
<p><strong>Material Balance (Cân bằng vật chất)</strong> dựa trên nguyên lý bảo toàn khối lượng: <em>"Cái gì đi vào phải đi ra — nếu không thành sản phẩm thì phải đi đâu đó!"</em></p>
<p>Công thức: <strong>Đầu vào (Input) = Thành phẩm (Output) + Phế phẩm (Waste) + Tồn kho thay đổi (Accumulation)</strong></p>
<p>Nói đơn giản: Nếu bạn đổ 100 kg nguyên liệu vào máy nhưng chỉ ra 92 kg thành phẩm → 8 kg đi đâu? Material Balance giúp trả lời câu hỏi này — tìm ra từng kg thất thoát.</p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Hai loại hao hụt</div>
    <p><strong>1. Hao hụt tất yếu (Inherent Loss)</strong>: Không thể tránh khỏi do bản chất quy trình — ví dụ: nước bay hơi khi sấy, vỏ trấu khi xay gạo → chấp nhận, không cải tiến được<br>
    <strong>2. Hao hụt kiểm soát được (Controllable Loss)</strong>: Có thể giảm bằng cải tiến — ví dụ: rơi vãi, overfill, đóng bao thừa → ĐÂY là mục tiêu cải tiến!<br><br>
    <strong>Yield (Tỷ lệ thu hồi)</strong> = Thành phẩm / Tổng đầu vào × 100%<br>
    <em>Ví dụ: 100 tấn NL → 92 tấn thành phẩm → Yield = 92%. Mục tiêu: nâng yield lên 95% bằng cách giảm controllable loss.</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định CHÍNH XÁC nguyên vật liệu thất thoát bao nhiêu và ở đâu trong quy trình</li>
    <li>Phân loại rõ: hao hụt nào là tất yếu (không cải tiến được) vs hao hụt nào kiểm soát được (CẦN cải tiến)</li>
    <li>Tìm ra điểm thất thoát lớn nhất trong quy trình → ưu tiên cải tiến ở đó</li>
    <li>Quy đổi hao hụt sang TIỀN (VND) — giúp ban giám đốc nhìn thấy mức thiệt hại để phê duyệt dự án</li>
    <li>Cải thiện yield (tỷ lệ thu hồi) và giảm phế thải → tiết kiệm hàng tỷ đồng/năm</li>
    <li>Kiểm soát tồn kho chính xác — phát hiện sớm mất mát, gian lận</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Vẽ sơ đồ quy trình và xác định ranh giới</div>
        <div class="step-card__desc">Vẽ sơ đồ dòng chảy quy trình (process flow diagram) từ đầu vào đến đầu ra. Xác định ranh giới phân tích: 1 công đoạn, 1 dây chuyền, hoặc toàn nhà máy. Liệt kê TẤT CẢ đầu vào (nguyên liệu, nước, phụ gia, bao bì...) và TẤT CẢ đầu ra (thành phẩm, phụ phẩm, phế thải, khí thải, nước thải, bụi...).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Đo lường tất cả đầu vào (Input)</div>
        <div class="step-card__desc">Cân/đo chính xác mọi nguyên vật liệu đầu vào: nguyên liệu chính (bắp, đậu nành, thép, nhựa...), phụ gia (vitamin, hóa chất...), nước, bao bì. Ghi nhận tồn kho đầu kỳ và cuối kỳ (không quên phần NL đang nằm trong máy!).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Đo lường tất cả đầu ra (Output)</div>
        <div class="step-card__desc">Cân/đo: thành phẩm, phụ phẩm (có thể bán — cám gạo, xương vụn, phoi thép...), phế phẩm phải bỏ, chất thải rắn, nước thải. ĐỪNG QUÊN: bụi bám lọc, khí bay hơi, rơi vãi trên sàn — đây thường là "hao hụt ẩn".</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Tính chênh lệch, phân tích và lập kế hoạch</div>
        <div class="step-card__desc">Hao hụt không giải thích được (Unaccounted loss) = Input - (Output đã đo + Waste đã xác định). Con số này thường gây BẤT NGỜ — nó chỉ ra lượng NL "biến mất" mà không ai biết! Quy đổi MỌI loại hao hụt sang tiền (VND) để so sánh. Ưu tiên cải tiến controllable loss lớn nhất trước.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Nhà máy TACN - Cân bằng NL toàn nhà máy",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Nhà máy TACN: Input (nhập kho) 100,000 tấn nguyên liệu/tháng. Output (thành phẩm xuất kho) 95,500 tấn. Hao hụt 4.5% = 4,500 tấn/tháng. Chi phí NL trung bình 8,000 VND/kg → thất thoát 36 tỷ VND/tháng! 4,500 tấn đi đâu?",
            "analysis": "Phân rã 4.5% hao hụt theo từng công đoạn:\n• Rơi vãi khi cân/nạp (batching spillage): 0.3% — NL rơi quanh miệng nạp, rơi trên sàn\n• Bụi nghiền (grinding dust): 0.5% — bụi bay ra khi nghiền, bám trên vách, thoát qua cyclone\n• Cặn bám máy trộn (mixer residue): 0.2% — NL dính trong máy trộn không xả hết\n• Biến đổi ẩm khi ép viên: ±1.5% — thêm hơi (steam) tăng ẩm, sau đó sấy lại giảm ẩm\n• Bay hơi khi làm mát (cooling evaporation): 0.8% — viên nóng 80°C ra cooler, nước bay hơi\n• Rơi vãi trên băng chuyền (conveyor spillage): 0.4% — NL rơi qua khe, mối ghép\n• Đóng bao thừa (bagging overfill): 0.5% — mỗi bao thừa 200-300g\n• Không giải thích được (unaccounted): 0.3% — nghi ngờ sai số cân hoặc mất mát khác",
            "result": "Phân loại:\n• Hao hụt tất yếu: Biến đổi ẩm ±1.5% + bay hơi cooler 0.8% = 2.3% → không thể tránh, nhưng có thể tối ưu\n• Hao hụt kiểm soát được: Rơi vãi + cặn mixer + overfill + unaccounted = 2.2% → CẢI TIẾN ĐƯỢC!\nHành động cụ thể:\n• Gắn ống bao che (spout sealing) tại miệng nạp cân → giảm rơi vãi\n• Lắp cánh gạt (scraper) trong mixer → giảm cặn bám\n• Hiệu chuẩn loadcell đóng bao → giảm overfill từ 300g xuống 50g/bao\n• Lắp nắp đậy băng chuyền (conveyor covers) + vệ sinh hàng ca\n→ Mục tiêu giảm tổng hao hụt từ 4.5% xuống dưới 2.5%. Tiết kiệm ~16 tỷ VND/tháng!"
        },
        {
            "title": "Cân bằng ẩm trong ép viên — Nước đi đâu?",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Nguyên liệu vào bộ tiền xử lý (conditioner): độ ẩm 12%. Viên ra máy làm mát (cooler): độ ẩm chỉ 11.5%. Trong quá trình ép, máy phun thêm 3-4% hơi nước (steam) → ẩm phải TĂNG, tại sao lại GIẢM? Nước đi đâu mất?",
            "analysis": "Cân bằng ẩm chi tiết:\n• Input: NL 12% ẩm + Steam bổ sung 3.5% = tổng 15.5% ẩm\n• Ra khỏi die (khuôn ép): 16% ẩm → OK, steam đã ngấm vào\n• Ra khỏi cooler: chỉ 11.5%! → Mất 4.5% ẩm trong cooler — quá nhiều!\n• Nguyên nhân: Không khí làm mát (cooling air) quá nóng/quá khô HOẶC thời gian sấy trong cooler quá dài (12 phút, chỉ cần 8 phút)\n→ Viên bị sấy quá mức → MẤT TRỌNG LƯỢNG (nước = trọng lượng = tiền!)",
            "result": "Tối ưu cooler:\n• Giảm lưu lượng gió (air volume) — hiện tại thổi quá mạnh, viên khô quá nhanh\n• Giảm thời gian cooling từ 12 phút xuống 8 phút — chỉ cần viên nguội đủ để đóng bao\n→ Ẩm ra cooler tăng từ 11.5% lên 12.5% (vẫn nằm trong spec 11-13%)\n→ Giữ được thêm 1% ẩm = giữ được 1% trọng lượng\n→ Với 300,000 tấn/năm × 1% = 3,000 tấn sản phẩm tương đương × 8,000 VND/kg = tiết kiệm 24 tỷ VND/năm chỉ bằng việc giảm gió cooler!"
        },
        {
            "title": "Nhà máy đường — 25% đường đi đâu?",
            "industry": "Mía đường",
            "situation": "Đưa vào 1,000 tấn mía (hàm lượng đường CCS = 12%, tức 120 tấn đường trong mía). Nhưng chỉ thu được 90 tấn đường thành phẩm. Yield = 90/120 = 75%. 25% đường (30 tấn) biến mất ở đâu?",
            "analysis": "Cân bằng đường (sucrose) chi tiết:\n• Đường thành phẩm: 90 tấn\n• Đường trong rỉ mật (molasses — chất lỏng còn lại sau kết tinh): 6.3 tấn — một phần đường không kết tinh được\n• Đường còn trong bã mía (bagasse): 2 tấn — ép chưa kiệt\n• Đường trong bùn lọc (filter mud): 1.5 tấn — mất theo bùn thải\n• Mất trong quá trình cô đặc/kết tinh: 2.2 tấn — đường phân hủy ở nhiệt độ cao\n→ Tổng đã xác định: 90 + 6.3 + 2 + 1.5 + 2.2 = 102 tấn\n→ Không giải thích được: 120 - 102 = 18 tấn đường! (15%!) → Đây là con số gây sốc!",
            "result": "Điều tra 18 tấn đường \"biến mất\":\n• Nghịch đảo đường (inversion loss — đường chuyển hóa thành glucose/fructose do pH thấp): 8 tấn — dung dịch mía quá acid, đường bị phân hủy\n• Cuốn theo hơi nước (entrainment in vapor): 4 tấn — giọt dung dịch đường bắn theo hơi khi cô đặc\n• Mất theo nước rửa: 3 tấn — nước rửa thiết bị kéo theo đường\n• Lãng phí khi lấy mẫu QC: 1 tấn\n• Sai số đo lường: 2 tấn\nHành động: Kiểm soát pH (tránh quá acid) + lắp bộ tách giọt (demister pad) trên tháp cô đặc + giảm lượng nước rửa\n→ Thu hồi thêm 12 tấn đường/vụ."
        },
        {
            "title": "Dầu ăn thất thoát trong sản xuất mì ăn liền",
            "industry": "Thực phẩm",
            "situation": "Sản xuất 1,000 tấn mì/tháng. Input dầu ăn: 180 tấn. Hàm lượng dầu trong mì thành phẩm 15% = 150 tấn. 30 tấn dầu mất đi đâu? (trị giá 600 triệu VND/tháng!)",
            "analysis": "Cân bằng dầu ăn (180 tấn input):\n• Trong sản phẩm (oil absorption): 150 tấn ✓\n• Dầu thải khi thay dầu bể chiên (waste oil): 12 tấn — dầu cũ đen, FFA cao phải thay\n• Tràn/rơi vãi (overflow/spillage): 5 tấn — bể chiên tràn khi nạp, rò rỉ van\n• Dầu lẫn trong nước ngưng hơi (steam condensate): 3 tấn — hơi nước ngưng trong bể chiên kéo theo dầu\n• Bám trong bã lọc (filter cake): 2 tấn — khi lọc dầu, bã giữ lại dầu\n• Bay hơi dạng sương (oil mist exhaust): 4 tấn — mù dầu theo ống khói\n• Không giải thích: 4 tấn",
            "result": "Hao hụt kiểm soát được:\n• Tràn/rơi vãi 5 tấn: Sửa bộ kiểm soát mức dầu (level control) — tự ngắt bơm khi đủ, không tràn\n• Sương dầu 4 tấn: Lắp bộ tách dầu sương (grease trap/oil mist collector) trên ống khói → thu hồi dầu ngưng\n• Dầu thải 12 tấn: Kéo dài tuổi thọ dầu bằng TPM bể chiên — lọc dầu thường xuyên hơn, kiểm soát nhiệt độ (dầu nóng quá nhanh hỏng) → giảm thay dầu từ 12 xuống 8 tấn\n→ Mục tiêu giảm tổng hao hụt dầu từ 17% xuống dưới 10%. Tiết kiệm 360 triệu VND/tháng."
        },
        {
            "title": "Tỷ lệ thu hồi gạo — Mất 30 tấn ở đâu?",
            "industry": "Nông sản",
            "situation": "Nhà máy xay xát gạo: Input 1,000 tấn lúa. Output gạo trắng 620 tấn (62%). Benchmark ngành: 65%. Gap = 30 tấn/tháng × 12,000 VND/kg = 360 triệu VND/tháng bị mất.",
            "analysis": "Cân bằng chi tiết:\n• Gạo trắng: 620 tấn (62%)\n• Trấu (vỏ lúa): 200 tấn (20%) — hao hụt tất yếu, không giảm được\n• Cám gạo: 120 tấn (12%) — phụ phẩm bán được, nhưng giá thấp hơn gạo\n• Tấm (gạo gãy): 40 tấn (4%) — gạo bị vỡ khi xay, bán giá thấp\n• Bụi: 8 tấn + Rơi vãi: 5 tấn + Không giải thích: 7 tấn\n→ Phát hiện 2 vấn đề:\n• Cám quá nhiều (12%): Máy xát (whitener) đang cài đặt quá mạnh → xát bỏ quá nhiều cám, ăn vào thịt gạo\n• Tấm quá cao (4%): Khoảng cách trục nghiền (rubber roller gap) sai → gạo bị vỡ nhiều",
            "result": "Cải tiến:\n• Điều chỉnh máy xát nhẹ hơn (gentler whitening): Giảm cám từ 12% xuống 10.5% → 1.5% thêm thành gạo\n• Chỉnh khoảng cách trục nghiền (rubber roller gap): Tấm giảm từ 4% xuống 2.5% → 1.5% thêm thành gạo\n• Bịt kín băng chuyền: Giảm rơi vãi\n→ Gạo tăng từ 620 lên 645 tấn (+25 tấn/tháng)\n→ Tiết kiệm 300 triệu VND/tháng (25 tấn × 12,000 VND/kg)."
        },
        {
            "title": "Cân bằng nước nhà máy bia — Tại sao tốn nhiều nước?",
            "industry": "Đồ uống",
            "situation": "Tỷ lệ nước: 6.5 lít nước để sản xuất 1 lít bia (6.5:1). Benchmark thế giới: 3.5:1. Đang dùng gần gấp đôi nước cần thiết! Chi phí nước + xử lý nước thải rất lớn.",
            "analysis": "Cân bằng nước (quy về 100 hL bia thành phẩm, cần 650 hL nước):\n• Bia thành phẩm: 100 hL\n• Rửa CIP (Clean-In-Place): 250 hL — chiếm tới 38%! Rửa tank lên men, đường ống, bồn\n• Nước làm mát (cooling): 120 hL — làm mát dịch nha sau nấu, làm mát tank lên men\n• Nồi hơi (boiler): 80 hL — cấp nước cho boiler tạo hơi\n• Rửa chai/lon (packaging rinse): 50 hL — rửa chai trước chiết\n• Rửa sàn: 30 hL\n• Không giải thích: 20 hL\n→ CIP chiếm 38% — đây là điểm lãng phí lớn nhất!",
            "result": "Giải pháp giảm nước:\n• CIP 250→150 hL: Tối ưu quy trình rửa CIP — rút ngắn bước rửa cuối (nước cuối sạch rồi), tái sử dụng nước rửa lần đầu cho CIP thiết bị ít critical\n• Cooling 120→30 hL: Chuyển sang hệ thống làm mát vòng kín (closed loop) — nước chạy vòng tròn qua chiller, không xả ra ngoài\n• Rửa chai 50→15 hL: Thay rửa nước bằng rửa khí nén (air rinse) cho chai PET\n→ Tỷ lệ nước giảm từ 6.5:1 xuống 3.8:1 (gần benchmark)\n→ Tiết kiệm 50% lượng nước = ~200 triệu VND/năm tiền nước + giảm 50% nước thải cần xử lý."
        },
        {
            "title": "Hiệu suất thu hồi kim loại — Đúc nhôm",
            "industry": "Đúc kim loại",
            "situation": "Input: 1,000 kg thỏi nhôm (aluminum ingot). Sản phẩm đúc thành: chỉ 650 kg. Yield hoàn chỉnh = 65%. 350 kg nhôm đi đâu? (Nhôm đắt ~60,000 VND/kg = 21 triệu VND thất thoát/tấn)",
            "analysis": "Cân bằng 1,000 kg nhôm:\n• Sản phẩm đúc đạt: 650 kg\n• Rãnh dẫn + cổng rót (runners/gates — nhôm đông trong hệ thống dẫn, không phải sản phẩm): 180 kg → TÁI CHẾ ĐƯỢC, nấu lại\n• Xỉ nhôm (dross — lớp oxy hóa trên bề mặt nhôm lỏng): 80 kg → mất một phần\n• Phoi gia công (machining chips — nhôm bị cắt bỏ khi gia công): 50 kg → TÁI CHẾ ĐƯỢC\n• Sản phẩm phế (scrap castings — bị rỗ khí, co ngót): 25 kg\n• Hao hụt nấu (melt loss — nhôm bay hơi, oxy hóa): 15 kg\n→ Tái chế được: 180 + 50 = 230 kg → nấu lại\n→ Yield thực (net yield): 650 / (1000-230) = 84.4% (tốt hơn con số 65% ban đầu!)",
            "result": "Cải tiến để tăng net yield:\n• Thiết kế khuôn đúc tốt hơn: Giảm rãnh dẫn từ 180 xuống 120 kg (dùng phần mềm mô phỏng dòng chảy nhôm → tối ưu kích thước rãnh dẫn nhỏ hơn mà vẫn đầy khuôn)\n• Giảm xỉ: Khử khí nhôm lỏng (degassing bằng argon) + phủ chất bảo vệ (cover flux) trên bề mặt nhôm lỏng → ít oxy hóa hơn\n• Giảm phoi gia công: Đúc gần kích thước hoàn thiện (near-net-shape) → gia công ít hơn\n→ Net yield mục tiêu 88%."
        },
        {
            "title": "Cân bằng ẩm khi sấy gỗ — Bao lâu là đủ?",
            "industry": "Gỗ",
            "situation": "Gỗ tươi vào lò sấy: 50% ẩm (100 tấn gỗ có 50 tấn nước). Yêu cầu ra lò: 10-12% ẩm. Thời gian sấy 14 ngày. Nhiên liệu tốn 300 triệu/lò. Cần tối ưu.",
            "analysis": "Cân bằng ẩm:\n• Input: 100 tấn gỗ tươi (50 tấn gỗ khô + 50 tấn nước)\n• Output mong muốn: 56 tấn (50 tấn gỗ + 6 tấn nước, tức ~11% ẩm)\n• Cần bay hơi: 44 tấn nước! Mỗi kg nước bay hơi cần ~700 kcal\n• Kiểm tra: Gỗ ra lò chỉ 8% ẩm → sấy QUÁ KHÔ! Mất thêm 2% ẩm = 1 tấn nước × nhiên liệu lãng phí. Gỗ quá khô dễ nứt, kém chất lượng\n• Nguyên nhân: Đặt thời gian sấy cố định 14 ngày cho tất cả loại gỗ, không đo ẩm trong quá trình sấy",
            "result": "Tối ưu:\n• Lắp cảm biến ẩm gỗ (moisture probe) trong lò → dừng sấy khi đạt 11% thay vì chạy đủ 14 ngày\n• Giảm thời gian sấy xuống 10-11 ngày (tùy loại gỗ) → tiết kiệm 20% nhiên liệu\n• Không sấy quá khô → giảm tỷ lệ gỗ nứt từ 5% xuống 2%\n→ Tiết kiệm 60 triệu/lò nhiên liệu + giảm gỗ nứt."
        },
        {
            "title": "Sơn lãng phí — 55% sơn không lên sản phẩm!",
            "industry": "Ô tô",
            "situation": "Phun sơn ô tô: Hiệu suất chuyển giao (transfer efficiency — tỷ lệ sơn bám lên sản phẩm) chỉ 45%. Nghĩa là 55% sơn phun ra không bám lên xe! Chi phí sơn lãng phí: 500 triệu VND/tháng.",
            "analysis": "Cân bằng 100 kg sơn phun ra:\n• Bám lên sản phẩm: 45 kg (45%) ✓\n• Overspray bị hút vào cabin (sơn bay qua người sản phẩm, bị bộ lọc cabin hấp thụ): 35 kg (35%) — một phần có thể thu hồi\n• Bám trên bộ lọc cabin (booth filter): 10 kg (10%)\n• Dung môi bay hơi (solvent evaporation): 5 kg (5%)\n• Sơn xả bỏ khi rửa đường ống (line flush waste): 5 kg (5%)\n→ Chỉ 45% sơn làm đúng chức năng!",
            "result": "Cải tiến:\n• Phun tĩnh điện (ESTA — Electrostatic Spray): Sơn được tích điện (+), sản phẩm nối đất (-) → sơn bị HÚT vào sản phẩm thay vì bay lung tung → transfer efficiency tăng từ 45% lên 70%!\n• Robot phun: Phun chính xác khoảng cách và góc → giảm overspray\n• Đầu phun bell cup (đĩa xoay): Sương sơn mịn hơn, bám tốt hơn\n→ Mục tiêu transfer efficiency 75%. Tiết kiệm 300 triệu VND/tháng!"
        },
        {
            "title": "Kem hàn SMT — 60% bị lãng phí",
            "industry": "Điện tử",
            "situation": "Kem hàn (solder paste — hỗn hợp thiếc dạng paste dùng hàn linh kiện lên bảng mạch PCB): Mua 50 kg/tháng, giá $80/kg ≈ 100 triệu/tháng. Tính toán lý thuyết chỉ cần 20 kg. 60% kem hàn bị lãng phí!",
            "analysis": "Cân bằng 50 kg kem hàn:\n• Trên bảng mạch (thực sự hàn): 20 kg (40%) ✓\n• Lau vệ sinh khuôn in (stencil cleaning): 12 kg (24%) — mỗi lần lau vứt bỏ kem dính\n• Kem quá hạn phải bỏ (expired): 8 kg (16%) — kem hàn chỉ sử dụng 24-48 giờ sau khi mở hộp, quá hạn tính chất thay đổi\n• Kem còn lại trên khuôn cuối ca (leftover on stencil): 5 kg (10%) — dùng không hết vứt bỏ\n• Bảng mạch in lỗi phải lau (misprinted PCB): 3 kg (6%)\n• Mẫu thử nghiệm: 2 kg (4%)",
            "result": "Hành động giảm lãng phí:\n• Kem hết hạn 8→2 kg: Áp dụng FIFO (hộp nhập trước dùng trước) + bảo quản lạnh đúng quy cách + dán nhãn ngày mở hộp, hạn sử dụng\n• Vệ sinh stencil 12→7 kg: Tối ưu tần suất lau stencil — dựa trên kết quả SPI (kiểm tra kem hàn bằng camera), chỉ lau khi cần thay vì lau định kỳ\n• Leftover 5→2 kg: Tính toán lượng kem cần dùng trước mỗi ca + gạt kem thừa trả về hộp bảo quản đúng cách\n→ Giảm từ 50 xuống 35 kg/tháng. Tiết kiệm $1,200/tháng ≈ 30 triệu VND."
        },
        {
            "title": "Phế liệu thép — Tối ưu cắt CNC",
            "industry": "Cơ khí",
            "situation": "Input: 500 tấn thép tấm/tháng. Sản phẩm: 320 tấn (64%). Phế liệu: 180 tấn — bán phế liệu giá thấp. Giá mua thép: 20,000 VND/kg, giá bán phế: 5,000 VND/kg. Chi phí cơ hội: 180 tấn × 15,000 VND/kg = 2.7 tỷ/tháng!",
            "analysis": "Cân bằng 500 tấn thép:\n• Sản phẩm: 320 tấn ✓\n• Phế khung (skeleton scrap — phần tấm thép còn lại sau khi cắt, giống khung xương): 120 tấn (24%)\n• Phế mảnh có thể tái dùng (offcut reusable — mảnh thừa nhưng đủ lớn làm chi tiết nhỏ): 30 tấn (6%)\n• Hao cắt (kerf loss — thép bị cắt thành bụi/phoi): 15 tấn (3%)\n• Phế phẩm lỗi (quality reject — cắt sai, sai kích thước): 10 tấn (2%)\n• Phế biên (edge trim — cắt mép tấm thép không dùng được): 5 tấn (1%)",
            "result": "Cải tiến:\n• Tối ưu nesting (xếp hình - sắp xếp chi tiết trên tấm thép tối ưu bằng phần mềm): Skeleton giảm từ 24% xuống 18%. Phần mềm xoay/lật chi tiết để vừa khít nhau, ít chừa khoảng trống\n• Quản lý mảnh thừa (offcut management): Nhập kho mảnh thừa đủ lớn, khi có đơn hàng chi tiết nhỏ → cắt từ mảnh thừa thay vì tấm mới\n• Giảm kerf: Dùng laser fiber thay plasma → đường cắt mỏng hơn (0.2mm vs 2mm) → tiết kiệm 2% thép\n• First-piece inspection: Kiểm tra chi tiết đầu tiên trước khi cắt hàng loạt → giảm reject\n→ Yield tăng từ 64% lên 72%. Tiết kiệm 600 triệu VND/tháng."
        },
        {
            "title": "Bê tông lãng phí — Công trường xây dựng",
            "industry": "Xây dựng",
            "situation": "Đặt bê tông: 5,000 m³/tháng. Sử dụng thực: 4,500 m³. Lãng phí 10% = 500 m³ × 1.5 triệu VND/m³ = 750 triệu VND/tháng đổ xuống cống!",
            "analysis": "Cân bằng 500 m³ bê tông lãng phí:\n• Đặt thừa (over-ordering — đặt dư phòng thiếu): 200 m³ (4%) — kỹ sư tính toán dư 5-10% \"cho chắc\"\n• Bê tông còn trong ống bơm (pump line residual): 80 m³ (1.6%) — khi bơm xong, bê tông trong ống phải xả bỏ\n• Đổ thừa/ván khuôn rò (over-pour/formwork leak): 100 m³ (2%) — ván khuôn không kín, bê tông chảy ra ngoài\n• Xe bồn bị từ chối (rejected trucks — đến trễ bê tông đông, sai mác): 50 m³ (1%)\n• Thừa trả về trạm (returned excess): 70 m³ (1.4%)",
            "result": "Giảm lãng phí:\n• Đặt thừa 4%→1.5%: Tính toán khối lượng chính xác bằng BIM (Building Information Modeling — mô hình 3D, tính thể tích chính xác từng cấu kiện)\n• Ống bơm 1.6%: Tối ưu chiều dài ống bơm + xả sớm khi gần xong\n• Ván khuôn 2%: Kiểm tra kín ván khuôn trước khi đổ — dùng checklist\n• Xe trễ 1%: Lên lịch giao chính xác, tránh đặt xe cuối ngày (dễ chở về)\n→ Mục tiêu giảm lãng phí từ 10% xuống 4%. Tiết kiệm 450 triệu VND/tháng."
        },
        {
            "title": "Cân bằng dung môi — Nhà máy sơn/keo",
            "industry": "Hóa chất",
            "situation": "Nhà máy phủ (coating): Tiêu thụ dung môi (solvent) 50 tấn/tháng. Chi phí 2 tỷ VND. Phát thải VOC (hợp chất hữu cơ bay hơi) gần vượt giới hạn quy định môi trường.",
            "analysis": "Cân bằng 50 tấn dung môi:\n• Còn trong sản phẩm (retained in coating): chỉ 5 tấn (10%!) ✓\n• Bay hơi trong quá trình sấy (process evaporation): 30 tấn (60%) → ra ống khói → ô nhiễm!\n• Rửa thiết bị/đường ống (cleaning/flush): 10 tấn (20%)\n• Rơi vãi/phế thải: 3 tấn (6%)\n• Bay hơi khi lưu trữ (storage loss): 2 tấn (4%)\n→ 90% dung môi trở thành phế thải hoặc khí thải! Chỉ 10% nằm trong sản phẩm.",
            "result": "Giải pháp:\n• Thu hồi dung môi (solvent recovery): Lắp hệ thống ngưng tụ (condensation) + than hoạt tính (activated carbon) trên ống khói → thu hồi 20 tấn dung môi/tháng từ khí thải, tái sử dụng\n• Giảm dung môi rửa: Hệ thống PIG (con thoi đẩy sạch ống → ít dung môi rửa hơn) + tối ưu CIP\n• Chuyển đổi sang sơn gốc nước (water-based) cho sản phẩm phù hợp → không cần dung môi\n→ Giảm mua dung môi từ 50 xuống 30 tấn/tháng. Tiết kiệm 800 triệu VND + tuân thủ môi trường."
        },
        {
            "title": "Nhiên liệu lò nấu kim loại — Nhiệt đi đâu?",
            "industry": "Kim loại",
            "situation": "Lò nấu LPG: tiêu thụ 120 tấn gas/tháng × 25 triệu/tấn = 3 tỷ VND. So với lò tương tự ở nhà máy khác, đang tốn nhiều hơn 30%.",
            "analysis": "Cân bằng NĂNG LƯỢNG (nhiệt) thay vì vật chất:\n• Nhiệt hữu ích (nấu chảy kim loại): chỉ 45% — phần thực sự làm việc!\n• Nhiệt theo khí thải (flue gas loss): 25% — khí nóng 400°C bay ra ống khói mang theo nhiệt\n• Nhiệt mất qua vách lò (wall radiation loss): 12% — vỏ lò nóng tỏa nhiệt ra môi trường\n• Nhiệt mất khi mở cửa lò (opening loss): 8% — mỗi lần mở cửa nạp nguyên liệu, nhiệt thoát ra\n• Nhiệt lãng phí khi chờ (standby/idle): 5% — lò giữ nhiệt khi không nấu\n• Đốt cháy không hoàn toàn (incomplete combustion): 3% — gas không cháy hết\n• Không giải thích: 2%",
            "result": "Tối ưu năng lượng:\n• Bộ thu hồi nhiệt khí thải (recuperator): Dùng khí thải nóng gia nhiệt không khí đầu vào → tiết kiệm 15% nhiên liệu\n• Cửa lò tự động đóng (auto-close mechanism): Giảm thời gian mở cửa, nhiệt ít thất thoát\n• Nâng cấp gạch chịu lửa (refractory): Vật liệu cách nhiệt tốt hơn → giảm mất nhiệt qua vách\n• Kiểm soát tỷ lệ gió/gas (O₂ trim control): Phân tích khí thải bằng O₂ sensor, tự động chỉnh lượng gió cho cháy hoàn toàn\n→ Giảm 25% tiêu thụ nhiên liệu. Tiết kiệm 750 triệu VND/tháng."
        }
    ]
}
