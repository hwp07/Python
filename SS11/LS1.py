# 1. tuple product_info ban đầu có 4 phần tử
# 2. phần tử "SP001" nằm ở index 0
# 3. dòng `product_code = product_info[1]` lấy sai mã sản phẩm vì index 1 chứa giá trị "Áo polo nam", không phải "SP001"
# 4. phần tử "Áo polo nam" nằm ở index 1
# 5. dòng `product_name = product_info[2]` lấy sai tên sản phẩm vì index 2 chứa giá trị "Size L", không phải "Áo polo nam"
# 6. dòng `product_length = product_info.length()` gây lỗi vì tuple không có phương thức `length()`
# 7. để đếm số phần tử trong tuple cần sử dụng hàm `len()`
# 8. dòng `product_info[3] = 279000` không hợp lệ vì tuple là kiểu dữ liệu immutable (không thể thay đổi phần tử sau khi được tạo)
# 9. tuple không cho phép sửa trực tiếp phần tử
# 10. muốn cập nhật giá bán từ 299000 thành 279000 cần tạo một tuple mới với giá trị giá bán đã được thay đổi

product_info = ("SP001", "Áo polo nam", "Size L", 299000)

product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)

product_info = (
    product_info[0],
    product_info[1],
    product_info[2],
    279000
)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)