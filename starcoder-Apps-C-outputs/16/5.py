
from collections import defaultdict
from collections import Counter
import sys

def add_or_sub(amount, a, b, d):
    if d[a][b] == 0:
        d[a][b] = amount
    else:
        d[a][b] += amount
        if d[a][b] == 0:
            del d[a][b]

def cancel(a, b, amount, d, graph, visited):
    visited[a] = True
    graph[a].remove(b)
    for c in graph[a]:
        if not visited[c]:
            cancel(c, a, amount, d, graph, visited)
    add_or_sub(amount, a, b, d)


def dfs(graph, a, b, visited):
    visited[a] = True
    graph[a].remove(b)
    for c in graph[a]:
        if not visited[c]:
            dfs(graph, c, b, visited)

# read input
n, m = list(map(int, sys.stdin.readline().split()))
d = defaultdict(Counter)
graph = defaultdict(list)
for _ in range(m):
    a, b, amount = list(map(int, sys.stdin.readline().split()))
    add_or_sub(amount, a, b, d)
    graph[a].append(b)

# delete edges that can be canceled
visited = [False] * n
for i in range(n):
    for j in range(n):
        if i != j and d[i][j] != 0 and not visited[i]:
            cancel(i, j, d[i][j], d, graph, visited)

# output the resulting IOUs
print(sum(len(graph[i]) for i in range(n)))
for i in range(n):
    for j in graph[i]:
        print('{} {} {}'.format(i, j, d[i][j]))
