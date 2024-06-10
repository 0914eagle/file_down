
import sys
from collections import defaultdict

def dfs(v, p, col, graph, res):
    red = 0
    blue = 0
    for u in graph[v]:
        if u == p:
            continue
        red_u, blue_u = dfs(u, v, col, graph, res)
        red += red_u
        blue += blue_u
    if col[v] == 1:
        red += 1
    elif col[v] == 2:
        blue += 1
    if red > 0 and blue > 0:
        res[0] += 1
    return red, blue


n = int(sys.stdin.readline())
col = [0] * (n + 1)
graph = defaultdict(list)
for i, c in enumerate(map(int, sys.stdin.readline().split())):
    col[i + 1] = c
for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
res = [0]
dfs(1, -1, col, graph, res)
print(res[0])

