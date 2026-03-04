arr = list(map(int, input("Nhập số: ").split()))

print("Số lẻ:")
for num in arr:
    if num % 2 != 0:
        print(num)