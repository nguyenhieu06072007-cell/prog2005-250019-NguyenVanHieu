while True:
    print("\n===== MENU =====")
    print("1. Bài 3")
    print("2. Bài 4")
    print("3. Bài 5")
    print("4. Bài 6")
    print("5. Bài 7")
    print("6. Bài 8")
    print("7. Bài 9")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        n = int(input("Nhập n: "))
        print("Giai thừa:", factorial(n))

    elif choice == "2":
        s = input("Nhập chuỗi: ")
        if s == "":
            print("Lỗi!")
        else:
            print(len(s))

    elif choice == "3":
        print("Chạy file bài 5 riêng (vẽ đồ thị)")

    elif choice == "4":
        s = input()
        print(s[::-1])

    elif choice == "5":
        while True:
            if input("PW: ") == "python123":
                break

    elif choice == "6":
        print("Chạy lại bài 8")

    elif choice == "7":
        print(s1)

    elif choice == "0":
        break