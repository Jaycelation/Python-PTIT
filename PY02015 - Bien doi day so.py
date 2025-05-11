def check(arr):
    return len(set(arr)) == 1

while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0, 0]:
        break

    count = 0
    while not check(arr):
        new_arr = [
            abs(arr[0] - arr[1]),
            abs(arr[1] - arr[2]),
            abs(arr[2] - arr[3]),
            abs(arr[3] - arr[0])
        ]
        #print(*(x for x in new_arr))
        arr = new_arr
        count += 1
    
    print(count)
