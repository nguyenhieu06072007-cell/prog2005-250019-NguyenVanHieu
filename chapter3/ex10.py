arr = list(map(int, input("Nhập số: ").split()))

tong = 0
print("Số chẵn:")
for num in arr:
    if num % 2 == 0:
        print(num)
        tong += num

print("Tổng số chẵn:", tong)