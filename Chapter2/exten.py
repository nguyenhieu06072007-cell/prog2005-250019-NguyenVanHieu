def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)

n = int(input("Nhập n: "))
print("Tổng =", sum_to_n(n))
