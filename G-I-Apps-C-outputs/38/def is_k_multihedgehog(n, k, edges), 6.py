
def is_k_multihedgehog(n, k, edges):
    if n == 1:
        return k == 1
    
    degree_counts = [0] * (n + 1)
    
    for u, v in edges:
        degree_counts[u] += 1
        degree_counts[v] += 1
    
    center_degree = max(degree_counts)
    
    if center_degree < 3 or k == 1:
        return "No"
    
    max_branches = center_degree - 1
    total_branches = sum(1 for degree in degree_counts if degree == 1)
    
    if total_branches != (k - 1) * max_branches:
        return "No"
    
    return "Yes"


# Input parsing
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

print(is_k_multihedgehog(n, k, edges))
