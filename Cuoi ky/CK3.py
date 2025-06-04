for _ in range(int(input())):
    s1 = set(x.lower() for x in input().split())
    s2 = input().split()
    result = [x for x in s2 if x.lower() in s1]
    print(' '.join(result))