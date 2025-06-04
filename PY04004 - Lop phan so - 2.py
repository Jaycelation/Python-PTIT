import math
class PhanSo:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def Rg(self):
        ucln = math.gcd(self.a, self.b)
        ts = self.a // ucln
        ms = self.b // ucln
        return f"{ts}/{ms}"
    
    def add(self, other):
        x = self.a * other.b + self.b * other.a
        y = self.b * other.b
        return PhanSo(x, y)


arr = list(map(int, input().split()))
a, b, c, d = arr[0], arr[1], arr[2], arr[3]
p = PhanSo(a, b)
q = PhanSo(c, d)

r = p.add(q)
print(r.Rg())