for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    crr = list(map(int, input().split()))
    
    count1 = {}
    count2 = {}
    count3 = {}

    for x in arr:
        count1[x] = count1.get(x, 0) + 1
    for x in brr:
        count2[x] = count2.get(x, 0) + 1
    for x in crr:
        count3[x] = count3.get(x, 0) + 1
    check = False
    for num in count1:
        if num in count2 and num in count3:
            check = True
            times = min(count1[num], count2[num], count3[num])
            print((str(num) + ' ') * times, end='')
    if not check:
        print("NO")
    print()
        