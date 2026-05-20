# total_budget đang được khai báo trong vòng lặp for dẫn đến mỗi lần chạy sẽ khởi tạo lại giá trị total_budget = 0
# => cần khởi tạo biến bên ngoài vòng lặp

# code
total_budget = 0
for employee_number in range(1,4):
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input('Nhập mức lương (VNĐ): '))
    total_budget = total_budget + salary

print('=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ: ',total_budget,'VNĐ')
