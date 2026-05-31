product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm
2. Bán sản phẩm cho khách hàng
3. Xử lý đổi trả sản phẩm
4. Áp dụng giảm giá cho sản phẩm
5. Nhập thêm hàng vào kho cửa hàng
6. Thoát chương trình
""")

    choice = input("Nhập lựa chọn: ").strip()

    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("-" * 110)
                print(
                    f"{'STT':<5}"
                    f"{'MÃ SP':<10}"
                    f"{'TÊN SẢN PHẨM':<25}"
                    f"{'GIÁ BÁN':<15}"
                    f"{'TỒN KHO':<10}"
                    f"{'ĐÃ BÁN':<10}"
                    f"{'ĐỔI TRẢ':<10}"
                    f"{'GIẢM GIÁ':<10}"
                    f"{'TRẠNG THÁI'}"
                )
                print("-" * 110)

                for index, product in enumerate(product_list, start=1):
                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"

                    print(
                        f"{index:<5}"
                        f"{product['product_id']:<10}"
                        f"{product['product_name']:<25}"
                        f"{product['price']:<15,}"
                        f"{product['quantity']:<10}"
                        f"{product['sold']:<10}"
                        f"{product['returned']:<10}"
                        f"{str(product['discount']) + '%':<10}"
                        f"{status}"
                    )

                print("-" * 110)

        case "2":
            product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
            product = None

            for item in product_list:
                if item["product_id"] == product_id:
                    product = item
                    break

            if product is None:
                print("Không tìm thấy sản phẩm cần bán")
                continue

            quantity = input("Nhập số lượng khách mua: ").strip()

            if not quantity.isdigit():
                print("Số lượng mua không hợp lệ")
                continue

            quantity = int(quantity)

            if quantity <= 0:
                print("Số lượng mua không hợp lệ")
                continue

            if quantity > product["quantity"]:
                print("Số lượng trong kho không đủ để bán")
                continue

            final_price = product["price"] * (100 - product["discount"]) / 100

            total = final_price * quantity

            product["quantity"] -= quantity
            product["sold"] += quantity

            print(f"Tổng tiền khách cần thanh toán: {int(total)} VNĐ")

        case "3":
            product_id = input("Nhập mã sản phẩm khách muốn đổi/trả: ").strip().upper()

            product = None

            for item in product_list:
                if item["product_id"] == product_id:
                    product = item
                    break

            if product is None:
                print("Không tìm thấy sản phẩm cần đổi trả")
                continue

            quantity = input("Nhập số lượng đổi/trả: ").strip()

            if not quantity.isdigit():
                print("Số lượng đổi/trả không hợp lệ")
                continue

            quantity = int(quantity)

            if quantity <= 0:
                print("Số lượng đổi/trả không hợp lệ")
                continue

            if quantity > product["sold"]:
                print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
                continue

            product["sold"] -= quantity
            product["quantity"] += quantity
            product["returned"] += quantity

            refund_price = product["price"] * (100 - product["discount"]) / 100

            refund_total = refund_price * quantity

            print(f"Số tiền hoàn lại: {int(refund_total)} VNĐ")

        case "4":
            product_id = input("Nhập mã sản phẩm cần áp dụng giảm giá: ").strip().upper()

            product = None

            for item in product_list:
                if item["product_id"] == product_id:
                    product = item
                    break

            if product is None:
                print("Không tìm thấy sản phẩm")
                continue

            discount = input("Nhập phần trăm giảm giá: ").strip()

            if not discount.isdigit():
                print("Phần trăm giảm giá không hợp lệ")
                continue

            discount = int(discount)

            if discount < 0 or discount > 70:
                print("Phần trăm giảm giá không hợp lệ")
                continue

            product["discount"] = discount

            print("Áp dụng giảm giá thành công")

        case "5":
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()

            product = None

            for item in product_list:
                if item["product_id"] == product_id:
                    product = item
                    break

            if product is None:
                print("Không tìm thấy sản phẩm")
                continue

            quantity = input("Nhập số lượng nhập thêm: ").strip()

            if not quantity.isdigit():
                print("Số lượng nhập thêm không hợp lệ")
                continue

            quantity = int(quantity)

            if quantity <= 0:
                print("Số lượng nhập thêm không hợp lệ")
                continue

            product["quantity"] += quantity

            print("Nhập hàng thành công")

        case "6":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")