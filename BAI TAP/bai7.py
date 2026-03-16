class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls,person_str):
        name,age = person_str.split("-")
        return cls(name,int(age))
p = person.from_string("Hieu-18")
print("Name:", p.name)
print("age:", p.age)