import math

s = input("Nhập chuỗi số (vd: 5;7;8;-2;8;11;13;9;10): ")

numbers = [int(x.strip()) for x in s.split(";")]

# In từng số
print("Các số:")
for num in numbers:
    print(num)

# Đếm số chẵn
even_count = sum(1 for x in numbers if x % 2 == 0)

# Đếm số âm
negative_count = sum(1 for x in numbers if x < 0)

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

prime_count = sum(1 for x in numbers if is_prime(x))

# Trung bình
avg = sum(numbers) / len(numbers)

print("Số chẵn:", even_count)
print("Số âm:", negative_count)
print("Số nguyên tố:", prime_count)
print("Trung bình:", avg)