
def minimum_operations(n, a):
    operations = []
    for i in range(1, n):
        diff = abs(a[i] - a[i-1])
        if diff > 0:
            if a[i] > a[i-1]:
                operations.append((1, i, i+1))
                a[i] += diff
            else:
                operations.append((2, i, i+1))
                a[i] -= diff
    return operations

n = int(input())
a = list(map(int, input().split()))
result = minimum_operations(n, a)

print(len(result))
for op in result:
    print(*op)
```
