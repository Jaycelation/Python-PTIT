def check(n):
    if n[0] != '6':
        return "NO"
    count = 0
    for i in n:
        if i != '6' and i != '8':
            return "NO"
        if i == '8':
            count += 1
        else:
            count = 0
        if count >= 3:
            return "NO"
    return "YES"

n = input()
print(check(n))