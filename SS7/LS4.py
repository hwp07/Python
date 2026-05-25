# input
#     số lượng phiếu đăng ký cần xử lý
#     chuỗi chứa thông tin đăng ký định dạng Họ tên | Khóa học | Mã học viên | Email

# output
#     in ra màn hình thông báo lỗi nếu dữ liệu rơi vào các "bẫy" (Edge cases)
#     in ra màn hình thông tin phiếu đăng ký đã chuẩn hóa theo format yêu cầu nếu dữ liệu hợp lệ

# giải pháp
#     tách dữ liệu: dùng phương thức .split('|') để chia chuỗi đầu vào thành một mảng (list) chứa 4 phần tử. kiểm tra độ dài mảng để bắt bẫy 2
#     chuẩn hóa họ tên & khóa học: chuỗi có thể dư khoảng trắng ở đầu, cuối hoặc giữa các từ. dùng .split() để tách rời các từ (tự động loại bỏ toàn bộ khoảng trắng thừa), sau đó dùng list comprehension kết hợp .capitalize() để viết hoa chữ cái đầu mỗi từ, và ghép lại bằng ' '.join()
#     chuẩn hóa mã học viên: dùng .strip() để xóa khoảng trắng hai đầu, dùng .upper() để viết hoa toàn bộ. kiểm tra độ dài len() < 5 để bắt bẫy 4
#     chuẩn hóa email: dùng .strip() để xóa khoảng trắng, dùng .lower() để viết thường toàn bộ. kiểm tra ký tự '@' bằng toán tử in để bắt bẫy 3
#     tạo mã xác nhận: ghép mã học viên và tên khóa học (đã viết hoa và dùng .replace(' ', '-') để biến khoảng trắng thành dấu gạch ngang).


num_forms = int(input("Nhập số lượng phiếu đăng ký: "))

if num_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")

else:
    for i in range(num_forms):
        raw_data = input("\nNhập chuỗi đăng ký: ")
        parts = raw_data.split("|")

        if len(parts) != 4: # đếm số lượng phần tử có trong 
            print("Dữ liệu đăng ký không hợp lệ")
            continue

        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_id = parts[2].strip().upper()
        email = parts[3].strip().lower()


        if "@" not in email:
            print("Email không hợp lệ")
            continue

        if len(student_id) < 5:
            print("Mã học viên không hợp lệ")
            continue

        confirmation_code = student_id + "_" + course_name.upper().replace(" ", "-")

        print("\n===== PHIẾU ĐĂNG KÝ =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_id)
        print("Email:", email)
        print("Mã xác nhận:", confirmation_code)