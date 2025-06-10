s = input()

def split_chunk(s, x):
    return [s[i:i+x] for i in range(0, len(s), x)]

if len(s) % 2 != 0:
    s = s[:-1:]

arr = split_chunk(s, 2)
A = set(arr)
A = sorted(A, reverse=False)
print(*A)