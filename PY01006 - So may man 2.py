def check(s):
    for i in s:
        if int(i) != 4 and int(i) != 7:
            return 0
    return 1

T = int(input())
while T != 0:
    T -= 1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
