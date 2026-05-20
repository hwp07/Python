# input: cần ép kiểu về int
# output:
#    Neu nhap sai: in thong bao loi va tiep tuc yeu cau nhap.
#    Neu nhap dung so nguyen duong: in "Ghi nhan thanh cong".

# giải pháp

# | tiêu chí       | while True + break          | while với biến điều kiện     |
# | độ ngắn gọn    | ngắn gọn hơn                | dài hơn                      |
# | mức độ dễ hiểu | gần với ý tưởng: lặp vô hạn | dễ theo dõi nhưng nhiều biến |

# => giải pháp 1: while True + brreak

while True:
    quantity = int(input("Vui lòng nhập số lượng nhân sự mới: "))

    if(quantity) <= 0 :
        print("Lỗi: Số lượng nhân sự phải lớn hơn 0. Vui lòng nhập lại!")
    else :
        print("Ghi nhận thành công!")
        break