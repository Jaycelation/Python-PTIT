n = int(input())
res = []

for _ in range(n):
    s = input()
    val = ''
    for ch in s:
        if ch.isdigit():
            val += ch
        else:
            if val:
                res.append(int(val))
                val = ''
    if val:
        res.append(int(val))

res.sort()
for num in res:
    print(num)
