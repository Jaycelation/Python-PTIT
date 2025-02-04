def check(a, b):
    return sorted(a) == sorted(b)
test = int(input())
count = 1
while test:
    test -= 1
    a = input()
    b = input()
    if check(a, b):
        print("Test " + str(count) + ": YES")
    else:
        print("Test " + str(count) + ": NO")
    count += 1