# phân tích lỗi
# strip() không sửa trực tiếp chuỗi gốc mà trả về chuỗi mới
# chuỗi được phân tách bằng ký tự "|"
# transaction.split("-") sai vì dấu - chỉ nằm trong mã khóa học PYTHON-01
# khi split sai:
# parts[0] -> "nguyEN vAn a | PYTHON"
# parts[1] -> "01 | 00000 | paid"
# -> dữ liệu bị sai, lệch
# => cần .strip() từng phần để xóa khoảng trắng dư sau khi tách
# => cần đổi amount sang số (int) trước khi định dạng tiền để xử lý đúng dữ liệu số

transaction = " nguyEN vAn a | PYTHON-01 | 00000 | paid "

transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", amount, "VND")
print("Trạng thái:", status)