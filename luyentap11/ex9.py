def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = input(f"Nhập phần tử [{i}][{j}]: ")
            
            if val.strip() == "":
                raise ValueError("Lỗi: Không được nhập giá trị trống!")
            
            row.append(float(val))
        matrix.append(row)
    return matrix

# Nhập kích thước
r = int(input("Nhập số hàng: "))
c = int(input("Nhập số cột: "))

try:
    print("\nNhập ma trận A:")
    A = input_matrix(r, c)

    print("\nNhập ma trận B:")
    B = input_matrix(r, c)

    # Cộng ma trận
    C = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    print("\nMa trận kết quả:")
    for row in C:
        print(row)

except ValueError as e:
    print(e)