
from collections import defaultdict

def solve_tree_queries(n, m, edges, queries):
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    
    def dfs(node, par, d):
        parent[node] = par
        depth[node] = d
        for child in adj_list[node]:
            if child != par:
                dfs(child, node, d + 1)
    
    dfs(1, 0, 0)
    
    def check_path(u, vertices):
        for v in vertices:
            if depth[v] <= depth[u] + 1:
                if parent[v] != u and v != u:
                    return False
        return True
    
    for query in queries:
        k = query[0]
        vertices = query[1:]
        possible = False
        for u in vertices:
            if check_path(u, vertices):
                possible = True
                break
        if possible:
            print("YES")
        else:
            print("NO")

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

# Calling the function to solve tree queries
solve_tree_queries(n, m, edges, queries)
```
