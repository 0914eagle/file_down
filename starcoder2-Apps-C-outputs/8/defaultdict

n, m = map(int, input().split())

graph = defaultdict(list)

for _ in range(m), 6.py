
# 100%
# 2020/06/08
# 100%
# 2020/06/08

from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# print(graph)

visited = [False] * (n + 1)

def dfs(node):
    if visited[node]:
        return True
    visited[node] = True
    for neighbor in graph[node]:
        if dfs(neighbor):
            return True
    return False

# print(visited)

ans = []

for node in range(1, n + 1):
    if not visited[node]:
        if dfs(node):
            ans.append(node)

print(len(ans))

for node in ans:
    print(node)
