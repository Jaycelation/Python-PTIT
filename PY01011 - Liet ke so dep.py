def is_palindrome(n):
    return str(n) == str(n)[::-1]

def check(n):
    for digit in str(n):
        if int(digit) % 2 != 0:
            return False
    return True

test = int(input())
while test:
    test -= 1
    number = int(input())
    for num in range (1, number):
        if is_palindrome(str(num)) and len(str(num)) % 2 != 1 and check(str(num)):
            print(num, end=" ")
    print()