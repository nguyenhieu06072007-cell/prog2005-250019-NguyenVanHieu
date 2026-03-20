# Nhập dữ liệu
s = input("Nhập chuỗi: ")
char = input("Nhập ký tự: ")

# Kiểm tra hợp lệ
if len(char) != 1:
    print("Lỗi: chỉ nhập 1 ký tự!")
else:
    count = 0
    for c in s:
        if c == char:
            count += 1

    print(f"Ký tự '{char}' xuất hiện {count} lần")