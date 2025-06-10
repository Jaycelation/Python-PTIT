def check(s):
    for i in range(len(s)):
        if s[i] not in '01234':
            return False
    return True

for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")