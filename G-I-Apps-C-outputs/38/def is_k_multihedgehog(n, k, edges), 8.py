
def is_k_multihedgehog(n, k, edges):
    degrees = [0] * (n + 1)
    
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    centers = []
    for i in range(1, n + 1):
        if degrees[i] >= 3:
            centers.append(i)
    
    if len(centers) != 1:
        return "No"
    
    center = centers[0]
    
    queue = [center]
    visited = set()
    
    while queue:
        curr = queue.pop(0)
        visited.add(curr)
        neighbors = []
        
        for u, v in edges:
            if u == curr:
                neighbors.append(v)
            elif v == curr:
                neighbors.append(u)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    queue.append(neighbor)
                elif degrees[neighbor] < 1:
                    return "No"
    
    for degree in degrees[1:]:
        if degree != 0:
            return "No"
    
    return "Yes"

# Example usage
n, k = 14, 2
edges = [(1, 4), (2, 4), (3, 4), (4, 13), (10, 5), (11, 5), (12, 5), (14, 5), (5, 13), (6, 7), (8, 6), (13, 6), (9, 6)]

result = is_k_multihedgehog(n, k, edges)
print(result)
```
