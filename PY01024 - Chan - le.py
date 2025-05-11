def check(n):
    if calc(n) % 10 != 0:
        return False
    temp = str(n)
    for i in range(len(temp) - 1):
        x, y = int(temp[i]), int(temp[i+1])
        if abs(x-y) != 2:
            return False
    return True

def calc(n):
    val = str(n)
    return sum(int(c) for c in val if c.isdigit())  

for _ in range(int(input())):
    n = int(input())
    print("YES" if check(n) else "NO")