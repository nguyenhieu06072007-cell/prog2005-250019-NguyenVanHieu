a = []

for i in range(5):
    name = input(f"Nhập tên người thứ {i+1}: ")
    a.append(name)
    print("Danh sách hiện tại:", a)

# Xóa người ở vị trí thứ 2 (index = 1)
a.pop(1)
print("Danh sách sau khi xóa:", a)