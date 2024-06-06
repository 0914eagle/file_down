
from collections import deque

n, m, k = map(int, input().split())

o = list(map(int, input().split()))
c = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(1, a[0]+1):
        graph[i].append(a[j])

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited = [False]*(n+1)
    visited[start] = True
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return visited[end]

def check(start):
    for i in o:
        if bfs(start, i):
            for j in c:
                if bfs(start, j):
                    return True
    return False

if check(1):
    print(1)
else:
    print("impossible")
