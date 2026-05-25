# phân tích lỗi:
#  - strip(), title(), upper(), lower() không sửa trực tiếp chuỗi gốc
#  - cần tạo biến mới sau đó gán để tạo ra đúng kết quả

# code
student_name = " nguYEn vAn a "
student_code = " rk-001-python "
email = " Student01@GMAIL.COM "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)