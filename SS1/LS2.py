print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân (kg): "))

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

# Trưởng nhóm IT viết thêm dòng này để kiểm tra dữ liệu của cân nặng
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))