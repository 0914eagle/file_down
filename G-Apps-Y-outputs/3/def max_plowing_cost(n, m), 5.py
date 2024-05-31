
def max_plowing_cost(n, m):
    return m + (n-2)*(n-1)//2

# Read input
n, m = map(int, input().split())

# Calculate and print the maximum plowing cost
print(max_plowing_cost(n, m))
