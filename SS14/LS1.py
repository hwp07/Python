# 1.
# - giá trị 15000 đang được gán cho discount
# - giá trị 0.1 đang được gán cho shipping_fee
#
# 2. do gán nhầm giá trị nên 15000 bị hiểu nhầm là discount thay vì shipping_fee => dẫn đến kết quả sai lệch, số âm rất lớn
#
# 3. order_total đang mang giá trị none => không thể cộng => TypeError
#
# 4. hiện tại order_total đang mang giá trị none do hàm chỉ trả về print mà không return gì
#
# 5.
# - print(): chỉ in kết quả ra màn hình
# - return: trả về kết quả của hàm
#
# 6 sửa code

# hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total


# đơn hàng mua áo thun
order_total = calculate_final_price(100000, 0.1, 15000)

# cộng thêm phí đóng gói
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)