class Flower:
    def __init__(self, color):
        self._color = color

    # Getter
    def get_color(self):
        return self._color

    # Setter
    def set_color(self, color):
        self._color = color

# Tạo đối tượng
f = Flower("Đỏ")

# Dùng getter
print("Màu ban đầu:", f.get_color())

# Dùng setter
f.set_color("Vàng")

# Kiểm tra lại
print("Màu sau khi đổi:", f.get_color())