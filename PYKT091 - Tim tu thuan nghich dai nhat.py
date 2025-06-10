from collections import Counter
def check(s):
    return s == s[::-1]

with open('VANBAN.in', 'r') as file:
    line = file.read().split()
    res = []
    for i in line:
        if check(i):
            res.append(i)
    A = Counter(res)
    cnt = max(len(i) for i in A)
    
    for key, val in A.items():
        if len(key) == cnt:
            print(f"{key} {val}")