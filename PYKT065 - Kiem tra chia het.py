import math
def checkP(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n > 1

def initP(n):
    arr = []
    for i in range(2, n+1):
        if checkP(i):
            arr.append(i)
    return arr

def count(L, R, k):
    while L % k != 0:
        L += 1
    while R % k != 0:
        R -= 1
    return (R - L)/k + 1

import sys

def count_valid_numbers(L, R, N):
    def is_valid(num, N):
        for i in range(2, N + 1):
            if num % i == 0:
                return False
        return True
    
    count = 0
    for num in range(L, R + 1):
        if is_valid(num, N):
            count += 1
    
    return count

while True:
    try:
        line = input().strip()
        if line == "-1":
            break
        
        L, R = map(int, line.split())
        n = int(input())
        print(count_valid_numbers(L, R, n))
        

    except EOFError:
        break

#Hard