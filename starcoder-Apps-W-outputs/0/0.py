
# -*- coding: utf-8 -*-


N, M = map(int,input().split())

task = list(map(int,input().split()))

link = [[0]*N for _ in range(N)]

for _ in range(M):
    t1, t2 = map(int,input().split())
    link[t1][t2] = 1

def dfs(n,visited):
    if n in visited:
        return
    
    visited.add(n)
    
    for i in range(N):
        if link[n][i] == 1:
            dfs(i,visited)
    
visited = set()

for i in range(N):
    if task[i] == 1 and i not in visited:
        dfs(i,visited)
        visited.add(i)

print(len(visited))
