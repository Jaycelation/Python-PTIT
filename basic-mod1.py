import string

flag = []

a = [165, 248, 94, 346 ,299, 73, 198, 221, 313, 137, 205, 87 ,336, 110, 186, 69, 223, 213 ,216, 216, 177, 138]

for i in range(len(a)):
    mod = a[i]%37
    
    if mod in range(26):
        flag.append(string.ascii_uppercase[mod])
    elif mod in range(26, 36):
        flag.append(string.digits[mod-26])
    else:
        flag.append("_")

print("picoCTF{%s}" % "".join(flag))