parking_lot = []
next_id = 1

while True:
    print("\n" + "=" * 50)
    print("          QUẢN LÝ BÃI XE - SMART PARING")
    print("=" * 50)
    print("""    1. Check-in (Đăng ký xe vào)
    2. Báo cáo tồn kho (Hiện thị danh sách)
    3. Tìm kiếm xe (Theo biển số)
    4. Check-out (Xư lý xe ra & Tính phí)
    5. Thoát chương trình""")

    print("=" * 50)

    choice = input("\nNhập lựa chọn của bạn (1-5): ")

    match choice:
        case "1":
            print("\n===== CHECK-IN =====")

            while True:
                plate = input("Nhập biển số xe: ").strip()

                if plate == "":
                    print("Biển số không được để trống!")
                    continue

                exist = False

                for xe in parking_lot:
                    if xe["plate"] == plate.upper():
                        exist = True
                        break

                if exist:
                    print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
                    continue
                break

            while True:
                vehicle_type = input("Loại xe (1.Xe máy, 2.Ô tô): ")

                if vehicle_type not in ["1", "2"]:
                    print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
                    continue

                vehicle_type = int(vehicle_type)
                break

            while True:
                entry_time = input("Nhập giờ vào: ")

                if not entry_time.isdigit():
                    print("Giờ phải là số!")
                    continue

                entry_time = int(entry_time)

                if entry_time < 0 or entry_time > 24:
                    print("Giờ không hợp lệ!")
                    continue

                break

            vehicle = {
                "id": next_id,
                "plate": plate.upper(),
                "type": vehicle_type,
                "entry_time": entry_time
            }

            parking_lot.append(vehicle)
            next_id += 1

            print(f"\n[Thành công]: Xe {vehicle['plate']} đã được đăng ký vào bãi")

        case "2":
            print("\n===== DANH SÁCH XE =====\n")

            if len(parking_lot) == 0:
                print("Bãi xe hiện đang trống!")
            else:
                print(f"{'ID':<3} | {'Biến số xe':<15} | {'Loại xe':<10} | {'Giờ vào'}")
                print("-" * 45)

                for xe in parking_lot:
                    vehicle_type = "Xe máy"

                    if xe["type"] == 2:
                        vehicle_type = "Ô tô"

                    print(
                        f"{xe['id']:<3} | "
                        f"{xe['plate']:<15} | "
                        f"{vehicle_type:<10} | "
                        f"{xe['entry_time']}"
                    )

        case "3":
            print("\n===== TÌM KIẾM XE =====")

            plate_search = input("Nhập biển số cần tìm: ").strip().upper()

            found = False

            for xe in parking_lot:
                if xe["plate"] == plate_search:
                    vehicle_type = "Xe máy"

                    if xe["type"] == 2:
                        vehicle_type = "Ô tô"

                    print(f"{'ID':<3} | {'Biến số xe':<15} | {'Loại xe':<10} | {'Giờ vào'}")
                    print("-" * 45)
                    print(
                        f"{xe['id']:<3} | "
                        f"{xe['plate']:<15} | "
                        f"{vehicle_type:<10} | "
                        f"{xe['entry_time']}"
                    )

                    found = True
                    break

            if not found:
                print("Không tìm thấy xe!")

        case "4":
            print("\n===== CHECK-OUT =====")

            plate_out = input("Nhập biển số xe: ").strip().upper()

            found = False

            for xe in parking_lot:
                if xe["plate"] == plate_out:

                    while True:
                        exit_time = input(
                            f"Nhập giờ ra ({xe['entry_time']} - 24): "
                        )

                        if not exit_time.isdigit():
                            print("Giờ ra không hợp lệ!")
                            continue

                        exit_time = int(exit_time)

                        if exit_time < xe["entry_time"] or exit_time > 24:
                            print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
                            continue

                        break

                    hours = exit_time - xe["entry_time"]

                    if xe["type"] == 1:
                        price = 5000
                        vehicle_type = "Xe máy"
                    else:
                        price = 10000
                        vehicle_type = "Ô tô"

                    total = hours * price

                    print("\n===== HÓA DƠN =====")
                    print(f"Bien so   : {xe['plate']}")
                    print(f"Loai xe   : {vehicle_type}")
                    print(f"Gio vao   : {xe['entry_time']}h")
                    print(f"Gio ra    : {exit_time}h")
                    print(f"So gio    : {hours}")
                    print(f"Thanh tien: {total:,} VND")

                    parking_lot.remove(xe)

                    print("Xe đã ra khỏi bãi!")
                    found = True
                    break

            if not found:
                print("Không tìm thấy xe!")

        case "5":
            print("Tạm biệt!")
            break

        case _:
            print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")