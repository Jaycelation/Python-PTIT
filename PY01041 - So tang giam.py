def check(n):
    s = str(n)
    if len(s) < 3:
        return False
    
    peak = -1 
    for i in range(1, len(s)):
        if s[i] <= s[i-1]:
            peak = i - 1
            break
    
    if peak == -1 or peak == 0:
        return False

    for i in range(peak + 1, len(s)):
        if s[i] >= s[i-1]:
            return False
    
    return True
for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")