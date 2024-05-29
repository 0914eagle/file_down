
def min_operations_to_equal_numbers(n, k, a):
    min_val = min(a)
    max_val = max(a)

    min_operations = float('inf')

    for target in range(min_val, max_val+1):
        operations = 0
        for num in a:
            diff = num - target
            operations += diff // 2 + diff % 2
        if operations <= min_operations:
            count = sum([1 for num in a if num == target])
            if count >= k:
                min_operations = operations

    return min_operations

# Input parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

result = min_operations_to_equal_numbers(n, k, a)
print(result)
```
