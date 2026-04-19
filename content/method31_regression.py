method = {
    "id": 31,
    "title": "Regression Analysis - Phân tích hồi quy tương quan",
    "short_name": "Regression Analysis",
    "icon": "📐",
    "pillar": "Overview",
    "description": "Phân tích mối tương quan và xây dựng công thức toán học giữa thông số đầu vào và kết quả đầu ra — để DỰ ĐOÁN và kiểm soát chất lượng.",
    "meaning": """
<p><strong>Regression Analysis (Phân tích hồi quy)</strong> là phương pháp thống kê xây dựng mô hình toán (công thức) mô tả mối quan hệ giữa biến kết quả (Y) và biến thông số (X).</p>
<p><em>Nói đơn giản: Regression trả lời câu hỏi "Khi X tăng/giảm, Y sẽ thay đổi bao nhiêu?" — và cho bạn 1 công thức DỰ ĐOÁN được kết quả!</em></p>
<p>Ví dụ: "Khi nhiệt độ ép viên tăng thêm 5°C, PDI sẽ tăng bao nhiêu %?" → Regression tính ra: PDI tăng 6% → bạn có thể ĐIỀU CHỈNH nhiệt để đạt PDI mong muốn!</p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Các loại Regression chính</div>
    <p><strong>1. Hồi quy tuyến tính đơn (Simple Linear)</strong>: Y = a + bX — 1 biến X, mối quan hệ đường thẳng<br>
    <strong>2. Hồi quy đa biến (Multiple Linear)</strong>: Y = a + b₁X₁ + b₂X₂ + ... — nhiều biến X ảnh hưởng đến Y<br>
    <strong>3. Hồi quy phi tuyến (Polynomial/Nonlinear)</strong>: Y = a + bX + cX² — mối quan hệ đường cong<br><br>
    <strong>R² (Hệ số xác định)</strong>: Cho biết mô hình giải thích được bao nhiêu % sự biến đổi của Y<br>
    • R² = 0.95 → Mô hình giải thích 95% — rất tốt!<br>
    • R² = 0.50 → Mô hình chỉ giải thích 50% — còn nhiều yếu tố khác chưa tính<br><br>
    <strong>r (Hệ số tương quan)</strong>: Đo mức độ "đi cùng" giữa X và Y<br>
    • r = +1: X tăng → Y tăng (tương quan thuận hoàn hảo)<br>
    • r = -1: X tăng → Y giảm (tương quan nghịch hoàn hảo)<br>
    • r = 0: X và Y không liên quan với nhau</p>
</div>
""",
    "purpose": """
<ul>
    <li>Xác định MỐI QUAN HỆ giữa thông số quá trình và kết quả — "X có thực sự ảnh hưởng đến Y không?"</li>
    <li>DỰ ĐOÁN kết quả dựa trên thông số đầu vào — nhập X vào công thức → biết trước Y sẽ ra bao nhiêu!</li>
    <li>Tìm thông số ảnh hưởng LỚN NHẤT — trong 10 yếu tố, yếu tố nào đóng góp nhiều nhất?</li>
    <li>Xây dựng công thức dự báo (predictive model) — dùng mỗi ngày để kiểm soát sản xuất</li>
    <li>Kiểm tra giả thuyết — "Mọi người nói tốc độ ảnh hưởng nhiều nhất, nhưng dữ liệu nói NHIỆT ĐỘ mới đúng!"</li>
    <li>Hỗ trợ bảo trì dự đoán — "Khi rung động đạt mức X, bao lâu nữa bearing sẽ hỏng?"</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Thu thập dữ liệu X (nguyên nhân) và Y (kết quả)</div>
        <div class="step-card__desc">Xác định rõ: Y là gì (PDI, trọng lượng, tỷ lệ lỗi...)? X là gì (nhiệt độ, áp suất, tốc độ...)? Thu thập ÍT NHẤT 30 cặp dữ liệu (X,Y) — càng nhiều càng chính xác. Kiểm tra dữ liệu: loại bỏ điểm bất thường (outlier), bổ sung dữ liệu thiếu (missing).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Vẽ biểu đồ phân tán và phân tích tương quan</div>
        <div class="step-card__desc">Vẽ scatter plot (biểu đồ phân tán) — mỗi điểm là 1 cặp (X,Y). NHÌN bằng mắt: Các điểm có xu hướng đi cùng hướng không? Tính hệ số tương quan r: |r| > 0.7 → tương quan mạnh (đáng để làm regression). |r| < 0.3 → tương quan yếu (X và Y không liên quan nhiều). Kiểm tra xem mối quan hệ có phải đường thẳng hay đường cong.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xây dựng mô hình hồi quy (công thức)</div>
        <div class="step-card__desc">Dùng phần mềm (Excel, Minitab, Python) để tính phương trình hồi quy: Y = a + bX. Kiểm tra R² (mô hình tốt: R² > 0.7), p-value (yếu tố có ý nghĩa: p < 0.05). Kiểm tra phần dư (residuals — sai số giữa dự đoán và thực tế) — phải ngẫu nhiên, không có pattern. Thử mô hình trên dữ liệu MỚI để xác nhận (validation).</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Ứng dụng công thức và cập nhật</div>
        <div class="step-card__desc">Dùng công thức để DỰ ĐOÁN kết quả trước khi sản xuất — nhập thông số → biết trước kết quả. Tìm vùng thông số tối ưu (process window) — khoảng X cho Y đạt spec. Cập nhật mô hình định kỳ khi có dữ liệu mới hoặc khi quá trình thay đổi.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Độ ẩm NL vs PDI viên thức ăn — Tìm vùng tối ưu",
            "industry": "Thức ăn chăn nuôi",
            "situation": "PDI (Pellet Durability Index — chỉ số độ bền viên) dao động 88-96%. Nghi ngờ độ ẩm (moisture) nguyên liệu đầu vào ảnh hưởng. Câu hỏi: Moisture bao nhiêu % thì PDI tốt nhất?",
            "analysis": "Thu thập 50 cặp dữ liệu (moisture NL, PDI) trong 2 tháng. Vẽ scatter plot → thấy rõ xu hướng: moisture tăng → PDI tăng.\n\nPhương trình hồi quy: PDI = 78.5 + 1.2 × Moisture%\n• R² = 0.78 → mô hình giải thích 78% biến động PDI (khá tốt!)\n• Hệ số 1.2 nghĩa là: Mỗi 1% moisture tăng → PDI tăng 1.2 điểm\n• Tính ngược: PDI ≥ 93% → cần Moisture ≥ (93-78.5)/1.2 = 12.1%\n→ Vùng tối ưu: Moisture 13-15% cho PDI > 93%",
            "result": "Ứng dụng thực tế:\n• Kiểm soát moisture NL vào 13-15% → PDI ổn định 93-96%\n• Khi moisture NL Bài học: 1 phương trình đơn giản giúp DỰ ĐOÁN chất lượng sản phẩm từ nguyên liệu đầu vào."
        },
        {
            "title": "Tuổi thọ die vs PDI — Biết trước khi nào cần thay",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Die (khuôn ép viên) chạy bao lâu thì cần thay? Hiện thay theo 'kinh nghiệm' — có người thay 800 giờ, có người chờ tới 1,500 giờ. Cần công thức tính chính xác.",
            "analysis": "Thu thập dữ liệu 30 die: Số giờ chạy (DieHours) vs PDI và năng suất (Throughput).\n\n2 phương trình hồi quy:\n• PDI = 96.5 - 0.003 × DieHours → PDI giảm 0.003 điểm mỗi giờ chạy\n• Throughput = 38 - 0.005 × DieHours → Năng suất giảm 0.005 T/h mỗi giờ\n\nTính ngược điểm giới hạn:\n• PDI rớt 93% (spec) khi: DieHours = (96.5-93)/0.003 = 1,167 giờ\n• Throughput giảm 6 T/h (từ 38 xuống 32) khi: DieHours = 6/0.005 = 1,200 giờ\n→ Nên thay die tại ~1,200 giờ — trước khi PDI rớt spec!",
            "result": "Ứng dụng:\n• Lập kế hoạch thay die CHỦ ĐỘNG (preventive replacement) tại 1,200 giờ — không chờ đến khi PDI rớt mới thay\n• Ghi số giờ chạy trên bảng theo dõi → khi gần 1,100 giờ → chuẩn bị die mới sẵn\n• Tiết kiệm 50% thời gian dừng máy: thay chủ động nhanh hơn (lên lịch trước) vs hỏng bất ngờ (khẩn cấp, chờ phụ tùng)\n→ Bài học: Regression biến 'kinh nghiệm' thành 'công thức' — ai cũng dùng được, không phụ thuộc 1 người."
        },
        {
            "title": "Nhiều yếu tố cùng ảnh hưởng — Multiple Regression",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Năng suất ép viên (output) dao động 25-38 T/h. Nhiều yếu tố nghi ngờ: nhiệt hơi (steam temp), ẩm NL (moisture), hàm lượng mỡ (fat content). Yếu tố nào QUAN TRỌNG NHẤT?",
            "analysis": "Hồi quy đa biến (Multiple Regression — nhiều X, 1 Y):\n\nOutput (T/h) = 5.2 + 8.5×SteamTemp + 3.2×Moisture - 0.4×FatContent\n• R² = 0.85 → mô hình giải thích 85% biến động năng suất\n\nĐọc hệ số:\n• Steam temp: hệ số 8.5 — LỚN NHẤT! → Nhiệt hơi ảnh hưởng mạnh nhất đến năng suất\n• Moisture: hệ số 3.2 → ảnh hưởng vừa\n• Fat content: hệ số -0.4 (dấu âm!) → Mỡ nhiều GIẢM năng suất (nhựa mỡ làm trơn die, viên ra chưa ép chặt)",
            "result": "Ứng dụng:\n• Steam temp 80-85°C là yếu tố CẦN KIỂM SOÁT CHẶT NHẤT (vì hệ số lớn nhất). Lắp PID controller cho van hơi\n• Fat > 5% → giảm năng suất → thêm chất kết dính (binder) bù lại\n• Dự đoán trước mỗi mẻ: Biết 3 thông số → nhập vào công thức → biết năng suất dự kiến → lên lịch giao hàng chính xác\n• Ví dụ: Steam 82°C + Moisture 14% + Fat 3% → Output = 5.2 + 8.5×82 + 3.2×14 - 0.4×3 = 35.8 T/h"
        },
        {
            "title": "Rung động vs tuổi thọ bạc đạn — Bảo trì dự đoán",
            "industry": "Sản xuất chung",
            "situation": "Hệ thống giám sát rung (vibration monitoring) lắp trên 50 motor/bơm. Câu hỏi: Khi rung động đạt mức nào thì bạc đạn (bearing) sắp hỏng? Còn bao lâu nữa?",
            "analysis": "Thu thập dữ liệu 80 trường hợp bearing hỏng: Mức rung RMS (mm/s) vs Số ngày đến khi hỏng.\n\nSurvival regression (hồi quy sinh tồn — dự đoán thời gian đến khi sự kiện xảy ra):\nNgày_đến_hỏng = 500 × e^(-0.3 × Vibration_RMS)\n\nTra bảng:\n• Rung 4 mm/s → ~150 ngày nữa mới hỏng\n• Rung 7 mm/s → ~60 ngày\n• Rung 10 mm/s → ~25 ngày — SẮP HỎNG!",
            "result": "Xây dựng hệ thống cảnh báo 3 mức dựa trên model:\n• Rung 5 mm/s (VÀNG — lên kế hoạch): Còn ~100 ngày → đặt phụ tùng, lên lịch thay bearing vào đợt dừng máy gần nhất\n• Rung 7 mm/s (CAM — 1 tháng): Còn ~60 ngày → lên lịch cụ thể, chuẩn bị nhân lực\n• Rung 10 mm/s (ĐỎ — khẩn cấp): Còn ~25 ngày → thay ngay khi có thể!\n→ Bài học: Regression cho phép CHUYỂN TỪ bảo trì phản ứng (chờ hỏng) → bảo trì DỰ ĐOÁN (biết trước khi nào hỏng)."
        },
        {
            "title": "Giờ đào tạo vs tỷ lệ lỗi — Đường cong học tập",
            "industry": "Sản xuất chung",
            "situation": "Nhân viên mới luôn có tỷ lệ lỗi cao. Bao nhiêu giờ training thì nhân viên mới đạt chuẩn (defect < 1%)? HR cần biết để lập kế hoạch.",
            "analysis": "Thu thập dữ liệu 40 nhân viên mới: Số giờ đào tạo vs tỷ lệ lỗi.\n\nHồi quy logarit (phi tuyến — vì tỷ lệ lỗi giảm nhanh lúc đầu, chậm dần sau):\nDefect% = 15 × e^(-0.05 × TrainingHours)\n\nĐường cong học tập (learning curve):\n• 0 giờ: 15% lỗi (mới hoàn toàn)\n• 20 giờ: 5.5% lỗi (học nhanh lúc đầu)\n• 40 giờ: 2.0% lỗi\n• 60 giờ: 0.7% lỗi ✓ (đạt chuẩn < 1%)\n• 80 giờ: 0.3% lỗi (plateau — chậm lại, gần bằng NV kinh nghiệm)",
            "result": "Ứng dụng:\n• Tối thiểu 60 giờ training trước khi NV mới được chạy máy độc lập (defect Bài học: Regression chứng minh BẰNG SỐ rằng đầu tư đào tạo mang lại giá trị cụ thể."
        },
        {
            "title": "Tốc độ cắt CNC vs độ nhám bề mặt",
            "industry": "Cơ khí",
            "situation": "Gia công chi tiết CNC: Độ nhám bề mặt (surface roughness Ra) yêu cầu ≤ 0.8 μm (micromet). Kết quả dao động 0.4-2.0 μm. Cần tìm thông số cắt cho Ra đạt yêu cầu.",
            "analysis": "Multiple Regression (3 biến: RPM — tốc độ trục chính, Feed — bước tiến, DOC — chiều sâu cắt):\n\nRa = 3.2 - 0.0008×RPM - 0.15×Feed + 0.02×DOC\n• R² = 0.88 → mô hình giải thích 88% biến động Ra\n\nĐọc hệ số (hệ số âm = tăng X → giảm Ra → tốt):\n• RPM: hệ số -0.0008 → Tăng RPM giảm Ra → RPM là yếu tố quan trọng nhất\n• Feed: hệ số -0.15 → Giảm feed giảm Ra (chạy chậm hơn)\n• DOC: hệ số +0.02 → DOC ít ảnh hưởng, và DOC sâu hơn làm Ra xấu hơn nhẹ",
            "result": "Tối ưu: RPM = 3,000 + Feed = 0.1 mm/vòng → Ra = 0.5 μm (đạt ≤ 0.8 μm!)\n• Dùng model dự đoán: Trước khi gia công → nhập RPM, Feed, DOC vào công thức → biết trước Ra → chỉnh nếu cần\n• Lập bảng tra (look-up table) cho operator: RPM bao nhiêu, Feed bao nhiêu → Ra dự kiến bao nhiêu\n→ Bài học: Multiple regression cho phép TỐI ƯU ĐỒNG THỜI nhiều thông số cắt — so với thử ngẫu nhiên, tiết kiệm hàng chục mẫu thử."
        },
        {
            "title": "Dự báo chi phí sản xuất TACN theo giá NL",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Cần dự báo chi phí sản xuất để đàm phán giá bán hợp đồng 6 tháng. Giá nguyên liệu biến động → chi phí SX dao động → khó báo giá.",
            "analysis": "Multiple Regression:\nChi phí/tấn = 5,200 + 0.65×Giá_Bắp + 0.22×Giá_Đậu_Nành + 0.08×Giá_Bột_Cá + 150×Giá_Điện\n• R² = 0.96 → mô hình giải thích 96% biến động chi phí — rất chính xác!\n\nPhân tích đóng góp:\n• Giá bắp: đóng góp 65% → yếu tố CHI PHỐI chi phí SX\n• Giá đậu nành: 22%\n• Giá bột cá: 8%\n• Giá điện: 5%",
            "result": "Ứng dụng thực tế:\n• Chiến lược mua (hedging): Lock giá bắp trước → ổn định 65% chi phí SX. Bắp ảnh hưởng mạnh nhất nên chỉ cần lock bắp là giảm rủi ro đáng kể\n• Mô hình báo giá tự động: Nhập giá NL thị trường hôm nay → công thức tự tính giá bán đề xuất → đàm phán hợp đồng chính xác, không bị lỗ\n• Độ chính xác dự báo: Từ ±15% (đoán cảm tính) xuống ±4% (model)\n→ Bài học: Regression không chỉ cho kỹ thuật — áp dụng cả cho TÀI CHÍNH và KINH DOANH!"
        },
        {
            "title": "Áp suất nén vs độ cứng viên thuốc — Phi tuyến!",
            "industry": "Dược phẩm",
            "situation": "Viên nén thuốc: Tỷ trọng (density) ảnh hưởng đến tốc độ tan (dissolution). Muốn tìm áp suất nén tối ưu — không quá cứng (chậm tan) không quá mềm (vỡ khi vận chuyển).",
            "analysis": "Regression bậc 2 (Quadratic — phi tuyến):\nDensity = 0.8 + 0.015×Pressure - 0.0001×Pressure²\n• R² = 0.89\n• Đây là đường CONG (parabol) — không phải đường thẳng!\n• Ở áp thấp (30-75 kN): Tăng áp → tăng density (tốt)\n• Ở áp cao (>85 kN): Tăng áp → density GIẢM! Tại sao? Vì viên bị nứt ngang (capping/lamination), cấu trúc bên trong bị phá → density thực tế giảm\n• Đỉnh parabol (áp tối ưu): Pressure = 0.015/(2×0.0001) = 75 kN",
            "result": "Tối ưu từ model:\n• Áp lực nén tối ưu: 75 kN (density cao nhất mà không bị nứt)\n• Vùng vận hành an toàn: 65-85 kN\n• Cài cảnh báo: Áp > 85 kN → DỪNG! Viên sẽ bị nứt\n→ Bài học quan trọng: Không phải mối quan hệ nào cũng là đường thẳng! Regression bậc 2 phát hiện điểm TỐI ƯU ở GIỮA, chứ không phải 'càng cao càng tốt'."
        },
        {
            "title": "Tỷ lệ nước/xi măng vs cường độ bê tông",
            "industry": "Xây dựng",
            "situation": "Bê tông: Tối ưu tỷ lệ nước/xi măng (W/C ratio) cho bê tông cường độ cao. Tỷ lệ W/C ảnh hưởng trực tiếp đến cường độ nén 28 ngày.",
            "analysis": "Hồi quy theo Định luật Abrams (regression mũ):\nCường độ = 120 / 1.5^(W/C)\n• W/C = 0.40 → Cường độ = 47 MPa\n• W/C = 0.35 → Cường độ = 55 MPa\n• W/C = 0.30 → Cường độ = 65 MPa\n• R² = 0.94 → mô hình rất chính xác!\n\n→ Mối quan hệ mũ: Giảm W/C 0.05 → cường độ tăng mạnh. Nhưng W/C quá thấp → bê tông khô, khó thi công → cần phụ gia siêu dẻo (superplasticizer) bù",
            "result": "Ứng dụng:\n• Mục tiêu M500 (cường độ 50 MPa): W/C = 0.32 + superplasticizer 1% để giữ workability (tính thi công)\n• Model validated (kiểm chứng) với 100 kết quả thử nén → dự đoán chính xác ±3 MPa\n• QC thông minh: Đo W/C inline NGÀY ĐỔ → công thức DỰ ĐOÁN cường độ 28 ngày NGAY TỪ NGÀY 1! Không cần chờ 28 ngày mới biết kết quả\n→ Phát hiện sớm mẻ bê tông kém chất lượng → sửa trước khi kết cấu chịu lực."
        },
        {
            "title": "Chỉ số acid vs tuổi thọ dầu chiên — Thay đúng lúc",
            "industry": "Thực phẩm",
            "situation": "Dầu chiên thực phẩm: Khi nào nên thay dầu? Hiện thay cố định 3 ngày/lần theo 'quy định'. Nhưng có mẻ dầu tốt chạy được 4 ngày, mẻ dầu xấu chỉ chạy 2 ngày. Thay cố định → lãng phí hoặc không an toàn.",
            "analysis": "Thu thập 60 mẫu dầu: AV (Acid Value — chỉ số acid — đo mức phân hủy dầu), số ngày sử dụng, số lượt chiên.\n\nRegression: AV = 0.5 + 0.8×Ngày + 0.002×Số_lượt_chiên\n• R² = 0.91 → mô hình chính xác!\n• Giới hạn an toàn thực phẩm: AV ≤ 2.5 (theo quy định)\n• Tính ngược: AV = 2.5 khi Ngày = (2.5 - 0.5 - 0.002×Cycles) / 0.8\n• Với tần suất chiên hiện tại: ~2.5 ngày → nhưng nếu chiên ít (cuối tuần nhẹ) → dầu bền hơn ~3.5 ngày",
            "result": "Chuyển từ thay cố định → thay THEO DỮ LIỆU:\n• Đo AV nhanh (quick test) mỗi ca bằng kit thử (test strip, 30 giây/lần, giá 5,000đ/lần)\n• Thay dầu khi AV tiệm cận 2.0 (chừa safety margin 0.5 trước giới hạn 2.5)\n• Kết quả: Có mẻ dầu dùng 3 ngày, có mẻ 4 ngày (tùy tần suất chiên) thay vì cứng nhắc 3 ngày\n→ Tiết kiệm dầu 15% (tránh thay sớm) + Đảm bảo an toàn 100% (phát hiện dầu xấu sớm)\n→ Mỗi tháng tiết kiệm ~$500."
        },
        {
            "title": "Dự báo doanh số — Lên kế hoạch sản xuất chính xác",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Sản lượng bán hàng TACN biến động theo mùa. Phòng Kinh doanh cần dự báo để Sản xuất lên kế hoạch. Hiện dự báo sai ±20% → sản xuất thừa (tồn kho) hoặc thiếu (mất đơn).",
            "analysis": "Time series regression (hồi quy chuỗi thời gian):\nSales = 20,000 + 500×Tháng + 3,000×sin(2π×Tháng/12) + 0.8×Giá_Heo + Sai_số\n\nGiải thích từng phần:\n• 20,000: Mức cơ bản (baseline)\n• 500×Tháng: Xu hướng tăng trưởng (trend) — mỗi tháng tăng 500 tấn\n• 3,000×sin(): Biến động theo mùa (seasonal) — cuối năm peak, giữa năm thấp\n• 0.8×Giá_Heo: Giá heo tăng → nông dân nuôi nhiều hơn → mua thêm TACN\n• R² = 0.88 → dự báo tốt!",
            "result": "Kết quả ứng dụng:\n• Độ chính xác dự báo: MAPE (Mean Absolute Percentage Error) = 8% (vs 20% trước khi có model)\n• Production planning: Dự báo trước 2 tháng → sản xuất đúng lượng → giảm 25% tồn kho thành phẩm\n• Mua nguyên liệu đúng lúc → giảm rủi ro NL hết hạn trong kho\n→ Bài học: Regression không chỉ dùng trong nhà máy — áp dụng cho DỰ BÁO kinh doanh, tài chính, nhân sự..."
        }
    ]
}
