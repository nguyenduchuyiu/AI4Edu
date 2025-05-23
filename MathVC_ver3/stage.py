
PROBLEM = r"""Xét tính đơn điệu của hàm số $f(x) = \frac{x-1}{x+1}$."""

SOLUTION = r"""**Bước 1: Tập Xác Định**

$D = \mathbb{R} \setminus \{-1\}$

**Bước 2: Tính Đạo Hàm**

$f'(x) = \frac{2}{(x+1)^2}$

**Bước 3: Xét Dấu Đạo Hàm**

$f'(x) > 0 \forall x \neq -1$

**Bước 4: Tính Giới Hạn Để Vẽ BBT**

$\lim_{x \to +\infty} f(x) = 1$
$\lim_{x \to -\infty} f(x) = 1$
$\lim_{x \to -1^+} f(x) = -\infty$
$\lim_{x \to -1^-} f(x) = +\infty$

**Bước 5: Bảng Biến Thiên**

| $x$    | $-\infty$ |       $-1$       | $+\infty$ |
| :------- | :-------: | :----------------: | :-------: |
| $f'(x)$ |    $+$    |          $\|$          |    $+$    |
| $f(x)$  |     1 $\nearrow$  $+\infty$     | $\|$  |    $-\infty$ $\nearrow$  1 |

**Bước 6: Kết Luận Tính Đơn Điệu**

Hàm số đồng biến trên khoảng $(-\infty; -1)$ và $(-1; +\infty)$.
"""

STAGES = [
    {
        "stage" : "1",
        "name" : "Tìm hiểu đề bài.",
        "description" : """Tìm hiểu nội dung đề bài, nhìn nhận vấn đề xuất hiện trong bài tập Toán, thu thập các dữ kiện (giả thuyết- kết luận) của bài tập. Lưu ý quan trọng, nếu bài toán đơn giản thì không cần thiết đi QUÁ SÂU vào quá trình này để chuyển sang bước khác.""",
        "tasks" : [
            "Tìm hiểu bài toán cho những gì? Đâu là ẩn? Đâu là dữ liệu? và Bài toán yêu cầu tìm hay chứng minh điều gì? (Chỉ cần nêu và nhận xét chứ không cần đi chi tiết vào)",
            "Khi đã giải quyết được câu các nhiệm vụ trên và nắm được các mục tiêu, đề nghị cả nhóm sang bước mới là \"Lên kế hoạch\"."
        ],
        "goals"  : [
            "Nhận biết đây là dạng bài toán xét tính đơn điệu của hàm số bậc nhất trên bậc nhất"
        ],
        "acts" : []
    },

    {
        "stage" : "2",
        "name" : "Lập kế hoạch giải bài.",
        "description" : "Đưa ra kế hoạch giải bài. Chỉ cần lên kế hoạch tổng quát, chứ không cần thực hiện chi tiết. Giúp hình thành thói quen nhìn bài toán dưới nhiều góc độ, để tìm phương hướng giải cần tập trung vào nhiều đối tượng kiến thức khác nhau, rèn luyện năng lực huy động kiến thức vốn có để triển khai được cách thức giải quyết vấn đề, đánh giá giải pháp đã thực hiện, lựa chọn giải pháp tối ưu, khái quát hóa được cho vấn đề tương tự.",
        "tasks" : [
            "Đề xuất phương pháp giải bài từ quan sát đánh giá bài toán. Nhận xét, phân tích một phương pháp cụ thể xem khả thi không. Tuy nhiên CHƯA cần thực hiện cụ thể, chi tiết.",
            "Khi đã giải quyết được câu các nhiệm vụ trên và nắm được các mục tiêu, đề nghị cả nhóm sang bước mới là \"Thực hiện giải bài cụ thể\"."
        ],

        "goals"  : [
            "Thống nhất được cách làm phổ biến nhất là dùng đạo hàm để xét tính đơn điệu và vẽ bảng biến thiên."
        ],

        "acts" : []
    },
    {
        "stage" : "3",
        "name" : "Thực hiện giải bài.",
        "description" : "Thực hiện cụ thể các bước làm. Trong quá trình thực hiện có đánh giá, nhận xét kết quả từng bước.",
        "tasks" : [
            f"Thực hiện TỪNG BƯỚC một để giải bài theo lời giải sau:\n{SOLUTION}",
            "Khi đã giải quyết được đầy đủ các bước làm của lời giải trên, đề nghị cả nhóm sang quá trình cuối là \"Kết luận và dánh giá cả bài làm\"."
        ],
        "goals"  : [
            "Tính đạo hàm và xét dấu đúng.",
            "Nhận biết tính đơn điệu của một hàm số trên một khoảng dựa vào dấu đạo hàm cấp một của nó.",
            "Sử dụng bảng biến thiên để xét tính đơn điệu của hàm số. Biết lập bảng biến thiên và xét dấu.",
        ],
        "acts" : []
    },
    {
        "stage" : "4",
        "name" : "Kết luận.",
        "description" : "Kết luận lại quá trình làm bài và đánh giá kết quả.",
        "tasks" : [
            "Tóm tắt những bước chính đã làm.",
            "Đánh giá phương pháp đã làm.",
            "Rút ra được nguyên tắc làm bài.",
            "Khi đã giải quyết được câu các nhiệm vụ trên và nắm được các mục tiêu, kết thúc bài toán ở đây và kết thúc thảo luận."
        ],
        "goals"  : [
            "Rút ra được nguyên tắc làm dạng này như sau:\nBước 1: Tìm tập xác định D của hàm số.\nBước 2: Tính đạo hàm f^'(x) của các hàm số. Tìm các điểm {x_1;x_2;...;x_n }∈D mà tại đó đạo hàm f^'(x) bằng 0 hoặc không tồn tại.\nBước 3: Sắp xếp các điểm x_1;x_2;...;x_n theo thứ tự tăng dần. Xét dấu f^' (x) và lập bảng biến thiên.\nBước 4: Nêu kết luận về các khoảng đồng biến, nghịch biến của hàm số.",
        ],
        "acts" : []
    },
]

