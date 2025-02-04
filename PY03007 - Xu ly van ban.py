import re

s = ""
regex = '[\w\s,:]+'
while True: 
    try: 
        s += input()
    except EOFError: 
        break
s = re.findall(regex, s)
for i in s:
    x = i.lower().split()
    x[0] = x[0].title()
    print(' '.join(x))

"""
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
"""