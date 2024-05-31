
def max_cost_plowing_roads(n, m):
    if m <= n - 1:
        return m * 2
    else:
        return n + (m - n + 1) * 2

# Reading input values
n, m = map(int, input().split())

# Calculate and display the maximum possible cost of plowing the roads
print(max_cost_plowing_roads(n, m))
