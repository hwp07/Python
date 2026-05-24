# phân tích lỗi
# 1. vòng lặp ngoài đang duyệt theo tháng trước, sau đó mới tới chi nhánh
# 2. vòng lặp ngoài nên duyệt theo chi nhánh rồi mới đến theo tháng

# code

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3
for branch in range(1, branch_count + 1):
    print(f"\n===== Chi nhánh {branch} =====")
    total = 0
    for month in range(1, month_count + 1):
        revenue = int(
            input(f"Nhập doanh thu tháng {month}: ")
        )
        total += revenue
        print(
            f"Tháng {month}: {revenue} triệu đồng"
        )

    print(f"Tổng doanh thu chi nhánh {branch}: {total} triệu đồng")