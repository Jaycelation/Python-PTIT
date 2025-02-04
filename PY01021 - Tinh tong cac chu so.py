import re

test = int(input())
while test:
    test -= 1
    s = input()
    result = ""
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
        else:
            result += c
    result = "".join(sorted(result))
    result += str(val)
    print(result)