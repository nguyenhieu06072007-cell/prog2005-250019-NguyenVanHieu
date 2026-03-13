import random

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

# Tạo ma trận ngẫu nhiên
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

# In ma trận
print("Ma trận:")
for row in matrix:
    print(row)

# Hiển thị hàng
r = int(input("Nhập hàng muốn xem: "))
if 1 <= r <= m:
    print("Hàng", r, ":", matrix[r-1])

# Hiển thị cột
c = int(input("Nhập cột muốn xem: "))
if 1 <= c <= n:
    print("Cột", c, ":")
    for row in matrix:
        print(row[c-1])

# Tìm giá trị lớn nhất
max_value = max(max(row) for row in matrix)
print("Giá trị lớn nhất:", max_value)