from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
in_degree = defaultdict(int)
nodes = set()

for _ in range(n):
    a, op, b = input().split()
    nodes.add(a)
    nodes.add(b)
    if op == '>':
        graph[a].append(b)
        in_degree[b] += 1
    else:  # op == '<'
        graph[b].append(a)
        in_degree[a] += 1

queue = deque([node for node in nodes if in_degree[node] == 0])
count = 0

while queue:
    u = queue.popleft()
    count += 1
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

if count == len(nodes):
    print("possible")
else:
    print("impossible")
