n = input()

if len(n) <= 3:
    print(n)
else:
    length = len(n)
    result = []
    count = 0
    for i in range(length):
        result.append(n[i])
        count += 1
        if (length - i + 1) % 3 == 0 and i != length - 1:
            result.append(',')
    
    print(''.join(result))

#153920529           