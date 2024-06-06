
from collections import defaultdict

def dfs(node):
    if node not in visited:
        visited.add(node)
        for child in graph[node]:
            dfs(child)
        if node in jokes:
            jokes[node].add(jokes[node])
        else:
            jokes[node] = set()
        jokes[node].add(types[node])
        for child in graph[node]:
            jokes[node] = jokes[node].union(jokes[child])

n = int(input())
types = [0] + list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = set()
jokes = {}
dfs(1)

ans = 0
for i in range(1, n + 1):
    if len(jokes[i]) == len(set(jokes[i])):
        ans += 1
print(ans)
