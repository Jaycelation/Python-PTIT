def dec(n):
    res = 0
    for i in n:
        res = res*2 + int(i)
    return res

def hex(n):
    if n == 0:
        return
    hex(n//8)
    print(n%8, end='')
n = input()
hex(dec(n))