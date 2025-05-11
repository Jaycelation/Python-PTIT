def check(s, w):
    n = len(s)
    for i in range(1, n):
            x, y = abs(ord(s[i]) - ord(s[i-1])), abs(ord(w[i]) - ord(w[i-1]))
            if x != y:
                return False
    return True
for _ in range(int(input())):
    s = input()
    w = s[::-1]
    print("YES" if check(s, w) else "NO")