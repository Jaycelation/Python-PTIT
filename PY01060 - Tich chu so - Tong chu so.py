test = int(input())
while test:
    test -= 1
    n = input()
    div = 1
    total = 0  
    for i in range(len(n)):
        if i % 2 != 0:
            total += int(n[i])
        else:
            if n[i] != '0':
                div *= int(n[i])
                continue
    
    print(f'{div} {total}')       