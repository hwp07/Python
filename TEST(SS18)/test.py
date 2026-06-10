player_list = [
    {
        "id": 'CT007',
        "name": "Nguyen Quang Hai",
        "match": 10,
        "goal": 5,
        "support": 4,
        "peformance": 33,
        "rank": "Trụ cột đội bóng"
    }
]

# hien thi danh sach
def display_player(list_player):
    print("\n     DANH SÁCH CẦU THỦ\n")
    print(f"{'Mã cầu thủ':<15} | {'Họ và tên':<25} | {'Số trận':<10} | {'Bàn thắng:':<10} | {'Kiến tạo':<10} | {'Điểm hiệu suất':<20} | {'Phân loại':<20}")
    for i in list_player:   
        peformance = (i["match"] * 1) + (i["goal"] * 3) + (i["support"] * 2)

        if peformance >= 50:
            rank = "Ngôi sao đẳng cấp"
        elif peformance >= 30:
            rank = "Trụ cột đội bóng"
        elif peformance >= 15:
            rank = "Dự biến chiến lược"
        else :
            rank = "Cần thanh lý / Cho mượn"

        print(f"{i["id"]:<15} | {i["name"]:<25} | {i["match"]:<10} | {i["goal"]:<10} | {i["support"]:<10} | {peformance:<20} | {rank:<20}")


# them cau thu
def add_player(list_player):
    new_player = {}

    while True:
        new_player["id"] = input("Nhập mã cầu thủ: ")
        flag = 0

        for i in list_player:
            if new_player["id"] == "" or new_player["id"] == i["id"]:
                print("Mã cầu thủ không hợp lệ!")
                flag = 1
                continue
        
        if flag == 0:
            break
        

    while True:
        new_player["name"] = input("Nhập tên cầu thủ: ")

        if new_player["name"] == "":
            print("Tên cầu thủ không được để trống")
            continue
        break

    while True:
        try:
            new_player["match"] = int(input("Nhập số trận: "))

            if new_player["match"] < 0 or new_player["match"] > 50 or new_player["match"] == "":
                print("Số trận không hợp lệ!")
                continue
            break
        except ValueError:
             print("Số trận không hợp lệ!")

    while True:
        try:
            new_player["goal"] = int(input("Nhập số bàn thắng: "))

            if new_player["goal"] < 0:
                print("Số bàn thắng không hợp lệ!")
                continue
            break
        except ValueError:
            print("Số bàn thắng không hợp lệ!")

    while True:
        try:
            new_player["support"] = int(input("Nhập số kiến tạo: "))

            if new_player["support"] < 0:
                print("Số kiến tạo không hợp lệ!")
                continue
            break
        except ValueError:
            print("Số kiến tạo không hợp lệ!")

    list_player.append(new_player)
    print(f"Thêm cầu thủ {new_player["id"]} thành công!")

    
# cap nhat
def update_player(list_player):
    while True:
        find_id = input('Nhập mã cầu thủ muốn cập nhật: ')

        for i in list_player:
            if find_id != i["id"]:
                print("Mã cầu thủ không tồn tại!")
                break
            else:
                while True:
                    try:
                        i["match"] = int(input("Nhập số trận: "))

                        if i["match"] < 0 or i["match"] > 50 or i["match"] == "":
                            print("Số trận không hợp lệ!")
                            continue
                        break
                    except ValueError:
                        print("Số trận không hợp lệ!")

                while True:
                    try:
                        i["goal"] = int(input("Nhập số bàn thắng: "))

                        if i["goal"] < 0:
                            print("Số bàn thắng không hợp lệ!")
                            continue
                        break
                    except ValueError:
                        print("Số bàn thắng không hợp lệ!")

                while True:
                    try:
                        i["support"] = int(input("Nhập số kiến tạo: "))

                        if i["support"] < 0:
                            print("Số kiến tạo không hợp lệ!")
                            continue
                        break
                    except ValueError:
                        print("Số kiến tạo không hợp lệ!")

                print(f"Cập nhật thành công cầu thủ {i["id"]}")
                break
        break
        
def delete_player(list_player):
    while True:
        find_id = input('Nhập mã cầu thủ muốn xóa: ').upper()

        for i in list_player:
            if find_id == i["id"]:
                confirm = input("Xác nhận xóa(Y/N): ").upper()

                if confirm == "Y":
                    list_player.remove(i)
                    print("Xóa thành công")
                    break
                else: 
                    print("Thao tác xóa bi hủy!")
            else:
                print("Không tồn tại cầu thủ!")
                break
        break

        
        
# tim kiem cau thu
def search_player(list_player):
    keyword = input("Nhập mã hoặc tên cầu thủ cần tìm: ").strip().lower()

    result = []

    for i in list_player:
        if i["id"].lower() == keyword:
            result.append(i)

        elif keyword in i["name"].lower():
            result.append(i)

    if len(result) == 0:
        print("Không tìm thấy sinh viên phù hợp!")
        return

    display_player(list_player)


# thong ke
def total_rank(list_player):
    best = 0
    good = 0
    mid = 0
    bad = 0

    for i in list_player:
        if i["rank"] == "Ngôi sao đẳng cấp":
            best += 1
        elif i["rank"] == "Trụ cột đội bóng":
            good += 1
        elif i["rank"] == "Dự bị chiến lược":
            mid += 1
        elif i["rank"] == "Cần thanh lý / Cho mượn": 
            bad += 1

    print(f"Ngôi sao đẳng cấp: {best} người\nTrụ cột đội bóng: {good} người\nDự bị chiến lược: {mid} người\nCần thanh lý / Cho mượn: {bad} người")

while True:
    print("""
        QUẢN LÝ CẦU THỦ
1. Hiển thị danh sách cầu thủ
2. Tiếp nhận cầu thủ
3. Cập nhật cầu thủ mới
4. Xóa cầu thủ (Thanh lý hợp đồng)
5. Tìm kiếm cầu thủ
6. Thống kê phân loại phong độ
7. Đánh giá phong độ tự động
8. Thoát chương trình
""")
    
    choice = input("Nhập sự lựa chọn của bạn: ")

    match choice:
        case "1":
            if len(player_list) == 0:
                print("Danh sách cầu thủ trống")
            else:
                display_player(player_list)

        case "2":
            add_player(player_list)

        case "3":
            update_player(player_list)

        case "4":
            delete_player(player_list)

        case "5":
            search_player(player_list)

        case "6":
            total_rank(player_list)


        case "8":
            print("See you later!")
        
        case _:
            print("Lựa chọn không hợp lệ!")