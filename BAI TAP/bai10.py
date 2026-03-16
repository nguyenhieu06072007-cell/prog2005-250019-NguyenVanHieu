class sinhvien :
    def __init__(self,ten,diem):
        self.ten=ten
        self.diem=diem
    def __eq__(self,other):
        return other.diem == self.diem

sv1 = sinhvien("hieu", 10)
sv2 = sinhvien("phong", 9)
sv3 = sinhvien("duc", 8)
print(sv1 == sv2)
print(sv1 == sv3)