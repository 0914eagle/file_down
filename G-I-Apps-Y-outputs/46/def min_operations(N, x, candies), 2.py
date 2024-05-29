
def min_operations(N, x, candies):
    operations = 0
    for i in range(1, N):
        total = candies[i-1] + candies[i]
        if total > x:
            diff = total - x
            if diff <= candies[i]:
                candies[i] -= diff
            else:
                candies[i-1] -= diff - candies[i]
                candies[i] = 0
            operations += diff
    return operations

# Read input
N, x = map(int, input().strip().split())
candies = list(map(int, input().strip().split()))

# Call the function and print the result
print(min_operations(N, x, candies))
```
