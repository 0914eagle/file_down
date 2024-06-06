
from collections import defaultdict

n = int(input())
jokes = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(node, jokes, graph):
    if node not in graph:
        return set([jokes[node-1]])
    else:
        s = set()
        for child in graph[node]:
            s = s.union(dfs(child, jokes, graph))
        s.add(jokes[node-1])
        return s

print(len(dfs(1, jokes, graph)))
