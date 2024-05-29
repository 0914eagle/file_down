
def min_operations(n, k, a):
    min_val = min(a)
    max_val = max(a)
    operations = float('inf')

    for target in range(min_val, max_val + 1):
        total_operations = 0
        
        for num in a:
            diff = abs(num - target)
            total_operations += diff // 2

        if total_operations <= operations and a.count(target) >= k:
            operations = total_operations

    return operations

# Input parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

print(min_operations(n, k, a))
```
