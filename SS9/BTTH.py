branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] #(Đơn vị: VND)
target_achieved = [True, True, False, True, False] #(True là Đạt chỉ tiêu, False là Không đạt)

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
""")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if not choice.isdigit():
        print("[Lỗi] Vui lòng nhập số từ 1 đến 4!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            print(f"\n{'Tên cơ sở':<30} | {'Doanh thu':<15} | {'Trạng thái':<20}")
            print("-" * 62)

            for i in range(len(branch_names)):
                if target_achieved[i] == True:
                    status = "Đạt"
                else :
                    status = "Không đạt"

                print(f"{branch_names[i] :<30} | {daily_revenues[i] :<15} | {status :<20}")

            total = 0
            total = sum(daily_revenues)

            print("-" * 62)

            print("=> TỔNG DOANH THU TOÀN VÙNG: ", total, " VND")

        case 2:
            print("\n--- THỐNG KÊ CƠ SỞ NỔI BẬT ---")

            max_revenue = daily_revenues[0]
            min_revenue = daily_revenues[0]

            max_branch = branch_names[0]
            min_branch = branch_names[0]

            for i in range(len(daily_revenues)):
                if daily_revenues[i] > max_revenue:
                    max_revenue = daily_revenues[i]
                    max_branch = branch_names[i]

                if daily_revenues[i] < min_revenue:
                    min_revenue = daily_revenues[i]
                    min_branch = branch_names[i]

            print(f"Cơ sở doanh thu CAO NHẤT: {max_branch} ({max_revenue} VND)")
            print(f"Cơ sở doanh thu THẤP NHẤT: {min_branch} ({min_revenue} VND)")
                
        case 3:
            print("\n--- DANH SÁCH CƠ SỞ CẦN HỖ TRỢ TRA CỨU ĐƯỢC ---")

            failed_branches = []

            for i in range(len(branch_names)):
                if target_achieved[i] == False:
                    failed_branches.append(branch_names[i])

            print(failed_branches)

        case 4:
            print("\n Thoát chương trình!")
            break

        case _:
            print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")