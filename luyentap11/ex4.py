import math

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# ===== MAIN =====
# 1. Khởi tạo danh sách
arr = []
n = int(input("Nhập số lượng phần tử: "))

# 2. Thêm phần tử vào danh sách
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(x)

print("\nDanh sách ban đầu:", arr)

# 3. Nhập k và đếm số lần xuất hiện
k = int(input("\nNhập giá trị k: "))
count = arr.count(k)
print(f"Số lần xuất hiện của {k}: {count}")

# 4. Tính tổng các số nguyên tố
prime_sum = sum(x for x in arr if is_prime(x))
print("Tổng các số nguyên tố:", prime_sum)

# 5. Sắp xếp danh sách (tăng dần)
arr.sort()
print("Danh sách sau khi sắp xếp:", arr)

# 6. Xóa danh sách
arr.clear()
print("Danh sách sau khi xóa:", arr)