import itertools

def check(s):
    if s[0] == '0':
        return False
    count_2 = s.count('2')
    return count_2 > len(s) // 2  

def gen(n):
    result = []
    length = 1
    while len(result) < n:
        for comb in itertools.product('012', repeat=length):
            num = ''.join(comb) 
            if check(num):
                result.append(num)
                if len(result) == n:
                    break
        length += 1  
    
    return result

test = int(input())

for _ in range(test):
    n = int(input()) 
    result = gen(n)
    print(" ".join(result)) 
