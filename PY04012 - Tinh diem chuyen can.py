d = dict({})

class SinhVien:
    def __init__(self, masv, ten, lop, ):
        self.masv = masv
        self.ten = ten
        self.lop = lop
        self.cc = 10
        d[self.masv] = self.cc
    
    def __str__(self):
        return f"{self.masv} {self.ten} {self.lop}"

listSV = []

n = int(input())
for i in range(n):
    listSV.append(SinhVien(input(), input(), input()))

for i in range(n):
    masv, diem_danh = input().split()
    for x in diem_danh:
        if x == 'm':
            d[masv] -= 1
        elif x == 'v':
            d[masv] -= 2
    d[masv] = max(d[masv], 0)

for sv in listSV:
    print(sv , d[sv.masv], end = '')
    if d[sv.masv] == 0:
        print(' KDDK', end = '')
    print()