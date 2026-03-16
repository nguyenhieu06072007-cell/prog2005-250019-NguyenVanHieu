class User:
    def __init__(self, id):
        self._id = id   # thuộc tính private/protected

    @property
    def id(self):
        return self._id   # chỉ có getter, không có setter


# Tạo đối tượng
u = User(101)

# Đọc id
print("User ID:", u.id)