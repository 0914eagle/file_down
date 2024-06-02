
def lexicographically_maximal_permutation(n, m, p, swaps):
    parent = list(range(n+1))
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    
    for a, b in swaps:
        parent[find(a)] = find(b)
    
    groups = {}
    for i in range(1, n+1):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    
    result = [0] * n
    for root, group in groups.items():
        group.sort(reverse=True)
        for i, val in enumerate(group):
            result[val-1] = group[i]
    
    return result

# Input parsing
n, m = map(int, input().split())
p = list(map(int, input().split()))
swaps = [list(map(int, input().split())) for _ in range(m)]

# Get the lexicographically maximal permutation
result = lexicographically_maximal_permutation(n, m, p, swaps)

# Output the result
print(*result)
