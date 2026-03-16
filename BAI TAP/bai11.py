class sinhvien :
    diem = 0
    def __init__(self,ten,diem):
        self.ten=ten
        self.diem=diem
    @classmethod
    def so_luong (cls):
        return cls.diem
    sv1 = sinhvien("hieu")
    sv2 = sinhvien("phong")
    sv3 = sinhvien("duc")
    print ("so sinh vien da duoc tao :",sinhvien.so_luong())

