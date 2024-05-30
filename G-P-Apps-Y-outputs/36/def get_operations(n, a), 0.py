
def get_operations(n, a):
    operations = []
    count = 0
    for i in range(1, n):
        if a[i] != a[i-1]:
            diff = abs(a[i] - a[i-1])
            if a[i] > a[i-1]:
                operations.append((1, i, i-1))
                a[i-1] += diff
                count += 1
            else:
                operations.append((2, i, i-1))
                a[i-1] -= diff
                count += 1
    return count, operations

# Input
n = int(input())
a = list(map(int, input().split()))

# Solve
min_operations, operations = get_operations(n, a)

# Output
print(min_operations)
for op in operations:
    print(' '.join(map(str, op)))
```
