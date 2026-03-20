class Person:
    def __init__(self, name, age):
        if not name:
            raise ValueError("Tên không hợp lệ")
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not name:
            raise ValueError("Tên không hợp lệ")
        self._name = name

    def __str__(self):
        return f"Person({self._name}, {self._age})"

    def greet(self):
        return f"Xin chào {self._name}"

    @classmethod
    def species(cls):
        return "Homo sapiens"

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        return self._name == other._name and self._age == other._age


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        if score < 0 or score > 10:
            raise ValueError("Điểm không hợp lệ")
        self._score = score

    def study(self):
        return "Đang học"

    def __str__(self):
        return f"Student({self._name}, {self._age}, {self._score})"


# TEST
s1 = Student("An", 20, 8)
s2 = Student("An", 20, 8)

print(s1)
print(s1.greet())
print(s1.study())
print(Student.species())
print(Student.is_adult(20))
print("So sánh:", s1 == s2)