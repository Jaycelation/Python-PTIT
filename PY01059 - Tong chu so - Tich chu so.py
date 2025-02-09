test = int(input())
while test:
    test -= 1
    n = input()
    total = 0  
    div = 1
    check = False  
    
    for i in range(len(n)):
        if i % 2 == 0: 
            total += int(n[i])
        else: 
            if n[i] != '0':  
                div *= int(n[i])
                check = True  
    
    if not check:  
        div = 0

    print(f"{total} {div}")  
