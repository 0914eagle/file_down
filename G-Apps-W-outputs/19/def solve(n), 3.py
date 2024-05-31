
def solve(n):
    a = []
    for i in range(1, n + 1):
        a.extend([i, i])
    return a

n = int(input())
result = solve(n)
print(*result)
