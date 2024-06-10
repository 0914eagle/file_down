
import sys
from collections import defaultdict

def dfs(node, parent):
    global cost
    global ways
    global checkposts
    if parent != -1:
        cost += costs[node - 1]
        checkposts += 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)

def dfs2(node, parent):
    global ways
    if parent != -1:
        ways = (ways * 2) % 1000000007
    for child in graph[node]:
        if child != parent:
            dfs2(child, node)

n = int(input())
costs = list(map(int, input().split()))
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cost = 0
checkposts = 0
ways = 1
dfs(1, -1)
dfs2(1, -1)
print(cost, ways)

