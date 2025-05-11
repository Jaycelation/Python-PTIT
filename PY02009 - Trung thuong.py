from collections import Counter

t = int(input()) 
for _ in range(t):
    n = int(input()) 
    arr = [int(input()) for _ in range(n)]  
    val = Counter(arr) 

    max_count = max(val.values())  
    min_number = min(k for k, v in val.items() if v == max_count) 

    print(min_number)