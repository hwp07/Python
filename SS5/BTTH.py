quantity = int(input("Nhập số lượng nhân viên: "))

for i in range(quantity):
    print()
    name = input("Nhập tên nhân viên: ")
    day = int(input("Nhập số ngày làm: "))
    if day < 0 or day > 22:
        print("Dữ liệu không hợp lệ")
        continue
    if day == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
        continue
    print(name + ": ", end="")
    for row in range(1):
        for col in range(day):
            print("*", end="")
    print()
    if day >= 18:
        print("Làm việc chăm chỉ")

    elif day < 10:
        print("Làm việc ít")

    else:
        print("Làm việc bình thường")