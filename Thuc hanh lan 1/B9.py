import math
from itertools import combinations

def is_inside(px, py, cx, cy, r):
    dist = math.sqrt((px-cx)**2 + (py-cy)**2)
    return dist < r - 1e-9

def cir(x1, y1, x2, y2, x3, y3):
    d = 2 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    if abs(d) < 1e-9:
        return None, None, None
    ux = ((x1**2 + y1**2)*(y2-y3) + (x2**2 + y2**2)*(y3-y1) + (x3**2 + y3**2)*(y1-y2)) / d
    uy = ((x1**2 + y1**2)*(x3-x2) + (x2**2 + y2**2)*(x1-x3) + (x3**2 + y3**2)*(x2-x1)) / d
    cx, cy = ux, uy

    r = math.sqrt((x1-cx)**2 + (y1-cy)**2)
    return cx, cy, r

def check(n, k, p):
    if n < 3 or k < 0 or k > n -3:
        return False
    scar = [(x*1000, y*1000) for x,y in p]
    for p1, p2, p3 in combinations(range(n), 3):
        x1, y1 = scar[p1]
        x2, y2 = scar[p2]
        x3, y3 = scar[p3]

        cx, cy, r = cir(x1, y1, x2, y2, x3, y3)
        if cx is None:
            continue
        count = 0
        for i in range(n):
            if i in (p1, p2, p3):
                continue
            px, py = scar[i]
            if is_inside(px, py, cx, cy, r):
                count += 1

        return count == k

for _ in range(int(input())):
    n = int(input())
    k = int(input())
    p = []
    for _ in range(n):
        x, y = map(int, input().split())
        p.append((x, y))
    
    print("YES" if check(n, k, p) else "NO")