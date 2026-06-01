# ==============================================================================
# HE THONG QUAN LY BAI DO XE THONG MINH
# Smart Parking Management System
# Dua tren tai lieu dac ta SRS - Smart Parking System
# ==============================================================================

parking_lot = []
next_id = 1

while True:
    print("\n" + "=" * 45)
    print("       HE THONG QUAN LY BAI DO XE")
    print("=" * 45)
    print("  1. Check-in  (Xe vao bai)")
    print("  2. Bao cao   (Danh sach xe trong bai)")
    print("  3. Tim kiem  (Tra cuu thong tin xe)")
    print("  4. Check-out (Xe ra bai & tinh phi)")
    print("  5. Thoat chuong trinh")
    print("=" * 45)

    try:
        choice = int(input("  Nhap lua chon cua ban: "))
    except ValueError:
        print("[Loi]: Lua chon khong hop le. Vui long nhap tu 1-5!")
        continue

    if choice < 1 or choice > 5:
        print("[Loi]: Lua chon khong hop le. Vui long nhap tu 1-5!")
        continue

    # ------------------------------------------------------------------
    # CHUC NANG 1: CHECK-IN
    # ------------------------------------------------------------------
    elif choice == 1:
        print("\n--- CHECK-IN: DANG KY XE VAO BAI ---")

        # Nhap bien so - khong duoc de trong
        plate = ""
        while plate.strip() == "":
            plate = input("Nhap bien so xe: ").strip()
            if plate == "":
                print("[Loi]: Bien so khong duoc de trong!")

        # Kiem tra trung bien so (ERR-01)
        da_ton_tai = False
        for xe in parking_lot:
            if xe["plate"].upper() == plate.upper():
                da_ton_tai = True
                break

        if da_ton_tai:
            print("[Loi]: Xe voi bien so nay da ton tai trong bai!")
            continue

        # Nhap loai xe (ERR-02) - loop den khi hop le
        loai_xe = 0
        while loai_xe not in [1, 2]:
            try:
                loai_xe = int(input("Nhap loai xe (1: Xe may | 2: O to): "))
                if loai_xe not in [1, 2]:
                    print("[Loi]: Loai xe khong hop le (1: Xe may, 2: O to)!")
            except ValueError:
                print("[Loi]: Loai xe khong hop le (1: Xe may, 2: O to)!")
                loai_xe = 0

        # Nhap gio vao
        gio_vao = -1
        while gio_vao < 0 or gio_vao > 24:
            try:
                gio_vao = int(input("Nhap gio vao (0-24): "))
                if gio_vao < 0 or gio_vao > 24:
                    print("[Loi]: Gio vao phai trong khoang 0 den 24!")
            except ValueError:
                print("[Loi]: Vui long nhap so nguyen hop le cho gio vao!")
                gio_vao = -1

        # Tao ban ghi xe moi
        xe_moi = {
            "id": next_id,
            "plate": plate.upper(),
            "type": loai_xe,
            "entry_time": gio_vao
        }

        parking_lot.append(xe_moi)
        next_id = next_id + 1

        ten_loai = "Xe may" if loai_xe == 1 else "O to"
        print(f"[Thanh cong]: Xe [{plate.upper()}] ({ten_loai}) da duoc dang ky vao bai luc {gio_vao}h.")

    # ------------------------------------------------------------------
    # CHUC NANG 2: BAO CAO TON KHO
    # ------------------------------------------------------------------
    elif choice == 2:
        print("\n--- BAO CAO: DANH SACH XE TRONG BAI ---")

        if len(parking_lot) == 0:
            print("[Thong bao]: Bai xe hien tai dang trong. Chua co xe nao duoc dang ky.")
        else:
            print(f"  Tong so xe dang trong bai: {len(parking_lot)}")
            print("-" * 55)
            print(f"  {'ID':<6} {'BIEN SO':<15} {'LOAI XE':<12} {'GIO VAO':<8}")
            print("-" * 55)
            for xe in parking_lot:
                ten_loai = "Xe may" if xe["type"] == 1 else "O to"
                print(f"  {xe['id']:<6} {xe['plate']:<15} {ten_loai:<12} {xe['entry_time']}h")
            print("-" * 55)

    # ------------------------------------------------------------------
    # CHUC NANG 3: TIM KIEM XE
    # ------------------------------------------------------------------
    elif choice == 3:
        print("\n--- TIM KIEM: TRA CUU THONG TIN XE ---")

        plate_search = ""
        while plate_search.strip() == "":
            plate_search = input("Nhap bien so can tim: ").strip()
            if plate_search == "":
                print("[Loi]: Bien so khong duoc de trong!")

        xe_tim_thay = None
        for xe in parking_lot:
            if xe["plate"].upper() == plate_search.upper():
                xe_tim_thay = xe
                break

        if xe_tim_thay is None:
            print(f"[Loi]: Khong tim thay bien so [{plate_search.upper()}] trong he thong!")
        else:
            ten_loai = "Xe may" if xe_tim_thay["type"] == 1 else "O to"
            print("-" * 40)
            print(f"  ID         : {xe_tim_thay['id']}")
            print(f"  Bien so    : {xe_tim_thay['plate']}")
            print(f"  Loai xe    : {ten_loai}")
            print(f"  Gio vao    : {xe_tim_thay['entry_time']}h")
            print(f"  Trang thai : Dang do trong bai")
            print("-" * 40)

    # ------------------------------------------------------------------
    # CHUC NANG 4: CHECK-OUT
    # ------------------------------------------------------------------
    elif choice == 4:
        print("\n--- CHECK-OUT: XE RA BAI & TINH PHI ---")

        plate_out = ""
        while plate_out.strip() == "":
            plate_out = input("Nhap bien so xe can lay ra: ").strip()
            if plate_out == "":
                print("[Loi]: Bien so khong duoc de trong!")

        # Tim xe trong bai (ERR-04)
        xe_can_lay = None
        vi_tri = -1
        for i in range(len(parking_lot)):
            if parking_lot[i]["plate"].upper() == plate_out.upper():
                xe_can_lay = parking_lot[i]
                vi_tri = i
                break

        if xe_can_lay is None:
            print(f"[Loi]: Khong tim thay bien so [{plate_out.upper()}] trong he thong!")
            continue

        # Nhap gio ra - phai >= gio vao (ERR-03)
        gio_ra = -1
        while True:
            try:
                gio_ra = int(input(f"Nhap gio ra (gio vao la {xe_can_lay['entry_time']}h, 0-24): "))
                if gio_ra < 0 or gio_ra > 24:
                    print("[Loi]: Gio ra phai trong khoang 0 den 24!")
                elif gio_ra < xe_can_lay["entry_time"]:
                    print("[Loi]: Gio ra phai sau hoac bang gio vao!")
                else:
                    break
            except ValueError:
                print("[Loi]: Vui long nhap so nguyen hop le cho gio ra!")

        # Tinh phi theo quy tac nghiep vu
        so_gio = gio_ra - xe_can_lay["entry_time"]

        if xe_can_lay["type"] == 1:
            don_gia = 2000
            ten_loai = "Xe may"
        else:
            don_gia = 5000
            ten_loai = "O to"

        tong_phi = so_gio * don_gia

        # Hien thi hoa don
        print("\n" + "=" * 40)
        print("            HOA DON THANH TOAN")
        print("=" * 40)
        print(f"  Bien so    : {xe_can_lay['plate']}")
        print(f"  Loai xe    : {ten_loai}")
        print(f"  Gio vao    : {xe_can_lay['entry_time']}h")
        print(f"  Gio ra     : {gio_ra}h")
        print(f"  So gio do  : {so_gio} gio")
        print(f"  Don gia    : {don_gia:,} VND/gio")
        print("-" * 40)
        print(f"  Tong phi   : {tong_phi:,} VND")
        print("=" * 40)

        # Xoa xe khoi danh sach
        parking_lot.pop(vi_tri)
        print(f"[Thanh cong]: Xe [{xe_can_lay['plate']}] da ra bai. Cam on quy khach!")

    # ------------------------------------------------------------------
    # CHUC NANG 5: THOAT
    # ------------------------------------------------------------------
    elif choice == 5:
        print("\n[He thong]: Cam on da su dung dich vu. Hen gap lai!")
        print("Chuong trinh da ket thuc.\n")
        break