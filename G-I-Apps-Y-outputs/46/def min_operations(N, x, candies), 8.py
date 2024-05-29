
def min_operations(N, x, candies):
    operations = 0
    for i in range(1, N):
        if candies[i] + candies[i-1] > x:
            diff = candies[i] + candies[i-1] - x
            if candies[i] >= diff:
                candies[i] -= diff
            else:
                candies[i-1] -= diff - candies[i]
                candies[i] = 0
            operations += diff
    return operations

# Read input
N, x = map(int, input().split())
candies = list(map(int, input().split()))

# Print minimum operations
print(min_operations(N, x, candies))
```
