
def find_max_degree_spanning_tree(n, m, edges):
    adj_list = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    degrees = [len(adj_list[i]) for i in range(1, n + 1)]
    max_degree_vertex = degrees.index(max(degrees)) + 1
    
    visited = set()
    spanning_tree_edges = []
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor != parent:
                if neighbor not in visited:
                    spanning_tree_edges.append((node, neighbor))
                    dfs(neighbor, node)
    
    dfs(max_degree_vertex, -1)
    
    return spanning_tree_edges

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Find and print the spanning tree
spanning_tree_edges = find_max_degree_spanning_tree(n, m, edges)
for edge in spanning_tree_edges:
    print(edge[0], edge[1])
```
