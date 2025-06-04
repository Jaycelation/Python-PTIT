def convert_base(decimal, base):
    if decimal == 0:
        return "0"
    digits = []
    chars = "0123456789ABCDEF"
    while decimal > 0:
        digits.append(chars[decimal % base])
        decimal //= base
    return ''.join(digits[::-1])

with open('DATA.in', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    t = int(lines[0])
    idx = 1
    for _ in range(t):
        b = int(lines[idx])
        n = lines[idx + 1]
        decimal = int(n, 2)
        result = convert_base(decimal, b)
        print(result)
        idx += 2