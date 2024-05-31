
def maximum_plow_cost(n, m):
    return m + (n-1) * (n-2) // 2

# Input parsing
n, m = map(int, input().split())

# Output
print(maximum_plow_cost(n, m))
