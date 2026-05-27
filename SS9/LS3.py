# Danh sách đơn hàng ban đầu
order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    # Nhập lựa chọn
    choice = input("Nhập lựa chọn của bạn: ").strip()

    # Kiểm tra dữ liệu menu
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")

                for index, order in enumerate(order_list, start=1):
                    print(f"{index}. {order}")

        case 2:
            new_order = input("Nhập mã đơn hàng mới: ")
            new_order = new_order.strip().upper()

            order_list.append(new_order)

            print("Thêm đơn hàng thành công!")

        case 3:
            remove_order = input("Nhập mã đơn hàng cần xóa: ")
            remove_order = remove_order.strip().upper()

            if remove_order in order_list:
                order_list.remove(remove_order)
                print("Xóa đơn hàng thành công!")
            else:
                print("Không tìm thấy mã đơn hàng cần xóa!")

        case 4:
            print("Thoát chương trình.")
            break