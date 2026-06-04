# 1. vì raw_diagnosis là chuỗi - kiểu dữ liệu bất biến nên không thể thay đổi
# 2. cần code như sau: raw_diagnosis = raw_diagnosis.strip().title()
# 3. extend() đã duyệt qua từng ký tự trong chuỗi và thêm từng ký tự vào list
# 4. nên thay  extend() = append()

# code hoàn chỉnh
patient_diagnoses = ["Sốt Xuất Huyết"]


def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)
    return current_list

new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis,patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)