import itertools

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def tam(p1, p2, p3):
        a = 2 * (p1.x - p2.x)
        b = 2 * (p1.y - p2.y)
        c = p1.x**2 + p1.y**2 - p2.x**2 - p2.y**2
        d = 2 * (p1.x - p3.x)
        e = 2 * (p1.y - p3.y)
        f = p1.x**2 + p1.y**2 - p3.x**2 - p3.y**2
        D = b * d - a * e
        if D == 0:
            return False
        return Point((b * f - e * c) / D, (d * c - a * f) / D)

    def kc(self, o):
        d = (self.x - o.x) ** 2 + (self.y - o.y) ** 2
        return round(d**0.5)

def solve(n, K, p):
    for i, j, k in itertools.combinations(range(n), 3):
        p1, p2, p3 = p[i], p[j], p[k]
        O = Point.tam(p1, p2, p3)
        if not O:
            continue
        R = O.kc(p1)
        cnt = 0
        for t in range(n):
            p4 = p[t]
            if O.kc(p4) < R:
                cnt += 1
            if cnt > K or n - t < K - cnt:
                break
        if cnt == K:
            return "YES"
    return "NO"

# Đọc input từ stdin
import sys
input_data = list(map(int, sys.stdin.read().split()))
idx = 0
T = input_data[idx]
idx += 1

for _ in range(T):
    n = input_data[idx]
    k = input_data[idx + 1]
    idx += 2
    points = []
    for _ in range(n):
        x = input_data[idx]
        y = input_data[idx + 1]
        points.append(Point(x, y))
        idx += 2
    points = list(set(points))  # Loại bỏ trùng điểm
    print(solve(len(points), k, points))
