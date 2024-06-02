
def lexicographically_maximal_permutation(n, m, permutation, swaps):
    positions = list(range(1, n+1))
    parent = list(range(n+1))
    
    def find(x):
        if parent[x] != x:
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
    for group in groups.values():
        group.sort(reverse=True)
    
    for i in range(1, n+1):
        root = find(i)
        result[i-1] = groups[root].pop()
    
    return result

# Input
n, m = map(int, input().split())
permutation = list(map(int, input().split()))
swaps = [list(map(int, input().split())) for _ in range(m)]

# Output
result = lexicographically_maximal_permutation(n, m, permutation, swaps)
print(*result)
