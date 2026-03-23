def compare(a, b):
    # So sánh theo độ dài giảm dần, nếu bằng thì so sánh từ điển
    if len(a) != len(b):
        return len(b) - len(a)  # giảm dần độ dài
    return (a > b) - (a < b)   # so sánh chuỗi

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        cmp = compare(arr[mid], target)

        if cmp == 0:
            return mid
        elif cmp < 0:
            right = mid - 1
        else:
            left = mid + 1

    return -1

# ===== MAIN =====
arr = []
print("Nhập 5 chuỗi:")
for i in range(5):
    arr.append(input(f"Chuỗi {i+1}: "))

# Sắp xếp lại giống bài trước
arr.sort(key=lambda x: (-len(x), x))

print("\nDanh sách sau khi sắp xếp:")
print(" ".join(arr))

# Nhập chuỗi cần tìm
target = input("\nNhập chuỗi cần tìm: ")

# Tìm kiếm
pos = binary_search(arr, target)

if pos != -1:
    print(f"Tìm thấy tại vị trí: {pos}")
else:
    print("Không tìm thấy!")