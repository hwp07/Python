# input/output
# input: branch_count(int), student_count(int)
# output: trạng thái lớp học, các thông báo lỗi

# giải pháp:
# 1. nhập số lượng chi nhánh
# 2. duyệt từng chi nhánh
# 3. mỗi chi nhánh có 2 lớp học
# 4. nhập số học viên đi học
# 5. kiểm tra dữ liệu hợp lệ bằng while
# 6. nếu lớp vắng toàn bộ -> bỏ qua đánh giá
# 7. nếu >= 20 -> lớp học ổn định
# 8. nếu < 20 -> lớp cần được nhắc nhở theo dõi



branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}:")

    for classroom in range(1, 3):
        while True:
            student_count = int(
                input(
                    f"Nhập số học viên đi học của lớp {classroom}: "
                )
            )

            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue
            break

        if student_count == 0:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
            )
            continue

        if student_count >= 20:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp học ổn định"
            )

        else:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp cần được nhắc nhở theo dõi"
            )