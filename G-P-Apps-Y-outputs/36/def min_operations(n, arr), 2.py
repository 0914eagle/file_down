
def min_operations(n, arr):
    ops = []
    min_ops = 0
    
    while len(set(arr)) > 1:
        max_diff = -1
        max_diff_idx = -1
        
        for i in range(n - 1):
            diff = abs(arr[i] - arr[i + 1])
            if diff > max_diff:
                max_diff = diff
                max_diff_idx = i
        
        if arr[max_diff_idx] > arr[max_diff_idx + 1]:
            ops.append((1, max_diff_idx + 1, max_diff_idx + 2))
            arr[max_diff_idx] -= max_diff
        else:
            ops.append((2, max_diff_idx + 1, max_diff_idx + 2))
            arr[max_diff_idx] += max_diff
            
        min_ops += 1
        
    return min_ops, ops

# Example input
n = 5
arr = [2, 4, 6, 6, 6]

min_ops, ops = min_operations(n, arr)
print(min_ops)
for op in ops:
    print(*op)
```
