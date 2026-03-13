class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")


s1 = Student("An", 10)
s2 = Student("Bình", 8)

s1.display()
s2.display()