# 1. new_prescription = old_prescription không tạo List mới mà chỉ tạo thêm một biến cùng trỏ tới List cũ => khi sử dụng append cũng làm thay đổi cẩ yesterday_prescription
# 2.
#  - cách 1: new_prescription = old_prescription.copy()
#  - cách 2: new_prescription = list(old_prescription)

# 3.  vì là string (immutable) nên chỉ tạo chuỗi mới nhưng không lưu lại kết quả
# 4. 
# new_prescription[0] = new_prescription[0].replace(
#     "Panadol",
#     "Paracetamol"
# )

yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()

    new_prescription[0] = new_prescription[0].replace("Panadol","Paracetamol")
    new_prescription.append("Oresol")

    return new_prescription

today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)