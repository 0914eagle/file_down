
def min_operations_to_equal_numbers(n, k, arr):
    min_val = min(arr)
    max_val = max(arr)
    
    operations = float('inf')
    
    for target in range(min_val, max_val+1):
        min_ops = 0
        for num in arr:
            diff = abs(num - target)
            min_ops += diff // target
        if min_ops <= k:
            operations = min(operations, sum(num % target for num in arr))
    
    return operations

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(min_operations_to_equal_numbers(n, k, arr))
```
