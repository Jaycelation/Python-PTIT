from collections import defaultdict, deque

graph = defaultdict(list)

n, m = map(int, input().split())

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = set()
queue = deque()

def dfs(u):
    print(f"Visiting: {u}")
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v)

def bfs(u):
    queue.append(u)
    visited.add(u)
    while queue:
        u = queue.popleft()
        print(f"Visiting: {u}")
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

bfs(1)