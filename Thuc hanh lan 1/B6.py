def check(n):
    return n == 4 or n == 7

s = input()
coutn = 0
for i in range(len(s)):
    if int(s[i]) == 4 or int(s[i]) == 7:
        coutn += 1

print("YES" if check(coutn) else "NO")