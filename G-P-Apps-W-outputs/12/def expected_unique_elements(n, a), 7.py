
def expected_unique_elements(n, a):
    total_unique = len(set(a))
    expected = 0
    for i in range(n):
        for j in range(i, n):
            expected += len(set(a[i:j+1])) / (n * (n + 1) / 2)
    return expected

n = int(input())
a = list(map(int, input().split()))

result = expected_unique_elements(n, a)
print("{:.6f}".format(result))
```
