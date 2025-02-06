import itertools

s = input()

perms = itertools.permutations(s)
for perm in perms:
    print(''.join(perm))