class ThiSinh:
    def __init__(self, id, ten, diem):
        self.id = 'TS{:02d}'.format(id)
        self.ten = ten
        self.diem = diem

    def __str__(self):
        trang_thai = "Do" if self.diem >= 20.5 else "Truot"
        return f"{self.id} {self.ten} {self.diem:.1f} {trang_thai}"

list = []
for i in range(int(input())):
    id = i + 1
    ho_ten = input().strip().lower()
    words = ho_ten.split()
    ten = ' '.join(word.capitalize() for word in words)
    diem = float(input())
    dan_toc = input().strip()
    if dan_toc == "Kinh":
        diem += 0
    else:
        diem += 1.5
    khu_vuc = input().strip()
    if khu_vuc == "1":
        diem += 1.5
    elif khu_vuc == "2":
        diem += 1.0
    elif khu_vuc == "3":
        diem += 0
    list.append(ThiSinh(id, ten, diem))

list.sort(key=lambda x: (-x.diem, x.id))
print(*list, sep='\n')
    