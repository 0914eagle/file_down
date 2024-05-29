
def min_operations_to_neighbor_constraint(N, x, candies):
    operations = 0
    for i in range(1, N):
        if candies[i-1] + candies[i] > x:
            diff = candies[i-1] + candies[i] - x
            operations += diff
            candies[i] = max(0, candies[i] - diff)
    return operations

# Read input
N, x = map(int, input().split())
candies = list(map(int, input().split()))

# Call the function and print the result
print(min_operations_to_neighbor_constraint(N, x, candies))
```
