class animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("tieng keu")
class dog(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("gaugau")
d = dog ("hyeu")
print("ten:", d.name)
d.sound()