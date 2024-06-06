
from collections import defaultdict
from collections import deque

n, m, k = map(int, input().split())
o = list(map(int, input().split()))
c = list(map(int, input().split()))

g = defaultdict(list)
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(1, a[0] + 1):
        g[i + 1].append(a[j])

def bfs(s):
    q = deque()
    q.append(s)
    visited = [False] * (n + 1)
    visited[s] = True
    while q:
        u = q.popleft()
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return visited

v = bfs(1)

if all(v[i] for i in o) and all(v[i] for i in c):
    print(1)
else:
    print("impossible")
