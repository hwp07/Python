import random

name = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính: ")
birth_year = int(input("Nhập năm sinh: "))
phone = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng ban đầu: ")
examination_fee = float(input("Nhập chi phí khám: "))

random_number = random.randint(100, 999)
patient_id = f"BN{birth_year}{random_number}"


print("\nTHẺ BỆNH NHÂN  ")
print("Mã BN      :", patient_id)
print("Tên        :", name, type(name))
print("Giới tính  :", gender, type(gender))
print("Năm sinh   :", birth_year, type(birth_year))
print("Điện thoại :", phone, type(phone))
print("Email      :", email, type(email))
print("Triệu chứng:", symptom, type(symptom))
print("Chi phí    :", examination_fee, "VND", type(examination_fee))