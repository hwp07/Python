# 1. insert()
# express_orders.insert(0, "GE100-FAST")
# sau khi chèn:
# ['GE100-FAST', 'GE101', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']
# => Các phần tử cũ bị đẩy sang phải 1 vị trí

# 2. sửa sai đơn hàng
# express_orders[1] = "GE102-UPDATED"
# sai vì:
# index 1 -> GE101
# index 2 -> GE102-WRONG
# => Phải sửa index 2
# đúng:
# express_orders[2] = "GE102-UPDATED"

# 3. xóa sai đơn hàng
# express_orders.pop(3)
# pop() xóa theo vị trí
# nên dùng:
# express_orders.remove("GE103-CANCEL")
# => remove() xóa theo giá trị

# 4. lấy sai đơn đang giao
# current_order = express_orders.pop()
# pop() mặc định lấy phần tử cuối → lấy "GE104"
# muốn lấy đơn đầu tiên:
# current_order = express_orders.pop(0)


# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)

