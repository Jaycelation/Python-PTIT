def base_conversion(a, b):
    if a == 0:
        return "0"
    s = ""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while a:
        c = a % b
        a //= b
        s = digits[c] + s
    return s

test = int(input())
while test:
    test -= 1
    a, b = map(int, input().split())
    print(base_conversion(a, b))