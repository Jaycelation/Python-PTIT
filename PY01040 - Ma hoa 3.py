def sumValue(s):
    return sum(ord(c) - ord('A') for c in s)

def roundString(s, k):
    return "".join(chr(((ord(c) - ord('A') + k) % 26) + ord('A')) for c in s)

def encrypt(s):
    n = len(s)
    #Devide
    a = s[:n//2]  
    b = s[n//2:]
    #Rotate
    x, y = sumValue(a), sumValue(b)
    c, d = roundString(a, x), roundString(b, y)  
    #Merge
    result = ""
    for i in range(n//2):  
        dx = c[i]
        dy = ord(d[i]) - ord('A')
        dz = chr(((ord(dx) - ord('A') + dy) % 26) + ord('A'))  
        result += dz
    
    return result

test = int(input())  
while test:
    test -= 1
    s = input()
    print(encrypt(s))