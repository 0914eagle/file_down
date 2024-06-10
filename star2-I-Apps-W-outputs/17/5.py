
from collections import defaultdict

def solve(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    labels = [0] * (n - 1)
    used = set()
    
    def dfs(u, parent):
        for v in adj[u]:
            if v != parent:
                dfs(v, u)
                labels[v - 1] = 0
                for i in range(n - 1):
                    if i not in used:
                        labels[v - 1] = i
                        used.add(i)
                        break
    
    dfs(1, -1)
    
    return labels

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
labels = solve(n, edges)
print(*labels, sep='\n')

