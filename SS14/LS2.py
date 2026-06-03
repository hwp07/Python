# 1. biến total_points là biến global
#
# 2. vì total_points đang thực hiện phép gán nên python tự động hiểu rằng total_points đang là biến cục bộ dẫn đến phát sinh lỗi
#
# 3. chương trình sẽ không bị lỗi, vì hàm chỉ đọc giá trị, không có phép gán,=> python sẽ tìm lên phạm vi global và sử dụng biến toàn cục
#
# 4. sử dụng từ khóa global
def add_reward_points(points_earned):
    global total_points
    total_points = total_points + points_earned

# 5. sử dụng từ khóa return, clean code hơn
def add_reward_points(current_points, points_earned):
    return current_points + points_earned


# code hoàn chỉnh

# tổng điểm hiện tại của khách hàng
total_points = 100

# hàm cộng điểm thưởng
def add_reward_points(current_points, points_earned):
    print("Đã cộng thêm", points_earned, "điểm.")
    return current_points + points_earned

# khách mua hàng được thưởng 50 điểm
total_points = add_reward_points(total_points, 50)

# in kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)