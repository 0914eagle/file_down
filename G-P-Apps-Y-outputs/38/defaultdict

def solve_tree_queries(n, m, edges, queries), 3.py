
from collections import defaultdict

def solve_tree_queries(n, m, edges, queries):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    def dfs(node, parent, nodes_in_path):
        if node in nodes_in_path:
            return True
        for child in tree[node]:
            if child != parent:
                if dfs(child, node, nodes_in_path):
                    return True
        return False
    
    for query in queries:
        k = query[0]
        nodes = query[1:]
        
        nodes_in_path = set()
        for node in nodes:
            nodes_in_path.add(node)
            for child in tree[node]:
                nodes_in_path.add(child)
        
        if dfs(1, 0, nodes_in_path):
            print("YES")
        else:
            print("NO")

# Input parsing
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n-1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

# Solve queries
solve_tree_queries(n, m, edges, queries)
```
