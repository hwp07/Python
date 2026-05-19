# input: age(int), sys_bp(int), blood_sugar(int)
# output: thông báo lỗi, xác minh


# giải pháp 1: dùng các toán tử logic and, or để viết các điều kiện y khoa trên cùng một dòng lệnh if
# giải pháp 2: tầng 1 kiểm tra bẫy dữ liệu âm, tầng 2 kiểm tra từng chỉ số y khoa độc lập bằng cách lồng các khối if-else vào nhau để bóc tách chính xác chỉ số nào bị vi phạm


# => giải pháp 2



print("HỆ THỐNG SÀNG LỌC TIỀN PHẪU THUẬT")

age = int(input("Nhập tuổi bệnh nhân: "))
sys_bp = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập chỉ số đường huyết (mg/dL): "))

if age < 0 or sys_bp < 0 or blood_sugar < 0:
    print("\nLỖI: Dữ liệu nhập vào không hợp lệ")

else:
    print("\n--- KẾT QUẢ SÀNG LỌC ---")
    if age < 75:
        if 90 <= sys_bp <= 140:
            if blood_sugar < 150:
                print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
            else:
                print("TỪ CHỐI PHẪU THUẬT")
                print("Đường huyết vượt quá mức an toàn (Phải dưới 150 mg/dL).")
                
        else:
            print("  TỪ CHỐI PHẪU THUẬT")
            print("Huyết áp tâm thu ngoài khoảng an toàn (Yêu cầu: 90 - 140 mmHg).")
            
    else:
        print("  TỪ CHỐI PHẪU THUẬT")
        print("Bệnh nhân vượt quá độ tuổi phẫu thuật an toàn (Phải dưới 75 tuổi).")