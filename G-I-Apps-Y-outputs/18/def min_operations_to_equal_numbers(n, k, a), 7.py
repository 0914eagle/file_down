
def min_operations_to_equal_numbers(n, k, a):
    min_ops = float('inf')
    
    for num in set(a):
        freq = a.count(num)
        if freq >= k:
            min_ops = min(min_ops, 0)
        else:
            ops = 0
            count = freq
            while count < k:
                count *= 2
                ops += 1
            min_ops = min(min_ops, ops)
    
    return min_ops

# Input processing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(min_operations_to_equal_numbers(n, k, a))
```
