x, y = list(map(int, input().split()))

m = {}
for i in range(x) :
    line = input().lower() + ' '
    word = ''
    for char in line:
        if char.isalnum():
            word += char
        else:
            if (word != '') :
                if word in m : 
                    m[word] += 1
                else: 
                    m[word] = 1
                word = ''

m = sorted(m.items(), key = lambda x: (-x[1], x[0]))
for i in m:
    if i[1] >= y:
        print(i[0], i[1])

"""
3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""