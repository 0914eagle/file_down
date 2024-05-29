
def solve_maximum_degree_spanning_tree(n, m, edges):
    from collections import defaultdict
    
    adj_list = defaultdict(list)
    degrees = defaultdict(int)
    
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    
    max_degree_vertex = max(degrees, key=degrees.get)
    visited = set()
    tree_edges = []
    
    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                tree_edges.append((node, neighbor))
                dfs(neighbor)
    
    dfs(max_degree_vertex)
    
    return tree_edges

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = solve_maximum_degree_spanning_tree(n, m, edges)

for edge in result:
    print(edge[0], edge[1])
```
