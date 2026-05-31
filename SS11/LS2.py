# 1. dictionary employee gồm các key:
# - employee_id
# - full_name
# - department
# - status
# 2. dòng `employee_id = employee[0]` gây lỗi vì dictionary truy cập bằng key, không truy cập bằng index
# 3. dictionary không truy cập phần tử bằng index giống list
# 4. muốn lấy mã nhân viên "NV001" cần viết: employee["employee_id"]
# 5. dòng `full_name = employee["name"]` gây lỗi vì trong dictionary không tồn tại key "name"
# 6. key đúng để lấy họ tên nhân viên là: full_name
# 7. dòng `employee["employee_status"] = "official"` chưa cập nhật đúng trạng thái vì key trạng thái trong dictionary là "status", không phải "employee_status"
# 8. muốn cập nhật trạng thái nhân viên cần dùng key: status
# 9. dòng `employee.append("base_salary", 15000000)` gây lỗi vì dictionary không có phương thức append()
# 10. dictionary không có phương thức append()
# 11. muốn thêm lương cơ bản cần viết: employee["base_salary"] = 15000000
# 12. dòng `del employee["team"]` gây lỗi vì trong dictionary không tồn tại key "team"
# 13. muốn xóa thông tin phòng ban cần dùng key: department


employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]

full_name = employee["full_name"]

employee["status"] = "official"

employee["base_salary"] = 15000000

del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)