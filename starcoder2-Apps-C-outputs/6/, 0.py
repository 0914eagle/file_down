
from collections import deque

n, m, k = map(int, input().split())
o = list(map(int, input().split()))
c = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    a = list(map(int, input().split()))
    for j in range(1, a[0] + 1):
        graph[i].append(a[j])

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [0] * (n + 1)
    visited[start] = 1
    while q:
        cur = q.popleft()
        if cur == end:
            return True
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    return False

if bfs(1, o[0]) and bfs(1, c[0]):
    print(1)
elif bfs(o[0], c[0]):
    print(1)
else:
    print("impossible")
