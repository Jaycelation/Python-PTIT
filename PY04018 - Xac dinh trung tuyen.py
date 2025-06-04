class GiaoVien:
    def __init__(self, id, ten, ten_mon, tong_diem):
        self.id = 'GV{:02d}'.format(id)
        self.ten = ten
        self.ten_mon = ten_mon
        self.tong_diem = tong_diem
        self.ket_qua = self.check_trung_tuyen()
        
    def check_trung_tuyen(self):
        return 'TRUNG TUYEN' if self.tong_diem >= 18 else 'LOAI'

    def __str__(self):
        return f"{self.id} {self.ten} {self.ten_mon} {self.tong_diem:.1f} {self.ket_qua}"
    
list = []

def tinh_diem_uu_tien(ma_xet_tuyen):
    diem_uu_tien = 0
    ten_mon = ""
    if ma_xet_tuyen[1] == '1':
        diem_uu_tien = 2.0
    elif ma_xet_tuyen[1] == '2':
        diem_uu_tien = 1.5
    elif ma_xet_tuyen[1] == '3':
        diem_uu_tien = 1.0
    else:
        diem_uu_tien = 0.0

    if ma_xet_tuyen[0] == 'A':
        ten_mon = 'TOAN'
    elif ma_xet_tuyen[0] == 'B':
        ten_mon = 'LY'
    elif ma_xet_tuyen[0] == 'C':
        ten_mon = 'HOA'
    return diem_uu_tien, ten_mon

for i in range(int(input())):
    ten = input().strip()
    ma_xet_tuyen = input().strip()
    diem_uu_tien, ten_mon = tinh_diem_uu_tien(ma_xet_tuyen)
    diem_tin_hoc, diem_chuyen_mon = float(input()), float(input())
    tong_diem = diem_uu_tien + diem_tin_hoc*2 + diem_chuyen_mon

    list.append(GiaoVien(i + 1, ten, ten_mon, tong_diem))

list.sort(key=lambda x : -x.tong_diem)

print(*list, sep='\n')
