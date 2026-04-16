n = int(input("Nhap n: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()