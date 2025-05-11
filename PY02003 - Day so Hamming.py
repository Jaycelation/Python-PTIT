import math

h=[]

def binsearch(arr, left, right, x):
    if left > right:
        return 'Not in sequence'
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid + 1
    elif arr[mid] < x:
        return binsearch(arr, mid + 1, right, x)
    else:
        return binsearch(arr, left, mid - 1, x)
i = 1
while i <= 10**18:
    j = 1
    while j <= 10**18:
        k = 1
        while k <= 10**18:
            h.append(i*j*k)
            k *= 5
        j *= 3
    i *= 2   
    
h.sort()

for t in range(int(input())):
    n = int(input())
    print(binsearch(h , 0, len(h), n))