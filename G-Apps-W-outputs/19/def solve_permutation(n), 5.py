
def solve_permutation(n):
    result = []
    for i in range(1, n + 1):
        result.extend([i, i])
    return result

# Input
n = int(input())

# Output
permuted_array = solve_permutation(n)
print(*permuted_array)
