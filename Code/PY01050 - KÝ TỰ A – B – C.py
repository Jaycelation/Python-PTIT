a=[]
def Try(s,n,na,nb,nc):
    if len(s)>n: return
    if na<=nb and nb<=nc and len(s)<=n and na>0 and nb>0 and nc>0:
        global a
        a.append(s)
    Try(s+'A',n,na+1,nb,nc)
    Try(s+'B',n,na,nb+1,nc)
    Try(s+'C',n,na,nb,nc+1)
    return
n=int(input())
Try('',n,0,0,0)
for i in range(3,n+1):
    for x in a:
        if len(x)==i:
            print(x)