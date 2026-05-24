# input/output
# input: room_count(int), rows(int), seats(int)
# output: sơ đồ phòng học bằng dấu *, các thông báo lỗi

# giải pháp:
# 1. nhập số lượng phòng -> kiểm tra điều kiện
# 2. duyệt từng phòng học
# 3. nhập dữ liệu và kiểm tra
# 4. in sơ 


room_count = int(input("Nhập số lượng phòng học: "))
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")

else:
    for room in range(1, room_count + 1):
        print(f"\n===== Phòng học {room} =====")

        rows = int(input("Nhập số hàng ghế: "))
        seats = int(input("Nhập số ghế mỗi hàng: "))

        if rows <= 0 or seats <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if rows > 10 or seats > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        print("\nSơ đồ chỗ ngồi:")

        for row in range(rows):
            for seat in range(seats):
                print("*", end="")
            print()