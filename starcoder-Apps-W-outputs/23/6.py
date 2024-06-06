
# graph problem

import math

n,m = map(int,input().split())

G = [[] for i in range(n)]

for i in range(m):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

def dfs(start,visited):
    visited[start] = True
    for i in G[start]:
        if visited[i]: continue
        dfs(i,visited)

def bfs(start,visited):
    queue = [start]
    visited[start] = True
    while queue:
        cur = queue.pop(0)
        for i in G[cur]:
            if visited[i]: continue
            visited[i] = True
            queue.append(i)

def solve(n,m,G):
    
    # 1) find a vertex v such that degree(v) < sqrt(n)
    for i in range(n):
        if len(G[i]) < math.sqrt(n):
            v = i
            break

    # 2) use dfs to find a set of n-sqrt(n) vertices that are reachable from v
    visited = [False for _ in range(n)]
    dfs(v,visited)

    # 3) from v, use bfs to find a cycle that passes through at least sqrt(n) vertices
    queue = [v]
    visited = [False for _ in range(n)]
    while queue:
        cur = queue.pop(0)
        for i in G[cur]:
            if i == v and len(visited) >= math.sqrt(n):
                return visited
            if visited[i]: continue
            visited[i] = True
            queue.append(i)

visited = solve(n,m,G)
print(visited)
