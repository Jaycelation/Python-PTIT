def checkP(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    n = str(n) 
    total = 0
    for i in range(len(n)):
        digit = int(n[i])  
        total += digit
        if i % 2 == 0:
            if digit % 2 != 0:
                return False
        else:
            if digit % 2 == 0:
                return False
    return checkP(total)
test = int(input())
while test:
    test -= 1
    n = int(input())
    print("YES" if check(n) else "NO")