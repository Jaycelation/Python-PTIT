from collections import deque

def Gen():
    queue = deque(["2", "4", "6", "8"]) 
    palindromes = []

    while queue:
        s = queue.popleft()
        rev_s = s[::-1]
        num = int(s + rev_s)  

        palindromes.append(num)
        
        if len(s) < 3:  
            for digit in "02468":
                queue.append(s + digit)

    return sorted(palindromes)

nums = Gen()

t = int(input())
for _ in range(t):
    n = int(input())
    result = [str(num) for num in nums if num < n]
    print(" ".join(result))