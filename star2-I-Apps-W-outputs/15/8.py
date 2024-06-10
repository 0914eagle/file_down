
from collections import deque

N, X, Y = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    graph[i].append(i + 1)
    graph[i + 1].append(i)
graph[X - 1].append(Y - 1)
graph[Y - 1].append(X - 1)

dist = [0] * N
visited = [False] * N
queue = deque([0])
visited[0] = True
while queue:
    v = queue.popleft()
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            dist[u] = dist[v] + 1
            queue.append(u)

for k in range(1, N):
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if dist[i] + dist[j] + 1 == k:
                count += 1
    print(count)

