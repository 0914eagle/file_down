
def max_plow_cost(n, m):
    # Calculate the maximum possible cost of plowing the roads
    return m + (n-2) * (n-1) // 2

# Read input
n, m = map(int, input().split())

# Calculate and print the maximum cost of plowing the roads
print(max_plow_cost(n, m))
