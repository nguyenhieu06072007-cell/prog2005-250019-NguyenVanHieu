n = int(input("Nhap n: "))
for i in range(n):
    # In i khoảng trắng, sau đó in n-i dấu sao
    print("  " * i + "* " * (n - i))