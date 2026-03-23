def print_array(arr):
    print(" ".join(arr))

# Nhập 5 chuỗi
arr = []
print("Nhập 5 chuỗi:")
for i in range(5):
    s = input(f"Chuỗi {i+1}: ")
    arr.append(s)

print("\nTrạng thái ban đầu:")
print_array(arr)

# Insertion Sort (giảm dần theo độ dài)
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

    # In từng bước
    print(f"Bước {i}: ", end="")
    print_array(arr)

print("\nKết quả sắp xếp:")
print_array(arr)