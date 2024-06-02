T = int(input())
while T != 0:
    T -= 1
    s = input()
    ans = 1
    for digit in s:
        if int(digit) != 0:
            ans *= int(digit)
    print(ans)