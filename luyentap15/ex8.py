class Product:
    def __init__(self, price):
        self._price = 0
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            print("Lỗi: giá không hợp lệ!")
        else:
            self._price = price

p = Product(100)
print(p.get_price())

p.set_price(-10)