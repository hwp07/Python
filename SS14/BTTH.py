grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]


def display_grades(book):   
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<5} | {'Tên Học Sinh':<15} | {'Điểm Toán':<5} | {'Điểm Anh':<5} | {'ĐTB':<5}")
    print("-" * 55)
    for i in book:
        avg = (i["info"][0] + i["info"][1]) / 2

        print(f"{i['id']:<5} | {i['name']:<15} | {i['info'][0]:<9} | {i['info'][1]:<9}| {avg:<5.2f}")

    print("-" * 55)


def add_student(book):
    while True:
        new_student = {}
        flag = 1

        new_student["id"] = input("Nhập mã học sinh mới: ")
        for i in book:
            if i["id"] == new_student["id"]:
                print(f"Lỗi: Mã học sinh {i["id"]} đã tồn tại! Vui lòng nhập mã khác.\n")
                flag = 0
                continue
        
        if flag == 1:
            new_student["name"] = input("Nhập tên học sinh: ")

            math_score = float(input("Nhập điểm Toán: "))
            english_score = float(input("Nhập điểm Anh: "))

            new_student["info"] = (math_score, english_score)

            book.append(new_student)

            print(f"Thành công: Đã thêm học sinh {new_student["id"]} vào hệ thống!\n")
            break


def update_scores(book):
    while True:
        find = input("Nhập mã học sinh cần cập nhật: ")

        for i in book:
            if find == i["id"]:
                new_math = float(input("Nhập điểm Toán mới: "))
                new_english = float(input("Nhập điểm Anh mới: "))

                i["info"] = (new_math, new_english)

                print(f"Thành công: Đã cập nhật điểm cho học sinh {i['id']}!")
                return

        print("Không tìm thấy mã học sinh!")


def delete_student(book):
    while True:
        find = input("Nhập mã học sinh cần xóa: ")

        for student in book:
            if find == student["id"]:
                book.remove(student)
                print(f"Thành công: Đã xóa hồ sơ học sinh {student['id']} khỏi hệ thống!")
                return

        print("Không tìm thấy mã học sinh!")


if __name__ == "__main__":
    while True:
        print("""
=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
""")

        choice = input("Nhập lựa chọn: ")

        match choice:
            case "1":
                display_grades(grade_book)

            case "2":
                add_student(grade_book)

            case "3":
                update_scores(grade_book)

            case "4":
                delete_student(grade_book)

            case "5":
                print("Thoát chương trình.")
                break

            case _:
                print("Lựa chọn không hợp lệ!")