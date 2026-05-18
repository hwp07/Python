# Input
# Họ tên bệnh nhân (string)
# Mã bệnh án (string)
# Khoa/phòng khám (string)


# Output
# Hiển thị phiếu khám bệnh điện tử gồm:
# Họ tên
# Mã bệnh án
# Khoa khám
# Trạng thái tiếp nhận


# Thuật toán
# Bắt đầu
# Nhập họ tên
# Nhập mã bệnh án
# Nhập khoa khám
# Hiển thị phiếu khám bệnh
# Kết thúc

# Code
# Tiếp nhận bệnh nhân

ho_ten = input("Nhập họ tên bệnh nhân: ")
ma_benh_an = input("Nhập mã bệnh án: ")
khoa_kham = input("Nhập khoa/phòng khám: ")

print("\n   PHIẾU KHÁM BỆNH")
print("Họ tên bệnh nhân:", ho_ten)
print("Mã bệnh án:", ma_benh_an)
print("Khoa khám:", khoa_kham)
print("Trạng thái: Đã tiếp nhận thành công")