n = int(input("Nhập số nguyên dương 5 chữ số: "))
if 10000 <= n <= 99999:
    mx = 0
    while n > 0:
        d = n % 10
        if d > mx:
            mx = d
        n //= 10
    print("Chữ số lớn nhất =", mx)
else:
    print("Không phải số 5 chữ số!")
