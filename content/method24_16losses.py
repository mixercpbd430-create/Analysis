method = {
    "id": 24,
    "title": "16 Big Losses / Loss Tree - Phân tích 16 tổn thất lớn",
    "short_name": "16 Big Losses",
    "icon": "🌳",
    "pillar": "Focus Improvement",
    "description": "Phân loại và định lượng 16 tổn thất lớn trong sản xuất theo cấu trúc Cây tổn thất (Loss Tree) để xác định ưu tiên cải tiến.",
    "meaning": """
<p><strong>16 Big Losses (16 Tổn thất lớn)</strong> là hệ thống phân loại TẤT CẢ các tổn thất trong nhà máy sản xuất theo TPM. Bất kỳ hoạt động nào không tạo ra giá trị đều nằm trong 16 loại này:</p>
<ul>
    <li><strong>8 Tổn thất thiết bị</strong>:
        <br>① Hỏng máy đột xuất (Breakdown) — máy dừng do hỏng hóc bất ngờ
        <br>② Chuẩn bị & chỉnh máy (Setup/Adjustment) — thời gian chuyển đổi sản phẩm
        <br>③ Thay dụng cụ (Tool change) — thay dao, die, khuôn theo tuổi thọ
        <br>④ Tổn thất khởi động (Startup) — sản phẩm đầu chưa đạt khi mới chạy máy
        <br>⑤ Dừng ngắn (Minor stop) — máy dừng dưới 5 phút rồi tự chạy lại
        <br>⑥ Giảm tốc độ (Speed loss) — máy chạy chậm hơn thiết kế
        <br>⑦ Phế phẩm & sửa lại (Defect/Rework) — sản phẩm lỗi phải bỏ/làm lại
        <br>⑧ Dừng theo kế hoạch (Shutdown) — vệ sinh, bảo trì kế hoạch
    </li>
    <li><strong>5 Tổn thất con người</strong>:
        <br>⑨ Quản lý (Management) — chờ lệnh, chờ quyết định, họp
        <br>⑩ Vận động (Motion) — đi lại, tìm kiếm dụng cụ, vận chuyển thủ công
        <br>⑪ Tổ chức dây chuyền (Line organization) — mất cân bằng giữa các trạm
        <br>⑫ Tự động hóa thay thế (Automation substitution) — người làm việc máy có thể làm
        <br>⑬ Đo lường & điều chỉnh (Measurement/Adjustment) — thời gian đo kiểm, hiệu chỉnh
    </li>
    <li><strong>3 Tổn thất nguyên vật liệu & năng lượng</strong>:
        <br>⑭ Hao hụt nguyên liệu (Yield loss) — NL đầu vào không thành sản phẩm
        <br>⑮ Lãng phí năng lượng (Energy loss) — điện, gas, hơi tiêu thụ vượt cần thiết
        <br>⑯ Hao mòn vật tư (Consumables) — dầu, mỡ, dao cụ, linh kiện tiêu hao
    </li>
</ul>
<div class="note-box note-box--info">
    <div class="note-title">📌 Loss Tree (Cây tổn thất)</div>
    <p>Loss Tree là sơ đồ cây phân rã tổn thất từ tổng thể xuống chi tiết:<br>
    <strong>Tổng thời gian</strong> → Thời gian kế hoạch + Dừng kế hoạch → <strong>16 loại loss cụ thể</strong> → Nguyên nhân gốc rễ<br>
    Cách đọc: Tổng loss 3000 giờ/năm → Thiết bị 1800h + Con người 700h + Vật tư 500h → Ưu tiên cải tiến loss lớn nhất trước</p>
</div>
""",
    "purpose": """
<ul>
    <li>Nhìn toàn cảnh tất cả tổn thất trong nhà máy — không bỏ sót bất kỳ loại lãng phí nào</li>
    <li>Phân loại tổn thất rõ ràng — biết chính xác mỗi giờ dừng máy thuộc loại nào</li>
    <li>Định lượng bằng số — quy ra giờ hoặc tiền VND để so sánh được</li>
    <li>Ưu tiên theo Pareto — tập trung vào 20% loại loss gây ra 80% tổng tổn thất</li>
    <li>Liên kết trực tiếp với OEE — 8 tổn thất thiết bị chính là nguyên nhân giảm A, P, Q</li>
    <li>Theo dõi tiến độ — so sánh Loss Tree tháng này vs tháng trước để đánh giá hiệu quả cải tiến</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xây dựng cấu trúc Cây tổn thất</div>
        <div class="step-card__desc">Vẽ sơ đồ cây: Tổng thời gian khả dụng → Dừng kế hoạch + Thời gian vận hành → Phân chia theo 16 loại loss. Áp dụng cho từng máy, từng line, hoặc toàn nhà máy.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Thu thập và phân loại dữ liệu</div>
        <div class="step-card__desc">Thu thập dữ liệu vận hành tối thiểu 1-3 tháng. Mỗi lần máy dừng hoặc có tổn thất, ghi nhận và phân loại vào 1 trong 16 loại. Quy đổi tất cả sang đơn vị thống nhất: giờ hoặc tiền (VND). Ví dụ: dừng máy 2 giờ × 50 triệu/giờ = 100 triệu.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Xếp hạng và vẽ biểu đồ Pareto</div>
        <div class="step-card__desc">Tính tổng giá trị mỗi loại loss. Sắp xếp từ lớn nhất → nhỏ nhất. Vẽ biểu đồ Pareto. Thường 3-5 loại loss đầu tiên chiếm 70-80% tổng tổn thất → đây là mục tiêu cải tiến.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Phân tích nguyên nhân gốc rễ và lập dự án Kaizen</div>
        <div class="step-card__desc">Với mỗi top loss, phân tích sâu bằng Why-Why hoặc biểu đồ nhân quả (CE) để tìm nguyên nhân gốc rễ. Lập dự án Kobetsu Kaizen (cải tiến trọng điểm) cho từng top loss. Đặt mục tiêu giảm loss cụ thể, có thời hạn và người chịu trách nhiệm.</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Nhà máy TACN - Cây tổn thất tổng thể",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Nhà máy thức ăn chăn nuôi công suất 300,000 tấn/năm. Tổng thời gian khả dụng 8,760 giờ/năm (24h × 365 ngày). Thời gian sản xuất thực tế chỉ 5,200 giờ. Nghĩa là mất 3,560 giờ — tương đương máy nằm im hơn 148 ngày/năm!",
            "analysis": "Phân loại 3,560 giờ tổn thất theo Loss Tree:\n• Tổn thất thiết bị (Equipment Loss): Hỏng máy đột xuất 580 giờ (16.3%) + Chuyển đổi sản phẩm 420 giờ (11.8%) + Chạy chậm do die mòn 650 giờ (18.3%) + Dừng ngắn (kẹt NL, hơi mất áp) 280 giờ (7.9%)\n• Tổn thất con người (Man Loss): Chờ nguyên liệu về silo 350 giờ + Chờ QC kiểm tra 180 giờ\n• Tổn thất vật tư (Material): Hao hụt nguyên liệu (yield loss) 5% ≈ 15,000 tấn bị thất thoát\n→ Top 3 tổn thất: Chạy chậm (650h) + Hỏng máy (580h) + Chuyển đổi (420h) = chiếm 46.3% tổng loss.",
            "result": "Lập 3 dự án Kobetsu Kaizen cho top 3 loss:\n• Chạy chậm 650h: Xây dựng chương trình quản lý tuổi thọ die — theo dõi số giờ chạy, thay die trước khi mòn quá mức gây giảm tốc\n• Hỏng máy 580h: Lập kế hoạch PM tổng thể (PM Master Plan) — bảo trì định kỳ thay vì chờ hỏng mới sửa\n• Chuyển đổi 420h: Áp dụng SMED (chuyển đổi nhanh) — chuẩn bị sẵn NL, dụng cụ trước khi dừng máy\n→ Mục tiêu giảm 40% tổng tổn thất trong năm đầu, tương đương tăng thêm 1,424 giờ sản xuất = ~40,000 tấn sản phẩm."
        },
        {
            "title": "Máy ép viên (Pellet Mill) - 8 tổn thất thiết bị",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Máy ép viên PM-01 hoạt động 7,200 giờ/năm. OEE chỉ đạt 62% — nghĩa là 38% thời gian bị lãng phí. Cần phân rã chi tiết 38% này thuộc những loại tổn thất nào.",
            "analysis": "Phân tích 8 tổn thất thiết bị chi tiết:\n① Hỏng máy: 480 giờ — nứt die 200h, hỏng bạc đạn (bearing) 120h, motor quá tải 80h, khác 80h\n② Chuyển đổi: 360 giờ — đổi code sản phẩm 300h, thay die 60h\n③ Khởi động: 120 giờ — mỗi lần start mất 15-20 phút làm nóng die\n④ Chạy chậm: 520 giờ — die mòn → phải giảm tốc, không đạt công suất thiết kế\n⑤ Dừng ngắn: 180 giờ — kẹt nguyên liệu, hơi (steam) dao động áp suất\n⑥ Phế phẩm: 216 giờ tương đương — 3% sản phẩm bị vỡ/bở phải làm lại\n⑦ Thay dụng cụ: 96 giờ — thay die và roller theo tuổi thọ\n⑧ Dừng kế hoạch: 48 giờ — PM định kỳ",
            "result": "Top 3 loss: Chạy chậm 520h + Hỏng máy 480h + Chuyển đổi 360h = chiếm 63% tổng tổn thất thiết bị.\nHành động:\n• Chạy chậm: Chương trình quản lý die — theo dõi số giờ chạy mỗi die, lập biểu đồ tương quan giữa tuổi die và tốc độ chạy, thay tại điểm tối ưu (trước khi chạy chậm quá nhiều nhưng không thay sớm lãng phí)\n• Hỏng máy: Kế hoạch bảo trì phòng ngừa chi tiết — kiểm tra bạc đạn bằng đo rung, kiểm tra dòng motor hàng ngày\n• Chuyển đổi: Áp dụng SMED — phân tách thao tác có thể làm khi máy đang chạy (chuẩn bị NL, sẵn die) vs khi máy dừng\n→ Mục tiêu giảm 35% tổng loss."
        },
        {
            "title": "Dây chuyền đóng chai nước giải khát",
            "industry": "Đồ uống",
            "situation": "Line đóng chai nước PET: tổng thời gian sản xuất 6,000 giờ/năm. Hiệu suất dây chuyền (Line Efficiency) chỉ đạt 55% — nghĩa là gần nửa năng lực bị lãng phí.",
            "analysis": "Phân rã tổn thất:\n• Tổn thất thiết bị: Hỏng máy 350 giờ + Dừng ngắn (chai kẹt trên băng chuyền, nhãn kẹt trong máy dán) 480 giờ + Chạy chậm 400 giờ + Chuyển đổi sản phẩm 280 giờ\n• Tổn thất con người: Chờ nhân viên vận hành (vắng, nghỉ giải lao kéo dài) 150 giờ + Thao tác chậm (nhân viên mới chưa thành thạo) 120 giờ\n• Tổn thất vật tư: Phôi chai PET bị lỗi phải bỏ 2%, nhãn bị lệch/rách 1.5%\n→ Dừng ngắn 480 giờ chiếm lớn nhất! Đây là loại loss rất khó thấy — mỗi lần dừng chỉ 1-3 phút nhưng xảy ra hàng trăm lần/ngày.",
            "result": "Ưu tiên cải tiến Dừng ngắn (480 giờ — lớn nhất):\n• Triển khai chương trình Tự bảo trì (Autonomous Maintenance - AM): Hướng dẫn nhân viên vận hành vệ sinh băng chuyền hàng ca (loại bỏ cặn, nước đọng gây trượt chai), chỉnh thanh dẫn (guide rail) đúng kích thước chai\n• Cải tiến Chạy chậm: Quản lý công thức trên PLC — lưu sẵn thông số cho từng sản phẩm, khi chuyển chỉ cần gọi recipe, không chỉnh tay\n→ Mục tiêu hiệu suất dây chuyền tăng từ 55% lên 70%."
        },
        {
            "title": "Nhà máy xi măng - Phân tích tổn thất lò nung",
            "industry": "Xi măng",
            "situation": "Lò nung (kiln) công suất thiết kế 2,500 tấn clinker/ngày. Tỷ lệ vận hành đạt 88% nhưng tiêu thụ năng lượng cao: 780 kcal/kg (mục tiêu 720 kcal/kg) — nghĩa là đang tốn thêm 60 kcal cho mỗi kg clinker.",
            "analysis": "Phân loại loss:\n• Thiết bị: Lò dừng tổng 420 giờ/năm — gạch chịu lửa (refractory) bị mòn/rơi 200 giờ, hỏng cơ khí 120 giờ, sự cố điện 100 giờ\n• Tốc độ: Lượng liệu nạp (kiln feed) giảm 15% vì lớp bám (coating) trong lò làm giảm diện tích → phải giảm feed\n• Năng lượng: Tháp trao đổi nhiệt (preheater) hoạt động kém hiệu quả + cooler (máy làm mát clinker) thu hồi nhiệt kém → nhiệt thất thoát theo khí thải và clinker nóng\n• Vật tư: Phối liệu (raw mix) không ổn định thành phần → lò đốt lãng phí nhiên liệu",
            "result": "Loss Tree cho thấy tổn thất năng lượng chiếm 45% tổng chi phí tổn thất — đây mới là vấn đề nghiêm trọng nhất (không phải dừng máy).\nHành động:\n• Bảo trì cyclone tháp trao đổi nhiệt — vệ sinh tắc nghẽn, sửa vỏ thép bị mòn → thu hồi nhiệt tốt hơn\n• Sửa chữa/thay tấm ghi (grate plate) cooler — tấm ghi mòn không phân phối đều khí làm mát → clinker ra quá nóng (nhiệt bị mang đi thay vì thu hồi)\n• Ổn định thành phần phối liệu — kiểm soát tỷ lệ đá vôi/đất sét/quặng sắt chính xác → lò đốt ổn định, ít tốn nhiên liệu\n→ Tiết kiệm khoảng 5 tỷ VND/năm tiền nhiên liệu."
        },
        {
            "title": "Dây chuyền SMT — Sản xuất bảng mạch điện tử",
            "industry": "Điện tử",
            "situation": "Dây chuyền gắn linh kiện bề mặt SMT (Surface Mount Technology) sản xuất bảng mạch PCB. Tỷ lệ sử dụng dây chuyền (Line utilization) chỉ 60% — cần tìm ra 40% thời gian mất đi đâu.",
            "analysis": "Phân rã 40% tổn thất:\n• Chuyển đổi sản phẩm 25% — lớn nhất! Do sản xuất nhiều model khác nhau, mỗi lần chuyển phải thay stencil (khuôn in kem hàn), nạp lại băng linh kiện (feeder), đổi chương trình máy\n• Dừng ngắn 12% — feeder bị kẹt linh kiện, vòi hút (nozzle) bị bám bẩn không hút được linh kiện\n• Hỏng máy 5% — lỗi servo, lỗi camera nhận dạng\n• Tổn thất con người: Chờ nguyên liệu (linh kiện) chưa kịp chuẩn bị 8% + Kiểm tra thiết lập (setup verify) 5%\n• Chất lượng: Lỗi hàn (solder defect) 0.5%, lỗi gắn sai vị trí 0.3%",
            "result": "Chuyển đổi sản phẩm chiếm lớn nhất (25%):\n• Giải pháp chính: Hệ thống xe chứa feeder (trolley exchange) — chuẩn bị sẵn xe chứa feeder cho sản phẩm tiếp theo TRONG KHI máy đang chạy sản phẩm hiện tại. Khi chuyển, chỉ cần đẩy xe cũ ra, xe mới vào → giảm từ 30 phút xuống 5 phút\n• Dừng ngắn (12%): Bảo trì feeder định kỳ (vệ sinh rãnh dẫn linh kiện) + chương trình vệ sinh nozzle hàng ca\n→ Tiềm năng tăng 20% tỷ lệ sử dụng dây chuyền."
        },
        {
            "title": "Dây chuyền đóng lon bia",
            "industry": "Đồ uống",
            "situation": "Dây chuyền đóng lon bia: OEE chỉ đạt 52%. Sản lượng thực tế thấp hơn 30% so với công suất thiết kế. Ban giám đốc muốn biết 48% tổn thất nằm ở đâu.",
            "analysis": "Phân rã theo 16 loại loss:\n• 8 tổn thất thiết bị: Rửa vệ sinh CIP 8% + Chuyển đổi (đổi loại bia) 6% + Lon kẹt trên băng chuyền (dừng ngắn) 10% + Máy ghép mí (seamer) chạy chậm 8% + Hỏng máy 5% + Khởi động 3% + Phế phẩm (lon bị bọt, mức sai) 2% + Dừng kế hoạch 4%\n• Tổn thất con người: Nhân viên vận hành chưa thành thạo xử lý sự cố 3%\n• Tổn thất vật tư: Lon cung cấp bị méo phải loại 1%\n→ Top 3: Lon kẹt 10% + Seamer chạy chậm 8% + CIP rửa vệ sinh 8% = 26% tổng loss",
            "result": "Cải tiến theo top 3 loss:\n• Lon kẹt 10%: Chỉnh thanh dẫn (guide rail) đúng kích thước lon + đào tạo nhân viên cách xử lý kẹt nhanh (quan trọng: xử lý nhanh để tránh hàng loạt lon đằng sau đổ dây chuyền)\n• Seamer chạy chậm 8%: Tháo lắp và đại tu bộ phận ghép mí (seamer rebuild) — thay rollers, chỉnh khoảng cách ép mí → máy chạy ổn định ở tốc độ cao\n• CIP 8%: Tối ưu quy trình rửa — dùng hóa chất mạnh hơn ở nhiệt độ cao hơn để rút ngắn thời gian rửa (nhưng vẫn đạt tiêu chuẩn vệ sinh)\n→ Mục tiêu OEE tăng từ 52% lên 68%."
        },
        {
            "title": "Dây chuyền lắp ráp xe máy",
            "industry": "Ô tô/Xe máy",
            "situation": "Dây chuyền lắp ráp xe máy sản xuất 800 xe/ngày (2 ca). Mục tiêu 1,000 xe. Cần phân tích xem 200 xe thiếu hụt do nguyên nhân gì.",
            "analysis": "Phân rã tổn thất (quy ra % thời gian mất):\n• Thiết bị: Băng chuyền dừng 2% + Dụng cụ hỏng (súng bắn vít, cờ lê lực) 1.5%\n• Con người (chiếm lớn nhất!): Mất cân bằng chuyền 8% (trạm A xong trong 45 giây, trạm B mất 70 giây → trạm A phải chờ) + Tay nghề chênh lệch 4% (công nhân mới chậm hơn) + Lãng phí thao tác 5% (đi lại lấy linh kiện xa, xoay người, tìm dụng cụ)\n• Vật tư: Thiếu linh kiện (nhà cung cấp giao trễ) 3% + Linh kiện lỗi phải tháo ra lắp lại 2%\n→ Tổn thất con người chiếm tới 17% — lớn nhất! Đây khác biệt lớn so với nhà máy process (thiết bị thường lớn nhất).",
            "result": "Tập trung vào tổn thất con người (17%):\n• Mất cân bằng chuyền 8%: Dùng biểu đồ Yamazumi (biểu đồ cột xếp chồng thao tác từng trạm) để nhìn rõ chênh lệch. Phân bổ lại công việc giữa các trạm cho đều nhịp\n• Tay nghề 4%: Xây dựng Skill Matrix (ma trận kỹ năng) — biết ai cần đào tạo gì, đào tạo chéo (cross-training) để linh hoạt bố trí\n• Lãng phí thao tác 5%: Bố trí linh kiện trong tầm tay (bàn xoay, xe đẩy theo trạm), dụng cụ treo balancer ngay trên đầu\n• Thiếu linh kiện 3%: Hệ thống kanban — linh kiện tự động được bổ sung khi hộp gần hết\n→ Mục tiêu 950 xe/ngày."
        },
        {
            "title": "Máy xeo giấy (Paper Machine)",
            "industry": "Giấy",
            "situation": "Máy xeo giấy #2: tốc độ thiết kế 800 m/phút nhưng thực tế chỉ chạy 620 m/phút (78%). Nhiều loại loss chồng chéo, khó xác định đâu là vấn đề chính.",
            "analysis": "Phân rã loss:\n• Thiết bị: Giấy đứt (web break) 180 giờ/năm — mỗi lần đứt mất 20-30 phút luồn lại + giấy bỏ. Thay chăn lọc (felt) 120 giờ. Sự cố sấy (dryer) 80 giờ. Giảm tốc độ 15% (phần ướt wet end không ổn định, tăng tốc là đứt)\n• Con người: Chuyển đổi loại giấy (grade change) chậm 60 giờ — nhân viên chỉnh nhiều thông số thủ công\n• Vật tư: Hao hụt sợi (fiber loss) 4% — sợi trôi theo nước thải thay vì bám vào tấm giấy. Hóa chất (chất keo, chất bảo lưu) dùng quá liều 2%\n• Năng lượng: Hơi sấy tiêu thụ cao hơn chuẩn 20% — do phần ép (press section) không ép đủ ẩm nên phần sấy phải làm việc nhiều hơn",
            "result": "Giảm tốc độ (15%) + Giấy đứt (180 giờ) là 2 loss lớn nhất:\n• Chương trình quản lý chăn lọc (felt management): Thay chăn đúng tuổi thọ, vệ sinh đúng quy trình → giấy ít đứt hơn\n• Tối ưu bộ phận phân phối bột (headbox): Đảm bảo bột được phân bổ đều trên chiều ngang → giảm điểm yếu gây đứt\n• Chỉnh liều lượng chất bảo lưu (retention aid): Giúp sợi bám lên lưới tốt hơn, giảm sợi mất theo nước thải, tấm giấy chắc chắn hơn → có thể tăng tốc\n• Năng lượng: Lắp thanh sấy khí (dryer bar) + cải thiện thông gió buồng sấy → sấy hiệu quả hơn, giảm hơi\n→ Mục tiêu tốc độ 720 m/phút."
        },
        {
            "title": "Nhà máy sản xuất pin lithium",
            "industry": "Pin/Ắc quy",
            "situation": "Dây chuyền sản xuất pin lithium-ion: tỷ lệ thành phẩm (yield) chỉ đạt 91%, mục tiêu 97%. Mất 6% = hàng tỷ đồng giá trị sản phẩm lỗi.",
            "analysis": "Phân rã 9% tổn thất yield (6% cần cải tiến):\n• Thiết bị: Lỗi phủ điện cực (coating defect — lớp hoạt chất phủ không đều) 2.5% + Lỗi cán ép (calendering — khoảng cách trục ép không chính xác) 1% + Lỗi bơm dung dịch điện giải (electrolyte filling — bơm sai lượng) 0.8%\n• Con người: Hư hỏng do thao tác (cầm nắm sai, để rơi cell) 0.5% + Bỏ sót lỗi khi kiểm tra 0.3%\n• Vật tư: Huyền phù (slurry — hỗn hợp bột hoạt chất) không đồng nhất giữa các mẻ trộn 1.2% + Lỗi màng ngăn (separator) từ nhà cung cấp 0.5% + Lỗi hàn tab điện cực (tab welding) 1.2%\n• Môi trường: Phòng khô (dry room) ẩm dao động → pin bị ẩm loại bỏ 1%",
            "result": "Top losses:\n• Coating defect 2.5%: Lắp hệ thống kiểm tra lớp phủ inline (camera + cảm biến chiều dày) → phát hiện ngay khi phủ, dừng sớm tránh tiếp tục phủ lên cuộn lỗi\n• Slurry không đồng nhất 1.2%: Kiểm soát độ nhớt (viscosity) slurry chặt chẽ — đo trước khi bơm vào máy phủ, nếu ngoài spec phải chỉnh lại\n• Tab welding 1.2%: Khóa chặt thông số hàn laser (công suất, tốc độ, focal point) trên máy — không cho thay đổi tùy ý\n→ Mục tiêu yield tăng từ 91% lên 95%. Mỗi 1% yield tăng ≈ tiết kiệm hàng trăm triệu đồng/tháng."
        },
        {
            "title": "Nhà máy dược phẩm - Dây chuyền viên nén",
            "industry": "Dược phẩm",
            "situation": "Dây chuyền sản xuất viên nén (tablet line): OEE chỉ 45% — cực kỳ thấp! Lý do là trong ngành dược, rất nhiều thời gian dành cho vệ sinh, kiểm tra, hồ sơ — theo yêu cầu của GMP (Thực hành sản xuất tốt).",
            "analysis": "Phân rã 55% tổn thất:\n• Thiết bị: Chuyển đổi sản phẩm + Vệ sinh xác nhận (cleaning validation) chiếm tới 25%! — mỗi lần đổi thuốc phải rửa sạch + chứng minh không còn dư thuốc cũ. Chỉnh máy dập viên 8%. Lỗi bao phim (coating defect) 3%\n• Con người: Chờ QC kiểm nghiệm (lab phải test xong mới được sản xuất tiếp) 10%! Ghi chép hồ sơ sản xuất (documentation) 5%\n• Vật tư: Bột trộn không đồng nhất (blend uniformity — thành phần hoạt chất không đều trong bột) gây reject 2%. Độ cứng viên dao động (hardness variation) 2%\n• Kế hoạch: Các mẻ validation (sản xuất kiểm tra xác nhận) 5%",
            "result": "Chuyển đổi + Vệ sinh chiếm tới 25% — đây là loss đặc trưng ngành dược:\n• Giải pháp chính: Chuyên biệt hóa thiết bị theo nhóm sản phẩm (dedicated equipment) — máy A chỉ sản xuất nhóm thuốc X, máy B nhóm Y → giảm số lần vệ sinh xác nhận\n• Chờ QC 10%: Áp dụng PAT (Process Analytical Technology — công nghệ phân tích trong quá trình) kiểm tra inline ngay trên máy, không cần gửi mẫu ra lab chờ\n• Hồ sơ 5%: Chuyển sang hồ sơ điện tử (Electronic Batch Record) — nhập trên tablet tại chỗ, ký điện tử, không cần viết tay rồi photocopy\n→ Mục tiêu OEE tăng từ 45% lên 62%."
        },
        {
            "title": "Nhà máy chế biến cà phê",
            "industry": "Thực phẩm",
            "situation": "Dây chuyền rang – xay – đóng gói cà phê: tỷ lệ sử dụng (utilization) chỉ 58%. Nhiều thời gian lãng phí giữa các công đoạn do chờ đợi.",
            "analysis": "Phân rã 42% tổn thất:\n• Thiết bị: Máy rang (roaster) cần thời gian nguội giữa các mẻ 8% + Chuyển đổi cỡ xay trên máy xay (grinder changeover) 6% + Máy đóng gói bị kẹt film 5%\n• Con người: Chờ bộ phận QC nếm thử (cupping test — đánh giá mùi vị cà phê bằng cách pha thử) 7%! + Nhân viên chọn hạt (loại bỏ hạt lỗi bằng tay) 4%\n• Vật tư: Độ ẩm hạt xanh (green bean moisture) dao động → mẻ rang không đều 3% + Film đóng gói bị lãng phí khi chạy thử/chỉnh máy 2%\n• Năng lượng: Máy rang tiêu thụ gas cao hơn chuẩn 15% (do cháy không hoàn toàn)",
            "result": "Cải tiến:\n• Thời gian nguội 8%: Mở rộng khay làm mát (cooling tray) → cà phê nguội nhanh hơn, machine cycle ngắn hơn\n• Chờ cupping test 7%: Lắp máy đo màu inline (near-infrared color sensor) ngay sau máy rang — màu cà phê tương quan chặt với mức độ rang → thay thế phần lớn cupping test thủ công (vẫn giữ cupping ngẫu nhiên kiểm tra)\n• Chuyển đổi máy xay 6%: Quản lý recipe — lưu sẵn thông số cho từng loại cà phê (espresso, filter, drip) trên PLC, chuyển đổi chỉ cần chọn trên màn hình\n→ Mục tiêu utilization tăng từ 58% lên 72%."
        },
        {
            "title": "Nhà máy bao bì mềm - In ống đồng",
            "industry": "Bao bì",
            "situation": "Dây chuyền in ống đồng (gravure printing — in ấn chất lượng cao cho bao bì snack, mì gói): tỷ lệ sử dụng chỉ 50%! Một nửa thời gian máy không in. Lãng phí film và mực rất cao.",
            "analysis": "Phân rã 50% loss:\n• Thiết bị: Thay trục in (cylinder change — mỗi màu 1 trục, 8 màu = 8 trục) chiếm 15%! + Thay dao gạt mực (doctor blade) 5% + Lỗi sấy 3%\n• Tốc độ: Chỉnh chồng màu (registration — các màu phải trùng khớp chính xác) 8% — mỗi khi chạy bài mới mất 20-30 phút chỉnh. Độ nhớt mực dao động (ink viscosity variation) 4% — phải giảm tốc\n• Con người: Pha mực (ink mixing — trộn mực theo tỷ lệ màu) 3% + Chuẩn bị trục in 2%\n• Vật tư: Mực thừa/phế 5% + Film lãng phí tại mối nối cuộn (splice) 3% + Dung môi bay hơi (solvent loss)",
            "result": "Thay trục in 15% + Chỉnh chồng màu 8% = 23% loss — chiếm gần nửa tổng tổn thất:\n• Thay trục: Hệ thống shaft-less (không trục truyền — mỗi trục in có motor riêng) giúp tháo lắp nhanh hơn. Chuẩn bị sẵn trục + mực trên xe đẩy\n• Chồng màu: Hệ thống chỉnh chồng màu tự động (auto register) bằng camera + ESA (Electrostatic Assist - hỗ trợ tĩnh điện gúp mực bám tốt) → máy tự chỉnh, không cần chỉnh tay\n→ Mục tiêu utilization tăng từ 50% lên 68%."
        },
        {
            "title": "Trạm trộn bê tông",
            "industry": "Xây dựng",
            "situation": "Trạm trộn bê tông công suất 120 m³/giờ nhưng thực tế chỉ đạt 70 m³/giờ (58%). Xe bồn chờ lâu, công trình phàn nàn giao chậm.",
            "analysis": "Phân rã loss:\n• Thiết bị: Bảo trì máy trộn 3% + Băng tải cốt liệu hỏng 2% + Hiệu chuẩn cân 1%\n• Con người: Operator chưa thành thạo 2% + Truyền thông chậm (gọi điện xác nhận đơn hàng) 3%\n• Vật tư: Độ ẩm cốt liệu (đá, cát) thay đổi → phải chỉnh lại công thức mỗi lần 4%\n• Chờ đợi (lớn nhất!): Xe bồn quay về trạm không kịp, phải chờ xe trống → máy trộn xong nhưng không có xe chứa, chiếm tới 25%! + Chờ nguyên liệu giao đến 5%\n→ Chờ xe bồn 25% là loss chủ đạo!",
            "result": "Cải tiến:\n• Chờ xe bồn 25%: Hệ thống GPS quản lý xe bồn — biết xe nào đang ở đâu, khi nào về, tự động phân lịch trộn theo thời gian xe tới. Tối ưu lịch giao hàng để xe quay vòng nhanh (tránh giờ cao điểm kẹt xe)\n• Độ ẩm cốt liệu 4%: Lắp sensor đo ẩm inline trên băng tải — tự động điều chỉnh lượng nước trong công thức (không cần chỉnh tay)\n• Truyền thông 3%: Hệ thống phiếu xuất bê tông điện tử (digital batch ticket) — đơn hàng tự gửi từ văn phòng xuống trạm, không cần gọi điện\n→ Mục tiêu đạt 95 m³/giờ."
        },
        {
            "title": "Nhà máy chế biến tôm đông IQF",
            "industry": "Thủy sản",
            "situation": "Dây chuyền chế biến tôm đông nhanh IQF (Individual Quick Freezing): tỷ lệ thành phẩm (yield) chỉ 62% — nghĩa là từ 100 kg tôm nguyên liệu chỉ ra 62 kg thành phẩm. 38 kg hao hụt ở đâu?",
            "analysis": "Phân rã 38% hao hụt:\n• Thiết bị: Máy cấp đông IQF phải rã đông (defrost) định kỳ → dừng 5%. Máy mạ băng (glazing) phun nước không đều 2%\n• Con người (rất lớn!): Tay nghề lột vỏ tôm (peeling) chênh lệch — công nhân giỏi chỉ bỏ 30% vỏ, công nhân yếu bỏ tới 38% (cắt quá sâu vào thịt) → chênh 8% yield giữa người\n• Vật tư: Chất lượng tôm nguyên liệu dao động → size không đều, tỷ lệ hư hỏng cao = mất 10%! + Kích cỡ không đồng nhất gây khó phân loại 5%\n• Quy trình: Cắt tỉa (trimming) quá mức — cắt bỏ quá nhiều thịt 5% + Mất nước trong quá trình chế biến (dehydration) 3%",
            "result": "Chất lượng NL (10%) + Cắt tỉa quá mức (5%) + Tay nghề (8%) = 23% loss chính:\n• NL 10%: Chương trình phân loại nhà cung cấp (supplier grading) — chấm điểm NCC theo chất lượng, thưởng/phạt. Kiểm tra đầu vào chặt chẽ hơn\n• Cắt tỉa 5%: SOP cắt tỉa với hình ảnh + cân trọng lượng trước/sau để kiểm soát (nếu bỏ quá nhiều thịt sẽ thấy ngay trên cân)\n• Tay nghề 8%: Chế độ thưởng theo yield cá nhân — ai lột ra yield cao hơn thì thưởng thêm\n• IQF: Lập lịch rã đông tự động theo lượng tuyết bám (không rã đông theo thời gian cố định)\n→ Mục tiêu yield tăng từ 62% lên 68%."
        },
        {
            "title": "Nhà máy đúc áp lực nhôm — Linh kiện ô tô",
            "industry": "Ô tô",
            "situation": "Đúc áp lực nhôm (die casting) sản xuất vỏ hộp số: OEE chỉ 58%. Tỷ lệ phế phẩm 8% (mục tiêu dưới 3%).",
            "analysis": "Phân rã loss chi tiết:\n• Thiết bị: Thời gian phun chất ly khuôn (die spray) quá dài 10% — phun nhiều hơn cần thiết vì sợ kẹt khuôn. Máy cắt ba-via (trim press) kẹt 3%. Nhiệt độ lò nấu nhôm dao động 2%\n• Tốc độ: Chu kỳ (cycle time) chậm hơn 15% so với thiết kế — đặt thời gian làm nguội quá dài vì sợ sản phẩm co rút\n• Con người: Robot lấy sản phẩm (take-out robot) phải chỉnh dạy lại 2%\n• Chất lượng 8%: Rỗ khí (porosity — bọt khí bên trong sản phẩm) 4% + Co ngót (shrinkage — bề mặt bị lõm) 2% + Ba-via (flash — nhôm tràn ra mép khuôn) 2%\n• Khuôn: Khuôn bị nứt do mỏi nhiệt (thermal fatigue crack) → mất 50 giờ sửa/tháng",
            "result": "Chất lượng (8%) + Phun ly khuôn (10%) + Tốc độ (15%) — cần cải tiến đồng thời:\n• Phun ly khuôn 10%: Tối ưu pattern phun — dùng camera nhiệt kiểm tra nhiệt độ khuôn, chỉ phun nơi nào cần, giảm thời gian phun 50%\n• Rỗ khí 4%: Cải thiện khử khí nhôm lỏng (degassing — loại bọt khí khỏi nhôm trước khi đúc) bằng argon. Đúc chân không (vacuum die casting) cho sản phẩm critical\n• Tốc độ 15%: Thiết kế kênh làm mát bên trong khuôn theo hình dạng sản phẩm (conformal cooling channels) — nguội đều và nhanh hơn → giảm thời gian cooling mà không bị co ngót\n→ Mục tiêu OEE 72%, phế phẩm dưới 4%."
        }
    ]
}
