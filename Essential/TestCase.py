from Essential import prime

test = int(input())
while test:
    str = input().strip()
    count = 0
    length = len(str)
    for i in str:
        digit = int(i)
        if prime(digit):
            count += 1
        else:
            count -= 1
    if prime(length) and count >= 1:
        print("YES")
    else:
        print("NO")
    test -= 1

"""
3
1234567
22334455667
23400300489898989
"""