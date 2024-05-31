
def solve_permutation(n):
    permuted_array = []
    for i in range(1, n+1):
        permuted_array.extend([i, i])
    return permuted_array

# Input
n = int(input())

# Output
result = solve_permutation(n)
print(*result)
