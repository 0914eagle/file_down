
def minimum_operations(n, a):
    operations = []
    min_ops = 0
    
    while max(a) != min(a):
        max_idx = a.index(max(a))
        min_idx = a.index(min(a))
        
        if max(a) - a[max_idx] < a[min_idx] - min(a):
            diff = min(a) - a[min_idx]
            a[min_idx] += diff
            operations.append((1, min_idx+1, min_idx+2))
        else:
            diff = a[max_idx] - max(a)
            a[max_idx] -= diff
            operations.append((2, max_idx+1, max_idx+2))
        
        min_ops += 1
    
    return min_ops, operations

# Input processing
n = int(input())
a = list(map(int, input().split()))

# Get the minimum operations and the order of operations
min_ops, operations = minimum_operations(n, a)

# Output
print(min_ops)
for op in operations:
    print(*op)
```
