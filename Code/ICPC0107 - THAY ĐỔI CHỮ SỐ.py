def maxx(n,m,p,q):
    n=int(n.replace(p,q))
    m=int(m.replace(p,q))
    return n+m
for t in range(int(input())):
    p,q=map(int,input().split())
    if p>q:
        p,q=q,p
    s=input().split()
    if len(s)==1:
        x1=s[0]
        x2=input()
    else:
        x1,x2=s
    print(maxx(x1,x2,str(q),str(p)),maxx(x1,x2,str(p),str(q)))