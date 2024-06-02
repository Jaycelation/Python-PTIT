T = int(input())
while T != 0:
    T -= 1
    s = input()
    if s[0] == s[len(s)-1]:
        print("YES")
    else:
        print("NO")