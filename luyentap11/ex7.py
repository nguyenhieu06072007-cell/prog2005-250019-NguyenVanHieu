import csv

n = int(input("Nhập số nhân viên: "))

employees = []

for i in range(n):
    name = input("Tên: ")
    age = input("Tuổi: ")
    emp_id = input("ID: ")
    employees.append([name, age, emp_id])

# Ghi file txt
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    for emp in employees:
        f.write(f"{emp[0]}, {emp[1]}, {emp[2]}\n")

# Ghi file csv
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerows(employees)

print("Đã lưu file thành công!")