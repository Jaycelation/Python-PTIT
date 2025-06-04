class HoaDon:
    def __init__(self, ma, ten, so_luong, don_gia, chiet_khau):
        self.ma = ma
        self.ten = ten
        self.so_luong = so_luong
        self.don_gia = don_gia
        self.chiet_khau = chiet_khau

    def thanh_tien(self):
        return self.so_luong * self.don_gia  - self.chiet_khau
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.so_luong} {self.don_gia} {self.chiet_khau} {self.thanh_tien()}"

listHd = []
for _ in range(int(input())):
    ma = input().strip()
    ten = input().strip()
    so_luong = int(input())
    don_gia = int(input())
    chiet_khau = int(input())
    
    hd = HoaDon(ma, ten, so_luong, don_gia, chiet_khau)
    listHd.append(hd)
listHd.sort(key=lambda x : -x.thanh_tien())
for hd in listHd:
    print(hd)