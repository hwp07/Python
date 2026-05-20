choice = ''
while True:
    quantity = int(input('Nhập số lượng nhân viên: '))

    for i in range(1, quantity + 1, 1):
        print(f'\nNhân viên {i}')
        name = input('Nhập tên: ')
        day = int(input('Số ngày đi làm: '))

        print('Thông tin nhân viên:\n')
        print(f'Tên: {name}')
        print(f'Số ngày đi làm: {day}')

        if day > 20:
            print('Nhân viên chuyên cần tốt\n')
        else :
            print('Cần cải thiện chuyên cần\n')


    choice = input('Tiếp tục chương trình (y/n)')
    if choice == 'n':
        print('Chương trình kết thúc')
        break
