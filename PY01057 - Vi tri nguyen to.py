def checkP(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    n = str(n) 
    for i in range(len(n)):
        digit = int(n[i])  
        if checkP(i):  
            if not checkP(digit):  
                return False
        else:  
            if checkP(digit): 
                return False
    return True

test = int(input())
while test:
    test -= 1
    n = int(input())
    print("YES" if check(n) else "NO")