
def solve(n):
    res = [0] * (2 * n)
    for i in range(n):
        res[i] = i + 1
        res[n + i] = i + 1
    return res

n = int(input())
result = solve(n)
print(*result)
