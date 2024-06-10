
from collections import defaultdict

def solve(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    for i in range(1, n+1):
        if len(adj[i]) == n-1:
            return "Yes\n" + "a" * (i-1) + "b" + "a" * (n-i)
    
    return "No"

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solve(n, edges))

