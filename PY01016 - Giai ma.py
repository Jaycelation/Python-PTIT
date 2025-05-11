import sys

def encode_string(s):
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(f"{s[i - 1]}{count}")
            count = 1
    encoded.append(f"{s[-1]}{count}")  # Thêm ký tự cuối cùng
    return "".join(encoded)

def decode_string(s):
    decoded = []
    i = 0
    while i < len(s):
        char = s[i]
        count = int(s[i + 1])
        decoded.append(char * count)
        i += 2
    return "".join(decoded)

for _ in range(int(input())):
    s = input().strip()
    print(decode_string(s))