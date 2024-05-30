
def min_operations_to_equal_elements(n, arr):
    operations = []
    for i in range(n-1):
        while arr[i] != arr[i+1]:
            diff = abs(arr[i] - arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i] -= diff
                operations.append((2, i+1, i+2))
            else:
                arr[i] += diff
                operations.append((1, i+1, i+2))
    return len(operations), operations

# Example input
n = 5
arr = [2, 4, 6, 6, 6]
k, ops = min_operations_to_equal_elements(n, arr)
print(k)
for op in ops:
    print(*op)
```
