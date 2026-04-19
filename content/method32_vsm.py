method = {
    "id": 32,
    "title": "VSM - Value Stream Mapping (Bản đồ dòng giá trị)",
    "short_name": "VSM",
    "icon": "🗺️",
    "pillar": "Focus Improvement",
    "description": "Vẽ bản đồ toàn bộ dòng chảy vật liệu và thông tin từ nguyên liệu đến khách hàng — phát hiện thời gian chờ đợi, tồn kho, lãng phí ẩn giấu.",
    "meaning": """
<p><strong>VSM (Value Stream Mapping — Bản đồ dòng giá trị)</strong> là công cụ của Lean Manufacturing, vẽ bản đồ TOÀN BỘ dòng chảy: từ nhà cung cấp → qua các công đoạn sản xuất → đến tay khách hàng.</p>
<p><em>Nói đơn giản: VSM giống như Google Maps cho nhà máy — nó chỉ ra "chuyến hành trình" của sản phẩm từ đầu đến cuối, bao gồm cả thời gian di chuyển, thời gian chờ, và thời gian thực sự làm ra giá trị. Và bạn sẽ BẤT NGỜ vì phần lớn thời gian sản phẩm chỉ... NẰM CHỜ!</em></p>
<div class="note-box note-box--info">
    <div class="note-title">📌 Các khái niệm then chốt</div>
    <p><strong>Lead Time (Thời gian dẫn)</strong>: TỔNG thời gian từ đặt hàng đến khi giao hàng cho khách — bao gồm CẢ thời gian chờ<br>
    <strong>Cycle Time (Thời gian chu kỳ)</strong>: Thời gian hoàn thành 1 đơn vị sản phẩm tại 1 công đoạn<br>
    <strong>Value-Added Time (Thời gian tạo giá trị)</strong>: Thời gian máy/người THỰC SỰ gia công, biến đổi sản phẩm — <em>thường CHỈ chiếm 1-5% Lead Time!</em> Phần còn lại là CHỜ ĐỢI!<br>
    <strong>Takt Time (Nhịp sản xuất)</strong>: Thời gian khả dụng ÷ Nhu cầu khách hàng — ví dụ: 480 phút/ngày ÷ 960 sản phẩm = 30 giây/sản phẩm → nhà máy phải ra 1 SP mỗi 30 giây<br><br>
    <strong>Quy tắc sốc: Trong hầu hết nhà máy, thời gian tạo giá trị chỉ chiếm 1-5% tổng lead time. 95-99% còn lại là chờ đợi, lưu kho, vận chuyển!</strong></p>
</div>
""",
    "purpose": """
<ul>
    <li>Nhìn TOÀN CẢNH dòng giá trị từ đầu đến cuối (end-to-end) — không chỉ nhìn 1 công đoạn</li>
    <li>Phân biệt hoạt động TẠO GIÁ TRỊ (gia công, biến đổi) vs KHÔNG tạo giá trị (chờ đợi, tồn kho, vận chuyển)</li>
    <li>Phát hiện 7 loại lãng phí (waste/muda): Chờ đợi, tồn kho, vận chuyển, sản xuất thừa, gia công thừa, di chuyển, phế phẩm</li>
    <li>Thiết kế Future State Map (bản đồ trạng thái tương lai) — nhà máy sau cải tiến sẽ trông như thế nào</li>
    <li>Giảm lead time (thời gian đáp ứng khách hàng) — yếu tố cạnh tranh then chốt</li>
    <li>Là NỀN TẢNG cho mọi chương trình Lean — bước đầu tiên trước khi cải tiến</li>
</ul>
""",
    "how_to": """
<div class="step-card">
    <div class="step-card__num">1</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 1: Chọn sản phẩm/dòng sản phẩm và phạm vi</div>
        <div class="step-card__desc">Chọn sản phẩm hoặc nhóm sản phẩm (product family) chiếm tỷ trọng lớn nhất — ảnh hưởng nhiều nhất đến doanh số. Xác định phạm vi: Từ đâu đến đâu? (Từ nhận NL → đến xuất hàng? Hay từ đơn hàng → đến thu tiền?)</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">2</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 2: Vẽ Current State Map (Bản đồ hiện tại)</div>
        <div class="step-card__desc">ĐI THỰC TẾ (gemba walk) — không vẽ từ văn phòng! Vẽ dòng vận liệu (material flow): Từng công đoạn + lượng tồn kho giữa các công đoạn (tam giác WIP). Vẽ dòng thông tin (information flow): Đơn hàng đi đến đâu? Lệnh sản xuất phát ra sao? Ghi data box tại mỗi công đoạn: Thời gian chu kỳ (C/T), thời gian chuyển đổi (C/O), tỷ lệ chạy máy (Uptime), kích thước lô (Batch). Vẽ timeline ở cuối: Thời gian tạo giá trị vs Thời gian chờ.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">3</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 3: Phân tích và thiết kế Future State (Trạng thái tương lai)</div>
        <div class="step-card__desc">Tính Takt Time (nhịp sản xuất khách hàng yêu cầu). Xác định: Ở đâu có thể tạo dòng chảy liên tục (continuous flow) — không ngắt quãng? Ở đâu cần supermarket (kho đệm nhỏ, cung cấp theo kéo — pull system)? Loại bỏ tồn kho WIP thừa, giảm lead time. Mục tiêu: VA time chiếm tỷ lệ lớn hơn trong tổng lead time.</div>
    </div>
</div>
<div class="step-card">
    <div class="step-card__num">4</div>
    <div class="step-card__content">
        <div class="step-card__title">Bước 4: Lập kế hoạch triển khai và thực hiện PDCA</div>
        <div class="step-card__desc">Chia Future State thành các vòng lặp cải tiến (value stream loops) — mỗi vòng là 1 dự án có thể thực hiện trong 2-4 tuần. Ưu tiên theo mức ảnh hưởng (impact) và tính khả thi. Lập timeline + phân công trách nhiệm. Thực hiện từng vòng theo PDCA (Plan-Do-Check-Act). Đo kết quả: Lead time thay đổi bao nhiêu?</div>
    </div>
</div>
""",
    "examples": [
        {
            "title": "VSM nhà máy TACN — 97% thời gian là CHỜ ĐỢI!",
            "industry": "Thức ăn chăn nuôi",
            "situation": "Lead time từ nhận đơn hàng đến giao hàng cho khách: 5 ngày. Khách hàng muốn nhận trong 2 ngày. Đối thủ cạnh tranh đã giao được 3 ngày. Câu hỏi: Làm sao giảm lead time từ 5 ngày xuống 2 ngày?",
            "analysis": "Vẽ Current State Map và ĐO thời gian thực tế:\n• Nhận đơn hàng + xử lý hành chính: 1 ngày (nhập đơn vào SAP, kiểm tra tồn kho, xác nhận...)\n• Lập kế hoạch sản xuất: 0.5 ngày (lên lịch batch, phân máy)\n• Nguyên liệu CHỜ lên line: 1 ngày (NL đã có trong kho nhưng chờ xe nâng, chờ bin trống)\n• Sản xuất thực tế: chỉ 4 GIỜ! (batching 1h + grinding 0.5h + mixing 0.5h + pelleting 1h + cooling + bagging 1h)\n• QC kiểm tra: 0.5 ngày (chờ lab lấy mẫu, chờ kết quả)\n• Đóng bao + xếp kho: 0.5 ngày\n• Giao hàng: 1 ngày (chờ xe, xếp hàng, vận chuyển)\n\n→ Value-Added Time (thời gian tạo giá trị) = 4 giờ\n→ Lead Time = 5 ngày = 120 giờ\n→ VA Ratio = 4/120 = 3.3%! → 97% thời gian sản phẩm chỉ... NẰM CHỜ!",
            "result": "Future State Map — thiết kế lại:\n• Make-to-stock cho top 20 SKU (chiếm 80% sản lượng): Sản xuất trước, lưu kho thành phẩm → khi có đơn hàng → giao ngay trong 1 ngày!\n• Make-to-order cho sản phẩm đặc biệt (20% còn lại) → rút ngắn còn 3 ngày bằng cách loại bỏ thời gian chờ\n• QC inline: Kiểm tra mẫu NGAY trên dây chuyền thay vì gửi lab chờ → giảm 0.5 ngày\n• E-order: Đơn hàng vào hệ thống tự động → lệnh sản xuất phát ra ngay → giảm 1 ngày hành chính\n→ Lead time giảm 60%: MTS 1 ngày, MTO 3 ngày."
        },
        {
            "title": "Phê duyệt đơn mua hàng — 12 ngày chờ chữ ký!",
            "industry": "Đa ngành",
            "situation": "Quy trình phê duyệt đơn mua hàng (Purchase Requisition → Purchase Order): Trung bình 12 ngày! Sản xuất chờ phụ tùng, nguyên liệu mà mua không kịp.",
            "analysis": "VSM quy trình hành chính (administrative VSM):\n• Tạo PR (Purchase Requisition): 0.5 giờ ✓\n• Chờ quản lý ký: 3 ngày! (PR nằm trên bàn, quản lý họp liên miên)\n• Phòng mua hàng review: 1 ngày (kiểm tra nhà cung cấp, so giá)\n• Chờ Giám đốc ký PO: 5 NGÀY! — Giám đốc đi công tác, hồ sơ nằm trên bàn\n• PO phát hành + gửi nhà cung cấp: 0.5 ngày\n\n→ Value-Added Time: 3 giờ (viết PR + review + soạn PO)\n→ Lead Time: 12 ngày = 288 giờ\n→ VA Ratio = 3/288 = 1%! → 99% thời gian hồ sơ NẰM CHỜ!",
            "result": "Future State:\n• E-approval trên điện thoại: Giám đốc phê duyệt trên app bất kỳ lúc nào, bất kỳ đâu → không cần ký tay trên giấy → chờ 5 ngày → xuống 0.5 ngày\n• Auto-approve cho PO : Quản lý phê duyệt là đủ, không cần GĐ → giảm 5 ngày\n• Delegation matrix: Khi GĐ vắng → Phó GĐ ký thay → không bao giờ hồ sơ bị tắc\n→ Lead time: 12 ngày → 2 ngày!\n→ Bài học: VSM không chỉ cho sản xuất — áp dụng cho MỌI quy trình hành chính!"
        },
        {
            "title": "Chế biến tôm — Cold chain risk khi chờ quá lâu",
            "industry": "Thủy sản",
            "situation": "Từ tiếp nhận tôm nguyên liệu đến thành phẩm đông lạnh: 48 giờ. Tôm là thực phẩm nhạy cảm — chờ lâu → vi khuẩn phát triển → rủi ro an toàn thực phẩm (cold chain risk).",
            "analysis": "Current State Map:\n• Tiếp nhận tôm (cân, phân loại): 2 giờ ✓\n• Chờ đến lượt sơ chế: 8 GIỜ! — Tôm nằm trong thùng xốp chờ vì line sơ chế đang chạy mẻ trước\n• Sơ chế (đầu, lột vỏ, rể gân): 3 giờ ✓\n• Chờ máy đông IQF (Individual Quick Freezing): 4 giờ! — mẻ trước chưa xong\n• Đông IQF: 1 giờ ✓\n• Glazing (phủ lớp băng bảo vệ): 0.5 giờ ✓\n• Đóng gói: 1 giờ ✓\n• QC (lấy mẫu vi sinh, đợi kết quả): 4 giờ\n• Nhập kho lạnh\n\n→ Tổng thời gian CHỜ: 16/48 giờ = 33%! Tôm nằm ở nhiệt độ không lý tưởng → rủi ro!",
            "result": "Future State:\n• Flow production (sản xuất dòng chảy): Chia thành batch nhỏ liên tục thay vì đợi full batch lớn → tôm vào line ngay sau tiếp nhận, không chờ\n• FIFO lanes (làn đệm theo thứ tự): Tôm đến trước xử lý trước — không để mẻ mới chờ mẻ cũ xong\n• QC release theo ca: Phát hành kết quả QC theo từng ca sản xuất thay vì đợi cuối ngày\n• Bổ sung cooling tunnel giữa các công đoạn → giữ lạnh ngay cả khi chờ\n→ Lead time: 48 giờ → 18 giờ! Giảm rủi ro an toàn thực phẩm."
        },
        {
            "title": "VSM dây chuyền may — WIP buffer ăn mất 8 ngày",
            "industry": "Dệt may",
            "situation": "Lead time đơn hàng áo polo: 25 ngày. Khách hàng (brand quốc tế) yêu cầu 15 ngày. Nếu không giảm → mất đơn hàng.",
            "analysis": "Current State Map:\n• Cắt vải: 2 ngày ✓\n• WIP buffer (bán thành phẩm chờ) giữa cắt-may: 5 NGÀY! — Hàng cắt xong xếp đống chờ vì line may đang chạy đơn khác\n• May ráp: 3 ngày ✓ (tương đối nhanh)\n• WIP buffer giữa may-QC: 3 NGÀY — Hàng may xong chờ QC kiểm\n• QC (kiểm tra ngoại quan): 2 ngày\n• Là ủi: 1 ngày\n• Đóng gói: 1 ngày\n• Chờ xuất hàng: 3 ngày (gom đủ container)\n• Vận chuyển: 5 ngày\n\n→ WIP buffers chiếm 8/25 ngày = 32%! Hàng CẮT XONG rồi nhưng NẰM CHỜ 5 ngày mới được MAY!",
            "result": "Future State:\n• One-piece flow sections (dòng chảy từng chiếc): Cắt xong → chuyển ngay sang may, không đợi batch lớn\n• Kanban pull system: Line may chỉ KÉO hàng từ cắt khi cần → không cắt thừa, không tạo WIP\n• QC inline: Kiểm tra ngay trên chuyền may (mỗi trạm tự kiểm) thay vì gom lại cuối → giảm WIP 3 ngày\n• Ship consolidation hàng ngày thay vì chờ đủ container\n→ Lead time: 25 ngày → 14 ngày! Đạt yêu cầu khách hàng."
        },
        {
            "title": "VSM kho phân phối — Đi bộ chiếm 23% thời gian!",
            "industry": "Logistics",
            "situation": "Order fulfillment (lấy hàng + đóng gói + xuất kho): 4 giờ từ khi nhận đơn đến khi hàng lên xe. Khách yêu cầu 2 giờ.",
            "analysis": "VSM chi tiết thao tác trong kho:\n• Nhận đơn hàng (order receive): 15 phút ✓\n• In phiếu lấy hàng (picking list): 10 phút\n• ĐI BỘ đến khu vực hàng (walking): 20 phút!\n• Lấy hàng (picking): 40 phút ✓ (tạo giá trị)\n• ĐI BỘ đến khu đóng gói (walking): 15 phút!\n• Đóng gói (packing): 20 phút ✓\n• Kiểm tra lại (check): 15 phút\n• Chờ tại khu staging: 30 phút\n• Xếp lên xe (loading): 15 phút\n\n→ Walking time = 35 phút = 23% tổng thời gian → KHÔNG TẠO GIÁ TRỊ!",
            "result": "Future State:\n• Zone picking + conveyor: Chia kho thành vùng, mỗi nhân viên lấy hàng trong vùng của mình → hàng đặt lên băng chuyền tự chạy đến packing → không ai đi bộ xa\n• RF real-time (máy quét cầm tay): Thay vì in phiếu giấy → nhân viên nhận lệnh trên thiết bị RF → tiết kiệm 10 phút in\n• Pack-at-pick: Đóng gói NGAY tại chỗ lấy hàng (không di chuyển đến trạm packing riêng)\n• Cross-dock cho hàng fast-mover (hàng bán chạy): Nhập→ Xuất ngay không vào kệ\n→ 4 giờ → 1.5 giờ!"
        },
        {
            "title": "VSM bảo trì thiết bị — MTTR 4 giờ, 35% là chờ!",
            "industry": "Sản xuất chung",
            "situation": "MTTR (Mean Time To Repair — thời gian trung bình sửa chữa) = 4 giờ. Mỗi giờ dừng máy tốn 50 triệu VND (mất sản lượng). Muốn giảm MTTR xuống 2 giờ.",
            "analysis": "VSM quy trình sửa chữa (maintenance value stream):\n• Phát hiện máy hỏng + báo cáo: 15 phút ✓\n• Gọi bộ phận bảo trì: 10 phút ✓\n• Chờ kỹ thuật viên đến: 30 phút! (KTV đang sửa máy khác hoặc ở xa)\n• Chẩn đoán lỗi: 30 phút ✓\n• Chờ phụ tùng: 45 PHÚT! — KTV chạy xuống kho, tìm phụ tùng, giấy tờ xuất kho...\n• Lấy phụ tùng: 15 phút\n• Sửa chữa thực tế: 45 phút ✓ (tạo giá trị)\n• Test + bàn giao: 15 phút ✓\n\n→ Thời gian chờ: 85/240 phút = 35%!\n→ Sửa thực tế chỉ 45 phút — phần còn lại là CHỜ!",
            "result": "Future State:\n• Phụ tùng tại điểm sử dụng (point-of-use kanban): Phụ tùng phổ biến (bearing, belt, seal...) để NGAY TẠI máy → KTV không chạy xuống kho → giảm 45 phút chờ\n• KTV phân theo khu vực: Mỗi KTV phụ trách 1 khu → đến trong 10 phút thay vì 30 phút\n• Hướng dẫn chẩn đoán trên tablet: Bước chẩn đoán hiển thị trên tablet có hình ảnh → KTV junior cũng chẩn đoán nhanh → 30 phút xuống 15 phút\n• Pre-staging (chuẩn bị sẵn): Sửa chữa lặp lại thường xuyên → bộ phụ tùng đóng gói sẵn (repair kit)\n→ MTTR: 4 giờ → 2 giờ! Tiết kiệm 2 giờ × 50 triệu/giờ = 100 triệu mỗi lần sửa."
        },
        {
            "title": "Chuỗi cung ứng sữa tươi — 72 giờ quá lâu!",
            "industry": "Thực phẩm",
            "situation": "Sữa tươi từ trang trại đến kệ siêu thị: 72 giờ (3 ngày). Hạn sử dụng 7 ngày → chỉ còn 4 ngày trên kệ → khách hàng không muốn mua sản phẩm còn ít ngày!",
            "analysis": "VSM chuỗi cung ứng (supply chain VSM):\n• Vắt sữa: 1 giờ ✓\n• Làm lạnh tại trại (farm cooling): 4 giờ ✓\n• Chờ xe thu gom: 8 GIỜ! — Xe chỉ đến 1 lần/ngày (mỗi 2 ngày 1 lần cho trại xa)\n• Vận chuyển về nhà máy: 6 giờ ✓\n• Tiếp nhận tại nhà máy: 2 giờ ✓\n• Chế biến (thanh trùng, đồng hóa): 4 giờ ✓\n• Đóng hộp/chai: 2 giờ ✓\n• QC lab (vi sinh + hóa lý): 8 GIỜ — Mẫu vi sinh cần ủ 24-48 giờ (rút ngắn bằng rapid test)\n• Kho lạnh nhà máy: 12 giờ (chờ xe phân phối)\n• Vận chuyển đến trung tâm phân phối: 8 giờ\n• Từ DC đến kệ siêu thị: 12 giờ\n→ Tổng: 72 giờ → Chỉ còn 4 ngày trên kệ!",
            "result": "Future State:\n• Thu gom hàng ngày (thay vì 2 ngày/lần): Chờ xe giảm từ 8 giờ xuống 4 giờ\n• QC rapid micro test: Kết quả vi sinh nhanh trong 2 giờ (thay vì 8 giờ) bằng ATP test + PCR\n• Direct-to-DC bypass: Bỏ bước kho lạnh nhà máy → từ đóng gói giao thẳng DC\n• Smart routing: Tối ưu tuyến vận chuyển giảm thời gian giao\n→ Lead time: 72 giờ → 36 giờ! → 5.5 ngày trên kệ (thay vì 4 ngày) → khách hàng hài lòng hơn!"
        },
        {
            "title": "Phần mềm — Feature delivery 6 tuần!",
            "industry": "CNTT",
            "situation": "Thời gian phát triển tính năng (feature) từ yêu cầu → deploy lên production: 6 tuần. Mục tiêu Agile: 2 tuần.",
            "analysis": "VSM quy trình phát triển phần mềm:\n• Viết requirement (yêu cầu): 3 ngày ✓\n• Chờ trong backlog (hàng đợi): 10 NGÀY! — Feature nằm chờ vì dev team đang làm feature khác\n• Thiết kế (design): 2 ngày ✓\n• Chờ developer rảnh: 5 ngày!\n• Coding (lập trình): 5 ngày ✓\n• Chờ code review: 3 ngày! — Senior dev bận, PR nằm chờ\n• Testing (kiểm thử): 3 ngày ✓\n• Chờ deployment window: 5 ngày! — Chỉ deploy vào thứ 3 hàng tuần\n• Deploy: 1 ngày ✓\n\n→ Thời gian chờ: 23/42 ngày = 55%! Hơn nửa thời gian code NẰM CHỜ!",
            "result": "Future State:\n• WIP limit (giới hạn công việc đang làm): Mỗi dev chỉ làm 1-2 feature cùng lúc → xong nhanh hơn, không bị phân tán\n• Continuous deployment (deploy liên tục): Deploy bất kỳ lúc nào thay vì chờ thứ 3 → giảm 5 ngày chờ\n• Pair programming (2 người code cùng): Review ngay khi viết → không chờ code review → giảm 3 ngày\n• Feature toggle: Deploy code nhưng ẩn tính năng → bật khi sẵn sàng\n→ Lead time: 6 tuần → 2.5 tuần!"
        },
        {
            "title": "Order-to-Cash — Thu tiền mất 60 ngày!",
            "industry": "Đa ngành",
            "situation": "Chu kỳ từ nhận đơn hàng đến thu được tiền (Order-to-Cash): 60 ngày. Dòng tiền (cash flow) bị ảnh hưởng nghiêm trọng — phải vay ngân hàng bù.",
            "analysis": "VSM dòng tiền (financial value stream):\n• Nhận đơn hàng: 1 ngày ✓\n• Kiểm tra tín dụng khách (credit check): 3 ngày →thủ công!\n• Sản xuất: 5 ngày ✓\n• Giao hàng: 3 ngày ✓\n• Giao nhận biên bản: 2 ngày ✓\n• Hóa đơn (invoice processing): 5 ngày → in hóa đơn, gửi bưu điện!\n• Hạn thanh toán khách hàng (payment terms): 30 NGÀY! → Nửa cycle là chờ khách trả tiền\n• Nhắc nợ (collection follow-up): 7 ngày\n• Nhận thanh toán: 4 ngày\n→ 60 ngày DSO (Days Sales Outstanding) → tiền bị khách giữ 2 tháng!",
            "result": "Future State:\n• Kiểm tra tín dụng tự động (AI credit check): 3 ngày → 1 giờ\n• Hóa đơn điện tử (e-invoicing): Gửi hóa đơn ngay khi xuất hàng (không chờ đến đầu tháng) → giảm 5 ngày\n• Chiết khấu thanh toán sớm: Giảm 2% nếu khách trả trong 10 ngày (thay vì chờ 30 ngày) — nhiều khách sẽ trả sớm để được giảm giá\n• Hệ thống tự động nhắc nhở thanh toán (auto dunning) → giảm 7 ngày\n→ DSO giảm từ 60 xuống 45 ngày → giải phóng vốn lưu động hàng tỷ đồng."
        },
        {
            "title": "VSM line ép nhựa — OEE thấp vì changeover nhiều",
            "industry": "Nhựa",
            "situation": "Máy ép nhựa: Takt time yêu cầu 30 giây/sản phẩm. Cycle time chỉ 25 giây (đủ nhanh). Nhưng OEE thực tế rất thấp — throughput không đạt. Tại sao?",
            "analysis": "VSM phát hiện vấn đề KHÔNG NẰM Ở CYCLE TIME:\n• Injection + Cooling + Eject: 25 giây ✓ (nhanh hơn takt)\n• Robot lấy sản phẩm: 3 giây ✓\n• Kiểm tra thủ công (manual inspection): 5 giây\n• Đóng gói: 4 giây\n\nNHƯNG:\n• WIP giữa inspection và packing: 500 sản phẩm đệm! → 1 giờ WIP nằm chờ\n• Chuyển đổi khuôn (changeover): 2 GIỜ mỗi lần × 5 lần/ngày = 10 giờ/ngày!\n• Trong 16 giờ sản xuất → 10 giờ chuyển đổi → chỉ 6 giờ chạy!\n→ OEE = 58% → Changeover là thủ phạm chính, KHÔNG phải cycle time!",
            "result": "Future State:\n• SMED (Single Minute Exchange of Die): Giảm changeover từ 2 giờ → 30 phút (chuẩn bị khuôn sẵn, pre-heat khuôn, quick clamp...)\n• Kanban signal: Robot gắp SP → đặt trực tiếp vào khay đóng gói → loại bỏ WIP 500 SP\n• Vision inspection (camera kiểm tra tự động): Kiểm tra bằng camera thay người → nhanh + chính xác hơn\n→ OEE: 58% → 78%! Tăng 20% năng suất chỉ bằng giảm changeover và WIP."
        },
        {
            "title": "VSM phế liệu — Tỷ lệ tái chế chỉ 40%!",
            "industry": "Sản xuất chung",
            "situation": "Chi phí xử lý rác thải nhà máy: 800 triệu VND/năm. Tỷ lệ tái chế (recycling rate) chỉ 40%. 60% ra bãi rác → lãng phí + ô nhiễm.",
            "analysis": "VSM dòng phế liệu (waste stream mapping):\n• Phát sinh tại nhiều điểm → gom vào thùng chung (KHÔNG phân loại!)\n• Thu gom hàng ngày bởi 1 nhân viên\n• Kho tạm (chờ đủ xe): hàng tuần\n• Phân loại THỦ CÔNG: 1 người, 8 giờ/ngày → ĐÂY LÀ BOTTLENECK!\n• Độ chính xác phân loại: chỉ 60% → nhiều phế liệu tái chế được bị lẫn vào rác thường\n• Phế liệu phân loại được → bán cho nhà thu mua\n• Rác còn lại → bãi rác (trả phí xử lý cao)",
            "result": "Future State:\n• Phân loại TẠI NGUỒN (source separation): Đặt thùng phân loại theo MÀU tại MỌI vị trí phát sinh (xanh=giấy, vàng=nhựa, đỏ=kim loại, đen=rác thường) → nhân viên SX phân loại ngay khi bỏ, KHÔNG cần 1 người ngồi phân loại cuối\n• Ép gọn (compact) phế liệu tái chế → giảm diện tích kho + giảm chi phí vận chuyển\n• Đàm phán giá phế liệu tốt hơn bằng waste broker (người thu mua chuyên nghiệp)\n→ Tỷ lệ tái chế: 40% → 75%. Chi phí rác: giảm 50%. Doanh thu bán phế liệu tăng."
        }
    ]
}
