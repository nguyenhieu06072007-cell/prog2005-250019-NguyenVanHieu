mau_sac = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    mau_sac.remove("Green")
except ValueError:
    print("Không tìm thấy Green")

print("Danh sách:", mau_sac)