t = int(input())
for _ in range(t):
    a = list(input())
    n = len(a)
    
    # Tìm vị trí p sao cho a[p] > a[p+1]
    p = -1
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            p = i
            break
    
    if p == -1:
        print(-1)
        continue
    
    # Tìm phần tử lớn nhất nhỏ hơn a[p] ở bên phải
    q = p + 1
    for i in range(p + 1, n):
        if a[i] < a[p] and a[i] > a[q]:
            q = i
    
    a[p], a[q] = a[q], a[p]
    
    if a[0] == '0':
        print(-1)
    else:
        print("".join(a))