
def min_power_difference(n, k, batteries):
    batteries.sort()
    left, right = 0, len(batteries) - 1
    min_diff = float('inf')

    while left < right:
        diff = batteries[right] - batteries[left]
        if diff < min_diff:
            min_diff = diff

        if (right - left + 1) % 2 == 0:
            mid = (left + right) // 2
            diff1 = batteries[mid] - batteries[left]
            diff2 = batteries[right] - batteries[mid]
            if diff1 < diff2:
                right = mid
            else:
                left = mid + 1
        else:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            diff1 = batteries[mid1] - batteries[left]
            diff2 = batteries[right] - batteries[mid2]
            if diff1 < diff2:
                right = mid1
            else:
                left = mid2

    return min_diff

# Input
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Output
print(min_power_difference(n, k, batteries))
```
