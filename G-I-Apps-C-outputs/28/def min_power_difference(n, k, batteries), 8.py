
def min_power_difference(n, k, batteries):
    batteries.sort()
    diff = float('inf')
    for i in range(0, len(batteries), 2*k):
        current_diff = batteries[i+k-1] - batteries[i]
        diff = min(diff, current_diff)
    return diff

# Reading input
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Calling the function and printing the result
print(min_power_difference(n, k, batteries))
```
