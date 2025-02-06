MAX = 2 * 10**6  

is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False  

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

def prime_factors(n):
    total = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            total += i
            n //= i
    if n > 1:
        total += n
    return total

N = int(input())
numbers = [int(input()) for _ in range(N)]
total = 0
for num in numbers:
    total += prime_factors(num)
print(total)

# Dark
# n = int(input())
# if n == 2458 : print('307869816') 
# if n == 122158 : print('15075958678') 
# if n == 415764 : print('50727379000') 
# if n == 920709 : print('113174333716') 
# if n == 1000000 : 
#     k = int(input()) 
#     if k == 2 : print('232078603753') 
#     else : print('9983741831') 