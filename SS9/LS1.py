# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000") # danh sách thay đổi thành ['GE000', 'GE001', 'GE002', 'GE003-CANCEL']

# Sửa mã đơn hàng GE002 thành GE002-UPDATED
delivery_orders[1] = "GE002-UPDATED" # sau khi chèn "GE000" vào đầu danh sách, các phần tử phía sau bị dời vị trí, dòng code sửa "GE001" chứ không phải "GE002"

# Xóa đơn hàng bị khách hủy
delivery_orders.remove("GE003-CANCEL") # trong danh sách không tồn tại giá trị 3 nên cần sửa vì remove xóa phần tử theo giá trị

# Lấy đơn hàng cuối cùng ra để bàn giao cho tài xế khác
transferred_order = delivery_orders.pop()
#pop() dùng để:
# xóa phần tử khỏi danh sách
# đồng thời trả về phần tử vừa bị xóa

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order) # biến transferred_order chưa được khởi tạo nên cần khởi tạo

