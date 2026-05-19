# tuổi lớn hơn 18, tiền lớn hơn 10m
# in ra là True còn lâij in ra false

age = 18
money = 10

if age >= 18 and money >= 10:
    print('True')
else:
    print('False')



# điểm từ 8 - 10 là xuất sắc
# điểm từ 6 - 8 là vừa vừa
# còn lại cần nỗ lực

diem = int(input('Nhập điểm của bạn: '))

if diem >= 8 and diem <= 10:
    print('Sinh viên cưng của thầy!')

elif diem <= 8 and diem >= 6:
    print('Sinh viên vừa vừa')
else:
    print('Sinh viên ngu')

