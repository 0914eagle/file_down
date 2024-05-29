
def min_power_difference(n, k, batteries):
    batteries.sort()
    left, right = 1, max(batteries) - min(batteries)

    while left < right:
        mid = (left + right) // 2

        count = 0
        for i in range(0, len(batteries), 2*k):
            for j in range(k):
                if batteries[i+j+k] - batteries[i+j] <= mid:
                    continue
                else:
                    count += batteries[i+j+k] - batteries[i+j] - mid

        if count <= n*k:
            right = mid
        else:
            left = mid + 1
    
    return left

# Input
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Output
print(min_power_difference(n, k, batteries))
```
