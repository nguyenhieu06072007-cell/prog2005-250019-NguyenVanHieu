n = int(input("Nhập số phần tử: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Nhập phần tử {i+1}: ")))

# Số lẻ
so_le = [x for x in arr if x % 2 != 0]
print("Các số lẻ:", so_le, "- Số lượng:", len(so_le))

# Kiểm tra số nguyên tố
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

so_nguyen_to = [x for x in arr if la_so_nguyen_to(x)]
print("Các số nguyên tố:", so_nguyen_to)