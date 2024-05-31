
def solve_permutation(n):
    a = []
    for i in range(1, n+1):
        a.extend([i, i])
    return a

# Read input
n = int(input())

# Solve the problem
result = solve_permutation(n)

# Output the result
print(*result)
