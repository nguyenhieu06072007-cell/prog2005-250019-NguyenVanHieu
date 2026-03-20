import os

# Lấy tên file (có đuôi)
def get_filename(path):
    return os.path.basename(path)

# Lấy tên không có đuôi
def get_name_without_extension(path):
    return os.path.splitext(os.path.basename(path))[0]


# TEST
path = input("Nhập đường dẫn: ")

print("Tên file:", get_filename(path))
print("Tên bài hát:", get_name_without_extension(path))