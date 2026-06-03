students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def validate_score(score_input):
    try:
        score = float(score_input)
        return 0 <= score <= 10
    except ValueError:
        return False


def find_student_by_id(student_list, student_id):
    for index in range(len(student_list)):
        if student_list[index]["id"] == student_id:
            return index
    return -1


def get_rank(average_score):
    if average_score >= 8:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def display_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    print("--- DANH SÁCH HỌC SINH ---")
    for index, i in enumerate(student_list, start=1):
        print(f"{index}. Mã: {i["student_id"]} | Tên: {i["name"]:<15} | Toán: {i["math_score"]} | Anh: {i["english_score"]}")


def add_student(student_list):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()

        if find_student_by_id(student_list, student_id) != -1:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue
        break

    while True:
        name = input("Nhập tên học viên: ").strip().title()

        if name == "":
            print("Tên học viên không được để trống!")
            continue
        break

    while True:
        math_score = input("Nhập điểm Toán: ")

        if validate_score(math_score):
            math_score = float(math_score)
            break

        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    while True:
        english_score = input("Nhập điểm Anh: ")

        if validate_score(english_score):
            english_score = float(english_score)
            break

        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    student_list.append({
        "id": student_id,
        "name": name,
        "info": (math_score, english_score)
    })

    print("Thêm học viên thành công!")


def update_score(student_list):
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()

    index = find_student_by_id(student_list, student_id)

    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    while True:
        math_score = input("Nhập điểm Toán mới: ")

        if validate_score(math_score):
            math_score = float(math_score)
            break

        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    while True:
        english_score = input("Nhập điểm Anh mới: ")

        if validate_score(english_score):
            english_score = float(english_score)
            break

        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    student_list[index]["info"] = (math_score, english_score)

    print(f"Cập nhật điểm cho học viên {student_id} thành công!")


def evaluate_students(student_list):
    print("\n===== ĐÁNH GIÁ HỌC LỰC =====")

    for student in student_list:
        average = (student["info"][0] + student["info"][1]) / 2

        rank = get_rank(average)

        print(
            f"Mã: {student['id']} | "
            f"Tên: {student['name']} | "
            f"ĐTB: {average:.2f} | "
            f"Xếp loại: {rank}"
        )



if __name__ == "__main__":
    while True:
        print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
1. Hiển thị danh sách học viên
2. Thêm học viên mới
3. Cập nhật điểm thi theo mã học viên
4. Đánh giá học lực của toàn bộ học viên
5. Thoát chương trình
""")
        
        choice = input("Nhập lựa chọn: ")

        match choice:
            case "1":
                display_students(students)

            case "2":
                add_student(students)

            case "3":
                update_score(students)

            case "4":
                evaluate_students(students)

            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")
