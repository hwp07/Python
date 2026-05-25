raw_input = "   nGuyen vaN aN  ;  2004   "

while True:
    print("""
===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
=====================================
""")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            print("\nDữ liệu gốc:")
            print(raw_input)

        case 2:
            parts = raw_input.split(";")

            name = parts[0].strip().title()
            birth_year = parts[1].strip()

            age = 2026 - int(birth_year)

            print("\n===== THÔNG TIN THÀNH VIÊN =====")
            print(f"Họ tên   : {name}")
            print(f"Năm sinh : {birth_year}")
            print(f"Tuổi     : {age}")

        case 3:
            parts = raw_input.split(";")

            name = parts[0].strip().title()
            birth_year = parts[1].strip()

            words = name.split()

            first_name = words[0]
            middle_name = words[1]
            last_name = words[2]

            email = (
                first_name[0]
                + middle_name[0]
                + last_name
            ).lower() + "@company.com"

            member_id = last_name.upper() + birth_year[-2:]

            print("      THẺ THÀNH VIÊN")
            print(f"Họ tên : {name}")
            print(f"Email  : {email}")
            print(f"Mã ID  : {member_id}")

        case 4:
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")