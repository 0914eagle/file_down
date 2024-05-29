
def find_max_degree_spanning_tree(n, m, edges):
    # Create a list to keep track of the degree of each vertex
    degree = [0] * (n + 1)
    
    # Create a list to store the edges of the spanning tree
    spanning_tree_edges = []
    
    # Sort the edges by the sum of the degrees of their endpoints in decreasing order
    edges.sort(key=lambda x: degree[x[0]] + degree[x[1]], reverse=True)
    
    # Iterate through the sorted edges and add them to the spanning tree if they don't create a cycle
    for edge in edges:
        if degree[edge[0]] < 2 and degree[edge[1]] < 2:
            spanning_tree_edges.append(edge)
            degree[edge[0]] += 1
            degree[edge[1]] += 1
    
    return spanning_tree_edges

# Input parsing
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Find and print the maximum degree spanning tree
spanning_tree = find_max_degree_spanning_tree(n, m, edges)
for edge in spanning_tree:
    print(edge[0], edge[1])
```
