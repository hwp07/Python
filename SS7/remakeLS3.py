raw_data = " eMP-001; nguyen van a ;0987654321; sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("""
   HỆ THỐNG QUẢN LÝ NHÂN SỰ
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình
""")
    
    choice = int(input('Nhap chuc nang: '))

    new_raw_data = raw_data.split("|")

    match choice:
        case 1:
            print(f"Du lieu goc: {raw_data}")

        case 2:
            for employee in new_raw_data:  # có thể sử dụng range(len(new_raw_data))
                employee_detail = employee.strip().split(";")

                id = employee_detail[0].strip().upper()
                name = employee_detail[1].strip().title()
                phone = employee_detail[2].strip().replace("-", "")
                department = employee_detail[3].strip().upper()

                if phone.isdigit():
                    phone = "******" + phone[-4:]
                else :
                    phone = 'Invalid format'

                print(f"\nID: {id}\nHọ tên: {name}\nPhòng ban: {department}\nSố điện thoại: {phone}")
        case 3:
            print()

        case 4:
            print()

