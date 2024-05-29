
def min_operations(N, x, candies):
    operations = 0
    for i in range(1, N):
        if candies[i] + candies[i-1] > x:
            diff = candies[i] + candies[i-1] - x
            operations += diff
            candies[i] = max(candies[i] - diff, 0)
    return operations

input_data = input().split()
N, x = map(int, input_data[:2])
candies = list(map(int, input_data[2:]))

print(min_operations(N, x, candies))
```
