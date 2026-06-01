cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]

while True:
    print("=" * 55)
    print("             SHOPEE CART MANAGEMENT SYSTEM")
    print("=" * 55)
    print("""
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của 1 sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
""")
    print("=" * 55)

    choice = input("Mời bạn chọn chức năng (1-5): ")

    match choice:
        case "1":
            if not cart_items:
                print("Giỏ hàng hiện đang trống!")
            else:
                print("     CHI TIẾT GIỎ HÀNG")
                print(
                    f"{'| STT':<5} | "
                    f"{'MÃ SP':<10} | "
                    f"{'TÊN SẢN PHẨM':<25} | "
                    f"{'SL':<5} | "
                    f"{'ĐƠN GIÁ':<15} | "
                    f"{'THÀNH TIỀN':<15} | "
                )
                print("-" * 95)

                total = 0

                for index, items in enumerate(cart_items, start=1):
                    sum = items["price"] * items["number"]
                    total += sum

                    print(
                        f"| {index:<5} | "
                        f"{items['id']:<10} | "
                        f"{items['name']:<25} | "
                        f"{items['number']:<5} | "
                        f"{items['price']:<15,} | "
                        f"{sum:<15,} | "
                    )

                print("-" * 95)
                print(f"TỔNG TIỀN: {total:,} VND")

