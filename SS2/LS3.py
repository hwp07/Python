# input: name(str), age(int)

# output: 
# + thông báo lỗi 
# + in ra phiếu khám


# giải pháp:
# + sử dụng hàm .strip() để loai bỏ khoảng trắng đầu cuối
# + sử dụng toán tử or kết hợp if else


name = input("Nhập họ và tên bệnh nhân: ").strip()
age = int(input("Nhập tuổi của bệnh nhân: "))

if name == "" or age < 0 or age > 150:
    print("\nLỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")

else:
    if age < 6:
        triage_result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif age >= 80:
        triage_result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        triage_result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    print("           PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print(f"Họ và tên bệnh nhân : {name}")
    print(f"Tuổi                : {age}")
    print(f"Kết quả phân luồng  : {triage_result}")
