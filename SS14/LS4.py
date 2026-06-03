student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def calculate_average(student):
    return (
        student["math"]
        + student["physics"]
        + student["chemistry"]
    ) / 3


def display_grades(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):
        avg = calculate_average(student)

        if avg >= 8:
            rank = "Giỏi"
        elif avg >= 6.5:
            rank = "Khá"
        elif avg >= 5:
            rank = "Trung bình"
        else:
            rank = "Yếu"

        print(
            f"{index}. [{student['student_id']}] {student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {avg:.2f} - {rank}"
        )

    print("---------------------------")


def update_student_score(records):
    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    student_found = None

    for student in records:
        if student["student_id"] == student_id:
            student_found = student
            break

    if student_found is None:
        print(
            f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!"
        )
        return

    subject_choice = input(
        "Chọn môn học (1-Toán, 2-Lý, 3-Hóa): "
    )

    if subject_choice == "1":
        subject_key = "math"
        subject_name = "Toán"
    elif subject_choice == "2":
        subject_key = "physics"
        subject_name = "Lý"
    elif subject_choice == "3":
        subject_key = "chemistry"
        subject_name = "Hóa"
    else:
        print("Lựa chọn môn học không hợp lệ!")
        return

    while True:
        try:
            new_score = float(input("Nhập điểm mới: "))

            if 0 <= new_score <= 10:
                break

            print(
                "Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!"
            )

        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")

    student_found[subject_key] = new_score

    print(
        f">> Đã cập nhật điểm {subject_name} của sinh viên "
        f"'{student_found['name']}' thành {new_score}."
    )


def generate_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    passed = 0
    failed = 0

    for student in records:
        avg = calculate_average(student)

        if avg >= 5:
            passed += 1
        else:
            failed += 1

    passed_percent = passed / total_students * 100
    failed_percent = failed / total_students * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): "
        f"{passed} sinh viên "
        f"(Chiếm {passed_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): "
        f"{failed} sinh viên "
        f"(Chiếm {failed_percent:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    top_avg = calculate_average(top_student)

    for student in records:
        current_avg = calculate_average(student)

        if current_avg > top_avg:
            top_avg = current_avg
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(
        f"Sinh viên: {top_student['name']} "
        f"(Mã: {top_student['student_id']})"
    )
    print(f"Điểm Trung Bình: {top_avg:.2f}")
    print(
        "Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!"
    )
    print("--------------------------")


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
        print("1. Xem bảng điểm và học lực")
        print("2. Cập nhật điểm thi sinh viên")
        print("3. Báo cáo thống kê (Đỗ/Trượt)")
        print("4. Tìm sinh viên Thủ khoa")
        print("5. Thoát chương trình")
        print("======================================================")

        choice = input("Chọn chức năng (1-5): ")

        match choice:
            case "1":
                display_grades(student_records)

            case "2":
                update_student_score(student_records)

            case "3":
                generate_report(student_records)

            case "4":
                find_valedictorian(student_records)

            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()