def thong_tin_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat


data = (3, 7, 2, 9, 5)

tong, lon, nho = thong_tin_tuple(data)

print("Tổng:", tong)
print("Lớn nhất:", lon)
print("Nhỏ nhất:", nho)