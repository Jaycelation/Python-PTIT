def split_size(n, size):
    return str(int(n, 2)) 

n = input().strip()

while len(n) % 3 != 0:
    n = '0' + n

result = ""
for i in range(0, len(n), 3):
    result += split_size(n[i:i+3], 3)

print(result)
