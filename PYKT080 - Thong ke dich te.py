from collections import deque

n, m = map(int, input().split())
count = 0
matrix = []
q = deque()
b = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(m):
        if row[j] == -1:
            q.append((i, j))  

while q:
    u = q.popleft()  
    for dx, dy in b:
        x, y = u[0] + dx, u[1] + dy
        if 0 <= x < n and 0 <= y < m and matrix[x][y] != 0:
            count += matrix[x][y]
            matrix[x][y] = 0  

print(count)