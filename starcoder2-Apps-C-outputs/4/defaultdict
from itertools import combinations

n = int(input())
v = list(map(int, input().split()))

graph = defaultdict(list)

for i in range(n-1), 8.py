
from collections import defaultdict
from itertools import combinations

n = int(input())
v = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(node, visited):
    visited.add(node)
    for child in graph[node]:
        dfs(child, visited)

def solve(v):
    visited = set()
    dfs(1, visited)
    visited = list(visited)
    visited.sort()
    res = 0
    for i in range(len(visited)):
        for j in range(i, len(visited)):
            if visited[j] - visited[i] == j - i:
                res += 1
    return res

print(solve(v))
