patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


def validate_gender(gender_input):
    gender_input = gender_input.strip().lower()
    return gender_input in ["nam", "nu"]


def find_patient_index(patient_list, patient_id):
    patient_id = patient_id.strip().upper()

    for index, patient in enumerate(patient_list):
        if patient[0] == patient_id:
            return index

    return -1


def display_patients(patient_list):
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    for i, patient in enumerate(patient_list, start=1):
        print(
            f"{i}. Mã: {patient[0]:<5} | "
            f"Tên: {patient[1]:<20} | "
            f"Giới tính: {patient[2]:<5} | "
            f"Bệnh: {patient[3]}"
        )


def add_patient(patient_list):
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip().title()

    if patient_name == "":
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        gender = input("Nhập giới tính Nam/Nu: ")

        if validate_gender(gender):
            gender = gender.strip().lower().capitalize()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    disease = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    patient = [
        patient_id,
        patient_name,
        gender,
        disease
    ]

    patient_list.append(patient)

    print("Tiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list,patient_id)

    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return

    patient = patient_list[index]

    print(f"Tìm thấy bệnh nhân: {patient[1]}")
    print(f"Chẩn đoán hiện tại: {patient[3]}")

    new_disease = input("Nhập chẩn đoán mới: ").strip().capitalize()

    if new_disease == "":
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient[3] = new_disease

    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input("Nhập từ khóa tên bệnh: ").strip()

    if keyword == "":
        print("Từ khóa tìm kiếm không được để trống!")
        return

    count = 0

    print("Kết quả tìm kiếm:")

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1

            print(
                f"{count}. Mã: {patient[0]:<5} | "
                f"Tên: {patient[1]:<20} | "
                f"Giới tính: {patient[2]:<5} | "
                f"Bệnh: {patient[3]}"
            )

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")

    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case "1":
            display_patients(patients)

        case "2":
            add_patient(patients)

        case "3":
            update_diagnosis(patients)

        case "4":
            search_by_disease(patients)

        case "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")