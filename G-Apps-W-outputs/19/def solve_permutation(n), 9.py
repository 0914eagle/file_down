
def solve_permutation(n):
    result = []
    for i in range(1, n+1):
        result.extend([i, i])
    return result

n = int(input())
result = solve_permutation(n)
print(" ".join(map(str, result)))
