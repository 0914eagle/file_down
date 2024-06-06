
from collections import defaultdict
from sys import stdin

n = int(stdin.readline())

graph = defaultdict(list)

for _ in range(n - 1):
    a, b, z = map(int, stdin.readline().split())
    graph[a].append((b, z))
    graph[b].append((a, z))

order = list(map(int, stdin.readline().split()))

visited = [False] * (n + 1)

def dfs(node, parent, xor_sum):
    visited[node] = True
    for child, z in graph[node]:
        if not visited[child]:
            dfs(child, node, xor_sum ^ z)

def get_boring_pairs(xor_sum):
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1, xor_sum)
            count += 1
    return count

for i in range(n - 1):
    a, b, z = graph[order[i]]
    graph[a].remove((b, z))
    graph[b].remove((a, z))
    print(get_boring_pairs(z))
