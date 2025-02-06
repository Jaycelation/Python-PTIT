def Try(cur, c2, c3, c5, c7, length, maxlength, result):
    if length >= 4:
        if c2 > 0 and c3 > 0 and c5 > 0 and c7 > 0 and cur[-1] in "357":
            result.append(cur)
    if length < maxlength:
        Try(cur + "2", c2 + 1, c3, c5, c7, length + 1, maxlength, result)
        Try(cur + "3", c2, c3 + 1, c5, c7, length + 1, maxlength, result)
        Try(cur + "5", c2, c3, c5 + 1, c7, length + 1, maxlength, result)
        Try(cur + "7", c2, c3, c5, c7 + 1, length + 1, maxlength, result)

n = int(input())
result = []
val = []
Try("", 0, 0, 0, 0, 0, n, result)

for num in result:
    val.append(int(num))
val.sort()
for i in val:
    print(i)