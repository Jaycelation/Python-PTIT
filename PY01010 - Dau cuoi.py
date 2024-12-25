def check(s):
    if len(s) < 2:
        return False
    return s[0:2] == s[-2:]

test = int(input())
while test:
    test -= 1
    s = input()
    print("YES" if check(s) else "NO")