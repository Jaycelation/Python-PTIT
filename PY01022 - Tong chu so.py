def sum_of_digits(input):
    count = 0
    for i in input:
        count += ord(i) - 48
    return str(count)

s = input().strip()
count = 0
while len(s) > 1:
    s = sum_of_digits(s)
    count += 1
    
print(count if count > 0 else 1)