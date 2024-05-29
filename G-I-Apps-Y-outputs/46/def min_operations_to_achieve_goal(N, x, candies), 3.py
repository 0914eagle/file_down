
def min_operations_to_achieve_goal(N, x, candies):
    operations = 0
    for i in range(1, N):
        total_candies = candies[i] + candies[i-1]
        if total_candies > x:
            excess_candies = total_candies - x
            operations += excess_candies
            candies[i] -= excess_candies
    
    return operations

# Read input
N, x = map(int, input().split())
candies = list(map(int, input().split()))

# Call the function and print the result
print(min_operations_to_achieve_goal(N, x, candies))
```
