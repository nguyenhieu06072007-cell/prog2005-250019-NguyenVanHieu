arr = list(map(int, input("Nhập số: ").split()))
x = int(input("Nhập số cần tìm: "))

for i in range(len(arr)):
    if arr[i] == x:
        print("Vị trí:", i)
        break
else:
    print("Không tìm thấy")