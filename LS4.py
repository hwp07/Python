product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("""
===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
2. Bán sản phẩm cho khách hàng
3. Nhập thêm hàng vào kho
4. Xem báo cáo doanh thu
5. Thoát chương trình
""")

    choice = input("Nhập lựa chọn: ").strip()

    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("-" * 100)
                print(f"{'STT':<5}{'MÃ SP':<10}{'TÊN SẢN PHẨM':<25}{'GIÁ':<15}{'TỒN':<10}{'ĐÃ BÁN':<10}{'TRẠNG THÁI'}")
                print("-" * 100)

                for index, product in enumerate(product_list, start=1):
                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"

                    print(f"{index:<5}{product['product_id']:<10}{product['product_name']:<25}{product['price']:<15,}{product['quantity']:<10}{product['sold']:<10}{status}")

                print("-" * 100)

        case "2":
            product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()

            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break

            if product_found is None:
                print("Không tìm thấy sản phẩm cần bán")
                continue

            quantity = input("Nhập số lượng khách mua: ").strip()

            if not quantity.isdigit() or int(quantity) <= 0:
                print("Số lượng mua không hợp lệ")
                continue

            quantity = int(quantity)

            if quantity > product_found["quantity"]:
                print("Số lượng trong kho không đủ để bán")
                continue

            product_found["quantity"] -= quantity
            product_found["sold"] += quantity

            total = quantity * product_found["price"]

            print(f"Tổng tiền khách cần thanh toán: {total:,} VNĐ")

        case "3":
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()

            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break

            if product_found is None:
                print("Không tìm thấy sản phẩm cần nhập kho")
                continue

            quantity = input("Nhập số lượng nhập thêm: ").strip()

            if not quantity.isdigit() or int(quantity) <= 0:
                print("Số lượng nhập kho không hợp lệ")
                continue

            quantity = int(quantity)

            product_found["quantity"] += quantity

            print("Nhập kho thành công")

        case "4":
            total_revenue = 0
            best_seller = None
            max_sold = 0

            for product in product_list:
                total_revenue += product["price"] * product["sold"]

            if total_revenue == 0:
                print("Chưa có doanh thu phát sinh.")
                continue

            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")

            for index, product in enumerate(product_list, start=1):
                revenue = product["price"] * product["sold"]

                print(f"{index}. {product['product_name']} | Đã bán: {product['sold']} | Doanh thu: {revenue:,}")

                if product["sold"] > max_sold:
                    max_sold = product["sold"]
                    best_seller = product["product_name"]

            print(f"\nTổng doanh thu: {total_revenue:,}")
            print(f"Sản phẩm bán chạy nhất: {best_seller}")

        case "5":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")