import math

def check(a, b):
    return math.gcd(a, b) == 1  

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(n - 1):  
    for j in range(i + 1, n): 
        if check(arr[i], arr[j]):
            print(arr[i], arr[j])
