def find_kth_character(n, k):
    if k == (1 << (n - 1)):
        return chr(ord('A') + n - 1)
    elif k < (1 << (n - 1)):
        return find_kth_character(n - 1, k)
    else: 
        return find_kth_character(n - 1, k - (1 << (n - 1)))

test = int(input())
while test:
    test -= 1
    n, k = map(int, input().split()) 
    print(find_kth_character(n, k))