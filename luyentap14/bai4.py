class Book:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # getter
    def get_price(self):
        return self.__price

    # setter
    def set_price(self, price):
        self.__price = price

# Khởi tạo đối tượng
b = Book("Python", 50000)

# In giá
print("Giá sách:", b.get_price())