
from collections import defaultdict

def is_k_multihedgehog(n, k, edges):
    degrees = defaultdict(int)
    
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    center_found = False
    for node, degree in degrees.items():
        if degree >= 3:
            if center_found or degree < k:
                return "No"
            else:
                center_found = True
    
    return "Yes"

# Input parsing
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]

# Check if the tree is a k-multihedgehog
result = is_k_multihedgehog(n, k, edges)
print(result)
```
