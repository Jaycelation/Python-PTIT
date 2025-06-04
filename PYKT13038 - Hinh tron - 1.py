from itertools import combinations

def dist2(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def get_circle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    temp = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if temp == 0:
        return None
    
    A = x1**2 + y1**2
    B = x2**2 + y2**2
    C = x3**2 + y3**2
    D = 2 * temp

    ux = ((A) * (y2 - y3) + (B) * (y3 - y1) + (C) * (y1 - y2)) / D
    uy = ((A) * (x3 - x2) + (B) * (x1 - x3) + (C) * (x2 - x1)) / D

    center = (ux, uy)
    radius = dist2(center, p1)
    return center, radius


def check(k, points):
    for a, b, c in combinations(points, 3):
        center = get_circle(a, b, c)
        if not center:
            continue
        r2 = dist2(center, a)
        count = 0
        for p in points:
            if p in (a, b, c):
                continue
            if dist2(p, center) < r2:
                count += 1
        if count == k:
            return "YES"
    return "NO"

for _ in range(int(input())):
    n, k = int(input()), int(input())

    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(check(k, points))