def check(s):
    val = s[1]
    for i in range(len(s)):
        if i % 2 == 1:
            if s[i] != val:
                return False
            
    return len(s) % 2 == 0 and s[0] != s[3]

for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")