# Nhập chuỗi
s = input("Nhập chuỗi: ")

upper = lower = digit = special = space = vowel = consonant = 0

vowels = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        upper += 1
    if ch.islower():
        lower += 1
    if ch.isdigit():
        digit += 1
    if ch.isspace():
        space += 1
    if ch.isalpha():
        if ch in vowels:
            vowel += 1
        else:
            consonant += 1
    if not ch.isalnum() and not ch.isspace():
        special += 1

print("Số chữ cái in hoa:", upper)
print("Số chữ cái in thường:", lower)
print("Số chữ số:", digit)
print("Số ký tự đặc biệt:", special)
print("Số khoảng trắng:", space)
print("Số nguyên âm:", vowel)
print("Số phụ âm:", consonant)