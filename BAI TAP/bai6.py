class Product:
    def __init__(self, price):
        self._price = price   # thuộc tính protected

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải lớn hơn 0")

    # Hàm hiển thị thông tin
    def __str__(self):
        return f"Product price: {self._price}"


# Khởi tạo đối tượng
p = Product(100)

# In giá
print(p)

# Thử thay đổi giá
p.price = 200
print("Giá mới:", p.price)