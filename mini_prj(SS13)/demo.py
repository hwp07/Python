list_emp = []

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

    choice = input("Nhập lựa chọn của bạn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            new_employee = {}

            if len(list_emp) == 0:
                new_employee["id"] = 101
            else:
                new_employee["id"] = list_emp[-1]["id"] + 1

            while True:
                name = input("Mời bạn nhập tên: ")

                if not name.strip():
                    print("Tên không được để trống!")
                else:
                    new_employee["name"] = name
                    break

            while True:
                salary = input("Mời bạn nhập lương: ")

                if not salary:
                    print("Mức lương không được để trống!")
                    continue

                if not salary.replace(".", "", 1).isdigit():
                    print("Mức lương phải là số!")
                    continue

                salary = float(salary)

                if salary < 0:
                    print("Mức lương không hợp lệ!")
                    continue

                new_employee["salary"] = salary
                break

            list_emp.append(new_employee)
            print("Thêm nhân viên thành công!")

        case 2:
            if not list_emp:
                print("Chưa có dữ liệu!")
            else:
                print(f"\n{'ID':<10} | {'TÊN NHÂN VIÊN':<30} | {'MỨC LƯƠNG':<15}")
                print("-" * 65)

                for emp in list_emp:
                    print(
                        f"{emp['id']:<10} | "
                        f"{emp['name']:<30} | "
                        f"{emp['salary']:<15,.0f}"
                    )

        case 3:
            if not list_emp:
                print("Chưa có dữ liệu!")
                continue

            id_search = input("Nhập mã nhân viên cần tìm: ")

            if not id_search.isdigit():
                print("Mã nhân viên không hợp lệ!")
                continue

            id_search = int(id_search)

            found = False

            for emp in list_emp:
                if emp["id"] == id_search:
                    print("\nThông tin nhân viên:")
                    print(f"ID: {emp['id']}")
                    print(f"Tên: {emp['name']}")
                    print(f"Lương: {emp['salary']}")
                    found = True
                    break

            if not found:
                print("Không tìm thấy nhân viên!")

        case 4:
            if not list_emp:
                print("Chưa có dữ liệu!")
                continue

            id_delete = input("Nhập mã nhân viên cần xóa: ")

            if not id_delete.isdigit():
                print("Mã nhân viên không hợp lệ!")
                continue

            id_delete = int(id_delete)

            found = False

            for emp in list_emp:
                if emp["id"] == id_delete:
                    list_emp.remove(emp)
                    print("Xóa nhân viên thành công!")
                    found = True
                    break

            if not found:
                print("Không tìm thấy nhân viên!")

        case 5:
            print("Thoát chương trình!")
            break

        case _:
            print("Vui lòng chọn từ 1 đến 5!")