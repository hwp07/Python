blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


def find_blood_bag_index(inventory, bag_id):
    bag_id = bag_id.strip().upper()

    for index, bag in enumerate(inventory):
        data = bag.split("-")

        if data[0] == bag_id:
            return index

    return -1


def display_inventory(inventory):
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    total_volume = 0

    print("\n--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("-" * 62)

    for bag in inventory:
        data = bag.split("-")

        bag_id = data[0]
        donor = data[1]

        if data[3] == "":
            blood_group = data[2] + "-"
            volume = data[4]
            expiry = data[5]
        else:
            blood_group = data[2]
            volume = data[3]
            expiry = data[4]

        total_volume += int(volume)

        print(
            f"{bag_id:<6} | "
            f"{donor:<16} | "
            f"{blood_group:<9} | "
            f"{volume} ml".ljust(8) + " | "
            f"{expiry}"
        )

    print("-" * 62)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    bag_id = input("Nhập mã túi máu mới: ").strip().upper()

    if bag_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    if find_blood_bag_index(inventory, bag_id) != -1:
        print(f"Lỗi: Mã túi máu {bag_id} đã tồn tại! Vui lòng nhập mã khác.")
        return

    donor = input("Nhập tên người hiến: ").strip().title()

    if donor == "":
        print("Lỗi: Tên người hiến không được để trống!")
        return

    blood_group = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()

    if not volume.isdigit() or int(volume) <= 0:
        print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    record = "-".join([
        bag_id,
        donor,
        blood_group,
        volume,
        expiry
    ])

    inventory.append(record)

    print(f"\nThành công: Đã nhập túi máu {bag_id} vào kho!")


def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    bag_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()

    if bag_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag_index(inventory,bag_id)

    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {bag_id} trong kho!")
        return

    new_expiry = input("Nhập ngày hết hạn mới: ").strip()

    data = inventory[index].split("-")

    data[-1] = new_expiry

    inventory[index] = "-".join(data)

    print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {bag_id}!")


def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    bag_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()

    if bag_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag_index(inventory,bag_id)

    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {bag_id} trong kho!")
        return

    inventory.pop(index)

    print(f"\nThành công: Đã xuất túi máu {bag_id} khỏi kho!")


while True:
    print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
    print("1. Xem danh sách túi máu trong kho")
    print("2. Nhập túi máu mới")
    print("3. Gia hạn / Sửa ngày hết hạn")
    print("4. Xuất / Hủy túi máu")
    print("5. Thoát chương trình")
    print("========================================")

    choice = input("Chọn chức năng (1-5): ").strip()

    match choice:
        case "1":
            display_inventory(blood_inventory)

        case "2":
            add_blood_bag(blood_inventory)

        case "3":
            update_expiry(blood_inventory)

        case "4":
            remove_blood_bag(blood_inventory)

        case "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")