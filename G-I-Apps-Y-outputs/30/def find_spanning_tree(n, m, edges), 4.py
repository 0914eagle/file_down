
def find_spanning_tree(n, m, edges):
    adjacency_list = {}
    for i in range(1, n+1):
        adjacency_list[i] = []
    
    degree_count = [0] * (n+1)
    
    for edge in edges:
        v, u = edge
        adjacency_list[v].append(u)
        adjacency_list[u].append(v)
        degree_count[v] += 1
        degree_count[u] += 1
    
    result_edges = []
    
    max_degree_vertex = max(range(1, n+1), key=lambda x: degree_count[x])
    
    visited = set()
    stack = [max_degree_vertex]
    
    while stack:
        current_vertex = stack.pop()
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor in adjacency_list[current_vertex]:
            if neighbor not in visited:
                result_edges.append([current_vertex, neighbor])
                stack.append(neighbor)
    
    return result_edges

# Input parsing
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Find and print the spanning tree
result = find_spanning_tree(n, m, edges)
for edge in result:
    print(edge[0], edge[1])
