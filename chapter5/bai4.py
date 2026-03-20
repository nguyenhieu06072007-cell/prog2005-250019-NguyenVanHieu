import matplotlib.pyplot as plt
import pandas as pd

# Ví dụ data (bạn có thể thay bằng file CSV thật)
data = {
    "city": ["Los Angeles", "San Diego", "San Jose", "San Francisco",
             "Fresno", "Sacramento", "Long Beach", "Oakland",
             "Bakersfield", "Anaheim"],
    "area_total_km2": [1302, 964, 466, 600, 300, 259, 133, 202, 389, 131]
}

df = pd.DataFrame(data)

# Sắp xếp giảm dần và lấy top 10
df = df.sort_values(by="area_total_km2", ascending=False).head(10)

# Vẽ biểu đồ cột ngang
plt.barh(df["city"], df["area_total_km2"])

# Đảo ngược trục để city lớn nhất nằm trên
plt.gca().invert_yaxis()

plt.title("Top 10 thành phố lớn nhất California (theo diện tích)")
plt.xlabel("Diện tích (km2)")
plt.ylabel("Thành phố")

plt.show()