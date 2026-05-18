# Input
# Mã bệnh nhân: string
# Nhiệt độ: string
# Nhịp tim: string


# Output
# Nhiệt độ: float
# Nhịp tim: int


# Giải pháp ép kiểu
# Ép kiểu qua biến trung gian
# Ép kiểu trực tiếp khi nhập


# Chọn giải pháp
# Chọn biến trung gian vì dễ kiểm tra lỗi và an toàn hơn.


ma_benh_nhan = "BN999"
nhiet_do_raw = "37.5"
nhip_tim_raw = "85"

nhiet_do = float(nhiet_do_raw)
nhip_tim = int(nhip_tim_raw)

print("=== KẾT QUẢ ===")
print("Mã bệnh nhân:", ma_benh_nhan)

print("Nhiệt độ:", nhiet_do)
print(type(nhiet_do))

print("Nhịp tim:", nhip_tim)
print(type(nhip_tim))