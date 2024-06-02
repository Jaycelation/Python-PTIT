n = input()
ans = 0
for i in n:
    if int(i) == 4 or int(i) == 7:
        ans += 1
if ans == 4 or ans == 7:
    print("YES")
else:
    print("NO")