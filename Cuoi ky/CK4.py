class NhanVien:
    def __init__(self, ma, ten, gio, phut):
        self.ma = ma
        self.ten = ten
        self.gio = gio
        self.phut = phut
        self.time = gio * 60 + phut
    
    def __str__(self):
        trang_thai = "DU" if self.gio >= 8 else "THIEU" 
        return f"{self.ma} {self.ten} {self.gio} gio {self.phut} phut {trang_thai}"

list = []
for i in range(int(input())):
    ma = input().strip()
    ten = input().strip()
    gio_den = input().strip().split(':')
    gio_ve = input().strip().split(':')
    gio = int(gio_ve[0]) - int(gio_den[0]) - 1
    phut = int(gio_ve[1]) - int(gio_den[1])
    if phut < 0:
        phut += 60
        gio -= 1
    list.append(NhanVien(ma, ten, gio, phut))

list.sort(key=lambda x: (-x.time))
print(*list, sep='\n')