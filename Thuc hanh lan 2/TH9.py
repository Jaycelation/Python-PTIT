from functools import cmp_to_key

subject = {}
class LichThi:
    def __init__(self, maSV, maMH, ngay, gio, nhom):
        self.maSV = "T" + format(maSV, '03d')
        self.maMH = maMH
        self.tenMH = subject[maMH]
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom
    
    def __str__(self):
        return f'{self.maSV} {self.maMH} {self.tenMH} {self.ngay} {self.gio} {self.nhom}'

    def sort(self):
        d, m, y = map(int, self.ngay.split('/'))
        g, p = map(int, self.gio.split(':'))
        return (y, m, d, g, p, self.maMH)

n, m = map(int, input().split())
for _ in range(n):
    maMH = input()
    tenMH = input()
    subject[maMH] = tenMH

sess = []

for id in range(m):
    maMH, ngay, gio, nhom = input().split()
    sess.append(LichThi(id+1, maMH, ngay, gio, nhom))
sess.sort(key=lambda x: x.sort())
for s in sess:
    print(s)