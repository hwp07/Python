plate_out = input("Nhập biển số cần lấy: ")

for xe in parking_lot:
    if xe["plate"] == plate_out.upper():

        gio_ra = int(input("Nhập giờ ra: "))
        so_gio = gio_ra - xe["entry_time"]

        don_gia = 2000 if xe["type"] == 1 else 5000
        tong_phi = so_gio * don_gia

        print("Tổng phí:", tong_phi, "VND")

        parking_lot.remove(xe)
        print("Check-out thành công!")
        break
else:
    print("Không tìm thấy xe")