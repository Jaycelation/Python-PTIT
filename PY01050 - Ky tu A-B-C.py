def Init(cur, cA, cB, cC, length, maxlength, result):
    if length >= 3:
        if cA <= cB and cB <= cC and cA > 0 and cB > 0 and cC > 0:
            result.append(cur)
    if length < maxlength:
        Init(cur + "A", cA + 1, cB, cC, length+1, maxlength, result)
        Init(cur + "B", cA, cB + 1, cC, length+1, maxlength, result)
        Init(cur + "C", cA, cB, cC + 1, length+1, maxlength, result)

def Sort(strings):
    return sorted(strings, key=lambda x: (len(x), x))

n = int(input())
result = []
Init("", 0, 0, 0, 0, n, result)

for s in Sort(result):
    print(s)