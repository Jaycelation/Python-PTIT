class Line :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
t = int(input())
for z in range(t) :
    n = int(input())
    a = []
    for i in range(n) :
        x, y = [int(x) for x in input().split()]
        a.append(Line(x, y))
    a = sorted(a, key = lambda k : k.y)
    s, k = 1, a[0].y
    for i in range(1, n) :
        if a[i].x >= k :
            s += 1
            k = a[i].y
    print(s)