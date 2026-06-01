saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": "50000000",
        "term_months": "6",
        "interest_rate": "6.5",
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": "120000000",
        "term_months": "12",
        "interest_rate": "7.2",
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Chọn chức năng: ").strip()

    match choice:

        case "1":
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")
                stt = 1

                for account in saving_accounts:
                    print(
                        f"{stt}. Mã sổ: {account['account_id']} | "
                        f"Khách hàng: {account['customer_name']} | "
                        f"Số tiền gửi: {account['balance']} | "
                        f"Kỳ hạn: {account['term_months']} tháng | "
                        f"Lãi suất: {account['interest_rate']}%/năm | "
                        f"Trạng thái: {account['status']}"
                    )
                    stt += 1

        case "2":
            account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()

            exist = False

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    exist = True
                    break

            if exist:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            customer_name = input("Nhập tên khách hàng: ").strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            balance = input("Nhập số tiền gửi: ").strip()
            term_months = input("Nhập kỳ hạn gửi theo tháng: ").strip()

            if (not balance.isdigit() or int(balance) <= 0 or not term_months.isdigit() or int(term_months) <= 0):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            interest_rate = input("Nhập lãi suất năm: ").strip()

            if (not interest_rate.replace(".", "", 1).isdigit() or float(interest_rate) <= 0):
                print("Lãi suất không hợp lệ!")
                continue

            saving_accounts.append(
                {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": balance,
                    "term_months": term_months,
                    "interest_rate": interest_rate,
                    "status": "active"
                }
            )

            print("Mở sổ tiết kiệm thành công!")

        case "3":
            account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

            found = False

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = True

                    if account["status"] == "closed":
                        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break

                    customer_name = input("Nhập tên khách hàng mới: ").strip()

                    if customer_name == "":
                        print("Tên khách hàng không được để trống")
                        break

                    balance = input("Nhập số tiền gửi mới: ").strip()

                    term_months = input("Nhập kỳ hạn mới theo tháng: ").strip()

                    if (not balance.isdigit() or int(balance) <= 0 or not term_months.isdigit() or int(term_months) <= 0):
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        break

                    interest_rate = input("Nhập lãi suất năm mới: ").strip()

                    if (not interest_rate.replace(".", "", 1).isdigit() or float(interest_rate) <= 0):
                        print("Lãi suất không hợp lệ!")
                        break

                    account["customer_name"] = customer_name
                    account["balance"] = balance
                    account["term_months"] = term_months
                    account["interest_rate"] = interest_rate

                    print("Cập nhật thành công!")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")

        case "4":
            account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()

            found = False

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = True
                    account["status"] = "closed"
                    print("Tất toán sổ tiết kiệm thành công!")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "5":
            account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

            found = False

            for account in saving_accounts:

                if account["account_id"] == account_id:
                    found = True

                    if account["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break

                    interest = (int(account["balance"]) * float(account["interest_rate"]) / 100 * int(account["term_months"]) / 12)

                    total = int(account["balance"]) + interest

                    print(f"Tiền lãi dự kiến: {interest:,.0f} VNĐ")
                    print(f"Tổng tiền nhận khi đến hạn: {total:,.0f} VNĐ")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "6":
            account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()

            found = False

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = True

                    if account["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break

                    actual_months = input("Nhập số tháng thực gửi: ").strip()

                    if (not actual_months.isdigit() or int(actual_months) <= 0):
                        print("Số tháng thực gửi không hợp lệ!")
                        break

                    if int(actual_months) < int(account["term_months"]):
                        rate = 0.5
                        print("Khách hàng rút trước hạn.")
                    else:
                        rate = float(account["interest_rate"])
                        print("Khách hàng đủ điều kiện hưởng lãi đúng hạn.")

                    interest = (int(account["balance"]) * rate / 100 * int(actual_months) / 12)

                    total = int(account["balance"]) + interest

                    print(f"Lãi suất áp dụng: {rate}%/năm")
                    print(f"Tiền lãi thực nhận: {interest:,.0f} VNĐ")
                    print(f"Tổng tiền thực nhận: {total:,.0f} VNĐ")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "7":
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")