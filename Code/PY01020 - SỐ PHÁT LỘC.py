t=int(input())
for test in range(t):
    n=input()
    if len(n)<2:
        print("NO")
    else:
        if n[len(n)-1]=='6' and n[len(n)-2]=='8':
            print("YES")
        else:
            print("NO")