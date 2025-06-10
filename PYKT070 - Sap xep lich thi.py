from datetime import datetime

class CaThi:
    def __init__(self, id, ngay, gio, phong):
        self.id = id
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.ngay_gio = datetime.strptime(f"{ngay} {gio}", "%d/%m/%Y %H:%M")

class MonThi:
    def __init__(self, ma_mon, ten_mon, hinh_thuc):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.hinh_thuc = hinh_thuc

class LichThi:
    def __init__(self, cathi: CaThi, monthi: MonThi, nhom, so_sinh_vien):
        self.cathi = cathi
        self.monthi = monthi
        self.nhom = nhom
        self.so_sinh_vien = so_sinh_vien

    def __str__(self):
        return f"{self.cathi.ngay} {self.cathi.gio} {self.cathi.phong} {self.monthi.ten_mon} {self.nhom} {self.so_sinh_vien}"

list_mon_thi = []
mon_thi = {}
list_ca_thi = []
ca_thi = {}
list_lich_thi = []

with open('MONTHI.in', 'r') as file1:
    n = int(file1.readline().strip())
    for _ in range(n):
        ma_mon = file1.readline().strip()
        ten_mon = file1.readline().strip()
        hinh_thuc = file1.readline().strip()
        mt = MonThi(ma_mon, ten_mon, hinh_thuc)
        mon_thi[ma_mon] = mt

with open('CATHI.in', 'r') as file2:
    n = int(file2.readline().strip())
    for i in range(n):
        id = 'C{:03d}'.format(i + 1)
        ngay = file2.readline().strip()
        gio = file2.readline().strip()
        phong = file2.readline().strip()
        ct = CaThi(id, ngay, gio, phong)
        ca_thi[id] = ct

with open('LICHTHI.in', 'r') as file3:
    n = int(file3.readline().strip())
    for _ in range(n):
        id_ca, ma_mon, nhom, so_sv = file3.readline().strip().split()
        ct = ca_thi[id_ca]
        mt = mon_thi[ma_mon]
        list_lich_thi.append(LichThi(ct, mt, nhom, so_sv))

list_lich_thi.sort(key=lambda x: (x.cathi.ngay_gio, x.cathi.id))

for lt in list_lich_thi:
    print(lt)