# khởi tạo biến
total_revenue = 0
high_revenue_days = 0

# doanh thu 7 ngày
for day in range(1, 8):
    revenue = int(input(f"Nhập doanh thu Ngày {day}: "))
    
    total_revenue += revenue

    if revenue >= 5000000:
        high_revenue_days += 1

average_revenue = total_revenue / 7

# hiển thị kết quả
print("\n--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print("Tổng doanh thu cả tuần:", total_revenue, "VND")
print("Doanh thu trung bình mỗi ngày:", int(average_revenue), "VND")
print("Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND):", high_revenue_days, "ngày")