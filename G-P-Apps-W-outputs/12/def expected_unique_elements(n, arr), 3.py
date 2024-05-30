
def expected_unique_elements(n, arr):
    total_unique = len(set(arr))
    expected = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            expected += len(set(arr[i-1:j])) / (n * (n + 1) / 2)
    return expected

n = int(input())
arr = list(map(int, input().split()))
result = expected_unique_elements(n, arr)
print("{:.6f}".format(result))
```
