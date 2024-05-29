
def min_operations(N, x, candies):
    operations = 0
    for i in range(1, N):
        diff = candies[i-1] + candies[i] - x
        if diff > 0:
            operations += diff
            candies[i] -= diff
    return operations

# Read input
N, x = map(int, input().split())
candies = list(map(int, input().split()))

# Call the function and print the result
print(min_operations(N, x, candies))
```
