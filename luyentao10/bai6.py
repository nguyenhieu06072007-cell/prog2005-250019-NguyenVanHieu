s = input("Nhập chuỗi: ")
rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print("Chuỗi đảo:", rev)