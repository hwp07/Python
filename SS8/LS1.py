account_name = ""
title = ""
description = ""
hashtags = ""

while True:
    print("""
+===================================================+
|        HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK           |
+===================================================+
|  1. Nhập và phân tích thông tin video             |
|  2. Chuẩn hóa tên tài khoản                       |
|  3. Kiểm tra tính hợp lệ của hashtag              |
|  4. Tìm kiếm và thay thế từ khóa trong mô tả      |
|  5. Thoát chương trình                            |
+===================================================+
""")

    choice = input("> Mời bạn chọn chức năng (1-5): ")

    if not choice.isdigit():
        print("Vui lòng nhập số.")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Chỉ được nhập từ 1 đến 5.")
        continue

    match choice:
        case 1:

            print("\n--- NHẬP THÔNG TIN VIDEO ---")

            account_name = input("Tên tài khoản: ").strip()

            if account_name == "":
                print(" Tên tài khoản không được rỗng.")
                continue

            title = input("Tiêu đề video: ").strip()

            description = input("Mô tả video: ").strip()

            if description == "":
                print(" Mô tả không được rỗng.")
                continue

            hashtags = input("Nhập hashtag: ").strip()

            print("\n--- KẾT QUẢ ---")
            print("Tên tài khoản:", account_name)
            print("Tiêu đề:", title.title())
            print("Mô tả:", description)
            print("Số ký tự:", len(description))
            print("Số từ:", len(description.split()))
            print("Hashtag:", hashtags)
            print("Chữ thường:", description.lower())
            print("Chữ hoa:", description.upper())

        case 2:
            print("\n--- CHUẨN HÓA TÀI KHOẢN ---")

            acc = input("Nhập tài khoản: ").strip()

            if acc == "":
                print(" Tài khoản không được rỗng.")
                continue

            acc = acc.lower()

            if not acc.startswith("@"):
                acc = "@" + acc

            print("Tài khoản sau chuẩn hóa:", acc)

        case 3:
            print("\n--- KIỂM TRA HASHTAG ---")

            hashtag = input("Nhập hashtag: ").strip()

            if hashtag == "":
                print(" Hashtag không được rỗng.")

            elif not hashtag.startswith("#"):
                print(" Hashtag phải bắt đầu bằng #")

            elif " " in hashtag:
                print(" Hashtag không được chứa khoảng trắng.")

            elif len(hashtag) < 2:
                print(" Hashtag không hợp lệ.")

            else:
                hop_le = True

                for char in hashtag[1:]:

                    if not (char.isalnum() or char == "_"):
                        hop_le = False
                        break

                if hop_le:
                    print(" Hashtag hợp lệ.")

                else:
                    print(" Hashtag chứa ký tự không hợp lệ.")

        case 4:
            print("\n--- TÌM KIẾM VÀ THAY THẾ ---")

            if description == "":
                print(" Chưa có mô tả video.")
                continue

            old = input("Từ cần tìm: ")
            new = input("Từ thay thế: ")

            if old in description:

                count = description.count(old)

                description = description.replace(old, new)

                print("\nMô tả mới:")
                print(description)

                print("Số lần thay thế:", count)

            else:
                print(" Không tìm thấy từ khóa.")

        case 5:
            print("\nThoát chương trình!")
            break