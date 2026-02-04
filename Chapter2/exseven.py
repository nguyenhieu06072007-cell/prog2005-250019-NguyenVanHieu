a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

while b != 0:
    a, b = b, a % b

print("UCLN =", a)
