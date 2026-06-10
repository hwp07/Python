# 1. trong python, phép chia cho 0 là không hợp lệ và tronbg try except cũng k có đoạn xử lý trường hợp này nên chương trình bị dừng luôn
# 2. màn hình sẽ in ra lỗi valueError vì python cố gắng chuyển "ba" thành 3 nhưng không thể
# 3. 
# - player_stats
# - player
# - name
# - kills
# - deaths
# - assists
# 4. 
# - dễ bảo trì
# - dễ test
# - tái sử dụng


player_stats = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths


def process_player_stats(player_stats):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player in player_stats:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(kills, deaths, assists)

            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")

        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
            continue

        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")
            continue

    print("--- HOÀN TẤT ---")


process_player_stats(player_stats)