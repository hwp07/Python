cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n" + "=" * 55)
    print("        SHOPEE CART MANAGEMENT SYSTEM")
    print("=" * 55)

    print("1. Xem chi tiết giỏ hàng và tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")

    choice = input("\nMời bạn chọn chức năng (1-5): ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn phải từ 1 đến 5!")
        continue

    match choice:
        case 1:
            if len(cart_items) == 0:
                print("\nGiỏ hàng đang rỗng!")
                continue

            print("\n===== CHI TIẾT GIỎ HÀNG =====")

            print(
                f"{'STT':<5}"
                f"{'Mã SP':<10}"
                f"{'Tên Sản Phẩm':<30}"
                f"{'SL':<10}"
                f"{'Đơn Giá':<15}"
                f"{'Thành Tiền':<15}"
            )

            total_quantity = 0
            total_price = 0

            for index, product in enumerate(cart_items, start=1):

                product_id = product[0]
                product_name = product[1]
                quantity = product[2]
                unit_price = product[3]

                thanh_tien = quantity * unit_price

                total_quantity += quantity
                total_price += thanh_tien

                print(
                    f"{index:<5}"
                    f"{product_id:<10}"
                    f"{product_name:<30}"
                    f"{quantity:<10}"
                    f"{unit_price:<15,}"
                    f"{thanh_tien:<15,}"
                )

            print("-" * 90)
            print(f"Tổng số lượng sản phẩm: {total_quantity}")
            print(f"TỔNG TIỀN THANH TOÁN: {total_price:,} VND")

        case 2:
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            product_name = input("Nhập tên sản phẩm: ").strip()

            if product_name == "":
                print("Tên sản phẩm không được để trống!")
                continue

            quantity = input("Nhập số lượng: ").strip()
            unit_price = input("Nhập đơn giá: ").strip()

            if not quantity.isdigit() or not unit_price.isdigit():
                print("Vui lòng nhập đúng định dạng số!")
                continue

            quantity = int(quantity)
            unit_price = int(unit_price)

            if quantity <= 0 or unit_price < 0:
                print("Số lượng hoặc đơn giá không hợp lệ!")
                continue

            found = False

            for product in cart_items:
                if product[0].upper() == product_id:
                    product[2] += quantity

                    found = True

                    print("Đã cộng dồn số lượng sản phẩm!")
                    break

            if not found:
                cart_items.append([
                    product_id,
                    product_name,
                    quantity,
                    unit_price
                ])

                print("Đã thêm sản phẩm mới!")

        case 3:
            product_id = input(
                "Nhập mã sản phẩm cần cập nhật: "
            ).strip().upper()

            found = False

            for product in cart_items:
                if product[0].upper() == product_id:
                    found = True

                    new_quantity = input(
                        "Nhập số lượng mới: "
                    ).strip()

                    if not new_quantity.isdigit():
                        print("Vui lòng nhập số hợp lệ!")
                        break

                    new_quantity = int(new_quantity)
                    if new_quantity <= 0:
                        print("Số lượng phải lớn hơn 0!")
                        break

                    product[2] = new_quantity

                    print("Cập nhật số lượng thành công!")

                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case 4:
            product_id = input(
                "Nhập mã sản phẩm cần xóa: "
            ).strip().upper()

            found = False

            for product in cart_items:
                if product[0].upper() == product_id:
                    cart_items.remove(product)

                    found = True

                    print("Đã xóa sản phẩm khỏi giỏ hàng!")

                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case 5:
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break