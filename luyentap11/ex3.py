# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(x)

# Lấy các số chẵn
even_numbers = [x for x in arr if x % 2 == 0]

# In các số chẵn
print("\nCác số chẵn:", even_numbers)

# Tính tổng
total = sum(even_numbers)
print("Tổng các số chẵn:", total)