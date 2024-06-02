import string

def endecode(a, b):
    for i in range(1, b):
        if (((a % b) * (i % b)) % b == 1):
            return i
    return -1

flag = []

a = [268,413,438,313,426,337,272,188,392,338,77,332,139,113,92,239,247,120,419,72,295,190,131]

for i in range(len(a)):
    mod = endecode(a[i], 41)

    if mod in range(1, 27):
        flag.append(string.ascii_letters[mod-1])
    elif mod in range(27, 37):
        flag.append(string.digits[mod-27])
    else:   
        flag.append("_")

print("picoCTF{%s}" % "".join(flag))