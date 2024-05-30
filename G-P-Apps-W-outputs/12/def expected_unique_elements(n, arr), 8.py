
def expected_unique_elements(n, arr):
    total_unique = len(set(arr))
    expected = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            expected += total_unique * (j - i + 1) / n
    return expected

n = int(input())
arr = list(map(int, input().split()))

result = expected_unique_elements(n, arr)
print('{:.6f}'.format(result))
```
