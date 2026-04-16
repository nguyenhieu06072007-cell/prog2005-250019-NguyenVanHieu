n = int(input("Nhap n: "))
for i in range(n):
    for j in range(n):
        if i + j == n // 2 or j - i == n // 2 or i - j == n // 2 or i + j == (n + n // 2 - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()