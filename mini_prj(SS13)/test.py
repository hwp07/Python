employee_list = []

while True:
    print("=" * 50)
    print("         QUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("=" * 50)
    print("""
1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Tìm kiếm nhân viên (theo mã)
4. Xóa nhân viên khỏi hệ thống
5. Thoát chương trình
""")
    print("=" * 50)

    choie = input("Nhập lựa chọn của bạn: ")

    match choie:
        case "1":

            name = input("\nTên nhân viên: ")
            if name == "":
                print("Tên nhân viên không được để trống.")
                    


            salary = input("Mức lương: ")
            input_salary = float(salary)
            if input_salary < 0:
                print("Mức lương không hợp lệ! Vui lòng nhập lại!")
                continue


            if employee_list == []:
                id = 101
            else:
                id += 1

            new_employee = {
                "id": id,
                "name": name,
                "salary": input_salary
            }

            employee_list.append(new_employee)
            print(f"Thêm nhân viên thành công! ID: [{id}]")

        case "2":
            if employee_list == []:
                print("Chưa có dữ liệu nhân sự!")
                continue
            
            print(f"{'ID':<10} | {'TÊN NHÂN VIÊN':<30} | {'MỨC LƯƠNG':<15}")
            print("-" * 65)

            for employee in employee_list:
                print(
                    f"{employee['id'] :<10} | " 
                    f"{employee['name'] :<30} | " 
                    f"{employee['salary'] :<15}" 
                )

        case "5":
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")
            continue

