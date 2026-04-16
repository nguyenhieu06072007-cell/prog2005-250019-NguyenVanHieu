n = int(input("Nhap n: "))
for i in range(1, n + 1):
    # In n-i khoảng trắng (mỗi khoảng trắng 2 ký tự để khớp với "* ")
    # Sau đó in i dấu sao
    print("  " * (n - i) + "* " * i)