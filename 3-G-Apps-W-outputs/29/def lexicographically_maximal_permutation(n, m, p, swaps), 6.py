
def lexicographically_maximal_permutation(n, m, p, swaps):
    positions = {i: i for i in range(1, n+1)}
    
    for a, b in swaps:
        positions[p[a-1]], positions[p[b-1]] = positions[p[b-1]], positions[p[a-1]]
    
    result = [0] * n
    for i, pos in positions.items():
        result[pos-1] = p[i]
    
    return result

# Input parsing
n, m = map(int, input().split())
p = list(map(int, input().split()))
swaps = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
result = lexicographically_maximal_permutation(n, m, p, swaps)
print(*result)
