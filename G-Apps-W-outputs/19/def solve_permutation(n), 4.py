
def solve_permutation(n):
    res = []
    for i in range(1, n+1):
        res.extend([i, i])
    return res

# Input
n = int(input())

# Output
result = solve_permutation(n)
print(*result)
