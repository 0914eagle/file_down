
def min_operations_to_equal_elements(n, a):
    ops = []
    for i in range(n-1):
        diff = abs(a[i] - a[i+1])
        if a[i] < a[i+1]:
            a[i] += diff
            ops.append((1, i+1, i+2))
        elif a[i] > a[i+1]:
            a[i] -= diff
            ops.append((2, i+1, i+2))
    return len(ops), ops

# Input
n = 5
a = [2, 4, 6, 6, 6]

# Output
k, operations = min_operations_to_equal_elements(n, a)
print(k)
for op in operations:
    print(*op)
```
