from collections import Counter

for _ in range(int(input())):
    s = input()

    c = Counter(s)
    x, y = "", ""
    for key, val in c.items():
        if val == 1:
            x += key
        else:
            y += key
    print("NONE" if x == "" else x)
    print("NONE" if y == "" else y) 