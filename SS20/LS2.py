# 1. indexError xảy ra vì sofm chỉ có 2 phần tử nên p[2] không hợp lệ
# 2. chuong trình sẽ sập ở dòng int(r) vì "N/A" không thể chuyển thành số nguyên bằng int()
# 3. giúp biết chương trình đang xử lý bản ghi nào trước khi bị lỗi, từ đó nhanh chóng xác định dữ liệu gây crash
# 4. 
# - player_records
# - record
# - name
# - matches
# - mmr
# - bonus

player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]

def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)

def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        name = record[0]

        try:
            matches = record[1]
            mmr = int(record[2])

            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")

        except IndexError:
            print(f"{name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"{name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

process_bonus(player_records)