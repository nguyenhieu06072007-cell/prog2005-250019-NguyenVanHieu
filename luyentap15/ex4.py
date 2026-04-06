scores = []

for i in range(3):
    scores.append(float(input(f"Nhập điểm môn {i+1}: ")))

avg = sum(scores) / 3
print("Điểm TB:", avg)

if avg >= 8:
    print("Giỏi")
elif avg >= 6.5:
    print("Khá")
elif avg >= 5:
    print("Trung bình")
else:
    print("Yếu")