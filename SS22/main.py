import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)


def show_devices(devices_list):
    logger.debug(f"Hiển thị danh sách thiết bị. Tổng số: {len(devices_list)}")

    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return

    print("-" * 95)
    print(
        f"{'MÃ THIẾT BỊ':<15}"
        f"{'VỊ TRÍ PHÂN XƯỞNG':<30}"
        f"{'CHỈ SỐ CŨ':>15}"
        f"{'CHỈ SỐ MỚI':>15}"
        f"{'TRẠNG THÁI':>20}"
    )
    print("-" * 95)

    for device in devices_list:
        print(
            f"{device['id']:<15}"
            f"{device['location']:<30}"
            f"{device['old_index']:>15,.2f}"
            f"{device['new_index']:>15,.2f}"
            f"{device['status']:>20}"
        )

    print("-" * 95)

# UPDATE INDICES
def update_indices(devices_list):
    logger.debug("Bắt đầu cập nhật chỉ số điện")

    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return

    device_id = input("Nhập mã thiết bị cần cập nhật chỉ số: ").strip()

    device = None

    for item in devices_list:
        if item["id"] == device_id:
            device = item
            break

    if device is None:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        logger.error("ERR-E01 - Device not found")
        return

    while True:
        try:
            old_index = float(input("Nhập chỉ số cũ: "))

            if old_index < 0:
                raise ValueError

            break

        except ValueError:
            print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
            logger.error("ERR-E03 - Invalid old index")

    while True:
        try:
            new_index = float(input("Nhập chỉ số mới: "))

            if new_index < 0:
                raise ValueError

            if new_index < old_index:
                print("[Lỗi] (ERR-E02): Số liệu lỗi! Chỉ số mới không được nhỏ hơn chỉ số cũ!")
                logger.error("ERR-E02 - New index < old index")
                continue

            break

        except ValueError:
            print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
            logger.error("ERR-E03 - Invalid new index")

    device["old_index"] = old_index
    device["new_index"] = new_index

    logger.info(f"[Thành công]: Đã check-in số liệu cho thiết bị {device_id}")

    print(f"[Thành công]: Đã cập nhật chỉ số cho thiết bị {device_id}")

# TRIGGER OVERLOAD
def trigger_overload_alert(devices_list):
    logger.debug("Kiểm tra trạng thái Overload")

    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return

    device_id = input("Nhập mã thiết bị cần cập nhật: ").strip()

    device = None

    for item in devices_list:
        if item["id"] == device_id:
            device = item
            break

    if device is None:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        logger.error("ERR-E01 - Device not found")
        return

    if device["status"] == "Overload":
        print("[Lỗi] (ERR-E04): Thao tác bị hủy! Thiết bị này đã được kích hoạt trạng thái OVERLOAD từ trước!")
        logger.error("ERR-E04 - Already overload")
        return

    consumption = (device["new_index"] - device["old_index"])

    if consumption > 5000:
        device["status"] = "Overload"

        logger.warning(f"[Cảnh báo]: Thiết bị {device_id} đã vượt ngưỡng tiêu thụ an toàn, chuyển sang OVERLOAD!")

        print(f"[Thành công]: Thiết bị {device_id} đã được chuyển sang trạng thái OVERLOAD")

    else:
        print("Thiết bị chưa vượt ngưỡng tiêu thụ 5000 kWh.")



# CALCULATE FINANCIALS
def calculate_energy_financials(devices_list):
    logger.debug(f"Đang tính toán chi phí năng lượng cho {len(devices_list)} thiết bị")

    if not devices_list:
        return (0.0, 0.0, 0.0)

    total_kwh = 0

    for device in devices_list:
        total_kwh += (device["new_index"] - device["old_index"])

    unit_price = 3000

    total_cost = ( total_kwh * unit_price)

    discount_percent = 0

    if total_kwh >= 50000:
        discount_percent = 3

    discount_amount = (total_cost * discount_percent / 100)

    final_cost = (total_cost - discount_amount)

    return (
        total_kwh,
        discount_percent,
        final_cost
    )

# MAIN
def main():

    devices_list = [
        {
            "id": "M01",
            "location": "Mechanical Shop A",
            "old_index": 10000,
            "new_index": 16000,
            "status": "Normal"
        },
        {
            "id": "M02",
            "location": "Assembly Line B",
            "old_index": 25000,
            "new_index": 28000,
            "status": "Normal"
        },
        {
            "id": "M03",
            "location": "Packaging Area",
            "old_index": 5000,
            "new_index": 6200,
            "status": "Normal"
        }
    ]

    while True:
        print("\n===== SMART ENERGY MONITOR =====")
        print("1. Xem danh sách thiết bị")
        print("2. Cập nhật chỉ số điện")
        print("3. Kích hoạt cảnh báo quá tải")
        print("4. Tính tổng điện & chi phí")
        print("5. Thoát")

        choice = int(input("Nhập lựa chọn của bạn: "))

        match choice:
            case 1:
                show_devices(devices_list)

            case 2:
                update_indices(devices_list)

            case 3:
                trigger_overload_alert(devices_list)

            case 4:
                total_kwh, discount_percent, final_cost = calculate_energy_financials(devices_list)

                print(f"\n===== BÁO CÁO =====\nTổng điện tiêu thụ: {total_kwh:,.2f} kWh\nChiết khấu: {discount_percent}%\nTổng tiền sau chiết khấu: {final_cost:,.0f} VND")

            case 5:
                logger.info("System shutdown.")
                print("Đóng hệ thống...")
                break

            case _:
                print("[Lỗi] (ERR-E05): Lựa chọn sai! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 5!")

if __name__ == "__main__":
    main()