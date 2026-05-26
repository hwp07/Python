# input: raw_data(str), choice(int), search_id(str)
# output:
#     case 1: hiển thị dữ liệu gốc
#     case 2: 
#         ID viết hoa
#         họ tên viết hoa chữ cái đầu
#         xóa dấu - trong số điện thoại
#         ẩn 6 số đầu của số điện thoại
#         ohòng ban viết hoa

#     case 3: thông tin nhân viên cần tìm hoặc thông báo lỗi không tìm thấy nhân viên
#     case 4: thông báo thoát chương trình


# giải pháp: sử dụng:
#     while True để tạo menu lặp
#     match-case để xử lý từng chức năng
#     split() để tách dữ liệu
#     strip() để xóa khoảng trắng
#     upper() để chuẩn hóa ID và phòng ban
#     title() để chuẩn hóa họ tên
#     replace() để xóa dấu -
#     isdigit() để kiểm tra số điện thoại hợp lệ

raw_data = " eMP-001; nguyen van a ;0987654321; sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("""
   HỆ THỐNG QUẢN LÝ NHÂN SỰ
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình
""")

    choice = int(input("Nhập sự lựa chọn của bạn: "))

    match choice:
        case 1:
            print(raw_data)

        case 2:
            employees = raw_data.strip().split("|")

            for emp in employees:
                parts = emp.strip().split(";")

                emp_id = parts[0].strip().upper()
                name = parts[1].strip().title()
                phone = parts[2].strip().replace("-", "")
                department = parts[3].strip().upper()


                # kiểm tra số điện thoại
                if phone.isdigit():
                    phone = "******" + phone[-4:]
                else:
                    phone = "Invalid Format"

                print(f"\nID: {emp_id}\nHọ tên: {name}\nPhòng ban: {department}\nSố điện thoại: {phone}")

        case 3:
            search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()

            employees = raw_data.strip().split("|")
            found = False

            for emp in employees:
                parts = emp.strip().split(";")

                emp_id = parts[0].strip().upper()
                name = parts[1].strip().title()
                phone = parts[2].strip().replace("-", "")
                department = parts[3].strip().upper()

                # kiểm tra số điện thoại
                if phone.isdigit():
                    phone = "******" + phone[-4:]
                else:
                    phone = "Invalid Format"

                # so sánh ID
                if emp_id == search_id:
                    found = True
                    print(f"\nID: {emp_id}\nHọ tên: {name}\nPhòng ban: {department}\nSố điện thoại: {phone}")
                    break

            if not found:
                print("Không tìm thấy nhân viên")

        case 4:
            print("Thoát chương trình")
            break