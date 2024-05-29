
def solve_spanning_tree(n, m, edges):
    adj_list = [[] for _ in range(n)]
    degree = [0] * n
    
    for edge in edges:
        u, v = edge
        adj_list[u-1].append(v)
        adj_list[v-1].append(u)
        degree[u-1] += 1
        degree[v-1] += 1
    
    max_degree_vertex = degree.index(max(degree)) + 1
    tree_edges = []
    visited = [False] * n
    visited[max_degree_vertex-1] = True
    
    for neighbor in adj_list[max_degree_vertex-1]:
        tree_edges.append((max_degree_vertex, neighbor))
        visited[neighbor-1] = True
        
    for vertex in adj_list[max_degree_vertex-1]:
        for neighbor in adj_list[vertex-1]:
            if not visited[neighbor-1]:
                tree_edges.append((vertex, neighbor))
                visited[neighbor-1] = True
    
    return tree_edges

# Input reading
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
result = solve_spanning_tree(n, m, edges)
for edge in result:
    print(edge[0], edge[1])
```
