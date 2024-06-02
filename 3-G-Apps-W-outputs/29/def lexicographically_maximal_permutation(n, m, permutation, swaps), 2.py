
def lexicographically_maximal_permutation(n, m, permutation, swaps):
    positions = list(range(1, n+1))
    
    for a, b in swaps:
        a_idx = permutation.index(a)
        b_idx = permutation.index(b)
        
        if a_idx > b_idx:
            a_idx, b_idx = b_idx, a_idx
        
        positions[a_idx] = max(positions[a_idx], b)
        positions[b_idx] = max(positions[b_idx], a)
    
    result = [0] * n
    for i in range(n):
        result[positions[i]-1] = permutation[i]
    
    return result

# Input
n, m = map(int, input().split())
permutation = list(map(int, input().split()))
swaps = [tuple(map(int, input().split())) for _ in range(m)]

# Output
result = lexicographically_maximal_permutation(n, m, permutation, swaps)
print(*result)
