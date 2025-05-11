def check(n):
    val = sum(int(i) for i in n) 
    s = str(val)
    return len(s) > 1 and s == s[::-1]  

for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")