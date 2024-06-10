
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

def dfs(node, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

def is_valid(s):
    graph_from_s = defaultdict(set)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j] or (s[i] == 'a' and s[j] == 'b') or (s[i] == 'b' and s[j] == 'a') or (s[i] == 'b' and s[j] == 'c') or (s[i] == 'c' and s[j] == 'b'):
                graph_from_s[i+1].add(j+1)
                graph_from_s[j+1].add(i+1)
    
    visited = set()
    dfs(1, visited, graph_from_s)
    return len(visited) == n and graph_from_s == graph

for s in ['a' * n, 'b' * n, 'c' * n, 'ab' * (n//2), 'ba' * (n//2), 'bc' * (n//2), 'cb' * (n//2)]:
    if is_valid(s):
        print("Yes")
        print(s)
        break
else:
    print("No")

