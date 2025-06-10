for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count_dict = dict({})
    for i in range(n):
        if arr[i] in count_dict:
            count_dict[arr[i]] += 1
        else:
            count_dict[arr[i]] = 1

    for key, val in count_dict.items():
        if val % 2 != 0:
            print(key)