
from collections import defaultdict

n = int(input())

def dfs(graph, node):
    sum_tree[node] = 1
    for child in graph[node]:
        dfs(graph, child)
        sum_tree[node] += sum_tree[child]

graph = defaultdict(list)
sum_tree = [0] * (n+1)

for _ in range(n):
    v, p = map(int, input().split())
    graph[p].append(v)

for v in graph:
    graph[v].sort(reverse=True)

dfs(graph, 0)

print(sum_tree[0])
