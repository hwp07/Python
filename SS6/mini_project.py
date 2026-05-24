laptop = 0
phone = 0
tablet = 0

while True:
    print("\n   MENU QUẢN LÝ TỒN KHO")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo tồn kho thấp")
    print("5. Thoát")

    choice = input("Nhập lựa chọn của bạn: ")

    match choice:

        case "1":
            print("\n   BÁO CÁO TỒN KHO")
            print(f"Laptop: {laptop}")
            print(f"Phone: {phone}")
            print(f"Tablet: {tablet}")

            print("\n   BIỂU ĐỒ TỒN KHO")

            print(f"Laptop ({laptop}): ", end="")
            for i in range(laptop):
                print("*", end="")
            print()

            print(f"Phone ({phone}): ", end="")
            for i in range(phone):
                print("*", end="")
            print()

            print(f"Tablet ({tablet}): ", end="")
            for i in range(tablet):
                print("*", end="")
            print()


        case "2":

            print("\n   NHẬP KHO")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")

            product = input("Chọn mặt hàng: ")

            while True:
                quantity = int(input("Nhập số lượng cần thêm: "))

                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue
                else:
                    break

            match product:

                case "1":
                    laptop += quantity
                    print("Nhập kho Laptop thành công!")

                case "2":
                    phone += quantity
                    print("Nhập kho Phone thành công!")

                case "3":
                    tablet += quantity
                    print("Nhập kho Tablet thành công!")

                case _:
                    print("Mặt hàng không hợp lệ!")

        case "3":

            print("\n   XUẤT KHO")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")

            product = input("Chọn mặt hàng: ")

            while True:
                quantity = int(input("Nhập số lượng cần xuất: "))

                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue
                else:
                    break

            match product:
                case "1":
                    if quantity > laptop:
                        print("Không đủ hàng!")
                    else:
                        laptop -= quantity
                        print("Xuất kho Laptop thành công!")

                case "2":
                    if quantity > phone:
                        print("Không đủ hàng!")
                    else:
                        phone -= quantity
                        print("Xuất kho Phone thành công!")

                case "3":
                    if quantity > tablet:
                        print("Không đủ hàng!")
                    else:
                        tablet -= quantity
                        print("Xuất kho Tablet thành công!")

                case _:
                    print("Mặt hàng không hợp lệ!")

        case "4":
            print("\n   CẢNH BÁO TỒN KHO")

            if laptop < 10:
                print(f"[CẢNH BÁO] Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")

            if phone < 10:
                print(f"[CẢNH BÁO] Phone sắp hết (Chỉ còn {phone} sản phẩm)")

            if tablet < 10:
                print(f"[CẢNH BÁO] Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")

        case "5":
            print("Đã thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ! Vui lòng nhập lại.")