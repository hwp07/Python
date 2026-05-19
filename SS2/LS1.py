# trade code: chương trình chạy từ trên xuống gặp điều kiện If đầu tiên > 100 nên in ra YELLOW và thoát luôn

# luồng thực thi: cấu trúc if-elif-else hoạt động theo quy tắc từ trên xuống, đến khi gặp điều kiện đúng sẽ thực hiện lệnh trong đó và thoát khỏi vòng lặp

# nguyên nhân khối RED bị bỏ qua: do 135 > 100 và > 120 nên sẽ luôn in ra YELLOW


print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")