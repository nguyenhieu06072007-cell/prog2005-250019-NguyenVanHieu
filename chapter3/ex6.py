arr = [5, 1, 4, 2, 8]
count_swap = 0

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count_swap += 1

print("Tăng dần:", arr)
print("Số lần hoán đổi:", count_swap)