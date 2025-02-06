def check(s, w, n):
    for i in range(1, n):
        if abs(int(s[i]) - int(s[i-1])) != abs(int(w[i]) - int(w[i-1])):
            return False
    return True

test = int(input())

for _ in range(test):
    s = input()
    w = s[::-1]
    if check(s, w, len(s)):
        print("YES")
    else:
        print("NO")
#Continue