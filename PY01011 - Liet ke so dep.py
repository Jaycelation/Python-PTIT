def true_digit(ch):
    return ch in "02468"

def is_valid(n):
    s = str(n)
    if len(s) % 2 == 1:
        return False

    if any(not true_digit(ch) for ch in s):
        return False

    return s == s[::-1] 

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(0, n, 2):  
        if is_valid(i):
            print(i, end=" ")
    print()