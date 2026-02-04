def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Nhập n: "))
res = factorial(n)
print("Không hợp lệ" if res is None else f"{n}! = {res}")
