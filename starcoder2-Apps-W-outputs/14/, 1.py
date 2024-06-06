
# -*- coding: utf-8 -*-


import sys

sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, z = map(int, input().split())
    graph[a].append((b, z))
    graph[b].append((a, z))

order = list(map(int, input().split()))

visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    for child, z in graph[node]:
        if not visited[child]:
            dfs(child)

dfs(1)

for i in range(N-1):
    a, b, z = graph[order[i]]
    if visited[a] and visited[b]:
        print(1)
    else:
        print(0)
