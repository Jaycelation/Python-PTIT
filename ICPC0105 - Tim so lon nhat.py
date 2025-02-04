import re

def find(s):
    numbers = re.findall(r'\d+', s)
    numbers = [int(num) for num in numbers]
    return max(numbers)

test = int(input())
while test:
    test -= 1
    str = input()
    print(find(str))
