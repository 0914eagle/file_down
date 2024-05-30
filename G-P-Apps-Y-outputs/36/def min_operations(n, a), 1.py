
def min_operations(n, a):
    operations = []
    for i in range(n-1):
        diff = abs(a[i] - a[i+1])
        if a[i] != a[i+1]:
            if (a[i] + a[i+1]) % 2 == 0:
                target = (a[i] + a[i+1]) // 2
                if a[i] > target:
                    a[i] -= diff
                    operations.append((2, i+1, i+2))
                else:
                    a[i] += diff
                    operations.append((1, i+1, i+2))
            else:
                if a[i] < a[i+1]:
                    a[i] += diff
                    operations.append((1, i+1, i+2))
                else:
                    a[i] -= diff
                    operations.append((2, i+1, i+2))
    return len(operations), operations

n = int(input())
a = list(map(int, input().split()))
k, operations = min_operations(n, a)
print(k)
for op in operations:
    print(*op)
```
