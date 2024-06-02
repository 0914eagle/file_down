
def lexicographically_maximal_permutation(n, m, permutation, swaps):
    positions = {i: i for i in range(1, n + 1)}
    
    for a, b in swaps:
        positions[permutation[a - 1]], positions[permutation[b - 1]] = positions[permutation[b - 1]], positions[permutation[a - 1]]
    
    result = [0] * n
    for i in range(1, n + 1):
        result[positions[i] - 1] = i
    
    return result

# Input parsing
n, m = map(int, input().split())
permutation = list(map(int, input().split()))
swaps = [list(map(int, input().split())) for _ in range(m)]

result = lexicographically_maximal_permutation(n, m, permutation, swaps)
print(*result)
