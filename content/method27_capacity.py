method = {
    "id": 27,
    "title": "Capacity Analysis - Phân tích công suất",
    "short_name": "Capacity Analysis",
    "icon": "🏭",
    "pillar": "Planned Maintenance",
    "description": "Phân tích năng lực sản xuất thực tế so với thiết kế, xác định công đoạn yếu nhất (bottleneck) và lập kế hoạch nâng cao công suất.",
    "meaning": """
<p><strong>Capacity Analysis (Phân tích công suất)</strong> là phương pháp đánh giá năng lực sản xuất thực tế của từng công đoạn, thiết bị, dây chuyền và toàn nhà máy — để trả lời câu hỏi: <em>"Nhà máy thực sự sản xuất được bao nhiêu? Và có thể tăng lên bao nhiêu?"</em></p>
<p>Phân biệt 3 loại công suất:</p>
<ul>
    <li><strong>Công suất thiết kế (Design Capacity)</strong>: Năng lực tối đa theo thông số nhà sản xuất thiết bị — ví dụ: máy ép viên 40 tấn/giờ theo catalogue</li>
    <li><strong>Công suất hiệu dụng (Effective Capacity)</strong>: Sau khi trừ các khoảng dừng kế hoạch (bảo trì, vệ sinh, chuyển đổi) — ví dụ: 40T/h × 85% khả dụng = 34 tấn/giờ</li>
    <li><strong>Sản lượng thực tế (Actual Output)</strong>: Số máy thực sự làm ra — ví dụ: chỉ 28 tấn/giờ do die mòn, chạy chậm, dừng ngắn</li>
</ul>
<div class="note-box note-box--info">
    <div class="note-title">📌 Các chỉ số quan trọng</div>
    <p><strong>Tỷ lệ sử dụng (Utilization)</strong> = Sản lượng thực / Công suất thiết kế × 100% — <em>"Dùng được bao nhiêu % so với khả năng tối đa?"</em><br>
    <strong>Hiệu suất (Efficiency)</strong> = Sản lượng thực / Công suất hiệu dụng × 100% — <em>"Khi máy chạy, có đạt kỳ vọng không?"</em><br>
    <strong>Năng suất (Throughput rate)</strong> = Sản lượng / Thời gian — ví dụ: tấn/giờ, sản phẩm/phút<br><br>
    <strong>Bottleneck (Nút cổ chai)</strong>: Công đoạn có công suất THẤP NHẤT → quyết định công suất toàn bộ nhà máy<br>
    <em>Ví dụ: Dây chuyền 5 công đoạn, 4 công đoạn đạt 40T/h nhưng 1 công đoạn chỉ 28T/h → toàn nhà máy chỉ đạt 28T/h!</em></p>
</div>
""",
    "purpose": """
<ul>
    <li>Biết chính xác nhà máy sản xuất được bao nhiêu so với thiết kế — thường kết quả gây bất ngờ!</li>
    <li>Tìm ra bottleneck (nút cổ chai) — công đoạn nào đang kéo lùi toàn bộ nhà máy?</li>
    <li>Lập kế hoạch sản xuất chính xác (MPS — Master Production Schedule): nhận đơn hàng vừa sức, không hứa quá khả năng</li>
    <li>Đánh giá có cần mua máy mới không — hay chỉ cần cải tiến máy hiện tại là đủ (thường tiết kiệm hàng tỷ đồng!)</li>
    <li>Cân bằng tải (load balancing) giữa các máy/line — máy nào rảnh phân thêm việc, máy nào quá tải giảm bớt</li>
    <li>Dự báo (forecasting) khả năng đáp ứng đơn hàng mới — có nhận thêm được không?</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Xác định công suất thiết kế (Design Capacity)</div>
        <div class="step-card__desc">Thu thập thông số từ catalogue/nameplate nhà sản xuất: công suất danh định, tốc độ tối đa, thời gian chu kỳ (cycle time) lý thuyết. Quy đổi sang đơn vị thống nhất (tấn/giờ, sản phẩm/phút...) cho tất cả công đoạn. Lưu ý: catalogue thường là điều kiện lý tưởng, cần thực tế hóa.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Đo lường công suất thực tế (Actual Capacity)</div>
        <div class="step-card__desc">Thu thập dữ liệu sản xuất thực tế ít nhất 1-3 tháng: sản lượng (output), thời gian chạy (run time), thời gian dừng (downtime), phế phẩm (reject). Tính năng suất thực tế (throughput rate) CHO TỪNG CÔNG ĐOẠN — đây là bước quan trọng nhất.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: So sánh, tìm gap và bottleneck</div>
        <div class="step-card__desc">Vẽ biểu đồ cột so sánh công suất thiết kế vs thực tế của TẤT CẢ công đoạn trên cùng 1 biểu đồ. Công đoạn có công suất thực thấp nhất chính là BOTTLENECK — nút cổ chai giới hạn toàn bộ nhà máy. Phân tích nguyên nhân gap: tại sao thực tế thấp hơn thiết kế?</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Lập kế hoạch cải tiến/mở rộng</div>
        <div class="step-card__desc">Ngắn hạn: Tăng OEE (hiệu suất) thiết bị hiện có — chi phí thấp, thực hiện nhanh. Trung hạn: Giải quyết bottleneck bằng cải tiến hoặc bổ sung thiết bị nhỏ. Dài hạn: Đầu tư mở rộng mua máy mới — chỉ khi đã khai thác hết tiềm năng máy cũ. Luôn hỏi: "Có cần mua máy mới, hay cải tiến máy cũ là đủ?"</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "Nhà máy TACN - Phân tích công suất toàn line",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Nhà máy thức ăn chăn nuôi thiết kế 300,000 tấn/năm. Thực tế chỉ sản xuất được 210,000 tấn. Tỷ lệ sử dụng (utilization) = 210/300 = 70%. Câu hỏi: Tại sao mất 30% công suất? Công đoạn nào có vấn đề?",
            "analysis": "Phân tích công suất TỪNG CÔNG ĐOẠN (tất cả quy về tấn/giờ):\n• Nhận nguyên liệu: 50 T/h ✓ (đủ)\n• Nghiền (Hammer Mill): thiết kế 45 T/h, thực tế 42 T/h ✓\n• Trộn (Mixer): thiết kế 40 T/h, thực tế 38 T/h ✓\n• Ép viên (Pellet Mill): thiết kế 40 T/h, thực tế chỉ 28 T/h = 70% → ĐÂY LÀ BOTTLENECK!\n• Đóng bao: thiết kế 35 T/h, thực tế 32 T/h ✓\n\n→ Dù các công đoạn khác có thể chạy nhanh hơn, nhưng MÁY ÉP VIÊN chỉ đạt 28 T/h → toàn bộ nhà máy bị kéo lùi xuống 28 T/h!\n→ Nguyên nhân bottleneck: die mòn giảm tốc + chuyển đổi code thường xuyên + áp suất hơi (steam) không ổn định",
            "result": "Kế hoạch theo giai đoạn:\n• Giai đoạn 1 (chi phí thấp): Tối ưu máy ép viên hiện tại — quản lý tuổi thọ die, cải tiến SMED chuyển đổi nhanh, ổn định hơi → OEE từ 62% lên 78% → tăng thêm 5 T/h lên 33 T/h\n• Giai đoạn 2 (đầu tư): Mua thêm 1 máy ép viên → tổng capacity ép viên tăng lên 55 T/h → bottleneck chuyển sang đóng bao → tiếp tục cải tiến đóng bao\n→ Mục tiêu 280,000 tấn/năm\n→ Bài học: KHÔNG mua máy mới ngay! Giai đoạn 1 cải tiến máy cũ tăng được 5 T/h mà không tốn tiền mua máy."
        },
        {
            "title": "Capacity nghiền nguyên liệu — Cần mua máy không?",
            "industry": "Thức ăn chăn nuôi",
            "situation": "2 máy nghiền búa (Hammer Mill): HM1 thiết kế 30 T/h nhưng thực tế chỉ 22 T/h. HM2 thiết kế 25 T/h nhưng thực tế 20 T/h. Tổng thực tế = 42 T/h, nhưng nhu cầu sản xuất cần 48 T/h. Thiếu 6 T/h! Giám đốc muốn mua máy nghiền mới (~3 tỷ VND).",
            "analysis": "Trước khi mua máy mới, phân tích tại sao 2 máy hiện tại không đạt thiết kế:\n• HM1 gap 8 T/h: Búa nghiền mòn giảm hiệu quả (-4 T/h) + lưới sàng rách (-2 T/h — hạt to lọt qua, phải nghiền lại) + chờ nguyên liệu đổ về bin (-2 T/h)\n• HM2 gap 5 T/h: Motor quá tải phải giảm tốc (-3 T/h — dây quấn motor bị chạm, cần quấn lại) + thời gian chuyển đổi loại NL lâu (-2 T/h)\n→ Tổng gap = 13 T/h. Nhu cầu thiếu = 6 T/h. Chỉ cần phục hồi 6/13 T/h là đủ!",
            "result": "KHÔNG mua máy mới! Cải tiến máy hiện tại:\n• HM1: Thay búa mới + vá lưới sàng → phục hồi từ 22 lên 28 T/h (+6 T/h)\n• HM2: Quấn lại motor + áp dụng SMED chuyển đổi NL nhanh → phục hồi từ 20 lên 24 T/h (+4 T/h)\n→ Tổng = 28 + 24 = 52 T/h > nhu cầu 48 T/h. Thừa 4 T/h dự phòng!\n→ Tiết kiệm 3 tỷ VND không cần mua máy mới! Chi phí cải tiến chỉ ~200 triệu."
        },
        {
            "title": "Đóng bao có đủ cho mùa cao điểm không?",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Line đóng bao: thiết kế 20 bao/phút = 1,200 bao/giờ. Mùa cao điểm (tháng 10-12) nhu cầu tăng lên 1,500 bao/giờ. Liệu có cần đầu tư thêm dây chuyền đóng bao thứ 2?",
            "analysis": "Thực tế hiện tại chỉ đạt 14 bao/phút (70% thiết kế). Phân tích nguyên nhân mất 6 bao/phút:\n• Thay cuộn film (màng bao): mỗi lần mất 2 phút, 6 lần/ca = mất 12 phút/ca\n• Film kẹt: mỗi lần mất 5 phút, trung bình 4 lần/ca = mất 20 phút/ca\n• Chuyển đổi code sản phẩm: mỗi lần 15 phút, 5 lần/ca = mất 75 phút/ca\n• Khi máy chạy OK thì tốc độ cũng chỉ đạt 16 bao/phút (không phải 20) do bộ dao cắt cùn\n→ Tổng mất 107 phút dừng + chạy chậm 20%",
            "result": "Tối ưu trước khi đầu tư:\n• Film: Hệ thống nối film tự động (auto splice) — máy tự nối cuộn mới khi cuộn cũ sắp hết, không cần dừng\n• Kẹt film: Bảo trì thanh hàn (sealer PM) + kiểm tra lực căng film\n• Chuyển đổi: Quick changeover — chuẩn bị sẵn nhãn, cài đặt recipe trước\n• Tốc độ: Mài/thay dao cắt → tốc độ phục hồi 18 bao/phút\n→ Sau cải tiến: 18 bao/phút × 90% khả dụng = 16.2 bao/phút × 60 = 972 bao/giờ\n→ Vẫn chưa đủ cho 1,500 bao/giờ mùa cao điểm → Cần đầu tư thêm dây chuyền 2 cho mùa cao điểm."
        },
        {
            "title": "Nồi hơi có đủ cho mở rộng nhà máy?",
            "industry": "Sản xuất chung",
            "situation": "Nồi hơi (Boiler) hiện tại: công suất 10 tấn hơi/giờ. Đang sử dụng 8 T/h (80%). Kế hoạch mở rộng nhà máy thêm 1 dây chuyền mới cần thêm 3 T/h hơi. Tổng nhu cầu = 11 T/h — vượt công suất boiler!",
            "analysis": "Phân tích chi tiết:\n• Hiện tại: 8 T/h sử dụng + 2 T/h dự phòng\n• Sau mở rộng: 8 + 3 = 11 T/h nhu cầu > 10 T/h công suất → thiếu 1 T/h\n• Câu hỏi: Mua boiler mới (~5 tỷ VND) hay có cách nào khác?\n• Kiểm tra: Nhiều hơi đang bị lãng phí — ống dẫn hơi bị rò rỉ, nước ngưng (condensate) bị đổ bỏ thay vì thu hồi, bẫy hơi (steam trap) hỏng xả hơi sống",
            "result": "Phương án tiết kiệm trước khi mua boiler mới:\n• Lắp bộ tiết kiệm nhiệt (economizer) — tận dụng nhiệt khí thải để gia nhiệt nước cấp → tiết kiệm 0.8 T/h hơi\n• Thu hồi nước ngưng (condensate recovery) — nước ngưng nóng 80°C đưa lại boiler thay vì bỏ, giảm năng lượng cần gia nhiệt → tiết kiệm 0.7 T/h\n→ Boiler hiệu dụng = 10 + 1.5 = 11.5 T/h → ĐỦ cho mở rộng!\n→ Dài hạn (giai đoạn 2 mở rộng tiếp): Đầu tư boiler 5 T/h bổ sung."
        },
        {
            "title": "Phòng lab QC — Tăng lượng mẫu phân tích",
            "industry": "Dược phẩm",
            "situation": "Phòng lab QC có 5 máy HPLC (máy sắc ký lỏng hiệu năng cao — dùng phân tích thành phần thuốc). Mỗi máy chạy 8 mẫu/ngày = 40 mẫu/ngày. Nhu cầu tăng lên 55 mẫu/ngày do thêm sản phẩm mới. Giám đốc: Có cần mua thêm 2 máy HPLC (~2 tỷ VND)?",
            "analysis": "Phân tích tại sao mỗi máy chỉ chạy 8 mẫu/ngày:\n• Thời gian phân tích: 45 phút/mẫu (phương pháp cũ, chạy dung môi chậm -> có thể rút ngắn)\n• Hiệu chuẩn (calibration): 15 phút/ngày/máy — 5 máy hiệu chuẩn cùng lúc buổi sáng → mất 1 giờ đầu ngày!\n• Nhân viên (analyst): Chỉ làm 7/8 giờ hiệu quả (1 giờ nghỉ, chuẩn bị, ghi chép)\n• Thực tế chỉ đạt 35 mẫu/ngày (87.5%)",
            "result": "Tối ưu TRƯỚC KHI mua máy mới:\n• Tối ưu phương pháp (method optimization): Rút ngắn thời gian phân tích từ 45 phút xuống 25 phút bằng cột sắc ký nhanh hơn → tăng 50% throughput!\n• Giãn lịch hiệu chuẩn (stagger calibration): Thay vì 5 máy hiệu chuẩn cùng lúc, chia ra mỗi máy 1 giờ khác nhau → luôn có 4 máy sẵn sàng\n• Chạy đêm (night run): Cho mẫu ổn định (stability) chạy qua đêm không cần người trực\n→ Capacity tăng lên 60 mẫu/ngày > nhu cầu 55. Tiết kiệm 2 tỷ VND không mua HPLC!"
        },
        {
            "title": "Kho lạnh — Đủ chỗ cho mùa tôm?",
            "industry": "Thủy sản",
            "situation": "Kho lạnh dung tích thiết kế 5,000 tấn. Tồn kho trung bình 4,500 tấn (90% đầy). Mùa tôm (tháng 3-5) dự kiến cần 6,500 tấn. Thiếu 1,500 tấn! Thuê kho ngoài rất đắt.",
            "analysis": "Kiểm tra thực tế kho:\n• Dung tích thiết kế 5,000 tấn — nhưng 15% diện tích bị chặn bởi layout cũ (kệ đặt sai vị trí, lối đi quá rộng, hàng xếp không tối ưu) → thực tế chỉ tiếp cận được 4,250 tấn\n• Hệ thống kệ hiện tại: single deep racking (kệ 1 hàng sâu) → lãng phí không gian\n• Gap với nhu cầu 6,500 tấn = 2,250 tấn thiếu",
            "result": "Giải pháp:\n• Giai đoạn 1: Thiết kế lại layout kho — chuyển sang kệ double-deep racking (kệ 2 hàng sâu, dùng xe nâng reach truck) + thu hẹp lối đi (narrow aisle) → dung tích tăng lên 6,200 tấn\n• Giai đoạn 2 (cho peak): Xây thêm 1 kho phụ 2,000 tấn cho mùa cao điểm\n• Cải thiện FIFO: Dán nhãn ngày (date coding) trên mỗi pallet → hàng cũ xuất trước, không bị ùn đọng chiếm chỗ\n→ Giai đoạn 1 tăng tới 6,200 tấn, gần đủ cho mùa tôm."
        },
        {
            "title": "Nhà máy xi măng — Debottleneck hay mua kiln mới?",
            "industry": "Xi măng",
            "situation": "Lò nung (kiln) thiết kế 3,000 tấn clinker/ngày. Thực tế chỉ đạt 2,400 tấn (80%). Nhu cầu thị trường tăng 20%/năm. Giám đốc cân nhắc xây lò nung mới (~500 tỷ VND).",
            "analysis": "Phân tích capacity toàn dây chuyền:\n• Lò nung (Kiln): 2,400 T/ngày (80%) — thiếu do đầu đốt (burner) hiệu suất kém + gạch chịu lửa (refractory) mòn phải giảm tải\n• Nghiền nguyên liệu (Raw Mill): 280 T/h thiết kế, 240 thực tế — bộ phân ly (separator) kém\n• Nghiền xi măng (Finish Mill): 200 T/h thiết kế, 180 thực tế — bộ phân loại (classifier) cần nâng cấp",
            "result": "Kế hoạch debottleneck (giải phóng nút cổ chai) thay vì xây kiln mới:\n• Năm 1: Sửa đầu đốt + thay gạch chịu lửa → kiln phục hồi lên 2,800 T/ngày\n• Năm 2: Nâng cấp separator nghiền NL → Raw Mill đạt 270 T/h, đủ cung cấp cho kiln\n• Năm 3: Thêm nghiền xi măng mới cho dòng sản phẩm mới (xi măng bền sulfat, PCB...)\n→ Hoãn đầu tư kiln mới (500 tỷ!) ít nhất 3 năm chỉ bằng cải tiến debottleneck chi phí ~30 tỷ."
        },
        {
            "title": "Lập kế hoạch ca sản xuất — Nhà máy ô tô",
            "industry": "Ô tô",
            "situation": "Dây chuyền lắp ráp ô tô: năng suất 60 xe/giờ (JPH — Jobs Per Hour). Chạy 2 ca × 8 giờ = 960 xe/ngày. Nhu cầu tăng lên 1,100 xe/ngày. Cần thêm bao nhiêu?",
            "analysis": "Tính toán các phương án:\n• Hiện tại: 960 xe/ngày × 22 ngày làm = 21,120 xe/tháng\n• Nhu cầu: 1,100 xe/ngày × 22 = 24,200 xe/tháng → thiếu 3,080 xe/tháng\n• Phương án A: Thêm ca 3 (đêm) → +960 xe/ngày nhưng chi phí nhân công ca đêm cao + an toàn\n• Phương án B: Tăng tốc độ 60→70 JPH → cần cân bằng lại tất cả trạm, rất phức tạp\n• Phương án C: Tăng ca cuối tuần (overtime thứ 7) → +960/2 = 480 xe/thứ 7 × 4 tuần = 1,920 xe/tháng",
            "result": "Kết hợp phương án tối ưu:\n• Overtime thứ Bảy (4 ngày/tháng): +1,920 xe/tháng → tổng 23,040\n• Tăng JPH nhẹ 60→63 bằng cải thiện cân bằng dây chuyền (line balance) → +3 xe/giờ × 16 giờ × 22 ngày = +1,056\n→ Tổng: 23,040 + 1,056 = 24,096 → gần đủ 24,200\n→ Ca 3 chỉ cần cho giai đoạn 2 khi nhu cầu tăng thêm."
        },
        {
            "title": "Trạm biến áp có đủ cho thiết bị mới?",
            "industry": "Sản xuất chung",
            "situation": "Trạm biến áp nhà máy: 2,000 kVA (kilovolt-ampere — đơn vị đo công suất điện). Tải cao điểm (peak demand) hiện tại 1,750 kVA (87.5%). Lắp thêm 2 máy sản xuất mới cần thêm 400 kVA. Tổng = 2,150 kVA → vượt 150 kVA! Cần nâng trạm biến áp (~1 tỷ VND)?",
            "analysis": "Kiểm tra chi tiết trước khi nâng trạm:\n• Hệ số công suất (power factor) hiện tại = 0.82 — khá thấp! Nghĩa là nhà máy đang sử dụng điện không hiệu quả, phải kéo nhiều dòng điện hơn cần thiết\n• Tất cả motor lớn khởi động cùng lúc vào đầu ca → tạo peak demand nhân tạo, nhưng peak chỉ kéo dài 15 phút\n• Nếu nâng power factor lên 0.95 bằng tụ bù → giải phóng được capacity",
            "result": "Giải pháp không cần nâng trạm:\n• Bù công suất phản kháng (power factor correction): Lắp tủ tụ bù đưa PF từ 0.82 lên 0.95 → giải phóng 250 kVA capacity trên cùng trạm biến áp\n• Quản lý tải (demand management): Cài đặt khởi động tuần tự (stagger startup) — motor khởi động lần lượt thay vì cùng lúc → giảm peak 100 kVA\n→ Capacity khả dụng = 2,000 - 1,750 + 250 + 100 = 600 kVA dư > 400 kVA cần\n→ Tiết kiệm 1 tỷ VND không cần nâng trạm! Chi phí tụ bù + hệ thống điều khiển chỉ ~100 triệu."
        },
        {
            "title": "Hệ thống xử lý nước thải — Mở rộng nhà máy dệt",
            "industry": "Dệt nhuộm",
            "situation": "Hệ thống xử lý nước thải (WWTP) thiết kế 2,000 m³/ngày. Lượng nước thải hiện tại 1,800 m³ (90%). Mở rộng nhà máy dệt nhuộm cần thêm 800 m³/ngày. Tổng = 2,600 m³ → vượt 30%! Xây WWTP mới tốn 20 tỷ VND.",
            "analysis": "Phân tích capacity từng công đoạn WWTP:\n• Bơm hút + Bể điều hòa (equalization): OK — đủ dung tích\n• Bể xử lý sinh học (biological treatment): BOTTLENECK! — Bể sục khí (aeration basin) không đủ dung tích cho tải hữu cơ (BOD — chất ô nhiễm hữu cơ) tăng thêm\n• Bể lắng + Lọc: OK cho hiện tại, nhưng sẽ quá tải nhẹ nếu mở rộng\n• Khi quá tải: chi phí hóa chất tăng 30% vì phải dùng nhiều hóa chất bù cho xử lý sinh học kém",
            "result": "Giải pháp thay vì xây WWTP mới:\n• Lắp MBBR (Moving Bed Biofilm Reactor — giá thể vi sinh di động) vào bể hiện có: Vi sinh vật bám trên các hạt nhựa nhỏ trôi nổi trong bể → diện tích bề mặt xử lý tăng 50% MÀ KHÔNG cần mở rộng bể → chi phí chỉ 3 tỷ (vs 20 tỷ xây mới)\n• Tối ưu liều lượng hóa chất (dosing optimization)\n• Tái sử dụng nước thải đã xử lý cho rửa máy, làm mát (không cần đạt tiêu chuẩn nước uống)\n→ Hoãn đầu tư WWTP mới, tiết kiệm 17 tỷ VND!"
        },
        {
            "title": "Máy nén khí — Rò rỉ ẩn giấu \"ăn\" mất công suất",
            "industry": "Sản xuất chung",
            "situation": "Hệ thống 3 máy nén khí: 2 máy × 100 CFM + 1 máy × 150 CFM = tổng 350 CFM (Cubic Feet per Minute — đơn vị đo lưu lượng khí). Nhu cầu bình thường 280 CFM (80%), peak 340 CFM (97%). Khi 1 máy bảo trì → thiếu khí!",
            "analysis": "Kiểm tra thực tế — phát hiện ĐÁNG BẤT NGỜ:\n• Khảo sát rò rỉ khí nén (air leak audit): Ước tính 20% lượng khí bị rò rỉ = 56 CFM! — qua các mối nối cũ, van hỏng, ống mềm nứt, quick coupler mòn\n• Nhu cầu sử dụng THỰC SỰ: 280 - 56 = chỉ 224 CFM cho sản xuất\n• 56 CFM rò rỉ = máy nén chạy để... phun khí vào không khí! Tốn khoảng 500 triệu VND tiền điện/năm cho rò rỉ!",
            "result": "Hành động:\n• Sửa chữa rò rỉ: Dùng máy dò siêu âm (ultrasonic leak detector) quét toàn bộ nhà máy → tìm và sửa 180 điểm rò rỉ → thu hồi 56 CFM\n• Kết quả: Nhu cầu thực giảm xuống 224 CFM → 2 máy (200 CFM) gần đủ cho bình thường\n• Lắp biến tần VFD trên máy 150 CFM → chạy nhẹ khi peak, tắt khi normal → tiết kiệm điện\n→ Tiết kiệm 500 triệu VND/năm tiền điện + không cần mua thêm máy nén. Không tốn đồng đầu tư nào đáng kể!"
        },
        {
            "title": "Dây chuyền sơn tĩnh điện — Tìm bottleneck",
            "industry": "Kim loại",
            "situation": "Dây chuyền sơn tĩnh điện (powder coating): thiết kế 120 sản phẩm/giờ. Thực tế chỉ đạt 75 SP/giờ (62.5%). Đơn hàng mới cần 100 SP/giờ.",
            "analysis": "Phân tích capacity từng công đoạn:\n• Treo hàng lên conveyor (Loading): 20 SP/giờ → BOTTLENECK RÕ RÀNG! Do thao tác thủ công (manual), nhân viên treo từng sản phẩm lên móc, rất chậm + vấn đề ergonomics (tư thế bất lợi, mệt cuối ca)\n• Phòng phun sơn (spray booth): OK — phun nhanh, không tắc nghẽn\n• Lò sấy (oven): OK — liên tục chạy\n• Tháo hàng (unloading): OK nhưng cũng manual\n→ Loading = nút cổ chai, quyết định toàn bộ = 75 SP/giờ",
            "result": "Giải quyết bottleneck Loading:\n• Giai đoạn 1: Thiết kế lại jig treo hàng (từ 1 SP/jig → 2 SP/jig) — mỗi lần treo 2 sản phẩm thay vì 1 → throughput nhân đôi mà không cần thêm người\n• Giai đoạn 2: Robot tự động treo hàng (auto loading) cho sản phẩm tiêu chuẩn — phù hợp sản phẩm lặp lại nhiều\n→ Mục tiêu 110 SP/giờ, đủ cho đơn hàng 100 SP/giờ."
        },
        {
            "title": "Đội xe vận chuyển — Tối ưu trước khi mua thêm xe",
            "industry": "Logistics",
            "situation": "Đội 20 xe tải 10 tấn. Nhu cầu giao 250 tấn hàng/ngày. Capacity lý thuyết: 20 xe × 2 chuyến × 10 tấn = 400 tấn/ngày. Thực tế chỉ giao được 220 tấn (55%). Thiếu 30 tấn! Giám đốc muốn mua thêm 5 xe (~5 tỷ VND).",
            "analysis": "Phân tích tại sao chỉ đạt 55%:\n• Tải trọng trung bình: Chỉ 8T/chuyến (80% tối đa) — do không tối ưu ghép hàng, nhiều chuyến chở non tải\n• Số chuyến: 1.8 chuyến/ngày (vs thiết kế 2) — tài xế chờ bốc/dỡ hàng quá lâu (1-2 giờ/điểm)\n• Xe khả dụng: Chỉ 16/20 xe hoạt động mỗi ngày — 4 xe luôn OFF do sửa chữa, bảo trì, hoặc tài xế nghỉ",
            "result": "Tối ưu TRƯỚC KHI mua thêm xe:\n• Phần mềm tối ưu tuyến đường (route optimization): Ghép đơn giao gần nhau + tránh giờ cao điểm → tăng từ 1.8 lên 2.2 chuyến/ngày\n• Lịch bốc dỡ hàng: Hẹn giờ chính xác với khách → tài xế không chờ đợi\n• PM phòng ngừa xe: Bảo trì đúng lịch thay vì sửa khi hỏng → 18/20 xe luôn sẵn sàng thay vì 16\n→ Capacity: 18 xe × 2.2 chuyến × 9T = 356 T/ngày > nhu cầu 250T\n→ Tiết kiệm 5 tỷ VND không mua thêm xe!"
        },
        {
            "title": "Server web — Chuẩn bị cho Black Friday",
            "industry": "CNTT",
            "situation": "Hệ thống website thương mại điện tử: server hiện tại chịu được tối đa 10,000 người dùng truy cập đồng thời (concurrent users). Peak bình thường 8,500 (85%). Dự kiến Black Friday: 25,000 người! Gấp 2.5 lần capacity!",
            "analysis": "Stress test (kiểm tra tải) chi tiết:\n• CPU utilization peak: 78% → còn dư\n• Bộ nhớ (Memory): 85% → sắp hết\n• Mạng (Network): 60% → OK\n• Database (cơ sở dữ liệu): 5,000 truy vấn/giây (max 7,000) → BOTTLENECK! Khi >12,000 users → database bị nghẽn, web chậm → khách bỏ đi\n• CDN (mạng phân phối nội dung): Đủ băng thông",
            "result": "Kế hoạch mở rộng:\n• Web tier: Auto-scaling (tự mở rộng trên cloud) — tự thêm server web khi tải tăng, 10K→30K users. Chi phí chỉ trả khi dùng (pay-as-you-go)\n• Database (bottleneck): Thêm bản sao chỉ đọc (read replicas) + bộ nhớ đệm Redis (caching — lưu kết quả truy vấn phổ biến, không cần hỏi database lần nữa)\n• CDN: Pre-warm (tải sẵn hình ảnh sản phẩm lên CDN trước Black Friday)\n→ Load test verify: 28,000 users OK! Quyết định: cloud burst (thuê thêm cloud tạm) cho Black Friday thay đầu tư server vĩnh viễn."
        },
        {
            "title": "Dây chuyền mì ăn liền — 3 line hay mua thêm line 4?",
            "industry": "Thực phẩm",
            "situation": "3 dây chuyền sản xuất mì ăn liền, thiết kế 600 gói/phút mỗi line. Thực tế: Line A ~450, Line B ~420, Line C ~390 gói/phút. Tổng = 1,260 vs nhu cầu 1,400 gói/phút. Ban giám đốc đang ký hợp đồng mua Line 4 (~15 tỷ VND).",
            "analysis": "Phân tích tại sao 3 line đều chạy dưới thiết kế:\n• Bottleneck chung cả 3 line: Bể chiên (fryer) — tốc độ bị giới hạn bởi khả năng phục hồi nhiệt dầu (oil temperature recovery). Khi chạy nhanh → dầu nguội quá → mì chiên không giòn\n• Line A: 75% design (fryer ổn nhất)\n• Line B: 70% design (fryer bắt đầu cũ)\n• Line C: 65% design (fryer degradation nhanh nhất) — bộ trao đổi nhiệt (heat exchanger) bám muội, giảm hiệu suất gia nhiệt",
            "result": "HOÃN mua Line 4!\n• Nâng cấp heat exchanger fryer tất cả 3 line: Thay bộ trao đổi nhiệt mới (chống bám cặn) + cải thiện hệ thống lọc dầu (oil filtration) → dầu sạch hơn, truyền nhiệt tốt hơn\n→ Tất cả 3 line đạt 500 gói/phút\n→ Tổng: 3 × 500 = 1,500 > nhu cầu 1,400\n→ Hoãn đầu tư Line 4 (15 tỷ VND!), chỉ tốn ~1 tỷ nâng cấp fryer\n→ Đặc biệt tập trung bảo trì fryer Line C (xuống cấp nhanh nhất)."
        },
        {
            "title": "Hệ thống khí nén cho tự động hóa — Robot mới",
            "industry": "Sản xuất chung",
            "situation": "Hệ thống khí nén nhà máy: 7 bar, tổng 500 CFM. Kế hoạch lắp thêm 10 robot khí nén (pneumatic robot) mới cần thêm 150 CFM peak. Tổng nhu cầu = 420 + 150 = 570 CFM → vượt capacity 500 CFM! Cần mua thêm máy nén?",
            "analysis": "Khảo sát chi tiết hệ thống khí nén:\n• Áp suất tại máy nén: 7 bar\n• Áp suất tại điểm sử dụng xa nhất: chỉ 5.5 bar! Mất 1.5 bar (21%) trên đường ống!\n• Nguyên nhân: Ống dẫn quá nhỏ + quá nhiều co nối vuông góc (elbow) + mối nối rò rỉ\n• Mất áp 1.5 bar = máy nén phải chạy nặng hơn 25% để bù → lãng phí năng lượng khổng lồ\n• Rò rỉ: 50 CFM (10% lượng khí bị mất qua rò rỉ)",
            "result": "Giải pháp KHÔNG mua máy nén mới:\n• Giảm tổn thất áp suất: Thay ống lớn hơn tại header chính + giảm số co nối (dùng ống cong thay co vuông) → mất áp giảm từ 1.5 bar xuống 0.5 bar. Capacity hiệu dụng tại điểm sử dụng tăng 15%\n• Sửa rò rỉ: Thu hồi 50 CFM\n→ Capacity khả dụng = 500 - 420 + 50 + (15% × 420) = 193 CFM > 150 CFM cần thiết\n→ Tiết kiệm cả chi phí mua máy nén MÀ CÒN giảm điện năng hiện tại!"
        }
    ]
}
