
def max_cost_plow_roads(n, m):
    if m <= n:
        return m*(m+1)//2
    else:
        remaining = m - n
        return n + (remaining)*(remaining+1)//2

# Input
n, m = map(int, input().split())

# Output
print(max_cost_plow_roads(n, m))
