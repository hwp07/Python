# cho 1 list [100,200,300,101,103]
# tạo 1 list chỉ chứa các số lẻ

number = [100,200,300,101,103]
new_list = []

for index, number in enumerate(number, start=0):
    if number % 2 != 0:
        new_list.append(number)

print(new_list)