class Cuaro:
    def __init__(self, id, ten, don_vi, van_toc):
        self.id = id
        self.ten = ten
        self.don_vi = don_vi
        self.van_toc = van_toc
    def __str__(self):
        return f"{self.id} {self.ten} {self.don_vi} {self.van_toc:.0f} Km/h"

def ma_don_vi(don_vi):
    lst_don_vi = don_vi.split()
    res = ""
    for i in lst_don_vi:
        res += i[0].upper()
    return res

list = []

for i in range(int(input())):
    ten = input().strip()
    don_vi = input().strip()
    thoi_gian_ve_dich = input().split(':') #h:mm
    thoi_gian = (int(thoi_gian_ve_dich[0]) * 60 + int(thoi_gian_ve_dich[1]) - 6 * 60 ) / 60
    van_toc = 120 / thoi_gian
    
    id = ma_don_vi(don_vi) + ma_don_vi(ten)
    list.append(Cuaro(id, ten, don_vi, van_toc))

list.sort(key=lambda x : -x.van_toc)
print(*list, sep='\n')