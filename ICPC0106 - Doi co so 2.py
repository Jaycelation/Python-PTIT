test = int(input()) 
while test:
    test -= 1
    b = int(input())  
    num = input()  
    if b == 2:
        print(num)
    else:
        val = int(num, 2)
        result = ""
        while val > 0:
            temp = val % b
            if temp < 10:
                result = str(temp) + result
            else:
                result = chr(temp - 10 + ord('A')) + result
            val //= b
        
        print(result if result else "0")
