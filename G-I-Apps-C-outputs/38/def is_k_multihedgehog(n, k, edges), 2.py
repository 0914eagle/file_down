
def is_k_multihedgehog(n, k, edges):
    degree_counts = [0] * n
    for u, v in edges:
        degree_counts[u - 1] += 1
        degree_counts[v - 1] += 1
    
    centers = [i + 1 for i, count in enumerate(degree_counts) if count >= 3]
    
    if len(centers) != 1:
        return "No"
    
    center = centers[0]
    for i in range(n):
        if degree_counts[i] == 1:
            return "No"
    
    return "Yes"

# Input parsing
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]

# Check if given graph is k-multihedgehog
result = is_k_multihedgehog(n, k, edges)
print(result)
```
