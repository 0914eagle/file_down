
from collections import deque
n, m, k = map(int, input().split())
o = list(map(int, input().split()))
c = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(1, a[0]+1):
        graph[i].append(a[j])

def bfs(s):
    visited = [False]*(n+1)
    visited[s] = True
    q = deque([s])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return visited

visited = bfs(1)

def check(visited):
    for i in o:
        if visited[i]:
            return True
    for i in c:
        if visited[i]:
            return True
    return False

if check(visited):
    print(1)
else:
    visited = bfs(2)
    if check(visited):
        print(2)
    else:
        print("impossible")
