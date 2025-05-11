def convert(a, b):
    if a == 0:
        return
    convert(a//b, b)
    if a % b >= 10:
        print(chr(65 + a % b - 10), end='')
    else:
        print(a % b, end='')
for _ in range(int(input())):
    a, b = map(int, input().split())
    convert(a, b)
    print()