
def max_cost_plowing_roads(n, m):
    if m <= n:
        return m * 2
    else:
        return n + (m - n) * 2

# Input
n, m = map(int, input().split())

# Output
print(max_cost_plowing_roads(n, m))
