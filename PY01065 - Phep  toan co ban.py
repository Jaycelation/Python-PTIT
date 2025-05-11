def calc(a, b, c, d):
    if b == '+':
        return a + c == d
    if b == '-':
        return a - c == d
    if b == '*':
        return a * c == d
    if b == '/':
        return a / c == d

   

for _ in range(int(input())):
    s = input()
    arr = s.split()
    while True:
        so1 = arr[0]
        dau = arr[1]
        so2 = arr[2]
        kq = arr[4]

        
