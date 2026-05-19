from datetime import datetime 

# 1. Nhập thông tin bệnh nhân
name = input('Nhap ten benh nhan: ').strip()
age = int(input('Nhap nam sinh: '))
date = int(input('Nhap so ngay bi benh: '))
temperature = float(input('Nhap nhiet do co the: ')) 
price = int(input('Nhap chi phi kham: '))

current_year = datetime.now().year

if name == "":
    print('Tên không được để trống')
elif age < 1900 or age > current_year:
    print('Năm sinh không hợp lệ')
elif date < 0:
    print('Số ngày bị bệnh không hợp lệ')
elif temperature < 30 or temperature > 45:
    print('Nhiệt độ không hợp lệ')
elif price <= 0:
    print('Chi phí khám không hợp lệ')

else:
    age_patient = current_year - age
    fee = price * 0.1
    total_price = price + fee

    result = ''
    if temperature > 38 and date > 3:
        result = 'Nguy hiểm'
    elif temperature > 38:
        result = 'Sốt cao'
    elif temperature > 37.5:
        result = 'Sốt nhẹ'
    else:
        result = 'Bình thường'

    if result == 'Nguy hiểm':
        if age_patient > 60:
            rate = 'Cấp cứu'
        else:
            rate = 'Ưu tiên cao'
    else:
        rate = 'Bình thường'

    cost_level = 'Cao' if total_price > 500000 else 'Thấp'

    print("\n--- KẾT QUẢ ---")
    print(f"Tên: {name}")
    print(f"Tuổi: {age_patient}")
    print(f"Nhiệt độ: {temperature:.1f} °C")
    print(f"Số ngày bệnh: {date}")
    print()
    print(f"Tình trạng: {result}")
    print(f"Mức độ ưu tiên: {rate}")
    print()
    print(f"Tổng chi phí: {total_price:.1f} VND")
    print(f"Mức chi phí: {cost_level}")