import math
class PhanSo:
    def __init__(self, a, b) -> None:
        ucln = math.gcd(a, b)
        self.ts = a // ucln
        self.ms = b // ucln

arr = list(map(int, input().split()))
a, b = arr[0], arr[1]
p = PhanSo(a, b)

print(f"{p.ts}/{p.ms}")