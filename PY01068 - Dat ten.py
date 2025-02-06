import itertools
n, m = map(int, input().split())
arr = list(map(str, input().split()))

lst = sorted(set(arr))
perms = itertools.combinations(lst, m)
for perm in perms:
    print(' '.join(map(str, perm)))