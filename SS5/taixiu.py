# # import random

# # money = int(input('Nhập số tiền: '))

# # bet = int(input('Nhập số tiền cược'))

# import random
# import time

# money = int(input('Nhập số tiền cần nạp: '))

# while True:
#     print("\n=== BẮT ĐẦU LẮC TÀI XỈU ===")
#     print("Đang lắc xúc xắc... 🎲🎲🎲")
#     time.sleep(2)

#     bet = int(input('Vui lòng đặt tiền cược: '))
#     if bet > money :
#         print('Không đủ lúa. Vui lòng nạp thêm')
#         continue

#     choice = input('Tài/Xỉu: ').upper()

#     dice1 = random.randint(1, 6)
#     print("🎲 Xúc xắc 1 đang mở...")
#     time.sleep(1)
#     print(f"-> Kết quả xúc xắc 1: {dice1}\n")


#     dice2 = random.randint(1, 6)
#     print("🎲 Xúc xắc 2 đang mở...")
#     time.sleep(1)
#     print(f"-> Kết quả xúc xắc 2: {dice2}\n")


#     dice3 = random.randint(1, 6)
#     print("🎲 Xúc xắc 3 đang mở...")
#     time.sleep(1)
#     print(f"-> Kết quả xúc xắc 3: {dice3}\n")

#     total = dice1 + dice2 + dice3
#     print("---------------------------")
#     print(f"Tổng điểm 3 xúc xắc: {total}")

#     if dice1 == dice2 == dice3:
#         result = "NỔ HŨ"
#     elif 4 <= total <= 10:
#         result = "XỈU"
#     elif 11 <= total <= 17:
#         result = "TÀI"

#     if choice == result:
#         time.sleep(0.5)
#         print(f"\nXIN CHÚC MỪNG 🎉")

#         total = money + bet
#         print('Số tiền còn lại: ',total) 
#     else :
#         time.sleep(0.5)
#         print('\nHAHAH MÀY NGUUUU')

#         total = money - bet
#         print('Số tiền còn lại: ',total)


import random
import time

# --- BƯỚC 1: NẠP TIỀN BAN ĐẦU ---
while True:
    try:
        money = int(input('Nhập số tiền cần nạp: '))
        if money > 0:
            break
        print("⚠️ Số tiền nạp phải lớn hơn 0!")
    except ValueError:
        print("⚠️ Vui lòng nhập một số nguyên hợp lệ!")

# --- BƯỚC 2: VÒNG LẶP CHƠI GAME ---
while True:
    print(f"\n=====================================")
    print(f"💰 SỐ DƯ HIỆN TẠI: {money} VND")
    
    # 1. Điều kiện hết tiền (Cháy tài khoản)
    if money <= 0:
        print("\n❌ Bạn đã hết sạch tiền!")
        nap_them = input("Nhập 'Y' để nạp thêm tiền, nhấn phím bất kỳ khác để THOÁT: ").upper()
        if nap_them == 'Y':
            while True:
                try:
                    them = int(input('Nhập số tiền nạp thêm: '))
                    if them > 0:
                        money += them
                        break
                    print("⚠️ Số tiền nạp thêm phải lớn hơn 0!")
                except ValueError:
                    print("⚠️ Vui lòng nhập số nguyên hợp lệ!")
            continue  # Quay lại đầu vòng lặp sau khi nạp tiền
        else:
            print("Cảm ơn bạn đã trải nghiệm game. Hẹn gặp lại!")
            break

    # 2. Lựa chọn chơi tiếp hoặc rút tiền (Thoát game)
    action = input("Nhấn Enter để chơi tiếp, hoặc nhập 'Q' để RÚT TIỀN & THOÁT: ").upper()
    if action == 'Q':
        print(f"\n🎉 Bạn đã rút thành công {money} VND về tài khoản ngân hàng!")
        print("Hẹn gặp lại bạn lần sau!")
        break

    # 3. Đặt tiền cược và kiểm tra hợp lệ
    while True:
        try:
            bet = int(input('Vui lòng đặt tiền cược: '))
            if bet <= 0:
                print('⚠️ Tiền cược phải lớn hơn 0!')
            elif bet > money:
                print('⚠️ Không đủ lúa! Vui lòng cược ít hơn số tiền bạn có.')
            else:
                break  # Tiền cược hợp lệ
        except ValueError:
            print('⚠️ Vui lòng nhập số tiền cược bằng số nguyên!')

    # 4. Chọn Tài hoặc Xỉu (Cho phép nhập tắt T/X, chữ thường, chữ hoa)
    while True:
        choice_input = input('Chọn Tài (T) hoặc Xỉu (X): ').strip().upper()
        if choice_input in ['T', 'TAI', 'TÀI']:
            choice = "TÀI"
            break
        elif choice_input in ['X', 'XIU', 'XỈU']:
            choice = "XỈU"
            break
        else:
            print('⚠️ Lựa chọn không hợp lệ! Vui lòng chỉ chọn Tài (T) hoặc Xỉu (X).')

    # 5. Bắt đầu lắc xúc xắc
    print("\nĐang lắc xúc xắc... 🎲🎲🎲")
    time.sleep(2)

    dice1 = random.randint(1, 6)
    print("🎲 Xúc xắc 1 đang mở...")
    time.sleep(0.8)
    print(f"-> Kết quả xúc xắc 1: {dice1}\n")

    dice2 = random.randint(1, 6)
    print("🎲 Xúc xắc 2 đang mở...")
    time.sleep(0.8)
    print(f"-> Kết quả xúc xắc 2: {dice2}\n")

    dice3 = random.randint(1, 6)
    print("🎲 Xúc xắc 3 đang mở...")
    time.sleep(0.8)
    print(f"-> Kết quả xúc xắc 3: {dice3}\n")

    # Tính tổng điểm (dùng tên biến tránh đè lên nhau)
    dice_sum = dice1 + dice2 + dice3
    print("-------------------------------------")
    print(f"Tổng điểm 3 xúc xắc: {dice_sum}")

    # Xác định kết quả xúc xắc theo luật thực tế
    if dice1 == dice2 == dice3:
        result = "NỔ HŨ"  # Bộ ba đồng nhất (Bão), luật web thực tế là nhà cái ăn hết
    elif 4 <= dice_sum <= 10:
        result = "XỈU"
    elif 11 <= dice_sum <= 17:
        result = "TÀI"

    print(f"Kết quả bàn cược: {result}")

    # 6. Xử lý Thắng / Thua tiền cược
    if choice == result:
        time.sleep(0.5)
        print(f"\n🎉 XIN CHÚC MỪNG! Bạn đã thắng +{bet} VND")
        money += bet  # Cộng tiền thắng trực tiếp vào tài khoản
    else:
        time.sleep(0.5)
        if result == "NỔ HŨ":
            print(f"\n❌ Chia buồn! Kết quả là NỔ HŨ (Bão {dice1}). Bạn mất -{bet} VND")
        else:
            print(f"\n❌ Chia buồn! Kết quả là {result}. Bạn đoán sai và mất -{bet} VND")
        money -= bet  # Trừ tiền thua trực tiếp khỏi tài khoản

    time.sleep(1)