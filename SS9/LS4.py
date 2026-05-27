order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED",
    "GE004 - PENDING"
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình          
""")
    
    choice = input("Chọn chức năng: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            print("Danh sách đơn hàng hiện tại:")
            for index, item in enumerate(order_list, start=1):
                print(f"{index}. {item}")

        case 2:
            while True:
                print("""
----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính""")
                
                option = input("Nhập lựa chọn: ")

                if not option.isdigit():
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                    continue

                option = int(option)

                match option:
                    case 1:
                        new_id = input("Mã đơn hàng: ")
                        new_status = input("Trạng thái: ")

                        new_order = new_id.strip().upper() + " - " + new_status.strip().upper()

                        order_list.append(new_order)

                        print("Đã thêm đơn hàng!")

                    case 2:
                        index = (input("Nhập vị trí đơn hàng cần sửa: "))

                        if not index.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue

                        index = int(index)

                        if index < 1 or index > len(order_list):
                            print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            new_id = input("Nhập mã đơn mới: ")
                            new_status = input("Nhập trạng thái mới: ")

                            new_order = new_id.strip().upper() + " - " + new_status.strip().upper()

                            order_list[index - 1] = new_order

                            print("Đã cập nhật đơn hàng!")

                    case 3:
                        delete = input("Nhập vị trí đơn hàng cần xóa: ")

                        if not delete.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue

                        delete = int(delete)

                        if delete < 1 or delete > len(order_list):
                            print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            del_order = order_list.pop(order_list[delete - 1])

                            print("Đã xóa đơn hàng!")
  
                    case 4:
                        break

        case 3:
            pending = 0
            delivering = 0
            completed = 0
            cancelled = 0

            for item in order_list:
                part = item.split(" - ")

                status = part[1]

                if status == "PENDING":
                    pending += 1

                elif status == "DELIVERING":
                    delivering += 1

                elif status == "COMPLETED":
                    completed += 1

                elif status == "CANCELLED":
                    cancelled += 1

            print("===== THỐNG KÊ ĐƠN HÀNG =====")
            print(f"PENDING: {pending}")
            print(f"DELIVERING: {delivering}")
            print(f"COMPLETED: {completed}")
            print(f"CANCELLED: {cancelled}")
            print(f"Tổng số đơn hàng: {len(order_list)}")

        case 4:
            print("Thoát chương trình!")
            break