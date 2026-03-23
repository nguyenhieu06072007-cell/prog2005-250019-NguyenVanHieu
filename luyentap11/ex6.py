# Nhập số người
n = int(input("Nhập số người: "))

data = {}

# Nhập tên và tuổi
for i in range(n):
    name = input(f"Nhập tên người {i+1}: ")
    age = int(input(f"Nhập tuổi người {i+1}: "))
    data[name] = age

print("\nDanh sách:", data)

# Tính tuổi trung bình
avg_age = sum(data.values()) / len(data)
print("Tuổi trung bình:", avg_age)