n = int(input())

m = {}
for i in range(n) :
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
    print(i[0], i[1])