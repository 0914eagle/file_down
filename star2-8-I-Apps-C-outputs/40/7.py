
from collections import deque

n, m, alpha = map(int, input().split())

roads = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    roads[u].append((v, c))
    roads[v].append((u, c))

queue = deque([1])
visited = [False] * (n + 1)
visited[1] = True
dist = [float('inf')] * (n + 1)
dist[1] = 0
parent = [0] * (n + 1)

while queue:
    u = queue.popleft()
    for v, c in roads[u]:
        if not visited[v]:
            visited[v] = True
            dist[v] = dist[u] + 1
            parent[v] = u
            queue.append(v)

if dist[-1] == float('inf'):
    print('Poor girl')
else:
    max_candies = max(c for u, c in roads[parent[-1]])
    min_energy = max_candies ** 2 + alpha * dist[-1]
    print(min_energy)

