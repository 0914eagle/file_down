
from collections import defaultdict

n = int(input())
jokes = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(node, visited, jokes_set):
    visited[node] = True
    jokes_set.add(jokes[node-1])
    for child in graph[node]:
        if not visited[child]:
            dfs(child, visited, jokes_set)

def solve(node):
    visited = [False] * (n+1)
    jokes_set = set()
    dfs(node, visited, jokes_set)
    jokes_set = sorted(list(jokes_set))
    if len(jokes_set) == 1:
        return 1
    else:
        ans = 1
        for i in range(1, len(jokes_set)):
            if jokes_set[i] - jokes_set[i-1] != 1:
                ans += 1
        return ans

print(solve(1))
