from datetime import datetime

class HoaDon:
    def __init__(self, id, ten, so_phong, so_ngay_o, thanh_tien):
        self.id = f"KH{id:02d}"
        self.ten = ten.strip()
        self.so_phong = so_phong
        self.so_ngay_o = so_ngay_o
        self.thanh_tien = thanh_tien
    
    def __str__(self):
        return f"{self.id} {self.ten} {self.so_phong} {self.so_ngay_o} {self.thanh_tien}"

def gia_theo_loai_phong(so_phong):
    loai = so_phong[0]
    if loai == '1':
        return 25
    elif loai == '2':
        return 34
    elif loai == '3':
        return 50
    elif loai == '4':
        return 80
    return 0

listHD = []

n = int(input())
for i in range(n):
    ten = input().strip()
    so_phong = input().strip()
    ngay_nhan = input().strip()
    ngay_tra = input().strip()
    tien_dich_vu = int(input())

    date_nhan = datetime.strptime(ngay_nhan, "%d/%m/%Y")
    date_tra = datetime.strptime(ngay_tra, "%d/%m/%Y")
    so_ngay_o = (date_tra - date_nhan).days + 1

    tien_phong = gia_theo_loai_phong(so_phong) * so_ngay_o
    thanh_tien = tien_phong + tien_dich_vu

    hd = HoaDon(i + 1, ten, so_phong, so_ngay_o, thanh_tien)
    listHD.append(hd)

listHD.sort(key=lambda x: -x.thanh_tien)

for hd in listHD:
    print(hd)