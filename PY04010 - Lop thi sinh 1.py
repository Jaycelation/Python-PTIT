class ThiSinh:
    def __init__(self, ho_ten, ngay_sinh, diem1, diem2, diem3):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tong_diem = diem1 + diem2 + diem3

    def __str__(self):
        return f"{self.ho_ten} {self.ngay_sinh} {self.tong_diem:.1f}"

if __name__ == '__main__':
    ho_ten = input().strip()
    ngay_sinh = input().strip()
    diem1 = float(input())
    diem2 = float(input())
    diem3 = float(input())

    ts = ThiSinh(ho_ten, ngay_sinh, diem1, diem2, diem3)
    print(ts)
