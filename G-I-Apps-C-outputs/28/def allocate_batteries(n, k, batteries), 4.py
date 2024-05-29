
def allocate_batteries(n, k, batteries):
    batteries.sort()
    left, right = 0, max(batteries)
    
    while left < right:
        mid = (left + right) // 2
        count = 0
        for i in range(0, 2*n*k, 2*k):
            count += batteries[i + k] - batteries[i] <= mid
        
        if count == n:
            right = mid
        else:
            left = mid + 1
    
    return left

# Read input
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Call the function and print the result
result = allocate_batteries(n, k, batteries)
print(result)
```
