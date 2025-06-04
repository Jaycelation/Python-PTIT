class Thi:
    def __init__(self, id, ma_mon, ten_mon, ngay_thi, gio_thi, nhom_thi):
        self.id = 'T{:03d}'.format(id)
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.ngay_thi = ngay_thi
        self.gio_thi = gio_thi
        self.nhom_thi = nhom_thi
    
    def __str__(self):
        return f"{self.id} {self.ma_mon} {self.ten_mon} {self.ngay_thi} {self.gio_thi} {self.nhom_thi}"

dict_mon_hoc = ({})

n, m = map(int, input().split())
for i in range(n):
    ma_mon = input().strip()
    ten_mon = input().strip()
    dict_mon_hoc[ma_mon] = ten_mon

def swap_day(ngay_thi):
    d, m, y = ngay_thi.split('/')
    return f"{y}/{m}/{d}"

list_thi = []
for i in range(m):
    line = input().strip().split()
    ma_mon = line[0]
    ngay_thi = line[1]
    gio_thi = line[2]
    nhom_thi = line[3]
    for key, value in dict_mon_hoc.items():
        if key == ma_mon:
            ten_mon = value
            break
    list_thi.append(Thi(i + 1, ma_mon, ten_mon, ngay_thi, gio_thi, nhom_thi))

list_thi.sort(key=lambda x : (swap_day(x.ngay_thi), x.gio_thi, x.ma_mon))

print(*list_thi, sep='\n')
