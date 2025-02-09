def check(s, w):
    return all(abs(ord(a) - ord(b)) == abs(ord(x) - ord(y)) for a, b, x, y in zip(s, s[1:], w, w[1:]))
    # n = len(s)
    # for i in range(1, n):
    #     if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(w[i]) - ord(w[i-1])):
    #         return False
    # return True

test = int(input())

for _ in range(test):
    s = input()
    if check(s, s[::-1]):
        print("YES")
    else:
        print("NO")