# ham tinh BMI
def bmi(can, cao):
    if not cao == 0:
        value = can / (cao*cao)
        print("Chi so BMI: ", value)
    else:
        print("Loix")

    

bmi(53, 0)

# ham phan loai hoc luc
def avg(*score):
    total = 0
    for value in score:
        total += value

    avg_score = total / len(score)
    
    if avg_score >= 9:
        hoc_luc = 'Xuat sac'
    elif avg_score >= 8:
        hoc_luc = 'Gioi'
    elif avg_score >= 6.5:
        hoc_luc = 'Kha'
    elif avg_score >= 5:
        hoc_luc = "Trung binh"
    else:
        hoc_luc = "Yeu"

    return hoc_luc


print("Hoc luc cua cinh vien: ", avg(1,2,3,4,5))