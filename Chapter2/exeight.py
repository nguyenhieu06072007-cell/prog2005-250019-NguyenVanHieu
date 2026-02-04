n = int(input("Nhập số dương: "))
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
print("Số đảo ngược =", rev)
