raw_logs = []
processed_logs = []


def clean_logs():
    global raw_logs

    print("--- NẠP DỮ LIỆU LOG ---")
    logs = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")

    table = str.maketrans("", "", "!@#$")
    cleaned_data = logs.translate(table)

    raw_logs = [log.strip() for log in cleaned_data.split(";") if log.strip()]

    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")


def filter_logs():
    global processed_logs

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    processed_logs = [
        log for log in raw_logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

    print("--- LỌC CẢNH BÁO ---")

    if not processed_logs:
        print("Không tìm thấy cảnh báo nguy hiểm.")
        return

    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")

    for log in processed_logs:
        print(f"- {log}")


def mask_ip():
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    if not processed_logs:
        print("Chưa có log cảnh báo để mã hóa.")
        return

    masked_logs = []

    for log in processed_logs:
        words = log.split()

        for i in range(len(words)):
            if "." in words[i]:
                ip_parts = words[i].split(".")

                if len(ip_parts) == 4:
                    words[i] = ".".join(ip_parts[:2] + ["*", "*"])

        masked_logs.append(" ".join(words))

    print("--- MÃ HÓA IP ---")
    print("Báo cáo log an toàn:")

    for index, log in enumerate(masked_logs, start=1):
        print(f"{index}. {log}")

    return masked_logs



while True:
    print("\n============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
    print("3. Mã hóa địa chỉ IP (Masking)")
    print("4. Đóng hệ thống")
    print("=================================================")

    choice = input("Chọn chức năng (1-4): ")

    match choice:
        case "1":
            clean_logs()

        case "2":
            filter_logs()

        case "3":
            mask_ip()

        case "4":
            print("Đóng hệ thống...")
            break

        case _:
            print("Lựa chọn không hợp lệ.")


