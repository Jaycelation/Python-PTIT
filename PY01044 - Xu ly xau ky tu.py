s = set(input().lower().split())
w = set(input().lower().split())

giao = sorted(s & w)
hop = sorted(s | w)

print(' '.join(hop))
print(' '.join(giao))