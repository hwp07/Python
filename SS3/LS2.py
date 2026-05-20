# code bị lỗi vì câu lệnh if đang thiếu lệnh thoát ra khỏi vòng lặp dẫn đến dòng lệnh chúc mừng bên dưới luôn được in ra với mọi ngày công
# => thêm continue để thoát ra khỏi câu lệnh if nếu điều kiện k thỏa mãn

print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")
    
    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))
    
    # Kiểm tra điều kiện
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        continue # thêm điều kiện 
        
    bonus_amount = working_days * 200000
    print("→ Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiền thưởng!")
    print("--------------------------------------------------\n")
    
print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")