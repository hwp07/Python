# toán tử logic bị dùng sai: sử dụng toán tử or thay vì toán tử and 

# trace code: chương trình kiểm tra điều kiện: 16 >= 18 or 55 >= 50

# vì sử dụng toán tử or, chỉ cần một trong hai vế đúng là toàn bộ biểu thức điều kiện trả về đúng

# Sự khác biệt giữa and và or:
# and: trả về true khi tất cả các điều kiện đều đúng
# or: trả về true khi chỉ cần một trong các điều kiện đúng


print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu chính xác
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    
    # Nêu rõ lý do cụ thể cho người khai báo
    if donor_age < 18 and donor_weight < 50:
        print("Lý do: Không đủ tuổi (dưới 18) và không đủ cân nặng (dưới 50kg).")
    elif donor_age < 18:
        print("Lý do: Không đủ tuổi (phải từ 18 tuổi trở lên).")
    else:
        print("Lý do: Không đủ cân nặng (phải từ 50kg trở lên).")