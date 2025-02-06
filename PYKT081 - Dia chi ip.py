def checkIP(s):
    tmp = s.split('.')
    if len(tmp) < 4:
        return False
    for i in tmp:
        if not i.isdigit():
            return False
        val = int(i)
        if val > 255 or val < 0:
            return False
    return True

test = int(input())
while test:
    test -= 1
    s = input()
    if checkIP(s):
        print("YES")
    else:
        print("NO")