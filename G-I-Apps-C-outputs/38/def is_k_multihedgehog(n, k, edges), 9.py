
def is_k_multihedgehog(n, k, edges):
    degrees = [0] * (n + 1)
    
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    center_degree = max(degrees)
    
    if center_degree < 3:
        return "No"
    
    leaf_count = degrees.count(1)
    non_center_vertices = n - leaf_count - 1
    
    if non_center_vertices % (k - 1) == 0 and non_center_vertices >= (k - 1):
        return "Yes"
    else:
        return "No"

# Input parsing
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Check if the given tree is a k-multihedgehog
result = is_k_multihedgehog(n, k, edges)
print(result)
```
