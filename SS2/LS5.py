print("=== HỆ THỐNG KIOSK TỰ PHỤC VỤ - BỆNH VIỆN SỨC KHỎE VÀNG ===")
print("Vui lòng nhập chính xác các thông tin dưới đây để được phân luồng tự động.\n")

patient_name = input("1. Nhập họ và tên bệnh nhân (Ví dụ: Nguyen Van A): ").strip()
patient_age = int(input("2. Nhập tuổi hiện tại của bệnh nhân (Ví dụ: 35): "))
spo2_level = int(input("3. Nhập nồng độ oxy trong máu SpO2 % (Ví dụ: 96): "))
heart_rate = int(input("4. Nhập nhịp tim - nhịp/phút (Ví dụ: 80): "))
has_insurance = input("5. Bạn có thẻ Bảo hiểm Y tế không? (có/không): ").strip().lower()



if patient_name == "":
    print("\nTên bệnh nhân không được để trống!")
elif patient_age < 0 or patient_age > 150:
    print("\nTuổi bệnh nhân không hợp lệ (Phải nằm trong khoảng 0 - 150)!")
elif spo2_level < 0 or spo2_level > 100:
    print("\nChỉ số SpO2 không hợp lệ (Phải nằm trong khoảng 0% - 100%)!")
elif heart_rate < 0 or heart_rate > 300:
    print("\nChỉ số nhịp tim không hợp lệ (Phải nằm trong khoảng 0 - 300 nhịp/phút)!")
elif has_insurance != "có" and has_insurance != "không":
    print("\nLựa chọn Bảo hiểm y tế không đúng định dạng (Chỉ chấp nhận 'yes' hoặc 'no')!")

else:
    if spo2_level < 90 or heart_rate > 120:
        triage_status = "BÁO ĐỘNG ĐỎ (Cấp cứu khẩn cấp - Chuyển ngay vào phòng hồi sức!)"
    elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
        triage_status = "BÁO ĐỘNG VÀNG (Theo dõi sát - Di chuyển tới khu vực chờ ưu tiên)"
    else:
        triage_status = "XANH (Khám thường - Chờ gọi số theo lượt tại sảnh chính)"


    base_fee = 500000
    
    if patient_age < 6 or patient_age >= 80:
        advance_payment = 0
        fee_note = "Miễn phí 100% viện phí (Đối tượng ưu tiên: Trẻ em < 6 tuổi hoặc Người già >= 80 tuổi)"
    elif has_insurance == "yes":
        advance_payment = 250000
        fee_note = "Giảm 50% viện phí (Đã áp dụng quyền lợi thẻ Bảo hiểm Y tế)"
    else:
        advance_payment = 500000
        fee_note = "Thu 100% viện phí (Không có thẻ BHYT hoặc không thuộc diện miễn giảm)"


    print("\n" + "="*60)
    print("                 PHIẾU PHÂN LUỒNG KHÁM BỆNH")
    print("               (Hệ thống Kiosk tự động cấp)")
    print("="*60)
    print(f" Họ và tên bệnh nhân   : {patient_name.upper()}")
    print(f" Tuổi                  : {patient_age} tuổi")
    print(f" Chỉ số sinh hiệu      : SpO2 {spo2_level}% | Nhịp tim: {heart_rate} nhịp/phút")
    print(f" Trạng thái thẻ BHYT   : {'Có áp dụng' if has_insurance == 'yes' else 'Không áp dụng'}")
    print("-"*60)
    print(f" KẾT QUẢ PHÂN LUỒNG    : {triage_status}")
    print(f" SỐ TIỀN TẠM ỨNG       : {advance_payment:,} VNĐ")
    print(f" Ghi chú diện chi trả  : {fee_note}")
    print("="*60)
    print("Vui lòng cầm phiếu này và di chuyển theo hướng dẫn của mũi tên trên sàn.")