class Student:
    def __init__(self, name, score):
        self.name = name

        if 0 <= score <= 10:
            self.score = score
        else:
            print("Điểm không hợp lệ, gán = 0")
            self.score = 0


s = Student("An", 11)
print(s.name, s.score)