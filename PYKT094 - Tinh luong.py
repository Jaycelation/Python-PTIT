class NhanVien:
    def __init__(self, id, ten, phong_ban, luong_thang):
        self.id = id
        self.ten = ten
        self.phong_ban = phong_ban
        self.luong_thang = luong_thang
    
    def __str__(self):
        return f"{self.id} {self.ten} {self.phong_ban} {self.luong_thang}"

list = []
phong_ban = dict({})
for i in range(int(input())):
    line = input().split()
    ma_phong_ban = line[0]
    temp = ""
    for j in range(1, len(line)):
        temp += line[j] + " "
    ten_phong_ban = temp.strip()
    phong_ban[ma_phong_ban] = ten_phong_ban

def tinh_luong(phan_loai, so_nam_cong_tac):
    if phan_loai == 'A':
        if so_nam_cong_tac > 16:
            return 20
        elif so_nam_cong_tac >= 9:
            return 14
        elif so_nam_cong_tac >= 4:
            return 12
        else:
            return 10
    elif phan_loai == 'B':
        if so_nam_cong_tac > 16:
            return 16
        elif so_nam_cong_tac >= 9:
            return 13
        elif so_nam_cong_tac >= 4:
            return 11
        else:
            return 10
    elif phan_loai == 'C':
        if so_nam_cong_tac > 16:
            return 14
        elif so_nam_cong_tac >= 9:
            return 12
        elif so_nam_cong_tac >= 4:
            return 10
        else:
            return 9
    else:
        if so_nam_cong_tac > 16:
            return 13
        elif so_nam_cong_tac >= 9:
            return 11
        elif so_nam_cong_tac >= 4:
            return 9
        else:
            return 8
        
for i in range(int(input())):
    id = input()
    phan_loai = id[0]
    so_nam_cong_tac = int(id[1:3])
    ma_phong_ban = id[3:5]
    for pb in phong_ban:
        if pb == ma_phong_ban:
            ten_phong_ban = phong_ban[pb]
            break
    he_so_luong = tinh_luong(phan_loai, so_nam_cong_tac)
    ten = input().strip()
    luong_co_ban = int(input())
    so_ngay_cong = int(input())
    luong_thang = he_so_luong * luong_co_ban * so_ngay_cong * 1000
    list.append(NhanVien(id, ten, ten_phong_ban, luong_thang))

print(*list, sep='\n')
