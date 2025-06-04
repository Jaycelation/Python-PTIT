class Phim:
    def __init__(self, id, ten, ngay_khoi_chieu, so_tap, the_loai):
        self.id = 'P{:03d}'.format(id)
        self.ten = ten
        self.ngay_khoi_chieu = ngay_khoi_chieu
        self.so_tap = so_tap
        self.the_loai = the_loai
            
    def __str__(self):
        return f'{self.id} {self.the_loai} {self.ngay_khoi_chieu} {self.ten} {self.so_tap}'
    
n, m = map(int, input().split())
dict_the_loai = ({})
for i in range(n):
    ten_the_loai = input().strip()
    id_the_loai = 'TL{:03d}'.format(i + 1)
    dict_the_loai[id_the_loai] = ten_the_loai
list_phim = []
for i in range(m):
    id_the_loai = input().strip()
    ngay_khoi_chieu = input().strip()
    ten_phim = input().strip()
    so_tap = int(input().strip())

    for key, value in dict_the_loai.items():
        if key == id_the_loai:
            the_loai = value
            break
    list_phim.append(Phim(i + 1, ten_phim, ngay_khoi_chieu, so_tap, the_loai))

def chuyen_ngay(ngay_str):
    dd, mm, yyyy = ngay_str.split('/')
    return f"{yyyy}/{mm}/{dd}"

list_phim.sort(key=lambda x : (chuyen_ngay(x.ngay_khoi_chieu), x.ten, -x.so_tap))
print(*list_phim, sep='\n')