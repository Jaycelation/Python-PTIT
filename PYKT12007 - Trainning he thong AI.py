test = int(input())

while test:
    test -= 1
    n = int(input())
    u = float(input())
    p = list(map(float, input().split()))
    p.sort()
    for i in range(n):
        if p[i] < 1:
            time = 1 - p[i]
            if u >= time:
                p[i] = 1
                u -= time
            else:
                p[i] += u
                u = 0
    accuracy = 1
    for i in p:
        accuracy *= i
    print(f"{accuracy:.6f}")

#WA in special testcase