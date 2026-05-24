# input: id(str) ,name(str), department(str)
# output: thông báo lỗi và thông tin nhan viện hợp lệ

# giải pháp: sử dụng điều kiện if để kiểm tra dữ liệu tên và mã nhân viên

# thuật toán
# - sử dụng vòng lặp for ... in range(3)
# - input thông tin
# - check thông tin:
#     + hợp lệ => in phiếu
#     + không hợp lệ => báo lỗi và không in phiếu

for i in range(3):
    id = input('Mã nhân viên: ')
    name = input('Họ và tên nhân viên: ')
    department = input('Phòng ban công tác: ')

    if id.strip() == '' or name.strip() == '':
        print('\n[CẢNH BÁO] Dữ liệu tên hoặc mã khôgn hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.\n')
        continue

    print('\n   Phiếu Hồ sơ Điện tử')
    print(f'Mã nhân viên        : {id}')
    print(f'Họ và tên nhân viên : {name}')
    print(f'Phòng ban công tác  : {department}\n')

