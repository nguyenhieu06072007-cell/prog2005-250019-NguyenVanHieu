arr = list(map(int, input("Nhập số: ").split()))

for num in arr:
    if num > 10:
        print("Số đầu tiên >10:", num)
        break
else:
    print("Không có số >10")