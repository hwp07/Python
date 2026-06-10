
import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

roster = [
    {"player_id": "P01", "name": "Faker", "role": "Mid Lane", "salary": 5000.0, "status": "Active"},
    {"player_id": "P02", "name": "Oner", "role": "Jungle", "salary": 3500.0, "status": "Active"},
    {"player_id": "P03", "name": "Ruler", "role": "ADC", "salary": 6000.0, "status": "Benched"}
]


def find_player(roster_list, player_id):
    for player in roster_list:
        if player.get("player_id", "").upper() == player_id:
            return player
    return None

def display_roster(roster_list):
    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<12} | Trạng thái")

    for player in roster_list:
        try:
            status = player["status"]
        except KeyError:
            status = "Unknown"

        name = player.get("name", "Unknown")
        if status == "Benched":
            name += " [DỰ BỊ]"

        print(
            f"{player.get('player_id','N/A'):<8} | "
            f"{name:<20} | "
            f"{player.get('role','N/A'):<15} | "
            f"{player.get('salary',0):<12,.1f} | "
            f"{status}"
        )

    logging.info("Coach viewed the team roster.")

def sign_player(roster_list):
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    if find_player(roster_list, player_id):
        print(f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại.")
        logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
        return

    name = input("Nhập tên tuyển thủ: ").strip().title()
    role = input("Nhập vị trí thi đấu: ").strip().title()

    while True:
        try:
            salary = float(input("Nhập mức lương hàng tháng: "))
            if salary <= 0:
                print("Lương phải là số dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")

    roster_list.append({
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    })

    logging.info(f"Signed new player {name} with salary {salary}")
    print(f"Thành công: Đã chiêu mộ tuyển thủ {name}.")

def update_player_status(roster_list):
    player_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()

    player = find_player(roster_list, player_id)

    if not player:
        print(f"Không tìm thấy tuyển thủ mang mã {player_id}.")
        logging.warning(f"Failed to update player - Player ID {player_id} not found")
        return

    print(f"\nTuyển thủ: {player['name']}")
    print(f"Vị trí: {player['role']}")
    print(f"Lương hiện tại: {player['salary']:,.1f}")
    print(f"Trạng thái hiện tại: {player['status']}")

    print("\n1. Cập nhật lương")
    print("2. Cập nhật trạng thái thi đấu")

    choice = input("Chọn chức năng cập nhật (1-2): ")

    if choice == "1":
        old_salary = player["salary"]

        while True:
            try:
                new_salary = float(input("Nhập mức lương mới: "))
                if new_salary <= 0:
                    print("Lương phải là số dương.")
                    continue
                break
            except ValueError:
                print("Lương phải là số.")

        player["salary"] = new_salary

        logging.info(
            f"Updated player {player_id} salary from "
            f"{old_salary} to {new_salary}"
        )

    elif choice == "2":
        print("1. Active")
        print("2. Benched")

        status_choice = input("Nhập lựa chọn trạng thái (1-2): ")
        old_status = player["status"]

        player["status"] = "Active" if status_choice == "1" else "Benched"

        logging.info(
            f"Updated player {player_id} status from "
            f"{old_status} to {player['status']}"
        )

def generate_payroll_report(roster_list):
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")

    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return

    total = 0

    try:
        print(f"{'ID':<8} | {'Tên':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | Lương thực nhận")

        for player in roster_list:
            salary = player["salary"]
            status = player["status"]

            actual_salary = salary if status == "Active" else salary * 0.5

            total += actual_salary

            print(
                f"{player['player_id']:<8} | "
                f"{player['name']:<15} | "
                f"{status:<10} | "
                f"{salary:<12,.1f} | "
                f"{actual_salary:,.1f}"
            )

        print("-" * 80)
        print(f"Tổng quỹ lương hàng tháng: {total:,.1f}")

        logging.info(
            f"Generated monthly payroll report. Total: {total}"
        )

    except KeyError as error:
        print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
        logging.error(f"Missing key while generating payroll report: {error}")

if __name__ == "__main__":
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")

        choice = input("Chọn chức năng (1-5): ")

        match choice:
            case "1":
                display_roster(roster)

            case "2":
                sign_player(roster)

            case "3":
                update_player_status(roster)

            case "4":
                generate_payroll_report(roster)

            case "5":
                logging.info("System shutdown.")
                break

            case _:
                print("Lựa chọn không hợp lệ.")


