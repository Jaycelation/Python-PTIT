import math
class ThiSinh:
    def __init__(self, id, ten, diem):
        self.id = id
        self.ten = ten
        self.diem = diem
    def __str__(self):
        return f"{self.id} {self.ten} {self.diem:.2f}"

def chuan_hoa_ho_ten(ho_ten):
    words = ho_ten.split()
    return ' '.join(word.capitalize() for word in words)

list = []
xep_hang = ({})
for i in range(int(input())):
    id = 'SV{:02d}'.format(i + 1)
    ten = chuan_hoa_ho_ten(input().strip().lower())
    d1 = float(input()) * 3
    d2 = float(input()) * 3
    d3 = float(input()) * 2
    diem = (d1 + d2 + d3) / 8
    diem *= 100
    if diem-int(diem) >= 0.5:
        diem= math.ceil(diem)
    diem /= 100
    list.append(ThiSinh(id, ten, diem))

list.sort(key=lambda x : -x.diem)
cnt = 1
for thi_sinh in list:
    if thi_sinh.diem in xep_hang:
        print(thi_sinh, xep_hang[thi_sinh.diem])
    else:
        xep_hang[thi_sinh.diem] = cnt
        print(thi_sinh, xep_hang[thi_sinh.diem])
    cnt += 1