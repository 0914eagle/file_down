

import sys
sys.setrecursionlimit(10000)
def dfs(node,parent):
    global visited
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        if child != parent:
            dfs(child,node)
N = int(input())
L = int(input())
walk = [int(x) for x in input().split()]
graph = [[] for i in range(N)]
for i in range(N):
    l = [int(x) for x in input().split()]
    for j in range(1,l[0]+1):
        graph[i].append(l[j])
visited = set()
dfs(walk[0],-1)
if walk[L-1] not in visited:
    print(1.0)
else:
    visited = set()
    dfs(walk[L-1],-1)
    count = 0
    for i in walk:
        if i in visited:
            count += 1
    prob = 1/len(graph[walk[L-1]])
    prob = prob**count
    print(prob)

