
from collections import deque

def solve(N, X, Y):
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
    graph[X - 1].append(Y - 1)
    graph[Y - 1].append(X - 1)
    dist = [-1] * N
    dist[0] = 0
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                queue.append(u)
    ans = [0] * (N - 1)
    for i in range(N):
        for j in range(i + 1, N):
            ans[dist[i] - 1] += 1
    return ans

N, X, Y = map(int, input().split())
ans = solve(N, X, Y)
for a in ans:
    print(a)

