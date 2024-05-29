
def min_operations_to_satisfy_constraints(N, x, candies):
    operations = 0
    for i in range(1, N):
        total_candies = candies[i-1] + candies[i]
        if total_candies > x:
            diff = total_candies - x
            operations += diff
            candies[i] = max(0, candies[i] - diff)
    return operations

# Read input
N, x = map(int, input().split())
candies = list(map(int, input().split()))

# Call the function and print the result
result = min_operations_to_satisfy_constraints(N, x, candies)
print(result)
```
