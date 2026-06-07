from functools import reduce

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


def show_labels():
    print("\n--- DANH SÁCH TEM NHÃN ---")

    template = "Mã: {code} | Tên: {name:<20} | Giá: {price} VND | Rating: {rating}*"

    for product in product_list:
        try:
            data = product.split("-")

            code = data[0]
            name = data[1]
            price = int(data[2])
            rating = data[3]

            info = {
                "code": f"{code:<10}",
                "name": name,
                "price": f"{price:,}",
                "rating": rating
            }

            print(template.format_map(info))

        except IndexError:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Bỏ qua sản phẩm {data[0]} do dữ liệu giá không hợp lệ")


def sort_products():
    print("\n--- SẮP XẾP SẢN PHẨM ---")

    valid_products = []

    for product in product_list:
        try:
            data = product.split("-")

            if len(data) < 4:
                raise IndexError

            int(data[2])
            float(data[3])

            valid_products.append(product)

        except IndexError:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Bỏ qua sản phẩm {data[0]} do dữ liệu không hợp lệ")

    valid_products.sort(
        key=lambda item: (
            -float(item.split("-")[3]),
            int(item.split("-")[2])
        )
    )

    for index, product in enumerate(valid_products, start=1):
        print(f"{index}. {product}")


def calculate_total():
    print("\n--- TỔNG GIÁ TRỊ KHO ---")

    prices = []

    for product in product_list:
        try:
            data = product.split("-")

            if len(data) < 4:
                raise IndexError

            price = int(data[2])

            prices.append(price)

        except IndexError:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Bỏ qua sản phẩm {data[0]} do dữ liệu giá không hợp lệ")

    if not prices:
        print("Không có dữ liệu hợp lệ")
        return

    total = reduce(lambda x, y: x + y, prices)

    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND")



while True:
    print("\n============= E-COMMERCE ANALYTICS =============")
    print("1. Hiển thị tem nhãn sản phẩm")
    print("2. Sắp xếp sản phẩm thông minh")
    print("3. Tính tổng giá trị kho hàng")
    print("4. Đóng hệ thống")
    print("================================================")

    choice = input("Chọn chức năng (1-4): ")

    match choice:
        case "1":
            show_labels()

        case "2":
            sort_products()

        case "3":
            calculate_total()

        case "4":
            print("Đóng hệ thống...")
            break

        case _:
            print("Lựa chọn không hợp lệ")

