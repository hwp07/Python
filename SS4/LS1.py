# nhập tổng tiền hóa đơn
total_money = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

# kiểm tra điều kiện giảm giá
if total_money >= 500000:
    discount = total_money * 0.10
else:
    discount = 0

# tính số tiền cần thanh toán
final_money = total_money - discount

# hiển thị kết quả
print("\nHÓA ĐƠN THANH TOÁN RIKKEI STORE")
print("Số tiền được giảm giá:", int(discount), "VND")
print("Tổng tiền khách phải trả:", int(final_money), "VND")