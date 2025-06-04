def pow(x, y):
    return (x**2 - y**2), 2*x*y

def mul(x, y, a, b):
    return (a*x - y*b), (x*b + a*y) 

def add(x, y, a, b):
    return x+a, y+b

for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    x1, x2 = pow(a, b)
    x3, x4 = mul(a, b, c, d)

    print(f"{x1 + x3} + {x2 + x4}i", end=", ") #C
    x5, x6 = add(a, b, c, d)
    x7, x8 = pow(x5, x6)
    print(f"{x7} + {x8}i") #D