n = int(input("Nhap n: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    # In phần tăng dần
    for j in range(1, i + 1):
        print(j, end=" ")
    # In phần giảm dần
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()