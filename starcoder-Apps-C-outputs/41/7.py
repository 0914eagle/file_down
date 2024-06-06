
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from collections import deque

def bfs(v,graph):
    q = deque()
    q.append(v)
    dist = [float("inf") for _ in range(n+1)]
    dist[v] = 0
    while q:
        v = q.popleft()
        for u in graph[v]:
            if dist[u] == float("inf"):
                dist[u] = dist[v]+1
                q.append(u)
    return dist

n = int(input())
time = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for i in range(1,n):
    tmp = list(map(int,input().split()))
    graph[i] = tmp[1:]
dist = bfs(1,graph)
tmp = 0
for i in range(1,n+1):
    tmp = max(tmp,time[i-1]*dist[i])
print(tmp)
