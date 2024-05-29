
def min_operations_to_meet_objective(N, x, candies):
    operations = 0
    for i in range(N-1):
        total_candies = candies[i] + candies[i+1]
        if total_candies > x:
            diff = total_candies - x
            candies[i+1] = max(0, candies[i+1]-diff)
            operations += diff
    return operations

# Read input
N, x = map(int, input().split())
candies = list(map(int, input().split()))

# Call the function
result = min_operations_to_meet_objective(N, x, candies)
print(result)
```
