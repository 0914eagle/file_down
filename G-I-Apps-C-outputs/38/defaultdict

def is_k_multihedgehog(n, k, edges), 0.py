
from collections import defaultdict

def is_k_multihedgehog(n, k, edges):
    degrees = defaultdict(int)
    
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    center_found = False
    centers = []
    
    for node, degree in degrees.items():
        if degree >= 3:
            centers.append(node)
            center_found = True
    
    if not center_found or len(centers) > 1:
        return "No"
    
    center = centers[0]
    for node in degrees:
        if node != center and degrees[node] != 1:
            return "No"
    
    return "Yes"

# Input parsing
n, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n-1)]

# Check if the given graph is a k-multihedgehog
result = is_k_multihedgehog(n, k, edges)
print(result)
```
