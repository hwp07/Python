# tìm số lẻ đầu tiên từ 10, 1
for i in range(10,0,-1):
    if (i % 2 != 0):
        print(i)
        break

# in ra số chẵn 1 -> 100, sử dụng continue
for number in range(1,101,1):
    if number % 2 != 0:
        continue
    print(number)

for i in range(1,2,1):
    for j in range(0,60):
        print(f'{i}:{j}')

