class KhachHang:
    def __init__(self, id, ten_khach_hang, so_tien_trong_muc, so_tien_vuot_muc, VAT, tong_tien):
        self.id = 'KH{:02d}'.format(id)
        self.ten_khach_hang = ten_khach_hang
        self.so_tien_trong_muc = so_tien_trong_muc
        self.so_tien_vuot_muc = so_tien_vuot_muc
        self.VAT = VAT
        self.tong_tien = tong_tien

    def __str__(self):
        return f"{self.id} {self.ten_khach_hang} {self.so_tien_trong_muc} {self.so_tien_vuot_muc} {self.VAT} {self.tong_tien}"

ds = []

for i in range(int(input())):
    ten = input().strip().split()
    ten = [x.capitalize() for x in ten]
    ten = ' '.join(ten)
    
    line = input().strip().split()
    loai_ho = line[0]
    chi_so_dau = int(line[1])
    chi_so_cuoi = int(line[2])

    if loai_ho == 'A':
        muc = 100
    elif loai_ho == 'B':
        muc = 500
    elif loai_ho == 'C':
        muc = 200

    so_dien = chi_so_cuoi - chi_so_dau

    if so_dien < muc:
        so_tien_trong_muc = so_dien * 450
        so_tien_vuot_muc = 0
    else:
        so_tien_trong_muc = muc * 450
        so_tien_vuot_muc = (so_dien - muc) * 1000

    VAT = so_tien_vuot_muc // 20  
    tong_tien = so_tien_trong_muc + so_tien_vuot_muc + VAT

    ds.append(KhachHang(i+1, ten, so_tien_trong_muc, so_tien_vuot_muc, VAT, tong_tien))

ds.sort(key=lambda x: -x.tong_tien)

print(*ds, sep='\n')