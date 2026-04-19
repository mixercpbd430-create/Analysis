method = {
    "id": 37,
    "title": "Cost-Benefit Analysis - Phân tích chi phí lợi ích",
    "short_name": "Cost-Benefit Analysis",
    "icon": "💰",
    "pillar": "Early Management",
    "description": "Đánh giá kinh tế các phương án đầu tư/cải tiến bằng cách so sánh TỔNG CHI PHÍ vs TỔNG LỢI ÍCH — để ra quyết định đúng đắn.",
    "meaning": """
<p><strong>Cost-Benefit Analysis (CBA — Phân tích Chi phí - Lợi ích)</strong> là phương pháp đánh giá kinh tế: So sánh TỔNG chi phí bỏ ra với TỔNG lợi ích nhận được → xác định có ĐÁNG ĐẦU TƯ hay không.</p>
<p><em>Nói đơn giản: CBA trả lời câu hỏi "Bỏ ra 1 đồng, thu được bao nhiêu đồng?" → Nếu thu > chi → ĐẦU TƯ. Nếu chi > thu → KHÔNG ĐẦU TƯ (hoặc tìm phương án khác).</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 4 chỉ số CBA quan trọng nhất</div>
    <p><strong>1. ROI (Return On Investment — Tỷ suất hoàn vốn)</strong> = (Lợi ích ròng ÷ Chi phí) × 100%<br>
    → ROI = 200% nghĩa là: Đầu tư 1 tỷ → Thu lợi 2 tỷ → Lãi 1 tỷ<br><br>
    <strong>2. Payback Period (Thời gian hoàn vốn)</strong> = Vốn đầu tư ÷ Tiết kiệm hàng năm<br>
    → Payback = 2 năm nghĩa là: Sau 2 năm → lấy lại vốn, từ năm 3 trở đi → LÃI!<br><br>
    <strong>3. NPV (Net Present Value — Giá trị hiện tại ròng)</strong> = Tổng dòng tiền tương lai QUY VỀ hiện tại - Đầu tư ban đầu<br>
    → NPV > 0: Dự án có lãi → ĐÁNG ĐẦU TƯ. NPV < 0: Lỗ → KHÔNG đầu tư<br><br>
    <strong>4. BCR (Benefit-Cost Ratio — Tỷ lệ lợi ích/chi phí)</strong> = Tổng lợi ích ÷ Tổng chi phí<br>
    → BCR > 1: Lợi ích > Chi phí → ĐÁNG ĐẦU TƯ. BCR < 1: Không đáng</p>
</div>
""",
    "purpose": """
<ul>
    <li>Ra quyết định đầu tư/cải tiến DỰA TRÊN DỮ LIỆU — không dùng cảm tính!</li>
    <li>So sánh NHIỀU phương án để chọn phương án TỐI ƯU NHẤT (lợi ích cao nhất, rủi ro thấp nhất)</li>
    <li>Thuyết phục Ban Giám đốc phê duyệt ngân sách — "đầu tư 2 tỷ, tiết kiệm 5 tỷ trong 5 năm"</li>
    <li>Ưu tiên hóa danh sách dự án — nếu có 10 dự án nhưng chỉ đủ ngân sách cho 3 → chọn 3 dự án ROI cao nhất</li>
    <li>Đánh giá RỦI RO tài chính — "nếu doanh số chỉ đạt 60% dự kiến, dự án vẫn có lãi không?"</li>
    <li>Theo dõi kết quả thực tế vs kế hoạch — sau khi đầu tư, lợi ích thực có đạt như dự tính?</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định phạm vi và các phương án</div>
        <div class="step-card__desc">Mô tả rõ dự án/cải tiến: Mua máy mới? Lắp biến tần? Đào tạo NV? Xác định base case (phương án gốc — KHÔNG LÀM GÌ) vs alternatives (các phương án thay thế). Xác định thời gian đánh giá: Thiết bị → 5-10 năm. Cải tiến nhỏ → 1-3 năm. Xây dựng → 10-20 năm.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Liệt kê và ĐỊNH LƯỢNG tất cả chi phí (Costs)</div>
        <div class="step-card__desc"><strong>CAPEX (vốn đầu tư ban đầu)</strong>: Mua thiết bị, lắp đặt, chạy thử (commissioning). <strong>OPEX (chi phí vận hành hàng năm)</strong>: Bảo trì, nhân công, năng lượng, vật tư tiêu hao. <strong>Chi phí ẨN (hidden costs)</strong>: Đào tạo NV sử dụng thiết bị mới, dừng SX trong lúc lắp đặt (opportunity cost — chi phí cơ hội), chi phí xử lý thiết bị cũ.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Liệt kê và ĐỊNH LƯỢNG tất cả lợi ích (Benefits)</div>
        <div class="step-card__desc"><strong>Lợi ích HỮU HÌNH (tangible — đo được bằng tiền)</strong>: Giảm chi phí SX, tăng sản lượng, giảm phế phẩm, giảm năng lượng, giảm nhân công. <strong>Lợi ích VÔ HÌNH (intangible — khó đo bằng tiền nhưng quan trọng)</strong>: Tăng an toàn, tăng tinh thần NV (morale), hình ảnh thương hiệu (brand image), tuân thủ pháp luật (compliance). Lưu ý: Lợi ích vô hình cũng cần CỐ GẮNG quy ra tiền! (ví dụ: giảm 1 tai nạn = tiết kiệm 200 triệu chi phí bồi thường + y tế)</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Tính toán, phân tích độ nhạy, và ra quyết định</div>
        <div class="step-card__desc">Tính ROI, Payback, NPV, BCR cho từng phương án. Sensitivity analysis (phân tích độ nhạy — kịch bản): Best case (lạc quan) / Likely case (khả năng nhất) / Worst case (xấu nhất) → Dự án vẫn có lãi trong worst case? So sánh các phương án → Chọn phương án có NPV cao nhất (hoặc Payback ngắn nhất). Trình bày cho BGĐ phê duyệt.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Mua máy ép viên mới vs Sửa chữa máy cũ — Đầu tư 5 tỷ hay tiếp tục sửa?",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Pellet mill (máy ép viên) 15 năm tuổi: Breakdown 480 giờ/năm. Chi phí sửa chữa 800 triệu/năm. Mua máy mới giá 5 tỷ VND. Ban Giám đốc hỏi: \"Nên mua hay tiếp tục sửa?\"",
            "analysis": "Phương án A — Giữ máy cũ (base case — không làm gì):\n• Sửa chữa: 800 triệu/năm\n• Mất sản lượng do dừng máy: 480h × 35T/h × 500,000 VND/T = 1.2 tỷ/năm\n• Lãng phí năng lượng (motor cũ hiệu suất kém): 400 triệu/năm\n→ Tổng chi phí GIỮ MÁY CŨ: 2.4 tỷ/năm! (nhiều người không nhận ra vì \"không bỏ tiền mua máy\")\n\nPhương án B — Mua máy mới 5 tỷ:\n• CAPEX: 5 tỷ (máy + lắp đặt + commissioning)\n• Sửa chữa: Chỉ 200 triệu/năm (máy mới, ít hỏng)\n• Mất sản lượng: 100h × 35T × 500K = 200 triệu/năm (breakdown giảm 75%)\n• Tiết kiệm năng lượng: 300 triệu/năm (motor IE3 hiệu suất cao)\n→ Lợi ích ròng so với giữ cũ: 2.4 - (200+200-300+200) = 2 tỷ/năm",
            "result": "So sánh 5 năm:\n• NPV (5 năm, discount rate 10%): Phương án A = -9.1 tỷ (tốn 2.4 tỷ/năm quy về hiện tại). Phương án B = -5 + 7.6 = +2.6 tỷ!\n• Payback mua mới: 5 tỷ ÷ 2 tỷ/năm = 2.5 năm → Sau 2.5 năm lấy lại vốn!\n• ROI: 40%/năm\n\n→ Quyết định: MUA MÁY MỚI! Tưởng tốn 5 tỷ nhưng thực tế TIẾT KIỆM 2.6 tỷ sau 5 năm!\n→ Bài học: \"Giữ máy cũ\" KHÔNG PHẢI là \"không tốn tiền\" — chi phí ẨN (sửa + dừng máy + năng lượng) rất lớn!"
        },
        {
            "title": "Lắp biến tần (VFD) cho máy nghiền — Payback 5 tháng!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Hammer mill (máy nghiền búa) 110 kW chạy full speed 24/7. Có nên lắp VFD (Variable Frequency Drive — biến tần) để điều chỉnh tốc độ theo loại NL?",
            "analysis": "Chi phí:\n• VFD 110kW: 120 triệu VND\n• Lắp đặt + cáp: 30 triệu\n→ Tổng CAPEX: 150 triệu VND\n\nLợi ích:\n• Tiết kiệm năng lượng 25%: 110kW × 25% × 7,000 giờ/năm × 2,000 VND/kWh = 385 triệu/năm!\n• Giảm ứng suất cơ khí (không chạy max liên tục) → Tuổi thọ bearing tăng 50% → Tiết kiệm thêm 30 triệu/năm phụ tùng\n• Giảm tiếng ồn → cải thiện môi trường làm việc (intangible)\n→ Tổng lợi ích: ~415 triệu/năm",
            "result": "Đánh giá:\n• Payback: 150 ÷ 415 = 4.3 tháng → Sau 4.3 tháng lấy lại vốn!\n• ROI: 277%/năm!\n• NPV (5 năm): +1.6 tỷ VND\n\n→ Đây là dự án \"no-brainer\" (không cần suy nghĩ — ĐẦU TƯ NGAY!)\n→ Bài học: Dự án payback < 12 tháng → phê duyệt ngay, KHÔNG CẦN phân tích NPV phức tạp!"
        },
        {
            "title": "Tự động hóa đóng bao — So 8 người vs máy tự động",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Line đóng bao hiện tại: 8 nhân viên/ca × 3 ca. Đề xuất mua máy đóng bao tự động giá 3 tỷ VND → giảm xuống 2 NV/ca.",
            "analysis": "Chi phí tự động hóa:\n• CAPEX: 3 tỷ (máy + lắp đặt + đào tạo)\n• OPEX: 2 NV/ca × 3 ca × 8 triệu/người/năm = 48 triệu + Bảo trì 100 triệu/năm = 148 triệu/năm\n\nChi phí HIỆN TẠI (giữ manual):\n• 8 NV × 3 ca × 8 triệu = 192 triệu/năm chỉ riêng lương\n• Lỗi đóng bao do con người: 50 triệu/năm (sai trọng lượng, bao rách, nhầm nhãn...)\n→ Tiết kiệm = (192+50) - 148 = 194 triệu/năm (chênh lệch khiêm tốn!)\n\nNhưng thêm lợi ích VÔ HÌNH:\n• Sản lượng tăng 20% (máy nhanh hơn người) → doanh thu thêm ~500 triệu/năm\n• Consistency chất lượng → ít khiếu nại → giữ khách hàng",
            "result": "Đánh giá:\n• Payback (chỉ tính tangible): 3,000 ÷ 194 = 15.5 tháng\n• Payback (tính cả throughput tăng): 3,000 ÷ 694 = 4.3 tháng\n• NPV (7 năm): +5.8 tỷ\n\nLƯU Ý QUAN TRỌNG: 18 NV (6/ca × 3 ca) bị ảnh hưởng → cần KẾ HOẠCH BỐ TRÍ LẠI: Chuyển sang line khác, đào tạo vận hành/bảo trì máy mới, phụ trách AM/PM...\n→ CBA không chỉ tính tiền — phải tính cả YẾU TỐ CON NGƯỜI!"
        },
        {
            "title": "Hệ thống bảo trì dự đoán (PdM) — Payback 1 tháng!",
            "industry": "Sản xuất chung",
            "situation": "Xem xét đầu tư hệ thống CBM (Condition Based Monitoring — giám sát tình trạng): Cảm biến rung + camera nhiệt + phần mềm. Chi phí: 2 tỷ VND.",
            "analysis": "Hiện trạng (reactive — chờ hỏng mới sửa):\n• Breakdown: 800 giờ/năm\n• Thiệt hại mất sản lượng: 800h × 50 triệu/h = 40 tỷ/năm! (con số BẤT NGỜ lớn)\n• Chi phí sửa chữa khẩn cấp: 2 tỷ/năm (phụ tùng gấp, OT KTV, thuê ngoài...)\n→ Tổng thiệt hại từ reactive: 42 tỷ/năm!\n\nVới PdM (dự đoán trước — sửa TRƯỚC KHI hỏng):\n• Breakdown giảm 60%: Thiệt hại giảm 24 tỷ\n• Sửa theo kế hoạch (rẻ hơn gấp): Tiết kiệm 1 tỷ/năm\n• OPEX PdM: 300 triệu/năm (lương analyst + calibration cảm biến)\n→ Lợi ích ròng: ~25 tỷ/năm (!)",
            "result": "Đánh giá:\n• Payback: 2,000 ÷ (25,000/12) = 1 THÁNG!\n• NPV: Con số rất lớn (astronomical)\n• Ngay cả nếu lợi ích chỉ đạt 10% ước tính → vẫn payback Bài học CBA: Nhiều khi chi phí \"không đầu tư\" LỚN HƠN NHIỀU so với chi phí đầu tư! Breakdown 800h × 50 triệu/h = 40 tỷ mỗi năm nhưng vì không ai TÍNH nên không ai biết!"
        },
        {
            "title": "Đèn LED — ROI 680%, không cần phân tích!",
            "industry": "Sản xuất chung",
            "situation": "Thay 500 bóng metal halide 400W bằng LED 150W. Chi phí: 250 triệu VND.",
            "analysis": "Chi phí: 250 triệu (mua đèn LED + lắp đặt)\n\nLợi ích:\n• Tiết kiệm điện: 500 bóng × (400-150)W × 6,000 giờ × 2,000 VND/kWh = 1.5 tỷ/năm!\n• Tiết kiệm bảo trì: LED tuổi thọ 50,000 giờ (gấp 5 lần bóng cũ 10,000 giờ) → không phải thay bóng thường xuyên → tiết kiệm 200 triệu/năm nhân công thay bóng\n→ Tổng lợi ích: 1.7 tỷ/năm!",
            "result": "Đánh giá:\n• Payback: 250 ÷ 1,700 = 1.8 THÁNG!!\n• ROI: 680%/năm!\n• BCR: 6.8 (đầu tư 1 đồng → thu 6.8 đồng)\n\n→ Đây là dự án \"just do it\" — KHÔNG CẦN làm CBA phức tạp! Payback < 2 tháng, triển khai NGAY!\n→ Nếu nhà máy bạn vẫn dùng bóng metal halide / huỳnh quang → đây là cơ hội tiết kiệm DỄ NHẤT, NHANH NHẤT!"
        },
        {
            "title": "Đào tạo TPM — Đầu tư 500 triệu, thu 2.5 tỷ!",
            "industry": "Đa ngành",
            "situation": "Chương trình đào tạo TPM: 500 triệu/năm (trainer + tài liệu + thời gian NV nghỉ SX để học). CEO hỏi: \"Có ĐÁNG hay chỉ tốn thời gian?\"",
            "analysis": "Chi phí đào tạo: 500 triệu/năm (bao gồm thuê giảng viên, in tài liệu, workshop, và chi phí cơ hội khi NV nghỉ SX để học)\n\nLợi ích HỮU HÌNH (tangible — đo được):\n• OEE tăng 5% → sản lượng thêm → 2 tỷ/năm\n• Breakdown giảm (nhờ AM + PM cải tiến) → tiết kiệm 300 triệu/năm chi phí bảo trì\n• Reject giảm (nhờ operator giỏi hơn) → tiết kiệm 200 triệu/năm phế phẩm\n→ Tổng tangible: 2.5 tỷ/năm\n\nLợi ích VÔ HÌNH (intangible): Tinh thần NV tăng (\"công ty đầu tư cho mình\"), turnover giảm, văn hóa cải tiến, an toàn tốt hơn",
            "result": "Đánh giá:\n• ROI: 2,500/500 = 5:1 → Mỗi 1 đồng đào tạo → thu 5 đồng!\n• Ngay cả nếu chỉ 50% lợi ích quy cho đào tạo (các yếu tố khác cũng đóng góp) → vẫn 2.5:1!\n• Tính cả intangible → excellent investment\n\n→ Khuyến nghị: Chương trình đào tạo TPM HÀNG NĂM\n→ Bài học CBA: Đào tạo là đầu tư CÓ HOÀN VỐN, không phải chi phí!"
        },
        {
            "title": "An toàn lao động — KHÔNG tính ROI trên mạng người!",
            "industry": "Sản xuất chung",
            "situation": "Nâng cấp an toàn: Rào che máy (machine guarding) + khóa liên động (interlock) + nút dừng khẩn (emergency stop). Chi phí: 800 triệu.",
            "analysis": "Chi phí: 800 triệu (thiết kế + mua + lắp đặt + đào tạo)\n\nLợi ích hữu hình:\n• Chi phí trung bình 1 tai nạn: 200 triệu (y tế + bảo hiểm + pháp lý + dừng SX + tác động tinh thần)\n• Lịch sử: 2 tai nạn/năm = 400 triệu/năm\n• Sau nâng cấp: Dự kiến 0.3 tai nạn/năm = 60 triệu/năm\n→ Tiết kiệm: 340 triệu/năm → Payback: 2.4 năm\n\nNhưng...: Payback 2.4 năm có vẻ \"lâu\" so với VFD (5 tháng) hay LED (2 tháng).",
            "result": "Quyết định: ĐẦU TƯ NGAY LẬP TỨC — KHÔNG CẦN TÍNH ROI!\n\nTại sao?\n• Tính mạng con người > Mọi tính toán tài chính! Không có con số nào đo được giá trị 1 mạng người\n• Tuân thủ pháp luật: Bắt buộc theo Luật An toàn Vệ sinh Lao động\n• Phạt nếu không tuân thủ: 500 triệu VND/sự kiện + có thể bị đình chỉ SX\n• Rủi ro nếu không đầu tư: Tai nạn nghiêm trọng → bồi thường hàng tỷ + tù hình sự cho người quản lý\n\n→ Bài học CBA quan trọng nhất: Có những dự án KHÔNG CẦN và KHÔNG NÊN tính ROI — an toàn, môi trường, sức khỏe con người."
        },
        {
            "title": "Tự sản xuất (Make) vs Mua ngoài (Buy) — Bài toán kinh điển",
            "industry": "Cơ khí",
            "situation": "Chi tiết X: Hiện mua ngoài 50,000 VND/chiếc × 100,000 chiếc/năm = 5 tỷ/năm. Có máy CNC rảnh công suất. Nên tự sản xuất?",
            "analysis": "Phương án Buy (mua ngoài — hiện tại): 50,000 VND/chiếc × 100,000 = 5 tỷ/năm. Ưu: Không đầu tư, linh hoạt, NCC chịu rủi ro\n\nPhương án Make (tự sản xuất):\n• CAPEX: CNC machine 2 tỷ + tooling (dụng cụ cắt, fixture) 200 triệu + setup 100 triệu = 2.3 tỷ\n• Variable cost (chi phí biến đổi): NL 20K + nhân công 10K + overhead 8K = 38,000 VND/chiếc\n• Capacity: Máy CNC có đủ năng lực SX 120,000 chiếc (còn dư 20%)\n→ Tiết kiệm mỗi chiếc: 50K - 38K = 12,000 VND → 1.2 tỷ/năm!",
            "result": "Đánh giá:\n• Payback: 2,300 ÷ 1,200 = 1.9 năm\n• NPV (5 năm): +2.2 tỷ\n\nNhưng xem xét thêm:\n• NCC cung cấp SỰ LINH HOẠT khi demand thay đổi (tăng/giảm đơn không cần lo máy)\n• Tự SX cần quản lý thêm (chất lượng, tồn kho, bảo trì CNC...)\n\n→ Khuyến nghị HYBRID (kết hợp): 70% tự SX (phần ổn định) + 30% mua NCC (buffer cho biến động). → Tiết kiệm 70% lợi ích, giữ linh hoạt!"
        },
        {
            "title": "Thuê ngoài logistics vs Tự vận chuyển — Hybrid là tối ưu!",
            "industry": "Logistics",
            "situation": "Đội xe 20 chiếc, chi phí vận hành 4 tỷ/năm. Công ty 3PL (nhà cung cấp logistics bên thứ 3) báo giá 3.5 tỷ/năm cho cùng dịch vụ. Nên outsource?",
            "analysis": "Phương án A — Giữ đội xe (in-house):\n• Chi phí: 4 tỷ/năm (xăng + tài xế + bảo trì + khấu hao + bảo hiểm + quản lý)\n• Ưu: Kiểm soát hoàn toàn, linh hoạt giao hàng gấp, mang thương hiệu công ty\n\nPhương án B — Thuê 3PL hoàn toàn:\n• Chi phí: 3.5 tỷ/năm → Tiết kiệm 500 triệu\n• Rủi ro: Mất kiểm soát chất lượng dịch vụ. Phạt SLA (Service Level Agreement) nếu 3PL giao trễ → ước tính 200 triệu rủi ro/năm\n→ Net saving thực tế: 500 - 200 = 300 triệu/năm (không nhiều lắm!)",
            "result": "Đánh giá:\n• Full outsource tiết kiệm 300 triệu nhưng mất kiểm soát — rủi ro mất khách hàng nếu 3PL giao kém\n• Full in-house tốn hơn 500 triệu nhưng kiểm soát tốt\n\n→ Khuyến nghị HYBRID: Core routes (tuyến chính, khách hàng lớn) → giữ đội xe 15 chiếc (80% volume). Peak + tuyến xa → thuê 3PL (20%)\n• Bán 5 xe cũ → thu hồi vốn\n• Giảm chi phí nhân viên quản lý xe\n• Linh hoạt mùa peak: Thuê thêm 3PL, không cần mua thêm xe\n→ Chi phí hybrid: ~3.2 tỷ → Tiết kiệm 800 triệu vs full in-house!"
        },
        {
            "title": "Chương trình R&D — Rủi ro cao nhưng kỳ vọng lớn!",
            "industry": "Đa ngành",
            "situation": "Phát triển enzyme độc quyền cho thức ăn thủy sản. Chi phí R&D: 5 tỷ trong 3 năm. Xác suất thành công: 40%. Nếu thành công: Thay thế enzyme nhập khẩu, tiết kiệm 3 tỷ/năm + Bán license thu 2 tỷ/năm.",
            "analysis": "Đây là bài toán CBA với RỦI RO CAO:\n\nNếu THÀNH CÔNG (40%): Lợi ích = 5 tỷ/năm × 10 năm = 50 tỷ (quy NPV ~30 tỷ)\nNếu THẤT BẠI (60%): Mất 5 tỷ sunk cost (chi phí chìm — không thu hồi được)\n\nExpected Value (giá trị kỳ vọng) = 40% × 30 tỷ − 5 tỷ = +7 tỷ!\n→ Mặc dù 60% thất bại, nhưng nếu thành công → lợi ích quá lớn → kỳ vọng DƯƠNG!",
            "result": "Quyết định: ĐẦU TƯ — nhưng THEO GIAI ĐOẠN (stage-gate approach)!\n\n• Phase 1 (Lab proof — 1 tỷ): Chứng minh concept trong phòng thí nghiệm. Nếu pass → tiếp\n• Phase 2 (Pilot — 2 tỷ): Sản xuất thử quy mô nhỏ. Nếu pass → tiếp\n• Phase 3 (Scale-up — 2 tỷ): Sản xuất thương mại\n\n→ Nếu Phase 1 thất bại → DỪNG → chỉ mất 1 tỷ (không mất 5 tỷ!)\n→ Bài học CBA cho dự án rủi ro cao: Chia nhỏ để giảm rủi ro! review sau mỗi phase."
        }
    ]
}
