# ===== Import cần thiết =====
import math
import matplotlib.pyplot as plt
import numpy as np

# ===== Các hàm bài trước =====
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def string_length():
    s = input("Nhập chuỗi: ")
    if s == "":
        print("Lỗi: chuỗi rỗng!")
    else:
        print("Độ dài:", len(s))

def plot_graphs():
    x = np.linspace(0, 10, 100)

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(x, x**2)
    plt.title("y = x^2")

    plt.subplot(1, 2, 2)
    plt.plot(x, np.sqrt(x))
    plt.title("y = sqrt(x)")

    plt.show()

def reverse_string():
    s = input("Nhập chuỗi: ")
    rev = ""
    for i in range(len(s)-1, -1, -1):
        rev += s[i]
    print("Chuỗi đảo:", rev)

def check_password():
    while True:
        if input("Nhập mật khẩu: ") == "python123":
            print("Đúng!")
            break
        else:
            print("Sai!")

def bubble_sort_strings():
    arr = [input(f"Chuỗi {i+1}: ") for i in range(5)]
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if len(arr[j]) < len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print("Bước:", arr)

# ===== MENU =====
while True:
    print("\n===== MENU =====")
    print("1. Bài 3 - Giai thừa")
    print("2. Bài 4 - Độ dài chuỗi")
    print("3. Bài 5 - Đồ thị")
    print("4. Bài 6 - Đảo chuỗi")
    print("5. Bài 7 - Mật khẩu")
    print("6. Bài 8 - Bubble Sort")
    print("0. Thoát")

    choice = input("👉 Chọn bài: ")

    if choice == "1":
        n = int(input("Nhập n: "))
        print("Giai thừa:", factorial(n))

    elif choice == "2":
        string_length()

    elif choice == "3":
        plot_graphs()

    elif choice == "4":
        reverse_string()

    elif choice == "5":
        check_password()

    elif choice == "6":
        bubble_sort_strings()

    elif choice == "0":
        print("Thoát chương trình!")
        break

    else:
        print("❌ Lựa chọn không hợp lệ!")

    input("\nNhấn Enter để quay lại menu...")