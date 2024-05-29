
def min_operations(N, x, candies):
    operations = 0
    for i in range(1, N):
        total_candies = candies[i-1] + candies[i]
        if total_candies > x:
            diff = total_candies - x
            candies[i] = max(candies[i] - diff, 0)
            operations += diff
    return operations

# Reading input from Standard Input
N, x = map(int, input().split())
a = list(map(int, input().split()))

# Calling the function with the input values
result = min_operations(N, x, a)
print(result)
```
