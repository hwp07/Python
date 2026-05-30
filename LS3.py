product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
""")

    choice = input("Nhập lựa chọn: ").strip()

    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("-" * 80)
                print(
                    f"{'STT':<5}"
                    f"{'MÃ SP':<10}"
                    f"{'TÊN SẢN PHẨM':<25}"
                    f"{'GIÁ':<15}"
                    f"{'SỐ LƯỢNG'}"
                )
                print("-" * 80)

                for index, product in enumerate(product_list, start=1):
                    print(
                        f"{index:<5}"
                        f"{product['product_id']:<10}"
                        f"{product['product_name']:<25}"
                        f"{product['price']:<15,}"
                        f"{product['quantity']}"
                    )

                print("-" * 80)

        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()

            is_duplicate = False

            for product in product_list:
                if product["product_id"] == product_id:
                    is_duplicate = True
                    break

            if is_duplicate:
                print("Mã sản phẩm bị trùng")
                continue

            product_name = input("Nhập tên sản phẩm: ").strip()

            price = input( "Nhập giá sản phẩm: ").strip()

            quantity = input("Nhập số lượng sản phẩm: ").strip()

            if (
                not price.isdigit()
                or int(price) <= 0
                or not quantity.isdigit()
                or int(quantity) <= 0
            ):
                print("Giá/Số lượng không hợp lệ")
                continue

            new_product = {
                "product_id": product_id,
                "product_name": product_name,
                "price": int(price),
                "quantity": int(quantity)
            }

            product_list.append(new_product)

            print("Thêm sản phẩm thành công")

        case "3":
            product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

            product_found = None

            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break

            if product_found is None:
                print("Không tìm thấy mã sản phẩm cần cập nhật!")
                continue

            product_name = input("Nhập tên sản phẩm mới: ").strip()

            price = input("Nhập giá sản phẩm mới: ").strip()

            quantity = input("Nhập số lượng mới: ").strip()

            if (
                not price.isdigit()
                or int(price) <= 0
                or not quantity.isdigit()
                or int(quantity) <= 0
            ):
                print("Giá/Số lượng không hợp lệ")
                continue

            product_found["product_name"] = product_name
            product_found["price"] = int(price)
            product_found["quantity"] = int(quantity)

            print("Cập nhật sản phẩm thành công")

        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

            product_found = None

            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break

            if product_found is None:
                print("Không tìm thấy mã sản phẩm cần xoá!")
                continue

            product_list.remove(product_found)

            print("Xóa sản phẩm thành công")

        case "5":
            print("Thoát chương trình.")
            break

        case _:
            print(
                "Lựa chọn không hợp lệ, vui lòng nhập lại!"
            )