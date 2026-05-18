# Thu thập dữ liệu
patient_name = input("Nhập họ tên: ")
patient_id = input("Nhập mã BN (VD: BN001): ")

body_temperature = float(input("Nhập nhiệt độ (VD: 36.5): "))
heart_rate = int(input("Nhập nhịp tim (VD: 80): "))
weight = float(input("Nhập cân nặng (VD: 55.5): "))

# Hiển thị
print("\n=== PHIẾU KHÁM ===")
print("Tên:", patient_name)
print("Mã BN:", patient_id)
print("Nhiệt độ:", body_temperature)
print("Nhịp tim:", heart_rate)
print("Cân nặng:", weight)

print("\n=== LOG HỆ THỐNG ===")
print(type(body_temperature))
print(type(heart_rate))
print(type(weight))