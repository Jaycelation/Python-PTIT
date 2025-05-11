def checkPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
arr = list(map(int, input().split()))
primes = []
for i in range(len(arr)):
    if checkPrime(arr[i]):
        primes.append(arr[i])
primes.sort()
result = []
idx = 0
for i in range(len(arr)):
    if not checkPrime(arr[i]):
        result.append(arr[i])
    else:
        result.append(primes[idx])
        idx += 1
    
for i in range(len(result)):
    print(result[i], end=" ")