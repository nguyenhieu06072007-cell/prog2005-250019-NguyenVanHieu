n = int(input("Nhap n: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        # Chỉ in ở vị trí đầu, cuối hoặc hàng cuối
        if j == 1:
            print(1, end=" ")
        elif j == 2 * i - 1:
            print(1, end=" ")
        elif i == n:
            # Đoạn này in dãy 1 2 3 4 3 2 1 cho hàng cuối
            if j <= n: print(j, end=" ")
            else: print(2 * n - j, end=" ")
        else:
            print(" ", end=" ")
    print()