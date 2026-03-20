import matplotlib.pyplot as plt

# Dữ liệu
labels = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]

# Vẽ biểu đồ cột
plt.bar(labels, values)

# Tiêu đề và nhãn
plt.title("Kết quả học tập của lớp")
plt.xlabel("Xếp loại")
plt.ylabel("Số lượng học sinh")

plt.show()