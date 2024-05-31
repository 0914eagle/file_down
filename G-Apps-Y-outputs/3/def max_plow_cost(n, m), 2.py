
def max_plow_cost(n, m):
    if m <= n - 1:
        return m * 2
    else:
        return n + (m - n + 1) * 2

# Input
n, m = map(int, input().split())

# Output
print(max_plow_cost(n, m))
