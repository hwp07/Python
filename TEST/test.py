students = [
    {
        "id": "SV001",
        "name": "Nguyen Van A",
        "math_score": 8.5,
        "physic_score": 7.0,
        "chemistry_score": 9.0,
    }
]

def display_student(list):
    if len(list) == 0:
        print("Danh sách sinh viên hiện đang trống!")
        return
    
    print("\n--- DANH SÁCH SINH VIÊN ---")
    print(f"{"ID":<7} | {"Họ và tên":<20} | {"Điểm toán":<10} | {"Điểm lý":<10} | {"Điểm hóa":<10} | {"Điểm TB":<10} | {"Học lực":<20}")

    for i in list:
        avg_score = (
            float(i["math_score"]) +
            float(i["physic_score"]) +
            float(i["chemistry_score"])
        ) / 3


        if avg_score < 5:
            rank = "Yếu"
        elif avg_score < 7:
            rank = "Trung bình"
        elif avg_score < 8:
            rank = "Khá"
        else:
            rank = "Giỏi"

        print(f"{i["id"]:<7} | {i["name"]:<20} | {i["math_score"]:<10} | {i["physic_score"]:<10} | {i["chemistry_score"]:<10} | {avg_score:<10.2f} | {rank:<20}")



def check_score_input(score):
    try:
        score = float(score)

        if 0 <= score <= 10:
            return True

        print("Điểm phải từ 0 đến 10!")
        return False

    except ValueError:
        print("Điểm phải là số!")
        return False
        

def add_student(student_list):
    new_student = {}

    while True:
        new_student["id"] = input("Nhập mã SV: ")

        duplicate = False

        for i in student_list:
            if new_student["id"] == i["id"]:
                duplicate = True
                break

        if len(new_student["id"]) == 0 or duplicate:
            print("Mã SV không hợp lệ!")
            continue

        break


    while True:
        new_student["name"] = input("Nhập họ tên SV: ")

        if len(new_student["name"]) == 0:
            print("Tên SV không hợp lệ!")
            continue
        break

    while True:
        new_student["math_score"] = input("Nhập điểm Toán: ") 

        if not check_score_input( new_student["math_score"]):
            continue
        break

    while True:
        new_student["physic_score"] = input("Nhập điểm Lý: ") 

        if not check_score_input( new_student["physic_score"]):
            continue
        break

    while True:
        new_student["chemistry_score"] = input("Nhập điểm Hóa: ") 

        if not check_score_input( new_student["chemistry_score"]):
            continue
        break

    students.append(new_student)


def update_student(student_list):
    student_id = input("Nhập mã SV cần cập nhật: ")

    for student in student_list:
        if student["id"] == student_id:
            print(f"Tìm thấy sinh viên: {student['name']}")

            while True:
                math_score = input("Nhập điểm Toán mới: ")
                if check_score_input(math_score):
                    student["math_score"] = float(math_score)
                    break

            while True:
                physic_score = input("Nhập điểm Lý mới: ")
                if check_score_input(physic_score):
                    student["physic_score"] = float(physic_score)
                    break

            while True:
                chemistry_score = input("Nhập điểm Hóa mới: ")
                if check_score_input(chemistry_score):
                    student["chemistry_score"] = float(chemistry_score)
                    break

            print("Cập nhật điểm thành công!")
            return

    print("Không tìm thấy mã sinh viên!")


def del_student(student_list):
    input_id = input("Nhập mã sinh viên muốn xóa: ")

    for student in student_list:
        if student["id"] == input_id:
            student_list.remove(student)
            print("Xóa sinh viên thành công!")
            return

    print(f"Không tồn tại sinh viên có mã {input_id}")


def search_student(student_list):
    keyword = input("Nhập mã hoặc tên sinh viên cần tìm: ").strip().lower()

    result = []

    for student in student_list:
        if student["id"].lower() == keyword:
            result.append(student)

        elif keyword in student["name"].lower():
            result.append(student)

    if len(result) == 0:
        print("Không tìm thấy sinh viên phù hợp!")
        return

    display_student(student_list)

while True:
    print("""
--- STUDENTS MANAGER ---
1. Hiển thị danh sách sinh viên
2. Tiếp nhận sinh viên
3. Cập nhật kết quả học tập
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Thống kê điểm TB
7. Phân loại học lực
8. Thoát
""")
    
    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case "1":
            display_student(students)

        case "2":
            add_student(students)

        case "3":
            update_student(students)

        case "4":
            del_student(students)

        case "5":
            search_student(students)

        case "8":
            print("See you later!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")