
from collections import defaultdict

def solve(n, edges):
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    labels = [0] * (n - 1)
    
    def dfs(u, p):
        for v in adj_list[u]:
            if v != p:
                labels[v - 1] = dfs(v, u) + 1
                return labels[v - 1]
    
    dfs(1, -1)
    
    return labels

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
labels = solve(n, edges)
print(*labels, sep="\n")

