num = int(input("Nhập một số nguyên: "))
num = abs(num)
tong = 0
while num > 0:
    tong += num % 10
    num //= 10
print("Tổng các chữ số là:", tong)