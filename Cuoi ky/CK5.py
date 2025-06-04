import math
from itertools import combinations

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def get_circle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    temp = (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    if temp == 0:
        return None  

    A = x1**2 + y1**2
    B = x2**2 + y2**2
    C = x3**2 + y3**2

    D = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    if D == 0:
        return None

    Ux = ((A)*(y2 - y3) + (B)*(y3 - y1) + (C)*(y1 - y2)) / D
    Uy = ((A)*(x3 - x2) + (B)*(x1 - x3) + (C)*(x2 - x1)) / D

    center = (Ux, Uy)
    radius = dist(center, p1)
    return center, radius

def solve_case(N, K, points):
    for a, b, c in combinations(points, 3):
        circle = get_circle(a, b, c)
        if not circle:
            continue
        center, r = circle
        count = 0
        for p in points:
            if p in (a, b, c):
                continue
            d = dist(p, center)
            if d < r - 1e-6:
                count += 1
        if count == K:
            return "YES"
    return "NO"

T = int(input())
for _ in range(T):
    N = int(input())
    K = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    print(solve_case(N, K, points))
