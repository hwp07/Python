shop_name = ""
product_name = ""
description = ""
category = ""
keywords = ""

while True:

    print("""
+===================================================+
|        HỆ THỐNG QUẢN LÝ NỘI DUNG SHOPEE           |
+===================================================+
|  1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê |
|  2. Chuẩn hóa tên shop                            |
|  3. Kiểm tra mã giảm giá hợp lệ                  |
|  4. Tìm kiếm và thay thế từ khóa trong mô tả      |
|  5. Thoát chương trình                            |
+===================================================+
""")

    choice = input("> Mời bạn chọn chức năng (1-5): ")

    if not choice.isdigit():
        print(" Lựa chọn không hợp lệ.")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print(" Vui lòng chọn từ 1 đến 5.")
        continue

    match choice:
        case 1:
            print("\n*** NHẬP DỮ LIỆU SẢN PHẨM ***")

            shop_name = input("Tên shop: ").strip()

            if shop_name == "":
                print(" Tên shop không được bỏ trống.")
                continue

            product_name = input("Tên sản phẩm: ").strip()
            description = input("Mô tả sản phẩm: ").strip()

            if description == "":
                print(" Mô tả sản phẩm không được rỗng.")
                continue

            category = input("Danh mục sản phẩm: ").strip()
            keywords = input("Danh sách từ khóa: ").strip()

            category = " ".join(category.split()).lower()

            keywords = keywords.strip()

            count_keywords = 0

            for word in keywords.split(","):
                if word.strip() != "":
                    count_keywords += 1

            print("\n========== KẾT QUẢ ==========")
            print("Tên shop:", shop_name)
            print("Tên sản phẩm:", product_name.title())
            print("Mô tả sản phẩm:", description)
            print("Độ dài mô tả:", len(description))
            print("Danh mục:", category)
            print("Danh sách từ khóa:", keywords)
            print("Số lượng từ khóa:", count_keywords)
            print("Mô tả chữ thường:", description.lower())
            print("Mô tả chữ hoa:", description.upper())

        case 2:
            print("\n*** CHUẨN HÓA TÊN SHOP ***")

            raw_shop = input("Nhập tên shop: ")

            if raw_shop.strip() == "":
                print(" Tên shop không được bỏ trống.")
                continue

            new_shop = raw_shop.strip().lower()
            new_shop = "-".join(new_shop.split())

            if not new_shop.startswith("shop-"):
                new_shop = "shop-" + new_shop

            print("Tên shop ban đầu:", raw_shop)
            print("Tên shop sau chuẩn hóa:", new_shop)

            shop_name = new_shop

        case 3:
            print("\n*** KIỂM TRA MÃ GIẢM GIÁ ***")

            code = input("Nhập mã giảm giá: ").strip()

            if code == "":
                print(" Mã giảm giá không được rỗng.")

            elif " " in code:
                print(" Mã giảm giá không được chứa khoảng trắng.")

            elif len(code) < 6 or len(code) > 12:
                print(" Mã giảm giá phải từ 6-12 ký tự.")

            elif not code.isupper():
                print(" Mã giảm giá phải viết hoa toàn bộ.")

            elif not code.isalnum():
                print(" Mã giảm giá chỉ được chứa chữ và số.")

            elif not code.startswith("SALE"):
                print(" Mã giảm giá phải bắt đầu bằng SALE.")

            else:
                print("✅ Mã giảm giá hợp lệ.")

        case 4:
            print("\n*** TÌM KIẾM VÀ THAY THẾ ***")

            if description == "":
                print(" Chưa có mô tả sản phẩm.")
                continue

            old = input("Từ khóa cần tìm: ")
            new = input("Từ khóa thay thế: ")

            if old in description:

                count = description.count(old)

                description = description.replace(old, new)

                print("\nSố lần xuất hiện:", count)
                print("Mô tả sau khi thay thế:")
                print(description)

            else:
                print(" Không tìm thấy từ khóa.")

        case 5:
            print("\nThoát chương trình.")
            break