
def max_plow_cost(n, m):
    max_cost = (n-1) + (n-m)*(n-m-1) // 2
    return max_cost

# Read input
n, m = map(int, input().split())

# Calculate and output the maximum plow cost
print(max_plow_cost(n, m))
