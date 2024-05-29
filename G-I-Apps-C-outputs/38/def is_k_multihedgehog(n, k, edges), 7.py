
def is_k_multihedgehog(n, k, edges):
    degrees = [0] * n
    for u, v in edges:
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    
    center_degrees = [d for d in degrees if d >= 3]
    
    if len(center_degrees) != 1:
        return "No"
    
    center = degrees.index(max(center_degrees)) + 1
    
    for d in degrees:
        if d == 1:
            return "No"
    
    return "Yes"

# Read input
n, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n - 1)]

# Check if the tree is a k-multihedgehog
result = is_k_multihedgehog(n, k, edges)

print(result)
```
