
from collections import defaultdict
from sys import stdin
from sys import stdout

n = int(stdin.readline())

graph = defaultdict(list)

for _ in range(n-1):
    a, b, z = map(int, stdin.readline().split())
    graph[a].append((b, z))
    graph[b].append((a, z))

order = list(map(int, stdin.readline().split()))

def dfs(node, parent, xor):
    res = 0
    if xor == 0:
        res += 1
    for child, weight in graph[node]:
        if child != parent:
            res += dfs(child, node, xor ^ weight)
    stdout.write(str(res) + "\n")
    return res

dfs(1, -1, 0)

for i in order:
    a, b, z = graph[i][0]
    if a == i:
        a, b = b, a
    graph[a].remove((b, z))
    graph[b].remove((a, z))
    dfs(1, -1, 0)
